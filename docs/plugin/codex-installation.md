# Install UI/UX Pro in Codex

This guide describes the Codex CLI workflow verified for UI/UX Pro `0.1.0` with Codex CLI `0.144.5`. It uses the repository's Git marketplace catalog at `.agents/plugins/marketplace.json` and the plugin source at `plugins/ui-ux-pro`.

## Prerequisites

- Codex CLI with `codex plugin marketplace` and `codex plugin add` support. Check `codex --version`, `codex plugin --help`, and the subcommand `--help` before installing.
- Access to the repository on GitHub, or a local clone for local-only installation.
- A Codex session to invoke the model. The marketplace can be added and the plugin installed without signing in, but model activation and task execution need an authenticated session and available usage.

## Install from GitHub

From a clean Codex environment, add this repository as a marketplace. To pin a reviewed branch or release, pass the exact ref:

```sh
codex plugin marketplace add SAeedajf/ui-ux-skill --ref main
codex plugin marketplace list
codex plugin list --available --marketplace ui-ux-pro-marketplace
codex plugin add ui-ux-pro@ui-ux-pro-marketplace
codex plugin list
```

The Phase 02 GitHub test uses a disposable `HOME` and `CODEX_HOME` and a fixed branch ref; see [the verification record](marketplace-verification.md). The commands above are the corresponding user workflow; they do not make the user's installation persistent during this report's tests.

## Install from a local clone

From the repository root:

```sh
codex plugin marketplace add .
codex plugin marketplace list
codex plugin list --available --marketplace ui-ux-pro-marketplace
codex plugin add ui-ux-pro@ui-ux-pro-marketplace
codex plugin list
```

The catalog's `source.path` is `./plugins/ui-ux-pro`, resolved from the repository/marketplace root. It is not relative to `.agents/plugins`.

## Confirm installation and discovery

`codex plugin list` should show `ui-ux-pro` as installed and enabled. The CLI's cache path contains `.codex-plugin/plugin.json` and the plugin's `skills/` tree. Codex discovers skills from that plugin tree; do not copy them into a project `.agents/skills/` directory as part of plugin installation.

For diagnostic skill discovery without invoking a model, run `codex debug prompt-input` from an otherwise empty project using the same Codex environment. Verify that all 15 `ui-ux-pro:<skill-id>` entries point into the installed plugin cache. This is discovery evidence only; it does not prove that the model selects or follows a skill.

## Activation and account limits

Plugin installation and skill discovery can be checked without a model. Positive/negative automatic selection and practical code repair require a logged-in Codex session and available model usage. The clean Phase 02 environment was deliberately not logged in; those model gates remain unverified. Do not copy credentials or authentication state into a disposable environment.

## Remove or roll back

Use the exact installed plugin identifier shown by `codex plugin list`:

```sh
codex plugin remove ui-ux-pro@ui-ux-pro-marketplace
codex plugin marketplace remove ui-ux-pro-marketplace
codex plugin list
codex plugin marketplace list
```

The removal commands were checked against CLI help. Phase 02 performed installation tests in disposable directories and removed those directories after recording evidence; it did not remove anything from the user's Codex home. For migration and recovery of legacy copies, see [duplicate-skills-migration.md](duplicate-skills-migration.md).

## Common issues

- **Plugin commands are missing:** check the installed CLI version and its `codex plugin --help`; this report verifies CLI `0.144.5` only.
- **Marketplace source is not found:** run marketplace commands from the repository root for local install, or verify GitHub access and the requested `--ref`.
- **Plugin appears unavailable:** check that the marketplace name is exactly `ui-ux-pro-marketplace` and that the catalog lists `ui-ux-pro` with `installation: AVAILABLE`.
- **Skills appear twice:** compare plugin-prefixed entries with legacy unprefixed entries. Follow the reversible migration steps before disabling legacy copies.
- **The model does not activate a skill:** `debug prompt-input` proves discovery only. Confirm login/usage and capture an actual model trace before claiming activation.
