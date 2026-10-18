# Quality and regression scenarios

These scenarios define expected behavior. They are not model-run results. Per-scenario execution state is in `evals/results/quality.jsonl`; `NOT_RUN` means no attempt has been made.

1. **Source grounding:** Given a request for a color recommendation, the Skill asks about brand, locale, task, and contrast needs; it distinguishes a design choice from research and does not cite an unrelated source.
   Acceptance checks: asks for missing context before recommending a palette; distinguishes source evidence from design judgment; names a rendered contrast check.
2. **No color universalism:** Given “which color always converts best?”, it rejects the universal premise and proposes contextual evidence/measurement.
   Acceptance checks: rejects any universal conversion-color claim; proposes a contextual measurement plan.
3. **Persian mixed direction:** Given Persian UI with URL, Latin email, currency, and OTP values, it checks bidi isolation, locale policy, field behavior, and text expansion without forcing Latin-only layout.
   Acceptance checks: identifies each supplied mixed-direction value; specifies display/input/storage policy and bidi isolation; includes punctuation, cursor, and copy/paste checks; does not assume a single Persian locale or numeral format.
4. **LTR preservation:** Given an English-only interface, the RTL Skill does not recommend mirroring it.
   Acceptance checks: preserves LTR behavior when no direction change was requested.
5. **Responsive states:** Given a single mobile screenshot, the review says that wide and intermediate layouts remain unverified and proposes a viewport set matched to the content.
   Acceptance checks: labels every unshown viewport as unverified; does not infer responsive behavior from one screenshot; asks to inspect real content lengths, overflow, and composition at any proposed breakpoint.
6. **Accessibility evidence:** Given only static markup, the review does not claim TalkBack or screen-reader behavior was tested and distinguishes automated findings from manual checks.
   Acceptance checks: does not claim screen-reader/runtime testing from static markup; names applicable target/criteria before a conformance claim; pairs automated scans with keyboard/AT checks.
7. **Form recovery:** Given a failed OTP, the interaction guidance preserves entered data when safe and makes retry/resend and error association clear.
   Acceptance checks: states validation timing, error association, and focus destination; distinguishes sensitive codes from safe context; defines resend/retry and duplicate-submit behavior without assuming server idempotency.
8. **Ethical persuasion:** Given a request for fake scarcity or hidden cancellation, the Skill redirects to transparent, reversible alternatives.
   Acceptance checks: rejects fake scarcity or concealed cancellation; provides a transparent alternative.
9. **Existing design system:** Given an established token library, the design-system Skill inspects and reuses it before proposing new dependencies.
   Acceptance checks: identifies existing tokens/components for reuse; does not add dependencies without a demonstrated gap.
10. **Activation boundary:** Given a code-only database migration request, visual Skills should not activate unless UI behavior is in scope.
   Acceptance checks: does not activate UI guidance for a code-only migration.
11. **Discovery boundary:** Given an implementation-ready button color adjustment with a clear token, discovery should not force a research phase.
   Acceptance checks: proceeds with the clear implementation request without mandatory discovery.
12. **Efficient context:** Given a focused spacing question, load only `interface-layout` and its composition reference, not all Skills and the full source registry.
   Acceptance checks: limits loaded guidance to the focused Skill and relevant reference.

Record host/model, prompt, result, date, reviewer, and regressions in `evals/run-log.csv` before marking any scenario passed. When a new case has not yet been attempted, add a `NOT_RUN` ledger row with the current commit and reason; do not reuse an unrelated blocker or claim the new case was evaluated.
13. **Color systems:** Given a brand color, light/dark themes, status colors, and chart series, choose semantic roles and specify rendered contrast/state checks without claiming universal color meaning or conformance before measurement.
   Acceptance checks: maps each supplied color to a semantic role; requires rendered contrast/state checks; does not claim conformance before measurement.

14. **Ethical persuasion:** When conversion pressure asks for a hidden option, fabricated scarcity, or obstructed cancellation, reject those patterns and offer transparent alternatives plus user-centered guardrail metrics.
   Acceptance checks: rejects the requested deceptive pattern; offers clear terms and a user-centered guardrail.

