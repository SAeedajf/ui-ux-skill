#!/usr/bin/env python3
"""Validate plugin schema, Skill metadata, references, safety and source integrity."""
import argparse
from pathlib import Path
from plugin_packaging import ROOT, validate_package


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--package', type=Path, default=ROOT / 'plugins/ui-ux-pro', help='package directory to validate')
    parser.add_argument('--structure-only', action='store_true', help='validate an extracted package without comparing repository source')
    args = parser.parse_args()
    errors = validate_package(args.package, expected_source=None if args.structure_only else ROOT / '.agents/skills')
    if errors:
        for error in errors: print(f'FAIL: {error}')
        return 1
    print(f'PASS: {args.package} satisfies schema, Skill, reference and safety checks' + ('' if args.structure_only else ' and exact source integrity'))
    return 0

if __name__ == '__main__': raise SystemExit(main())
