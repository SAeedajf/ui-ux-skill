# UI/UX Pro plugin implementation roadmap

This roadmap follows Phase 00. It is a proposal, not authorization to start later phases. The owner explicitly asked this run to stop after Phase 00.

## Phase 01 — Build a reproducible portable package

**Goal:** produce a valid skills-only portable package from the existing 15 canonical Skills.

- Add one source metadata/version file.
- Build `plugins/ui-ux-pro/` from `.agents/skills/` while preserving references and assets.
- Add the root portable `plugin.json`; do not add MCP configuration or service dependencies.
- Add `scripts/build-plugin.py` and `scripts/validate-plugin.py` using the standard library where practical.
- Validate against the canonical Agent Plugins v1.0.0 schema and enforce path containment, required files, all 15 skill IDs, and local-reference integrity.
- Validate ZIP upload constraints from OpenAI's current submission error reference: one plugin root, no absolute/parent paths, regular readable files, valid manifest, at least one Skill, and current archive size/entry limits.
- Add repo marketplace metadata only if the documented source-path/policy format is fully validated; keep it separate from the package.
- Add deterministic tests for repeatable output, package contents, reference links, and version/source metadata.
- Add CI that rebuilds to a temporary directory, compares generated package files, runs package validation, and produces a report. Keep model-based evals out of required CI.

**Exit evidence:** clean checkout build, 15/15 Skills, portable schema pass, no missing local references, stable second build, no secrets, exact source commit recorded.

## Phase 02 — Codex installation and activation

**Goal:** prove install, discovery, and activation independently for the supported Codex targets.

- First resolve the current Codex user-config parse blocker without overwriting the user's settings; prefer a disposable `CODEX_HOME` and no credentials for package-level CLI tests.
- Verify `codex plugin marketplace add/list`, plugin listing/add/remove, and exact argument syntax against the installed binary.
- Test both direct repo marketplace and local package installation in a clean environment.
- Test no duplicate loading when existing `.agents/skills/` are present; document one recommended install path.
- Run the 32 positive/negative activation cases on the user's selected model only if the host can execute it. The original 30 traces remain `NEEDS_REVIEW`; the OTP-specific positive/negative pair is `NOT_RUN`. Keep automatic traces `NEEDS_REVIEW` until human review, and preserve `BLOCKED` for usage-limit or environment failures.
- Test the desktop UI only as a separate surface; don't infer desktop success from CLI results.

**Exit evidence:** per-surface package/source commit, install location, 15-skill discovery inventory, invocation traces, exact model selection provenance, blocker list.

## Phase 03 — ChatGPT surfaces and workspace route

**Goal:** establish the exact supported ChatGPT installation route without conflating account surfaces.

- Use official Plugin Creator or local repository marketplace guidance for a personal test package.
- Test ChatGPT desktop local marketplace separately from ChatGPT Work web personal plugin support.
- Test workspace publication only with an authorized workspace admin; keep workspace-only distribution distinct from the universal directory.
- Verify mobile only if current documentation and an available test client explicitly support the target scenario.
- Keep Claude Code tests out of scope until the owner reopens them.

**Exit evidence:** surface-specific status, account/workspace prerequisites, fresh conversation discovery, invocation trace, and a clear `UNVERIFIED` state where testing is unavailable.

## Phase 04 — Release candidate and optional public submission preparation

**Goal:** prepare a traceable ZIP and review checklist, without publishing by default.

- Generate a versioned ZIP and adjacent SHA-256 manifest from a clean commit.
- Audit all package files for secrets, third-party content/assets, attribution, and license scope.
- Prepare publisher identity, category, listing fields, and required policies only after the owner supplies/approves them.
- If the owner asks for public submission, use the official OpenAI ZIP upload and review process; uploading, approval, and publishing are separate gates. Do not publish without explicit authorization.

**Exit evidence:** exact package SHA, source commit, all structural/local tests, license/provenance review, and separately stated submission/publish state.

## Cross-phase rules

- Maintain exactly 15 canonical Skills and map all 14 requested domains in the existing inventory.
- Preserve references, source attribution, and the six partial-review labels.
- No runtime server, API key, paid model, or network dependency for the skills-only package.
- Never promise all-host compatibility, quota bypass, mobile availability, or public listing without direct evidence.
- Keep test output, package validation, host install, host activation, quality, and public review as distinct states.
