import unittest

from scripts.validate_phase04_report import finalize_report, validate_report


def sample_report():
    gates = []
    for number in range(1, 19):
        gate_id = f'R{number:02d}'
        status = 'BLOCKED' if gate_id in {'R06', 'R07', 'R08', 'R10', 'R11', 'R12'} else 'PASS'
        gates.append({
            'id': gate_id,
            'status': status,
            'test_type': 'model_activation' if gate_id in {'R06', 'R07'} else 'deterministic',
            'executed_at': '2026-10-14T00:00:00Z',
            'method': 'isolated Codex CLI probe',
            'evidence': f'docs/plugin/reports/phase-04-evidence.md#{gate_id.lower()}',
            'reason': 'No authenticated runtime trace.' if status == 'BLOCKED' else 'Verified in isolated CI/local checks.',
        })
    return {
        'phase': '04',
        'status': 'PARTIAL',
        'base_commit': 'fea6e825306e7dec5162b0bb9fe37ac3129cb36c',
        'output_commit': 'fea6e825306e7dec5162b0bb9fe37ac3129cb36c',
        'plugin_version': '0.1.0',
        'skills_count': 15,
        'test_results': gates,
        'open_gates': [g['id'] for g in gates if g['status'] != 'PASS'],
        'blocked_gates': [g['id'] for g in gates if g['status'] == 'BLOCKED'],
        'ci_status': 'PENDING',
        'artifact_url': None,
        'artifact_sha256': None,
        'risks': [],
        'manual_actions': [],
        'next_phase': 'Owner-run authenticated Codex and private ChatGPT acceptance tests.',
    }


class Phase04ReportValidationTests(unittest.TestCase):
    def test_accepts_complete_report_with_open_model_gates(self):
        self.assertEqual(validate_report(sample_report()), [])

    def test_rejects_open_gate_index_that_disagrees_with_gate_statuses(self):
        report = sample_report()
        report['open_gates'].remove('R06')
        self.assertTrue(any('open_gates' in error for error in validate_report(report)))

    def test_rejects_model_gate_marked_pass_without_trace_evidence(self):
        report = sample_report()
        gate = next(g for g in report['test_results'] if g['id'] == 'R06')
        gate.update(status='PASS', evidence='')
        report['open_gates'].remove('R06')
        report['blocked_gates'].remove('R06')
        self.assertTrue(any('model' in error.lower() for error in validate_report(report)))

    def test_rejects_model_gate_pointing_to_a_missing_trace_file(self):
        report = sample_report()
        gate = next(g for g in report['test_results'] if g['id'] == 'R06')
        gate.update(status='PASS', evidence='evals/evidence/codex-runs/not-a-real-trace.jsonl')
        report['open_gates'].remove('R06')
        report['blocked_gates'].remove('R06')
        self.assertTrue(any('does not exist' in error for error in validate_report(report)))

    def test_finalizes_artifact_provenance_from_the_actual_ci_run(self):
        report = sample_report()
        finalized = finalize_report(
            report,
            artifact_url='https://github.com/SAeedajf/ui-ux-skill/actions/runs/12345',
            artifact_sha256='b' * 64,
        )
        self.assertEqual(finalized['output_commit'], report['output_commit'])
        self.assertEqual(finalized['artifact_url'], 'https://github.com/SAeedajf/ui-ux-skill/actions/runs/12345')
        self.assertEqual(finalized['artifact_sha256'], 'b' * 64)


if __name__ == '__main__':
    unittest.main()
