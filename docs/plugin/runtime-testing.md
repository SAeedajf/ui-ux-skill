# Runtime testing boundaries

## What the CLI checks prove

`codex debug prompt-input` is used to inspect model-visible prompt input without making a model request. With a blank disposable project and plugin-only setup it showed 15 `ui-ux-pro:` skill entries whose paths were inside the installed plugin cache. This verifies discovery and source paths. It does not prove automatic activation, reference retrieval during a task, response quality, or code changes.

## Model-dependent checks

Positive activation, negative activation, 30-scenario activation traces, and practical repair require a logged-in Codex model session. Phase 02 isolated environments reported `Not logged in`; no credentials were copied and no personal session was used. Therefore these checks are blocked/not run. Existing evaluation harness summaries are not treated as fresh activation evidence.

The isolated RTL shop fixture is intentionally defective and includes baseline tests for unlabeled cart controls, form error focus, mobile-menu keyboard/focus recovery, responsive overflow, and contrast. Its five baseline tests failed as expected before any agent ran. Since no authenticated model was available, no agent repair was attempted and no after-state or regression result is claimed.

When model access is available, use a fresh copy of `tests/fixtures/phase02-rtl-shop`, run the baseline test first, then ask naturally for a review and repair without naming a skill. Capture the Codex trace that identifies the selected skill and installed path, review file diffs, run the fixture tests, and record screenshots or DOM evidence for responsive states. Keep the model trace, actual changed files, and test output together. Mark an individual model-dependent gate BLOCKED if the session cannot run.

## Safe project isolation

Use a separate temporary `HOME`, `CODEX_HOME`, and project directory. A temporary `CODEX_HOME` alone may still allow the CLI to discover skills under the real home directory's `.agents/skills`; the Phase 02 first probe exposed that. Isolate both variables, use an empty project, and inspect `codex debug prompt-input` before interpreting the result. Remove only the exact temporary directories created for the run.
