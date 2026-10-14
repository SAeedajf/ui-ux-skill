# Phase 05 — Runtime Unblocking & Operational Proof

PHASE: 05

TITLE: Runtime Unblocking & Operational Proof

STATUS: PARTIAL

REPOSITORY: https://github.com/SAeedajf/ui-ux-skill

BASE_COMMIT: `6c8069d05c7ac147c2c3d83cd88303674f012518`

OUTPUT_COMMIT:  (implementation evidence commit; the CI artifact records the exact tested PR head).

BRANCH: `codex/ui-ux-plugin-phase-05`

PULL_REQUEST: Pending CI and publication of the Draft PR.

CODEX_VERSION: PATH-selected CLI `0.144.5`; direct installed CLI `0.153.4`.

MODEL_USED: `NOT_RUN`.

MODEL_AUTH_STATUS: Authenticated using ChatGPT with CLI `0.153.4`; the disposable Plugin-only CODEX_HOME is not logged in.

CONFIG_DIAGNOSIS: `CONFIG_ISSUE_DIAGNOSED` — shell PATH selects the older CLI, which rejects `[agents]` at line 12. Direct `0.153.4` accepts the same config and reports the existing login. No TOML, PATH, or auth file was changed.

CONFIG_REPAIR_STATUS: No personal change applied. Owner can call the verified CLI path or change PATH after reviewing the destination; see evidence report.

PLUGIN_DISCOVERY: `PASS` in a disposable Plugin-only CODEX_HOME: version `0.1.0`, installed and enabled, 15 discovered Skill files with source paths verified, and no legacy entries. Discovery tests also reproduced 15 Plugin-only, 15 Legacy-only, and 30 combined entries. This is not activation evidence.

POSITIVE_ACTIVATION: `BLOCKED` — no authenticated model trace in the Plugin-only environment.

NEGATIVE_ACTIVATION: `BLOCKED` — no authenticated model trace in the Plugin-only environment.

AGENT_REPAIR: `BLOCKED` — the five baseline failures were reproduced; no Agent change was made.

FIXTURE_TESTS_BEFORE: 5 seeded failures reproduced in a fresh temporary copy.

FIXTURE_TESTS_AFTER: `BLOCKED` — no Agent-authored diff exists.

BROWSER_REGRESSION: `NOT_RUN`.

DUPLICATE_SKILLS: `NEEDS_REVIEW` — isolated discovery is 15/0, 0/15, and 15/15 across Plugin-only, Legacy-only, and combined contexts. Eight personal overlaps differ from canonical repo content. No automatic migration or precedence claim.

CHATGPT_PLUGIN_STATUS: Exact existing plugin metadata still reports ID `plugins_6acfa25d79388191b9861545d52f6d03`, release `pluginrel_6acfa26265f48191b194fe33780fbe70`, version `0.1.0`, USER scope, PRIVATE visibility. This confirms `CREATED` only.

CHATGPT_RUNTIME_TESTS: `BLOCKED` installation/discovery; positive/negative tests `NOT_RUN`.

SOURCE_RIGHTS_REVIEW: `NEEDS_REVIEW` — six sources remain partial; Coolors S20 direct-page access remains independently limited. The new matrix records what is supported and what still requires a maintainer or rights-holder.

TEST_COUNT: 52 deterministic tests pass locally. GitHub Actions is still pending; it will finalize O14 in the run artifact.

CI_STATUS: `PENDING` for the new Phase 05 branch; CI produces a finalized machine report artifact for the exact run/commit.

FILES_CHANGED: Phase 05 report/schema/validator/tests, CI workflow, rights matrix, owner-runtime guide, and clarification of the S20 access-status note. Plugin Skills and manifest were not changed; version remains `0.1.0`.

EVIDENCE: [`phase-05-evidence.md`](phase-05-evidence.md), [`phase-05.json`](phase-05.json), [`source-rights-resolution.md`](../source-rights-resolution.md), [`owner-runtime-acceptance.md`](../owner-runtime-acceptance.md).

BLOCKERS:

- Authenticated account state and usage are available under CLI 0.153.4, but it is not installed in the authenticated profile. Logging in to the disposable CODEX_HOME needs the owner to use the official interactive flow; copying auth/session files is prohibited.
- ChatGPT Work installation, discovery, and per-Skill trace are not exposed through the available read-only metadata call.
- Duplicate selection precedence and human source-rights clearance remain unverified.

REMAINING_WORK: Owner-run Codex smoke cases, Agent repair and its post-repair/browser checks; owner-run ChatGPT Work installation/discovery/tests; human rights-holder decision. Do not merge, publish, test Claude, or migrate personal Skills.

OWNER_ACTION_REQUIRED: Choose an approved authentication route for the disposable Plugin-only CLI, then follow [`owner-runtime-acceptance.md`](../owner-runtime-acceptance.md). In the intended ChatGPT Work account, run the owner cases for the exact existing private plugin. Review personal Skill divergences before any migration.

NEXT_PHASE_RECOMMENDATION: Continue Phase 05 after owner access is prepared. Do not begin Phase 06 while required runtime and rights gates remain open.

## NEXT_PHASE_HANDOFF

Phase 05 is PARTIAL on `codex/ui-ux-plugin-phase-05`, based on `6c8069d05c7ac147c2c3d83cd88303674f012518`. The old PATH-selected CLI 0.144.5 produces the `AgentRoleToml` parse error; installed CLI 0.153.4 reads the same config and authenticates. Disposable Plugin-only installation/discovery passes for all 15 Skills, but no model was called because that isolated CODEX_HOME is unauthenticated and user auth was not copied. The five fixture baseline failures were reproduced; no Agent repair is claimed. Open gates: O04–O08 and O10–O14; ChatGPT positive/negative tests are not run. Eight overlapping personal Skills differ from canonical copies, so preserve them pending owner review. Six sources remain partial and S20 direct access remains limited. The next action is an owner-approved official login in the disposable Plugin-only CODEX_HOME or an explicitly authorized reversible install in the authenticated profile, followed by the two smoke cases, real fixture repair, post-repair tests, and browser checks. Keep the existing ChatGPT plugin PRIVATE and unchanged; do not merge, publish, test Claude, or begin Phase 06.
