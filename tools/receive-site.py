"""Verify a complete downloaded site and optionally restore verified source.

Use the manifest SHA from a separately trusted CI/release receipt. This command
does not execute archive code, contact a service, or acquire packages.
"""
import argparse
import json
from pathlib import Path
from source_custody import verify_site, restore_source

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site', type=Path, required=True)
    parser.add_argument('--manifest-sha256', required=True)
    parser.add_argument('--restore-source', type=Path)
    args = parser.parse_args()
    site, source, data, modes = verify_site(args.site, args.manifest_sha256)
    if args.restore_source:
        restore_source(data, modes, args.restore_source)
    print(json.dumps(dict(verified=True, source_commit=source['source_commit'], git_blobs=len(source['git_files']),
                         sizes=site['sizes'], restored=bool(args.restore_source))))
