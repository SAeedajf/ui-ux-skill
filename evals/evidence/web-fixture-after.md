# Web fixture — after repair

- URL: `http://127.0.0.1:8008/` served from `examples/fixtures/web-store/` using Python's standard-library HTTP server.
- Browser: Codex in-app browser. After-state screenshot captured at the default 1265 × 710 viewport showing the focused email field, visible focus indicator, and validation message; another screenshot showed the preserved value after the simulated error. Both captures are visible in the task trace and are not saved as local image files.
- Keyboard/form changes: `:focus-visible` indicator restored; invalid input gets `aria-invalid=true`, describes both help and error, and receives focus; error/success message uses a polite live region; loading disables submit and restores it afterward.
- Navigation changes: menu control exposes `aria-controls`, `aria-expanded`, and a changing Persian accessible name; selecting a mobile link closes the menu. CSS defines a single-column card layout below 760px. Narrow-viewport visual execution remains unverified because this browser control exposed no viewport override.
- Browser runtime checks: add-to-cart changed the count from ۰ to ۱; empty submit announced the error and focused the email input; `qa@example.fail` displayed the recovery message and retained the value; `qa@example.test` displayed success.
- These are direct fixture changes and browser observations, not changes made under automatic Skill invocation.
