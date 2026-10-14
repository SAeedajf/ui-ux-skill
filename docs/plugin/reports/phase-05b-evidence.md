# Phase 05-B Evidence

Collection date: 2026-10-14. Repository: `https://github.com/SAeedajf/ui-ux-skill`.

## Repository and PR baseline

- PR #15 was `MERGED` when this phase started.
- `git fetch origin main` advanced the base to `5a18b097ade439281e9d39b5c6476e84eb2e6ab0`.
- Branch `codex/ui-ux-plugin-phase-05b` was created from that exact `origin/main`; the Phase 05 worktree and branch were left intact.
- `plugins/ui-ux-pro/plugin.json` remains version `0.1.0`; SHA-256 is `1456bc5bf0f206ca92554b44b2377048259c209848ed64ef6c31e5b40290ca54`.
- The deterministic plugin archive from this source is SHA-256 `611b8eddaf74821dd2a1dd6a1d8ae576c32e20b4b23db12ec7021aa6ae634c7c`.
- No plugin Skill or manifest source was changed.

## CLI, account, model, and usage

- Verified executable: user-local Node install `~/.nvm/versions/node/v22.23.1/bin/codex`; version `codex-cli 0.153.4`.
- `codex login status` returned `Logged in using ChatGPT`.
- Usage snapshot returned `ordinaryUsageAllowed=true`, with 69% of the primary window and 70% of the weekly window used. No usage limit was reached.
- The existing config selected `gpt-6-luna` with high reasoning. The config was not edited and the CLI run did not override the model.
- `codex debug models` listed `gpt-6-luna`, but the first real `codex exec --json` attempt returned HTTP 400 `invalid_request_error`: `The 'gpt-6-luna' model is not supported when using Codex with a ChatGPT account.` The sanitized public trace is `evidence/phase-05b-positive-blocked.jsonl`; the raw local run output was kept outside Git.
- Trace events are exactly the startup and failure boundary: `turn.started`, `error`, `turn.failed`. No assistant message, tool call, Skill read, file modification, negative smoke, or repair call occurred. No retry was made because the error is a model/account compatibility failure, not a transient network failure.
- Codex startup also logged failed initialization attempts for an already configured localhost MCP endpoint. No MCP or backend was created or changed; the model-specific HTTP 400 is the recorded blocking error.

## Plugin install, discovery, and rollback

- Before installing, `/tmp/uiux-05b-plugin-list-before.json` and `/tmp/uiux-05b-marketplaces-before.json` captured the installed plugin and marketplace inventories. The target plugin and marketplace were absent.
- Added the local repository marketplace, then installed only `ui-ux-pro@ui-ux-pro-marketplace`. Codex reported version `0.1.0`, `installed=true`, `enabled=true`, and cache path under the user's Codex plugin cache.
- `codex debug prompt-input` returned 15 `ui-ux-pro:` entries. The source root was the installed plugin cache. The account also had 8 same-name directories under its personal legacy skill root; no copies were changed.
- After the rejected model request, removed only the newly installed plugin and newly added marketplace. The post-removal installed-plugin inventory and marketplace list compare equal to the pre-install snapshots; the model setting remained `gpt-6-luna`; the plugin cache was removed. No other plugin or configuration was changed.
- The inventory proves discovery, not model selection. No actual Skill was loaded because the request failed before Agent execution.

## Positive smoke and fixture baseline

- Positive prompt (Persian, without naming a Skill): «یک فرم خرید فارسی در موبایل دارم که وضعیت خطا، نحوه نمایش پیام‌ها، راست‌به‌چپ بودن و چیدمان واکنش‌گرای آن مشکل دارد. فایل‌های پروژه را بررسی کن و مشکلات واقعی را پیدا و اصلاح کن.»
- The CLI rejected the request before the Agent started. The isolated positive test files retained their original SHA-256 after the failure; there is no positive Agent response or diff.
- A new copy of `tests/fixtures/phase02-rtl-shop/` was created under `/tmp/uiux-phase05b-acceptance/repair`. The repository fixture was untouched. Hashes and all five expected failure names/results are in `evidence/phase-05b-fixture-baseline.txt`.
- No negative request or Agent repair was submitted. No post-repair tests, browser viewports, screenshot, DOM evaluation, or regression results are claimed. Firefox exists, but Playwright and Selenium Python packages were unavailable.

## Boundaries and owner action

- The existing ChatGPT plugin remains PRIVATE and version `0.1.0`; only its previously known created metadata is available. ChatGPT Work installation, discovery, and runtime were not tested.
- No new plugin content was introduced. The previous six partial source records and S20 access limitation stay unresolved.
- To resume, the owner must select or authorize a Codex CLI model compatible with the authenticated ChatGPT account. Keep the persistent default as-is unless explicitly requested. Then authorize at most three calls (positive, negative, one fixture repair) using the same approved model. An isolated profile still requires an owner-performed official login; credentials must not be copied.
- Do not start Phase 06, change personal Skills/configuration, modify the private ChatGPT plugin, use another account to bypass usage, test Claude, or publish publicly.
