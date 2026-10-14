# Persian storefront fixture verification

This record covers the local sample at `examples/fixtures/web-store/`. It is a synthetic implementation fixture, not a real shop or user study.

## Changes made

- Changed the product-section link from “دیدن همه” to “خبرهای تازه” because it leads to the newsletter form.
- Gave each repeated add-to-cart button a product-specific accessible name while keeping its visible label concise.
- Added explicit pending, error, and success feedback. The success state has a textual check mark and its own semantic color treatment; it is not communicated by color alone.
- Kept invalid-field focus and the retryable network-failure path, including the entered email value.

## Methods and evidence

| Check | Conditions and result | Method | Limit |
|---|---|---|---|
| Product action names and section link | Accessibility tree showed three distinct names: چراغ آفتاب، چراغ خاک، چراغ زیتون; “خبرهای تازه” points to `#newsletter`. | DOM/accessibility-tree inspection | Does not prove comprehension or task success with users. |
| Mobile navigation | At 390×844, menu opened with `aria-expanded=true`; Escape closed it, set `aria-expanded=false`, and returned focus to the menu trigger. | In-app browser keyboard interaction and accessibility tree | No screen-reader announcement or Android TalkBack check. |
| Invalid email | Empty submission showed a specific error, set `aria-invalid=true`, associated the status text with the field, and focused the field. | In-app browser form submission and accessibility tree | One invalid case; no full input/localization matrix. |
| Recoverable network error | Synthetic `test@example.fail` entered pending state, then showed a retry message while retaining the value. | In-app browser form submission and rendered screenshot | `.fail` is a deterministic local fixture path, not a network request. |
| Success feedback | Valid synthetic email entered pending state, then showed “✓ عضویتت ثبت شد. ممنون!” with a distinct green background and border. | In-app browser form submission and rendered screenshot | No real subscription is sent or stored. |
| Responsive composition | Visually inspected at 390×844, 768×1024, and 1280×900. Mobile navigation collapsed at 390px; three product columns and two-column newsletter appeared at wider widths; no obvious clipping was visible in the inspected states. | Browser viewport screenshots | This is a manual sample, not a complete viewport/orientation/zoom matrix. |
| State text contrast | Error `#8b2f25` on `#fdf0ed`: 7.45:1. Success `#285b36` on `#e4f2e6`: 6.87:1. Both exceed 4.5:1 for normal text. | WCAG relative-luminance calculation, also asserted by `tests/test_web_fixture.py` | These two text pairs do not establish full-page WCAG conformance or other component-state contrast. |

## Source application

- [S48 — Button States: Communicate Interaction](source-registry.csv): used as practitioner guidance for communicating pending/success/error and distinct control labels. Its states guidance does not replace accessibility criteria.
- [S52 — W3C ARIA Authoring Practices](source-registry.csv): consulted for semantics and keyboard interaction expectations; APG is implementation guidance, not itself a WCAG conformance standard.
- [S81 — WCAG 2.2](source-registry.csv): used for the normal-text contrast threshold. The computed color-pair checks are narrow evidence only.

The fixture changes were made directly from the review and repository guidance. No model was invoked during implementation, so the changes are not counted as proof that a Skill automatically activated or caused them. The broad library evaluation remains separate in [the readiness report](operational-readiness.md).
