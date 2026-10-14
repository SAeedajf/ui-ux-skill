import json
import hashlib
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts.eval_harness import report, validate_domain_quality_refs, validate_domain_source_refs, validate_result_rows


class ResultValidationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "evals/evidence").mkdir(parents=True)
        self.trace = self.root / "evals/evidence/trace.jsonl"
        self.trace.write_text('{"type":"skill.invoked","skill":"ux-discovery","invocation_mode":"automatic"}\n', encoding="utf-8")
        trace_hash = hashlib.sha256(self.trace.read_bytes()).hexdigest()
        self.base = {
            "run_id": "run-001",
            "scenario_id": "activation-ux-discovery-positive",
            "status": "PASS",
            "commit_sha": "a" * 40,
            "timestamp_utc": "2026-10-13T10:00:00Z",
            "runner": "codex-cli",
            "model": "gpt-6-luna",
            "evidence": ["evals/evidence/trace.jsonl"],
            "trace": "evals/evidence/trace.jsonl",
            "checks": [{"name": "expected activation", "passed": True}],
            "invocation_mode": "automatic",
            "activated_skills": ["ux-discovery"],
            "activation_review": {
                "reviewer": "reviewer@example.invalid",
                "reviewed_at": "2026-10-13T10:10:00Z",
                "trace_sha256": trace_hash,
                "scope": "whole_trace",
                "evidence_summary": "The reviewed trace explicitly records automatic skill loading.",
                "observed_skill_events": [{"line": 1, "skill": "ux-discovery"}],
            },
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

    def test_rejects_activation_pass_with_arbitrary_unreviewed_trace(self):
        row = {**self.base, "activation_review": None}
        errors = validate_result_rows([row], {row["scenario_id"]}, self.root, "activation", {row["scenario_id"]: True})
        self.assertTrue(any("review" in error.lower() for error in errors))

    def test_rejects_activation_review_bound_to_different_trace(self):
        row = {**self.base, "activation_review": {**self.base["activation_review"], "trace_sha256": "0" * 64}}
        errors = validate_result_rows([row], {row["scenario_id"]}, self.root, "activation", {row["scenario_id"]: True})
        self.assertTrue(any("hash" in error.lower() for error in errors))

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

    def test_domain_map_requires_real_quality_ids_and_complete_coverage(self):
        domains = [
            {"domain": "layout", "eval_scenario": "quality-20"},
            {"domain": "source-grounding", "eval_scenario": "scenario_fake"},
        ]
        errors = validate_domain_quality_refs(domains, {"quality-20", "quality-22"})
        self.assertTrue(any("unknown quality scenario" in error for error in errors))
        self.assertTrue(any("does not reference" in error for error in errors))

    def test_domain_map_requires_every_source_to_be_mapped(self):
        domains = [{"domain": "interaction", "source_ids": "43;49"}]
        errors = validate_domain_source_refs(domains, {"43", "49", "48"})
        self.assertTrue(any("does not reference source IDs" in error for error in errors))

    def test_report_uses_latest_run_per_scenario(self):
        with patch("scripts.eval_harness.read_jsonl", return_value=[
            {"scenario_id": "quality-20", "status": "NOT_RUN", "timestamp_utc": "2026-10-13T23:51:00Z"},
            {"scenario_id": "quality-20", "status": "NEEDS_REVIEW", "timestamp_utc": "2026-10-13T23:53:56Z"},
        ]):
            rendered = report()
        self.assertIn("NEEDS_REVIEW: 1", rendered)
        self.assertIn("1 unique scenarios; 2 total run records", rendered)


if __name__ == "__main__":
    unittest.main()
