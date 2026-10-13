#!/usr/bin/env python3
"""Run isolated Codex activation or quality prompts and preserve JSONL traces."""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.eval_harness import activation_definitions, quality_definitions, read_jsonl


def load_scenarios(kind: str) -> list[dict]:
    if kind == "activation":
        return read_jsonl(ROOT / "evals/activation.jsonl")
    text = (ROOT / "evals/quality-scenarios.md").read_text(encoding="utf-8")
    scenarios = []
    for number, title, description in re.findall(r"^(\d+)\. \*\*(.+?):\*\* (.+)$", text, re.M):
        scenarios.append({"id": f"quality-{int(number):02d}", "title": title, "prompt": f"Respond to this UI/UX scenario as you would to a user: {description}"})
    if {row["id"] for row in scenarios} != quality_definitions():
        raise ValueError("Could not map every quality definition to a runnable prompt")
    return scenarios


def run_scenario(kind: str, scenario: dict, model: str, codex: str = "codex") -> tuple[dict, str, str]:
    run_id = f"{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}-{scenario['id']}"
    prompt = scenario.get("prompt") or scenario.get("description")
    command = [codex, "exec", "--ignore-user-config", "--ephemeral", "--json", "--sandbox", "read-only", "--model", model, "-C", str(ROOT), prompt]
    try:
        completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, timeout=180, check=False)
        stdout, stderr, code = completed.stdout, completed.stderr, completed.returncode
    except (OSError, subprocess.TimeoutExpired) as exc:
        stdout, stderr, code = "", str(exc), 1
    trace_path = ROOT / f"evals/evidence/codex-runs/{run_id}.jsonl"
    stderr_path = ROOT / f"evals/evidence/codex-runs/{run_id}.stderr.txt"
    trace_path.parent.mkdir(parents=True, exist_ok=True)
    trace_path.write_text(stdout, encoding="utf-8")
    stderr_path.write_text(stderr, encoding="utf-8")
    failed_event = False
    failure_message = ""
    for line in stdout.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get("type") in {"error", "turn.failed"}:
            failed_event = True
            failure_message = str(event.get("message") or event.get("error", {}).get("message", "Codex run failed"))
            break
    blocked = code != 0 or failed_event
    result = {
        "run_id": run_id,
        "scenario_id": scenario["id"],
        "status": "BLOCKED" if blocked else "NEEDS_REVIEW",
        "commit_sha": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "runner": "Codex CLI isolated exec",
        "model": model,
        "evidence": [str(trace_path.relative_to(ROOT)), str(stderr_path.relative_to(ROOT))],
        "invocation_mode": "unverified",
        "activated_skills": [],
    }
    if blocked:
        result["blocker"] = failure_message or stderr.strip()[-1200:] or f"Codex exited with status {code}"
    else:
        result["review_note"] = "Response and automatic Skill invocation trace require independent review; runner never marks PASS."
    return result, stdout, stderr


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kind", choices=("activation", "quality"))
    parser.add_argument("--scenario-id", action="append", help="Run only the selected scenario ID; repeat to select more than one")
    parser.add_argument("--model", required=True, help="Codex model ID authorized for this evaluation")
    parser.add_argument("--dry-run", action="store_true", help="List selected IDs without starting model sessions")
    args = parser.parse_args()
    try:
        scenarios = load_scenarios(args.kind)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    requested = set(args.scenario_id or [])
    unknown = requested - {row["id"] for row in scenarios}
    if unknown:
        parser.error(f"unknown scenario IDs: {', '.join(sorted(unknown))}")
    selected = [row for row in scenarios if not requested or row["id"] in requested]
    if args.dry_run:
        print("\n".join(row["id"] for row in selected))
        return 0
    result_path = ROOT / f"evals/results/{args.kind}.jsonl"
    for scenario in selected:
        result, _, _ = run_scenario(args.kind, scenario, args.model)
        with result_path.open("a", encoding="utf-8") as stream:
            stream.write(json.dumps(result, ensure_ascii=False, separators=(",", ":")) + "\n")
        print(f"{scenario['id']}: {result['status']}")
        if result["status"] == "BLOCKED":
            print(result["blocker"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
