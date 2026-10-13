# ui-ux-skill

A public, evidence-led collection of task-oriented Agent Skills for designing and reviewing web and Android interfaces. The library is organized around work people need to do—not around individual books or websites.

## What is included

Eight Skills cover discovery, interface composition, interaction, design systems, responsive behavior, accessibility, Persian/RTL localization, and UI/UX review. A source registry records 124 references with two-pass review notes, source class, evidence scope, access limitations, and review date. Platform notes explain how to install the same canonical Skills for Codex, Claude Code, VS Code/Copilot, and compatible Agent Skills hosts.

The guidance distinguishes standards from research, platform guidance, practitioner methods, and visual inspiration. It does not treat a visual example as usability evidence or claim that one color, layout, or conversion tactic works for every audience.

## Quick start

- Codex: the repository's `.agents/skills/` folder is directly discoverable when the repository is opened as a project.
- Claude Code: run `python3 scripts/install-skills.py --target .claude/skills`.
- VS Code/Copilot: run `python3 scripts/install-skills.py --target .github/skills`.
- Other hosts: see [installation guidance](docs/installation.md) and check the host's current Agent Skills support and discovery path.

Use `python3 scripts/install-skills.py --help` to see selection and overwrite options. Each skill can also be copied manually as a folder.

## Contents

- [Skill index](skills/index.md)
- [Installation](docs/installation.md)
- [Source registry](docs/source-registry.csv)
- [Domain coverage](docs/domain-coverage.csv)
- [Platform adapters](adapters/)
- [Examples](examples/)
- [Evaluation scenarios](evals/)
- [Contribution and evidence policy](CONTRIBUTING.md)

## Rights and attribution

Original repository-authored material is licensed under [CC BY 4.0](LICENSE). The license does not apply to third-party websites, books, marks, screenshots, or other linked works. See the source registry for attribution links and access notes. No third-party source prose or visual assets are bundled.

## Status

This is an initial release candidate. The evaluation log records one partial Codex CLI smoke test and one Claude Code discovery check that could not reach model output because of local OAuth authentication. The 16 authored activation cases and 12 quality scenarios have not been run as a suite. Source review is current to 2026-10-13; partially verified and paywalled references are explicitly labeled.
