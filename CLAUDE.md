# UI/UX Skill guidance for Claude Code

- For UI/UX tasks, consult [the AI agent usage guide](docs/agent-usage-guide.md) and [Skill index](skills/index.md).
- Select the smallest relevant Skill set. Start a broad interface audit with `ui-ux-review`; do not load all 15 Skills by default.
- Read the selected Skill's `SKILL.md` and only the references relevant to the task.
- Inspect the actual interface or repository when available. Separate observed, user-reported, inferred, proposed, and verified statements.
- Cite precise source IDs from `docs/source-registry.csv` for library-backed claims; state access limits.
- Follow the user's requested scope. Do not implement changes when the user asked only for a review.
- Report checks actually run and any states that remain unverified. Manual Skill invocation does not prove automatic activation.
