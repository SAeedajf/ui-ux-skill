# ChatGPT compatibility review

Reviewed for Phase 03 on 2026-10-14 against current official OpenAI documentation. These statuses describe supported/documented routes separately from actual account installation and Skill invocation.

| Surface or scope | Skills-only package support | Private install route | Phase 03 result |
|---|---|---|---|
| ChatGPT Desktop | Portable `plugin.json` + root `skills/` is a documented package shape. Local/personal marketplace sources are documented for Work mode and the ChatGPT desktop app. | Owner-managed personal marketplace or repository marketplace; no MCP is needed for Skills. | **DOCS_CONFIRMED; NOT_INSTALLED**. No ChatGPT Desktop test profile was available. |
| ChatGPT Work Web | Work can use plugins and invoke personal plugins. The official Work web quickstart demonstrates a personal plugin built with MCP. The exact import/install route for this Skills-only ZIP is not established by that quickstart. | Try Plugin Creator with the archive only if the account offers the personal flow; stop if it cannot import the ZIP. | **PARTIAL / UNVERIFIED FOR THIS PACKAGE**. No account or chat test. |
| Personal plugin directory | Personal plugins are a documented scope; Plugin Creator can build plugins and local marketplaces. | ChatGPT account's personal plugin flow, subject to account/surface availability. | **DOCS_CONFIRMED; ACCOUNT_UNKNOWN**. No personal plugin created or installed. |
| Workspace plugins | Skills-only package format is supported in principle. Workspace ZIP upload and controls are role/permission-gated. | Eligible workspace upload or creator flow. Keep private; sharing/publishing are separate. | **DOCS_CONFIRMED; ROLE_UNKNOWN; NOT_INSTALLED**. No workspace changes. |
| ChatGPT Mobile | Plugin directory exists on mobile, but this does not prove this private/local ZIP route or all Skill features work there. | No tested private install path for this package. | **UNVERIFIED**. No mobile test. |
| Universal Plugin Directory | Public plugin publication is a separate submission/review/release process and the directory is shared between ChatGPT and Codex. | Public submission only. | **OUT OF SCOPE**. No submission or publication. |
| Local/repository marketplace | OpenAI documents local/repo marketplace sources for Work mode and ChatGPT desktop Codex. | Personal or repo source, with path relative to marketplace root. | **DOCS_CONFIRMED; THIS PACKAGE'S CHATGPT INSTALL NOT TESTED**. |

## Manifest decision

`plugins/ui-ux-pro/plugin.json` is the portable Agent Plugins manifest. The extracted archive passed the repository's vendored schema validator and exact canonical-source check. The ZIP has `plugin.json`, `LICENSE`, and `skills/` at its root, with exactly 15 Skills and 18 reference files.

OpenAI's package guide documents root `plugin.json` plus `skills/` for portable packages and says portable packages discover Skills from the fixed root `skills/` directory. It describes `.codex-plugin/plugin.json` as a supported compatibility fallback/scaffold, not a required overlay. There is no current documentation or test evidence that ChatGPT requires this package to add that fallback; no manifest was changed.

## Capability boundaries

- Skills-only means the plugin supplies instructions and references; it does not add remote tools, fetch data, or bypass model/account usage.
- A format/schema pass does not prove a ChatGPT account can install the package.
- A visible plugin card does not prove installation or Skill activation.
- Installing the plugin does not prove any of the 15 Skills ran. Use a fresh conversation and capture the strongest trace the surface exposes.
- A public GitHub Actions artifact is not a Universal Directory listing. This repository is public, so the artifact link is downloadable by repository visitors until GitHub expires it.

## Official references

- [OpenAI: Package your plugin](https://developers.openai.com/plugins/build/plugins)
- [OpenAI: Plugin quickstart](https://developers.openai.com/plugins/quickstart)
- [OpenAI Help: Plugins in ChatGPT](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt)
