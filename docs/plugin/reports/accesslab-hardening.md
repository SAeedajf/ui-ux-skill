# AccessLab OTP input hardening

## Confirmed defect and behavior change

A separate local Persian RTL login demo silently truncated security-code input before validation. Direct reproduction showed `4827319` and `۴۸۲۷۳۱x` both became `482731`; the demo flow accepted the overlong value. The AccessLab changes keep digit normalization lossless, parse the entire value, reject unsupported characters and excess digits, and retain malformed input so people can correct it. Only ASCII spaces or hyphens between digit groups are accepted by this demo contract. Its browser field no longer applies a six-character `maxlength` that could truncate paste before validation.

Before the fix, the demo had 61 passing Node tests and 50 passing browser checks. After the fix, it had 76 passing Node tests and 53 passing browser checks. The local app is a demonstration only; no authentication backend or security guarantee was added.

## Reusable guidance and regression fixture

Canonical Skills and references now distinguish normalization, parsing, and validation; require full-value checks for fixed-length codes; limit separators to an explicit input contract; cover pasted invalid values and invalid-to-valid recovery; and separate real browser zoom from viewport reflow and accessibility-tree evidence from screen-reader output. Async cancellation, stale responses, duplicate submissions, and resend/expiry checks are also called out. The review template distinguishes Skill discovery, file loading, application, and behavioral verification.

`tests/fixtures/otp_validation/` is a small sanitized Python fixture, not a production authentication library. Six standard-library tests cover digit mapping without data loss, strict length and character validation, approved separators, invalid repeated submission, correction, and expiry feedback. The fixture contains no AccessLab user data or demo credentials.

## Evidence state

- AccessLab: 76/76 Node tests and 53/53 in-app browser checks passed on the edited local project. Browser checks include a 10-width responsive matrix, paste preservation, repeated invalid submission, correction, successful local demo completion, and narrow error expansion.
- GitHub fixture: six deterministic `unittest` cases.
- Source/package parity, marketplace validation, and reproducible 0.1.0 archive: passed locally. GitHub Actions run [39147860950](https://github.com/SAeedajf/ui-ux-skill/actions/runs/39147860950) passed on main commit `a58aa59438e22402b2da19053f9f6518169dd599`; the previous PR-head run [39142600519](https://github.com/SAeedajf/ui-ux-skill/actions/runs/39142600519) also passed.
- Plugin version remains 0.1.0; the changes add guidance and tests without changing installation contracts.
- Automatic skill activation: `NOT_VERIFIED`. The current local Codex CLI reports `0.144.5`, but `codex login status` and `codex plugin list` stop on a configuration parse error in `[agents]` (boolean `true` received where an `AgentRoleToml` is expected). No model prompt was sent and no plugin activation trace was captured. The user's Codex configuration was inspected read-only and left unchanged; plugin installation/availability in this runtime therefore remains `UNKNOWN`.
- Real 200% browser zoom: `PASS` in isolated Firefox 147.0.4 on a 1280×720 Xvfb display. Native browser zoom changed the measured CSS viewport from 1280×720 to 640×360 and `devicePixelRatio` to 2. The embedded app had no horizontal overflow; the form stayed within the app viewport and keyboard focus remained visibly outlined. Screenshot and detailed metrics are in the separate AccessLab project, not this repository.
- Screen-reader output: `NOT_VERIFIED`. Orca 49.4 and AT-SPI2 2.58.1 are installed. In the current desktop session, AT-SPI reports `IsEnabled=false` and `ScreenReaderEnabled=false`; Orca's application enumeration listed 17 apps but also warned that its expected socket was missing/stale. This is not evidence of speech output. A separate Xvfb/private D-Bus attempt failed to activate an AT-SPI remote peer (`Could not activate remote peer: unit failed`) and listed zero apps. No spoken output was captured, and the desktop session/accessibility settings were not changed.
- Full WCAG 2.2 AA conformance, physical-device behavior, and real mobile-network performance are not established by these tests.
- After the OTP helper-copy change, the local UI screenshots were refreshed and visually reviewed with Firefox 147.0.4 at 1280×720 and 390×844 CSS px. The image files and hashes remain in the separate AccessLab project and are not included in this repository. These captures do not demonstrate 200% browser zoom.

This report records local implementation evidence separately from reusable Skill quality and activation evidence. The local AccessLab source is not copied into this repository.

## Latest continuation status (2026-10-18)

- GitHub shows PR #22 merged at `2026-10-18T17:04:01Z` by repository account `SAeedajf`, with merge commit `a58aa59438e22402b2da19053f9f6518169dd599`. This continuation did not issue a merge command. The earlier report's reference to checking the PR Checks tab is historical; current CI must be read from the `main` commit's checks.
- The local CLI configuration error prevents confirming installed/enabled plugins or obtaining a runtime activation trace. No settings were edited to work around it. Automatic activation remains `NOT_VERIFIED`, not PASS or FAIL.
- The main desktop has screen-reader support disabled according to AT-SPI status. An actual spoken interaction would require enabling/starting assistive technology in that session; that was not done. Orca output remains `NOT_VERIFIED`.
