#!/usr/bin/env python3
"""Validate the Phase 05-C retry report and its checked-in evidence."""
import argparse
import json
from copy import deepcopy
from pathlib import Path
import sys

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / 'docs/plugin/reports/phase-05c-retry.json'
SCHEMA = ROOT / 'schemas/phase-05c-retry-report.schema.json'


def validate(report):
    schema = json.loads(SCHEMA.read_text(encoding='utf-8'))
    jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    ).validate(report)
    errors = []
    for evidence_path in report['evidence']:
        candidate = (ROOT / evidence_path).resolve()
        if ROOT not in candidate.parents or not candidate.is_file():
            errors.append(f'missing or unsafe evidence path: {evidence_path}')
    if report['positive']['status'] == 'PASS' and not report['positive']['plugin_skill_read']:
        errors.append('positive activation PASS requires a Plugin Skill read')
    if report['negative']['status'] == 'PASS' and report['negative']['uiux_skill_read']:
        errors.append('negative activation PASS cannot include a UI/UX Skill read')
    if report['model_calls']['attempted'] != report['model_calls']['completed'] + report['model_calls']['failed']:
        errors.append('model call accounting does not reconcile')
    if report['model_calls']['attempted'] != 3 or report['model_calls']['retry'] != 0:
        errors.append('the authorized maximum is exactly three calls with no retry')
    if report['status'] == 'PASS' and (
        report['positive']['status'] != 'PASS'
        or report['model']['actual_identity'] != 'VERIFIED'
        or report['repair']['status'] != 'PASS'
    ):
        errors.append('overall PASS requires verified model identity, positive activation, and repair')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--finalize-run-url')
    parser.add_argument('--output-commit')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    try:
        report = json.loads(REPORT.read_text(encoding='utf-8'))
        errors = validate(report)
    except (OSError, json.JSONDecodeError, jsonschema.ValidationError) as exc:
        print(f'Phase 05-C retry report invalid: {exc}', file=sys.stderr)
        return 1
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    if args.finalize_run_url or args.output_commit or args.output:
        if not args.finalize_run_url or not args.output_commit or not args.output:
            print('CI finalization requires --finalize-run-url, --output-commit, and --output.', file=sys.stderr)
            return 1
        finalized = deepcopy(report)
        finalized['ci'] = {
            'status': 'PASS',
            'run_url': args.finalize_run_url,
            'output_commit': args.output_commit,
        }
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(
            json.dumps(finalized, ensure_ascii=False, indent=2) + '\n', encoding='utf-8'
        )
        print(f'Finalized Phase 05-C retry report for {args.output_commit}.')
    print('Phase 05-C retry report and evidence references are valid.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