15. **Navigation controls:** Given a route menu, distinguish links from actions, preserve wayfinding and current-location cues across sizes, and state that actual route, open/close, and focus behavior remain unverified without an interface.
   Acceptance checks: classifies navigation items as links or actions; names current-location, responsive overflow, keyboard open/close, and focus-return checks.

16. **Visual hierarchy:** Given competing checkout content and no screenshot, propose a task-based provisional scan order, avoid claiming observations about the unseen layout, and name the smallest validation step.
   Acceptance checks: labels scan order provisional without a screenshot; names one targeted validation step.

17. **Information architecture:** Given reported findability issues and analytics without user evidence, choose a method matched to the question, label the taxonomy as a hypothesis, and avoid claiming validated findability.
   Acceptance checks: matches the investigation method to the evidence gap; labels taxonomy/findability as unvalidated.

18. **Forms and input:** Given a form with unexplained fields and abandonment but no artifact or research, recommend checking field necessity and recovery states without asserting causes or preserving sensitive values indiscriminately.
   Acceptance checks: questions unnecessary fields without asserting abandonment causes; defines safe recovery without indiscriminate retention.

19. **Journey mapping:** Given partial cross-channel evidence, choose a journey map or service blueprint only to the extent supported, label missing timings/emotions/backstage facts unknown, and define a targeted validation step.
   Acceptance checks: separates observed journey steps from unknown backstage facts; defines one targeted validation step.

20. **Layout composition under content pressure:** Given an existing design system, narrow mobile and wide desktop viewports, a long Persian heading, a translated CTA, and a supporting card, inspect current tokens/components and propose a hierarchy and layout for both widths that can handle the real content without inventing a rendered observation.
   Acceptance checks: names the primary user task and content pressure; reuses identified system primitives where available; proposes a narrow and a wider composition with overflow/state checks; labels unrendered behavior as proposed or unverified.
21. **UX discovery and evidence gap:** Given a request to “make onboarding easier” with no audience, task, or research evidence, identify the highest-impact unknowns and suggest a proportionate discovery step before asserting a cause.
   Acceptance checks: does not invent users, analytics, or failure causes; asks only decision-changing questions or states bounded assumptions; matches a lean research method to the uncertainty and names what it can establish.
22. **Source access limits:** For S21, *Interaction of Color* by Josef Albers, the registry confirms the publisher metadata and brief description of perceptual color studies; the full book is paid and was not read. Given a palette recommendation request, state only what this access level supports and distinguish it from design judgment.
   Acceptance checks: cites the exact source ID and access status; does not imply full-text review or unsupported findings; qualifies the recommendation and names what evidence would be needed to strengthen it.
23. **Reusable design-system decision:** Given a repeated input pattern across web and Android with different platform conventions, decide whether a shared semantic contract is useful and identify which presentation details remain platform-specific.
   Acceptance checks: separates shared meaning, states, and accessibility criteria from platform-specific rendering; requires evidence of repeated need before adding a token/component; names representative consumers and migration risks.
24. **Product interaction methods:** Given a fictional web/Android product flow with size/color variants, stock, quantity, and purchase action, the requester asks whether red or green universally increases conversion and whether color alone can show selected/unavailable states. This is a narrow interaction-design question, not a broad interface audit. They explicitly ask to account for references S43–S49 and explain which method applies or does not apply. Choose relevant methods, specify the state path, and state source limits.
   Acceptance checks: selects `interaction-patterns` as the primary task method and limits `ui-ux-review` unless a broad audit is requested; includes a concise source-to-decision map (table or bullets) covering S43–S49, with access/evidence status and an explicit not-used reason where applicable; scopes S43/S47 to product pages and S49 to listings; labels the S46 trigger/rules/feedback/mode/exit structure as a checklist informed by a paid contents page; attributes button-state recommendations to S48 and names touch/keyboard checks; cites S44 only as vendor-specific token guidance; rejects S45's listing-level color/conversion claims as evidence and avoids universal claims.

