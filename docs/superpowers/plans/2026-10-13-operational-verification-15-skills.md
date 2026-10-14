# Operational verification plan: 15 UI/UX Skills

## Goal
Move `ui-ux-skill` from a documented release candidate toward operational verification without overstating unsupported model or device evidence.

## Constraints
- Preserve exactly 15 Skills, 124 source rows (118 reviewed, 6 partial), and 14 domains.
- Codex only; do not run Claude Code tests.
- Use a model available in the Codex environment running the evaluation; the repository does not mandate a model. Record the selected model and host details. The 2026-10-13 Luna-only limitation is historical to that run.
- Do not change the user's persistent model configuration without permission. Back up before any approved edit.
- A model-driven PASS requires actual invocation trace and evidence. Distinguish `BLOCKED`, `NOT_RUN`, and `NEEDS_REVIEW`.
- Use standard-library tooling; do not add dependencies or rely on legacy OpenAI Evals.

## Work plan
1. Record environment/model/config diagnostics and the exact blocker; do not modify persistent configuration without explicit permission.
2. Add scenario IDs, separate immutable scenario definitions from JSONL run results, evidence, and summary logs. Validate IDs, statuses, commit SHAs, evidence paths, and PASS requirements.
3. Add regression tests for the harness first, then implement the deterministic CLI (`validate`, `report`, and result recording).
4. Build a small self-contained web fixture with product/hero/cards, responsive navigation, Persian RTL, form validation, loading/error states, and a deliberately broken accessibility state. Capture before evidence, repair it, and verify with a local browser and reproducible smoke checks where available.
5. Assess Android tooling and record executable checks or precise blockers. Do not let Android availability gate web work.
6. Record every activation/quality scenario's honest current state. Attempt model-driven runs only if a compatible, policy-authorized Codex runtime is available; otherwise BLOCK them with evidence. Compare baseline/skills-enabled only when both real runs are possible.
7. Add operational-readiness matrix, deterministic GitHub Actions, and regression/maturity reporting. Preserve historical records and source registry.
8. Review the branch, run all relevant deterministic validations, then push the authorized branch and open a PR.

## Interfaces
- Activation scenario `id` values are stable keys consumed by `evals/results/activation.jsonl`.
- Quality scenario IDs are stable `quality-01` through `quality-24`, derived from the numbered definitions and consumed by `evals/results/quality.jsonl`.
- Results refer to evidence by repository-relative path and to the exact 40-character commit SHA that was exercised.
- The operational-readiness report consumes validated results and may grant only the maturity level supported by evidence.
