"""Verify a pinned complete source ZIP before optional restoration; no execution."""
import argparse
import json
from pathlib import Path
from source_custody import digest, verify_source, restore_source

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--sha256', required=True, help='Digest from a separately trusted build/release receipt')
    parser.add_argument('--commit', required=True)
    parser.add_argument('--restore-source', type=Path)
    args = parser.parse_args(); raw = args.source.read_bytes()
    if digest(raw) != args.sha256:
        raise ValueError('Source ZIP SHA mismatch')
    manifest, data, modes = verify_source(raw, args.commit)
    if args.restore_source:
        restore_source(data, modes, args.restore_source)
    print(json.dumps(dict(verified=True, source_commit=manifest['source_commit'], git_blobs=len(manifest['git_files']),
                         sha256=digest(raw), restored=bool(args.restore_source))))
