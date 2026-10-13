# Codex CLI diagnostic evidence

Date: 2026-10-13 (UTC)
Worktree baseline commit: c0706603544d881c51e021cb769442d823ecad50
CLI: `codex-cli 0.153.4` (`codex --version`)
Configured requested model: `gpt-6-luna` (from the user's Codex configuration; value not changed).

## Configuration parser

A normal CLI invocation fails while parsing `/home/saeed/.codex/config.toml` at line 12, `[agents]`: `invalid type: boolean true, expected struct AgentRoleToml`. The table contains scalar settings `agents.enabled = true`, `agents.default_subagent_model = "gpt-6-luna"`, and `agents.default_subagent_reasoning_effort = "high"`. The current published Codex configuration reference lists these three scalar keys as valid under `agents`; this is a local CLI/parser vs documented schema mismatch. No persistent config edit was made, so no backup was required.

Official reference: https://developers.openai.com/codex/config-reference

## Isolated model compatibility attempt

Command: `codex exec --ignore-user-config --ephemeral --model gpt-6-luna --json '<harmless interface prompt>'`
Result: CLI initialized and emitted `thread.started`, then the API returned HTTP 400: `The 'gpt-6-luna' model is not supported when using Codex with a ChatGPT account.` No model response was generated. Skills initialized, and Codex reported that skill descriptions were shortened to fit its context budget while all skill metadata remained visible. This is not activation evidence.

The required policy for this task permits only `gpt-6-luna`; no alternate model was selected.

## Discovery metadata probe

`CODEX_HOME=/tmp/ui-ux-codex-home-diagnostic codex debug prompt-input '<Persian RTL checkout review prompt>'` completed with a JSON prompt-input list. All 15 canonical repository Skill names were present in the metadata context; the sanitized list is in `codex-discovery-manifest.json`. This establishes that the Skills are discoverable to the CLI's prompt-input builder in this isolated probe; it does **not** establish automatic selection, body loading, or execution. The raw prompt-input dump is intentionally not committed because it includes host instructions.

## Android availability

`adb` is present at `/home/saeed/platform-tools/adb` and `adb devices` returned no attached devices; `ANDROID_HOME`, `ANDROID_SDK_ROOT`, and `JAVA_HOME` are unset, and neither `java` nor `gradle` nor a known SDK directory was found. Android build/runtime work is blocked pending a configured SDK/JDK.
