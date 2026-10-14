import copy
import unittest

from scripts.validate_phase05_report import finalize_ci_report, validate_report


def sample_report():
    gates = []
    for number in range(1, 17):
        gate_id = f'O{number:02d}'
        status = 'BLOCKED' if gate_id == 'O14' else 'NOT_RUN'
        if gate_id in {'O01', 'O02', 'O03', 'O09', 'O15', 'O16'}:
            status = 'PASS'
        gates.append({
            'id': gate_id,
            'status': status,
            'test_type': 'sample',
            'executed_on': None if status == 'NOT_RUN' else '2026-10-14',
            'method': 'isolated deterministic report test',
            'evidence': {
                'trace': [], 'diff': [], 'test_after': [],
                'other': ['docs/plugin/reports/phase-05-evidence.md'] if status == 'PASS' else [],
            },
            'output': None if status in {'BLOCKED', 'NOT_RUN'} else 'verified',
            'reason': 'Recorded status for validator contract test.',
        })
    open_gates = [g['id'] for g in gates if g['status'] != 'PASS']
    return {
        'phase': '05',
        'title': 'Runtime Unblocking & Operational Proof',
        'status': 'PARTIAL',
        'repository': 'https://github.com/SAeedajf/ui-ux-skill',
        'base_commit': '6c8069d05c7ac147c2c3d83cd88303674f012518',
        'output_commit': '6c8069d05c7ac147c2c3d83cd88303674f012518',
        'plugin_version': '0.1.0',
        'skills_count': 15,
        'codex_runtime': {
            'cli_path_selected': '/old/codex', 'selected_cli_version': '0.144.5',
            'alternate_cli_path': '/new/codex', 'alternate_cli_version': '0.153.4',
            'auth_status': 'AUTHENTICATED', 'usage_status': 'AVAILABLE_AT_SNAPSHOT',
            'usage_snapshot': {
                'observed_on': '2026-10-14', 'ordinary_usage_allowed': True,
                'primary_used_percent': 38, 'secondary_used_percent': 65,
                'rate_limit_reached': False,
            },
            'model_used': None, 'config_diagnosis': 'diagnosed',
            'config_repair_status': 'not changed',
        },
        'plugin_discovery': {
            'environment': 'temporary', 'installed': True, 'enabled': True,
            'version': '0.1.0', 'skill_count': 15, 'source_paths_verified': True,
            'discovery_scenarios': {
                'plugin_only': {'plugin_skills': 15, 'legacy_skills': 0},
                'legacy_only': {'plugin_skills': 0, 'legacy_skills': 15},
                'both': {'plugin_skills': 15, 'legacy_skills': 15},
            },
        },
        'fixture': {
            'baseline_expected_failures': 5, 'agent_repair': 'BLOCKED',
            'post_repair_tests': 'BLOCKED', 'browser_regression': 'NOT_RUN',
        },
        'chatgpt_plugin': {
            'plugin_id': 'plugins_test', 'release_id': 'pluginrel_test',
            'version': '0.1.0', 'scope': 'USER', 'visibility': 'PRIVATE',
            'metadata_status': 'CREATED', 'work_installation': 'BLOCKED',
            'runtime_tests': 'NOT_RUN',
        },
        'source_rights_review': {
            'status': 'NEEDS_REVIEW', 'matrix': 'docs/plugin/source-rights-resolution.md',
            'human_clearance': 'PENDING',
        },
        'test_results': gates,
        'open_gates': open_gates,
        'blocked_gates': ['O14'],
        'needs_review_gates': [],
        'not_run_gates': [g['id'] for g in gates if g['status'] == 'NOT_RUN'],
        'ci_status': 'PENDING', 'ci_run_url': None,
        'risks': [], 'owner_actions': [], 'next_phase_handoff': 'Continue Phase 05 only.',
    }


class Phase05ReportValidationTests(unittest.TestCase):
    def test_accepts_report_with_explicit_blocked_and_not_run_gates(self):
        self.assertEqual(validate_report(sample_report()), [])

    def test_rejects_pass_without_evidence(self):
        report = sample_report()
        gate = next(g for g in report['test_results'] if g['id'] == 'O03')
        gate['evidence']['other'] = []
        self.assertTrue(any('PASS requires evidence' in error for error in validate_report(report)))

    def test_rejects_activation_pass_without_trace(self):
        report = sample_report()
        gate = next(g for g in report['test_results'] if g['id'] == 'O04')
        gate.update(status='PASS', executed_on='2026-10-14', output='activated')
        gate['evidence']['other'] = ['docs/plugin/reports/phase-05-evidence.md']
        report['open_gates'].remove('O04')
        report['blocked_gates'] = ['O14']
        report['not_run_gates'].remove('O04')
        self.assertTrue(any('activation PASS requires trace' in error for error in validate_report(report)))

    def test_rejects_activation_pass_with_nonexistent_trace_file(self):
        report = sample_report()
        gate = next(g for g in report['test_results'] if g['id'] == 'O04')
        gate.update(status='PASS', executed_on='2026-10-14', output='activated')
        gate['evidence']['trace'] = ['codex-runs/not-a-real-trace.jsonl']
        report['open_gates'].remove('O04')
        report['not_run_gates'].remove('O04')
        self.assertTrue(any('existing sanitized JSONL trace file' in error for error in validate_report(report)))

    def test_rejects_agent_repair_pass_without_diff_or_post_tests(self):
        report = sample_report()
        gate = next(g for g in report['test_results'] if g['id'] == 'O06')
        gate.update(status='PASS', executed_on='2026-10-14', output='repaired')
        gate['evidence']['trace'] = ['codex-runs/trace.jsonl']
        gate['evidence']['other'] = ['docs/plugin/reports/phase-05-evidence.md']
        report['open_gates'].remove('O06')
        report['not_run_gates'].remove('O06')
        self.assertTrue(any('real diff' in error for error in validate_report(report)))
        self.assertTrue(any('post-repair test evidence' in error for error in validate_report(report)))

    def test_rejects_not_run_gate_with_output(self):
        report = sample_report()
        gate = next(g for g in report['test_results'] if g['id'] == 'O11')
        gate['output'] = 'invented result'
        self.assertTrue(any('NOT_RUN must not contain a fabricated output' in error for error in validate_report(report)))

    def test_ci_finalizer_records_actual_run_and_commit(self):
        report = sample_report()
        sha = 'a' * 40
        finalized = finalize_ci_report(
            report, 'https://github.com/SAeedajf/ui-ux-skill/actions/runs/12345', sha
        )
        self.assertEqual(finalized['output_commit'], sha)
        self.assertEqual(finalized['ci_status'], 'PASS')
        self.assertEqual(finalized['test_results'][13]['status'], 'PASS')
        self.assertNotIn('O14', finalized['open_gates'])


if __name__ == '__main__':
    unittest.main()
