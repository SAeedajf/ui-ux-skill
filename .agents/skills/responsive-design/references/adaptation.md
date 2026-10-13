# Responsive and adaptive behavior

- Choose breakpoints where content or interaction stops working; device labels alone are not enough.
- Start with **65–73** for web/adaptive guidance and relevant Android source IDs in `docs/source-registry.csv`. For Android, verify current guidance on window size classes and resizable windows; implementation APIs can change.
- Reflow and reprioritize content instead of scaling a desktop composition down. Adapt navigation, density, and interaction to the available width and input mode.
- Cover narrow, intermediate, and wide layouts, both orientations where supported, zoom/text scaling, keyboard, and long content. Include multi-window/foldable behavior when Android is in scope.
- A screenshot at one width is only evidence for that state. Record the tested dimensions and untested states.
