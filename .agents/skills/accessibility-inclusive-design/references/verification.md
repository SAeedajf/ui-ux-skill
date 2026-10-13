# Accessibility verification

- Confirm the target standard and version. **81** is WCAG 2.2; native Android checks should also use current Android guidance such as **82** and **89**.
- Inspect semantic names/roles/states, keyboard order and focus, contrast, non-color cues, text resizing/reflow, motion preferences, touch target behavior, errors, and status announcements.
- Combine automated checks with manual keyboard and assistive-technology use. Automated scans cannot establish full conformance or usability.
- Report evidence as `checked`, `not checked`, or `not applicable`, with tool/device/version where relevant. Do not infer screen-reader behavior from source code alone.
- Include users with varied abilities in research where possible; accessibility is not only a final compliance pass.
