"""Verify the pinned Cargo input capsule and restore into new independent folders.

Python 3.11+ only. Does not execute downloaded code or acquire packages.
The separately tracked capsule SHA anchors integrity, not third-party authorship.
"""
import argparse
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import tarfile
import tomllib
import zipfile


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def safe_path(name):
    path = PurePosixPath(name)
    reserved = {"CON", "PRN", "AUX", "NUL"} | {f"{s}{n}" for s in ("COM", "LPT") for n in range(1, 10)}
    if (not name or name == '.' or str(path) != name or path.is_absolute() or "\\" in name or ":" in name
            or any(p in (".", "..") or p.rstrip(" .") != p or p.split(".")[0].upper() in reserved for p in path.parts)):
        raise ValueError("Unsafe input path: " + name)


def verify(raw, expected_sha, lock):
    if digest(raw) != expected_sha:
        raise ValueError("Input capsule SHA mismatch")
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        names = archive.namelist()
        if len(names) > 10000 or sum(x.file_size for x in archive.infolist()) > 128 * 1024 * 1024:
            raise ValueError("Input capsule resource limit")
        for name in names:
            safe_path(name)
        if len(set(x.casefold() for x in names)) != len(names):
            raise ValueError("Duplicate or case-colliding input path")
        if any(x.external_attr >> 16 & 0o170000 == 0o120000 for x in archive.infolist()):
            raise ValueError("Input capsule symlink")
        data = {name: archive.read(name) for name in names}
        modes = {p.filename: p.external_attr >> 16 for p in archive.infolist()}
    manifest = json.loads(data["INPUT-MANIFEST.json"])
    if manifest['schema'] != 'ceres.cargo-inputs.v1':
        raise ValueError('Unknown capsule schema')
    rows = manifest['files']
    if len({r['path'] for r in rows}) != len(rows) or set(data) != {r['path'] for r in rows} | {'INPUT-MANIFEST.json'}:
        raise ValueError('Input file inventory mismatch')
    for row in rows:
        value = data[row['path']]
        if len(value) != row['bytes'] or digest(value) != row['sha256']:
            raise ValueError('Input file hash mismatch: ' + row['path'])
    # Git stores canonical LF; ordinary Windows checkouts can contain CRLF.
    canonical_lock = lock.replace(b'\r\n', b'\n')
    if digest(canonical_lock) != manifest['lock_sha256']:
        raise ValueError('Cargo.lock differs from captured lock')
    if hashlib.sha1(b'blob ' + str(len(canonical_lock)).encode() + b'\0' + canonical_lock).hexdigest() != manifest['lock_git_blob']:
        raise ValueError('Cargo.lock Git blob differs')
    packages = {(p['name'], p['version'], p['source']): p for p in tomllib.loads(lock.decode())['package'] if p.get('source')}
    expected = {(p['name'], p['version'], p['source']) for p in manifest['registry']}
    for repo in manifest['git_sources']:
        for package in repo['packages']:
            expected.add((package['name'], package['version'], package['source']))
        for row in repo['files']:
            value = data['original-git/' + repo['commit'] + '/' + row['path']]
            blob = hashlib.sha1(b'blob ' + str(len(value)).encode() + b'\0' + value).hexdigest()
            if (blob != row['git_blob'] or digest(value) != row['sha256'] or row['mode'] not in ['100644', '100755']
                    or modes['original-git/' + repo['commit'] + '/' + row['path']] != int(row['mode'], 8)):
                raise ValueError('Original Git blob mismatch')
    if set(packages) != expected:
        raise ValueError('Locked dependency closure differs from capsule')
    for package in manifest['registry']:
        name = package['name']; version = package['version']; checksum = package['checksum']
        if packages[(name, version, package['source'])]['checksum'] != checksum or digest(data[package['archive']]) != checksum:
            raise ValueError('Original registry archive checksum mismatch')
        members = {}
        with tarfile.open(fileobj=io.BytesIO(data[package['archive']]), mode='r:gz') as archive:
            for member in archive.getmembers():
                if member.isdir():
                    continue
                if not member.isfile() or not member.name.startswith(f'{name}-{version}/'):
                    raise ValueError('Unsafe registry archive member')
                relative = member.name[len(f'{name}-{version}/'):]; safe_path(relative)
                if relative in members:
                    raise ValueError('Duplicate registry archive member')
                value = archive.extractfile(member).read(); members[relative] = digest(value)
                if data[f'vendor/{name}-{version}/{relative}'] != value:
                    raise ValueError('Vendor differs from original registry member')
        if members != package['files']:
            raise ValueError('Original registry member inventory mismatch')
    for package in [*manifest['registry'], *(p for r in manifest['git_sources'] for p in r['packages'])]:
        prefix = f"vendor/{package['name']}-{package['version']}/"
        checks = json.loads(data[prefix + '.cargo-checksum.json'])
        files = {n[len(prefix):]: v for n, v in data.items() if n.startswith(prefix) and n != prefix + '.cargo-checksum.json'}
        if set(files) != set(checks['files']) or any(digest(value) != checks['files'][name] for name, value in files.items()):
            raise ValueError('Cargo vendor checksums differ')
        if checks['package'] != package.get('checksum'):
            raise ValueError('Cargo package checksum differs')
        if package['source'].startswith('git+'):
            repo = next(r for r in manifest['git_sources'] if package in r['packages'])
            original_prefix = str(PurePosixPath(package['manifest']).parent)
            original_prefix = '' if original_prefix == '.' else original_prefix + '/'
            for name, value in files.items():
                if name != 'Cargo.toml' and value != data['original-git/' + repo['commit'] + '/' + original_prefix + name]:
                    raise ValueError('Vendored Git file differs from pinned original')
            if digest(files['Cargo.toml']) != package['normalized_manifest_sha256']:
                raise ValueError('Cargo normalized Git manifest differs')
    return manifest, data


