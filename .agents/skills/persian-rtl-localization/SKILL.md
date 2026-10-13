---
name: persian-rtl-localization
description: Use when Persian/RTL or mixed-direction UI, typography, digits, dates, currency, phone, or OTP behavior is in scope.
---

# Persian Rtl Localization

## Scope
Activate when Persian/RTL or mixed-direction behavior in an interface needs design, implementation guidance, or review. Proofreading Persian prose in a standalone document, or copy editing that does not affect interface localization or behavior, is out of scope.

## Workflow
1. Confirm locale, direction, script, numeral/calendar/currency rules, text variants, and whether the experience is mixed-direction.
2. Inspect real Persian content in the actual interface, not placeholder Latin text. Check font coverage, shaping, line height, wrapping, truncation, and text expansion.
3. Use logical start/end layout and bidi isolation for embedded identifiers, URLs, email, numbers, codes, and phone values. Avoid hard-coded left/right assumptions.
4. Review navigation/icon direction by meaning; do not mirror universal symbols or media controls automatically. Check input mode, validation, and OTP/phone flow.
5. Verify mobile widths, zoom/text scaling, focus, screen reader order, contrast, and themes in both the localized and mixed-content states.

Read `references/persian-rtl-checks.md`; general accessibility requirements still apply.
