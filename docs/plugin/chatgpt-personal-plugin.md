# Owner steps: create a private UI/UX Pro plugin

Phase 03 did not access the owner's ChatGPT account or create/install a plugin. Use this guide only when the owner is ready to act in ChatGPT.

## Download and verify

Download the verified archive from [GitHub Actions](https://github.com/SAeedajf/ui-ux-skill/actions/runs/38586939721/artifacts/11904964103):

```text
ui-ux-pro-0.1.0.zip
SHA-256: 611b8eddaf74821dd2a1dd6a1d8ae576c32e20b4b23db12ec7021aa6ae634c7c
```

Verify the checksum before attaching the file. The current artifact is tied to source commit `819c432a64cee55c2a4d31b406817038c7ab5713` and contains portable root `plugin.json`, `LICENSE`, 15 skills, and their references.

## Request for Plugin Creator

In ChatGPT Work, install/open `Plugin Creator` if it is available, attach the ZIP, and paste this request:

> Create a **personal, private, skills-only** ChatGPT plugin named UI/UX Pro from the attached `ui-ux-pro-0.1.0.zip`. Preserve plugin ID `ui-ux-pro`, version `0.1.0`, and all 15 Skills with their bundled references. Do not create an MCP server, app, hook, external API dependency, or public/workspace-directory listing. Do not change or omit any Skill. Before saving or installing, show me the target scope and confirm the archive contents. If this ChatGPT surface cannot import the ZIP or cannot create a personal plugin, stop and explain the supported alternative; do not reconstruct it from memory.

This prompt is prepared for the owner; direct ZIP import into a personal Plugin Creator flow was not verified. Do not interpret a generated preview or a saved draft as a completed install.

## Confirm private scope

Before saving, verify the UI identifies the plugin as Personal and not as a Workspace plugin. If ChatGPT only offers a workspace upload control, cancel unless the owner specifically intends that workspace scope. A newly created workspace plugin being private by default does not authorize sharing or directory publication.

After the owner chooses to install, verify the plugin appears in Personal/Installed, open a new Work chat, select it explicitly with `@`, and run the explicit test first. Then run positive and negative cases from `chatgpt-test-cases.md`. Record the exact surface, plugin version, skills observed, response, and available evidence. ChatGPT may not expose a trace that proves which individual Skill file was read; if so, report that limitation.

## Supported fallback: local marketplace in ChatGPT Desktop

If the Work web account cannot import the archive as a personal plugin, the documented local marketplace route is available for the ChatGPT desktop app. Follow [chatgpt-installation.md](chatgpt-installation.md#chatgpt-desktop-local-marketplace-route). This route requires the owner to place files and a marketplace catalog in their own user directories; Phase 03 did not run those commands.