def restore(data, inputs, cargo_home):
    # Inspect lexical parents before resolve() follows links; 8.3 aliases are
    # ordinary filesystem names and remain valid canonicalized destinations.
    for destination in [inputs, cargo_home]:
        lexical = Path(os.path.abspath(destination))
        for part in [lexical, *lexical.parents]:
            if part.exists() or part.is_symlink():
                if part.is_symlink() or getattr(part.lstat(), 'st_file_attributes', 0) & 0x400:
                    raise ValueError('Destination parent is a link or junction')
    inputs = inputs.resolve(); cargo_home = cargo_home.resolve()
    repo = Path(__file__).resolve().parents[1]
    for dest in [inputs, cargo_home]:
        if dest.exists() or repo in [dest, *dest.parents]:
            raise ValueError('Use new folders outside this source repository')
        if os.environ.get('CARGO_TARGET_DIR'):
            target = Path(os.environ['CARGO_TARGET_DIR']).resolve()
            if target in [dest, *dest.parents] or dest in target.parents:
                raise ValueError('Keep inputs outside compiled target')
    if inputs in cargo_home.parents or cargo_home in inputs.parents or inputs == cargo_home:
        raise ValueError('Input and Cargo home folders must be separate')
    # Verify all destination parents before creating or writing anything.
    for dest in [inputs, cargo_home]:
        for parent in dest.parents:
            if parent.is_symlink() or (hasattr(parent, 'is_junction') and parent.is_junction()):
                raise ValueError('Destination parent is a link or junction')
    inputs.mkdir(parents=True); cargo_home.mkdir(parents=True)
    for name, value in data.items():
        if name.startswith('vendor/'):
            path = inputs / name; path.parent.mkdir(parents=True, exist_ok=True); path.write_bytes(value)
    config = data['CARGO-CONFIG.toml'].decode().replace('directory = "vendor"', 'directory = ' + json.dumps((inputs / 'vendor').as_posix()))
    (cargo_home / 'config.toml').write_text(config + '\n[net]\noffline = true\n', encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--capsule', type=Path, default=Path(__file__).resolve().parents[1] / 'cargo-inputs/inputs.zip')
    parser.add_argument('--sha256', required=True, help='Expected digest from the trusted checkout or release receipt')
    parser.add_argument('--lock', type=Path, default=Path(__file__).resolve().parents[1] / 'Cargo.lock')
    parser.add_argument('--inputs', type=Path)
    parser.add_argument('--cargo-home', type=Path)
    args = parser.parse_args()
    manifest, data = verify(args.capsule.read_bytes(), args.sha256, args.lock.read_bytes())
    if bool(args.inputs) != bool(args.cargo_home):
        parser.error('Supply both --inputs and --cargo-home for restoration')
    if args.inputs:
        restore(data, args.inputs, args.cargo_home)
    print(json.dumps(dict(verified=True, packages=32, files=len(manifest['files']), restored=bool(args.inputs))))


if __name__ == '__main__':
    main()
