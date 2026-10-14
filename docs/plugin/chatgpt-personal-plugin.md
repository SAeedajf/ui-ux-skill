# Owner-run checks for the existing private ChatGPT plugin

## Current verified state

On 2026-10-14, the official Plugin Creator metadata reader returned:

- Plugin ID: `plugins_6acfa25d79388191b9861545d52f6d03`
- Release ID: `pluginrel_6acfa26265f48191b194fe33780fbe70`
- Name: `ui-ux-pro`; version: `0.1.0`
- Scope: `USER`; visibility: `PRIVATE`
- Current release metadata confirms creation only. It does not expose installation in ChatGPT Work, discovery in a conversation, Skill activation, or execution.

Do not recreate, replace, upload a new release, change the audience, or publish this plugin during the checks. Open the existing [private plugin](https://chatgpt.com/plugins/plugins_6acfa25d79388191b9861545d52f6d03) in the intended ChatGPT Work account.

## Owner procedure

1. Confirm the page identifies the exact plugin ID above and Personal/Private scope. If the ID or scope differs, stop and record the screen state.
2. Check whether it is already installed. If not, install the existing private plugin from this page only. Do not upload the Phase 04 ZIP or choose an update/release action.
3. Start a fresh Work conversation. Select UI/UX Pro explicitly using the plugin picker/`@` flow and run T01. Record selection and the resulting response separately.
4. In a separate fresh conversation, leave the plugin unselected and run T02 as an automatic positive activation check. Then run T07 as a negative control. Do not mention a Skill name in the positive prompt.
5. Run T03–T06 as additional capability checks. Inspect available plugin/Skill status and evidence. If ChatGPT does not show a per-Skill trace, mark individual Skill loading `UNVERIFIED`; a response naming a Skill is not proof that its file was read.
6. Inspect the installed plugin's Skills list and any legacy/personal Skills with matching IDs. Record duplicates and the visible namespace or path. Do not delete or move any Skill as part of this test.

## Result interpretation

| Observation | Record as |
|---|---|
| Plugin page reports Personal/Private; exact ID matches | `CREATED` confirmed |
| Plugin appears in installed list | `INSTALLED` |
| Plugin appears in Work's plugin picker | `DISCOVERED` |
| Explicitly selected T01 runs successfully | `EXPLICITLY_INVOKED`; this alone does not prove automatic activation |
| Unselected, relevant T02 causes UI/UX behavior and a visible trace confirms the Skill | `ACTIVATED` / `EXECUTED` for that trace only |
| T07 selects/loads a UI/UX Skill without a UI/UX need | Negative test `FAIL` |
| No trace is exposed | Skill activation remains `UNVERIFIED`, even if the answer is good |

## Distinguishing installation and execution failures

- If the plugin is absent from the installed list, diagnose `INSTALLATION` first. Record the exact account surface and visible error; do not infer anything about model routing.
- If installed but absent from the Work picker, diagnose `DISCOVERY` or surface/account eligibility. Record the active workspace/surface and refresh/new-chat behavior.
- If present and selected but the explicit test has no relevant result, record an `EXECUTION` failure. Preserve the prompt, answer, plugin version, and any visible trace.
- If explicit invocation works but unselected T02 does not activate, record explicit invocation as successful and automatic activation as failed or unverified, according to the available trace.
- Keep ChatGPT results separate from Codex CLI discovery and from the existing Plugin Creator metadata.

## Evidence form

For each T01–T07, copy and complete:

```text
Test ID:
Date/time and timezone:
ChatGPT surface and account/workspace scope:
Plugin ID / version:
Installed state:
Discovered in picker:
Explicitly selected (yes/no):
Prompt (exact):
Observed Skills / trace paths:
Response or visible error:
Screenshot, trace, or evidence location:
Result: PASS / FAIL / BLOCKED / NOT_RUN / NEEDS_REVIEW
Limitations:
```

Do not attach credentials or private user data to the repository. Keep any account screenshots or traces local to the owner unless sanitized before sharing.
