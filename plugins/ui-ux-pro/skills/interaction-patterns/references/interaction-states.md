# Interaction states and recoverability

- Map each control to action, result, validation, and next step. Use semantic controls and preserve keyboard, focus, screen-reader, and touch behavior.
- For product detail/listing interactions, start with **43–49**; for navigation controls, use **50–55**; for forms, use **107–115**. Registry entries include platform and access notes.
- Include idle, focused, disabled, loading, success, error, and retry/cancel states when the interaction can reach them. Do not disable a control without explaining why and how to recover.
- For asynchronous form actions, test stale-response protection when a flow changes, cancellation/cleanup of pending work, duplicate-submit prevention, and restoration after failure. For code resend, verify expiry, cooldown, a fresh logical request, retained destination, and focus/error recovery; do not infer server rate limiting or idempotency from client-only controls.
- Validate inline when it helps the user fix a problem; preserve entered values after recoverable errors. Avoid arbitrary format rules and destructive clearing.
- Persuasion should be transparent and reversible. Do not hide costs, force consent, fake scarcity, or obstruct cancellation. Findings in commercial studies may not transfer to a different population or task.

## Product selection and feedback

- For a product detail flow, trace the actual decision path: inspect product information → select a variant/options → confirm the resulting price and availability → choose quantity → submit the purchase action → recover from an unavailable/failed state. Match the flow to this catalog and business rules; the ecommerce research in **43** and **47** is scoped to product pages, and premium guideline details were not available.
- For a product listing, inspect how people scan and compare items, how filters/sort change the results, and whether returning from a detail page preserves useful context. Source **49** covers ecommerce listings; treat its statistics as scoped evidence, not a universal conversion guarantee.
- Specify a microinteraction with **trigger → rules → feedback → mode/loop → exit or recovery**. Use this as a checklist derived from the table of contents of **46**; the full book was not read. Keep feedback perceivable without color or motion alone, allow user control, and honor reduced-motion settings.
- For button feedback, test enabled/disabled, hover where a pointer exists, keyboard focus, pressed, selected, loading, and completion/error states. Attribute that state guidance to **[S48]** when it informs a recommendation; it is practitioner research, not an accessibility standard. Hover is not evidence for touch behavior.
- If color communicates selection, stock, or action priority, consult `color-systems` and use the applicable WCAG criterion for rendered contrast. Cite **[S44]** only as an example of Atlassian's own token system; do not copy its values or names unless the product adopts that system. **S45** is an ebook listing, not a full-text review; explicitly reject its color/conversion claims as evidence for a universal answer.

## Source boundaries

Starting sources: [S43 Baymard product page research](https://baymard.com/research/product-page), [S44 Atlassian semantic color guidance](https://atlassian.design/foundations/color), [S45 Colin Shanley, *Colour in User Interface Design*](https://play.google.com/store/books/details?id=By7vDwAAQBAJ), [S46 Dan Saffer, *Microinteractions: Designing with Details*](https://www.oreilly.com/library/view/microinteractions-full-color/9781491945957/), [S47 Baymard product page UX](https://baymard.com/research-articles/current-state-ecommerce-product-page-ux), [S48 Nielsen Norman Group button states](https://www.nngroup.com/articles/button-states-communicate-interaction/), and [S49 Baymard product listing UX](https://baymard.com/blog/product-listing-page-plp-ux). Check the source registry for paywall, sample, publication-date, and platform scope before attaching any specific research claim.

When a request explicitly asks to use the reference set, include a compact source-to-decision table so another reviewer can see which method informed which decision and what the source cannot establish. Do not pad a narrow interaction answer with unrelated citations; mark a source as not used when its subject does not affect the task.

| Source | Apply when | Operational method | Limit |
|---|---|---|---|
| S43 and S47 | Product detail or variant selection | Trace information → options → price/availability → quantity → purchase → recovery; use the current public guidance and the overview as scoped context. | Ecommerce scope; detailed findings may be premium. |
| S49 | Product listing/catalog comparison | Inspect scan, comparison, filters/sort, and return context. | Ecommerce listing scope; validate catalog and population fit. |
| S46 | Small feedback behavior | Specify trigger, rules, feedback, mode/loop, exit/recovery; test the interaction in context. | Publisher contents only; the full book was not reviewed. |
| S48 | Button/control state clarity | Check enabled, disabled, hover, keyboard focus, pressed/selected, loading, and outcome. | Practitioner guidance; not a normative accessibility standard. |
| S44 | Color tokens represent state | Compare semantic color-role naming with the actual product system. | Atlassian-specific; do not copy without adopting that system. |
| S45 | A color-psychology claim is requested | Do not use the book listing as research evidence; route palette/contrast decisions to `color-systems` and WCAG. | Store listing only; full book was not read and its conversion claims are not established. |
