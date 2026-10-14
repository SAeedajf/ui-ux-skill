# Form review

## Field review

- Can the field be removed or derived from existing information? Explain why sensitive or contact data is needed.
- Does each field have a persistent visible label, clear required/optional status, and useful help before entry?
- Are input type, autocomplete, keyboard, allowed format, examples, and length appropriate to actual platform and locale rules?
- Are constraints communicated before submission where possible? Avoid rejecting valid regional formats based on an assumed locale.
- For errors, identify the field, describe the problem in plain language, provide a correction path, move or retain focus intentionally, and preserve safe values.
- For submission, show progress, prevent accidental duplicate submission, give a clear result, and provide retry/recovery without losing work when safe.
- Verify keyboard order, label/error association, focus visibility, screen-reader announcement, zoom, and localized layouts with the actual implementation.

## Recovery state record

For each failure that interrupts the task, record the trigger, visible message, field association, focus destination, retained values by sensitivity, and the next safe action. For network retries or resend actions, verify duplicate-submit/idempotency behavior when the system exposes it.

| Trigger | Error and association | Focus destination | Retained values | Recovery action |
|---|---|---|---|---|
| Client validation | State the invalid field and correction | Invalid field or error summary, according to form length | Keep unrelated, non-sensitive values | Correct and resubmit |
| Server/network error | Explain failure and whether submission may have completed | Summary or retry control | Preserve safe values; avoid repeating irreversible action blindly | Retry, check status, or contact support |
| OTP expired/incorrect | Identify the code field and expiry/retry condition | Code field or announced summary | Clear expired/secret code only when policy requires; keep safe contact context | Request new code or edit destination |

Treat this as a proposal until the actual form, persistence policy, and platform behavior have been inspected. Record `observed`, `user-reported`, `inferred`, or `proposed` for each entry.

## Evidence and handoffs

A text description can support a proposed checklist, not verification of an unseen form. Mark each observation as observed, user-reported, inferred, or proposed. Apply platform or locale policy only after confirming it; refer Persian/RTL-specific direction, numerals, and mixed-script behavior to `persian-rtl-localization`.

## Source boundaries

This independent checklist synthesizes form guidance and does not reproduce paid publications, article text, or proprietary components. Check registry access notes. Design-system pages provide patterns, not proof that an implementation works for a given user group.

Starting sources: [S107 GOV.UK Design System components](https://design-system.service.gov.uk/components/), [S108 Android Developers text in Compose](https://developer.android.com/develop/ui/compose/text), [S109 Baymard checkout usability research](https://baymard.com/research/checkout-usability), [S110 Adam Silver, *Form Design Patterns*](https://www.smashingmagazine.com/printed-books/form-design-patterns/), [S111 Luke Wroblewski, *Web Form Design*](https://rosenfeldmedia.com/books/web-form-design/), [S112 Jessica Enders, *Designing UX: Forms*](https://www.sitepoint.com/premium/books/designing-ux-forms/), [S113 Baymard current checkout UX](https://baymard.com/research-articles/current-state-of-checkout-ux), [S114 Baymard phone-field explanation](https://baymard.com/research-articles/explain-phone-number-field), [S115 Baymard checkout apply-button research](https://baymard.com/research-articles/checkout-usability-apply-buttons).
