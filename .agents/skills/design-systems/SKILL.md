---
name: design-systems
description: Use when changing shared tokens, components, or theming.
---

# Design Systems

## Workflow
1. Inspect current components, tokens, naming, variants, themes, platform boundaries, and consumers.
2. Confirm the repeated need and intended semantic contract before adding a token or component.
3. Prefer semantic tokens and composable variants over one-off values; preserve platform behavior where components differ.
4. Define usage, states, accessibility requirements, responsive behavior, ownership, and migration boundaries.
5. Name representative consumers on every target platform and verify that each has the repeated need before recommending shared adoption.
6. State the main compatibility or migration risks, a staged rollout/check, and exceptions; if source consumers are unavailable, label them unknown and make the recommendation provisional.

Read `references/system-principles.md`; use the registry for standards vs vendor guidance. Migrate shared components only when repeated need, evidence, and ownership are clear; avoid broad migration without them.

### Cross-platform decision output

When deciding whether web and Android should share a token or component contract, include a short **Cross-platform readiness** block:

- **Consumers:** name one real representative consumer per platform from the supplied repository or artifact. If none is available, write `not supplied` and name the consumer evidence to inspect; never invent a route or component name.
- **Shared need:** state which repeated task, meaning, or behavior is evidenced and which details remain platform-specific.
- **Risk and check:** name the main compatibility or migration risk and a staged validation/rollback check. If implementation details are unavailable, label the risk as unknown and keep the recommendation provisional.
