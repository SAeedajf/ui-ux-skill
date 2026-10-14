# Controlled Codex comparison: with and without the Skill library

## Setup

- Host: Codex CLI `0.144.5`; model selection left at `host-default` (CLI did not expose a model identity).
- Two isolated temporary project copies, each with a temporary `HOME` and `CODEX_HOME`; no global user Skills were available to either condition. The no-library copy also omitted project Skills and project guidance.
- Same implementation prompt, source fixture, focused tests, and runner settings were used in both copies. The initial fixture and focused test contents were SHA-checked as identical. Both started with 7 focused tests and 3 failures.
- Full JSONL and stderr traces: [without library](../evals/evidence/codex-runs/20261014T-controlled-without-library.jsonl) and [with library](../evals/evidence/codex-runs/20261014T-controlled-with-library.jsonl).
- Seed input hashes (both copies): `index.html` `b1e1f17eb6543fcdb8618c2044d99a738da779f4e2cf2ac25c830f02723cd47f`; `app.js` `a1a1548decaaf6ef1138c654312dd4c15ee8f4c477c27e7fd62efca3bbbb2630`; focused test `test_web_fixture.py` `17b0eb92cfe6734996521bfd56815fe115bc035147b6427e89701a8a59b7a01b`. These are the initial inputs, not post-run outputs.
- Trace hashes: without library `e81fa50c3b0d309e4a5286c6e4b48e1474d32217f5dc97c8d5675c00e21ab93a`; with library `3a71e67ca0136a093254eb0bb74cc424eef00a87dbd37fd3a12162867d3ef571`.

## Results

| Measure | Without library | With library |
|---|---|---|
| Seeded defects repaired | Distinct product names, link wording, form error/focus, visible keyboard focus | Same four seeded defects |
| Focused checks | 7/7; JavaScript syntax check passed | 7/7; full fixture suite 23/23; JavaScript syntax and repository validation passed |
| Skill behavior | No Skill files in isolated project or user home; trace contains no Skill paths | Trace records `ui-ux-review`, `persian-rtl-localization`, `accessibility-inclusive-design`, and responsive guidance being read/applied; WCAG source scope is cited |
| Outcome beyond seed | Changed the cart button to a non-interactive summary and introduced unrelated cart behavior | Preserved the apparent cart action's role/semantics; did not implement backend behavior outside the seeded defects |

The no-library run did identify the resulting static cart summary as misleading, but resolved it by removing the action. The Skill-enabled implementation retained the action and described only the requested fixes. A later, separately prompted read-only quality-25 review identified the original no-op cart, synthetic newsletter success, and counter-only cart state. This is evidence that the review prompt and task framing affect what is surfaced, and motivated the explicit outcome-tracing step in `ui-ux-review`.

## Interpretation and limits

This is one controlled pair, not a statistical estimate or proof that Skills always improve code. Both conditions repaired the seeded issues; the difference was in scope control and preservation of an expected action. No model identity was available, so this does not compare named models. It proves nothing about Claude, other hosts, screen readers, user outcomes, or Android. Browser checks of the Skills-enabled fixture were performed separately and are recorded in [fixture validation](fixture-ux-validation.md).
