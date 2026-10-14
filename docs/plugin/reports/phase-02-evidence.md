# Phase 02 execution evidence

Sanitized command summaries from the isolated Codex CLI `0.144.5` runs. Each listed Codex command exited `0`, unless stated otherwise. Temporary absolute paths identify the disposable environments used and are removed after recording this report.

## Initial state

- `git ls-remote --heads origin main codex/ui-ux-plugin-phase-02` — `main` resolved to `495d29922e8e3e9782d1a95b02d15b97e9e2cc90`; phase branch was created from that commit.
- `gh pr list --state all --limit 15 ...` — PR #10 and #11 showed `MERGED` (along with earlier phases).
- `codex --version` — `codex-cli 0.144.5`.
- `codex plugin --help`, `codex plugin marketplace --help`, `codex plugin add --help`, `codex plugin list --help` — plugin management commands available. `marketplace add --help` supports a Git ref and sparse checkout.
- `codex login status` in a fresh temporary `HOME` and `CODEX_HOME` — `Not logged in`.

## Local marketplace

Environment: `HOME=/tmp/uiux-phase02-clean-user-k0lpb0_j/home`, `CODEX_HOME=/tmp/uiux-phase02-clean-user-k0lpb0_j/codex-home`, project `/tmp/uiux-phase02-clean-user-k0lpb0_j/project`.

| Command | Exit | Observed result |
|---|---:|---|
| `codex plugin marketplace add "$PWD" --json` | 0 | `marketplaceName=ui-ux-pro-marketplace`; root is the Phase 02 checkout. |
| `codex plugin marketplace list --json` | 0 | Listed the local marketplace root. |
| `codex plugin list --available --json --marketplace ui-ux-pro-marketplace` | 0 | `ui-ux-pro@ui-ux-pro-marketplace`, `AVAILABLE`, `ON_INSTALL`; source resolves to `<repo>/plugins/ui-ux-pro`. |
| `codex plugin add ui-ux-pro@ui-ux-pro-marketplace --json` | 0 | Installed under `/tmp/uiux-phase02-clean-user-k0lpb0_j/codex-home/plugins/cache/ui-ux-pro-marketplace/ui-ux-pro/local`. |
| `codex plugin list --json` | 0 | `installed=true`, `enabled=true`. |
| `codex plugin remove ... --json`; `codex plugin marketplace remove ... --json` | 0 | Plugin and marketplace removed. Follow-up lists returned empty arrays. |

## GitHub marketplace

Environment root `/tmp/uiux-phase02-github-OSEpmB`; clean `HOME`, `CODEX_HOME`, and project directories beneath it. Source was pinned to branch `codex/ui-ux-plugin-phase-02` at `8e3b6cba1d3542cee01e6d48c618700fc18c23e9`.

| Command | Exit | Observed result |
|---|---:|---|
| `codex plugin marketplace add SAeedajf/ui-ux-skill --ref codex/ui-ux-plugin-phase-02 --json` | 0 | Added `ui-ux-pro-marketplace` from `https://github.com/SAeedajf/ui-ux-skill.git`. |
| `codex plugin marketplace list --json` | 0 | Marketplace listed with `sourceType=git`. |
| `codex plugin list --available --json --marketplace ui-ux-pro-marketplace` | 0 | Plugin discovered at `<marketplace-root>/plugins/ui-ux-pro`, policy `AVAILABLE`, auth `ON_INSTALL`. |
| `codex plugin add ui-ux-pro@ui-ux-pro-marketplace --json` | 0 | Installed under `/tmp/uiux-phase02-github-OSEpmB/codex-home/plugins/cache/ui-ux-pro-marketplace/ui-ux-pro/local`. |
| `codex plugin list --json` | 0 | Plugin listed `installed=true`, `enabled=true`. |
| SHA-256 comparison of Git snapshot source and installed cache | 0 | 35 source files; zero missing files and zero hash mismatches. Codex added only `.codex-plugin/plugin.json` to the cache. |
| `codex plugin remove ... --json`; marketplace remove; follow-up lists | 0 | Installed and available plugin lists and marketplace list were empty after removal. |

Both disposable runs printed the CLI warning that PATH aliases cannot be created below `/tmp`; plugin management still completed successfully. This warning did not indicate install failure.

## Skill discovery and duplicate scenarios

`codex debug prompt-input` ran from three separate empty projects. The CLI output was inspected for both skill IDs and source paths:

| Scenario | Plugin-prefixed entries | Legacy `.agents/skills` paths | Result |
|---|---:|---:|---|
| Plugin Only | 15 | 0 | All plugin skill paths came from the installed cache. |
| Legacy Only | 0 | 15 | Synthetic copies under isolated `HOME/.agents/skills` remained discoverable. |
| Both | 15 | 15 | Both namespaces were visible; precedence and actual model selection were not tested. |

In the plugin-only GitHub scenario, the 15 names were `ui-ux-pro:<skill-id>` and every path was beneath `/tmp/uiux-phase02-github-OSEpmB/codex-home/plugins/cache/ui-ux-pro-marketplace/ui-ux-pro/local/skills/`.

## Package and repository checks

Executed on the phase branch:

- `.venv/bin/python scripts/build-plugin.py` — pass.
- `.venv/bin/python scripts/validate-plugin.py` — pass; exact source integrity and safety checks.
- `.venv/bin/python scripts/validate_marketplace.py` — pass.
- `.venv/bin/python scripts/validate_repo.py` — `15 skills, 124 sources (118 reviewed / 6 partial), 14 domains, 30 activation cases, 29 quality scenarios`.
- `.venv/bin/python -m unittest discover -s tests -v` — 40/40 pass.
- `git diff --check` — pass.
- Fixture baseline `python3 tests/fixtures/phase02-rtl-shop/test_baseline.py` — 5 expected failures before any agent repair; the fixture remains unmodified by an agent.

## CI

Draft PR #12 triggered GitHub Actions workflow `Validate repository`, run `38586399158`, for implementation commit `8e3b6cba1d3542cee01e6d48c618700fc18c23e9`. Final CI conclusion is recorded in [phase-02.md](phase-02.md).
