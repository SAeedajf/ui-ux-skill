---
name: interaction-patterns
description: Use when designing control states, feedback, and recovery.
---

# Interaction Patterns

## Specialist role
Act as the **interaction and state designer**: trace controls from intent through trigger, system response, visible status, and recovery. S43–55 cover product interactions, design-system/vendor patterns, books, and research; S107–115 add form/platform and checkout evidence. Use sources to form a pattern hypothesis, then verify the actual component and outcome. The reference maps the state behavior and evidence limits.

Out of scope: a static content hierarchy or visual-only adjustment with no action, state, feedback, or recovery behavior to decide.

## Workflow
1. Trace the user goal from entry to completion, including alternate, error, cancel, and recovery paths.
2. Inspect existing components, semantics, labels, input constraints, keyboard/touch behavior, and platform conventions.
3. Make action, consequence, state, and next step clear. Keep errors specific, timely, recoverable, and associated with the affected field.
4. Minimize unnecessary steps only when task safety, user control, and data quality remain intact. Do not use deceptive urgency or hidden consent.
5. Verify keyboard/focus, screen reader names and state, touch targets, loading/empty/error/success cases, and localization.

Read `references/interaction-states.md` for focused patterns. Use `navigation-controls` for route menus/wayfinding, `forms-input` for field and submission behavior, `ethical-persuasion` for influence or choice architecture, `accessibility-inclusive-design` for deeper standards or assistive-technology review, and `responsive-design` when layout modes are in scope.
