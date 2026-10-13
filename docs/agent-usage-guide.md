# AI agent usage guide

This guide helps coding agents use the repository's 15 UI/UX Skills without loading every reference or treating a recommendation as a verified result. The Skills are modular workflows. A host may discover them, but the model still decides whether to use them unless the user explicitly selects one.

Treat Skill files as guidance to review, not as permission to ignore the user's request, repository instructions, or host safeguards. Inspect included scripts and external links before relying on them.

## 1. Make the Skills available to your host

Use the [installation guide](installation.md) for the host-specific discovery path. The short version:

| Host | Project-level setup |
|---|---|
| Codex | Open the repository as the project; use its canonical `.agents/skills/` directory. |
| Claude Code | Run `python3 scripts/install-skills.py --target .claude/skills`; start a new session or refresh skills, then inspect `/skills`. |
| VS Code / GitHub Copilot | Run `python3 scripts/install-skills.py --target .github/skills` and use `/skills` to inspect the available customizations. |
| Another compatible host | Install the skill folders where that host discovers `SKILL.md`; verify the path and metadata in that host. |

Use `python3 scripts/install-skills.py --list` to see the names and `--help` to inspect install options. Do not copy the same collection into multiple discovery directories unless the host requires it; duplicate copies can make version drift harder to notice.

Discovery means the host can see Skill metadata. It does not show that the model invoked a Skill. A manual invocation confirms the workflow can be requested; it does not count as automatic activation. See [Codex evaluation guidance](evaluation.md) for evidence requirements and the current [readiness report](operational-readiness.md) for platform-specific results.

## 2. Select the smallest useful set

Start with the user's task, not the Skill list. Read the [Skill index](../skills/index.md), choose one primary Skill, then add a supporting Skill only when a real handoff or separate concern requires it. Do not load all 15 by default.

| Task signal | Start with | Add only when the work also needs |
|---|---|---|
| A broad audit of an existing interface | `ui-ux-review` | Focused findings such as accessibility, RTL, forms, color, or responsive behavior |
| Unclear user goal or missing product evidence | `ux-discovery` | `information-architecture` for findability/taxonomy; `journey-mapping` for an end-to-end or cross-channel experience |
| Page arrangement or spacing | `interface-layout` | `visual-hierarchy` for task priority; `responsive-design` when viewport adaptation is in scope |
| Color roles or theme behavior | `color-systems` | `accessibility-inclusive-design` for relevant contrast and state checks; `design-systems` for shared tokens |
| A control's states, feedback, or recovery | `interaction-patterns` | `forms-input` for field/validation behavior; `navigation-controls` for wayfinding and menus |
| Persian, RTL, or mixed-direction content | `persian-rtl-localization` | `forms-input` for localized input; accessibility or responsive review when those checks are requested |
| Reusable components, tokens, or theming | `design-systems` | A focused component or platform Skill if the implementation crosses that boundary |
| Influence on purchase, sign-up, engagement, or another choice | `ethical-persuasion` | The relevant form, interaction, or journey Skill for the actual user flow |
| Adapting a web or Android layout | `responsive-design` | `adapters/web.md`, `adapters/android.md`, or `adapters/compose.md` for the target platform |

For a simple implementation request with a clear goal and existing token, act on that scope without forcing discovery. For an ambiguous product question, clarify the uncertainty first. A multi-issue task may need several Skills, but include only those needed to decide or verify the change.

## 3. Apply a Skill to the real task

1. Confirm the requested outcome, users, platform, locale, constraints, and whether the user asked for review, recommendations, or code changes.
2. Inspect the supplied interface, repository, screenshots, or research artifacts. If the artifact is unavailable, say what cannot be observed.
3. Read the selected `SKILL.md` and only the linked references that fit this task. Use the index's handoffs instead of loading unrelated Skills.
4. Separate standards, platform guidance, research, user-reported evidence, inference, and design judgment. Cite the precise source ID from `docs/source-registry.csv` when making a claim based on this library; state access limits.
5. Make only the changes the user requested. When implementation is in scope, follow the project's conventions and run relevant existing checks. Do not turn a review request into an unrequested redesign.
6. Report what was observed, what changed, which checks ran, and what remains unknown. Do not claim usability, accessibility conformance, responsive behavior, or Skill activation without matching evidence.

## 4. Reusable request template

Copy and fill the parts that matter; remove fields that do not apply.

```text
Review / improve [screen, flow, or component] for [user task].
Users/context: [who and what they need]
Platform and supported sizes: [web / Android / Compose; known viewports]
Locale and direction: [locale(s), RTL/LTR, mixed content]
Goal and constraints: [success criteria, existing system, must-keep behavior]
Available evidence: [repository path, screenshot, prototype, research, or none]
Scope: [review only / recommend / implement the agreed fixes]

Use the smallest relevant UI/UX Skill set. Inspect the actual artifact when available.
Separate observations, source-backed claims, assumptions, and proposals. If you change code,
run the relevant existing checks and report their results. List unverified states explicitly.
```

For a broad audit, name `ui-ux-review` as the starting point and ask the agent to add focused Skills only for findings that need them. For a narrow task, directly request the relevant Skill (for example, `forms-input` for a form recovery issue). Direct selection is useful for consistency; do not count it as evidence that automatic activation works.

## 5. Host-specific invocation

- **Codex:** open the repository as a project so workspace Skills can be discovered. For direct use, say “Use `forms-input` to review validation and recovery” or select the Skill in a supported Skill UI. User-level installation is available with `python3 scripts/install-skills.py --target ~/.codex/skills --all`.
- **Claude Code:** install to `.claude/skills/`, then inspect `/skills`. Claude can choose a relevant Skill automatically or you can invoke it as a slash command, such as `/ui-ux-review`.
- **VS Code / GitHub Copilot:** install to `.github/skills/`; use `/skills` to inspect available customizations. Invocation UI and behavior can vary by product version and agent mode. Confirm the installed Skill is listed before relying on it.
- **Other hosts:** follow that host's current documentation. Agent Skills format compatibility does not guarantee identical discovery, context loading, automatic selection, or tool access.

## 6. Evidence labels for the final report

Use these labels consistently:

- **Observed:** inspected directly in code, rendered UI, or a captured runtime state; name which one.
- **User-reported:** supplied by the user but not independently checked.
- **Inferred:** a reasoned explanation from available evidence; state the uncertainty.
- **Proposed:** a recommendation that has not been implemented or tested.
- **Verified:** a named acceptance check was executed and passed; state the tool, target, or test conditions.
- **Unverified / blocked:** the relevant interface, device, account, model, or evidence was unavailable. A blocker is not a pass.

If you are evaluating Skill activation, keep the exact prompt, host/version, model, result, and trace. A plausible response or a manually selected Skill is not proof of automatic activation. Do not mark an evaluation `PASS` until the trace contains evidence that a reviewer can verify; see [evaluation procedure](evaluation.md).

## Platform references

- [Codex skills and project instructions](https://developers.openai.com/api/docs/guides/tools-skills)
- [Codex `AGENTS.md` instructions](https://developers.openai.com/api/docs/guides/latest-model)
- [Claude Code Skills](https://code.claude.com/docs/en/skills)
- [VS Code Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills)
