# UI/UX specialist roles

These are decision-owning roles for a task, not a requirement to load 15 agents or Skills at once. Use one primary role for the main unresolved decision and add a specialist only when the task crosses a separate boundary or needs its own acceptance check. The linked source IDs are the library's starting points, not proof that every source supports every decision. Open the matching reference and registry entry; respect its evidence type, access, date, and claim limits.

## Discovery and structure

### UX discovery lead — `ux-discovery`

- **Owns:** framing the product question, user goal, audience, constraints, known evidence, and the lightest research method that can resolve uncertainty.
- **Produces:** a decision brief with observations, reports, assumptions, hypotheses, alternatives, and a validation plan.
- **Hands off:** taxonomy/findability to `information-architecture`; cross-stage experiences to `journey-mapping`; settled implementation questions to the owning design Skill.
- **Source basis:** foundational research and product guidance S1–17 plus relevant topic sources selected from the registry. Start at [`discovery.md`](../.agents/skills/ux-discovery/references/discovery.md); the homepage/index references are not evidence for specific claims.

### Journey and service mapper — `journey-mapping`

- **Owns:** selecting and constructing an evidence-labeled journey map, in-product flow, service blueprint, empathy map, or story map across the task's time horizon and channels.
- **Produces:** actor, goal, scope, stages/touchpoints, current vs. proposed state, evidence labels, service handoffs, and the next validation step.
- **Hands off:** user research gaps to `ux-discovery`; content grouping to `information-architecture`; in-product route behavior to `navigation-controls`.
- **Source basis:** S116–124. Start at [`journey-artifacts.md`](../.agents/skills/journey-mapping/references/journey-artifacts.md); distinguish user journeys from product flows and service maps from assumptions.

### Information architect — `information-architecture`

- **Owns:** content inventory, grouping, taxonomy, labels, hierarchy, cross-links, and the method for testing findability.
- **Produces:** candidate structures, terminology decisions, method selection, and a task-based validation plan.
- **Hands off:** menu mechanics to `navigation-controls`; unresolved audience or task evidence to `ux-discovery`.
- **Source basis:** S98–106. Start at [`ia-methods.md`](../.agents/skills/information-architecture/references/ia-methods.md); card sorting explores groupings, while tree testing evaluates a proposed hierarchy.

## Visual design and systems

### Interface composition designer — `interface-layout`

- **Owns:** page-level composition, grids, spacing, component placement, and how the layout uses existing product primitives.
- **Produces:** a layout proposal tied to content, task, actual constraints, and existing tokens/components.
- **Hands off:** content priority to `visual-hierarchy`; shared primitive changes to `design-systems`; viewport behavior to `responsive-design`.
- **Source basis:** S1–17 and S36–42, with applicable visual-design material S74–80. Start at [`composition.md`](../.agents/skills/interface-layout/references/composition.md); platform systems are examples for their own ecosystems.

### Visual hierarchy designer — `visual-hierarchy`

- **Owns:** the intended first, second, and supporting read; emphasis and scan order for a specific user task.
- **Produces:** ranked content/action priorities and the visual cues that express them, checked against reading and focus order.
- **Hands off:** spacing and page composition to `interface-layout`; color semantics to `color-systems`; validation of user comprehension to `ux-discovery`.
- **Source basis:** S74–80. Start at [`hierarchy-audit.md`](../.agents/skills/visual-hierarchy/references/hierarchy-audit.md); design principles and examples are not proof that users noticed or understood the hierarchy.

### Color and theme specialist — `color-systems`

- **Owns:** semantic color roles, palette/theme relationships, status encoding, and rendered color-pair checks.
- **Produces:** semantic role assignments and a tested matrix of relevant foreground/background, state, and theme pairs.
- **Hands off:** shared token changes to `design-systems`; broader non-color accessibility checks to `accessibility-inclusive-design`.
- **Source basis:** S18–26 and normative contrast criteria in S81. Start at [`color-decision.md`](../.agents/skills/color-systems/references/color-decision.md); palette generators and color-psychology articles are ideation or hypotheses, not conformance evidence.

### Design-system steward — `design-systems`

- **Owns:** whether a repeated need merits a shared token/component, its semantic contract, adoption boundaries, and governance/migration plan.
- **Produces:** token/component contract, supported variants and states, representative consumers, compatibility risks, and staged adoption checks.
- **Hands off:** one-screen composition to `interface-layout`; responsive implementation to `responsive-design`; accessibility contract checks to `accessibility-inclusive-design`.
- **Source basis:** S90–97. Start at [`system-principles.md`](../.agents/skills/design-systems/references/system-principles.md); DTCG, platform systems, Figma vendor guidance, and practitioner books have different authority and scope.

## Interaction and decision architecture

### Interaction designer — `interaction-patterns`

- **Owns:** component behavior, state transitions, feedback, reversibility, and recovery from errors or interrupted tasks.
- **Produces:** a state model that traces each visible control through trigger, system response, and user-visible outcome.
- **Hands off:** field entry and validation to `forms-input`; destinations and wayfinding to `navigation-controls`; semantics/AT verification to `accessibility-inclusive-design`.
- **Source basis:** S43–55 and S107–115. Start at [`interaction-states.md`](../.agents/skills/interaction-patterns/references/interaction-states.md); commercial studies and design-system patterns do not establish behavior in the target product.

