# Shared UI/UX guidance

Use the relevant Skill in `.agents/skills/` for the task. Read its `SKILL.md` first and load only its linked references that fit the current question.

- Begin with the user's goal, audience, context, constraints, platform, existing implementation, and success criteria. Inspect the actual repository or interface before prescribing a redesign.
- Separate requirements and standards from research findings, platform conventions, practitioner guidance, hypotheses, and aesthetic choices. Cite source IDs from `docs/source-registry.csv` when drawing on this library; explain context and limits.
- Prefer the smallest useful design change. Preserve working patterns and existing design tokens unless evidence or a stated goal justifies a change. Avoid adding a framework or dependency without need.
- Do not present conversion, color psychology, or behavioral claims as universal facts. Keep persuasion honest, consent-respecting, and easy to reverse.
- Check the relevant states, breakpoints, orientation, keyboard/focus, touch, contrast, zoom, and assistive-technology behavior. State what was actually inspected or tested; never claim unverified outcomes.
- Treat language direction as locale-specific. For Persian/Arabic, inspect bidirectional mixed text, numerals, dates, currency, phone/OTP fields, typography, icon direction, and text expansion. Do not apply RTL to an LTR locale.
- Keep third-party text and assets out of generated deliverables unless the user provides rights or the material is clearly licensed for that use. Link and attribute sources; do not imply the repository's CC BY license covers them.
