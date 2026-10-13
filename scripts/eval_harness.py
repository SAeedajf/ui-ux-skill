#!/usr/bin/env python3
"""Validate and summarize model-evaluation records without calling a model."""
from __future__ import annotations

import argparse
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
    if len(matches) != 19 or len(ids) != 19:
        raise ValueError(f"expected 19 uniquely numbered quality scenarios, found {len(matches)}")
    return ids


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
        counts = Counter(row.get("status", "INVALID") for row in rows)
        parts.append(f"## {kind.title()}")
        parts.append("")
        parts.append(", ".join(f"{status}: {counts[status]}" for status in ("PASS", "FAIL", "BLOCKED", "NOT_RUN", "NEEDS_REVIEW") if counts[status]) or "No results recorded.")
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
