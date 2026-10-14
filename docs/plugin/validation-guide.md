# Validation and safety checks

The packaging validator uses pinned `jsonschema` and `PyYAML` developer dependencies. Neither is part of the plugin or builder runtime; the builder itself uses only the Python standard library.

Validation checks:

- The portable manifest against the vendored Agent Plugins 1.0.0 schema, including required identity/version fields and standard `skills` extension path.
- Exactly the expected 15 Skill directories, unique folder identities, required `SKILL.md`, YAML frontmatter `name`/`description`, naming rules and description length.
- Local Markdown references resolve inside their Skill directory; absolute/home/traversal paths are rejected.
- Symlinks, hidden/cache/private files, non-UTF-8/binary content, and common credential patterns are rejected.
- Repository package files match canonical Skill bytes and generated manifest exactly.
- ZIP CRC validity, deterministic bytes, safe relative entry names, and SHA-256 provenance are covered by unit tests.

Credential scanning is a conservative pattern check, not a general secret-detection proof. CI runs the repository's existing regression suite and evaluation-ledger checks as separate gates. Extracted-package validation is structural; Codex/Claude/other-host install and runtime behavior is outside this phase.
