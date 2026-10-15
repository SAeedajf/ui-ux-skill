# Phase 05-D — Plugin-Only Activation and Skill Conflict Resolution

**Status:** BLOCKED (model runtime acceptance)
**Base:** `dbe4ffe24db4a2582533dd567af9f15de342fd79`
**Branch:** `codex/ui-ux-plugin-phase-05d`

**Draft PR:** [#19](https://github.com/SAeedajf/ui-ux-skill/pull/19)
**Plugin:** `ui-ux-pro@ui-ux-pro-marketplace` `0.1.0`

## Current result

Codex CLI 0.153.4 and the Plugin package are present. A saved `codex debug prompt-input` inventory from the disposable `CODEX_HOME` lists all 15 namespaced Plugin Skills and no Legacy skill paths for the unnamed positive request. This is discovery evidence only; it does not prove a Skill file was read during a model turn. The separate explicit prompt-input from the source workspace also lists 15 Plugin Skills, alongside 15 project-local source Skills. Both inventories report zero visible description-truncation markers. See [discovery evidence](evidence/phase-05d-discovery.json).

The user selected `gpt-6-luna` with high reasoning effort. That model was previously rejected by this Codex CLI/ChatGPT account with an unsupported-model error (recorded in the Phase 05-C retry report). No Phase 05-D model call has been made, and no alternative model was selected. The account owner reported that ChatGPT Security Settings rejects device-code sign-in and asks to enable device sign-in first. The isolated login was stopped; no retry, security bypass, alternate credentials, or model calls were made. See [authentication blocker](evidence/phase-05d-auth-blocker.txt). Consequently D01–D02 and D04–D07 remain BLOCKED; no activation or duplicate-priority claim is made.

## Duplicate inventory

The project-local personal scope has eight overlapping Skill names; all eight differ in content and description from the Plugin copies. The user Codex-home scope has 15 overlapping names; none is byte-identical to its Plugin copy, while 14 of 15 descriptions match. The checked-in repository Skill files and the Plugin package copies are byte-identical for all 15 names. This proves the copies differ; it does **not** prove Codex priority or explain the prior Legacy reads. Absolute personal paths and personal Skill text are omitted from the committed evidence. Detailed names and redacted comparisons are in [duplicate evidence](evidence/phase-05d-duplicates.json).

## Fixture repair and browser checks

The original `phase02-rtl-shop` fixture remains unchanged and still reproduces five baseline failures. A separate copy at `tests/fixtures/phase05d-rtl-shop/` repairs the accessible labels and error association, menu state and Escape focus restoration, product button names, contrast, responsive layout, and phone form behavior. Its phone contract accepts only a trimmed domestic ASCII mobile number matching `09` plus nine digits. Empty and invalid input produce an associated error and focus the field; valid input clears the error and reports local test success without network submission. Repeated valid submits remain idempotent.

All five structural checks and seven real-browser behavior checks pass. Firefox 157.0 controlled by Playwright reports actual viewport widths of 320, 390, 768, and 1280 CSS pixels; all are RTL, have no horizontal overflow, and show the expected one-, two-, and three-column layouts. Evidence: [baseline failures](evidence/phase-05d-fixture-baseline.txt), [structural checks](evidence/phase-05d-structural-tests.txt), [browser checks](evidence/phase-05d-browser-tests.txt), and [viewport measurements](evidence/phase-05d-browser.json). The five supplied fixture assertions were not changed.

## Gate status

| Gate | Status | Evidence / reason |
|---|---|---|
| D01 selected model executed | BLOCKED | `gpt-6-luna` was previously rejected; official device sign-in is blocked by the account Security Settings. |
| D02 authenticated Plugin-only environment | BLOCKED | Discovery inventory has no Legacy paths, but the isolated account session is not yet authenticated. |
| D03 all 15 Plugin Skills discoverable | PASS | Prompt-input inventory contains 15/15 namespaced Plugin Skills. |
| D04 explicit Plugin activation trace | BLOCKED | No Phase 05-D model turn; no Skill read trace. |
| D05 automatic Plugin activation trace | BLOCKED | Discovery is not a model turn. |
| D06 combined-context runtime case | BLOCKED | Requires D01 and Plugin-only runtime result. |
| D07 duplicate selection cause | BLOCKED | No controlled Plugin/Legacy model traces; no priority claim. |
| D08 personal Skills unchanged | PASS | No personal Skill or persistent model configuration was edited. |
| D09 fixture behavior | PASS | 5 structural + 7 browser checks pass; original fixture tests still show five baseline failures. |
| D10 actual desktop/mobile viewport | PASS | Requested and actual widths match at 320/390/768/1280. |
| D11 full regression and CI | PASS | 57 repository tests and local validators passed; [GitHub Actions run 38764660837](https://github.com/SAeedajf/ui-ux-skill/actions/runs/38764660837) passed for commit `f9a1d4384c6b037bbc00ec6efc74ff77332e10aa`. |
| D12 temporary install rollback | PASS | The disposable Plugin, marketplace entry, and package cache are absent after removal; personal configuration was not touched. See [rollback evidence](evidence/phase-05d-rollback.json). |
| D13 private ChatGPT Plugin unchanged | PASS | No private ChatGPT Plugin operation was performed. |
| D14 no merge or release | PASS | No merge, public release, or Phase 06 work performed. |

## Required next action

Runtime activation is blocked until the account owner enables official device sign-in in ChatGPT Security Settings. Do not retry authentication or switch models. After that account setting is changed, resume by checking the selected model without fallback and run the requested activation cases only if it executes. Offline fixture and repository checks passed. Roll back the disposable Plugin and marketplace, finish CI and the Draft PR, and keep runtime gates blocked. Do not merge, publish, or start Phase 06.
