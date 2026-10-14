# Phase 04 evidence record

Evidence collected 2026-10-14. Repository: `https://github.com/SAeedajf/ui-ux-skill`. All statuses distinguish current observations from older records and account-dependent gates.

## GitHub baseline

- `git fetch origin --prune` advanced `origin/main` to `fea6e825306e7dec5162b0bb9fe37ac3129cb36c`, matching the Phase 04 supplied baseline.
- PRs #10, #11, #12, and #13 are all `MERGED`. PR #13 merged at `2026-10-14T15:34:02Z`.
- Main validation run `38590465251` for `fea6e825306e7dec5162b0bb9fe37ac3129cb36c` completed `success`.
- New branch `codex/ui-ux-plugin-phase-04` starts at that main commit. It was created in the existing Phase 03 managed worktree after confirming that worktree was clean; no Phase 03 changes were reused or overwritten.
- The private Plugin Creator check was read-only. No ChatGPT plugin, account, Codex setting, Marketplace, or public visibility changed.

## Repository, package, and fixture checks

| Command / observation | Result |
|---|---|
| `.venv/bin/python scripts/validate_repo.py` | `15 skills, 124 sources (118 reviewed / 6 partial), 14 domains, 30 activation cases, 29 quality scenarios`; PASS. |
| `.venv/bin/python scripts/validate_marketplace.py` | PASS for `ui-ux-pro-marketplace` and local plugin source. |
| `.venv/bin/python -m unittest discover -s tests -v` | 45 tests passed, including five Phase 04 report-validator tests. |
| `.venv/bin/python scripts/build-plugin.py --check --archive` | PASS; canonical package unchanged; deterministic ZIP built. |
| `.venv/bin/python scripts/validate-plugin.py` | PASS for schema, all Skills/references, exact source bytes, and package safety checks. |
| `.venv/bin/python scripts/validate_phase04_report.py` | PASS; JSON schema and gate consistency validate. |
| 124-row registry inspection | 124 unique IDs; no blank required registry fields; every current URL has an HTTP(S) scheme and host; two submitted URLs use documented canonical replacements (S18 and S100); 118 reviewed / 6 partially verified. |
| `git diff --check` | PASS on final branch verification. |
| `tests/fixtures/phase02-rtl-shop`: `.venv/bin/python -m unittest -v test_baseline.py` | Expected baseline: 5 tests ran, 5 failed. Failures cover responsive fixed width, error contrast/state, form label/error association, menu state/focus recovery, and product button accessible names. This proves a controlled failing fixture only; no Agent repair occurred. |

The fixture baseline output was captured locally in `/tmp/uiux-phase04-fixture-baseline.log`. The isolated CLI discovery data was captured locally under a disposable `/tmp/uiux-phase04-discovery-*` root and summarized below. Temporary account data or credentials were not copied into those directories.

`actionlint` is not installed in this environment; GitHub Actions will parse and execute the Phase 04 workflow on the PR.

## Codex install/discovery and duplicate Skills

Codex CLI `0.144.5` was used with separate disposable `HOME`, `CODEX_HOME`, and project roots. Plugin installation used the repository-local Marketplace; discovery used `codex debug prompt-input` from each isolated project. No global Codex configuration was edited.

| Scenario | Result | UI/UX count and source |
|---|---|---|
| Plugin Only | Discovery PASS | 15 `ui-ux-pro:<id>` entries from `<temp>/codex/plugins/cache/ui-ux-pro-marketplace/ui-ux-pro/local/skills/<id>/SKILL.md`. |
| Legacy Only | Discovery PASS | 15 unprefixed `<id>` entries from `<temp>/project/.agents/skills/<id>/SKILL.md`. |
| Plugin + Legacy | Duplicate discovery confirmed | 30 entries: both 15-entry catalogs and both source paths are visible. |

Serialized `codex debug prompt-input` JSON sizes: Plugin Only 15,633 bytes; Legacy Only 13,763 bytes; Both 18,799 bytes. The inputs show catalog/path discovery overhead, not token usage or exact context billing. No selection precedence or model choice is observable from this command.

All isolated environments returned `Not logged in`. A read-only `codex login status` on the normal CLI could not start because the current personal config failed parsing (`invalid type: boolean true, expected struct AgentRoleToml`, line 12). This configuration was left unchanged. No model was substituted, no model calls or retries were made, and the Phase 04 model budget was capped at two smoke calls (0 used) pending authenticated CLI access. Therefore positive/negative automatic activation and practical repair remain blocked.

The migration strategy in `docs/plugin/duplicate-skills-migration.md` treats the Plugin as the maintained source for new installs, but leaves existing user skills untouched; it requires a content diff, timestamped backup outside scan roots, explicit opt-in, fresh-session discovery, and move-back rollback.

## Fixture repair and comparison

The five expected fixture failures were reproduced before any change. The current environment could not invoke an authenticated Codex CLI model, so there is no agent patch, agent trace, post-agent test result, or browser regression capture. The fixture was not repaired manually and no repair PASS is claimed.

The existing one-pair with/without-library comparison in `docs/baseline-comparison.md` is retained as narrow prior evidence only. It reports one controlled pair and existing JSONL traces; it is not a statistical result, a current Phase 04 run, or evidence that all users/models improve. No new comparison pair was run because no authenticated Codex model was available.

## Private ChatGPT plugin state

The official Plugin Creator metadata reader returned the exact existing record:

```text
plugin_id=plugins_6acfa25d79388191b9861545d52f6d03
release_id=pluginrel_6acfa26265f48191b194fe33780fbe70
name=ui-ux-pro
version=0.1.0
scope=USER
discoverability=PRIVATE
```

This confirms `CREATED` only. The available read-only metadata operation does not report installation in ChatGPT Work, discovery in a conversation, Skill selection, or runtime. No ChatGPT conversation/browser was used. C09 installation, C10 discovery, T01–T07, and duplicate Skill behavior remain blocked/not-run as shown in `acceptance-gates.md`.

## ZIP and provenance

- ZIP: `ui-ux-pro-0.1.0.zip`; hash: `611b8eddaf74821dd2a1dd6a1d8ae576c32e20b4b23db12ec7021aa6ae634c7c`.
- The bytes are identical to the Phase 03/main artifact; no Skill or manifest change justified a version bump. Keep `0.1.0`.
- `ZipFile.testzip()` returned `None`; 35 regular members comprise root `plugin.json`, `LICENSE`, 15 Skill trees, and 18 reference Markdown files. No path traversal or symlink member was found.
- The generated sidecar identifies source commit `fea6e825306e7dec5162b0bb9fe37ac3129cb36c`, `validation_status=PASS`, the same ZIP hash, and a 35-file inventory.
- The GitHub Actions job uploads the ZIP, sidecar, and CI-finalized machine report as `ui-ux-pro-0.1.0-phase-04-rc`. It is a private PR CI artifact, not a public release.

## Security and rights

Automated package checks plus targeted signature scans found no secrets/private keys, machine-specific package paths, binary/hidden/cache files, symlinks, traversal entries, dangerous shell/download-to-shell patterns, or obvious prompt-injection signatures. The scans are bounded and do not replace expert semantic/security review. The source registry remains 118 reviewed / 6 partial; S20's direct-page access limitation and human rights review are documented in `security-and-provenance-review.md`.

## Current outcome

Package and deterministic engineering checks pass; operational acceptance is `PARTIAL`. Codex activation/repair and ChatGPT installation/discovery/execution are not established. The Release Candidate does not imply public submission eligibility, OpenAI endorsement, or public-release readiness.
