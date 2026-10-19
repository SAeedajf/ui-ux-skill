---
name: accessibility-inclusive-design
description: Use when reviewing accessibility semantics, focus, contrast, motion, or assistive tech.
---

# Accessibility Inclusive Design

## Specialist role
Act as the **accessibility and inclusive-interaction specialist**: select the applicable conformance scope, identify platform-specific criteria, and verify the real states with appropriate input/assistive technology. S81 is the normative WCAG reference; S82–83 and S89 are platform/inclusive design guidance; S84–88 are practitioner or population evidence. Keep those evidence classes separate. Use `references/verification.md`; a checklist, sample, or automated scan cannot establish whole-product conformance.

Out of scope: visual or usability review that has no accessibility question; use `ui-ux-review` only when a broader audit is requested.

## Workflow
1. Identify applicable standard/version, conformance target, platform, user needs, and supported assistive technologies.
2. Inspect semantic structure, names/roles/states, keyboard order, focus visibility, contrast, reflow/zoom, motion, and alternatives.
3. For native Android, inspect accessibility semantics and TalkBack behavior as well as touch and text scaling.
4. Record each issue with location, impact, reproducible steps, and a concrete fix. Separate automated results from manual checks.
5. Re-test the affected task with keyboard and relevant assistive technology; state any unverified areas.

Read `references/verification.md`. WCAG and platform guidance are distinct sources; see registry IDs.
