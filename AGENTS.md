# Shared UI/UX guidance

Use the relevant Skill in `.agents/skills/` for the task. Read its `SKILL.md` first and load only its linked references that fit the current question.

For routing, host setup, prompt templates, and evidence labels, follow [docs/agent-usage-guide.md](docs/agent-usage-guide.md). Choose one primary Skill and add supporting Skills only for actual handoffs; do not load the full collection by default.

- Begin with the user's goal, audience, context, constraints, platform, existing implementation, and success criteria. Inspect the actual repository or interface before prescribing a redesign.
- Separate requirements and standards from research findings, platform conventions, practitioner guidance, hypotheses, and aesthetic choices. For externally grounded claims, cite the exact source ID from `docs/source-registry.csv` at the decision point; state if only a summary, listing, or paywalled description was reviewed, and do not stretch the claim beyond that evidence.
- Prefer the smallest useful design change. Preserve working patterns and existing design tokens unless evidence or a stated goal justifies a change. Avoid adding a framework or dependency without need.
- Do not present conversion, color psychology, or behavioral claims as universal facts. Keep persuasion honest, consent-respecting, and easy to reverse.
- Check only the states and conditions relevant to the task, such as breakpoints, orientation, keyboard/focus, touch, contrast, zoom, and assistive-technology behavior. For each important recommendation or finding, record the artifact/state inspected, acceptance criterion, observed outcome, and evidence class (`observed`, `user-reported`, `inferred`, or `proposed`). State what was actually tested; never claim unverified outcomes.
- Treat language direction as locale-specific. For Persian/Arabic, inspect bidirectional mixed text, numerals, dates, currency, phone/OTP fields, typography, icon direction, and text expansion. Do not apply RTL to an LTR locale.
- Keep third-party text and assets out of generated deliverables unless the user provides rights or the material is clearly licensed for that use. Link and attribute sources; do not imply the repository's CC BY license covers them.
