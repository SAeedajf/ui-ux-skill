---
name: navigation-controls
description: Use when designing menus, wayfinding, or action buttons.
---

# Navigation and Controls

Out of scope: form validation or a control's internal state when destinations, wayfinding, menus, and action-vs-link semantics are unchanged; use `forms-input` or `interaction-patterns`.

Help people understand where they are, what a control will do, and how to continue or return.

## Workflow
1. Identify the user's destination or task, information depth, platform, input modes, and available routes.
2. Choose navigation patterns that fit the content structure and frequency of use. Keep labels familiar and specific; show current location and preserve a predictable way back.
3. Distinguish navigation from actions. Use links for destinations and buttons for actions; label icon-only controls accessibly and avoid ambiguous symbols without context. Label a route map as proposed until you verify it in the actual product.
4. Review hierarchy, touch/keyboard reach, focus placement when menus open and close, Escape behavior, selected/current state, overflow, responsive changes, and recovery from dead ends. Do not rely on color or icon shape alone.
5. Verify with representative tasks and real routes or prototypes. Record what was inspected and what remains untested.

For pattern boundaries and source notes, see `references/navigation-controls.md`. Hand off component-state logic to `interaction-patterns`, multi-field forms to `forms-input`, and a full keyboard/AT audit to `accessibility-inclusive-design`.

**Navigation output:** state the proposed destinations, labels, current-location cue, and whether each item navigates or acts; include the routes/states inspected and what remains untested.
