# Phase 05 Evidence — Runtime Unblocking & Operational Proof

Evidence collected 2026-10-14. Repository: `https://github.com/SAeedajf/ui-ux-skill`. This record separates installed/discovered states from model activation, repair, and browser verification. No account credentials or raw private traces are included.

## GitHub baseline

- `git fetch origin main codex/ui-ux-plugin-phase-04` advanced `origin/main` to `6c8069d05c7ac147c2c3d83cd88303674f012518`.
- PR #14 is now `MERGED`; its head was `ad7f784b294eb4541a5211ec7d8c6163656c961f`. The prior Phase 04 report's “Draft; not merged” state is stale.
- `main`'s latest validation run at baseline is [38595152996](https://github.com/SAeedajf/ui-ux-skill/actions/runs/38595152996), `success`, on `6c8069d05c7ac147c2c3d83cd88303674f012518`.
- New branch `codex/ui-ux-plugin-phase-05` was created from that `main` commit. No Phase 04 worktree changes were carried into it.
- Root `plugins/ui-ux-pro/plugin.json` remains version `0.1.0`; no package Skill or manifest content was changed in this phase.

## Codex CLI configuration, authentication, and usage

- In this shell, `command -v codex` resolves to `/home/saeed/.local/bin/codex`, version `0.144.5`. The separately installed `/home/saeed/.nvm/versions/node/v22.23.1/bin/codex` reports `codex-cli 0.153.4`.
- The old selected executable reproduces `invalid type: boolean true, expected struct AgentRoleToml` at `~/.codex/config.toml:12:1` on login status and plugin-list commands. Python's TOML parser accepts the file and identifies `agents` as a table with `enabled` boolean. The current official config reference defines `agents.enabled` as a boolean. The exact source of failure is the stale CLI selected by PATH, not malformed TOML for the installed 0.153.4 CLI.
- The 0.153.4 executable, using the same existing user configuration and auth state, returned `Logged in using ChatGPT`. No config, PATH, login, model, or user plugin setting was modified. Therefore `CONFIG_ISSUE_DIAGNOSED`; a personal setting change was not needed to diagnose it. For reliable use, invoke the newer executable explicitly or have the owner adjust shell PATH after reviewing the target. Restore the prior PATH order to roll back a temporary shell-only change.
- A separate read-only account usage snapshot on 2026-10-14 reported `ordinaryUsageAllowed=true`, no rate-limit reached, 38% of the 5-hour window used and 65% of the 7-day window used. It reported no spend-control block. This establishes available usage at the snapshot only; it is not a model request or a promise of future availability.
- No model was invoked. `MODEL_USED=NOT_RUN`.

## Isolated Plugin install and Skill discovery

- Codex CLI 0.153.4 installed `ui-ux-pro@ui-ux-pro-marketplace` from the Phase 05 worktree into a disposable `CODEX_HOME`. Plugin listing confirmed version `0.1.0`, `installed=true`, `enabled=true`, and the source path under `plugins/ui-ux-pro`.
- The isolated cache contained exactly 15 `SKILL.md` files. `codex debug prompt-input` in an empty project showed all 15 `ui-ux-pro:<id>` entries. The plugin-only project had no legacy Skill directory and no unprefixed UI/UX Skill entry. The 33 canonical Skill/package files compared byte-for-byte with zero mismatches.
- Repeated non-model discovery controls: Plugin-only `15/0`, Legacy-only `0/15`, Plugin + Legacy `15/15`. All three use separate disposable HOME/CODEX_HOME roots or copies and the actual current CLI 0.153.4. The result proves discovery and source separation, not model selection or precedence.
- The temporary installed CODEX_HOME returned `Not logged in`. No auth/session/token files were copied into it. The authenticated user profile has not had the Plugin installed or enabled. Consequently no authenticated plugin activation test could be run without either (a) owner login through the official interactive flow inside the disposable CODEX_HOME or (b) owner-approved changes to personal Codex plugin configuration.

## Duplicate Skill review

