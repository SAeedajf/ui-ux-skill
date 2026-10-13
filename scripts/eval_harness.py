#!/usr/bin/env python3
"""Validate and summarize model-evaluation records without calling a model."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
VALID_STATUSES = {"PASS", "FAIL", "BLOCKED", "NOT_RUN", "NEEDS_REVIEW"}
SHA_RE = re.compile(r"^[0-9a-f]{40}$")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{number}: invalid JSON: {exc}") from exc
        if not isinstance(row, dict):
            raise ValueError(f"{path}:{number}: each JSONL line must be an object")
        rows.append(row)
    return rows


def validate_result_rows(
    rows: list[dict[str, Any]],
    scenario_ids: set[str],
    root: Path,
    kind: str,
    activation_expectations: dict[str, bool] | None = None,
) -> list[str]:
    errors: list[str] = []
    run_ids: set[str] = set()
    expectations = activation_expectations or {}
    for index, row in enumerate(rows, 1):
        label = f"{kind} result #{index}"
        required = ("run_id", "scenario_id", "status", "commit_sha", "timestamp_utc", "runner", "model", "evidence")
        for field in required:
            if field not in row:
                errors.append(f"{label}: missing {field}")
        run_id = row.get("run_id")
        if not isinstance(run_id, str) or not run_id.strip():
            errors.append(f"{label}: run_id must be a non-empty string")
        elif run_id in run_ids:
            errors.append(f"{label}: duplicate run_id {run_id}")
        else:
            run_ids.add(run_id)
        scenario_id = row.get("scenario_id")
        if scenario_id not in scenario_ids:
            errors.append(f"{label}: unknown scenario {scenario_id!r}")
        status = row.get("status")
        if status not in VALID_STATUSES:
            errors.append(f"{label}: invalid status {status!r}")
        if not isinstance(row.get("commit_sha"), str) or not SHA_RE.fullmatch(row.get("commit_sha", "")):
            errors.append(f"{label}: commit_sha must be a full 40-character lowercase SHA")
        for field in ("timestamp_utc", "runner", "model"):
            if not isinstance(row.get(field), str) or not row[field].strip():
                errors.append(f"{label}: {field} must be a non-empty string")
        evidence = row.get("evidence")
        if not isinstance(evidence, list) or any(not isinstance(item, str) for item in evidence):
            errors.append(f"{label}: evidence must be a list of repository-relative paths")
            evidence = []
        if status in {"PASS", "FAIL", "BLOCKED", "NEEDS_REVIEW"} and not evidence:
            errors.append(f"{label}: {status} requires evidence")
        for item in evidence:
            candidate = (root / item).resolve()
            if not candidate.is_relative_to(root.resolve()):
                errors.append(f"{label}: evidence path escapes repository: {item}")
            elif not candidate.is_file():
                errors.append(f"{label}: evidence file does not exist: {item}")
        if status == "BLOCKED" and not (isinstance(row.get("blocker"), str) and row["blocker"].strip()):
            errors.append(f"{label}: BLOCKED requires a blocker description")
        if status == "PASS":
            checks = row.get("checks")
            if not isinstance(checks, list) or not checks:
                errors.append(f"{label}: PASS requires at least one measurable check")
            elif any(not isinstance(check, dict) or check.get("passed") is not True for check in checks):
                errors.append(f"{label}: PASS contains a failed or malformed check")
        if kind == "activation" and status == "PASS":
            if row.get("invocation_mode") != "automatic":
                errors.append(f"{label}: activation PASS requires automatic invocation evidence")
            if not isinstance(row.get("trace"), str) or row.get("trace") not in evidence:
                errors.append(f"{label}: activation PASS requires a trace evidence path")
            trace_path = (root / row["trace"]).resolve() if isinstance(row.get("trace"), str) else None
            trace_lines: list[dict[str, Any]] = []
            if trace_path and trace_path.is_relative_to(root.resolve()) and trace_path.is_file():
                try:
                    trace_lines = [json.loads(line) for line in trace_path.read_text(encoding="utf-8").splitlines() if line.strip()]
                    if any(not isinstance(event, dict) for event in trace_lines):
                        errors.append(f"{label}: activation trace must contain JSON objects only")
                except (json.JSONDecodeError, OSError) as exc:
                    errors.append(f"{label}: activation trace is not readable JSONL: {exc}")
            if not trace_lines:
                errors.append(f"{label}: activation PASS requires a non-empty JSONL host trace")
            review = row.get("activation_review")
            if not isinstance(review, dict):
                errors.append(f"{label}: activation PASS requires a human activation_review attestation")
            else:
                for field in ("reviewer", "reviewed_at", "evidence_summary"):
                    if not isinstance(review.get(field), str) or not review[field].strip():
                        errors.append(f"{label}: activation_review requires non-empty {field}")
                if not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", str(review.get("reviewed_at", ""))):
                    errors.append(f"{label}: activation_review.reviewed_at must be a UTC timestamp")
                if review.get("scope") != "whole_trace":
                    errors.append(f"{label}: activation_review must attest to whole_trace")
                expected_hash = hashlib.sha256(trace_path.read_bytes()).hexdigest() if trace_path and trace_path.is_file() else None
                if review.get("trace_sha256") != expected_hash:
                    errors.append(f"{label}: activation_review trace hash does not match the reviewed trace")
                observed = review.get("observed_skill_events")
                if not isinstance(observed, list) or any(not isinstance(event, dict) for event in observed):
                    errors.append(f"{label}: activation_review.observed_skill_events must be a list of event references")
                    observed = []
                for ref in observed:
                    line_number = ref.get("line")
                    if not isinstance(line_number, int) or line_number < 1 or line_number > len(trace_lines):
                        errors.append(f"{label}: activation_review references a missing trace line")
                    if not isinstance(ref.get("skill"), str) or not ref["skill"].strip():
                        errors.append(f"{label}: activation_review event reference requires a skill name")
                if scenario_id in expectations:
                    target_skill = scenario_id.removeprefix("activation-").rsplit("-", 1)[0]
                    if expectations[scenario_id] and not any(ref.get("skill") == target_skill for ref in observed):
                        errors.append(f"{label}: positive activation review must reference the expected Skill event")
                    if not expectations[scenario_id] and observed:
                        errors.append(f"{label}: negative activation review must attest that the whole trace has no Skill events")
            activated = row.get("activated_skills")
            if not isinstance(activated, list) or any(not isinstance(name, str) for name in activated):
                errors.append(f"{label}: activation PASS requires activated_skills as a string list")
            elif scenario_id in expectations:
                expected_activation = expectations[scenario_id]
                target_skill = scenario_id.removeprefix("activation-").rsplit("-", 1)[0]
                if expected_activation and target_skill not in activated:
                    errors.append(f"{label}: positive scenario PASS lacks expected Skill {target_skill}")
                if not expected_activation and activated:
                    errors.append(f"{label}: negative scenario PASS unexpectedly activated Skills")
        if kind == "quality" and status == "PASS":
            if not isinstance(row.get("checks"), list) or not row["checks"]:
                errors.append(f"{label}: quality PASS requires measurable acceptance checks")
    return errors


def activation_definitions() -> tuple[set[str], dict[str, bool]]:
    rows = read_jsonl(ROOT / "evals/activation.jsonl")
    ids: set[str] = set()
    expectations: dict[str, bool] = {}
    for index, row in enumerate(rows, 1):
        sid = row.get("id")
        if not isinstance(sid, str) or not sid:
            raise ValueError(f"activation definition #{index}: missing id")
        if sid in ids:
            raise ValueError(f"activation definition: duplicate id {sid}")
        ids.add(sid)
        if row.get("expected") not in {"activate", "do_not_activate"}:
            raise ValueError(f"activation definition {sid}: invalid expected value")
        expectations[sid] = row["expected"] == "activate"
        if row.get("case") not in {"positive", "negative"} or not row.get("skill") or not row.get("prompt"):
            raise ValueError(f"activation definition {sid}: missing skill, case, or prompt")
        if row["case"] == "positive" and row["expected"] != "activate":
            raise ValueError(f"activation definition {sid}: positive case must expect activate")
        if row["case"] == "negative" and row["expected"] != "do_not_activate":
            raise ValueError(f"activation definition {sid}: negative case must expect do_not_activate")
    return ids, expectations


def quality_definitions() -> set[str]:
    text = (ROOT / "evals/quality-scenarios.md").read_text(encoding="utf-8")
    matches = re.findall(r"^(\d+)\. \*\*(.+?)\*\*", text, re.M)
    ids = {f"quality-{int(number):02d}" for number, _ in matches}
    expected_numbers = [str(number) for number in range(1, len(matches) + 1)]
    actual_numbers = [number for number, _ in matches]
    if not matches or len(ids) != len(matches) or actual_numbers != expected_numbers:
        raise ValueError("quality scenarios must have unique, sequential numbering starting at 1")
    return ids


def validate_domain_quality_refs(domains: list[dict[str, str]], quality_ids: set[str]) -> list[str]:
    errors: list[str] = []
    referenced: set[str] = set()
    for row in domains:
        domain = row.get("domain", "<unknown>")
        refs = [item.strip() for item in row.get("eval_scenario", "").split(";") if item.strip()]
        if not refs:
            errors.append(f"{domain}: needs at least one quality scenario ID")
        for scenario_id in refs:
            if scenario_id not in quality_ids:
                errors.append(f"{domain}: unknown quality scenario {scenario_id!r}")
            referenced.add(scenario_id)
    missing = quality_ids - referenced
    if missing:
        errors.append(f"domain coverage does not reference: {', '.join(sorted(missing))}")
    return errors


def validate_all() -> list[str]:
    errors: list[str] = []
    try:
        activation_ids, expectations = activation_definitions()
        quality_ids = quality_definitions()
    except (ValueError, OSError) as exc:
        return [str(exc)]
    for kind, ids in (("activation", activation_ids), ("quality", quality_ids)):
        path = ROOT / f"evals/results/{kind}.jsonl"
        try:
            rows = read_jsonl(path)
        except (ValueError, OSError) as exc:
            errors.append(str(exc))
            continue
        errors.extend(validate_result_rows(rows, ids, ROOT, kind, expectations if kind == "activation" else None))
        result_ids = [row.get("scenario_id") for row in rows]
        missing = ids - set(result_ids)
        if missing:
            errors.append(f"{kind}: missing result rows for {', '.join(sorted(missing))}")
    return errors


def report() -> str:
    parts = ["# Evaluation status report", "", "Scenario definitions are not execution evidence. Statuses below come from `evals/results/`.", ""]
    for kind in ("activation", "quality"):
        rows = read_jsonl(ROOT / f"evals/results/{kind}.jsonl")
        latest: dict[str, dict[str, Any]] = {}
        for row in rows:
            scenario_id = row.get("scenario_id")
            if not isinstance(scenario_id, str):
                continue
            if scenario_id not in latest or str(row.get("timestamp_utc", "")) >= str(latest[scenario_id].get("timestamp_utc", "")):
                latest[scenario_id] = row
        counts = Counter(row.get("status", "INVALID") for row in latest.values())
        parts.append(f"## {kind.title()}")
        parts.append("")
        parts.append(", ".join(f"{status}: {counts[status]}" for status in ("PASS", "FAIL", "BLOCKED", "NOT_RUN", "NEEDS_REVIEW") if counts[status]) or "No results recorded.")
        parts.append(f"Latest recorded state per scenario ({len(latest)} unique scenarios; {len(rows)} total run records).")
        parts.append("")
    return "\n".join(parts)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("validate", "report"), nargs="?", default="validate")
    args = parser.parse_args()
    if args.command == "report":
        print(report())
        return 0
    errors = validate_all()
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1
    print("OK: result ledgers match scenario definitions; statuses and evidence paths are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
