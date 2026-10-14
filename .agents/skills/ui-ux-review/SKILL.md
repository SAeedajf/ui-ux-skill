---
name: ui-ux-review
description: Use when auditing an interface for usability, accessibility, or consistency.
---

# Ui Ux Review

Out of scope: backend-only or code-only work with no user-facing interface question; trace UI outcomes only when they are in the requested review scope.

## Workflow
1. Establish scope, user tasks, audience, platforms, locales, target states, constraints, and available evidence.
2. Inspect the actual interface or code at representative sizes and states; distinguish code inspection, rendered inspection, automated checks, and user testing.
3. For visible controls in scope, trace the role and label to the actual link target, event handler, state/data change, and user-visible outcome. Check the key success, pending, error, and recovery paths where present. A local timer or in-memory counter is not evidence of a backend action, durable cart, purchase, or subscription; label simulations accurately.
4. Prioritize findings by user impact and confidence. Each finding includes location, evidence, consequence, recommended change, and verification step. If an apparent action has no outcome, report the mismatch and the product decision needed; do not silently remove or neutralize the affordance unless the user asked for that change or its intended behavior is established.
5. Map findings to applicable standards, research, platform guidance, or clearly labeled design judgment using source IDs. Do not claim conversion impact without relevant measurement.
6. Provide a concise summary, ordered findings, verified aspects, and explicit unknown/unverified areas.

Use `references/review-template.md`. Check the [repository source registry](https://github.com/SAeedajf/ui-ux-skill/blob/main/docs/source-registry.csv) for source access and applicability before using a source claim; if it is unavailable, keep source claims within the evidence actually available and label uncertainty. Select only the focused Skills that match findings: `color-systems`, `ethical-persuasion`, `forms-input`, `information-architecture`, `journey-mapping`, `navigation-controls`, `visual-hierarchy`, or the existing responsive, accessibility, layout, interaction, design-system, and Persian/RTL Skills.
