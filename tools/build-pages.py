"""Build CERES's bounded browser workbench from its native Rust core."""
import argparse
import json
import platform
import subprocess
from pathlib import Path
from source_custody import (source_data, source_zip, verify_source, new_destination,
                            encoded, digest, verify_site, RUNTIME_BUDGET, DOWNLOAD_BUDGET)

ROOT = Path(__file__).resolve().parents[1]


def run(*args):
    subprocess.run(args, cwd=ROOT, check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("dist/CERES"))
    parser.add_argument("--expected-source-head", help="Required outside Git; otherwise uses the clean checkout HEAD")
    args = parser.parse_args()
    output = new_destination(args.output, ROOT)
    if output == ROOT / "dist" or ROOT / "dist" not in output.parents:
        raise ValueError("Output must be a directory inside dist")
    head = args.expected_source_head
    if head is None:
        head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    source, modes = source_data(ROOT, head)
    archive = source_zip(source, modes)
    source_manifest, _, _ = verify_source(archive, head)
    version = subprocess.check_output(["wasm-bindgen", "--version"], text=True).strip()
    if version != "wasm-bindgen 0.2.127":
        raise ValueError(f"Expected wasm-bindgen 0.2.127, found {version}")
    run("cargo", "build", "--locked", "--release", "--target", "wasm32-unknown-unknown", "-p", "ceres-web", "--lib", "--features", "wasm")
    metadata = json.loads(subprocess.check_output(["cargo", "metadata", "--locked", "--offline", "--no-deps", "--format-version", "1"], cwd=ROOT))
    wasm = Path(metadata["target_directory"]) / "wasm32-unknown-unknown/release/ceres_web.wasm"
    output.mkdir(parents=True)
    run("wasm-bindgen", str(wasm), "--target", "web", "--out-dir", str(output / "pkg"))
    for name in ("index.html", "style.css", "app.js", "worker.js"):
        (output / name).write_bytes(source['web/' + name].replace(b'__SOURCE_COMMIT__', head.encode()))
    for original, target in [('LICENSE', 'LICENSE'), ('DEPENDENCY-NOTICES.txt', 'DEPENDENCY-NOTICES.txt'),
                             ('notices/rust-1.95.0-COPYRIGHT-library.html', 'RUST-RUNTIME-NOTICES.html')]:
        (output / target).write_bytes(source[original])
    (output / ".nojekyll").touch()
    downloads = output / 'downloads'; downloads.mkdir()
    (downloads / 'ceres-source.zip').write_bytes(archive)
    (downloads / 'SOURCE-MANIFEST.json').write_bytes(source['SOURCE-MANIFEST.json'])
    files = [dict(path=p.relative_to(output).as_posix(), bytes=p.stat().st_size, sha256=digest(p.read_bytes()))
             for p in sorted(output.rglob('*')) if p.is_file()]
    module = next(p for p in files if p['path'] == 'pkg/ceres_web_bg.wasm')
    manifest = dict(schema='ceres.site.v1', source_commit=head, source=dict(path='downloads/ceres-source.zip',
                    sha256=digest(archive), bytes=len(archive), git_blobs=len(source_manifest['git_files'])), wasm=module,
                    files=files, sizes={}, budgets=dict(runtime=RUNTIME_BUDGET, downloads=DOWNLOAD_BUDGET,
                    total=RUNTIME_BUDGET + DOWNLOAD_BUDGET), tools=dict(rustc=subprocess.check_output(['rustc', '-Vv'], text=True),
                    wasm_bindgen=version, python=platform.python_version()),
                    scope='Artifact/source integrity, not author, draft economics or historical certification. Toolchains not bundled.')
    runtime = sum(p['bytes'] for p in files if not p['path'].startswith('downloads/'))
    optional = sum(p['bytes'] for p in files if p['path'].startswith('downloads/'))
    # The manifest accounts for its own byte length; converge the decimal lengths.
    for _ in range(10):
        size = len(encoded(manifest))
        sizes = dict(runtime=runtime + size, downloads=optional, total=runtime + size + optional)
        if manifest['sizes'] == sizes:
            break
        manifest['sizes'] = sizes
    else:
        raise ValueError('Manifest size accounting did not converge')
    raw = encoded(manifest); (output / 'BUILD-MANIFEST.json').write_bytes(raw)
    verify_site(output, digest(raw))
    print(json.dumps(dict(output=str(output), source_commit=head, sizes=manifest['sizes'],
                          source_sha256=digest(archive), manifest_sha256=digest(raw))))


if __name__ == "__main__":
    main()
