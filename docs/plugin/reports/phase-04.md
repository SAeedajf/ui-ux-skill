# Phase 04 — Operational Acceptance & Release Candidate

PHASE: 04

TITLE: Operational Acceptance & Release Candidate

STATUS: PARTIAL

REPOSITORY: https://github.com/SAeedajf/ui-ux-skill

BASE_COMMIT: `fea6e825306e7dec5162b0bb9fe37ac3129cb36c`

OUTPUT_COMMIT: `122e0ab5af176bc05e4e19a75bf01180cf2957f8` (Phase 04 acceptance tooling, evidence, and release-candidate workflow)

BRANCH: `codex/ui-ux-plugin-phase-04`

PULL_REQUEST: https://github.com/SAeedajf/ui-ux-skill/pull/14 (Draft; not merged)

PLUGIN_VERSION: `0.1.0`

PRIVATE_PLUGIN_ID: `plugins_6acfa25d79388191b9861545d52f6d03`

PRIVATE_PLUGIN_STATUS: `CREATED` — Plugin Creator metadata confirms release `pluginrel_6acfa26265f48191b194fe33780fbe70`, USER scope, PRIVATE visibility, version `0.1.0`. Installation in ChatGPT Work is unverified.

CODEX_INSTALLATION: PASS for isolated local Plugin-only and duplicate discovery; earlier Phase 02 GitHub marketplace installation evidence remains valid. Current CLI activation is blocked: isolated environments were logged out, and the normal CLI could not parse personal config. No setting was changed.

CODEX_ACTIVATION: BLOCKED — no authenticated model trace. Positive and negative smoke cases were not run; two-call maximum budget was set, zero used.

CHATGPT_INSTALLATION: BLOCKED — only creation metadata could be read. The available official metadata operation does not expose ChatGPT Work installation or picker discovery.

CHATGPT_ACTIVATION: NOT_RUN — owner-run procedure and T01–T07 evidence form are prepared.

DUPLICATE_SKILLS: NEEDS_REVIEW — Codex discovery shows 15 Plugin-prefixed Skills, 15 unprefixed legacy Skills, and 30 entries when both exist. Selection precedence is not observable without a model trace. Migration remains optional, backed up, and reversible.

PRACTICAL_REPAIR: BLOCKED — all five controlled fixture baseline failures were reproduced. No authenticated Agent repair, post-repair suite, or browser regression run was available; no manual change is represented as an Agent result.

BASELINE_COMPARISON: PARTIAL — one prior controlled pair is documented and its trace hashes match. No new pair was run; no statistical or general quality claim is made.

SECURITY_AUDIT: PASS for bounded automated checks of package schema/source integrity, secrets, paths, file types, symlinks, traversal, dangerous shell patterns, and targeted prompt-injection signatures. This is not a formal security audit.

LICENSE_AUDIT: NEEDS_REVIEW — the 124-entry registry remains 118 reviewed / 6 partially verified. Six partial records are listed in `security-and-provenance-review.md`; S20's direct-page access limit remains explicit. No legal clearance is claimed.

RELEASE_CANDIDATE: `RELEASE_CANDIDATE_READY` — private PR artifact contains the deterministic `0.1.0` ZIP and provenance sidecar. No version bump was justified because the plugin payload is byte-identical to the previous artifact.

ZIP_SHA256: `611b8eddaf74821dd2a1dd6a1d8ae576c32e20b4b23db12ec7021aa6ae634c7c`

