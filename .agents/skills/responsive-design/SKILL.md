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

Read `references/adaptation.md`. If platform-specific behavior or implementation affects the decision, load the matching adapter: [web](../../../adapters/web.md), [Android](../../../adapters/android.md), or [Compose](../../../adapters/compose.md). Otherwise keep the recommendation platform-neutral.

**Responsive output:** give a compact mode matrix of the actual constraints, resulting hierarchy/navigation/interaction changes, and states checked. Mark unrendered or unavailable modes unverified.
