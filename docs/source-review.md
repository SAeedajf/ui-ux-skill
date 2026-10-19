# Source review notes

The registry preserves all 124 original user-supplied links and adds five clearly labeled curated follow-up references. The five additions received two review passes and a checkpoint after the group; the source review was updated through 2026-10-19. Original rows retain their individual review dates. Use the linked primary page for claims; this registry is a research map, not an endorsement or substitute for reading the source.

## Implementation trace audit (2026-10-19)

The original user-supplied source list contains 135 Markdown link occurrences, including 11 repeated links, for 124 unique URLs. All 124 unique URLs match `submitted_url` in this registry; the cross-check found no missing or extra source. The five added records have `source_origin=curated_follow_up`, blank `submitted_url`, and an editorial `curated_scope_fa` note; they are not represented as links supplied by the user. An older internal note saying 155 unique URLs is not supported by the original list and is not the registry target.

[`source-implementation-audit.csv`](source-implementation-audit.csv) gives one row per source with its topic domain, routed Skill(s), reference path, evidence/access class, provenance, and trace strength. In the Skill reference files, the original sources remain individually linked or grouped as documented; the new sources have direct individual links in focused references. The audit records a topic-level role and does not claim every recommendation came from every source. It carries both review-pass notes, access caveats, and review dates. For the original 124 links, `submitted_scope_fa` preserves the user's Persian descriptions, including alternate descriptions for repeated links. Added sources use `curated_scope_fa` for editorial scope. Neither description field is evidence that a linked source supports every detail. For a new claim, inspect the exact current page and observe the row's evidence and access limits.

The implementation trace audit does not replace the source-content review recorded below: two-pass notes and five-source checkpoints remain in each registry row. The new five-source checkpoint was reviewed as one batch; the six older partially verified sources remain partial.

## Curated follow-up references added 2026-10-19

- **S125 GOV.UK content design:** adds a content-design/UX-writing evidence lane for user need, content format and lifecycle. UK public-service/plain-English context; not a universal copy standard.
- **S126 GOV.UK moderated usability testing:** adds a task-based moderated research method reference. The page was last updated in 2017; check current privacy and ethics rules.
- **S127 Apple HIG Layout:** adds an Apple-only responsive/adaptive adapter for window, safe-area, text scaling, orientation, and localization decisions. It is not a web-wide breakpoint prescription.
- **S128 W3C WCAG-EM 2.0:** adds an informative evaluation-planning and reporting methodology. It does not replace normative WCAG criteria; sampling does not establish whole-site conformance.
- **S129 GOV.UK Design System error message:** adds a context-specific reference for field/service errors, association, summary, and recovery. Verify localized copy, semantics, and behavior in the target product.

Together these sources cover gaps in content design/UX writing, Apple platform guidance, usability testing, accessibility evaluation methodology, and error-state implementation. The registry maps them into existing task Skills and adds R14 (UX content designer and interface writer); it does not increase the Skill count.

`docs/domain-coverage.csv` maps every source ID to its registry domain; related domains may also cross-reference a source. The `source_ids` column is an index, not evidence that each source is equally authoritative or that every method fits every task. For an operational recommendation, use the source's evidence class and access notes and choose the relevant method for the user's actual question.

## Evidence classes

- `standard_or_specification`: normative text or a published technical specification. Check status/version before calling it normative.
- `research_or_public_service_guidance`: research publisher, evidence report, or public-service guidance. Scope varies by source.
- `official_platform_or_design_system`: implementation or vendor design guidance, authoritative for its own platform, not automatically for all products.
- `book_or_practitioner_publication`: method or professional advice; check edition and access.
- `practitioner_or_product_guidance`: secondary advice, tool documentation, or product-led claims.
- `commercial_or_visual_inspiration`: useful for seeing shipped patterns, not a standard or usability proof.

The source class is a navigation aid, not a quality score. Use `pass_1`, `pass_2`, `notes`, and `access_status` to evaluate each row. Commercial studies may use proprietary samples or methods; do not overgeneralize findings.

## Partial verification

Six rows remain explicitly partial:

- ID 36: official Material Design card page still returns only a JavaScript requirement in this review environment; component details remain unverified.
- ID 50: official Material Design component index still returns only a JavaScript requirement; exact button/navigation guidance remains unverified.
- ID 94: Brad Frost's official 2025-07-23 post says the second edition is a future goal and the course is an initial step; publication remains unverified as of 2026-10-14.
- ID 100: supplied Baymard URL failed; the canonical overview was checked on 2026-10-14. It describes ecommerce research and methodology, while the full findings remain Premium content.
- ID 102: Abby Covert's page confirms the complete online book is available; Google Books confirms the 2014 bibliographic year. Availability does not mean the complete text was read for this review.
- ID 109: Baymard's current checkout overview and published methodology were checked; detailed research findings remain Premium content.

Do not describe these six as fully read. Some other commercial or book references also have limited free access; see individual access notes.

Where the reference label includes an author, edition, or date, treat it as catalog metadata and check the linked source before relying on it; pass notes record known limits. The registry records its own review date separately.

For `source_origin=user_supplied`, `submitted_url` preserves each of the 124 distinct links exactly as supplied. Curated additions leave `submitted_url` blank. `url` is the reviewed or corrected canonical URL used for reference; ID 100 retains both the failed supplied URL and the canonical Baymard page identified during review.
