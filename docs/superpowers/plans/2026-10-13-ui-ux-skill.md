# UI/UX Skill Library Implementation Plan
> **For agentic workers:** Execute this plan in order. Keep each task small and reviewable; run the listed validation after each deliverable group.

**Goal:** Build a public, evidence-led, modular Agent Skills repository named `ui-ux-skill` that works with Codex, Claude, and compatible skill hosts, covering the approved UI/UX domains for web and Android.

**Architecture:** Keep one canonical set of Skills in `.agents/skills/`. Each task-oriented Skill has a short `SKILL.md` and focused, progressive-disclosure references. Shared repository guidance and the evidence registry live outside the Skills. An installer copies chosen Skills into platform-recognized folders without duplicating source content. Platform profiles explain how to apply design principles to web and Android without coupling the core rules to a framework.

**Tech Stack:** Markdown, CSV/JSONL for source and evaluation data, Python 3 standard library for install and repository validation, Git/GitHub.

**Approved spec:** Modular task-oriented architecture; public repository `ui-ux-skill`; CC BY 4.0 for original repository-authored content. Use synthesized guidance and attributable links; do not republish third-party prose/assets or imply that upstream material is relicensed.

## Global Constraints

- Map the 14 approved domains: UI/UX foundations; color and palettes; ethical persuasion; layout/cards/spacing/hero; product interaction; buttons/navigation; Persian typography/RTL/readability; responsive/adaptive design; visual hierarchy; accessibility; design systems/tokens; information architecture; forms/errors/validation; customer journey/user flows.
- Keep skills task-oriented, with common discovery/implementation/review flow and domain-specific references. Do not create one Skill per source.
- Distinguish standards, empirical research, practitioner guidance, hypotheses, and aesthetic judgment. Cite the source registry by stable ID and use qualified language for context-dependent findings.
- Respect the two-pass, five-source checkpoint workflow already recorded in `work/ui-ux-source-ledger.csv`. Preserve partial verification and access limitations in the published registry.
- Provide adapters/examples for web and Android, including a Compose example; keep framework-specific advice separate from platform-independent design principles.
- Include positive and negative activation cases, quality scenarios, source-use checks, and regression cases. Do not claim a scenario passed without recorded evidence.
- Keep Persian/RTL guidance explicit about mixed-direction text, numerals/dates/currency, phone/OTP fields, icon direction, typography, mobile, zoom, contrast, and accessibility; never impose RTL on LTR interfaces.

## Review Focus

- Does each Skill activate for its intended task and avoid unrelated tasks?
- Are recommendations traceable to reviewed sources and appropriately scoped?
- Are rights, attribution, access status, editions, and review date clear?
- Can a user install the selected skills into Codex, Claude Code, VS Code/Copilot, or another compatible location from one canonical source?
- Do examples make the advice actionable without prescribing an unnecessary framework or aesthetic?

---

## Task 1: Repository foundation and source registry

**Files:** `README.md`, `AGENTS.md`, `LICENSE`, `.gitignore`, `docs/source-registry.csv`, `docs/source-review.md`, `docs/domain-coverage.csv`, `skills/index.md`.

1. Initialize the project as a Git repository in `outputs/ui-ux-skill` and set public-facing metadata to `ui-ux-skill`.
2. Copy the 124-row reviewed reference ledger into `docs/source-registry.csv`, enriching rows with source class, evidence type, access/edition state, relevant domains, and review date while retaining stable IDs and limitations.
3. Reconcile all IDs, URLs, labels, and partial-verification notes against the working ledger. Do not silently upgrade partial rows.
4. Add the exact CC BY 4.0 license text with a clear scope statement for original repo content; third-party sources remain under their own terms.
5. Write a short README and root AGENTS guidance that explains purpose, layout, provenance, installation, contribution and non-claims.
6. Add a 14-domain coverage map to the planned Skills and sources.

**Validation:** CSV parses; IDs 1–124 are unique and complete; every source URL and label is retained; all six partial rows remain visibly partial; license scope is unambiguous.

## Task 2: Canonical task-oriented Skills

**Files:** `.agents/skills/{ux-discovery,interface-layout,interaction-patterns,design-systems,responsive-design,accessibility-inclusive-design,persian-rtl-localization,ui-ux-review}/SKILL.md` plus focused `references/*.md` files as required.

1. Create eight concise Skills with valid frontmatter (`name`, specific `description`) and clear trigger boundaries.
2. Give each Skill an actionable workflow: clarify goals and constraints, inspect the actual product/code/platform, choose proportionate patterns, explain trade-offs, implement or review, and verify stated outcomes.
3. Add focused reference notes with source IDs; synthesize in original language and avoid copying source prose.
4. Include ethical boundaries for persuasion, explicit evidence labels, and context-sensitive guidance instead of universal recipes.
5. Include accessibility and RTL checks where relevant, with the dedicated Skills providing deeper detail.

**Validation:** Run the official bundled `quick_validate.py` on every Skill folder. Inspect frontmatter, descriptions, relative links, progressive disclosure, trigger overlap, and source attribution.

## Task 3: Cross-platform installation and adapters

**Files:** `scripts/install-skills.py`, `docs/installation.md`, `docs/platforms/codex.md`, `docs/platforms/claude.md`, `docs/platforms/vscode-copilot.md`, `docs/platforms/other-hosts.md`, `adapters/web.md`, `adapters/android.md`, `adapters/compose.md`.

1. Implement a safe, standard-library installer that lists available Skills and copies selected folders to a user-specified target.
2. Support documented target layouts for Codex (`.agents/skills`), Claude Code (`.claude/skills`), and VS Code/Copilot (`.github/skills` or `.agents/skills`).
3. Explain manual import and compatibility boundaries for other hosts using the Agent Skills format.
4. Keep framework adaptation separate and provide web and Android/Compose implementation notes grounded in source IDs.

**Validation:** Exercise list, help, one-skill install, all-skill install, and refusal on overwrite without an explicit option using temporary directories only. Confirm copied output matches the canonical `SKILL.md` bytes.

## Task 4: Examples, evaluations, and coverage

**Files:** `examples/web/`, `examples/android/`, `evals/activation.jsonl`, `evals/quality-scenarios.md`, `evals/regression-matrix.csv`, `docs/domain-coverage.csv`.

1. Add at least one web and one Android example showing a grounded design/review output with source IDs, decisions, and verification boundaries.
2. Create positive/negative activation cases for every Skill and boundaries between overlapping Skills.
3. Define scenarios for evidence grounding, accessibility, Persian/RTL, responsive states, forms, design-system reuse, and context efficiency.
4. Record expected behavior and an unrun status until an actual model evaluation is performed; do not label authored scenarios as passed tests.
5. Ensure every approved domain maps to one or more Skills, examples, and sources.

**Validation:** Parse JSONL and CSV; check every Skill has positive and negative examples, every domain is covered, and every referenced source ID exists.

## Task 5: End-to-end repository review and GitHub publication

**Files:** all deliverables above; repository metadata on GitHub.

1. Run repository validation and the authorized Skill validators; inspect the generated install targets in disposable directories.
2. Review links, attribution, claim strength, privacy, platform-specific guidance, and partial-source limitations.
3. Confirm that repository content is original synthesis and source links/metadata, not copied upstream materials.
4. Initialize the default branch, commit the reviewable result, create the explicitly requested public GitHub repository `ui-ux-skill`, and push it.
5. Verify the repository URL, public visibility, default branch, and pushed commit before reporting success.

**Validation:** Report exact commands/results, local commit SHA, public repo URL, and any model-evaluation or source-access limitations that remain.
