# UI/UX Pro acceptance gates

Updated: 2026-10-14. Statuses below separate discovery and creation from installation and execution. `PASS` requires the specific evidence named in the gate; a package check cannot pass a model-runtime gate.

## Status meanings

`CREATED` means a plugin record/release exists. `INSTALLED` means the target host confirms installation. `DISCOVERED` means the plugin or Skills appear in that host's picker/input inventory. `ACTIVATED` means a trace shows the model selected the relevant Skill for the request. `EXECUTED` means a run shows the Skill file was loaded and applied. `VERIFIED` means independent result checks passed. These are separate lifecycle facts, not synonyms.

## Open Phase 02 and Phase 03 gates

| Gate | Status | Success criteria | Evidence required / current evidence | Responsible runner |
|---|---|---|---|---|
| G07 — Duplicate Skill selection | NEEDS_REVIEW | One intended source wins or migration is validated by an authenticated selection trace; no ambiguous duplicate selection remains. | Phase 04 isolated discovery shows 15 Plugin + 15 Legacy entries and doubled catalog size, but no model selection or precedence. See `reports/phase-04-evidence.md`. | Repository maintainer + authenticated Codex owner |
| G09 — Positive Codex activation | BLOCKED | Unnamed, relevant prompt selects the expected Skill from the installed plugin; trace points to plugin cache and `SKILL.md`; response is reviewed. | No authenticated Codex CLI session. Current local CLI cannot parse its config; disposable CLI reports `Not logged in`. | Authenticated Codex owner |
| G10 — Negative Codex activation | BLOCKED | Unrelated Python prompt does not select/load a UI/UX Skill, proven by trace. | No model trace; discovery metadata alone is not this test. | Authenticated Codex owner |
| G11 — Practical repair | BLOCKED | The five seeded fixture failures reproduce; an Agent changes source; all original checks pass; regression and browser/DOM states are reviewed. | Five baseline fixture tests fail as expected. No Agent repair run was possible; no hand edit is counted. | Authenticated Codex owner, with repository maintainer reviewing diff |
| C09 — Private ChatGPT installation | BLOCKED | Existing plugin ID is installed in the intended ChatGPT Work surface and shown as installed. | Plugin Creator read-only metadata confirms `CREATED`, USER scope, PRIVATE, v0.1.0; there is no installation-state API. | Plugin owner |
| C10 — ChatGPT discovery | BLOCKED | Existing plugin is visible in the Work plugin picker in a fresh conversation. | No authenticated conversation or picker was accessed. | Plugin owner |
| C11 — Positive ChatGPT test | NOT_RUN | T01 explicit invocation succeeds; T02 relevant unselected test has trace-backed activation where available. | Owner-run cases and evidence form in `chatgpt-test-cases.md`. | Plugin owner |
| C12 — Negative ChatGPT test | NOT_RUN | T07 unrelated Python request does not activate UI/UX Pro. | Owner-run case and trace/UI record in `chatgpt-test-cases.md`. | Plugin owner |
| C13 — ChatGPT duplicate Skills | NEEDS_REVIEW | Plugin and legacy inventories and actual selection/precedence are observed in ChatGPT. | Codex duplicate results do not transfer to ChatGPT; no ChatGPT Skill inventory/trace is available here. | Plugin owner |

## Phase 04 release and operational gates

| Gate | Status | Success criteria | Evidence | Responsible runner |
|---|---|---|---|---|
| R01 | PASS | Source package builds deterministically and passes the vendored schema validator. | `scripts/validate-plugin.py`, `scripts/build-plugin.py --check --archive`, `reports/phase-04-evidence.md`. | CI + maintainer |
| R02 | PASS | Exactly 15 canonical Skills remain under `.agents/skills/`. | Repository validator and package inventory. | CI |
| R03 | PASS | Internal references resolve and source registry validates. | `validate_repo.py`, package validator, evidence report. | CI |
| R04 | PASS | Codex GitHub installation remains reproducible. | Phase 02 isolated install and byte/hash comparison; current plugin source unchanged. | Repository maintainer |
| R05 | PASS | Duplicate policy is safe, reversible, and explicitly opt-in. | Migration guide and Phase 04 discovery matrix. | Repository maintainer |
| R06 | BLOCKED | Positive automatic Skill choice is proven from an authenticated Codex trace and plugin cache path. | No authenticated model trace. | Authenticated Codex owner |
| R07 | BLOCKED | Negative Codex prompt has no unrelated Skill selection, shown by trace. | No authenticated model trace. | Authenticated Codex owner |
| R08 | BLOCKED | Agent-authored repair, tests, and regressions all pass. | Baseline only; Agent was not run. | Authenticated Codex owner + maintainer |
| R09 | PASS | Exact private plugin ID/release metadata exists with USER scope and PRIVATE visibility. | Plugin Creator metadata read-only response in evidence report. This is `CREATED`, not `INSTALLED`. | Plugin Creator connector |
| R10 | BLOCKED | Existing plugin is installed and discoverable in the intended ChatGPT Work surface. | No installation/discovery surface or read API. | Plugin owner |
| R11 | NOT_RUN | Positive ChatGPT invocation/activation evidence recorded. | No ChatGPT test run. | Plugin owner |
| R12 | NOT_RUN | Negative ChatGPT test confirms no irrelevant activation. | No ChatGPT test run. | Plugin owner |
| R13 | PASS | Package security checks cover secrets, file types, links, symlinks, traversal, manifest safety, and instruction patterns. | Package validator, inventory, signature scan; limits documented in security review. | CI + maintainer |
| R14 | NEEDS_REVIEW | Human rights/provenance review resolves the six partial entries and registry inconsistency. | `security-and-provenance-review.md`; no legal opinion claimed. | Human maintainer/rightsholder |
| R15 | PASS | Traceable 0.1.0 Release Candidate ZIP and SHA-256 are produced without changing package content/version. | CI artifact and provenance sidecar in final report. | CI |
| R16 | PASS | GitHub Actions run on output commit succeeds. | Run `38594330226` passed; see the direct CI run and RC artifact link in `reports/phase-04.md`. | GitHub Actions |
| R17 | PASS | Machine report passes schema and semantic validation; open/blocked lists match gate details. | `validate_phase04_report.py` and tests. | CI |
| R18 | PASS | No personal settings, plugin state, ChatGPT release, public listing, Claude, or external paid account is changed. | Worktree diff and evidence boundaries. | Repository maintainer |

The overall phase remains `PARTIAL` unless R06–R12 are completed with the operational evidence required above. A package `RELEASE_CANDIDATE_READY` status is distinct from `PUBLIC_RELEASE_READY` and `OPERATIONALLY_VERIFIED`.
