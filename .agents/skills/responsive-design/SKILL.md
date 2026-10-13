---
name: responsive-design
description: Use when layouts or interactions must adapt across viewports, orientation, devices, or window sizes.
---

# Responsive Design

## Workflow
1. Identify supported tasks, content priority, platform, input modes, and actual device/window constraints.
2. Inspect the current layout at narrow, intermediate, and wide sizes and relevant orientations.
3. Set breakpoints from content pressure and component behavior, not device labels alone. For Android, account for window size classes and multi-window/foldable posture where applicable.
4. Adapt hierarchy, density, navigation, and interaction to available space; avoid merely shrinking the same layout.
5. Check long text, zoom, keyboard, touch, scroll, and stateful content at each meaningful layout mode.

Read `references/adaptation.md` and the platform adapters.
