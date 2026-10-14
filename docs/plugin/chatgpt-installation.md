# ChatGPT installation and compatibility guide

This guide distinguishes a validated portable package from a ChatGPT plugin installed in an account and from a Skill actually used in a conversation. Phase 03 prepared and validated the package; it did not install or publish it in any ChatGPT account.

## Verified package

- Plugin ID: `ui-ux-pro`
- Version: `0.1.0`
- Portable manifest: root `plugin.json`
- Skills: 15 under `skills/`
- References: 18 Markdown files under Skill `references/` directories
- Archive: [`ui-ux-pro-0.1.0.zip`](https://github.com/SAeedajf/ui-ux-skill/actions/runs/38588593437/artifacts/11906343261)
- SHA-256: `611b8eddaf74821dd2a1dd6a1d8ae576c32e20b4b23db12ec7021aa6ae634c7c`
- Plugin source/main commit: `819c432a64cee55c2a4d31b406817038c7ab5713`
- CI provenance commit: `96686641dfec26a25d65c88397ebe1a6aad14857` (GitHub's PR test merge commit; its parents are the main commit above and Phase 03 output commit `f397de44cbb06b38625dfd4682ca798575373214`)

The link is a GitHub Actions artifact from the public repository. It is a downloadable build artifact, not a listing in the Universal Plugin Directory. GitHub retains workflow artifacts for a limited time; if this link expires, download the artifact from a successful, current Actions run or rebuild with `scripts/build-plugin.py --archive`.

## ChatGPT Work Web: private personal plugin

OpenAI documents personal plugins and using plugins in Work on the web. The official quickstart demonstrates a personal plugin backed by MCP. The portable package format also permits Skills without MCP, and Work mode can use local marketplace sources, but this phase did not establish that ChatGPT Work Web can import this exact Skills-only ZIP into a personal plugin. Treat that specific route as unverified until the owner sees it in their account.

1. Download the ZIP above and keep the SHA-256 for integrity checking.
2. In ChatGPT Work, open Plugins and check whether your account exposes Plugin Creator and a personal plugin creation flow.
3. Attach the ZIP and use the prompt in [chatgpt-personal-plugin.md](chatgpt-personal-plugin.md).
4. Ask Plugin Creator to confirm that it imported the archive and retained the `ui-ux-pro` identity and 15 skills. If it cannot import the ZIP, stop and use the local marketplace route below; do not let it silently rebuild or omit skills.
5. Before saving, verify the target is **Personal**. Do not share it with a workspace or publish it to a directory.
6. If creation completes, install it yourself, open a new Work conversation, select it with `@`, and run the cases in [chatgpt-test-cases.md](chatgpt-test-cases.md).

Personal plugin availability, plan eligibility, and account controls were not inspectable from this Codex session. The Web ZIP upload control described by OpenAI Help is permission-gated and is a workspace-admin path; it should not be presented as a confirmed personal-plugin importer. See [Plugins in ChatGPT](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt).

## ChatGPT Desktop: local marketplace route

OpenAI documents repository and personal marketplaces in the Plugins Directory for Work mode and Codex in the ChatGPT desktop app. For a private local install, keep the package in a folder available only to your account and make a personal marketplace point to it. The paths below are examples; the owner must choose and review the destination before running them.

1. Download and extract the ZIP into a user-selected private folder.
2. Place the extracted plugin folder under `~/.codex/plugins/ui-ux-pro/` (the folder must contain `plugin.json`, `LICENSE`, and `skills/`).
3. Create `~/.agents/plugins/marketplace.json` with a local source:

   ```json
   {
     "name": "ui-ux-pro-personal",
     "interface": { "displayName": "UI/UX Pro" },
     "plugins": [
       {
         "name": "ui-ux-pro",
         "source": { "source": "local", "path": "./.codex/plugins/ui-ux-pro" },
         "policy": { "installation": "AVAILABLE", "authentication": "ON_INSTALL" },
         "category": "Creativity"
       }
     ]
   }
   ```

   This example assumes the personal marketplace root is the user's home directory, matching the documented `~/.agents/plugins/marketplace.json` and `~/.codex/plugins/` layout. Resolve and check the path against the actual marketplace root before installing. If the chosen folder layout differs, update the relative path accordingly.

4. Restart ChatGPT Desktop, open Plugins, select the personal marketplace, inspect `ui-ux-pro`, then choose Install only if the details show all 15 Skills.
5. Start a new conversation and perform the explicit and implicit tests in `chatgpt-test-cases.md`.

This Desktop route is documentation-backed but was not run on the owner's machine. The Phase 03 environment did not expose a ChatGPT Desktop test profile. Do not copy these files into the user's home or edit their marketplace automatically.

## Workspace ZIP upload

ChatGPT Help documents uploading a plugin ZIP on the web when the upload option is available and the account has eligible workspace permissions. This is not the same as creating a personal plugin. New workspace plugins can start private, but sharing and publishing to the workspace directory are separate permission-controlled actions. The owner's plan, role, and upload permission are unknown, and Phase 03 did not enter an Admin Console, upload a ZIP, create a workspace plugin, or change workspace visibility.

If the owner chooses this route, they should first verify the displayed target workspace and permissions, then upload the exact ZIP and keep the resulting plugin private. Do not select Share or Publish to workspace directory.

## Removal and rollback

For a local marketplace install, uninstall the plugin in the Plugins Directory, then remove only the personal marketplace entry and extracted folder that the owner created. Keep a backup until a new conversation confirms the previous workflow is restored. Do not remove legacy Skills automatically or delete unrelated plugins.

For a workspace plugin, use the workspace administrator's plugin controls and confirm affected members/apps before disabling or removing it. No rollback was performed in Phase 03 because no ChatGPT installation was made.

## Official references

- [OpenAI: Package your plugin](https://developers.openai.com/plugins/build/plugins)
- [OpenAI: Plugin quickstart](https://developers.openai.com/plugins/quickstart)
- [OpenAI Help: Plugins in ChatGPT](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt)
