import copy
import unittest

from scripts.validate_phase05b_report import finalize_ci_report, validate_report


def sample_report():
    return {
        'phase': '05-B',
        'title': 'Authenticated Runtime Acceptance & Real Agent Repair',
        'status': 'BLOCKED',
        'repository': 'https://github.com/SAeedajf/ui-ux-skill',
        'base_commit': '5a18b097ade439281e9d39b5c6476e84eb2e6ab0',
        'output_commit': '5a18b097ade439281e9d39b5c6476e84eb2e6ab0',
        'branch': 'codex/ui-ux-plugin-phase-05b',
        'pull_request': None,
        'codex_cli': {'path': '/home/<user>/codex', 'version': '0.153.4', 'config_model': 'gpt-6-luna', 'account_usage_allowed': True},
        'model_id': 'gpt-6-luna', 'auth_method': 'ChatGPT', 'auth_status': 'Authenticated; request rejected before model execution.',
        'plugin_install_method': 'Temporary installation; rollback verified.',
        'plugin_source': {'plugin_id': 'ui-ux-pro@ui-ux-pro-marketplace', 'version': '0.1.0', 'source': 'local worktree', 'manifest_sha256': '1456bc5bf0f206ca92554b44b2377048259c209848ed64ef6c31e5b40290ca54', 'archive_sha256': '611b8eddaf74821dd2a1dd6a1d8ae576c32e20b4b23db12ec7021aa6ae634c7c'},
        'plugin_discovery': {'status': 'PASS', 'plugin_skill_count': 15, 'plugin_namespace_count': 15, 'legacy_overlap_count': 8, 'rollback_verified': True},
        'positive_smoke': {'status': 'BLOCKED', 'attempted': True, 'accepted': False, 'trace_evidence': 'docs/plugin/reports/evidence/phase-05b-positive-blocked.jsonl', 'reason': 'Unsupported model.'},
        'negative_smoke': {'status': 'NOT_RUN', 'attempted': False, 'accepted': False, 'trace_evidence': None, 'reason': 'Stopped after the model compatibility error.'},
        'skills_actually_loaded': [],
        'fixture_baseline': {'status': 'EXPECTED_FAILURES', 'tests_run': 5, 'expected_failures': 5, 'evidence': 'docs/plugin/reports/evidence/phase-05b-fixture-baseline.txt'},
        'agent_authored_diff': {'created': False, 'files': [], 'diff_evidence': None},
        'repair_trace_evidence': None,
        'fixture_after': {'status': 'NOT_RUN', 'tests_run': 0, 'passed': 0},
        'regression_results': 'NOT_RUN', 'browser_results': 'NOT_RUN', 'duplicate_skill_findings': 'Selection unverified.',
        'chatgpt_plugin_status': 'Existing private plugin unchanged.', 'chatgpt_runtime_status': 'NOT_RUN',
        'source_rights_status': 'Unchanged unresolved.',
        'model_call_count': {'attempted': 1, 'accepted': 0, 'positive': 1, 'negative': 0, 'repair': 0, 'retry': 0},
        'ci_status': 'PENDING', 'ci_run_url': None, 'ci_output_commit': None, 'ci_checked_at': None, 'test_count': 5,
        'evidence_paths': ['docs/plugin/reports/phase-05b-evidence.md', 'docs/plugin/reports/evidence/phase-05b-positive-blocked.jsonl', 'docs/plugin/reports/evidence/phase-05b-fixture-baseline.txt'],
        'blockers': ['The selected model is not supported by this ChatGPT CLI account.'],
        'owner_action_required': ['Choose an account-supported CLI model.'],
        'next_phase_recommendation': 'Continue Phase 05-B after model compatibility is resolved.'
    }


class Phase05BReportTests(unittest.TestCase):
    def test_current_blocked_report_contract_is_valid(self):
        self.assertEqual(validate_report(sample_report()), [])

    def test_rejects_positive_pass_without_a_successful_plugin_skill_trace(self):
        report = sample_report()
        report['positive_smoke'].update(status='PASS', accepted=True)
        self.assertTrue(any('completed model trace' in error for error in validate_report(report)))

    def test_rejects_overall_pass_without_agent_diff_and_after_tests(self):
        report = sample_report()
        report['status'] = 'PASS'
        report['positive_smoke'].update(status='PASS', accepted=True)
        report['negative_smoke'].update(status='PASS', attempted=True, accepted=True, trace_evidence='docs/plugin/reports/evidence/phase-05b-positive-blocked.jsonl')
        self.assertTrue(any('Agent-authored diff' in error for error in validate_report(report)))

    def test_reconciles_call_budget_and_disallows_more_than_one_retry(self):
        report = sample_report()
        report['model_call_count'].update(attempted=1, retry=1)
        errors = validate_report(report)
        self.assertTrue(any('attempted calls must reconcile' in error for error in errors))
        report['model_call_count'].update(attempted=3, retry=2)
        errors = validate_report(report)
        self.assertTrue(any(error.startswith('schema:') for error in errors))

    def test_ci_finalizer_records_exact_run_and_commit(self):
        finalized = finalize_ci_report(sample_report(), 'https://github.com/SAeedajf/ui-ux-skill/actions/runs/123', '1' * 40)
        self.assertEqual(finalized['ci_status'], 'PASS')
        self.assertEqual(finalized['ci_output_commit'], '1' * 40)
        self.assertEqual(validate_report(finalized), [])


if __name__ == '__main__':
    unittest.main()
