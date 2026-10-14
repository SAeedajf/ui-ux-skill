# Plugin compatibility matrix

**Reviewed:** 2026-10-14
**Package under consideration:** `ui-ux-pro`, skills-only, portable Agent Plugins v1.0.0

Statuses describe evidence, not expected capability:

- **VERIFIED (surface/docs or CLI):** current official documentation or this installed executable confirms the named surface/command exists. It does not prove this package installs.
- **PARTIAL:** a relevant route is documented, but package installation or invocation was not tested, or a local blocker remains.
- **UNVERIFIED:** current evidence does not establish the claim.
- **OUT OF SCOPE:** deliberately not being tested in this phase.

| Host / route | Status | What is established | What is not established / next evidence |
| --- | --- | --- | --- |
| Codex CLI command availability | **VERIFIED** | Installed `codex-cli 0.144.5`; `codex plugin --help` lists plugin management; `codex plugin marketplace --help` lists `add/list/upgrade/remove`; `codex plugin add --help` supports `PLUGIN@MARKETPLACE` | No package add/install/invocation was attempted in Phase 00 |
| Codex CLI current marketplace runtime | **BLOCKED** | Read-only `codex plugin marketplace list --json` and `codex plugin list --json` were attempted | Both fail before command execution because `~/.codex/config.toml:12` has `agents = true`, but this binary expects an `AgentRoleToml` object. No persistent config change was made. Retest after owner-approved config repair or in an isolated disposable CLI home during a later phase |
| Codex project Skills from repo | **VERIFIED (existing baseline only)** | The repository has 15 canonical Skills under `.agents/skills/`; prior repo/Skill validators are part of existing workflow | Does not verify plugin loading or package references after install |
| Codex desktop local/repo marketplace | **PARTIAL** | OpenAI docs describe repo/personal marketplace entries and desktop installation flow | No package was added to a marketplace or loaded in the desktop app |
| ChatGPT desktop personal/repo marketplace | **PARTIAL** | OpenAI docs describe local marketplace discovery and installation through the desktop Plugins Directory | No desktop installation or activation evidence for this package |
| ChatGPT Work web personal plugin | **PARTIAL** | OpenAI's personal-plugin quickstart demonstrates creation and invocation in Work on the web for an MCP-backed plugin; the public directory is shared by ChatGPT and Codex | That quickstart is not evidence that this skills-only package or a repo marketplace works on web. No personal plugin was created; local repo-marketplace support in Work web is not established |
| ChatGPT workspace plugin | **PARTIAL** | Workspace publishing is documented for workspace admins and remains within the workspace | Requires account role/admin state and a separate publish action; neither was checked or performed |
| ChatGPT universal public directory | **PARTIAL** | Official flow is ZIP upload → automated checks → review → owner-controlled publish after approval | No identity verification, upload, review, approval, or publication was requested/performed |
| ChatGPT mobile | **UNVERIFIED** | No mobile plugin install or Skill invocation evidence was found in the reviewed material | Must not claim mobile support without current explicit documentation and a mobile-client test |
| Claude Code | **OUT OF SCOPE** | User explicitly deferred Claude testing | No test planned in this phase |
| Other portable Agent Plugins clients | **UNVERIFIED per client** | The format is vendor-neutral and specifies package layout | Compatibility requires a named client/version and package-level test; the format alone is not evidence |

## Installation versus discovery versus invocation

Track these as separate gates in later phases:

1. **Package validation:** manifest and package structure conform.
2. **Marketplace discovery:** a host lists the package from its configured source.
3. **Installation:** package files are materialized in the host's expected location.
4. **Skill discovery:** all 15 skill IDs appear to the agent in a fresh session.
5. **Invocation:** relevant positive prompts select the intended Skill; negative prompts do not spuriously load unrelated Skills.
6. **Quality:** the task output follows the relevant Skill and the existing evidence/claim limits.

A PASS at one gate does not imply a PASS at later gates. Report exact host version, package/source commit, install route, and evidence for every host-specific result.

## Current Codex command evidence

Observed from the installed binary (read-only help):

```text
codex-cli 0.144.5
codex plugin: add, list, marketplace, remove
codex plugin marketplace: add, list, upgrade, remove
codex plugin add: PLUGIN@MARKETPLACE or --marketplace
```

Runtime marketplace discovery is blocked by the existing user configuration parse error described above. This is an environment blocker, not proof that the plugin package is incompatible. Do not repair or overwrite the user's config as part of Phase 00.

## Official documentation reviewed

- [OpenAI package format and local marketplaces](https://developers.openai.com/plugins/build/plugins)
- [OpenAI plugin architecture](https://developers.openai.com/plugins/concepts/plugins)
- [OpenAI Skills](https://developers.openai.com/plugins/concepts/skills)
- [OpenAI public submission and publication flow](https://developers.openai.com/plugins/deploy/submission)
- [OpenAI ZIP validation and submission errors](https://developers.openai.com/plugins/deploy/submission-errors)
- [OpenAI personal Work quickstart](https://developers.openai.com/plugins/quickstart)
- [Agent Plugins specification v1.0.0](https://agent-plugins.org/specification)
