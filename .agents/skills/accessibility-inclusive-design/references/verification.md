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

Do not mark a whole site conformant from this sample. Run the complete required audit scope and combine automated scans with manual keyboard and assistive-technology checks. Automated results are triage evidence only. For native Android/Compose, record device/API, TalkBack traversal and announcements, font scaling, orientation/window size, and measured touch target; Android's 48 dp recommendation is platform guidance (source ID **89**), not a WCAG criterion.
