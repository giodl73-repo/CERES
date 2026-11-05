"""Rebuild a verified complete site source kit outside Git, without Cargo acquisition.

Installed compiler/linker/target, wasm-bindgen, Node/npm modules and browser are
prerequisites. Compiled target reuse is explicit; dependency inputs/Cargo home
are independent. A successful replay is software proof, not draft validation.
"""
import argparse
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import time
import urllib.request

from source_custody import digest, encoded, git_id, new_destination, restore_source, verify_site

ROOT = Path(__file__).resolve().parents[1]
ORIGINAL = 'context/waves/2026-11-05-reader-delivery/validation/original-cli-controls.json'


def verify_contract(data):
    contract = json.loads(data['tests/fixtures/native-contract.json'])
    for row in contract['files']:
        value = data[row['path']]
        if digest(value) != row['sha256'] or git_id('blob', value) != row['git_blob']:
            raise ValueError('Original native contract changed: ' + row['path'])
        if (ROOT / row['path']).read_bytes().replace(b'\r\n', b'\n') != value:
            raise ValueError('Working native inputs differ from pinned source: ' + row['path'])
    return contract


def cli_controls(binary, source, output, original, env):
    output.mkdir(); rows = []
    for row in original['rows']:
        args = list(row['argv'])
        for i, flag in enumerate(args[:-1]):
            if flag in ['--packet', '--jsonl']:
                args[i + 1] = str(output / Path(args[i + 1].replace('\\', '/')).name)
        p = subprocess.run([str(binary), *args], cwd=source, env=env, capture_output=True, timeout=30)
        rows.append(dict(argv=args, exit_code=p.returncode, stdout=p.stdout.decode('utf-8'), stderr=p.stderr.decode('utf-8')))
    files = {p.name: p.read_bytes() for p in output.iterdir()}
    return rows, files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site', type=Path, required=True)
    parser.add_argument('--manifest-sha256', required=True)
    parser.add_argument('--scratch', type=Path, required=True)
    parser.add_argument('--port', type=int, default=8198)
    args = parser.parse_args()
    if not 1024 <= args.port <= 65535:
        raise ValueError('Use a nonprivileged local port')
    site, source_manifest, data, modes = verify_site(args.site, args.manifest_sha256)
    contract = verify_contract(data)
    scratch = new_destination(args.scratch, ROOT)
    if ROOT in scratch.parents:
        raise ValueError('Independent scratch must be outside source repository')
    scratch.mkdir(parents=True)
    env = os.environ.copy()
    for name in ['GH_TOKEN', 'GITHUB_TOKEN', 'GH_DEBUG']:
        env.pop(name, None)
    env.update(CARGO_NET_OFFLINE='true', CARGO_INCREMENTAL='0', RUSTUP_TOOLCHAIN='1.95.0')
    commands = []

    def observe(name, command, cwd=ROOT):
        p = subprocess.run(command, cwd=cwd, env=env, capture_output=True)
        (scratch / (name + '.stdout')).write_bytes(p.stdout); (scratch / (name + '.stderr')).write_bytes(p.stderr)
        commands.append(dict(name=name, command=command, exit=p.returncode))
        (scratch / 'commands.json').write_bytes(encoded(commands))
        print(f'{name}: exit {p.returncode}', flush=True)
        if p.returncode:
            raise RuntimeError(f'{name} failed; retained stdout/stderr in {scratch}')
        return p

    metadata = json.loads(observe('checkout-metadata', ['cargo', '+1.95.0', 'metadata', '--locked', '--offline', '--no-deps', '--format-version', '1']).stdout)
    target = Path(metadata['target_directory']).resolve(); env['CARGO_TARGET_DIR'] = str(target)
    suffix = '.exe' if os.name == 'nt' else ''
    observe('checkout-cli-build', ['cargo', '+1.95.0', 'build', '-p', 'ceres', '--bin', 'ceres', '--locked', '--offline'])
    checkout_binary = scratch / ('checkout-ceres' + suffix); shutil.copy2(target / ('debug/ceres' + suffix), checkout_binary)
    original = json.loads(data[ORIGINAL])
    before, before_files = cli_controls(checkout_binary, ROOT, scratch / 'checkout-generated', original, env)
    (scratch / 'checkout-cli.json').write_bytes(encoded(before))
    source = restore_source(data, modes, scratch / 'source')
    capsule_sha = (source / 'cargo-inputs/sha256.txt').read_text().split()[0]
    observe('archive-inputs', [sys.executable, 'tools/input-custody.py', '--sha256', capsule_sha,
                              '--inputs', str(scratch / 'inputs'), '--cargo-home', str(scratch / 'cargo-home')], source)
    env['CARGO_HOME'] = str(scratch / 'cargo-home')
    archive_metadata = json.loads(observe('archive-metadata', ['cargo', '+1.95.0', 'metadata', '--all-features', '--locked', '--offline', '--format-version', '1'], source).stdout)
    packages = [p for p in archive_metadata['packages'] if p.get('source')]
    if len(packages) != 32 or any(not Path(p['manifest_path']).is_relative_to(scratch / 'inputs/vendor') for p in packages):
        raise ValueError('Archive dependencies did not resolve from independent inputs')
    for name, command in [
        ('archive-input-checks', [sys.executable, 'tests/input_custody.py']),
        ('archive-tests', ['cargo', '+1.95.0', 'test', '--workspace', '--all-targets', '--locked', '--offline']),
        ('archive-format', ['cargo', '+1.95.0', 'fmt', '--all', '--check']),
        ('archive-clippy', ['cargo', '+1.95.0', 'clippy', '--workspace', '--all-targets', '--all-features', '--no-deps', '--locked', '--offline', '--', '-D', 'warnings']),
        ('archive-native', ['cargo', '+1.95.0', 'build', '-p', 'ceres', '--bin', 'ceres', '--locked', '--offline']),
        ('archive-control', ['cargo', '+1.95.0', 'build', '-p', 'ceres-web', '--example', 'reader-control', '--locked', '--offline'])]:
        observe(name, command, source)
    archive_binary = scratch / ('archive-ceres' + suffix); shutil.copy2(target / ('debug/ceres' + suffix), archive_binary)
    after, after_files = cli_controls(archive_binary, source, scratch / 'archive-generated', original, env)
    (scratch / 'archive-cli.json').write_bytes(encoded(after))
    if len(before) != 30 or any(any(a[k] != b[k] for k in ['exit_code', 'stdout', 'stderr']) for a, b in zip(before, after)) or before_files != after_files or len(after_files) != 3:
        raise ValueError('Original CLI behavior differs between checkout and archive')
    archive_site = source / 'dist/qualification/CERES'
    observe('archive-site', [sys.executable, 'tools/build-pages.py', '--expected-source-head', source_manifest['source_commit'], '--output', str(archive_site)], source)
    archive_identity = json.loads((archive_site / 'BUILD-MANIFEST.json').read_bytes())
    if (args.site / site['source']['path']).read_bytes() != (archive_site / site['source']['path']).read_bytes():
        raise ValueError('Complete source ZIP differs across checkout/archive')
    observe('archive-parity', [sys.executable, 'tools/check-reader.py', '--site', str(archive_site), '--output', str(scratch / 'archive-parity.json')], source)
    env['CERES_TEST_SITE'] = str(archive_site)
    observe('archive-receivers', [sys.executable, 'tests/source_custody.py'], source)
    # Reuse installed, pinned test tools; no npm/browser acquisition in replay.
    shutil.copytree(ROOT / 'node_modules', source / 'node_modules', symlinks=True)
    driver = json.loads((source / 'node_modules/@playwright/test/package.json').read_bytes())['version']
    lock = json.loads(data['package-lock.json'])['packages']['node_modules/@playwright/test']['version']
    if driver != lock or driver != '1.58.2':
        raise ValueError('Installed browser driver differs from pinned prerequisites')
    config = scratch / 'archive-browser.config.mjs'
    config.write_text('import {defineConfig} from ' + json.dumps((source / 'node_modules/@playwright/test/index.mjs').as_uri()) + ';\nexport default defineConfig(' + json.dumps(dict(
        testDir=(source / 'tests/browser').as_posix(), timeout=60000, workers=1, retries=0,
        outputDir=(scratch / 'archive-browser-results').as_posix(), reporter=[['json', dict(outputFile=(scratch / 'archive-browser-report.json').as_posix())]],
        use=dict(baseURL=f'http://127.0.0.1:{args.port}', browserName='chromium'))) + ');\n', encoding='utf-8')
    with (scratch / 'server.stdout').open('wb') as stdout, (scratch / 'server.stderr').open('wb') as stderr:
        server = subprocess.Popen([sys.executable, '-m', 'http.server', str(args.port), '--bind', '127.0.0.1', '--directory', str(archive_site.parent)],
                                  stdout=stdout, stderr=stderr, creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)
        try:
            for _ in range(100):
                if server.poll() is not None:
                    raise RuntimeError('Owned archive HTTP server exited')
                try:
                    with urllib.request.urlopen(f'http://127.0.0.1:{args.port}/CERES/BUILD-MANIFEST.json', timeout=1) as response:
                        if digest(response.read()) == digest((archive_site / 'BUILD-MANIFEST.json').read_bytes()):
                            break
                except OSError:
                    pass
                time.sleep(0.1)
            else:
                raise RuntimeError('Owned archive HTTP server not ready')
            observe('archive-browser', ['node', str(source / 'node_modules/playwright/cli.js'), 'test', '--config', str(config)], source)
        finally:
            server.terminate()
            try:
                server.wait(timeout=10)
            except subprocess.TimeoutExpired:
                server.kill(); server.wait()
    stats = json.loads((scratch / 'archive-browser-report.json').read_bytes())['stats']
    if stats['expected'] != 43 or any(stats[k] for k in ['unexpected', 'skipped', 'flaky']):
        raise ValueError('Archive browser suite incomplete')
    if (scratch / 'cargo-home/registry').exists() or (scratch / 'cargo-home/git').exists():
        raise ValueError('Unexpected dependency acquisition/cache in new Cargo home')
    parity = json.loads((scratch / 'archive-parity.json').read_bytes())
    receipt = dict(schema='ceres.source-replay.v1', platform=platform.platform(), source_commit=source_manifest['source_commit'],
                   source_files=len(source_manifest['git_files']), original_native_contract=contract['original_runtime_head'],
                   source_zip_sha256=site['source']['sha256'], source_zip_exact=True, site_manifest_sha256=args.manifest_sha256,
                   original_cli_controls=30, all_cli_outputs_exits_exact=True, generated_files=[dict(path=n, bytes=len(v), sha256=digest(v)) for n, v in sorted(after_files.items())],
                   independent_input_packages=32, new_cargo_home=True, acquisition_offline=True, shared_compiled_target_reused=str(target),
                   installed_toolchains_and_npm_browser_reused=True, input_custody_checks=11, native_tests=7, source_receiver_checks=18, typed_native_wasm_controls=parity['controls'],
                   typed_all_exact=parity['all_exact'], checkout_wasm=site['wasm'], archive_wasm=archive_identity['wasm'],
                   module_byte_identity=site['wasm']['sha256'] == archive_identity['wasm']['sha256'], browser_stats=stats, commands=commands,
                   scope='Checkout versus receiver-restored outside-Git source, independent Cargo inputs, actual native/WASM and archive browser replay. Not economics/catalog promotion or live release.')
    if not receipt['typed_all_exact'] or receipt['typed_native_wasm_controls'] != 135:
        raise ValueError('Typed native/WASM parity incomplete')
    (scratch / 'receipt.json').write_bytes(encoded(receipt)); print(json.dumps(dict(receipt=str(scratch / 'receipt.json'), source_commit=source_manifest['source_commit'], browser_cases=43)), flush=True)


if __name__ == '__main__':
    main()
