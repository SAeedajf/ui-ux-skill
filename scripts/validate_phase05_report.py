#!/usr/bin/env python3
"""Validate Phase 05 runtime evidence and enforce trace/diff/status gates."""
import argparse
from copy import deepcopy
from datetime import datetime, timezone
import json
from pathlib import Path
import re

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / 'schemas/phase-05-report.schema.json'
REPORT_PATH = ROOT / 'docs/plugin/reports/phase-05.json'
REQUIRED_GATES = {f'O{number:02d}' for number in range(1, 17)}
ACTIVATION_GATES = {'O04', 'O05', 'O11', 'O12'}


def _evidence_values(gate):
    return [item for values in gate['evidence'].values() for item in values]


def _repo_evidence_exists(value):
    path = value.split('#', 1)[0]
    if re.match(r'^https?://', path):
        return True
    candidate = (ROOT / path).resolve()
    return ROOT == candidate or ROOT in candidate.parents and candidate.is_file()


def _valid_trace_ref(value):
    if re.match(r'^https?://', value) or not any(token in value.lower() for token in ('trace', 'codex-runs')):
        return False
    path = value.split('#', 1)[0]
    candidate = (ROOT / path).resolve()
    return candidate.suffix == '.jsonl' and ROOT in candidate.parents and candidate.is_file()


def validate_report(report):
    errors = []
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding='utf-8'))
        jsonschema.Draft202012Validator(
            schema, format_checker=jsonschema.FormatChecker()
        ).validate(report)
    except jsonschema.ValidationError as exc:
        return [f'schema: {exc.message}']
    except (OSError, json.JSONDecodeError) as exc:
        return [f'schema: cannot load schema: {exc}']

    gates = report['test_results']
    gate_ids = [gate['id'] for gate in gates]
    if len(gate_ids) != len(set(gate_ids)):
        errors.append('test_results contains duplicate gate IDs')
    if set(gate_ids) != REQUIRED_GATES:
        errors.append(f'test_results must contain exactly O01-O16; found={sorted(gate_ids)}')
    by_id = {gate['id']: gate for gate in gates}
    expected_open = sorted(gate['id'] for gate in gates if gate['status'] != 'PASS')
    expected_blocked = sorted(gate['id'] for gate in gates if gate['status'] == 'BLOCKED')
    expected_review = sorted(gate['id'] for gate in gates if gate['status'] == 'NEEDS_REVIEW')
    expected_not_run = sorted(gate['id'] for gate in gates if gate['status'] == 'NOT_RUN')
    for key, expected in (
        ('open_gates', expected_open),
        ('blocked_gates', expected_blocked),
        ('needs_review_gates', expected_review),
        ('not_run_gates', expected_not_run),
    ):
        if sorted(report[key]) != expected:
            errors.append(f'{key} does not match test_results statuses')

    for gate in gates:
        evidence = _evidence_values(gate)
        if gate['status'] == 'PASS':
            if gate['executed_on'] is None:
                errors.append(f"{gate['id']} PASS requires an execution date")
            if not evidence:
                errors.append(f"{gate['id']} PASS requires evidence")
        elif gate['status'] == 'NOT_RUN':
            if gate['executed_on'] is not None:
                errors.append(f"{gate['id']} NOT_RUN must not claim an execution date")
            if gate['output'] is not None:
                errors.append(f"{gate['id']} NOT_RUN must not contain a fabricated output")
        elif gate['status'] == 'BLOCKED' and gate['output'] is not None:
            errors.append(f"{gate['id']} BLOCKED must not contain a successful output")

        if gate['status'] == 'PASS':
            for value in evidence:
                if not _repo_evidence_exists(value):
                    errors.append(f"{gate['id']} evidence does not resolve inside the repository or to a URL: {value}")

        if gate['id'] in ACTIVATION_GATES and gate['status'] == 'PASS':
            traces = gate['evidence']['trace']
            if not traces:
                errors.append(f"{gate['id']} activation PASS requires trace evidence")
            elif not any(_valid_trace_ref(trace) for trace in traces):
                errors.append(f"{gate['id']} activation requires an existing sanitized JSONL trace file inside the repository")

        if gate['id'] == 'O06' and gate['status'] == 'PASS':
            if not any(_valid_trace_ref(trace) for trace in gate['evidence']['trace']):
                errors.append('O06 repair PASS requires an existing sanitized Agent JSONL trace file inside the repository')
            if not gate['evidence']['diff']:
                errors.append('O06 repair PASS requires a real diff')
            if not gate['evidence']['test_after']:
                errors.append('O06 repair PASS requires post-repair test evidence')
        if gate['id'] == 'O07' and gate['status'] == 'PASS' and not gate['evidence']['test_after']:
            errors.append('O07 PASS requires post-repair regression evidence')

    if report['status'] == 'PASS' and report['open_gates']:
        errors.append('overall PASS is not allowed while acceptance gates remain open')
    if report['ci_status'] == 'PASS' and not report['ci_run_url']:
        errors.append('ci_status PASS requires ci_run_url')
    if report['test_results'][13]['id'] != 'O14':
        errors.append('O14 CI gate must remain part of the exact O01-O16 contract')
    return errors


