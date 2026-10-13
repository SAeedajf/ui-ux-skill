# Web fixture — before repair

- URL: `http://127.0.0.1:8008/` (local-only static fixture).
- Browser: Codex in-app browser, captured at its default 1265 × 710 viewport.
- Screenshot: captured with `cua_repl` during this run and shown in the task trace; no local image export API was available, so no screenshot file is claimed here.
- Accessibility issue: global CSS suppressed every keyboard focus outline (`:focus { outline: none }`). The newsletter form had no `aria-invalid` state and its changing message had no live-region semantics.
- Runtime observation: submitting an empty email rendered an error, but focus remained on the submit button rather than returning to the field. The error text was not programmatically associated with the email input.
- Fixture included the requested hero, three product cards, responsive navigation, Persian RTL content, validation, loading, error, and success states.