- The existing migration guide is sufficient; no migration script was created and no legacy directory was moved or deleted.
- Read-only comparison found eight names overlapping between the personal `~/.agents/skills` directory and the repository's 15 canonical UI/UX Skills. All eight directory contents differ from the current repository copies. The difference may reflect local edits or version drift; it is not safe to overwrite or archive them without an owner review. Other personal Skill directories were left untouched.
- Discovery tests still expose both catalogues when both are present. No authenticated selection trace exists, so source precedence remains `NEEDS_REVIEW`.

## Fixture baseline and repair

- A fresh disposable copy of `tests/fixtures/phase02-rtl-shop/` was used. Before any Agent action, `python3 -m unittest -v test_baseline` ran all five seeded tests and all five failed as expected: contrast, label/error association, fixed-width layout, menu state/focus return, and accessible button names.
- No Agent repair was attempted because the authenticated Codex profile does not have this plugin installed, while the isolated plugin-only profile is not authenticated. The fixture remains unmodified by an Agent. No post-repair test, browser regression, or quality-evaluation result is claimed.

## Existing private ChatGPT plugin

The read-only Plugin Creator metadata call on this date returned:

```text
plugin_id=plugins_6acfa25d79388191b9861545d52f6d03
release_id=pluginrel_6acfa26265f48191b194fe33780fbe70
name=ui-ux-pro
version=0.1.0
scope=USER
discoverability=PRIVATE
```

This proves `CREATED` and current private metadata only. It does not prove `INSTALLED`, `DISCOVERED`, `ACTIVATED`, or `EXECUTED` in ChatGPT Work. No Work conversation or plugin picker was accessed. No release update or visibility change was made.

## Source and rights review

- New matrix: [`docs/plugin/source-rights-resolution.md`](../source-rights-resolution.md). S36 and S50 still require JavaScript for rendered content; S100 and S109 expose public overview/method pages while detailed research is Premium; S94's author page does not prove a newer edition is released; S102's author page links to free online reading but does not grant a reuse license; S20 direct access failed and remains distinct from its reviewed source identity.
- No affected source content or assets were copied. All six partially verified sources remain partial. No rights-holder clearance is claimed.
- Clarified the S20 registry note so `review_status=reviewed` cannot be read as full-page access. The direct-access limitation remains explicit in `access_status` and notes.

## Deterministic verification

- `.venv/bin/python -m unittest discover -s tests -v`: 52 tests passed, including six Phase 05 report-contract tests.
- `scripts/validate_repo.py`: PASS — 15 Skills, 124 sources (118 reviewed / 6 partial), 14 domains, 30 activation cases, 29 quality scenarios.
- `scripts/validate_marketplace.py`, `scripts/validate-plugin.py`, `scripts/validate_phase04_report.py`, and `scripts/validate_phase05_report.py`: PASS.
- `scripts/build-plugin.py --check --archive`: PASS. The deterministic version 0.1.0 ZIP hash remains `611b8eddaf74821dd2a1dd6a1d8ae576c32e20b4b23db12ec7021aa6ae634c7c`, identical to the Phase 04 release candidate. No payload version bump is needed.
- `git diff --check`: PASS. GitHub Actions for the new branch remains pending; the CI-finalized report artifact is the evidence for O14.

## Files and scope

Phase 05 adds this evidence report, a machine report/schema/validator and CI integration, a rights-resolution matrix, and an owner-run runtime acceptance guide. The Plugin payload and version remain unchanged. No ChatGPT plugin, personal Codex config, user legacy Skill, public listing, external account, or Claude runtime was modified or tested.

## Owner action required

To finish the model gates, the owner must either log in through the official interactive flow in the disposable Plugin-only CODEX_HOME (no credential copying) or authorize a reversible install/config change in the authenticated profile. Then run the two unnamed smoke cases, the fixture repair, post-repair tests, and browser checks from [`owner-runtime-acceptance.md`](../owner-runtime-acceptance.md). ChatGPT Work install/discovery/runtime still requires the owner to operate the intended account; keep raw private traces/screenshots out of the public repo.
