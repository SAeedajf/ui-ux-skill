import json
import tempfile
import unittest
from pathlib import Path

from scripts.eval_harness import validate_result_rows


class ResultValidationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "evals/evidence").mkdir(parents=True)
        (self.root / "evals/evidence/trace.json").write_text("{}", encoding="utf-8")
        self.base = {
            "run_id": "run-001",
            "scenario_id": "activation-ux-discovery-positive",
            "status": "PASS",
            "commit_sha": "a" * 40,
            "timestamp_utc": "2026-10-13T10:00:00Z",
            "runner": "codex-cli",
            "model": "gpt-6-luna",
            "evidence": ["evals/evidence/trace.json"],
            "trace": "evals/evidence/trace.json",
            "checks": [{"name": "expected activation", "passed": True}],
            "invocation_mode": "automatic",
            "activated_skills": ["ux-discovery"],
        }

    def tearDown(self):
        self.tmp.cleanup()

    def test_accepts_evidenced_automatic_positive_activation(self):
        errors = validate_result_rows([self.base], {"activation-ux-discovery-positive"}, self.root, "activation", {"activation-ux-discovery-positive": True})
        self.assertEqual(errors, [])

    def test_rejects_pass_without_evidence(self):
        row = {**self.base, "evidence": []}
        errors = validate_result_rows([row], {row["scenario_id"]}, self.root, "activation", {row["scenario_id"]: True})
        self.assertTrue(any("evidence" in error.lower() for error in errors))

    def test_rejects_manual_activation_marked_pass(self):
        row = {**self.base, "invocation_mode": "manual"}
        errors = validate_result_rows([row], {row["scenario_id"]}, self.root, "activation", {row["scenario_id"]: True})
        self.assertTrue(any("automatic" in error.lower() for error in errors))

    def test_rejects_negative_activation_that_invoked_skill(self):
        sid = "activation-ux-discovery-negative"
        row = {**self.base, "scenario_id": sid}
        errors = validate_result_rows([row], {sid}, self.root, "activation", {sid: False})
        self.assertTrue(any("unexpected" in error.lower() or "negative" in error.lower() for error in errors))

    def test_rejects_unknown_status_and_missing_commit(self):
        row = {**self.base, "status": "MAYBE", "commit_sha": "c070660"}
        errors = validate_result_rows([row], {row["scenario_id"]}, self.root, "activation", {row["scenario_id"]: True})
        self.assertGreaterEqual(len(errors), 2)

    def test_rejects_duplicate_run_id_and_unknown_scenario(self):
        row = {**self.base, "scenario_id": "missing-case"}
        errors = validate_result_rows([row, row], {self.base["scenario_id"]}, self.root, "activation", {self.base["scenario_id"]: True})
        self.assertTrue(any("duplicate" in error.lower() for error in errors))
        self.assertTrue(any("unknown scenario" in error.lower() for error in errors))

    def test_rejects_missing_evidence_file_and_false_quality_check(self):
        row = {**self.base, "evidence": ["evals/evidence/absent.json"], "checks": [{"name": "grounded", "passed": False}]}
        errors = validate_result_rows([row], {row["scenario_id"]}, self.root, "quality", {})
        self.assertTrue(any("does not exist" in error.lower() for error in errors))
        self.assertTrue(any("failed or malformed check" in error.lower() for error in errors))


if __name__ == "__main__":
    unittest.main()
