# Codex

Use `.agents/skills/` as the canonical project-level location. Open the repository as a project and check that the intended Skills appear in the active host. For user-level installation, copy the Skills to `~/.codex/skills` with `python3 scripts/install-skills.py --target ~/.codex/skills --all`. The `SKILL.md` files use the common `name` and `description` frontmatter fields. For API/sandbox use, make the skill directory available through the execution environment's current skill/capability configuration. Installation and discovery do not prove model auto-activation; test positive and adjacent negative prompts in the host and record the model and version.

Current reference: [OpenAI Skills guide](https://developers.openai.com/api/docs/guides/tools-skills).
