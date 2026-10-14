# Phase 02 — Codex Marketplace Installation & Runtime Verification

PHASE: 02

TITLE: Codex Marketplace Installation & Runtime Verification

STATUS: PARTIAL

REPOSITORY: https://github.com/SAeedajf/ui-ux-skill

BASE_COMMIT: `495d29922e8e3e9782d1a95b02d15b97e9e2cc90`

OUTPUT_COMMIT: `8e3b6cba1d3542cee01e6d48c618700fc18c23e9` (implementation; report and evidence are added in the following documentation commit)

BRANCH: `codex/ui-ux-plugin-phase-02`

PULL_REQUEST: https://github.com/SAeedajf/ui-ux-skill/pull/12 (draft)

PLUGIN_VERSION: `0.1.0`

MARKETPLACE_NAME: `ui-ux-pro-marketplace`

CODEX_CLI_VERSION: `codex-cli 0.144.5`

ISOLATION_METHOD: Separate disposable `HOME`, `CODEX_HOME`, and empty project directories under `/tmp`; local and GitHub installation runs cleaned up after evidence collection. No credentials were copied.

LOCAL_MARKETPLACE: PASS — repository-scoped catalog added, listed, and resolved to `plugins/ui-ux-pro` using the real CLI.

GITHUB_MARKETPLACE: PASS — added from `SAeedajf/ui-ux-skill` pinned to branch `codex/ui-ux-plugin-phase-02`, resolving commit `8e3b6cba1d3542cee01e6d48c618700fc18c23e9`.

PLUGIN_INSTALLATION: PASS — local and GitHub installations both appeared installed and enabled. GitHub cache path was `/tmp/uiux-phase02-github-OSEpmB/codex-home/plugins/cache/ui-ux-pro-marketplace/ui-ux-pro/local`.

SKILL_DISCOVERY: PASS — `codex debug prompt-input` showed exactly 15 `ui-ux-pro:<skill-id>` entries from the installed cache in a blank project. This is discovery evidence, not model activation.

DUPLICATE_SKILLS: NEEDS_REVIEW — Plugin Only showed 15 plugin-prefixed entries; Legacy Only showed 15 unprefixed entries; Both showed both sets (15 + 15). No precedence or model selection behavior was observable without a model trace. Migration and reversible rollback guidance is in `docs/plugin/duplicate-skills-migration.md`.

REFERENCE_VALIDATION: PASS — 18 packaged `references/*.md` files are present; validator checks nested Markdown references relative to each source file. GitHub installed cache matched all 35 source package files by SHA-256 with no missing or mismatched source files.

ACTIVATION_TESTS: BLOCKED — clean isolated environment returned `Not logged in`; positive, negative, and full 30-case activation traces were not run. Existing evaluation data was not reinterpreted as fresh Phase 02 evidence.

PRACTICAL_IMPLEMENTATION: BLOCKED — no authenticated model was available to run an agent against the RTL fixture. The isolated fixture's baseline suite showed 5 expected failures; no manual repair is represented as model output.

REGRESSION_TESTS: PASS — package build, package and marketplace validators, repository validator, and all 40 unit tests passed locally. Model-based activation/repair is excluded from public CI.

ROLLBACK: PASS — plugin and marketplace removal commands were run in both local and GitHub disposable environments. Follow-up plugin and marketplace lists were empty. No personal installation was targeted.

CI_STATUS: PASS — GitHub Actions run `38586399158` completed successfully for implementation SHA `8e3b6cba1d3542cee01e6d48c618700fc18c23e9`.

TEST_EVIDENCE: `docs/plugin/reports/phase-02-evidence.md`; disposable command outputs and path/hash inspection described there. Local CLI version and command syntax are captured in the report.

FILES_CHANGED:

- `.agents/plugins/marketplace.json` — repository marketplace catalog.
- `.github/workflows/validate.yml` — CI invokes marketplace validation.
- `plugins/ui-ux-pro/plugin.json`, `scripts/plugin_packaging.py` — portable manifest uses the fixed `skills/` directory; validation covers nested relative references.
- `scripts/validate_marketplace.py`, `tests/test_marketplace.py` — catalog validator and regressions.
- `tests/fixtures/phase02-rtl-shop/` — isolated Persian RTL repair fixture and baseline tests.
- `docs/plugin/codex-installation.md`, `docs/plugin/marketplace-verification.md`, `docs/plugin/duplicate-skills-migration.md`, `docs/plugin/runtime-testing.md` — user guidance and limitations.
- `docs/plugin/reports/phase-02*.md` — report and evidence.
- `docs/superpowers/plans/2026-10-14-phase-02.md` — execution plan.

RISKS:

- Codex CLI behavior was verified on version `0.144.5`; other versions may differ.
- When both plugin and legacy copies are discoverable, both namespaces are loaded. Precedence and context/selection effects remain unmeasured.
- The `/tmp` CLI warning about PATH aliases was non-blocking; tests used commands directly.
- Codex generated `.codex-plugin/plugin.json` in its install cache; that extra file was not part of the source and all 35 source files still matched byte-for-byte by hash.

BLOCKERS: Authenticated Codex model access/usage was unavailable in the clean environment, blocking activation and practical repair gates.

REMAINING_WORK: Complete G09–G11 with a logged-in Codex session and captured traces; resolve duplicate-loading policy after observing actual model selection; confirm final GitHub Actions result.

NEXT_PHASE_RECOMMENDATION: Do not start Phase 03 until this report is independently reviewed and model-dependent gates are either completed or explicitly accepted as outstanding.

## Acceptance gate matrix

| Gate | Status | Evidence |
|---|---|---|
| G01 Marketplace JSON valid | PASS | `.agents/plugins/marketplace.json`; marketplace validator. |
| G02 Local marketplace discoverable | PASS | CLI add/list output in `phase-02-evidence.md`. |
| G03 Local plugin install succeeds | PASS | CLI install/list and cache path in evidence. |
| G04 GitHub marketplace resolves | PASS | Git source, fixed branch ref and resolved commit in evidence. |
| G05 GitHub plugin install succeeds | PASS | Installed/enabled listing and cache in evidence. |
| G06 Exactly 15 plugin Skills discoverable | PASS | Prompt input lists 15 namespaced entries from installed cache. |
| G07 No uncontrolled duplicate loading | NEEDS_REVIEW | Both scenario visibly exposes 15 plugin and 15 legacy entries; no model precedence trace. |
| G08 All packaged references accessible | PASS | 18 reference files present, nested link validation, source/cache hash match. |
| G09 Positive activation evidenced | BLOCKED | No logged-in model session. |
| G10 Negative activation evidenced | BLOCKED | No logged-in model session. |
| G11 Real code repair and test evidenced | BLOCKED | No model execution; only fixture baseline run. |
| G12 Plugin removal and rollback verified | PASS | Both test environments removed plugin/marketplace; lists empty. |
| G13 Existing tests and CI pass | PASS | 40 tests and local validators pass; GitHub Actions run `38586399158` succeeded for the implementation commit. |
| G14 Personal/global configuration unchanged | PASS | All install, discovery, and removal commands used temporary HOME/CODEX_HOME. No personal config or installed plugin was targeted. |
