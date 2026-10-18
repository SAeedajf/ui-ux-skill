# Accessibility verification

- Confirm the target standard and version. **81** is WCAG 2.2; native Android checks should also use current Android guidance such as **82** and **89**.
- Inspect semantic names/roles/states, keyboard order and focus, contrast, non-color cues, text resizing/reflow, motion preferences, touch target behavior, errors, and status announcements.
- Combine automated checks with manual keyboard and assistive-technology use. Automated scans cannot establish full conformance or usability.
- Report evidence as `checked`, `not checked`, or `not applicable`, with tool/device/version where relevant. Do not infer screen-reader behavior from source code alone.
- Include users with varied abilities in research where possible; accessibility is not only a final compliance pass.

## Web acceptance checks when WCAG 2.2 AA is the agreed target

Use these as a focused regression set, not as a claim that the whole site or process conforms. Check applicability and WCAG exceptions for the actual content before recording a failure or pass. Cite source ID **81** for normative requirements; the procedure below is an operational checklist.

| Area | Acceptance check | Evidence to record |
|---|---|---|
| Text contrast (1.4.3) | Rendered text meets 4.5:1, or 3:1 for large text, except where the criterion exempts it. | Foreground/background pair, ratio, state/theme, tool/version. |
| Non-text contrast (1.4.11) | Required control boundaries, states, and meaningful graphics meet 3:1 against adjacent colors, subject to criterion exceptions. | Element/state, adjacent pair, ratio, tool/version. |
| Text resize (1.4.4) | At 200% text resize, content and function remain available. | Browser, page/state, resize method, affected controls. |
| Reflow (1.4.10) | At 320 CSS px width for vertically scrolling content, information and function remain available without two-dimensional scrolling, except content whose use or meaning needs two dimensions. | Viewport/zoom, page/state, any permitted two-dimensional region. |
| Text spacing (1.4.12) | Applying the criterion's line, paragraph, letter, and word spacing overrides causes no loss of content or function. | Override values, page/state, clipping or overlap observed. |
| Keyboard and focus (2.1.1, 2.1.2, 2.4.7, 2.4.11) | Complete the core task by keyboard without a trap; focus is visible and not entirely hidden by author-created content. | Task steps, browser, focus sequence, overlays/sticky content. |
| Pointer target size (2.5.8) | In-scope targets meet 24 by 24 CSS px or a documented criterion exception. | Measured target and spacing, viewport, exception if used. |

For form regressions, inspect rendered invalid and corrected states: visible message, programmatic field association, invalid state, focus destination, and announcement behavior. Verify that stateful controls such as password visibility expose their current state. Measure text and control-boundary contrast in relevant focus/error states; source tokens alone do not prove rendered contrast.

Do not mark a whole site conformant from this sample. Run the complete required audit scope and combine automated scans with manual keyboard and assistive-technology checks. Automated results are triage evidence only. For native Android/Compose, record device/API, TalkBack traversal and announcements, font scaling, orientation/window size, and measured touch target; Android's 48 dp recommendation is platform guidance (source ID **89**), not a WCAG criterion.

## Inclusive research and source use

Use these sources to choose a practical next step, while keeping standards, methods, and aggregate evidence distinct:

| Source | Apply it to | Evidence boundary |
|---|---|---|
| [**S83** Microsoft Inclusive Design](https://inclusive.microsoft.design/) | Look for mismatches that exclude people; invite affected perspectives and use inclusive-design activities during the product lifecycle. | A design methodology, not a conformance standard or proof of accessibility. |
| [**S84** *Accessible UX Research*](https://shop.smashingmagazine.com/printed-books/accessible-ux-research/) | When planning a study, consider disabled participants from formative through summative work; make recruitment, facilitation, questions, and reporting accessible. | The registry records publisher description and contents only, not a full-book review; do not attribute undisclosed steps to the book. |
| [**S85** *Web Accessibility Cookbook*](https://www.oreilly.com/library/view/web-accessibility-cookbook/9781098145590/) | Use its public contents as an index when choosing a web topic such as focus, forms, or navigation, then verify against current semantic HTML, browser support, WCAG, and actual AT behavior. | Paid book; listing/contents only, so do not claim a recipe was reviewed. |
| [**S86** *What Every Engineer Should Know About Digital Accessibility*](https://www.taylorfrancis.com/books/mono/10.1201/9781003288060/every-engineer-know-digital-accessibility-sarah-horton-david-sloan) | Treat accessibility as a shared engineering lifecycle concern, not a final visual-polish pass. | Publisher metadata and description only; use WCAG/platform documents for testable criteria. |
| [**S87** WebAIM Million 2026](https://webaim.org/projects/million/) | Use automated issue categories to seed regression checks and compare trend questions. | February 2026 automated scan of top-ranked home pages; not a random sample, not all pages/apps, and not a prediction or conformance judgment for this product. |
| [**S88** W3C “What’s New in WCAG 2.2”](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/) | Spot new or changed criteria that may be missing from a plan, then open the exact normative WCAG 2.2 criterion, level, exceptions, and test conditions. | Informative overview; the WCAG Recommendation is normative. |

For **83–88**, label source-based reasons by ID and access level. A study plan, checklist, or aggregate report can direct inspection; only checks on the target artifact and relevant user evidence support product-specific claims.
