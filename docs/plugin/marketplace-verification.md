# Marketplace verification

## Catalog

The repository marketplace is `.agents/plugins/marketplace.json` and is named `ui-ux-pro-marketplace`. Its sole plugin entry has ID `ui-ux-pro`, local source `./plugins/ui-ux-pro`, category `Creativity`, installation policy `AVAILABLE`, and authentication policy `ON_INSTALL`. The path is interpreted from the repository/marketplace root. The plugin requires no MCP server or external authentication service.

The catalog uses the current OpenAI plugin marketplace shape: `name`, `interface.displayName`, and `plugins[]` with `name`, `source`, `policy`, and `category`. The plugin manifest uses the conventional root `skills/` directory; it does not declare `extensions.skills`, which is not needed for this package.

## Validator

Run from the repository root:

```sh
.venv/bin/python scripts/validate_marketplace.py
.venv/bin/python -m unittest discover -s tests -p 'test_marketplace.py' -v
```

The validator checks JSON shape, stable and unique IDs, supported category/policy values, local-only source paths, path escape and personal-path rejection, manifest and SemVer identity, all 15 skill directories, and package/reference validity. Its tests cover malformed JSON, duplicate IDs, traversal and absolute paths, invalid policy, missing skills, external source objects, nested Markdown references, and links that escape a skill.

## CLI evidence

The following commands passed in the clean disposable local-marketplace environment with exit code 0. Exact paths and full outputs are retained in the Phase 02 execution logs while that environment exists; the report summarizes the outputs:

1. `codex plugin marketplace add "$PWD" --json` — returned `ui-ux-pro-marketplace` rooted at the Phase 02 checkout.
2. `codex plugin marketplace list --json` — listed that marketplace root.
3. `codex plugin list --available --json --marketplace ui-ux-pro-marketplace` — returned `ui-ux-pro@ui-ux-pro-marketplace`, with `AVAILABLE` and `ON_INSTALL` policies.
4. `codex plugin add ui-ux-pro@ui-ux-pro-marketplace --json` — installed into the isolated `CODEX_HOME/plugins/cache/ui-ux-pro-marketplace/ui-ux-pro/local` cache.
5. `codex plugin list --json` — reported `installed=true`, `enabled=true`.

GitHub installation results, including the exact commit ref and installed-file hash comparison, are recorded here after that test is run.

## Official references

- [OpenAI: Build plugins and marketplaces](https://developers.openai.com/plugins/build/plugins)
- [Agent Plugins: Plugin format and schema](https://agent-plugins.org/)
