# Security and provenance review — Phase 04

Review date: 2026-10-14. Scope: canonical 15 Skills, generated `plugins/ui-ux-pro` package, 18 packaged reference files, repository source registry, deterministic ZIP, and public-submission provenance. This is an engineering review, not a legal opinion or formal external security audit.

## Package security checks

| Check | Result | Evidence and limits |
|---|---|---|
| Manifest schema, exact 15 Skill IDs, YAML frontmatter | PASS | `scripts/validate-plugin.py`; schema is the vendored Agent Plugins 1.0.0 schema. |
| Exact package-to-canonical source bytes | PASS | `scripts/build-plugin.py --check --archive` and `validate-plugin.py`. |
| Secret/token signatures and private-key blocks | PASS | Packaging validator signature scan; no matching credentials found. Pattern scanning cannot prove absence of every secret format. |
| Absolute/private paths | PASS | Targeted path scan of package content found no machine-specific home path or credential. Generic user-home migration examples are intentionally documented in the repository guide and are not packaged. |
| Binary, hidden, key, env, cache files | PASS | Package build only emits UTF-8 source, root manifest, and LICENSE; archive inventory has 35 regular files. |
| Symlink and path traversal | PASS | ZIP contains no symlinks, absolute members, or `..` path components; `ZipFile.testzip()` returned `None`. |
| Dangerous shell/download/evaluation patterns | PASS | Targeted scan of packaged source found no `rm -rf`, `sudo`, piped download-to-shell, `eval(`, credential literals, or private key blocks. This is a bounded signature scan. |
| Prompt-injection-like instruction signatures | PASS, bounded | Targeted scan found no instruction to reveal system/developer prompts or ignore higher-priority instructions. A signature scan does not establish semantic safety; reviewer should still treat linked third-party content as untrusted input. |
| Hidden service/backend/API dependency | PASS | Root manifest has no MCP server, app, hook, backend, or API configuration; source package remains Skills-only. |

## Source and rights provenance

- The canonical source registry has 124 entries: the repository validator reports 118 reviewed and 6 partially verified. Registry identifiers and per-source evidence remain in [`docs/source-registry.csv`](../source-registry.csv).
- Keep these six rows partial; this phase supplies no new source-specific evidence that justifies upgrading them: S36 Material Design 3 Cards, S50 Material Design 3 Buttons & Navigation, S94 *Atomic Design*, S100 Baymard Homepage & Category Navigation, S102 *How to Make Sense of Any Mess*, and S109 Baymard Checkout UX.
- S20 Coolors is labeled `reviewed` in `review_status`, while its pass-2/checkpoint notes say the direct page was inaccessible and only the official search index/public overview was checked. Do not cite inaccessible full content or treat this as full-content verification; clarify the intended `review_status` versus `access_status` distinction in a later registry maintenance pass. S20 is not one of the six rows with `review_status=partially_verified`.
- The package contains the project's original Skill instructions and author-written reference notes with links/attribution, not copied books, paid articles, screenshots, brand images, or third-party logos. The 124-row registry is not bundled into the ZIP.
- The repository's CC BY 4.0 license covers only material the project has rights to license. It does not relicense linked sources or grant rights to third-party books, commercial research, screenshots, trademarks, or other assets.
- The access/provenance notes identify commercial/paywalled and practitioner material. Do not imply full access to Baymard premium findings or that a link alone establishes a reuse license.
- `LICENSE` and source-level attribution were included in the ZIP. Whether every contribution and reference is legally cleared for a public directory still needs human rightsholder review.

## Decision

Automated package security and provenance structure: `PASS` for the checks listed above. Human rights clearance: `NEEDS_REVIEW`. Public release: `NOT_READY` until the human review resolves the six partial-source evidence records, clarifies how S20's direct-page access limit should be represented, and supplies verified publisher/listing requirements in `publication-readiness.md`. No content was copied or modified from any third-party source during this phase.
