# Example: Android sign-in flow review

**Request:** Review a Persian sign-in flow with phone number and one-time code entry.

**Inspect:** Actual locale direction and digit policy; label/format/help text; keyboard type; phone normalization; code paste/autofill; resend timer and explanation; invalid/expired states; focus movement; TalkBack order and announcements; text scaling; narrow, tablet, and resized-window behavior.

**Possible finding format:** `P1 — Code expired state: the error is announced visually but focus remains on a disabled submit action. Impact: a screen-reader user may not learn the recovery path. Evidence: observed in the tested build; confirm current Android accessibility guidance (registry IDs 82/89). Fix: announce the state, preserve the phone value, and expose an enabled resend/retry action. Verify with TalkBack and keyboard.`

The finding above is an illustrative template, not a claim about a real app. Use source IDs 56, 62–64, 66, 82, 89, and 108 as relevant. Record build, device, Android version, locale, and checks performed.