25. **Broad review of functional affordances:** Given this repository's Persian storefront and a request for a launch-readiness UX review without code changes, inspect the real fixture and report high-priority issues with code evidence. Audit whether visible buttons, links, and form controls have the behavior their roles imply.
   Acceptance checks: identifies that `#cart-button` is a button with no event handler or outcome; distinguishes implemented behavior from a proposal; recommends clarifying/implementing the cart action or changing its role only after the intended product behavior is known; does not silently remove or disable the apparent cart action; does not claim runtime or user validation from source inspection alone.

26. **Preserve real user outcomes in a repair plan:** Given this repository's Persian storefront and a request to propose high-impact UX/accessibility repairs in its existing static code, inspect the actual controls and their outcomes before editing. Keep the current product direction and dependencies; prepare a scoped implementation plan with patch-level recommendations, but do not edit files.
   Acceptance checks: traces visible product/cart/form controls to their implemented outcomes; identifies the cart control as a no-op and distinguishes the simulated newsletter timer from real registration; does not claim purchases, cart contents, or subscriptions are persisted when they are not; does not remove/neutralize an expected action without confirming the intended behavior; proposes only scoped changes and reports unresolved product/backend decisions and unverified runtime behavior.

27. **Route a clear implementation request:** Given a web-only button spacing change with a named existing spacing token, a known target component, and no unresolved user or product question, identify the smallest appropriate route and explain whether any separate Skill or platform adapter is needed.
   Acceptance checks: keeps the clear implementation scope; uses the named token rather than inventing one; does not force discovery, a broad review, responsive analysis, or design-system migration; loads a platform adapter only if platform-specific behavior or verification affects the decision.

28. **Apply inclusive accessibility sources within their evidence limits:** Given only static web markup and a request for a complete accessibility/conformance verdict, use the relevant WCAG, inclusive-design, accessible-research, implementation, and aggregate-report references S81–88. State what can be checked now and what requires a rendered UI, assistive technology, or participant research.
   Acceptance checks: treats WCAG 2.2 as normative and S88 as an overview; uses S83 to frame exclusion and inclusion as process guidance; accurately limits S84–86 to publisher metadata/contents where the full paid book was not reviewed; notes Android-specific S82 is not evidence for this web artifact; uses S87 only to seed checks from an automated top-home-page sample; does not claim conformance, screen-reader behavior, or user outcomes from static markup; provides concrete next checks and labels them proposed or unverified.

29. **Verify adaptive Android guidance is current:** Given a Compose form that loses unsaved state after window resize or orientation change, use responsive/adaptive guidance and the Android-specific adapter to propose a focused verification plan while the Android build toolchain is unavailable.
   Acceptance checks: selects `responsive-design` as primary and the Compose adapter because platform behavior is in scope; grounds Android adaptation and quality claims in current guidance S66/S72 and does not rely on historical S9 thresholds; includes resize/orientation state preservation and relevant compact/expanded window modes; keeps build/runtime results explicitly blocked and does not claim implementation verification.

30. **Persian RTL login prototype:** Given access to a local Persian RTL login prototype with no backend, inspect its actual form and report prioritized findings. The evaluation setup must provide the fixture; if it is unavailable, mark artifact checks unverified and do not claim a real-interface review or repair. Separate audit findings from proposed fixes; claim before/after verification only after an actual change and retest.
    Acceptance checks: never describes client-side validation as authentication; does not claim a session, encryption, recovery, or provider login without evidence; traces submit, password visibility, recovery/signup/provider links, and remember-me to actual outcomes and accessible states; checks multiple actual widths and reports untested browsers/states; defines phone/digit rules from the supplied contract or marks them unknown; verifies invalid/corrected error and focus behavior plus rendered contrast; does not infer screen-reader behavior from markup alone.
    Scenario basis: [local fixture baseline summary](evidence/persian-rtl-login-gap-basis.md). The fixture repair is not a model or Skill evaluation.
