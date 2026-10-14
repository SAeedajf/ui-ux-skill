# Owner Runtime Acceptance — Phase 05

This procedure is for the maintainer to finish account-dependent checks that are deliberately not performed by repository CI. It uses the existing `ui-ux-pro` version `0.1.0` and does not change the ChatGPT private plugin, the selected model, or personal legacy Skills.

## Codex CLI: isolated Plugin-only run

Use the latest installed Codex CLI executable explicitly. In this environment, `codex` resolved to 0.144.5 while `/home/saeed/.nvm/versions/node/v22.23.1/bin/codex` was 0.153.4; the latter read the current config and authenticated successfully. Confirm your paths with `type -a codex` and `codex --version` before running.

1. Create a fresh test root with a temporary `HOME`, `CODEX_HOME`, and project directory. Do not copy `auth.json`, keychain exports, session files, or tokens into it.
2. In that temporary environment, add this repository as a local marketplace and install exactly `ui-ux-pro@ui-ux-pro-marketplace`:

   ```sh
   codex plugin marketplace add /path/to/ui-ux-skill
   codex plugin add ui-ux-pro@ui-ux-pro-marketplace
   codex plugin list
   ```

3. Confirm `installed` and `enabled`, the exact 0.1.0 cache path, all 15 `ui-ux-pro:<id>` entries, and no unprefixed or `~/.agents/skills` copies in the isolated project’s `codex debug prompt-input` output.
4. If the temporary Codex home is not authenticated, use the official interactive `codex login` flow with the owner present and the intended existing account. Do not copy credentials from another Codex home. Check `codex login status` and available usage once; do not retry a blocked model call.
5. Keep the user-selected model. Record its exact model identifier and `codex --version` for each run.

If the owner prefers testing from the existing Codex home instead, first authorize the personal plugin installation/configuration change. Back up the exact config and listed plugin state; never alter legacy Skill directories as part of installation.

## Codex smoke cases

Run each in a fresh conversation with `codex exec --json` and retain the JSONL trace privately. Do not name a Skill in either prompt.

**Positive prompt**

> یک فرم خرید فارسی در موبایل دارم. مدیریت خطا، نحوه تعامل کاربر، راست‌به‌چپ بودن، دسترس‌پذیری و چیدمان واکنش‌گرای آن را بررسی کن و مشکلات قابل اثبات را اصلاح کن.

**Negative prompt**

> Write a Python function that sorts a list of numbers in ascending order.

For each run, record the prompt, CLI and model version, login/usage state, event/trace reference, exact Skill path if the trace exposes it, response, and PASS/FAIL/BLOCKED. A good answer alone does not prove Skill activation. If the trace does not expose Skill selection or loading, record activation as `UNKNOWN`.

## Codex fixture repair

1. Make a new disposable copy of `tests/fixtures/phase02-rtl-shop/`; record hashes and Git status. Run `python3 -m unittest -v test_baseline` before the Agent and preserve the five baseline failures.
2. In that project, ask: “This is a Persian RTL store. Inspect real UX and accessibility issues, make limited reversible code changes without unnecessary dependencies, then run the relevant tests.” Do not name a Skill.
3. Save the actual JSONL trace and patch privately. Review that at least one seeded defect changed because of the Agent, then rerun the five checks and regression tests.
4. If a browser is available, inspect 320, 390, 768, and 1440 px; RTL rendering; keyboard/focus recovery; and form error announcement/recovery. Report source-level and browser evidence separately.
5. Mark the repair PASS only with a trace, Agent-authored diff, passing post-repair tests, and no important regression. Otherwise preserve the precise BLOCKED/FAIL result.

## ChatGPT Work: existing private plugin only

Use the existing plugin ID `plugins_6acfa25d79388191b9861545d52f6d03` (release `pluginrel_6acfa26265f48191b194fe33780fbe70`, USER / PRIVATE / 0.1.0). Do not recreate, edit, update, share, or publish it.

1. In ChatGPT, confirm the exact plugin shows `Installed` and `Enabled`; in a fresh Work chat, confirm it appears in the picker.
2. Run the positive Persian form prompt with the plugin explicitly selected. In a second new chat, run the same prompt without explicit selection and record any visible activation evidence.
3. In a third new chat, run the unrelated Python sort prompt without selecting the plugin.
4. Record the visible plugin state, exact prompt, date, result, and whatever trace or invocation indicators the host exposes. If no per-Skill trace is available, mark skill activation `UNKNOWN`; do not infer it from answer quality.
5. Keep screenshots, account identifiers, and raw private traces out of this public repository. Publish only sanitized status and evidence references that the owner approves.

## Result form

For every case, record:

- `status`: PASS / FAIL / BLOCKED / NOT_RUN / NEEDS_REVIEW
- execution date and exact host/model version
- exact prompt and test-project baseline
- installed/enabled/discovered evidence
- selected/loaded Skill and exact path, only if the trace exposes it
- changed-file diff and post-change test result for repair
- regressions and browser viewport states actually checked
- evidence location kept private or sanitized reference suitable for the repository

Lifecycle states are separate: `CREATED` ≠ `INSTALLED` ≠ `DISCOVERED` ≠ `ACTIVATED` ≠ `EXECUTED` ≠ `VERIFIED`.
