# Persian RTL login scenario basis

This note records why quality-30 was added. It is a fixture observation, not a model/Skill evaluation and not evidence that any Skill activated.

## Baseline observed

- The local Persian RTL login demo had 2 passing and 6 failing checks out of 8 before repair. At a 320 CSS-pixel viewport, the document measured `scrollWidth=334` against `clientWidth=305`.
- Non-empty malformed email and phone values passed the original client-side check.
- The password visibility control did not expose its toggle state through `aria-pressed`.
- The page claimed a secure/encrypted connection despite lacking a backend; the form's demo response and inactive recovery/provider/account links needed clearer boundaries.
- One RTL identity field used the same direction for email and phone values, so value-specific reading order needed an interaction check.
- The remember-me control did not persist a session, which needed to be stated rather than implied.

These failures motivated explicit checks for input contracts, state/focus/error behavior, rendered direction and overflow, and demo/backend honesty. The separate fixture repair later passed its local 10-case browser regression, but that does not validate automatic Skill activation or the new quality-30 model response.

## Evidence boundary

The source fixture and its before/after report were local to the repair task and are not included in this repository. The counts and viewport measurement above are a summary of that run; they are not independently reproducible from this repository. Do not treat this note or the repaired fixture result as a `quality-30` PASS.
