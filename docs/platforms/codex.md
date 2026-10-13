# Codex

Use `.agents/skills/` as the canonical project-level location. Open the repository as a project and check that the intended Skills appear in the active host. For user-level installation, copy the Skills to `~/.codex/skills` with `python3 scripts/install-skills.py --target ~/.codex/skills --all`. The `SKILL.md` files use the common `name` and `description` frontmatter fields. For API/sandbox use, make the skill directory available through the execution environment's current skill/capability configuration. Installation and discovery do not prove model auto-activation; test positive and adjacent negative prompts in the host and record the model and version. For prompt design, Skill selection, and reporting boundaries, use the [AI agent usage guide](../agent-usage-guide.md).

Current reference: [OpenAI Skills guide](https://developers.openai.com/api/docs/guides/tools-skills).

## Evaluation status and local checks

Run `python3 scripts/validate_repo.py` to validate repository structure and result ledgers, `python3 -m unittest discover -s tests -v` for deterministic regressions, and `python3 scripts/eval_harness.py report` for current result counts. Prompt-input discovery is not automatic activation evidence. Only mark activation PASS when the Codex session trace proves automatic invocation for the positive case and no unintended invocation for the negative case. Current environment limitations are in [operational readiness](../operational-readiness.md).
