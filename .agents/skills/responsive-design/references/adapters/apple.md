# Apple platform layout adapter

Load only when the target includes Apple platforms. S127 is Apple's Human Interface Guidelines for layout; it is platform guidance, not a universal web breakpoint specification.

- Evaluate the actual window and available content area, including safe areas, rather than relying on a device label alone.
- Check supported size classes, window resizing, orientation, and the target app's navigation/content hierarchy at each meaningful size.
- Check Dynamic Type and long localized strings; verify that text growth does not clip controls or hide task-critical content.
- For localized interfaces, verify directionality and layout behavior with real RTL strings rather than assuming mirroring resolves localization.
- Record platform, OS/version, window dimensions, size class, text-size setting, orientation, and the rendered states actually checked.

Use the current [Apple HIG layout guide](https://developer.apple.com/design/human-interface-guidelines/layout) for implementation-specific details. These checks do not replace web responsive testing or accessibility criteria.
