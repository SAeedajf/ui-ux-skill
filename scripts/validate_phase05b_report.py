#!/usr/bin/env python3
"""Validate Phase 05-B operational evidence and CI report finalization."""
import argparse
from copy import deepcopy
from datetime import datetime, timezone
import json
from pathlib import Path
import re

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / 'docs/plugin/reports/phase-05b.json'
SCHEMA_PATH = ROOT / 'schemas/phase-05b-report.schema.json'


def _exists_in_repo(value):
    if not value:
        return False
    path = value.split('#', 1)[0]
    candidate = (ROOT / path).resolve()
    return ROOT in candidate.parents and candidate.is_file()


def _trace_text(value):
    if not _exists_in_repo(value):
        return None
    return (ROOT / value.split('#', 1)[0]).read_text(encoding='utf-8')


def _completed_trace(value):
    text = _trace_text(value)
    if text is None:
        return False
    try:
        events = [json.loads(line) for line in text.splitlines() if line.strip()]
    except json.JSONDecodeError:
        return False
    types = {event.get('type') for event in events if isinstance(event, dict)}
    return 'turn.completed' in types and not (types & {'error', 'turn.failed'})


def _plugin_skill_trace(value):
    text = _trace_text(value)
    if text is None or not _completed_trace(value):
        return False
    lowered = text.lower()
    return 'skill.md' in lowered and 'ui-ux-pro-marketplace' in lowered


def validate_report(report):
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding='utf-8'))
        jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).validate(report)
    except jsonschema.ValidationError as exc:
        return [f'schema: {exc.message}']
    except (OSError, json.JSONDecodeError) as exc:
        return [f'schema: cannot load schema: {exc}']

    errors = []
    for name in ('positive_smoke', 'negative_smoke'):
        case = report[name]
        if case['status'] == 'PASS':
            if not case['attempted'] or not case['accepted']:
                errors.append(f'{name} PASS requires an attempted, accepted model request')
            if not _exists_in_repo(case['trace_evidence']):
                errors.append(f'{name} PASS requires an existing in-repository trace reference')
            elif not _completed_trace(case['trace_evidence']):
                errors.append(f'{name} PASS requires a completed model trace without errors')
            elif name == 'positive_smoke' and not _plugin_skill_trace(case['trace_evidence']):
                errors.append('positive_smoke PASS requires a completed trace reading a namespaced Plugin Skill file')
            elif name == 'negative_smoke':
                trace = _trace_text(case['trace_evidence']).lower()
                if 'ui-ux-pro-marketplace' in trace and 'skill.md' in trace:
                    errors.append('negative_smoke PASS cannot include a UI/UX Plugin Skill file read')
        if case['status'] == 'NOT_RUN' and (case['attempted'] or case['accepted']):
            errors.append(f'{name} NOT_RUN cannot claim an attempted or accepted request')
        if case['trace_evidence'] and not _exists_in_repo(case['trace_evidence']):
            errors.append(f'{name} trace evidence must resolve to an in-repository file')

    discovery = report['plugin_discovery']
    if discovery['status'] == 'PASS' and (discovery['plugin_skill_count'] != 15 or discovery['plugin_namespace_count'] != 15):
        errors.append('plugin discovery PASS requires exactly 15 namespaced Plugin skills')
    if report['plugin_install_method'] and not discovery['rollback_verified']:
        errors.append('temporary Plugin installation requires verified rollback before completion')

    calls = report['model_call_count']
    if calls['accepted'] > calls['attempted']:
        errors.append('accepted model calls cannot exceed attempted calls')
    if calls['attempted'] != calls['positive'] + calls['negative'] + calls['repair'] + calls['retry']:
        errors.append('attempted calls must reconcile with positive, negative, repair, and retry counts')
    if calls['retry'] > 1:
        errors.append('at most one retry is allowed')
    if report['status'] == 'PASS':
        if report['positive_smoke']['status'] != 'PASS' or report['negative_smoke']['status'] != 'PASS':
            errors.append('overall PASS requires positive and negative smoke PASS')
        if not report['agent_authored_diff']['created'] or not report['agent_authored_diff']['diff_evidence']:
            errors.append('overall PASS requires a real Agent-authored diff')
        if report['fixture_after']['status'] != 'PASS' or report['fixture_after']['tests_run'] != 5 or report['fixture_after']['passed'] != 5:
            errors.append('overall PASS requires all five post-repair fixture tests to pass')
    if report['agent_authored_diff']['created']:
        diff_path = report['agent_authored_diff']['diff_evidence']
        if not report['agent_authored_diff']['files'] or not _exists_in_repo(diff_path):
            errors.append('Agent-authored diff requires changed file names and existing diff evidence')
        if not _plugin_skill_trace(report['repair_trace_evidence']):
            errors.append('Agent-authored repair requires a completed trace reading a namespaced Plugin Skill file')
    elif report['repair_trace_evidence'] is not None:
        errors.append('repair trace cannot be claimed when no Agent-authored diff exists')
    if report['fixture_baseline']['status'] == 'EXPECTED_FAILURES':
        if report['fixture_baseline']['tests_run'] != report['fixture_baseline']['expected_failures']:
            errors.append('expected-failure baseline counts must match')
        if not _exists_in_repo(report['fixture_baseline']['evidence']):
            errors.append('fixture baseline evidence must resolve to an in-repository file')
    if report['ci_status'] == 'PASS':
        if not report['ci_run_url'] or not report['ci_output_commit']:
            errors.append('CI PASS requires run URL and exact output commit')
    if report['status'] == 'BLOCKED' and not report['blockers']:
        errors.append('overall BLOCKED requires a recorded blocker')
    for ref in report['evidence_paths']:
        if not _exists_in_repo(ref):
            errors.append(f'evidence path does not resolve in the repository: {ref}')
    return errors


def finalize_ci_report(report, run_url, output_commit):
    finalized = deepcopy(report)
    finalized['ci_status'] = 'PASS'
    finalized['ci_run_url'] = run_url
    finalized['ci_output_commit'] = output_commit
    finalized['ci_checked_at'] = datetime.now(timezone.utc).isoformat()
    return finalized


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', type=Path, default=REPORT_PATH)
    parser.add_argument('--finalize-run-url')
    parser.add_argument('--output-commit')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    try:
        report = json.loads(args.report.read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError) as exc:
        print(f'FAIL: cannot read report: {exc}')
        return 1
    finalize_args = (args.finalize_run_url, args.output_commit, args.output)
    if any(finalize_args):
        if not all(finalize_args):
            print('FAIL: finalization requires --finalize-run-url, --output-commit, and --output')
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
        print(f'PASS: finalized Phase 05-B report written to {args.output}')
        return 0
    errors = validate_report(report)
    if errors:
        for error in errors:
            print(f'FAIL: {error}')
        return 1
    print(f'PASS: {args.report} conforms to the Phase 05-B schema and evidence contract')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
