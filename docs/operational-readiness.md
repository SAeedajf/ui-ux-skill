# Operational readiness report

**Report date:** 2026-10-14
**Baseline exercised:** `c0706603544d881c51e021cb769442d823ecad50`
**Current verified scope:** Codex only; no Claude test was run during this mission. Earlier historical rows remain in `evals/run-log.csv` and were not repeated.

## Overall status

All 15 Skills are **DISCOVERABLE** in a Codex `debug prompt-input` probe using an isolated `CODEX_HOME`. The probe found all 15 Skill metadata entries in the generated model input. This does not prove automatic activation. Earlier Codex CLI 0.153.4 requests on 2026-10-13 failed with HTTP 400 because `gpt-6-luna` was unsupported by that ChatGPT account; that was a constraint of those runs, not a repository-wide model policy. On 2026-10-14, Codex CLI 0.144.5 completed two activation prompts (one positive and one negative) and multiple quality prompts with the CLI default model. The positive trace contains explicit Skill-use messages and reads of `interface-layout` and `visual-hierarchy`; the negative trace contains no UI/UX Skill reads. Both activation results remain `NEEDS_REVIEW`. Quality scenario 24 passed a separate rubric review after five prompt/workflow iterations; scenarios 20 and 22 remain `NEEDS_REVIEW`, 21 and 23 are `NOT_RUN`, and the earlier 19 scenarios remain `BLOCKED`. Current latest state is 28 of 30 unique activation scenarios `BLOCKED` and 2 `NEEDS_REVIEW`; for quality, 19 are `BLOCKED`, 1 `PASS`, 2 `NEEDS_REVIEW`, and 2 `NOT_RUN`. Baseline comparison remains `BLOCKED`. One Codex trace also warned that Skill descriptions were shortened to fit its skills-context budget. Use any model available in the target Codex environment and record its exposed identifier, or `host-default` if it is not exposed.

The Codex CLI used for the latest run is `0.144.5`. Earlier 0.153.4 diagnostics found a normal CLI startup error in the existing `[agents]` table at `~/.codex/config.toml:12` (`invalid type: boolean true, expected struct AgentRoleToml`). No persistent config edits were made. See [CLI diagnostic evidence](../evals/evidence/codex-cli-diagnostics.md) and the new [activation traces](../evals/results/activation.jsonl).

The web fixture was built and run locally. A real keyboard focus visibility and invalid form recovery issue was repaired. Add-to-cart, invalid-email focus/error, delayed error recovery with the entered value retained, and success feedback were exercised in the in-app browser. The browser screenshots were captured in the Codex session, but the current browser interface did not provide a local screenshot export path; screenshot pixels are therefore not committed as files. Responsive visual behavior and assistive-technology behavior remain unverified. This fixture run is not attributed to any Skill because no model invocation occurred. See [before evidence](../evals/evidence/web-fixture-before.md) and [after evidence](../evals/evidence/web-fixture-after.md).

Android build/runtime is **BLOCKED**: `adb` is present, but Java, Gradle, SDK environment variables, and a known Android SDK directory are absent.

## Maturity levels

- **DOCUMENTED:** Skill and use boundaries exist in the repository.
- **DISCOVERABLE:** its metadata appeared in Codex prompt-input discovery.
- **ACTIVATION VERIFIED:** a real positive and negative Codex session trace proves expected automatic selection.
- **IMPLEMENTATION VERIFIED:** an automatically activated Skill guided code changes that pass project build and regression checks.
- **OPERATIONALLY VERIFIED:** activation, implementation, runtime, responsive/accessibility checks, and regression evidence all pass for the target workflow.

A higher level requires all evidence listed for that level. Source install/hash parity does not substitute for automatic activation.

## Per-Skill results

