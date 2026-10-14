# Responsive and adaptive behavior

- Choose breakpoints where content or interaction stops working; device labels alone are not enough.
- Start with **65–73** for web/adaptive guidance. For Android, use [S11 Android Developers Design](https://developer.android.com/design) as a hub to locate the relevant current subguide, then verify its exact window-size/resizability scope; it is platform guidance, not a web-wide standard, and APIs can change.
- Reflow and reprioritize content instead of scaling a desktop composition down. Adapt navigation, density, and interaction to the available width and input mode.
- Cover narrow, intermediate, and wide layouts, both orientations where supported, zoom/text scaling, keyboard, and long content. Include multi-window/foldable behavior when Android is in scope.
- For Android resize/orientation work, treat [**S9**](https://developer.android.com/blog/posts/goodbye-mobile-only-hello-adaptive) as dated migration context only. Use current platform guidance such as **S66** and the adaptive-app quality checklist in **S72**, then test with a resizable emulator. Verify that UI state survives window-size and orientation changes; do not copy Android-version thresholds from the 2025 post without checking current platform guidance.
- A screenshot at one width is only evidence for that state. Record the tested dimensions and untested states.
