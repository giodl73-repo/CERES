"""Exact Git source packaging and read-only source/site receiver verification."""
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import zipfile

SPEC = importlib.util.spec_from_file_location('input_custody', Path(__file__).with_name('input-custody.py'))
INPUTS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(INPUTS)
digest = INPUTS.digest
safe_path = INPUTS.safe_path
SOURCE_MANIFEST = 'SOURCE-MANIFEST.json'
BUILD_MANIFEST = 'BUILD-MANIFEST.json'
RUNTIME_BUDGET = 5_000_000
DOWNLOAD_BUDGET = 12_000_000


def encoded(value):
    return (json.dumps(value, indent=2, ensure_ascii=False) + '\n').encode('utf-8')


def git_id(kind, raw):
    return hashlib.sha1(kind.encode() + b' ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()


def validate_paths(names):
    for name in names:
        safe_path(name)
    if len({name.casefold() for name in names}) != len(names):
        raise ValueError('Duplicate or case-colliding paths')
    paths = {name.casefold() for name in names}
    if any(str(parent).casefold() in paths for name in names for parent in PurePosixPath(name).parents if str(parent) != '.'):
        raise ValueError('File/directory path collision')


def git_tree(rows):
    tree = {}
    validate_paths([row['path'] for row in rows])
    for row in rows:
        if row['mode'] not in ['100644', '100755'] or not re.fullmatch('[a-f0-9]{40}', row['git_blob']):
            raise ValueError('Unsupported Git mode/blob')
        parent = tree
        parts = PurePosixPath(row['path']).parts
        for part in parts[:-1]:
            parent = parent.setdefault(part, {})
        parent[parts[-1]] = (row['mode'], row['git_blob'])

    def hash_tree(node):
        result = bytearray()
        for name, value in sorted(node.items(), key=lambda item: item[0].encode('utf-8') + (b'' if isinstance(item[1], tuple) else b'/')):
            is_file = isinstance(value, tuple)
            mode = value[0] if is_file else '40000'
            blob = value[1] if is_file else hash_tree(value)
            result.extend(mode.encode() + b' ' + name.encode('utf-8') + b'\0' + bytes.fromhex(blob))
        return git_id('tree', bytes(result))
    return hash_tree(tree)


def read_zip(raw):
    if len(raw) > DOWNLOAD_BUDGET:
        raise ValueError('Source ZIP exceeds download budget')
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        entries = archive.infolist()
        validate_paths([entry.filename for entry in entries])
        if len(entries) > 10000 or sum(entry.file_size for entry in entries) > 128 * 1024 * 1024:
            raise ValueError('Source resource limit')
        if any(entry.external_attr >> 16 not in [0o100644, 0o100755] for entry in entries):
            raise ValueError('Source modes must be explicit regular Git file modes')
        return {p.filename: archive.read(p) for p in entries}, {p.filename: p.external_attr >> 16 for p in entries}


def verify_source_data(data, modes, expected_head):
    manifest = json.loads(data[SOURCE_MANIFEST])
    if manifest['schema'] != 'ceres.source.v1' or manifest['source_commit'] != expected_head or not re.fullmatch('[a-f0-9]{40}', expected_head):
        raise ValueError('Source commit mismatch')
    commit = bytes.fromhex(manifest['commit_object_hex'])
    if git_id('commit', commit) != expected_head:
        raise ValueError('Original commit object mismatch')
    rows = manifest['git_files']
    if modes[SOURCE_MANIFEST] != 0o100644:
        raise ValueError('Source manifest mode mismatch')
    if set(data) != {row['path'] for row in rows} | {SOURCE_MANIFEST} or any(row['path'] == SOURCE_MANIFEST for row in rows):
        raise ValueError('Source inventory mismatch')
    if commit.split(b'\n', 1)[0] != b'tree ' + git_tree(rows).encode():
        raise ValueError('Complete original Git tree mismatch')
    for row in rows:
        value = data[row['path']]
        if (len(value) != row['bytes'] or digest(value) != row['sha256'] or git_id('blob', value) != row['git_blob']
                or modes[row['path']] != int(row['mode'], 8)):
            raise ValueError('Original source blob/mode mismatch: ' + row['path'])
    capsule_sha = data['cargo-inputs/sha256.txt'].decode().split()[0]
    inputs, input_data = INPUTS.verify(data['cargo-inputs/inputs.zip'], capsule_sha, data['Cargo.lock'])
    if json.loads(data['cargo-inputs/manifest.json']) != inputs or data['DEPENDENCY-NOTICES.txt'] != input_data['DEPENDENCY-NOTICES.txt']:
        raise ValueError('Input manifest/notices differ from source')
    return manifest


def verify_source(raw, expected_head):
    data, modes = read_zip(raw)
    return verify_source_data(data, modes, expected_head), data, modes


def git_source(repo, head):
    if subprocess.check_output(['git', 'status', '--porcelain'], cwd=repo):
        raise ValueError('Commit source changes before export')
    actual = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=repo, text=True).strip()
    if actual != head:
        raise ValueError('Expected source head differs from checkout')
    rows = []
    for entry in subprocess.check_output(['git', 'ls-tree', '-rz', head], cwd=repo).split(b'\0'):
        if not entry:
            continue
        header, name = entry.split(b'\t', 1)
        mode, kind, blob = header.decode().split()
        if kind != 'blob':
            raise ValueError('Unbundled Gitlink or unsupported object')
        rows.append(dict(path=name.decode('utf-8'), mode=mode, git_blob=blob))
    # Read raw Git objects, bypassing checkout/export filters on every platform.
    raw = subprocess.check_output(['git', 'cat-file', '--batch'], input=''.join(r['git_blob'] + '\n' for r in rows).encode(), cwd=repo)
    stream = io.BytesIO(raw); data = {}
    for row in rows:
        blob, kind, size = stream.readline().decode().strip().split()
        value = stream.read(int(size))
        if blob != row['git_blob'] or kind != 'blob' or stream.read(1) != b'\n':
            raise ValueError('Git object transport mismatch')
        row.update(bytes=len(value), sha256=digest(value)); data[row['path']] = value
    if stream.read():
        raise ValueError('Unexpected Git object output')
    commit = subprocess.check_output(['git', 'cat-file', 'commit', head], cwd=repo)
    manifest = dict(schema='ceres.source.v1', source_commit=head, commit_object_hex=commit.hex(), git_files=rows,
                    scope='Complete original Git tree plus locked dependency capsule; original grants apply. Installed toolchains are not bundled. Integrity is not economic or author certification.')
    data[SOURCE_MANIFEST] = encoded(manifest)
    modes = {row['path']: int(row['mode'], 8) for row in rows}; modes[SOURCE_MANIFEST] = 0o100644
    verify_source_data(data, modes, head)
    return data, modes


