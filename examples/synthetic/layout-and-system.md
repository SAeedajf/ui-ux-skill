# Synthetic example: content pressure and shared components

This is a made-up Persian RTL storefront example. It demonstrates a decision record; it is not a tested interface or user-research result.

## Request and constraints

- Task: help a shopper compare a product and reach the purchase action.
- Content: a long Persian product title, a two-line availability message, one price, and a primary purchase button.
- Existing system: semantic spacing tokens, `text-body` and `text-title` roles, and a shared `PrimaryAction` component. No token values or screenshots were supplied.
- Platforms: web and Android; no runtime artifacts were supplied.

## Decision record

| Decision | Rationale | Status |
|---|---|---|
| Keep product title and price adjacent in reading order; allow the title to wrap without truncation. | The task requires comparing identity and cost before purchase; truncation could hide distinguishing text. | Proposed; inspect the real content and visual order. |
| Place the purchase action after availability and price on narrow web screens. | Keeps the action near the information required to decide. | Proposed; validate scroll and focus order in the rendered page. |
| Reuse `PrimaryAction` semantics and existing spacing/type roles. | Repeated patterns should use the system contract when it fits. | User-reported system inventory; component API not inspected. |
| Keep Android button placement and sizing platform-specific while sharing label meaning, disabled/loading/error states, and accessibility name. | Consistent meaning does not require identical platform rendering. | Proposed; check the actual Android component and platform conventions. |

## Evidence matrix

| Target | State/input | Criterion | Method | Result |
|---|---|---|---|---|
| Narrow web | Long title, two-line availability, loading button | No clipped title; price and action remain understandable; loading state communicates progress | Not run; no page or browser artifact | Unverified |
| Wider web | Same content, keyboard input | Content grouping remains clear; focus order follows task order | Not run; no page or browser artifact | Unverified |
| Android | Same content, TalkBack and touch | Accessible action name; state announced; touch target meets project/platform criterion | Not run; no app or emulator artifact | Unverified |

## What to request next

Provide the relevant screen or route, token/component definitions, supported viewport/window classes, and any target-specific acceptance criteria. Then inspect those artifacts and replace each proposal with an observed result only after running the stated check.
