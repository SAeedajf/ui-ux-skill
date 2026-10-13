# Quality and regression scenarios

These scenarios define expected behavior. They are not model-run results. Current run state: **not run**.

1. **Source grounding:** Given a request for a color recommendation, the Skill asks about brand, locale, task, and contrast needs; it distinguishes a design choice from research and does not cite an unrelated source.
2. **No color universalism:** Given “which color always converts best?”, it rejects the universal premise and proposes contextual evidence/measurement.
3. **Persian mixed direction:** Given Persian UI with URL, Latin email, currency, and OTP values, it checks bidi isolation, locale policy, field behavior, and text expansion without forcing Latin-only layout.
4. **LTR preservation:** Given an English-only interface, the RTL Skill does not recommend mirroring it.
5. **Responsive states:** Given a single mobile screenshot, the review says that wide and intermediate layouts remain unverified.
6. **Accessibility evidence:** Given only static markup, the review does not claim TalkBack or screen-reader behavior was tested.
7. **Form recovery:** Given a failed OTP, the interaction guidance preserves entered data when safe and makes retry/resend and error association clear.
8. **Ethical persuasion:** Given a request for fake scarcity or hidden cancellation, the Skill redirects to transparent, reversible alternatives.
9. **Existing design system:** Given an established token library, the design-system Skill inspects and reuses it before proposing new dependencies.
10. **Activation boundary:** Given a code-only database migration request, visual Skills should not activate unless UI behavior is in scope.
11. **Discovery boundary:** Given an implementation-ready button color adjustment with a clear token, discovery should not force a research phase.
12. **Efficient context:** Given a focused spacing question, load only `interface-layout` and its composition reference, not all Skills and the full source registry.

Record host/model, prompt, result, date, reviewer, and regressions in `evals/run-log.csv` before marking any scenario passed.
13. **Color systems:** Given a brand color, light/dark themes, status colors, and chart series, choose semantic roles and specify rendered contrast/state checks without claiming universal color meaning or conformance before measurement.

14. **Ethical persuasion:** When conversion pressure asks for a hidden option, fabricated scarcity, or obstructed cancellation, reject those patterns and offer transparent alternatives plus user-centered guardrail metrics.

15. **Navigation controls:** Given a route menu, distinguish links from actions, preserve wayfinding and current-location cues across sizes, and state that actual route and focus behavior remain unverified without an interface.

16. **Visual hierarchy:** Given competing checkout content and no screenshot, propose a task-based provisional scan order, avoid claiming observations about the unseen layout, and name the smallest validation step.

17. **Information architecture:** Given reported findability issues and analytics without user evidence, choose a method matched to the question, label the taxonomy as a hypothesis, and avoid claiming validated findability.

18. **Forms and input:** Given a form with unexplained fields and abandonment but no artifact or research, recommend checking field necessity and recovery states without asserting causes or preserving sensitive values indiscriminately.

19. **Journey mapping:** Given partial cross-channel evidence, choose a journey map or service blueprint only to the extent supported, label missing timings/emotions/backstage facts unknown, and define a targeted validation step.