def source_data(repo, expected_head):
    if (repo / '.git').exists():
        return git_source(repo, expected_head)
    manifest = json.loads((repo / SOURCE_MANIFEST).read_bytes())
    rows = manifest['git_files']
    validate_paths([r['path'] for r in rows])
    data = {r['path']: (repo / r['path']).read_bytes() for r in rows}
    data[SOURCE_MANIFEST] = (repo / SOURCE_MANIFEST).read_bytes()
    modes = {row['path']: int(row['mode'], 8) for row in rows}; modes[SOURCE_MANIFEST] = 0o100644
    verify_source_data(data, modes, expected_head)
    return data, modes


def source_zip(data, modes):
    result = io.BytesIO()
    with zipfile.ZipFile(result, 'w') as archive:
        for name, value in sorted(data.items()):
            item = zipfile.ZipInfo(name, (2026, 11, 5, 0, 0, 0)); item.create_system = 3
            item.compress_type = zipfile.ZIP_DEFLATED; item.external_attr = modes[name] << 16
            archive.writestr(item, value)
    return result.getvalue()


def package_source(repo, output, expected_head):
    output = new_destination(output, repo)
    if repo in output.parents and repo / 'dist' not in output.parents:
        raise ValueError('Use source output outside the repository or within dist')
    data, modes = source_data(repo, expected_head)
    raw = source_zip(data, modes)
    manifest, _, _ = verify_source(raw, expected_head)
    output.parent.mkdir(parents=True, exist_ok=True); output.write_bytes(raw)
    return dict(source_commit=expected_head, git_blobs=len(manifest['git_files']), bytes=len(raw), sha256=digest(raw))