### Forms and input specialist — `forms-input`

- **Owns:** field necessity, labels, input methods, validation timing, data preservation, error recovery, and submission states.
- **Produces:** field contract and valid/invalid/retry/success state checks, including localized and sensitive values.
- **Hands off:** general control-state behavior to `interaction-patterns`; Persian/mixed-direction input to `persian-rtl-localization`; assistive-technology checks to `accessibility-inclusive-design`.
- **Source basis:** S107–115. Start at [`form-review.md`](../.agents/skills/forms-input/references/form-review.md); paid checkout findings, platform examples, and practitioner methods retain their stated access and scope limits.

### Navigation and controls specialist — `navigation-controls`

- **Owns:** destinations, menu structure, current-location cues, action-vs-link semantics, and the route for continuing or returning.
- **Produces:** destination/label map plus keyboard, focus, overflow, and dead-end checks.
- **Hands off:** content grouping to `information-architecture`; stateful control behavior to `interaction-patterns`; full keyboard/AT assessment to `accessibility-inclusive-design`.
- **Source basis:** S50–55 and the IA/journey sources S98–124 when they address routes or user flows. Start at [`navigation-controls.md`](../.agents/skills/navigation-controls/references/navigation-controls.md); ARIA APG describes accessible interaction patterns, not a mandate to use a particular visual design.

### Ethical behavior designer — `ethical-persuasion`

- **Owns:** whether influence supports a user-valued outcome, preserves informed choice, and gives a usable way to decline, exit, or reverse a commitment.
- **Produces:** a choice-architecture review, user-value evidence needs, guardrails, and outcome/stop measures beyond conversion.
- **Hands off:** behavior research to `ux-discovery`; states and exits to `interaction-patterns`; multi-step service impact to `journey-mapping`.
- **Source basis:** S27–35. Start at [`ethical-review.md`](../.agents/skills/ethical-persuasion/references/ethical-review.md); models and case studies generate hypotheses and do not guarantee lift or justify coercion.

## Adaptation, inclusion, and review

### Responsive and adaptive design specialist — `responsive-design`

- **Owns:** content and interaction adaptation across actual viewport/window sizes, orientation, input modes, and supported platform constraints.
- **Produces:** a mode matrix with the changed hierarchy/navigation/interaction and the exact rendered states verified.
- **Hands off:** page composition to `interface-layout`; shared responsive primitives to `design-systems`; accessibility states to `accessibility-inclusive-design`.
- **Source basis:** S36–42 and S65–73. Start at [`adaptation.md`](../.agents/skills/responsive-design/references/adaptation.md); distinguish web breakpoints from Android window/adaptive guidance and verify current platform docs for implementation.

### Accessibility and inclusive design specialist — `accessibility-inclusive-design`

- **Owns:** applicable standard/target selection and evidence for semantics, keyboard, focus, contrast, reflow, motion, and relevant assistive technology behavior.
- **Produces:** criterion-level checks with artifact/state/tool/version and checked, not checked, or not applicable status.
- **Hands off:** fixes to the owning component Skill; keeps automated scans, manual checks, and user research as distinct evidence.
- **Source basis:** normative S81; platform guidance S82, S83, S89; supporting practice/report sources S84–88. Start at [`verification.md`](../.agents/skills/accessibility-inclusive-design/references/verification.md); no single sample or automated scan establishes whole-product conformance.

### Persian RTL localization specialist — `persian-rtl-localization`

- **Owns:** locale/direction policy, Persian typography and shaping, bidi isolation, localized values, and RTL behavior without imposing RTL on LTR products.
- **Produces:** locale-specific decisions and mixed-direction checks for real content across widths, input types, focus, and text scaling.
- **Hands off:** field validation to `forms-input`; layout adaptation to `responsive-design`; assistive-technology checks to `accessibility-inclusive-design`.
- **Source basis:** S56–64 plus form-related S107–115 when the task includes localized inputs. Start at [`persian-rtl-checks.md`](../.agents/skills/persian-rtl-localization/references/persian-rtl-checks.md); standards, font references, books, and platform typography guidance are not interchangeable.

### UI/UX review lead — `ui-ux-review`

- **Owns:** broad, in-scope interface inspection; severity/confidence ordering; evidence labeling; and routing each finding to the right specialist.
- **Produces:** findings with location, user impact, evidence class, concrete fix, and acceptance check, plus explicit unknowns.
- **Hands off:** specialized decisions to the smallest applicable Skills; does not convert a review into implementation without that request.
- **Source basis:** S81–89 establish accessibility review sources; select topic-specific sources from the other domains for each finding. Start at [`review-template.md`](../.agents/skills/ui-ux-review/references/review-template.md) and use `docs/source-implementation-audit.csv` to trace a claim to the exact link and Skill reference.

## Routing rule

The role that owns the main unresolved product decision is primary. Add a second role only when it owns a distinct decision or acceptance check; share the evidence packet and explicit handoff, not the full context dump. A role or source link is a routing aid, not evidence that the target interface passed review.
