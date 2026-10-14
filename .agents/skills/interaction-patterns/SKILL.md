---
name: interaction-patterns
description: Use when designing control states, feedback, and recovery.
---

# Interaction Patterns

Out of scope: a static content hierarchy or visual-only adjustment with no action, state, feedback, or recovery behavior to decide.

## Workflow
1. Trace the user goal from entry to completion, including alternate, error, cancel, and recovery paths.
2. Inspect existing components, semantics, labels, input constraints, keyboard/touch behavior, and platform conventions.
3. Make action, consequence, state, and next step clear. Keep errors specific, timely, recoverable, and associated with the affected field.
4. Minimize unnecessary steps only when task safety, user control, and data quality remain intact. Do not use deceptive urgency or hidden consent.
5. Verify keyboard/focus, screen reader names and state, touch targets, loading/empty/error/success cases, and localization.

Read `references/interaction-states.md` for focused patterns. Use `navigation-controls` for route menus/wayfinding, `forms-input` for field and submission behavior, `ethical-persuasion` for influence or choice architecture, `accessibility-inclusive-design` for deeper standards or assistive-technology review, and `responsive-design` when layout modes are in scope.