CI_STATUS: PASS for output commit `122e0ab5af176bc05e4e19a75bf01180cf2957f8`; Phase 04 run `38594330226`. [RC ZIP and provenance artifact](https://github.com/SAeedajf/ui-ux-skill/actions/runs/38594330226/artifacts/11909456276). The report artifact is generated from the same workflow run. The successful baseline `main` run is `38590465251`.

TEST_COUNTS: 45 deterministic unit tests passed; 5/5 controlled fixture baseline failures reproduced as expected; 0 Codex model activation cases; 0 ChatGPT cases.

ACCEPTANCE_GATES: R01–R05 PASS; R06–R08 BLOCKED; R09 PASS (created metadata only); R10 BLOCKED; R11–R12 NOT_RUN; R13 PASS (bounded security checks); R14 NEEDS_REVIEW; R15–R18 PASS for package artifact, CI, report validation, and scope boundaries. Full criteria and all Phase 02/03 carry-forward gates are in `acceptance-gates.md`.

FILES_CHANGED:

- `.github/workflows/validate.yml` — validates Phase 04 report and uploads the RC ZIP/provenance and finalized report as CI artifacts.
- `schemas/phase-04-report.schema.json`, `scripts/validate_phase04_report.py`, `tests/test_phase04_report.py` — machine schema, semantic gate validator, and regression tests.
- `docs/plugin/acceptance-gates.md` — open Phase 02/03 gates and R01–R18 evidence/ownership.
- `docs/plugin/duplicate-skills-migration.md` — current isolated discovery counts and safe migration/rollback policy.
- `docs/plugin/chatgpt-personal-plugin.md`, `docs/plugin/chatgpt-test-cases.md` — owner steps for the exact existing private plugin; T01–T07 remain unrun.
- `docs/plugin/security-and-provenance-review.md`, `docs/plugin/publication-readiness.md` — bounded security/rights review and public submission checklist.
- `docs/plugin/reports/phase-04-evidence.md`, `docs/plugin/reports/phase-04.json`, this report — reproducible evidence, machine status, and handoff.

RISKS:

- Actual model selection, Skill file loading, and practical repair remain unverified without an authenticated Codex runtime.
- ChatGPT Plugin Creator metadata proves the private release exists but not that it is installed, discoverable, activated, or executed in Work.
- Duplicate Codex catalog discovery is confirmed, but precedence and selection are unknown.
- Automated provenance/security checks cannot settle legal rights or replace human review.
- Public listing identity/metadata and OpenAI Skill scans have not been completed; `PUBLIC_RELEASE_READY=NO`.

BLOCKERS:

- Codex CLI runtime is not currently usable for account-backed model tests: isolated environments are not logged in; the normal CLI reports `invalid type: boolean true, expected struct AgentRoleToml` in the user's existing config.
- ChatGPT Work install/discovery and T01–T07 require the plugin owner to operate the existing account/plugin.
- Rights clearance for the six partial source records requires a human rightsholder/maintainer.

MANUAL_ACTIONS:

1. After the owner decides to repair/authorize the existing CLI config, run the two unnamed Codex smoke prompts first; do not switch models or copy auth into temporary environments.
2. In an isolated authenticated project, run the fixture repair prompt, save the actual Agent trace and patch, run the five baseline checks plus regressions, and capture browser evidence if available.
3. In the intended ChatGPT Work account, inspect/install the exact existing plugin ID, run T01–T07 in fresh chats, and record the trace/UI limits. Do not upload a new release or change scope.
4. Have the human maintainer/rightsholder resolve S36, S50, S94, S100, S102, and S109; keep S20's direct-page limitation explicit.

REMAINING_WORK: Authenticated Codex activation/negative/repair; ChatGPT Work installation/discovery/execution; final human rights review; final Phase 04 PR CI and artifact check. Keep Claude, public submission, and publication out of scope.

NEXT_PHASE_HANDOFF:

```text
Continue UI/UX Pro Phase 04 only from https://github.com/SAeedajf/ui-ux-skill/pull/14 and branch codex/ui-ux-plugin-phase-04. Read docs/plugin/reports/phase-04.md, docs/plugin/reports/phase-04.json, docs/plugin/reports/phase-04-evidence.md, and docs/plugin/acceptance-gates.md first. Do not repeat completed package/CI setup. The current phase is PARTIAL: finish the authenticated Codex positive/negative smoke tests and Agent fixture repair only when Codex account/model access is available; test the exact existing private ChatGPT plugin plugins_6acfa25d79388191b9861545d52f6d03 without recreating/updating/sharing it; preserve all status distinctions and require trace evidence for activation. Keep the six partial source records and S20 access limitation explicit until human rights review. Do not test Claude, submit publicly, publish, merge, or change personal settings.
```
