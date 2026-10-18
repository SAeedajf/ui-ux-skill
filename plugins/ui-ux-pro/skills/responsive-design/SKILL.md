---
name: responsive-design
description: Use when adapting UI to viewport, device, or window changes.
---

# Responsive Design

Out of scope: a fixed-size copy or visual tweak when supported viewport, window, orientation, or device constraints do not change the design decision.

## Workflow
1. Identify supported tasks, content priority, platform, input modes, and actual device/window constraints.
2. Inspect the current layout at narrow, intermediate, and wide sizes and relevant orientations.
3. Set breakpoints from content pressure and component behavior, not device labels alone. For Android, account for window size classes and multi-window/foldable posture where applicable.
4. Adapt hierarchy, density, navigation, and interaction to available space; avoid merely shrinking the same layout.
5. Check long text, zoom, keyboard, touch, scroll, and stateful content at each meaningful layout mode.

Read `references/adaptation.md`. If platform-specific behavior or implementation affects the decision, load only the matching adapter: [web](references/adapters/web.md), [Android](references/adapters/android.md), or [Compose](references/adapters/compose.md). Use `android.md` for native Android guidance and `compose.md` when the implementation specifically uses Jetpack Compose. Keep the recommendation platform-neutral when no platform-specific choice is needed.

**Responsive output:** give a compact mode matrix of the actual constraints, resulting hierarchy/navigation/interaction changes, and states checked. Mark unrendered or unavailable modes unverified.

For browser checks, include requested and actual viewport dimensions. At representative narrow, intermediate, and wide widths, check document overflow and confirm the primary task surface stays within the viewport. A screenshot or passing width is evidence for that state only; list untested widths and browsers.