| Skill | Discovery | Positive activation | Negative activation | Quality | Skill-attributed code change | Practical run | Maturity | Evidence / blocker |
|---|---|---|---|---|---|---|---|---|
| `accessibility-inclusive-design` | **DISCOVERABLE** | BLOCKED | BLOCKED | BLOCKED | NOT_RUN | Fixture exercised manually; not attributed | **DISCOVERABLE** | [activation results](../evals/results/activation.jsonl), [quality results](../evals/results/quality.jsonl), [CLI evidence](../evals/evidence/codex-cli-diagnostics.md), [discovery manifest](../evals/evidence/codex-discovery-manifest.json) |
| `color-systems` | **DISCOVERABLE** | BLOCKED | BLOCKED | NEEDS_REVIEW | NOT_RUN | Fixture exercised manually; not attributed | **DISCOVERABLE** | [quality response](../evals/evidence/codex-runs/20261013T235425Z-quality-22.jsonl), [quality results](../evals/results/quality.jsonl), [discovery manifest](../evals/evidence/codex-discovery-manifest.json) |
| `design-systems` | **DISCOVERABLE** | BLOCKED | BLOCKED | NEEDS_REVIEW | NOT_RUN | Fixture exercised manually; not attributed | **DISCOVERABLE** | [quality response](../evals/evidence/codex-runs/20261013T235356Z-quality-20.jsonl), [quality results](../evals/results/quality.jsonl), [discovery manifest](../evals/evidence/codex-discovery-manifest.json) |
| `ethical-persuasion` | **DISCOVERABLE** | BLOCKED | BLOCKED | BLOCKED | NOT_RUN | Fixture exercised manually; not attributed | **DISCOVERABLE** | [activation results](../evals/results/activation.jsonl), [quality results](../evals/results/quality.jsonl), [CLI evidence](../evals/evidence/codex-cli-diagnostics.md), [discovery manifest](../evals/evidence/codex-discovery-manifest.json) |
| `forms-input` | **DISCOVERABLE** | BLOCKED | BLOCKED | BLOCKED | NOT_RUN | Fixture exercised manually; not attributed | **DISCOVERABLE** | [activation results](../evals/results/activation.jsonl), [quality results](../evals/results/quality.jsonl), [CLI evidence](../evals/evidence/codex-cli-diagnostics.md), [discovery manifest](../evals/evidence/codex-discovery-manifest.json) |
| `information-architecture` | **DISCOVERABLE** | BLOCKED | BLOCKED | BLOCKED | NOT_RUN | Fixture exercised manually; not attributed | **DISCOVERABLE** | [activation results](../evals/results/activation.jsonl), [quality results](../evals/results/quality.jsonl), [CLI evidence](../evals/evidence/codex-cli-diagnostics.md), [discovery manifest](../evals/evidence/codex-discovery-manifest.json) |
| `interaction-patterns` | **DISCOVERABLE** | BLOCKED | BLOCKED | PASS | NOT_RUN | Fixture exercised manually; not attributed | **DISCOVERABLE** | [quality-24 response](../evals/evidence/codex-runs/20261014T000621Z-quality-24.jsonl), [rubric checks](../evals/results/quality.jsonl) |
| `interface-layout` | **DISCOVERABLE** | NEEDS_REVIEW | NEEDS_REVIEW | NEEDS_REVIEW | NOT_RUN | Fixture exercised manually; not attributed | **DISCOVERABLE** | [positive trace](../evals/evidence/codex-runs/20261013T235247Z-activation-interface-layout-positive.jsonl), [negative trace](../evals/evidence/codex-runs/20261013T235306Z-activation-interface-layout-negative.jsonl), [quality response](../evals/evidence/codex-runs/20261013T235356Z-quality-20.jsonl) |
| `journey-mapping` | **DISCOVERABLE** | BLOCKED | BLOCKED | BLOCKED | NOT_RUN | Fixture exercised manually; not attributed | **DISCOVERABLE** | [activation results](../evals/results/activation.jsonl), [quality results](../evals/results/quality.jsonl), [CLI evidence](../evals/evidence/codex-cli-diagnostics.md), [discovery manifest](../evals/evidence/codex-discovery-manifest.json) |
| `navigation-controls` | **DISCOVERABLE** | BLOCKED | BLOCKED | BLOCKED | NOT_RUN | Fixture exercised manually; not attributed | **DISCOVERABLE** | [activation results](../evals/results/activation.jsonl), [quality results](../evals/results/quality.jsonl), [CLI evidence](../evals/evidence/codex-cli-diagnostics.md), [discovery manifest](../evals/evidence/codex-discovery-manifest.json) |
| `persian-rtl-localization` | **DISCOVERABLE** | BLOCKED | BLOCKED | NEEDS_REVIEW | NOT_RUN | Fixture exercised manually; not attributed | **DISCOVERABLE** | [quality response](../evals/evidence/codex-runs/20261013T235356Z-quality-20.jsonl), [quality results](../evals/results/quality.jsonl), [discovery manifest](../evals/evidence/codex-discovery-manifest.json) |
| `responsive-design` | **DISCOVERABLE** | BLOCKED | BLOCKED | NEEDS_REVIEW | NOT_RUN | Fixture exercised manually; not attributed | **DISCOVERABLE** | [quality response](../evals/evidence/codex-runs/20261013T235356Z-quality-20.jsonl), [quality results](../evals/results/quality.jsonl), [discovery manifest](../evals/evidence/codex-discovery-manifest.json) |
| `ui-ux-review` | **DISCOVERABLE** | BLOCKED | BLOCKED | BLOCKED | NOT_RUN | Fixture exercised manually; not attributed | **DISCOVERABLE** | [activation results](../evals/results/activation.jsonl), [quality results](../evals/results/quality.jsonl), [CLI evidence](../evals/evidence/codex-cli-diagnostics.md), [discovery manifest](../evals/evidence/codex-discovery-manifest.json) |
| `ux-discovery` | **DISCOVERABLE** | BLOCKED | BLOCKED | BLOCKED | NOT_RUN | Fixture exercised manually; not attributed | **DISCOVERABLE** | [activation results](../evals/results/activation.jsonl), [quality results](../evals/results/quality.jsonl), [CLI evidence](../evals/evidence/codex-cli-diagnostics.md), [discovery manifest](../evals/evidence/codex-discovery-manifest.json) |
| `visual-hierarchy` | **DISCOVERABLE** | NEEDS_REVIEW | NEEDS_REVIEW | NEEDS_REVIEW | NOT_RUN | Fixture exercised manually; not attributed | **DISCOVERABLE** | [positive trace](../evals/evidence/codex-runs/20261013T235247Z-activation-interface-layout-positive.jsonl), [negative trace](../evals/evidence/codex-runs/20261013T235306Z-activation-interface-layout-negative.jsonl), [quality response](../evals/evidence/codex-runs/20261013T235356Z-quality-20.jsonl) |

