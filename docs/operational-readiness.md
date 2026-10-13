# Operational readiness report

**Report date:** 2026-10-13
**Baseline exercised:** `c0706603544d881c51e021cb769442d823ecad50`
**Current verified scope:** Codex only; no Claude test was run during this mission. Earlier historical rows remain in `evals/run-log.csv` and were not repeated.

## Overall status

All 15 Skills are **DISCOVERABLE** in a Codex `debug prompt-input` probe using an isolated `CODEX_HOME`. The probe found all 15 Skill metadata entries in the generated model input. This does not prove automatic activation. The actual Codex model request failed with HTTP 400 because `gpt-6-luna` is unsupported by this ChatGPT account in the current CLI. The applicable task policy prohibits selecting another model, so the 30 automatic activation scenarios, 19 response-quality scenarios, and baseline comparison remain `BLOCKED`; none is marked PASS.

The Codex CLI is `0.153.4`. A normal CLI startup also rejects the existing `[agents]` table at `~/.codex/config.toml:12` (`invalid type: boolean true, expected struct AgentRoleToml`). The published config reference currently lists `agents.enabled`, `agents.default_subagent_model`, and `agents.default_subagent_reasoning_effort` as valid scalar keys. The CLI/runtime parser and published schema disagree. No persistent config edits were made. See [CLI diagnostic evidence](../evals/evidence/codex-cli-diagnostics.md).

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
| `color-systems` | **DISCOVERABLE** | BLOCKED | BLOCKED | BLOCKED | NOT_RUN | Fixture exercised manually; not attributed | **DISCOVERABLE** | [activation results](../evals/results/activation.jsonl), [quality results](../evals/results/quality.jsonl), [CLI evidence](../evals/evidence/codex-cli-diagnostics.md), [discovery manifest](../evals/evidence/codex-discovery-manifest.json) |
| `design-systems` | **DISCOVERABLE** | BLOCKED | BLOCKED | BLOCKED | NOT_RUN | Fixture exercised manually; not attributed | **DISCOVERABLE** | [activation results](../evals/results/activation.jsonl), [quality results](../evals/results/quality.jsonl), [CLI evidence](../evals/evidence/codex-cli-diagnostics.md), [discovery manifest](../evals/evidence/codex-discovery-manifest.json) |
| `ethical-persuasion` | **DISCOVERABLE** | BLOCKED | BLOCKED | BLOCKED | NOT_RUN | Fixture exercised manually; not attributed | **DISCOVERABLE** | [activation results](../evals/results/activation.jsonl), [quality results](../evals/results/quality.jsonl), [CLI evidence](../evals/evidence/codex-cli-diagnostics.md), [discovery manifest](../evals/evidence/codex-discovery-manifest.json) |
| `forms-input` | **DISCOVERABLE** | BLOCKED | BLOCKED | BLOCKED | NOT_RUN | Fixture exercised manually; not attributed | **DISCOVERABLE** | [activation results](../evals/results/activation.jsonl), [quality results](../evals/results/quality.jsonl), [CLI evidence](../evals/evidence/codex-cli-diagnostics.md), [discovery manifest](../evals/evidence/codex-discovery-manifest.json) |
| `information-architecture` | **DISCOVERABLE** | BLOCKED | BLOCKED | BLOCKED | NOT_RUN | Fixture exercised manually; not attributed | **DISCOVERABLE** | [activation results](../evals/results/activation.jsonl), [quality results](../evals/results/quality.jsonl), [CLI evidence](../evals/evidence/codex-cli-diagnostics.md), [discovery manifest](../evals/evidence/codex-discovery-manifest.json) |
| `interaction-patterns` | **DISCOVERABLE** | BLOCKED | BLOCKED | BLOCKED | NOT_RUN | Fixture exercised manually; not attributed | **DISCOVERABLE** | [activation results](../evals/results/activation.jsonl), [quality results](../evals/results/quality.jsonl), [CLI evidence](../evals/evidence/codex-cli-diagnostics.md), [discovery manifest](../evals/evidence/codex-discovery-manifest.json) |
| `interface-layout` | **DISCOVERABLE** | BLOCKED | BLOCKED | BLOCKED | NOT_RUN | Fixture exercised manually; not attributed | **DISCOVERABLE** | [activation results](../evals/results/activation.jsonl), [quality results](../evals/results/quality.jsonl), [CLI evidence](../evals/evidence/codex-cli-diagnostics.md), [discovery manifest](../evals/evidence/codex-discovery-manifest.json) |
| `journey-mapping` | **DISCOVERABLE** | BLOCKED | BLOCKED | BLOCKED | NOT_RUN | Fixture exercised manually; not attributed | **DISCOVERABLE** | [activation results](../evals/results/activation.jsonl), [quality results](../evals/results/quality.jsonl), [CLI evidence](../evals/evidence/codex-cli-diagnostics.md), [discovery manifest](../evals/evidence/codex-discovery-manifest.json) |
| `navigation-controls` | **DISCOVERABLE** | BLOCKED | BLOCKED | BLOCKED | NOT_RUN | Fixture exercised manually; not attributed | **DISCOVERABLE** | [activation results](../evals/results/activation.jsonl), [quality results](../evals/results/quality.jsonl), [CLI evidence](../evals/evidence/codex-cli-diagnostics.md), [discovery manifest](../evals/evidence/codex-discovery-manifest.json) |
| `persian-rtl-localization` | **DISCOVERABLE** | BLOCKED | BLOCKED | BLOCKED | NOT_RUN | Fixture exercised manually; not attributed | **DISCOVERABLE** | [activation results](../evals/results/activation.jsonl), [quality results](../evals/results/quality.jsonl), [CLI evidence](../evals/evidence/codex-cli-diagnostics.md), [discovery manifest](../evals/evidence/codex-discovery-manifest.json) |
| `responsive-design` | **DISCOVERABLE** | BLOCKED | BLOCKED | BLOCKED | NOT_RUN | Fixture exercised manually; not attributed | **DISCOVERABLE** | [activation results](../evals/results/activation.jsonl), [quality results](../evals/results/quality.jsonl), [CLI evidence](../evals/evidence/codex-cli-diagnostics.md), [discovery manifest](../evals/evidence/codex-discovery-manifest.json) |
| `ui-ux-review` | **DISCOVERABLE** | BLOCKED | BLOCKED | BLOCKED | NOT_RUN | Fixture exercised manually; not attributed | **DISCOVERABLE** | [activation results](../evals/results/activation.jsonl), [quality results](../evals/results/quality.jsonl), [CLI evidence](../evals/evidence/codex-cli-diagnostics.md), [discovery manifest](../evals/evidence/codex-discovery-manifest.json) |
| `ux-discovery` | **DISCOVERABLE** | BLOCKED | BLOCKED | BLOCKED | NOT_RUN | Fixture exercised manually; not attributed | **DISCOVERABLE** | [activation results](../evals/results/activation.jsonl), [quality results](../evals/results/quality.jsonl), [CLI evidence](../evals/evidence/codex-cli-diagnostics.md), [discovery manifest](../evals/evidence/codex-discovery-manifest.json) |
| `visual-hierarchy` | **DISCOVERABLE** | BLOCKED | BLOCKED | BLOCKED | NOT_RUN | Fixture exercised manually; not attributed | **DISCOVERABLE** | [activation results](../evals/results/activation.jsonl), [quality results](../evals/results/quality.jsonl), [CLI evidence](../evals/evidence/codex-cli-diagnostics.md), [discovery manifest](../evals/evidence/codex-discovery-manifest.json) |

## Results by scenario

- Activation: 30 of 30 `BLOCKED`; automatic host traces do not exist.
- Quality: 19 of 19 `BLOCKED`; no model responses were generated for scoring.
- Baseline vs. Skills-enabled: `BLOCKED`; neither side could be run as a controlled model pair.
- Web implementation fixture: static build served and browser-interacted; visual behavior at narrow viewport and screen-reader behavior are still `NEEDS_REVIEW`.
- Android fixture: no build attempted because the required JDK/SDK toolchain is absent.

Run `python3 scripts/eval_harness.py report` for the machine-readable result summary. Result records are linked to the exact baseline SHA and require evidence; the validator rejects a model-activation PASS without an automatic trace.
