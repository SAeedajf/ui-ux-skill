# Installation

The repository keeps one canonical copy of each Skill under `.agents/skills/`. The installer copies the selected folders to a host's supported project-level skill directory. Skill discovery and automatic invocation depend on each host and its settings; installation alone does not guarantee activation.

## Codex

Open the repository as a Codex project. Codex discovers workspace skills under `.agents/skills/`. The repo's canonical location can be used directly; no copy is needed. For user-level installation, choose the appropriate personal skill directory for your Codex setup and verify against current Codex documentation.

## Claude Code

From the repository root, run:

```sh
python3 scripts/install-skills.py --target .claude/skills
```

Claude Code project skills use `.claude/skills/<skill-name>/SKILL.md`. Start a new session or use the host's skill discovery/reload behavior, then inspect available skills. Invocation behavior depends on Claude Code's current version and configuration.

## VS Code / GitHub Copilot

Run:

```sh
python3 scripts/install-skills.py --target .github/skills
```

VS Code also supports `.agents/skills/` and `.claude/skills/` in current documentation. Use the location that matches your workspace and agent setup.

## Other Agent Skills hosts

If your host implements the open Agent Skills format, install each folder where that host discovers `SKILL.md`. Use `--target PATH` to copy to that directory or copy a selected folder manually. Consult the host's current documentation for metadata extensions, personal vs project locations, and invocation behavior.

## Commands

```sh
python3 scripts/install-skills.py --list
python3 scripts/install-skills.py --target .claude/skills --skill ux-discovery --skill ui-ux-review
python3 scripts/install-skills.py --target .github/skills --all
```

The installer refuses to overwrite existing skill folders by default. Add `--overwrite` only when you intend to replace those folders. It does not delete files outside the selected skill destination.

## Platform references

- [OpenAI Skills guide](https://developers.openai.com/api/docs/guides/tools-skills)
- [Claude Code Skills](https://code.claude.com/docs/en/skills)
- [VS Code Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills)

These hosts share the `SKILL.md` pattern, but activation, supported metadata, user-level install paths, and tool availability may differ.
