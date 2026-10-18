# ui-ux-skill

A public, evidence-led collection of task-oriented Agent Skills for designing and reviewing web and Android interfaces. The library is organized around work people need to do—not around individual books or websites.

## What is included

Fifteen task-oriented Skills cover 14 UI/UX topic areas plus cross-cutting review: discovery, hierarchy, color, ethical persuasion, layout, interactions, navigation, typography/RTL, accessibility, design systems, information architecture, forms, journeys, and responsive behavior. A source registry records 124 references with two-pass review notes, source class, evidence scope, access limitations, and review date. Platform notes explain how to install the same canonical Skills for Codex, Claude Code, VS Code/Copilot, and compatible Agent Skills hosts.

Each Skill has a narrow trigger, cross-skill handoffs, source notes, and a positive/negative activation prompt. The guidance distinguishes standards from research, platform guidance, practitioner methods, and visual inspiration. It does not treat a visual example as usability evidence or claim that one color, layout, or conversion tactic works for every audience.

## Quick start

- Codex: the repository's `.agents/skills/` folder is directly discoverable when the repository is opened as a project. For user-level installation, run `python3 scripts/install-skills.py --target ~/.codex/skills --all`.
- Claude Code: run `python3 scripts/install-skills.py --target .claude/skills`.
- VS Code/Copilot: run `python3 scripts/install-skills.py --target .github/skills`.
- Other hosts: see [installation guidance](docs/installation.md) and check the host's current Agent Skills support and discovery path.

Use `python3 scripts/install-skills.py --help` to see selection and overwrite options. Each skill can also be copied manually as a folder.

## Contents

- [Skill index](skills/index.md)
- [AI agent usage guide](docs/agent-usage-guide.md)
- [Installation](docs/installation.md)
- [Source registry](docs/source-registry.csv)
- [Domain coverage](docs/domain-coverage.csv)
- [Platform adapters](adapters/)
- [Examples](examples/)
- [Persian storefront fixture and verification record](docs/fixture-ux-validation.md)
- [Synthetic layout and design-system decision record](examples/synthetic/layout-and-system.md)
- [Evaluation scenarios and result status](evals/)
- [Codex evaluation workflow](docs/evaluation.md)
- [Operational readiness report](docs/operational-readiness.md)
- [Contribution and evidence policy](CONTRIBUTING.md)

## Rights and attribution

Original repository-authored material is licensed under [CC BY 4.0](LICENSE). The license does not apply to third-party websites, books, marks, screenshots, or other linked works. See the source registry for attribution links and access notes. No third-party source prose or visual assets are bundled.

## Status

Operational status is documented in [the readiness report](docs/operational-readiness.md). The repository contains 15 model-neutral Skills and an [AI-agent usage guide](docs/agent-usage-guide.md) for routing, selective reference loading, handoffs, and evidence-based reporting. On Codex CLI 0.144.5 using the host default, the original 30-case positive/negative activation suite was rerun on commit `5a674e9`; all positives read their target Skill and all negatives leave their target unselected. Results remain `NEEDS_REVIEW` until a separate human reviewer attests to the whole traces. Two OTP-specific automatic-selection prompts are now defined but `NOT_RUN`; no current automatic activation is inferred. A fresh metadata probe found all 15 Skills in Codex prompt input; this establishes discovery only. Twenty-nine quality scenarios pass criterion-level review; Persian RTL login review (`quality-30`) and strict OTP input (`quality-31`) remain `NOT_RUN`. The deterministic OTP fixture is regression coverage, not model evaluation. Android runtime remains blocked by the missing toolchain. No Claude test was run in this mission. The earlier `gpt-6-luna` rejection is one historical environment result, not a repository model restriction; the runner uses the user/host choice by default and accepts an optional model override. Source review is current to 2026-10-14; six partially verified and paywalled references remain labeled.
