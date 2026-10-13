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
12. **Efficient context:** Given a focused spacing question, load only `interface-layout` and its composition reference, not all eight Skills and the full source registry.

Record host/model, prompt, result, date, reviewer, and regressions in `evals/run-log.csv` before marking any scenario passed.
