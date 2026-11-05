"""Run the original typed native/WASM controls with platform-correct paths."""
import argparse
import json
import os
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site', type=Path, default=ROOT / 'dist/CERES')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    metadata = json.loads(subprocess.check_output(['cargo', '+1.95.0', 'metadata', '--locked', '--offline', '--no-deps', '--format-version', '1'], cwd=ROOT))
    native = Path(metadata['target_directory']) / 'debug/examples' / ('reader-control.exe' if os.name == 'nt' else 'reader-control')
    subprocess.run(['node', str(ROOT / 'tools/check-reader.mjs'), str(args.site.resolve() / 'pkg/ceres_web.js'),
                    str(native), str(args.output.resolve())], cwd=ROOT, check=True)
