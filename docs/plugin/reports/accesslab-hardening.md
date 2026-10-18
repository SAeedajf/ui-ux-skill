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
- Source/package parity, marketplace validation, and reproducible 0.1.0 archive: passed locally. GitHub Actions status is pending on the PR's latest head and should be read from the live Checks tab.
- Plugin version remains 0.1.0; the changes add guidance and tests without changing installation contracts.
- Automatic skill activation: `NOT_VERIFIED`. One natural-language OTP positive and one non-UI negative prompt are defined as `NOT_RUN`; no fresh model invocation or trace is claimed.
- Real 200% browser zoom: `NOT_VERIFIED`; the in-app browser shortcuts left measured `innerWidth=1280`, `devicePixelRatio=1`, and `visualViewport.scale=1` unchanged. A 640×360 reflow check is not zoom evidence.
- Screen-reader output: `NOT_VERIFIED`; Orca is installed, but no spoken output was captured because the current AT-SPI socket was unavailable.
- Full WCAG 2.2 AA conformance, physical-device behavior, and real mobile-network performance are not established by these tests.
- The existing local desktop/mobile screenshots predate the OTP helper-copy change; they are not represented as screenshots of the final UI.

This report records local implementation evidence separately from reusable Skill quality and activation evidence. The local AccessLab source is not copied into this repository.
