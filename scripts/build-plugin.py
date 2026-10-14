#!/usr/bin/env python3
"""Build/check the generated portable UI/UX Pro Agent Plugin."""
import argparse
import subprocess
from pathlib import Path
from plugin_packaging import ROOT, build_package, build_archive, load_metadata


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'plugins/ui-ux-pro', help='package output directory')
    parser.add_argument('--check', action='store_true', help='verify generated package without writing')
    parser.add_argument('--archive', action='store_true', help='create deterministic ZIP and provenance sidecar under dist/')
    args = parser.parse_args()
    try:
        build_package(args.output, check=args.check)
        print(f'PASS: package {"matches source" if args.check else "built"} at {args.output}')
        if args.archive:
            if args.check is False:
                build_package(args.output, check=True)
            sha = subprocess.check_output(['git','-C',str(ROOT),'rev-parse','HEAD'],text=True).strip()
            metadata = load_metadata()
            zip_path = ROOT / 'dist' / f"{metadata['plugin_id']}-{metadata['version']}.zip"
            _, sidecar = build_archive(args.output, zip_path, sha, metadata['version'])
            print(f'PASS: deterministic archive {zip_path}')
            print(f'PASS: provenance {sidecar}')
    except Exception as exc:
        print(f'FAIL: {exc}')
        return 1
    return 0

if __name__ == '__main__': raise SystemExit(main())
