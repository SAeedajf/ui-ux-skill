# Plugin phase report contract

Every plugin phase must write a durable report under `docs/plugin/reports/phase-<NN>.md` before asking the owner to review the next step.

## Required fields

```text
PHASE: <two-digit id>
TITLE: <short title>
STATUS: PASS | PARTIAL | BLOCKED | FAIL
BASE_COMMIT: <full SHA>
OUTPUT_COMMIT: <full SHA or NOT_COMMITTED>
BRANCH: <branch name>
PULL_REQUEST: <URL or NOT_CREATED>

COMPLETED:
- <verified work only>

TESTS_EXECUTED:
- <command, host/version, scope>

TEST_RESULTS:
- Executed: <observed result, evidence path>
- Planned/not executed: <reason; do not present as a result>

FILES_CHANGED:
- <repo-relative path and purpose>

ARCHITECTURE_DECISIONS:
- <decision and evidence/source>

OPEN_RISKS:
- <risk, state, next evidence>

BLOCKERS:
- <exact blocker or NONE>

LIMITATIONS:
- <host, model, account, rights, or test boundaries>

REMAINING_WORK:
- <next required work>

NEXT_PHASE_RECOMMENDATION:
- <proposal only; later phase requires owner instruction>
```

## Status rules

- **PASS:** all acceptance criteria for the phase have direct evidence and no required phase work remains.
- **PARTIAL:** useful work is complete, but at least one acceptance criterion lacks direct evidence or is explicitly unverified.
- **BLOCKED:** work cannot proceed because of an external condition; name the exact condition and evidence. Use this for a specific test/track, not as a substitute for phase status when other work completed.
- **FAIL:** an acceptance criterion was attempted and failed for a product/package defect, not because evidence was unavailable.

Creating a file, build, ZIP, or manifest does not prove installation or runtime success. Keep planned tests separate from executed tests. Cite report evidence paths relative to the repository and use full commits when source identity matters.
