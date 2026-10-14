# Source review notes

The registry preserves the original 124 references, with two review-pass notes and a checkpoint after each five-reference group. Reviews were completed on 2026-10-13. Use the linked primary page for claims; this registry is a research map, not an endorsement or substitute for reading the source.

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

- ID 36: official Material Design card page; dynamic rendering limited direct extraction.
- ID 50: official Material buttons/navigation page; dynamic rendering limited direct extraction.
- ID 94: Atomic Design first edition confirmed; second-edition publication was not verified.
- ID 100: supplied Baymard URL failed; canonical page was found, while detailed research is gated.
- ID 102: Abby Covert book page/full online text identified; original publication year remains unverified.
- ID 109: Baymard checkout research overview reviewed; premium research details remain gated.

Do not describe these six as fully read. Some other commercial or book references also have limited free access; see individual access notes.

Where the reference label includes an author, edition, or date, treat it as catalog metadata and check the linked source before relying on it; pass notes record known limits. The registry records its own review date separately.

`submitted_url` preserves each of the 124 distinct links exactly as supplied. `url` is the verified or corrected canonical URL used for reference; ID 100 retains both the failed supplied URL and the canonical Baymard page identified during review.