def finalize_ci_report(report, run_url, output_commit):
    """Create a CI artifact report for the exact GitHub Actions commit/run."""
    finalized = deepcopy(report)
    finalized['output_commit'] = output_commit
    finalized['ci_status'] = 'PASS'
    finalized['ci_run_url'] = run_url
    gate = next(item for item in finalized['test_results'] if item['id'] == 'O14')
    gate.update(
        status='PASS',
        executed_on=datetime.now(timezone.utc).date().isoformat(),
        method='GitHub Actions Phase 05 deterministic validation workflow',
        evidence={
            'trace': [], 'diff': [], 'test_after': [],
            'other': [run_url],
        },
        output='Phase 05 report, tests, repository, marketplace, package, and schema validators passed in this run.',
        reason='The current GitHub Actions run completed successfully on output_commit.',
    )
    finalized['open_gates'] = sorted(item['id'] for item in finalized['test_results'] if item['status'] != 'PASS')
    finalized['blocked_gates'] = sorted(item['id'] for item in finalized['test_results'] if item['status'] == 'BLOCKED')
    finalized['needs_review_gates'] = sorted(item['id'] for item in finalized['test_results'] if item['status'] == 'NEEDS_REVIEW')
    finalized['not_run_gates'] = sorted(item['id'] for item in finalized['test_results'] if item['status'] == 'NOT_RUN')
    return finalized


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', type=Path, default=REPORT_PATH)
    parser.add_argument('--finalize-run-url', help='finalize a separate CI report artifact for the actual run')
    parser.add_argument('--output-commit', help='full commit SHA tested by this CI run')
    parser.add_argument('--output', type=Path, help='write finalized CI report to this path')
    args = parser.parse_args()
    try:
        report = json.loads(args.report.read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError) as exc:
        print(f'FAIL: cannot read report: {exc}')
        return 1
    finalize_args = (args.finalize_run_url, args.output_commit, args.output)
    if any(finalize_args):
        if not all(finalize_args):
            print('FAIL: --finalize-run-url, --output-commit, and --output must be provided together')
            return 1
        if not re.fullmatch(r'[0-9a-f]{40}', args.output_commit):
            print('FAIL: --output-commit must be a full lowercase commit SHA')
            return 1
        report = finalize_ci_report(report, args.finalize_run_url, args.output_commit)
        errors = validate_report(report)
        if errors:
            for error in errors:
                print(f'FAIL: {error}')
            return 1
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print(f'PASS: finalized CI report written to {args.output}')
        return 0

    errors = validate_report(report)
    if errors:
        for error in errors:
            print(f'FAIL: {error}')
        return 1
    print(f'PASS: {args.report} conforms to the Phase 05 schema and evidence contract')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
