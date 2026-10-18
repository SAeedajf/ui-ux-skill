---
name: forms-input
description: Use when designing form fields, validation, or error recovery.
---

# Forms and Input

Out of scope: static text or page styling when field choice, entry, validation, submission, or recovery behavior is unchanged.

Make it clear what information is needed, why it is needed, how to enter it, and how to recover from a problem.

## Workflow
1. Map the user's task, each requested field, why it is necessary, data sensitivity, platform, locale, and downstream effect. Remove fields without a justified need.
2. Give each field a visible, persistent label; explain required status and non-obvious constraints before entry. Choose suitable input, autocomplete, keyboard, and formatting behavior for the platform and locale.
3. Design validation around the user's next action: validate at an appropriate point, associate errors with fields, explain what happened and how to fix it, and preserve safe entered values. Keep normalization separate from parsing and validation; do not silently discard unsupported input or truncate fixed-length security codes before checking the full value. Avoid clearing the entire form after a recoverable error.
4. Cover focus, keyboard, screen-reader announcement, loading, disabled, success, retry, and duplicate-submit states. Trace each visible control to its handler and user-visible outcome, including password visibility, recovery, remember-me, and provider actions. Confirm data handling and sensitive-field retention are appropriate before preserving values.
5. Test realistic valid/invalid inputs, long and localized content, mobile keyboards, and error recovery. Report the exact interface and states checked; do not claim behavior or compliance without evidence.

For authentication-like forms, distinguish client-side validation from authentication. Do not imply a demo signed a user in, saved a session, sent a recovery request, or connected a provider. Confirm whether data stays local; do not claim encryption or security properties without evidence from the actual transport and service. When a prototype is meant to submit locally only, verify that submission makes no network request. Define email/phone acceptance from the confirmed product and locale contract, not a guessed regional rule.

For field and recovery review, read `references/form-review.md`. Hand off route menus to `navigation-controls`, detailed non-form component behavior to `interaction-patterns`, Persian/RTL localization to `persian-rtl-localization`, and a full accessibility audit to `accessibility-inclusive-design`.
