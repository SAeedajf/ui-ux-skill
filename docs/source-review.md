# Source review notes

The registry preserves the original 124 references, with two review-pass notes and a checkpoint after each five-reference group. The review was updated through 2026-10-14; individual rows retain their own review date. Use the linked primary page for claims; this registry is a research map, not an endorsement or substitute for reading the source.

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

`submitted_url` preserves each of the 124 distinct links exactly as supplied. `url` is the verified or corrected canonical URL used for reference; ID 100 retains both the failed supplied URL and the canonical Baymard page identified during review.
