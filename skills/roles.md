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

## Cross-functional professional profiles

The specialist Skills above are decision lanes. These profiles combine those lanes into common professional responsibilities. A single model or agent can cover a profile; create separate agents only when the work can be independently reviewed or needs parallel expertise. `Source anchors` are direct example links. The `Assigned source IDs` list under each profile is its full source-routing set across the 124 submitted links; a source may support multiple roles because the domains overlap. This routing is based on the reviewed source role, original scope, evidence type, and Skill mapping, but does not claim that every assigned source supports every claim in the profile. Use the [source implementation audit](../docs/source-implementation-audit.csv) to inspect each source-to-Skill trace and [source registry](../docs/source-registry.csv) for review, access, method, date, and claim ceiling.

### R01 — UX problem-framing lead

- **Activate when:** the user goal, audience, success measure, or evidence is unclear.
- **Owns:** turning a vague product request into a focused user problem and deciding whether to research, map, test, or proceed with a bounded hypothesis.
- **Core Skills:** `ux-discovery`; add `information-architecture` or `journey-mapping` only for those separate decisions.
- **Deliverable:** problem statement, known/unknown evidence, decision question, options, and smallest useful validation step.
- **AI workflow:** restate the user decision in one sentence; sort inputs into observed, user-reported, inferred, and missing; choose research only if the missing evidence could change the decision.
- **Completion check:** the brief names one decision owner, one next action, the evidence needed to change course, and any assumption that remains unverified.
- **Source anchors:** [S3 NN/g research index](https://www.nngroup.com/), [S10 Baymard research index](https://baymard.com/research-articles), [S124 journey-mapping practitioner survey](https://www.nngroup.com/articles/journey-mapping-how/).
- **Assigned source IDs (complete set):** `5, 12, 16, 121` — open these rows in the source audit/registry before use.
- **Boundary:** the organization homepages are indexes; cite a specific article for a detailed research claim. A framing hypothesis is not user evidence.

### R02 — UX researcher and method planner

- **Activate when:** the decision depends on user behavior, comprehension, findability, needs, or a disputed assumption.
- **Owns:** choosing a method and participant/task scope that answer the question; preserving accessibility, consent, privacy, and bias considerations in the plan.
- **Core Skills:** `ux-discovery`; hand off taxonomy validation to `information-architecture` and end-to-end experience evidence to `journey-mapping`.
- **Deliverable:** research question, method, participant/task criteria, evidence capture, analysis limits, and decision rule.
- **AI workflow:** translate the decision into a research question; match method and participant/task criteria to that question; define consent, data minimization, capture, analysis, and stop rules before interpreting findings.
- **Completion check:** a plan specifies the question, participant/task scope, method, consent/capture, analysis, and decision rule; completed findings trace to captured evidence and sample limits. A plan or secondary-source statistic is not target-user behavior.
- **Source anchors:** [S99 Optimal Workshop research methods](https://www.optimalworkshop.com/), [S105 card sorting vs. tree testing](https://www.nngroup.com/articles/card-sorting-tree-testing-differences/), [S124 practitioner methods survey](https://www.nngroup.com/articles/journey-mapping-how/).
- **Assigned source IDs (complete set):** `3, 8, 10, 12, 14, 16, 33, 54, 98–106, 116–124` — open these rows in the source audit/registry before use.
- **Boundary:** a vendor's advertised capability does not establish study validity; a study plan or aggregate statistic does not establish what this product's users did.

### R03 — Journey and service designer

- **Activate when:** the user's goal spans stages, channels, service staff, or backstage operations.
- **Owns:** choosing between a journey map, in-product flow, service blueprint, empathy map, or story map and keeping current experience distinct from a proposed future state.
- **Core Skills:** `journey-mapping`; add `ux-discovery`, `information-architecture`, or `navigation-controls` for distinct research, taxonomy, or route questions.
- **Deliverable:** actor and goal, boundaries, stages/touchpoints, responsible handoffs, evidence labels, opportunity hypotheses, and follow-up validation.
- **AI workflow:** set the actor, goal, start/end, channels, and current/future-state boundary; place evidence-backed touchpoints and handoffs; label hypotheses and missing backstage evidence explicitly.
- **Completion check:** each stage has an owner or a stated unknown, and each proposed opportunity links to evidence or a validation question.
- **Source anchors:** [S117 Service Design Tools journey map](https://servicedesigntools.org/tools/journey-map), [S118 GOV.UK experience map](https://www.gov.uk/service-manual/user-research/creating-an-experience-map), [S123 journeys vs. flows](https://www.nngroup.com/articles/user-journeys-vs-user-flows/).
- **Assigned source IDs (complete set):** `116–124` — open these rows in the source audit/registry before use.
- **Boundary:** maps synthesize evidence and do not prove behavior or causality; never invent backstage facts, emotions, or quotes.

### R04 — Information architect and content-structure designer

- **Activate when:** people cannot locate, classify, understand, or navigate content, or the taxonomy is changing.
- **Owns:** content inventory, grouping, labels, hierarchy, cross-links, and the method for evaluating findability.
- **Core Skills:** `information-architecture`; add `navigation-controls` for menu mechanics and `ux-discovery` when audience/task evidence is missing.
- **Deliverable:** inventory and candidate structure, terminology decisions, task-based test plan, and unresolved assumptions.
- **AI workflow:** inventory the in-scope content and destinations; group by user task and source terminology; choose card sorting to explore groupings or tree testing to evaluate a proposed structure; test representative findability tasks.
- **Completion check:** labels and hierarchy can be traced to user tasks or explicitly marked hypotheses, and the validation method tests the actual decision at issue.
- **Source anchors:** [S98 NN/g information architecture](https://www.nngroup.com/topic/information-architecture/), [S105 card sorting vs. tree testing](https://www.nngroup.com/articles/card-sorting-tree-testing-differences/), [S106 NN/g menu-design checklist](https://www.nngroup.com/articles/menu-design/).
- **Assigned source IDs (complete set):** `50, 53–55, 98–106` — open these rows in the source audit/registry before use.
- **Boundary:** card sorting explores possible groupings; tree testing evaluates a proposed hierarchy. Neither alone proves the final taxonomy is preferred or usable in context.

### R05 — Ecommerce and checkout UX specialist

- **Activate when:** product discovery, product details, category/listing, cart, checkout, or purchase recovery is in scope.
- **Owns:** reducing task friction while preserving accurate product, price, delivery, data-use, and commitment information.
- **Core Skills:** `forms-input` or `interaction-patterns` for the main decision; add `information-architecture`, `navigation-controls`, `ethical-persuasion`, or `accessibility-inclusive-design` only when those separate issues are present.
- **Deliverable:** prioritized flow findings, state/recovery requirements, transparent-choice checks, and specific acceptance tests.
- **AI workflow:** trace product discovery through post-purchase or recovery; inspect product/price/availability/delivery claims, field burden, error recovery, and commitment/exit points; validate commercial-source findings against their access limits and the target market.
- **Completion check:** the purchase path has no unexamined commitment, price, delivery, or recovery state in scope, and no benchmark is treated as a forecast for this product.
- **Source anchors:** [S43 Baymard product-page research](https://baymard.com/research/product-page), [S109 Baymard checkout research](https://baymard.com/research/checkout-usability), [S114 phone-field explanation](https://baymard.com/research-articles/explain-phone-number-field), [S115 checkout apply-button research](https://baymard.com/research-articles/checkout-usability-apply-buttons).
- **Assigned source IDs (complete set):** `10, 29, 35, 43, 47, 49, 55, 100, 109, 113–115` — open these rows in the source audit/registry before use.
- **Boundary:** Baymard detailed findings may be Premium; do not reproduce unseen findings or infer this product's conversion impact from a benchmark or case study.

### R06 — Interaction and state designer

- **Activate when:** users need clear feedback, state transitions, reversibility, retry, or error recovery.
- **Owns:** the contract between trigger, system response, visible status, next action, and recovery for each in-scope control.
- **Core Skills:** `interaction-patterns`; add `forms-input` for field behavior, `navigation-controls` for route behavior, and `accessibility-inclusive-design` for semantics/AT checks.
- **Deliverable:** state model covering idle, pending, success, error, disabled, retry, and exit where applicable, with outcomes verified against the real implementation.
- **AI workflow:** for each control, record trigger, precondition, system result, visible feedback, next action, and cancellation/retry path; inspect timing, repeated input, failure, and interruption where relevant.
- **Completion check:** every in-scope state has an observable outcome and recovery rule; a visual mock or client animation is not treated as proof of a server-side result.
- **Source anchors:** [S48 NN/g button states](https://www.nngroup.com/articles/button-states-communicate-interaction/), [S52 W3C ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/patterns/), [S107 GOV.UK components](https://design-system.service.gov.uk/components/).
- **Assigned source IDs (complete set):** `46, 48, 50–52, 107–115` — open these rows in the source audit/registry before use.
- **Boundary:** ARIA patterns are accessibility implementation guidance, not visual design prescriptions. A local animation or mock state does not prove a server-side action.

### R07 — Visual and interface designer

- **Activate when:** a screen needs clearer composition, scan order, spacing, typography, imagery, or visual emphasis.
- **Owns:** translating the user's task and content priority into an interface composition, then checking it in the actual product context.
- **Core Skills:** choose `interface-layout` for composition, `visual-hierarchy` for ordering, or `color-systems` for semantic palette decisions; add `responsive-design` when layouts change across viewports.
- **Deliverable:** hierarchy and layout rationale, use of existing design primitives, and representative rendered-state checks.
- **AI workflow:** inspect the actual screen and task content; set reading/action priority before spacing or decoration; reuse existing primitives; compare representative rendered states and defer separate color, responsive, or system decisions to their owners.
- **Completion check:** the layout expresses the stated task hierarchy in the rendered artifact without unsupported claims about comprehension or preference.
- **Source anchors:** [S74 NN/g visual-design principles](https://www.nngroup.com/articles/principles-visual-design/), [S75 Adobe Spectrum attention hierarchy](https://spectrum.adobe.com/foundations/composition/attention-hierarchy), [S76 Android composition guidance](https://developer.android.com/design/ui/mobile/guides/layout-and-content/content-structure).
- **Assigned source IDs (complete set):** `1–2, 4, 6–8, 11, 18–26, 36–42, 44–45, 57, 59–61, 64, 74–81` — open these rows in the source audit/registry before use.
- **Boundary:** platform guidelines apply to their named ecosystem; examples and visual conventions do not prove that users understand or prefer this design.

### R08 — Design-system architect and steward

- **Activate when:** multiple screens or products need consistent tokens, components, themes, contribution rules, or migration.
- **Owns:** deciding whether a shared primitive is justified and defining its semantics, variants, accessibility contract, consumers, ownership, and rollout.
- **Core Skills:** `design-systems`; add `color-systems`, `interface-layout`, or `responsive-design` for separate token, composition, or adaptation decisions.
- **Deliverable:** documented contract, representative consumers per platform, compatibility risks, migration/rollback plan, and adoption checks.
- **AI workflow:** confirm a repeated cross-screen need before proposing a shared primitive; define semantics, tokens, variants, states, accessibility contract, owners, and platform scope; check representative consumers and a reversible migration path.
- **Completion check:** the contract names supported consumers and limits, and a small adoption check can detect regressions or token drift.
- **Source anchors:** [S90 IBM Carbon](https://carbondesignsystem.com/), [S91 DTCG Design Tokens Format](https://www.designtokens.org/TR/2025.10/format/), [S97 Android Material components](https://developer.android.com/design/ui/mobile/guides/components/material-overview), [S96 Figma workflow guidance](https://www.figma.com/blog/how-to-streamline-your-design-system-workflow-in-figma/).
- **Assigned source IDs (complete set):** `1, 51, 90–97` — open these rows in the source audit/registry before use.
- **Boundary:** S91 defines an interchange format, not a design-system method; S96 is vendor guidance and does not independently prove usability or adoption outcomes.

### R09 — Accessibility and inclusive-design specialist

- **Activate when:** accessibility criteria, assistive technology, cognitive/physical access, inclusive research, or conformance evidence is requested.
- **Owns:** identifying applicable standards and platform guidance, and verifying the actual UI against the requested scope and user needs.
- **Core Skills:** `accessibility-inclusive-design`; add `forms-input`, `interaction-patterns`, `color-systems`, `responsive-design`, or `persian-rtl-localization` for concrete specialist states.
- **Deliverable:** criterion-level findings with route/state, input, tool/device/version, result, impact, remediation, and unverified areas.
- **AI workflow:** choose the applicable standard/target and criterion; inspect the actual route and state with relevant keyboard, zoom, contrast, semantic, and assistive-technology methods; record automated, manual, and user evidence separately.
- **Completion check:** every reported criterion has a reproducible method and status (`pass`, `fail`, `not applicable`, or `not verified`); sampled checks are not generalized to the whole product.
- **Source anchors:** [S81 WCAG 2.2](https://www.w3.org/TR/WCAG22/), [S82 Android accessibility guidance](https://developer.android.com/guide/topics/ui/accessibility/apps), [S89 Compose accessibility codelab](https://developer.android.com/codelabs/jetpack-compose-accessibility).
- **Assigned source IDs (complete set):** `52, 62–63, 81–89, 107` — open these rows in the source audit/registry before use.
- **Boundary:** normative WCAG criteria, platform recommendations, automated scans, and manual/user research evidence are different. A sample does not establish whole-product conformance.

### R10 — Responsive and adaptive product designer

- **Activate when:** supported viewport, window size, orientation, foldable/multi-window posture, or input mode can change content or interaction.
- **Owns:** adapting hierarchy, density, navigation, and control behavior to actual available space rather than shrinking a desktop composition.
- **Core Skills:** `responsive-design`; add `interface-layout`, `design-systems`, or `accessibility-inclusive-design` only for separate concerns.
- **Deliverable:** supported-mode matrix with real dimensions/device constraints, changed behavior, state coverage, and unverified combinations.
- **AI workflow:** establish supported viewport/window and input modes; inspect content priority, navigation, reflow, overflow, and control behavior at representative constraints; keep web breakpoints distinct from native adaptive-window guidance.
- **Completion check:** each claimed mode is tied to a measured viewport/device and rendered state, with unsupported combinations listed as unknown rather than inferred.
- **Source anchors:** [S65 web.dev responsive design](https://web.dev/learn/design/), [S66 Android adaptive layouts](https://developer.android.com/design/ui/mobile/guides/layout-and-content/adapt-layout), [S67 MDN responsive design](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design), [S72 Android adaptive quality](https://developer.android.com/develop/adaptive-apps/quality-guidelines/adaptive-app-quality).
- **Assigned source IDs (complete set):** `9, 11, 15, 17, 42, 65–73, 97` — open these rows in the source audit/registry before use.
- **Boundary:** web breakpoints and Android window/adaptive guidance are not interchangeable. Verify current APIs and report only tested widths/devices.

### R11 — Persian, RTL, and mixed-direction localization specialist

- **Activate when:** Persian/RTL content or mixed Arabic, Persian, Latin, numbers, URLs, email, phone, or code values appear in the interface.
- **Owns:** locale policy, script/font shaping, logical layout, bidi isolation, content expansion, and localized input behavior without imposing RTL on LTR experiences.
- **Core Skills:** `persian-rtl-localization`; add `forms-input`, `responsive-design`, and `accessibility-inclusive-design` for the relevant form, viewport, or assistive-technology checks.
- **Deliverable:** locale decisions and rendered tests using real strings and mixed-direction values across representative states and widths.
- **AI workflow:** confirm locale and direction per surface; exercise real Persian/Arabic/Latin mixtures, numerals, dates, currency, phone/OTP, URLs, and code; inspect logical layout, bidi isolation, font shaping, focus order, and icon meaning.
- **Completion check:** representative mixed-direction strings render and remain operable in the tested states; locale policy and untested language/assistive-technology combinations are explicit.
- **Source anchors:** [S56 W3C Arabic and Persian layout requirements](https://w3c.github.io/alreq/), [S62 W3C inline bidirectional text](https://www.w3.org/International/articles/inline-bidi-markup/index), [S58 Vazirmatn reference](https://github.com/rastikerdar/vazirmatn).
- **Assigned source IDs (complete set):** `56–64, 114` — open these rows in the source audit/registry before use.
- **Boundary:** apply language and digit conventions from the confirmed product policy; do not infer Arabic/Persian behavior from generic RTL assumptions or mirror every icon.

### R12 — Ethical behavior and growth specialist

- **Activate when:** a design seeks to influence conversion, engagement, habit, purchase, subscription, renewal, or user choice.
- **Owns:** confirming user benefit, informed choice, fair prominence of alternatives, clear commitment/exit terms, and outcome guardrails beyond business conversion.
- **Core Skills:** `ethical-persuasion`; add `ux-discovery`, `interaction-patterns`, or `journey-mapping` for evidence, choice states, or cross-stage consequences.
- **Deliverable:** choice-architecture review, user-value evidence, opt-out/reversal checks, follow-up measures, and stop/remediation thresholds.
- **AI workflow:** map the requested behavior and affected users; inspect prominence and clarity of accept/decline, cost/data/commitment disclosure, exit and reversal; define a user-value measure and guardrails before proposing optimization.
- **Completion check:** the proposed change preserves informed, reversible choice and has an outcome measure that can reject a conversion gain that harms users.
- **Source anchors:** [S28 Stanford Fogg Behavior Model](https://behaviordesign.stanford.edu/resources/fogg-behavior-model), [S29 Baymard conversion research](https://baymard.com/blog/knowledge-hub?category=conversion-optimization), [S35 Baymard cart-abandonment guidance](https://baymard.com/blog/reduce-cart-abandonment).
- **Assigned source IDs (complete set):** `5, 13, 27–35` — open these rows in the source audit/registry before use.
- **Boundary:** behavioral models and commercial case studies generate hypotheses; they neither guarantee lift nor justify deception, coercion, or hiding a decline/cancel path.

### R13 — UI/UX quality review lead

- **Activate when:** the user requests a broad audit or needs findings coordinated across multiple UI concerns.
- **Owns:** review scope, evidence separation, impact/confidence ranking, and routing to the smallest set of specialist roles.
- **Core Skills:** `ui-ux-review`; call in only the specialist profiles required by evidence and acceptance checks.
- **Deliverable:** prioritized findings with location, observed evidence, user impact, recommendation, concrete verification, and explicit unknowns.
- **AI workflow:** define routes/states and review limits; inspect the artifact; rank findings by user impact and confidence; attach one focused specialist handoff and a testable acceptance check to each material finding.
- **Completion check:** each finding has location, evidence class, impact, recommendation, and verification; unknowns remain visible, and review has not silently expanded into implementation.
- **Source anchors:** [S81 WCAG 2.2](https://www.w3.org/TR/WCAG22/) for applicable normative checks, [S87 WebAIM Million report](https://webaim.org/projects/million/), and the exact topic source selected for each finding. Use [`review-template.md`](../.agents/skills/ui-ux-review/references/review-template.md) and the audit CSV for traceability.
- **Assigned source IDs (complete set):** `81, 87–88` — open these rows in the source audit/registry before use.
- **Boundary:** broad review is not permission to redesign or implement. A population report, checklist, screenshot, or code scan is not proof that the target product is usable or conformant.

## Profile selection

Choose a profile by the decision to make, not by job title keywords. For a multi-part request, assign one lead profile and name the additional profile only for a separate acceptance check. Preserve the user-selected model and the host's available model; these profiles describe work, not model restrictions or a mandate to create subagents.
