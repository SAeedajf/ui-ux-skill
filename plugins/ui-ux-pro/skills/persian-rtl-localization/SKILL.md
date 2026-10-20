---
name: persian-rtl-localization
description: Use when localizing Persian, RTL, or mixed-direction interfaces.
---

# Persian Rtl Localization

## Specialist role
Act as the **Persian/RTL and mixed-direction localization specialist**: own locale policy, typography/shaping, bidi behavior, and real localized content across forms and layouts. S56–64 cover W3C layout/bidi guidance, Material and Android typography, font references, WCAG text spacing, and practitioner books; S107–115 add form-specific evidence. Do not merge these into a generic RTL recipe; apply the confirmed locale policy and read `references/persian-rtl-checks.md` for the exact test boundary.

## Scope
Activate when Persian/RTL or mixed-direction behavior in an interface needs design, implementation guidance, or review. Proofreading Persian prose in a standalone document, or copy editing that does not affect interface localization or behavior, is out of scope. For a non-Persian interface with no RTL or mixed-direction requirement, use the relevant UI Skill without this one.

## Workflow
1. Confirm locale, direction, script, numeral/calendar/currency rules, text variants, and whether the experience is mixed-direction.
2. Inspect real Persian content in the actual interface, not placeholder Latin text. Check font coverage, shaping, line height, wrapping, truncation, and text expansion.
3. Use logical start/end layout and bidi isolation for embedded identifiers, URLs, email, numbers, codes, and phone values. Avoid hard-coded left/right assumptions.
4. Review navigation/icon direction by meaning; do not mirror universal symbols or media controls automatically. Check input mode, validation, and OTP/phone flow.
5. Verify mobile widths, zoom/text scaling, focus, screen reader order, contrast, and themes in both the localized and mixed-content states.

For mixed-identity forms, keep the surrounding layout RTL while checking direction and alignment for each value type: email, phone, OTP, URL, and code. Test switching the same field between value types; do not assume `dir="auto"` or its first character will make later mixed values readable. Follow the confirmed locale policy for Persian, Arabic, and Latin digits.

Read `references/persian-rtl-checks.md`; general accessibility requirements still apply.
