# Color decision and review

## Build from purpose

- Start from brand constraints, content, actions, hierarchy, states, themes, locale, and platform. Avoid starting from a tool-generated palette without an interface use case.
- Name tokens by role (for example, `text-primary`, `surface-raised`, `border-focus`, `status-warning`) and document foreground/background pairings. Keep brand palette names separate from semantic use.
- Check light and dark themes, hover/pressed/focus/disabled states, charts, overlays, and states that also need icons or text.

## Verify accessibility

- Read the currently applicable WCAG success criteria and conformance target from source 81 before stating a pass. Test actual rendered foreground/background pairs, including alpha compositing; a palette tool's preview is not conformance evidence.
- Include non-text UI boundaries and focus indicators where relevant. Do not use color alone to convey meaning.
- Use an approved project's existing test tool when available; record exact pair, state, theme, measured ratio, criterion, and tool/version.

## Treat psychology carefully

- Color associations vary by culture, task, and context. Keep emotional or conversion claims as hypotheses to validate with the target audience and product data.
- Palette wheels and generators are ideation tools, not research evidence. Do not copy paid-book illustrations, vendor assets, or sample palettes from the linked sources.

## Source map

- **18 Material Design 3 — Color System**: official design-system guidance; use for Material role concepts, not as a universal token mandate. [Source](https://m3.material.io/styles/color/roles)
- **19 Adobe Color** and **20 Coolors**: palette exploration tools, not normative standards. Direct access to source 20 was limited during review. [Adobe](https://color.adobe.com/create/color-wheel) · [Coolors](https://coolors.co/)
- **21–23 color books**: publisher metadata only; full contents were not reviewed. Do not imply otherwise or reproduce protected content.
- **24 Smashing Magazine** and **26 Nielsen Norman Group**: secondary/practitioner guidance; do not turn associations into universal laws. [Smashing](https://www.smashingmagazine.com/2025/08/psychology-color-ux-design-digital-products/) · [NN/g](https://www.nngroup.com/articles/color-enhance-design/)
- **25 Android Developers — Color**: official Android guidance; recheck the current page when implementing. [Source](https://developer.android.com/design/ui/mobile/guides/styles/color)
- **81 WCAG 2.2**: normative accessibility source; check exact criterion, level, and test conditions. [Source](https://www.w3.org/TR/WCAG22/)
