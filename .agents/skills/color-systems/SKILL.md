---
name: color-systems
description: Use when choosing interface palettes, color roles, themes, or contrast.
---

# Color Systems

Choose colors for a product's content, tasks, brand, locale, platform, and states. A palette is a design decision to validate in context, not a universal behavior formula.

## Workflow
1. Identify the product, audience, brand constraints, supported themes, platforms, and the states the palette must communicate.
2. Inspect existing tokens and rendered combinations before proposing replacements. Prefer semantic roles for text, surfaces, borders, focus, actions, and status.
3. Check text and non-text contrast against the requested conformance target and current applicable standard. Record the tested pair, ratio, target, and any exception; do not infer conformance from a palette preview.
4. Evaluate meaning across locale and context. Treat color psychology claims as hypotheses, never universal conversion rules; pair status colors with labels or shapes where needed.
5. Review actual components in each theme, including disabled, focus, selected, error, charts, and image/text overlays. State which combinations remain untested.

Use `references/color-decision.md` for a compact review checklist and source boundaries. For a full accessibility audit beyond color contrast and non-color encoding, hand off to `accessibility-inclusive-design`.
