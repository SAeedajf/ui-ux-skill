# Phase 05-C Evidence

Date: 2026-10-15 (Asia/Tehran). Base: `3d89041d47c0c3bcd3a6ebb3aec81f74cb7ddc3a`.

## Environment and source

- `codex --version`: `codex-cli 0.153.4`.
- `codex login status`: `Logged in using ChatGPT`.
- `~/.codex/config.toml` retained `model = "gpt-6-luna"`; no config write was made.
- The selected CLI model argument on each of the three runs was `gpt-5.6-terra`. CLI trace emitted `Model metadata for gpt-5.6-terra not found. Defaulting to fallback metadata`. The final repair turn failed with the usage-limit message. There is no authoritative backend model ID field in the captured run events, so model identity remains unverified.
- PR #16 was merged. `origin/main` was fetched and the Phase 05-C worktree was created from `3d89041d47c0c3bcd3a6ebb3aec81f74cb7ddc3a`.

## Install, paths, duplicate Skills, rollback

- Pre-install JSON snapshots: `/tmp/uiux-05c-plugin-list-before.json` and `/tmp/uiux-05c-marketplaces-before.json`. They showed 33 installed plugins and 3 marketplaces; `ui-ux-pro@ui-ux-pro-marketplace` and `ui-ux-pro-marketplace` were absent. An unrelated `uiuxdesigner@openai-curated-remote` remained installed.
- Temporary install result: Plugin `0.1.0`, enabled, from the current repository; installed cache root was `~/.codex/plugins/cache/ui-ux-pro-marketplace/ui-ux-pro/0.1.0`. The source tree contained exactly 15 `skills/*/SKILL.md` files. Plugin files are in this namespaced cache; personal Skills are under `~/.agents/skills/` and remain separate.
- Positive trace excerpts list five actual personal Skill file paths and no Plugin cache path. Full sanitized trace: [`phase-05c-positive.jsonl`](evidence/phase-05c-positive.jsonl).
- Negative trace completed without any UI/UX Skill file read: [`phase-05c-negative.jsonl`](evidence/phase-05c-negative.jsonl).
- CLI removal commands returned success for the temporary Plugin and Marketplace. The temporary cache directory was absent after cleanup. Post-removal CLI inventory commands stalled after the quota error, so a complete before/after inventory equality check is unavailable. No personal Skill, default-model config, or private ChatGPT Plugin was modified.

## Positive activation

Prompt: «این پروژه یک فروشگاه فارسی RTL است. مشکلات فرم، نمایش خطاها، دسترس‌پذیری و چیدمان موبایل را بررسی کن و راهکار اصلاح ارائه بده.»

The Agent inspected a temporary Persian RTL page and gave code-grounded findings about form semantics/validation, the error relationship and contrast, and fixed-width mobile overflow. However, the trace contains reads of personal Legacy Skills (`ui-ux-review`, `persian-rtl-localization`, `responsive-design`, `accessibility-inclusive-design`, `forms-input`) and not the installed Plugin files. The findings show useful behavior, but they do not prove this Plugin's Skill activation. Browser and assistive-technology inspection were not performed.

## Negative activation

Prompt: «یک تابع Python برای مرتب‌سازی صعودی اعداد بنویس و برای آن یک تست ساده ایجاد کن.»

The fresh CLI invocation returned a sorting function and a simple test as text. No UI/UX Skill file appears in the full trace. The agent could not create files because this check used a read-only sandbox; no UI/UX files were loaded.

## Fixture and repair gate

- A copy of `tests/fixtures/phase02-rtl-shop/` was made at `/tmp/uiux-phase05c-acceptance/repair-fixture`; SHA-256 values and all five initial failures are recorded in [`phase-05c-fixture-baseline.txt`](evidence/phase-05c-fixture-baseline.txt). The source fixture stayed unchanged.
- The third model call began by listing temporary fixture files, then ended with the account usage-limit error. The sanitized trace is [`phase-05c-repair-blocked.jsonl`](evidence/phase-05c-repair-blocked.jsonl). No product file changed; `git diff` against the temporary pre-repair commit is empty. The unchanged baseline tests were not rerun as “after” tests.
- Browser responsive/RTL/focus checks were not run because there was no post-repair state.

## CI and limits

This report separates a completed model turn from actual backend model identity, Plugin discovery from Plugin selection, baseline failures from post-repair results, and CLI removal success from full inventory equality. CI creates a finalized machine-report artifact with the run URL and exact tested commit; the checked-in JSON is the pre-CI source report. No model calls beyond the three listed above were attempted. No Phase 06, merge, or public release was performed.