def new_destination(path, repo=None):
    path = Path(os.path.abspath(path))
    for part in [path, *path.parents]:
        if part.exists() or part.is_symlink():
            attributes = getattr(part.lstat(), 'st_file_attributes', 0)
            if part.is_symlink() or attributes & 0x400:
                raise ValueError('Destination or parent is a link/junction')
    path = path.resolve()
    if path.exists():
        raise ValueError('Use a new destination; existing files are preserved')
    if repo and (path == repo or path in repo.parents):
        raise ValueError('Destination overlaps source root')
    if os.environ.get('CARGO_TARGET_DIR'):
        target = Path(os.environ['CARGO_TARGET_DIR']).resolve()
        if path in [target, *target.parents] or target in path.parents:
            raise ValueError('Destination overlaps compiled target')
    return path


def restore_source(data, modes, destination):
    destination = new_destination(destination, Path(__file__).resolve().parents[1])
    validate_paths(list(data))
    destination.mkdir(parents=True)
    for name, value in data.items():
        target = destination / name; target.parent.mkdir(parents=True, exist_ok=True); target.write_bytes(value)
        target.chmod(modes[name] & 0o777)
    return destination


def verify_site(root, expected_manifest_sha):
    root = Path(root).resolve(); raw = (root / BUILD_MANIFEST).read_bytes()
    if digest(raw) != expected_manifest_sha:
        raise ValueError('Build manifest SHA mismatch')
    manifest = json.loads(raw)
    if manifest['schema'] != 'ceres.site.v1':
        raise ValueError('Unknown build manifest')
    names = []
    for p in root.rglob('*'):
        if p.is_symlink() or getattr(p.lstat(), 'st_file_attributes', 0) & 0x400:
            raise ValueError('Site contains link/junction')
        if p.is_file():
            names.append(p.relative_to(root).as_posix())
    rows = manifest['files']; validate_paths([r['path'] for r in rows])
    if set(names) != {r['path'] for r in rows} | {BUILD_MANIFEST}:
        raise ValueError('Site inventory mismatch')
    for row in rows:
        data = (root / row['path']).read_bytes()
        if digest(data) != row['sha256'] or len(data) != row['bytes']:
            raise ValueError('Site file hash mismatch: ' + row['path'])
    module = (root / manifest['wasm']['path']).read_bytes()
    if digest(module) != manifest['wasm']['sha256'] or module[:8] != b'\0asm\x01\0\0\0':
        raise ValueError('WASM identity/header mismatch')
    source = (root / manifest['source']['path']).read_bytes()
    if digest(source) != manifest['source']['sha256']:
        raise ValueError('Source ZIP identity mismatch')
    source_manifest, data, modes = verify_source(source, manifest['source_commit'])
    for name in ['index.html', 'app.js', 'worker.js', 'style.css']:
        if (root / name).read_bytes() != data['web/' + name].replace(b'__SOURCE_COMMIT__', manifest['source_commit'].encode()):
            raise ValueError('Site UI differs from source: ' + name)
    if (root / 'LICENSE').read_bytes() != data['LICENSE']:
        raise ValueError('Site license differs from source')
    if (root / 'downloads/SOURCE-MANIFEST.json').read_bytes() != data[SOURCE_MANIFEST]:
        raise ValueError('Download source manifest mismatch')
    if (root / 'DEPENDENCY-NOTICES.txt').read_bytes() != data['DEPENDENCY-NOTICES.txt'] or (root / 'RUST-RUNTIME-NOTICES.html').read_bytes() != data['notices/rust-1.95.0-COPYRIGHT-library.html']:
        raise ValueError('Site/source notice identity mismatch')
    runtime = sum(r['bytes'] for r in rows if not r['path'].startswith('downloads/')) + len(raw)
    downloads = sum(r['bytes'] for r in rows if r['path'].startswith('downloads/'))
    if runtime >= RUNTIME_BUDGET or downloads >= DOWNLOAD_BUDGET or manifest['sizes'] != dict(runtime=runtime, downloads=downloads, total=runtime + downloads):
        raise ValueError('Site budget/size declaration mismatch')
    return manifest, source_manifest, data, modes
