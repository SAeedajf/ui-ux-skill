# Phase 05-D Evidence Ledger

## Baseline and repository state

- Base commit: `dbe4ffe24db4a2582533dd567af9f15de342fd79`, the merge commit of PR #18.
- At inspection, PR #18 was MERGED and the latest `main` was the same commit. Its latest validation run was successful: [run 38759248679](https://github.com/SAeedajf/ui-ux-skill/actions/runs/38759248679).
- New working branch: `codex/ui-ux-plugin-phase-05d`.
- CLI: `/home/saeed/.nvm/versions/node/v22.23.1/bin/codex`, version `0.153.4`; the login status for the regular CLI profile was ChatGPT. A separate temporary `CODEX_HOME` contains no copied auth data.
- The official device login in the temporary `CODEX_HOME` was stopped after the user reported that ChatGPT Security Settings blocks device-code sign-in. No credential file was copied, no retry or alternate login was attempted, and no Phase 05-D model call was made. See `phase-05d-auth-blocker.txt`.

## Discovery and conflict inventory

- Temporary Plugin-only automatic prompt-input capture: 20 total Skill entries, including 15 namespaced `ui-ux-pro:*` entries and zero project Legacy Skill paths. The 15 names are listed in `phase-05d-discovery.json`; visible truncation markers: zero.
- The explicit prompt-input capture from the source project contains 35 Skill entries: 15 Plugin entries, 15 project-local Skills, and 5 system Skills. It confirms the `ui-ux-pro:forms-input` namespace appears in the Plugin catalog, but it is not Plugin-only.
- Neither prompt-input capture is a model turn. No `SKILL.md` read by an agent is asserted in this phase yet.
- The project-local user Skill directory has eight overlaps with Plugin names. The separate Codex-home Skill directory has 15 overlaps. All 23 copies differ byte-for-byte from Plugin package files; project-local descriptions differ for all eight, while the Codex-home descriptions match for 14 of 15. The checked-in `.agents/skills` copies and Plugin package copies match byte-for-byte for all 15 names.
- Personal absolute paths and descriptions were omitted from the committed inventory. No personal Skill files were modified.

## Fixture evidence

- The original fixture baseline still fails its five original checks: contrast (2.712:1), missing form label/error association, fixed 720px width, missing menu expanded/escape behavior, and unlabeled cart buttons. Captured in `phase-05d-fixture-baseline.txt`.
- The separate Phase 05-D copy keeps `test_baseline.py` identical to the original. All five structural checks pass after repair.
- Seven browser tests pass in Firefox 157.0 via Playwright: empty, invalid, valid, recovery, duplicate valid submit, accessible name/error/live-region, and Escape focus return.
- Phone test contract: trim surrounding whitespace; accept ASCII `09` plus nine ASCII digits only. The success state explicitly says this is a test and no data was sent. Browser instrumentation observed no HTTP(S) request during submission.

## Viewport evidence

Firefox 157.0 (Playwright headless), height 900 CSS pixels:

| Requested | Actual `innerWidth` | `scrollWidth` | RTL | Columns | Overflow |
|---:|---:|---:|---|---:|---|
| 320 | 320 | 320 | yes | 1 | no |
| 390 | 390 | 390 | yes | 1 | no |
| 768 | 768 | 768 | yes | 2 | no |
| 1280 | 1280 | 1280 | yes | 3 | no |

Machine capture: `phase-05d-browser.json`.

## Open runtime gates

The user selected `gpt-6-luna` at high reasoning effort. Phase 05-C already records this CLI/ChatGPT account rejecting that model as unsupported. No fallback was tried. The user-selected model is not considered verified, and Phase 05-D activation traces remain unrun. The temporary login is blocked by the account Security Settings. Do not retry authentication or switch models. D01/D02 and D04-D07 remain blocked; resume only after official device sign-in is enabled and the selected model can be checked without fallback.

The full repository test suite passes (57 tests); repository, marketplace, Plugin package, Phase 05-D report validators, and deterministic package check also pass locally. The captured test log is `phase-05d-repo-tests.txt`. The temporary Plugin and marketplace were removed from the disposable CODEX_HOME; post-removal CLI snapshots show no installed Plugin, no marketplace, and no Plugin cache. D12 passes. Current branch CI and Draft PR creation remain pending.