## Results by scenario

- Activation: 2 scenarios have traces awaiting independent review; 28 of 30 unique scenarios remain `BLOCKED`.
- Quality: 19 of 24 scenarios are `BLOCKED`, 1 is `PASS`, 2 are `NEEDS_REVIEW`, and 2 are `NOT_RUN`. The product-interaction case was iterated after early outputs omitted some reference limits; the final response passed the written rubric.
- Baseline vs. Skills-enabled: `BLOCKED`; neither side could be run as a controlled model pair.
- Web implementation fixture: static build served and browser-interacted; visual behavior at narrow viewport and screen-reader behavior are still `NEEDS_REVIEW`.
- Android fixture: no build attempted because the required JDK/SDK toolchain is absent.

Run `python3 scripts/eval_harness.py report` for the machine-readable result summary. Result records are linked to the exact baseline SHA and require evidence; the validator rejects a model-activation PASS without an automatic trace.

## Source and coverage audit

The submitted source-list attachment's links were compared with `docs/source-registry.csv` on 2026-10-14. After excluding 55 icon/image URL mentions (31 unique image URLs), the attachment contained 135 non-icon URL mentions and 124 unique references. The registry contains exactly 124 rows and 124 unique `submitted_url` values; the submitted and registered URL sets matched exactly (no missing or extra references). All 124 rows have a date and two review-pass fields; 118 are `reviewed` and 6 are `partially_verified`. The 14-domain coverage map still accounts for the original set of 15 Skills. Its source column maps all 124 registry IDs (with cross-domain reuse where appropriate), its evaluation column points to defined quality scenario IDs, and repository validation rejects dangling IDs or unmapped sources/scenarios. This verifies source-list parity, registry bookkeeping, and map traceability, not the correctness of every claim in inaccessible, paid, dynamic, or partially reviewed material.

## Independent skill review follow-up

Read-only reviews of all 15 Skills identified the main gap as measurable acceptance and task evidence. Updates add a criterion-level accessibility check matrix while preserving the distinction between normative web criteria and Android platform advice; locale-policy capture for Persian data; safer form recovery states; task-based evidence for hierarchy/layout; sample-denominator guidance for design-system adoption; confidence and evidence-class fields for review findings; and exact claim-level source attribution. Existing expertise boundaries and 15-Skill inventory are preserved. These documentation improvements have not yet been shown to change model behavior because the model scenarios remain blocked.

The activation validator now also binds an activation PASS to a non-empty JSONL trace, a SHA-256 of the trace reviewed, review scope, reviewer/time, and referenced event lines. This guards against a PASS row pointing to an arbitrary file, but it still relies on a human reviewer to decide whether a cited host event actually proves automatic Skill invocation. No current result has that review attestation.
