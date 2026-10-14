# Public directory readiness checklist

Prepared 2026-10-14 from current [OpenAI plugin submission requirements](https://developers.openai.com/plugins/deploy/submission), [submission error reference](https://developers.openai.com/plugins/deploy/submission-errors), and [plugin guidelines](https://developers.openai.com/plugins/plugin-guidelines). This is a checklist only. No portal, account, identity, or public visibility was changed.

## Package checks

- [x] ZIP integrity and deterministic build: PASS; SHA-256 is recorded in the Phase 04 report.
- [x] Portable root `plugin.json`, one plugin root, exact 15 Skill directories, and skills-only package structure: PASS.
- [x] No MCP server, backend, app, hooks, or hidden API configuration.
- [x] Internal reference validation, inventory and source provenance sidecar: PASS.
- [ ] OpenAI directory security/policy scans for every bundled Skill: not run; the official submission workflow scans uploaded Skills and requires successful current results before submitting.
- [ ] Resolve all findings from the portal for the selected package version: not run.

## Listing metadata and identity

- [x] Stable package name `ui-ux-pro`, version `0.1.0`, repository URL, and license identifier are present.
- [ ] Public listing display name, short description (30 characters max), long description (4,000 max), verified developer name, and category must be supplied in submission metadata.
- [ ] `author.name` and public-submission interface/listing metadata are not present in the current minimal portable manifest. Do not invent an author name, publisher identity, or category. Add only after the owner supplies the exact verified identity and selected metadata.
- [ ] Individual or business publisher identity must be verified in the OpenAI Platform Dashboard. Current private USER plugin ownership does not prove public publisher verification or submission eligibility.
- [ ] Skills-only plugins may have additional directory eligibility requirements; confirm them in the portal before submission.
- [x] Website, support, privacy, and terms URLs are optional for ZIP uploads of skills-only plugins under the current submission field reference. Do not invent URLs. Recheck if the package architecture changes.

## Review materials and process

- [x] Internal operational acceptance cases T01–T07 are prepared in `chatgpt-test-cases.md`; results remain `NOT_RUN`.
- [ ] Public directory Skill scans and all review findings: not run.
- [x] Five positive/three negative MCP test cases and a demo recording are not package requirements for a skills-only plugin in the current submission documentation; those requirements apply to remote MCP plugin review. Product acceptance tests remain useful and are still pending.
- [ ] Confirm organization/project ownership and required Apps Management write permission; unknown and not inspected.
- [ ] Complete required policy attestations and submit the draft for review only after package scans, metadata, publisher verification, and rights review pass.
- [ ] Wait for OpenAI review/approval; approval does not publish automatically. The owner must explicitly choose when to publish.
- [ ] Public visibility and any country availability remain owner decisions.

## Current decision

`PUBLIC_RELEASE_READY = NO`. The package may be reviewed as a private Release Candidate, but publisher verification, listing fields, directory scans, final human rights clearance, and real operational acceptance are incomplete. Do not upload, submit, or publish this package without a separate owner decision.
