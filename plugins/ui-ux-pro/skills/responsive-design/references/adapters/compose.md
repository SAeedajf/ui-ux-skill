# Jetpack Compose adapter

This adapter is a checklist for applying the task Skills to a Compose interface; it is not a framework tutorial. Inspect existing composables, modifiers, state holders, theme/tokens, semantics, and navigation first. Use the project's established architecture.

- Prefer semantic components and test accessibility semantics, TalkBack labels/actions, and focus traversal.
- Check text scaling, dynamic content, RTL mirroring, and mixed-direction strings in the rendered app.
- Verify adaptive behavior on phones, tablets, resizable windows, and relevant foldables; do not infer it from a phone-only preview.
- Check loading, empty, validation, error, success, and retry states, plus keyboard and touch behavior.
- Use official source IDs 42, 64, 66, 72, 82, 89, 97, and 108 as relevant. Verify current API signatures in Android documentation before code changes.
