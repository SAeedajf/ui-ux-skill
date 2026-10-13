# Navigation and action review

## Quick checks

- Map primary, secondary, local, and utility destinations to user tasks and information hierarchy.
- Prefer visible, concise labels that match users' vocabulary; keep route labels stable across views.
- Show current location in a programmatically available way. Ensure menu open/close, focus placement/restoration, Escape, back, and selection work for the chosen platform. Mark routes and behaviors as proposed until checked in the actual product.
- Choose buttons for actions and links for navigation. Include action intent in accessible names; don't use color alone for current, selected, or destructive state.
- At narrow sizes, retain access to essential routes and actions; test menu open state, long labels, keyboard, touch target, and zoom.
- Verify routes and state changes in an actual interface; an illustrative pattern example is not proof of correct implementation.

## Handoffs

- Use `interaction-patterns` for a control's detailed state, feedback, and recovery behavior.
- Use `forms-input` for form field design, validation, and multi-field submission.
- Use `accessibility-inclusive-design` for broader semantics, keyboard, and assistive-technology review.
- Use `information-architecture` to evaluate content grouping and taxonomy before polishing a navigation menu.

## Source boundaries

This is an original synthesis; do not copy source-site prose or proprietary visuals. Check registry notes before relying on any source: design-system references are implementation guidance, ARIA APG documents interaction patterns rather than guaranteeing conformance, and commercial books/research pages have access limits.

Starting sources: [S50 Material Design 3 components](https://m3.material.io/components), [S51 Atlassian Design System](https://atlassian.design/components/), [S52 W3C ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/patterns/), [S53 James Kalbach, *Designing Web Navigation*](https://www.oreilly.com/library/view/designing-web-navigation/9780596528102/), [S54 Nielsen Norman Group hamburger-menu research](https://www.nngroup.com/articles/hamburger-menu-icon-recognizability/), [S55 Baymard ecommerce navigation research](https://baymard.com/research-articles/ecommerce-navigation-best-practice).
