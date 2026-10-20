# UI/UX Skill inventory

Canonical definitions are in `.agents/skills/<name>/SKILL.md`. Skills are independently installable. No per-Skill release version is declared in this repository; use the repository commit/release tag for provenance. Optional handoffs below are routing suggestions, not hard dependencies.

The [specialist role catalog](roles.md) expands these short purpose statements into decision ownership, expected outputs, handoffs, and source bases. Use it to route the task to one accountable role first; it does not require creating a separate agent for every Skill.

| Skill | Purpose and boundary | Optional handoffs | Version | Quality evidence |
|---|---|---|---|---|
| `accessibility-inclusive-design` | Accessibility requirements and inclusive interaction; separates web criteria from platform guidance and verified AT behavior. | `interaction-patterns`, `forms-input`, `color-systems`, `persian-rtl-localization` | Unversioned | PASS: quality-06, 13, 15, 23, 28 |
| `color-systems` | Semantic color roles, palette/theme choices, and contrast checks; does not claim universal meanings or conversion effects. | `accessibility-inclusive-design`, `design-systems` | Unversioned | PASS: quality-01, 02, 13 |
| `design-systems` | Reusable tokens, components, theming, adoption, and governance; requires evidence before introducing shared primitives. | `interface-layout`, `responsive-design` | Unversioned | PASS: quality-09, 23 |
| `ethical-persuasion` | Transparent influence and choice architecture; rejects deceptive pressure and hidden controls. | `interaction-patterns`, `forms-input`, `journey-mapping` | Unversioned | PASS: quality-08, 14 |
| `forms-input` | Field purpose, input constraints, validation, and safe error recovery; does not assume causes from abandonment alone. | `interaction-patterns`, `persian-rtl-localization`, `accessibility-inclusive-design` | Unversioned | PASS: quality-03, 07, 18, 23, 26 |
| `information-architecture` | Content grouping, taxonomy, labels, and findability; hypotheses require user/task evidence before validation claims. | `ux-discovery`, `navigation-controls` | Unversioned | PASS: quality-17 |
| `interaction-patterns` | Control behavior, state transitions, feedback, and recovery; distinguishes local state from service outcomes. | `forms-input`, `navigation-controls`, `accessibility-inclusive-design` | Unversioned | PASS: quality-07, 15, 21, 24, 26 |
| `interface-layout` | Page composition, spacing, cards, and layout using existing system primitives. | `visual-hierarchy`, `responsive-design`, `design-systems` | Unversioned | PASS: quality-20, 27 |
| `journey-mapping` | Evidence-labeled end-to-end and cross-channel experiences; unknown backstage facts remain unknown. | `ux-discovery`, `information-architecture` | Unversioned | PASS: quality-19, 21 |
| `navigation-controls` | Wayfinding, route menus, action buttons, current-location cues, and keyboard behavior. | `interaction-patterns`, `accessibility-inclusive-design` | Unversioned | PASS: quality-15, 25, 26 |
| `persian-rtl-localization` | Persian/RTL and mixed-direction localization; preserves provider-required identifier formats and locale policy. | `forms-input`, `responsive-design`, `accessibility-inclusive-design` | Unversioned | PASS: quality-03, 04, 20 |
| `responsive-design` | Responsive web and adaptive Android behavior across viewports/devices; only claims states actually inspected. | `interface-layout`, platform adapters, `accessibility-inclusive-design` | Unversioned | PASS: quality-05, 20, 29 |
| `ui-ux-review` | Broad evidence-based interface audit and prioritized report; routes focused findings to specialists. | Any specialist required by a distinct finding | Unversioned | PASS: quality-06, 13, 15, 25 |
| `ux-discovery` | User goals, research evidence, and unresolved product questions; keeps discovery proportionate to decision risk. | `information-architecture`, `journey-mapping` | Unversioned | PASS: quality-11, 17, 21 |
| `visual-hierarchy` | Content emphasis and task-based scan order; proposals remain provisional without rendered/user evidence. | `interface-layout`, `accessibility-inclusive-design` | Unversioned | PASS: quality-16 |

Quality statuses refer to the scenario ledger, not a claim that every Skill was comprehensively validated. The latest results show 29 PASS in [`evals/results/quality.jsonl`](../evals/results/quality.jsonl). An earlier usage-limited quality-26 attempt and the exploratory quality-29 run remain as historical evidence. Codex activation traces remain pending whole-trace human attestation; Android runtime remains blocked by missing toolchain. See [operational readiness](../docs/operational-readiness.md).
