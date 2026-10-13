# Running and recording Codex evaluations

Scenario definitions are kept separate from the evidence ledger:

- `evals/activation.jsonl` defines 30 positive/negative prompts.
- `evals/quality-scenarios.md` defines 19 quality cases and measurable acceptance checks.
- `evals/results/activation.jsonl` and `evals/results/quality.jsonl` store one record per run.
- `evals/evidence/` stores Codex JSONL traces and reviewer evidence.

## Commands

```sh
python3 scripts/run_codex_eval.py activation --model <codex-model-id> --dry-run
python3 scripts/run_codex_eval.py quality --model <codex-model-id> --dry-run
python3 scripts/run_codex_eval.py activation --model <codex-model-id> --scenario-id activation-forms-input-positive
python3 scripts/run_codex_eval.py quality --model <codex-model-id> --scenario-id quality-07
python3 scripts/eval_harness.py validate
python3 scripts/eval_harness.py report
```

Each non-dry run starts a separate ephemeral `codex exec --json` session with `--ignore-user-config`. The current Codex CLI still discovers Skills in the project; this switch bypasses the malformed user config and does not remove skill discovery. Every run saves stdout/stderr evidence and appends a result. Inspect and redact traces before publishing them; the scenarios are public and synthetic, but model output may include environment context. Failed CLI requests are `BLOCKED`; successful model responses are `NEEDS_REVIEW`. The runner never grants PASS automatically.

For activation PASS, a human reviewer must establish from the complete host trace that the expected Skill was selected automatically on the positive prompt and no Skill was selected on the negative prompt. The record must contain `invocation_mode: automatic`, the exact `activated_skills`, a non-empty JSONL trace, measurable checks, evidence, and a full commit SHA. It must also include `activation_review` with the reviewer, UTC review time, whole-trace scope, a concise evidence summary, the SHA-256 of the exact trace reviewed, and Skill-event line references for positive cases (none for negative cases). The validator checks the JSONL structure, path, hash binding, and line references; it cannot determine whether a cited host event truly means automatic Skill invocation. The human attestation remains necessary and must not be inferred from a plausible answer. Quality PASS requires measurable checks and evidence. `BLOCKED` and `NEEDS_REVIEW` never count as PASS.

The current environment's `gpt-6-luna` incompatibility is recorded in [operational readiness](operational-readiness.md). This repository intentionally does not select a fallback model automatically; use only a model authorized for the environment and evaluation.
