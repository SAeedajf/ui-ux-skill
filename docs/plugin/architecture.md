# UI/UX Pro plugin architecture

**Phase:** 00 — architecture audit
**Reviewed:** 2026-10-14
**Repository:** [SAeedajf/ui-ux-skill](https://github.com/SAeedajf/ui-ux-skill)

## Decision

Adopt a **portable, skills-only Agent Plugin** as the package format. The package needs no MCP server, hosted service, API key, or runtime dependency: these Skills provide instructions and local references, and do not need live data or controlled external actions. Keep MCP as a future, separately reviewed extension only if a concrete live-data or action requirement appears.

Keep editable Skills in the existing canonical `.agents/skills/<skill-id>/` tree. A deterministic builder should assemble the 15 canonical folders and their required references into `plugins/ui-ux-pro/`, the installable package. Treat that folder as generated output: never edit a bundled Skill there by hand. CI should rebuild into a temporary directory and fail on any difference. This gives Git-based marketplace clients a complete package while retaining one authored copy per Skill.

Use the portable root `plugin.json` as the package manifest. Do not add `.codex-plugin/plugin.json` by default: current OpenAI packaging documentation accepts the portable manifest and describes the Codex manifest as a compatibility fallback. Add a Codex overlay only if a later target-client test demonstrates a specific required field or behavior; generate it from the same metadata input, and test conflict/precedence behavior. Keep marketplace catalog metadata separate from package identity.

## Audited repository baseline

| Item | Evidence at Phase 00 start |
| --- | --- |
| Default branch | `main`, confirmed from GitHub and `origin/HEAD` |
| Base commit | `9f7cd28619a5e5e45816f70ad176ec7f978456e3` (2026-10-14) |
| Repository visibility | Public |
| Repository license | CC BY 4.0, confirmed from GitHub metadata and `LICENSE` |
| Current work branch | `codex/ui-ux-plugin-phase-00`, created from the base commit |
| Canonical Skills | 15 `SKILL.md` files under `.agents/skills/` |
| Skill reference files | 15 files under the Skill `references/` directories |
| Reference registry | 124 rows: 118 reviewed, 6 partially verified |
| Activation suite | 30 cases; existing results include `NEEDS_REVIEW` and `BLOCKED`, not 30 PASS results |
| CI | `.github/workflows/validate.yml` runs `validate_repo.py`, deterministic unit tests, and the eval report |
| Runtime dependencies | Current validation/build utilities are Python standard-library based; no plugin runtime dependency is needed |
| Existing plugin package/catalog | No portable plugin manifest or repo marketplace catalog exists at the audited base |
| Local workspace state | 71 pre-existing changed/untracked paths were present before Phase 00 edits; they are not included in the Phase 00 commit |

The repository contains contributor/install guidance and an existing cross-host Skill installer. This plan preserves those surfaces and adds a generated plugin package rather than moving the canonical Skill tree.

## Package and repository layout

```text
config/ui-ux-pro.json                 # authored package metadata; single version source
.agents/skills/<skill-id>/            # canonical, editable Skills and references
.agents/plugins/marketplace.json      # optional local/repo catalog; distribution metadata only
plugins/ui-ux-pro/plugin.json         # generated portable manifest
plugins/ui-ux-pro/skills/<skill-id>/  # generated copies of all 15 canonical Skills
dist/ui-ux-pro-<version>.zip          # generated release candidate, not hand-edited
dist/ui-ux-pro-<version>.manifest.json # source commit, version, file list, hashes
scripts/build-plugin.py               # deterministic package builder
scripts/validate-plugin.py            # package/schema/path/reference/license checks
docs/plugin/                           # architecture, operation, and phase reports
```

The built package is checked into the repository so a Git-backed local marketplace can resolve all package-relative references from one commit. CI must prove it is a reproducible copy of `.agents/skills/` before accepting changes. `dist/` is generated for release candidates and should be ignored in normal source commits; CI/release artifacts hold the ZIP and hash manifest. A release manifest outside the plugin root records the exact source commit because the portable manifest has a closed schema and must not receive custom top-level fields.

`marketplace.json` is a catalog, not part of the portable plugin manifest and not the public OpenAI directory. Its plugin entry may point to `./plugins/ui-ux-pro`. The builder owns plugin identity/version; the marketplace owns the catalog name, local source path, category, and install policy. Do not maintain a second hand-authored copy of publisher/version/name in a Codex compatibility manifest.

## Format comparison

| Choice | Strength | Cost or limitation | Decision |
| --- | --- | --- | --- |
| A. Portable root `plugin.json` + `skills/` | Open format; direct fit for an instructions-and-references plugin; one package layout; documented by OpenAI and Agent Plugins v1.0.0 | Each client still controls discovery, installation, permissions, and supported components; portability is not proof of host installation | **Canonical package** |
| B. Codex compatibility manifest only (`.codex-plugin/plugin.json`) | Useful for a Codex-specific package or a client that requires Codex-only fields | Ties package discovery/metadata to one host; weaker reuse as a cross-client public artifact | Do not use as the only manifest |
| A plus generated Codex compatibility fallback | Can bridge a demonstrated client gap while keeping portable core | Two manifests require explicit precedence and synchronized fields; not needed for the documented current path | Add only after a failing compatibility test; generate from one metadata source |

Portable Agent Plugins defines a package, not a promise that every listed client supports every feature. OpenAI docs describe root `plugin.json`, `skills/`, optional MCP configuration, client-specific extensions, and a Codex compatibility fallback. A portable package containing only Skills is a supported package shape; MCP is optional and unnecessary for this repository's current content.

## Host and distribution boundaries

- **Codex CLI:** this host has `codex-cli 0.144.5`; `codex plugin` exposes `add`, `list`, `remove`, and `marketplace` commands. The installed CLI documents marketplace `add`, `list`, `upgrade`, and `remove`. This confirms local command availability, not that this package installs or activates. Marketplace runtime commands in this environment currently stop while parsing the user's existing `~/.codex/config.toml` (`agents` has a boolean where this CLI expects an `AgentRoleToml` object). Phase 00 made no user config edits.
- **Codex desktop / ChatGPT desktop:** OpenAI docs describe local repo and personal marketplaces in the desktop Plugins Directory, with Codex CLI marketplace sources also supported. A local package install and activation have not been performed in this phase.
- **ChatGPT Work on the web:** OpenAI's quickstart documents a personal plugin flow, and the universal directory is shared with Codex. This does not prove that the local repository marketplace is browsable from web Work. Treat local marketplace discovery there as unverified; public-directory access requires the separate submission path.
- **ChatGPT mobile:** the reviewed material did not establish plugin installation or Skill availability on mobile. Mark mobile support unverified; do not extrapolate from the web/desktop UI.
- **GitHub:** the public repository remains the source of truth. A repo/local marketplace can be used for authoring/testing and some team/client distribution. It is not the universal public Plugins Directory and does not itself publish a public OpenAI plugin listing.
- **Universal public directory:** OpenAI documents upload of a ZIP, automated checks, submission for review, and a separate publish action after approval. Publication is not authorized in this phase and no eligibility/account state was checked.

The current submission-error reference explicitly lists a Skills-only ZIP route, requires a supported manifest and at least one valid Skill, and says ZIP uploads are normalized to `.codex-plugin/plugin.json`. It also calls for verified publisher identity and passing safety/security scans. This portal-side normalization is part of the public-submission path; it does not mean the source repository should author two divergent manifests. Keep the portable package and a host's install route as separate deliverables, and keep claims in `compatibility-matrix.md` at those boundaries.

## Build and version model

1. Author plugin metadata and the plugin semantic version once in `config/ui-ux-pro.json`.
2. Read the 15 source Skill folders from `.agents/skills/`; preserve relative references and required assets.
3. Build the package deterministically into `plugins/ui-ux-pro/` without network access or model calls.
4. Validate required manifest fields against the published Agent Plugins schema and verify names, links, references, and file containment.
5. On CI, build to a temporary path and compare all package files with the committed package. A mismatch is a failure, not a warning.
6. Produce the ZIP and a companion release manifest containing package version, source commit SHA, file inventory, and SHA-256 hashes. Do not add that custom provenance field to root `plugin.json`.
7. Run deterministic tests and secret/license checks before attaching a release candidate to a GitHub release or submission workflow.

The package version is the only release version. Individual Skill folders do not gain independent package versions. A skill-content change requires rebuilding the plugin; the release tag ties that built version to a source commit. OpenAI directory updates for bundled Skills require a new ZIP according to current submission docs.

## Decisions deferred to implementation

- Whether the Codex compatibility overlay is actually required by the supported CLI/desktop version.
- Whether marketplace metadata is committed at repo root and which local policy values are appropriate for public contributors.
- Final publisher identity, listing copy, category, assets, and release version.
- User-account eligibility and public-directory review outcome.
- Any mobile support claim.

## Sources

- [OpenAI: Package your plugin](https://developers.openai.com/plugins/build/plugins)
- [OpenAI: Plugin architecture](https://developers.openai.com/plugins/concepts/plugins)
- [OpenAI: Skills](https://developers.openai.com/plugins/concepts/skills)
- [OpenAI: Upload and submit your plugin](https://developers.openai.com/plugins/deploy/submission)
- [OpenAI: Plugin submission errors and ZIP validation](https://developers.openai.com/plugins/deploy/submission-errors)
- [OpenAI: Plugin quickstart and personal Work route](https://developers.openai.com/plugins/quickstart)
- [Agent Plugins: Specification v1.0.0](https://agent-plugins.org/specification)
- [Agent Plugins: Overview](https://agent-plugins.org/)
