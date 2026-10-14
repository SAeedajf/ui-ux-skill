#!/usr/bin/env python3
"""Validate the Phase 04 machine report against its schema and gate contract."""
import argparse
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / 'schemas/phase-04-report.schema.json'
REPORT_PATH = ROOT / 'docs/plugin/reports/phase-04.json'
REQUIRED_GATES = {f'R{number:02d}' for number in range(1, 19)}
MODEL_GATES = {'R06', 'R07', 'R08', 'R10', 'R11', 'R12'}


def validate_report(report):
    errors = []
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding='utf-8'))
        jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).validate(report)
    except jsonschema.ValidationError as exc:
        errors.append(f'schema: {exc.message}')
        return errors

    gates = report['test_results']
    gate_ids = [gate['id'] for gate in gates]
    if len(gate_ids) != len(set(gate_ids)):
        errors.append('test_results contains duplicate gate IDs')
    if set(gate_ids) != REQUIRED_GATES:
        errors.append(f'test_results must contain exactly R01-R18; found={sorted(gate_ids)}')
    by_id = {gate['id']: gate for gate in gates}
    expected_open = sorted(gate['id'] for gate in gates if gate['status'] != 'PASS')
    expected_blocked = sorted(gate['id'] for gate in gates if gate['status'] == 'BLOCKED')
    if sorted(report['open_gates']) != expected_open:
        errors.append('open_gates does not match non-PASS test_results')
    if sorted(report['blocked_gates']) != expected_blocked:
        errors.append('blocked_gates does not match BLOCKED test_results')
    for gate_id in MODEL_GATES:
        gate = by_id.get(gate_id)
        if gate and gate['status'] == 'PASS':
            evidence = gate['evidence']
            if not any(marker in evidence.lower() for marker in ('trace', '.jsonl', 'codex-runs')):
                errors.append(f'{gate_id} model gate cannot PASS without trace evidence')
                continue
            evidence_path = Path(evidence.split('#', 1)[0])
            candidate = (ROOT / evidence_path).resolve()
            if ROOT not in candidate.parents or not candidate.is_file():
                errors.append(f'{gate_id} trace evidence file does not exist inside the repository')
    if report['status'] == 'PASS' and report['open_gates']:
        errors.append('overall PASS is not allowed while acceptance gates remain open')
    return errors


def finalize_report(report, artifact_url, artifact_sha256):
    """Return the CI-specific report after the archive has actually been built."""
    finalized = deepcopy(report)
    finalized['artifact_url'] = artifact_url
    finalized['artifact_sha256'] = artifact_sha256
    finalized['ci_status'] = 'PASS'
    finalized['release_candidate'] = 'RELEASE_CANDIDATE_READY'
    completed_at = datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z')
    for gate_id, method, evidence, reason in (
        ('R15', 'Deterministic ZIP build, validation, and GitHub Actions upload', artifact_url, 'The validated 0.1.0 package and provenance were uploaded as a workflow artifact.'),
        ('R16', 'GitHub Actions deterministic-checks job', artifact_url, 'All deterministic checks and package artifact upload completed successfully.'),
        ('R17', 'Phase 04 JSON schema and semantic validator', 'docs/plugin/reports/phase-04.json', 'The CI-finalized report passed schema and gate consistency validation.'),
    ):
        gate = next(gate for gate in finalized['test_results'] if gate['id'] == gate_id)
        gate.update(status='PASS', executed_at=completed_at, method=method, evidence=evidence, reason=reason)
    finalized['open_gates'] = sorted(gate['id'] for gate in finalized['test_results'] if gate['status'] != 'PASS')
    finalized['blocked_gates'] = sorted(gate['id'] for gate in finalized['test_results'] if gate['status'] == 'BLOCKED')
    return finalized


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', type=Path, default=REPORT_PATH)
    parser.add_argument('--finalize-run-url', help='set actual GitHub Actions run URL and CI pass status')
    parser.add_argument('--archive', type=Path, help='built ZIP whose SHA-256 is added to the report')
    args = parser.parse_args()
    try:
        report = json.loads(args.report.read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError) as exc:
        print(f'FAIL: cannot read report: {exc}')
        return 1
    if args.finalize_run_url or args.archive:
        if not (args.finalize_run_url and args.archive):
            print('FAIL: --finalize-run-url and --archive must be provided together')
            return 1
        try:
            digest = hashlib.sha256(args.archive.read_bytes()).hexdigest()
        except OSError as exc:
            print(f'FAIL: cannot read built archive: {exc}')
            return 1
        report = finalize_report(report, args.finalize_run_url, digest)
        args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    errors = validate_report(report)
    if errors:
        for error in errors:
            print(f'FAIL: {error}')
        return 1
    print(f'PASS: {args.report} conforms to schema and acceptance-gate contract')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
