"""Validate the evidence-linked Phase 05-D report and finalize its CI artifact."""
import argparse
from copy import deepcopy
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / 'docs/plugin/reports/phase-05d.json'
GATE_STATES = {'PASS', 'FAIL', 'BLOCKED', 'NOT_RUN', 'NEEDS_REVIEW'}


def validate(report):
    errors = []
    for key in ('phase', 'status', 'base_commit', 'branch', 'model', 'plugin', 'gates', 'evidence'):
        if key not in report:
            errors.append(f'missing report field: {key}')
    if report.get('phase') != '05-D':
        errors.append('phase must be 05-D')
    if report.get('status') not in GATE_STATES:
        errors.append('overall status must be a supported gate state')
    if report.get('branch') != 'codex/ui-ux-plugin-phase-05d':
        errors.append('report branch does not match Phase 05-D branch')
    gates = report.get('gates', {})
    required_gates = {f'D{i:02}' for i in range(1, 15)}
    if set(gates) != required_gates:
        errors.append('gate set must contain D01 through D14 exactly')
    if any(value not in GATE_STATES for value in gates.values()):
        errors.append('all gates must use supported gate states')
    if gates.get('D04') == 'PASS' and not report.get('activation_traces', {}).get('explicit_plugin_skill_paths'):
        errors.append('D04 PASS requires trace paths to Plugin Skill files')
    if gates.get('D05') == 'PASS' and not report.get('activation_traces', {}).get('automatic_plugin_skill_paths'):
        errors.append('D05 PASS requires trace paths to Plugin Skill files')
    if gates.get('D06') == 'PASS' and not report.get('activation_traces', {}).get('combined_context_skill_paths'):
        errors.append('D06 PASS requires combined-context trace paths')
    if report.get('status') == 'PASS' and any(gates.get(g) != 'PASS' for g in required_gates):
        errors.append('overall PASS requires all D01-D14 gates to PASS')
    if report.get('plugin', {}).get('plugin_only_prompt_input_skill_count', 0) > report.get('plugin', {}).get('expected_skill_count', 0):
        errors.append('Plugin discovery count exceeds expected skill count')
    for path in report.get('evidence', []):
        candidate = (ROOT / path).resolve()
        if ROOT not in candidate.parents or not candidate.is_file():
            errors.append(f'missing or unsafe evidence path: {path}')
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
    except (OSError, json.JSONDecodeError) as exc:
        print(f'Phase 05-D report invalid: {exc}', file=sys.stderr)
        return 1
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    if args.finalize_run_url or args.output_commit or args.output:
        if not args.finalize_run_url or not args.output_commit or not args.output:
            print('CI finalization requires --finalize-run-url, --output-commit, and --output.', file=sys.stderr)
            return 1
        finalized = deepcopy(report)
        finalized['output_commit'] = args.output_commit
        finalized['ci'] = {'status': 'PASS', 'run_url': args.finalize_run_url}
        finalized['gates']['D11'] = 'PASS'
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(finalized, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print(f'Finalized Phase 05-D report for {args.output_commit}.')
    print('Phase 05-D report and evidence references are valid.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
