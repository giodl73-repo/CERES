"""Integrity and safe restore controls over the actual committed input capsule."""
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('custody', ROOT / 'tools/input-custody.py')
custody = importlib.util.module_from_spec(spec); spec.loader.exec_module(custody)


class CustodyChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = (ROOT / 'cargo-inputs/inputs.zip').read_bytes()
        cls.sha = (ROOT / 'cargo-inputs/sha256.txt').read_text().split()[0]
        cls.lock = (ROOT / 'Cargo.lock').read_bytes()
        cls.manifest, cls.data = custody.verify(cls.raw, cls.sha, cls.lock)

    def modified(self, path, value, update_inventory=True):
        values = dict(self.data); values[path] = value
        if update_inventory:
            manifest = json.loads(values['INPUT-MANIFEST.json'])
            for row in manifest['files']:
                if row['path'] == path:
                    row.update(bytes=len(value), sha256=custody.digest(value))
            values['INPUT-MANIFEST.json'] = json.dumps(manifest).encode()
        modes = {'original-git/' + r['commit'] + '/' + p['path']: int(p['mode'], 8)
                 for r in self.manifest['git_sources'] for p in r['files']}
        result = io.BytesIO()
        with zipfile.ZipFile(result, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
            for name, data in values.items():
                info = zipfile.ZipInfo(name); info.external_attr = modes.get(name, 0o100644) << 16
                info.compress_type = zipfile.ZIP_DEFLATED; archive.writestr(info, data)
        return result.getvalue()

    def test_complete_original_inputs(self):
        self.assertEqual(len(self.manifest['registry']), 27)
        self.assertEqual(sum(len(r['packages']) for r in self.manifest['git_sources']), 5)

    def test_changed_outer_digest(self):
        with self.assertRaisesRegex(ValueError, 'SHA mismatch'):
            custody.verify(self.raw + b'changed', self.sha, self.lock)

    def test_changed_lock(self):
        with self.assertRaisesRegex(ValueError, 'Cargo.lock differs'):
            custody.verify(self.raw, self.sha, self.lock + b'\n')

    def test_windows_and_canonical_lock_line_endings(self):
        canonical = self.lock.replace(b'\r\n', b'\n')
        custody.verify(self.raw, self.sha, canonical)
        custody.verify(self.raw, self.sha, canonical.replace(b'\n', b'\r\n'))

    def test_unsafe_archive_path(self):
        raw = self.modified('../escape', b'unsafe', False)
        with self.assertRaisesRegex(ValueError, 'Unsafe input path'):
            custody.verify(raw, custody.digest(raw), self.lock)

    def test_registry_source_corruption_with_updated_file_hash(self):
        path = next(p for p in self.data if p.startswith('vendor/serde-') and p.endswith('/src/lib.rs'))
        raw = self.modified(path, self.data[path] + b'\n// changed\n')
        with self.assertRaisesRegex(ValueError, 'Vendor differs from original registry member'):
            custody.verify(raw, custody.digest(raw), self.lock)

    def test_original_git_corruption_with_updated_file_hash(self):
        path = next(p for p in self.data if p.startswith('original-git/') and p.endswith('/src/lib.rs'))
        raw = self.modified(path, self.data[path] + b'\n// changed\n')
        with self.assertRaisesRegex(ValueError, 'Original Git blob mismatch'):
            custody.verify(raw, custody.digest(raw), self.lock)

    def test_existing_destination_is_preserved(self):
        with tempfile.TemporaryDirectory() as tmp:
            existing = Path(tmp) / 'existing'; existing.mkdir(); marker = existing / 'keep'; marker.write_text('keep')
            home = Path(tmp) / 'home'
            with self.assertRaisesRegex(ValueError, 'Use new folders'):
                custody.restore(self.data, existing, home)
            self.assertEqual(marker.read_text(), 'keep'); self.assertFalse(home.exists())

    def test_verified_restore(self):
        with tempfile.TemporaryDirectory() as tmp:
            inputs = Path(tmp) / 'inputs'; home = Path(tmp) / 'home'
            custody.restore(self.data, inputs, home)
            for path, value in self.data.items():
                if path.startswith('vendor/'):
                    self.assertEqual((inputs / path).read_bytes(), value)
            config = (home / 'config.toml').read_text()
            self.assertIn((inputs / 'vendor').as_posix(), config)
            self.assertIn('offline = true', config)
            self.assertFalse((home / 'registry').exists()); self.assertFalse((home / 'git').exists())

    def test_nested_destinations_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            inputs = Path(tmp) / 'inputs'
            with self.assertRaisesRegex(ValueError, 'must be separate'):
                custody.restore(self.data, inputs, inputs / 'home')
            self.assertFalse(inputs.exists())


if __name__ == '__main__':
    unittest.main()
