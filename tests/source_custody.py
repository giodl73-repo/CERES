"""Receiver/corruption controls over a real complete built CERES artifact."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import source_custody as custody


class SourceChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.site = Path(os.environ.get('CERES_TEST_SITE', ROOT / 'dist/CERES')).resolve()
        cls.raw_manifest = (cls.site / 'BUILD-MANIFEST.json').read_bytes()
        cls.site_sha = custody.digest(cls.raw_manifest)
        cls.build, cls.source, cls.data, cls.modes = custody.verify_site(cls.site, cls.site_sha)
        cls.head = cls.build['source_commit']

    def altered_source(self, mutate):
        data = dict(self.data); modes = dict(self.modes)
        manifest = json.loads(data[custody.SOURCE_MANIFEST]); mutate(data, modes, manifest)
        data[custody.SOURCE_MANIFEST] = custody.encoded(manifest)
        return custody.source_zip(data, modes)

    def test_complete_git_source_and_modes(self):
        if (ROOT / '.git').exists():
            rows = subprocess.check_output(['git', 'ls-tree', '-rz', self.head], cwd=ROOT).split(b'\0')
            expected = {}
            for row in rows:
                if row:
                    header, path = row.split(b'\t', 1); mode, kind, blob = header.decode().split()
                    self.assertEqual(kind, 'blob'); expected[path.decode()] = (mode, blob)
            self.assertEqual(expected, {r['path']: (r['mode'], r['git_blob']) for r in self.source['git_files']})
        self.assertGreaterEqual(len(self.source['git_files']), 300)
        for path in ['src/main.rs', 'src/lib.rs', 'ceres-web/src/lib.rs', 'Cargo.lock', 'CLAUDE.md', 'docs/REBUILD.md', 'cargo-inputs/inputs.zip']:
            self.assertIn(path, self.data)

    def test_omitted_file_cannot_redefine_complete_tree(self):
        def omit(data, modes, manifest):
            del data['src/main.rs']; del modes['src/main.rs']
            manifest['git_files'] = [r for r in manifest['git_files'] if r['path'] != 'src/main.rs']
        with self.assertRaisesRegex(ValueError, 'Complete original Git tree mismatch'):
            custody.verify_source(self.altered_source(omit), self.head)

    def test_changed_original_source(self):
        def corrupt(data, modes, manifest): data['src/lib.rs'] += b'\n// changed\n'
        with self.assertRaisesRegex(ValueError, 'Original source blob/mode mismatch'):
            custody.verify_source(self.altered_source(corrupt), self.head)

    def test_changed_git_mode_cannot_redefine_tree(self):
        def corrupt(data, modes, manifest):
            for row in manifest['git_files']:
                if row['path'] == 'src/main.rs': row['mode'] = '100755'; modes[row['path']] = 0o100755
        with self.assertRaisesRegex(ValueError, 'Complete original Git tree mismatch'):
            custody.verify_source(self.altered_source(corrupt), self.head)

    def test_changed_commit_object(self):
        def corrupt(data, modes, manifest): manifest['commit_object_hex'] += '0a'
        with self.assertRaisesRegex(ValueError, 'Original commit object mismatch'):
            custody.verify_source(self.altered_source(corrupt), self.head)

    def test_unsafe_source_path(self):
        def corrupt(data, modes, manifest): data['../escape'] = b'unsafe'; modes['../escape'] = 0o100644
        with self.assertRaisesRegex(ValueError, 'Unsafe input path'):
            custody.verify_source(self.altered_source(corrupt), self.head)

    def test_case_colliding_source_path(self):
        def corrupt(data, modes, manifest): data['cargo.lock'] = data['Cargo.lock']; modes['cargo.lock'] = 0o100644
        with self.assertRaisesRegex(ValueError, 'case-colliding'):
            custody.verify_source(self.altered_source(corrupt), self.head)

    def test_file_directory_collision(self):
        def corrupt(data, modes, manifest): data['src'] = b'collision'; modes['src'] = 0o100644
        with self.assertRaisesRegex(ValueError, 'File/directory path collision'):
            custody.verify_source(self.altered_source(corrupt), self.head)

    def test_build_manifest_corruption(self):
        with self.assertRaisesRegex(ValueError, 'Build manifest SHA mismatch'):
            custody.verify_site(self.site, '0' * 64)

    def test_corrupt_module_rejected_before_restore(self):
        with tempfile.TemporaryDirectory() as tmp:
            site = Path(tmp) / 'site'; shutil.copytree(self.site, site)
            p = site / self.build['wasm']['path']; raw = p.read_bytes(); p.write_bytes(raw[:-1] + bytes([raw[-1] ^ 1]))
            dest = Path(tmp) / 'must-not-exist'
            p = subprocess.run([sys.executable, str(ROOT / 'tools/receive-site.py'), '--site', str(site),
                                '--manifest-sha256', self.site_sha, '--restore-source', str(dest)], capture_output=True)
            self.assertNotEqual(p.returncode, 0); self.assertIn(b'Site file hash mismatch', p.stderr)
            self.assertFalse(dest.exists())

    def test_changed_ui_with_updated_site_hashes(self):
        with tempfile.TemporaryDirectory() as tmp:
            site = Path(tmp) / 'site'; shutil.copytree(self.site, site)
            p = site / 'app.js'; p.write_bytes(p.read_bytes() + b'\n// changed\n')
            manifest = json.loads(self.raw_manifest)
            for row in manifest['files']:
                if row['path'] == 'app.js': row.update(bytes=p.stat().st_size, sha256=custody.digest(p.read_bytes()))
            raw = custody.encoded(manifest); (site / custody.BUILD_MANIFEST).write_bytes(raw)
            with self.assertRaisesRegex(ValueError, 'Site UI differs from source'):
                custody.verify_site(site, custody.digest(raw))

    def test_existing_restore_destination_preserved(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / 'existing'; dest.mkdir(); marker = dest / 'keep'; marker.write_text('keep')
            with self.assertRaisesRegex(ValueError, 'existing files are preserved'):
                custody.restore_source(self.data, self.modes, dest)
            self.assertEqual(marker.read_text(), 'keep'); self.assertEqual(list(dest.iterdir()), [marker])

    def test_compiled_target_overlap(self):
        with tempfile.TemporaryDirectory() as tmp:
            old = os.environ.get('CARGO_TARGET_DIR'); os.environ['CARGO_TARGET_DIR'] = str(Path(tmp) / 'compiled')
            try:
                with self.assertRaisesRegex(ValueError, 'compiled target'):
                    custody.new_destination(Path(tmp) / 'compiled/receiver')
            finally:
                if old is None: os.environ.pop('CARGO_TARGET_DIR')
                else: os.environ['CARGO_TARGET_DIR'] = old

    def test_linked_destination_parent(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / 'target'; target.mkdir(); marker = target / 'keep'; marker.write_text('keep')
            link = Path(tmp) / 'linked'
            if os.name == 'nt':
                p = subprocess.run(['cmd', '/c', 'mklink', '/J', str(link), str(target)], capture_output=True)
                self.assertEqual(p.returncode, 0, p.stderr.decode())
            else:
                link.symlink_to(target, target_is_directory=True)
            with self.assertRaisesRegex(ValueError, 'link/junction'):
                custody.restore_source(self.data, self.modes, link / 'source')
            self.assertEqual(marker.read_text(), 'keep'); self.assertFalse((target / 'source').exists())

    def test_default_target_overlap_without_environment_override(self):
        old = os.environ.pop('CARGO_TARGET_DIR', None)
        try:
            with self.assertRaisesRegex(ValueError, 'compiled target'):
                custody.new_destination(ROOT / 'target/unwanted-receiver-source', ROOT)
        finally:
            if old is not None: os.environ['CARGO_TARGET_DIR'] = old

    def test_archive_rebuild_rejects_unlisted_cargo_config(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = custody.restore_source(self.data, self.modes, Path(tmp) / 'source')
            (source / '.cargo').mkdir(exist_ok=True)
            config = source / '.cargo/config.toml'; config.write_text('[build]\nrustflags = ["--cfg", "unlisted"]\n')
            with self.assertRaisesRegex(ValueError, 'Unexpected source/config file: .cargo/config.toml'):
                custody.source_data(source, self.head)
            self.assertTrue(config.exists())

    def test_documented_generated_outputs_are_not_source_inputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = custody.restore_source(self.data, self.modes, Path(tmp) / 'source')
            for directory in ['dist', 'target', 'node_modules', 'test-results', 'tools/__pycache__']:
                path = source / directory; path.mkdir(parents=True, exist_ok=True); (path / 'generated.bin').write_bytes(b'generated')
            data, modes = custody.source_data(source, self.head)
            self.assertEqual(data, self.data); self.assertEqual(modes, self.modes)

    def test_valid_receiver_restores_every_source_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / 'source'
            p = subprocess.run([sys.executable, str(ROOT / 'tools/receive-site.py'), '--site', str(self.site),
                                '--manifest-sha256', self.site_sha, '--restore-source', str(dest)], capture_output=True)
            self.assertEqual(p.returncode, 0, p.stderr.decode())
            for name, value in self.data.items():
                self.assertEqual((dest / name).read_bytes(), value)
                if os.name != 'nt': self.assertEqual((dest / name).stat().st_mode & 0o777, self.modes[name] & 0o777)


if __name__ == '__main__':
    unittest.main()
