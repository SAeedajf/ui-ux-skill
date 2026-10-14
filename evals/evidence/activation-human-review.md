# Codex activation human-attestation packet

This packet prepares the independent whole-trace review required before any activation case can be marked `PASS`. It is an index, not the attestation itself. All 30 model runs are still `NEEDS_REVIEW`.

- Source commit: `5a674e961e208868795193e03e411f312d83deb6`
- Host: Codex CLI 0.144.5, host-default model
- Expected: each positive trace reads its target Skill; its paired negative trace does not read that target. A different relevant Skill may appear in a negative trace.
- Review the complete trace, not only the cited event. Confirm the prompt, automatic read event(s), final output, neighboring Skills, and whether scope/evidence stayed accurate.
- Record reviewer, UTC time, whole-trace scope, decision, SHA-256, and event-line references in `evals/results/activation.jsonl` as specified in [evaluation guidance](../evaluation.md#review-and-record-results).

| Skill | Positive trace and target read | Negative trace and observed Skill reads | Human decision |
|---|---|---|---|
| `accessibility-inclusive-design` | [trace](codex-runs/20261014T093957Z-activation-accessibility-inclusive-design-positive.jsonl#L5) — target read at L5 | [trace](codex-runs/20261014T094040Z-activation-accessibility-inclusive-design-negative.jsonl#L1) — target absent; none | [ ] Positive correct [ ] Negative correct |
| `color-systems` | [trace](codex-runs/20261014T094306Z-activation-color-systems-positive.jsonl#L5) — target read at L5 | [trace](codex-runs/20261014T094412Z-activation-color-systems-negative.jsonl#L5) — target absent; L5: interface-layout, visual-hierarchy | [ ] Positive correct [ ] Negative correct |
| `design-systems` | [trace](codex-runs/20261014T093721Z-activation-design-systems-positive.jsonl#L5) — target read at L5 | [trace](codex-runs/20261014T093831Z-activation-design-systems-negative.jsonl#L1) — target absent; none | [ ] Positive correct [ ] Negative correct |
| `ethical-persuasion` | [trace](codex-runs/20261014T094513Z-activation-ethical-persuasion-positive.jsonl#L5) — target read at L5 | [trace](codex-runs/20261014T094551Z-activation-ethical-persuasion-negative.jsonl#L5) — target absent; L5: accessibility-inclusive-design | [ ] Positive correct [ ] Negative correct |
| `forms-input` | [trace](codex-runs/20261014T094953Z-activation-forms-input-positive.jsonl#L5) — target read at L5 | [trace](codex-runs/20261014T095028Z-activation-forms-input-negative.jsonl#L5) — target absent; L5: interface-layout | [ ] Positive correct [ ] Negative correct |
| `information-architecture` | [trace](codex-runs/20261014T094833Z-activation-information-architecture-positive.jsonl#L5) — target read at L5 | [trace](codex-runs/20261014T094908Z-activation-information-architecture-negative.jsonl#L5) — target absent; L5: interface-layout | [ ] Positive correct [ ] Negative correct |
| `interaction-patterns` | [trace](codex-runs/20261014T093613Z-activation-interaction-patterns-positive.jsonl#L5) — target read at L5 | [trace](codex-runs/20261014T093700Z-activation-interaction-patterns-negative.jsonl#L1) — target absent; none | [ ] Positive correct [ ] Negative correct |
| `interface-layout` | [trace](codex-runs/20261014T093523Z-activation-interface-layout-positive.jsonl#L5) — target read at L5 | [trace](codex-runs/20261014T093551Z-activation-interface-layout-negative.jsonl#L1) — target absent; none | [ ] Positive correct [ ] Negative correct |
| `journey-mapping` | [trace](codex-runs/20261014T095046Z-activation-journey-mapping-positive.jsonl#L5) — target read at L5 | [trace](codex-runs/20261014T095107Z-activation-journey-mapping-negative.jsonl#L5) — target absent; L5: forms-input | [ ] Positive correct [ ] Negative correct |
| `navigation-controls` | [trace](codex-runs/20261014T094619Z-activation-navigation-controls-positive.jsonl#L7) — target read at L7 | [trace](codex-runs/20261014T094710Z-activation-navigation-controls-negative.jsonl#L5) — target absent; L5: forms-input | [ ] Positive correct [ ] Negative correct |
| `persian-rtl-localization` | [trace](codex-runs/20261014T094047Z-activation-persian-rtl-localization-positive.jsonl#L5) — target read at L5 | [trace](codex-runs/20261014T094142Z-activation-persian-rtl-localization-negative.jsonl#L5) — target absent; L5: visual-hierarchy | [ ] Positive correct [ ] Negative correct |
| `responsive-design` | [trace](codex-runs/20261014T093841Z-activation-responsive-design-positive.jsonl#L5) — target read at L5 | [trace](codex-runs/20261014T093943Z-activation-responsive-design-negative.jsonl#L1) — target absent; none | [ ] Positive correct [ ] Negative correct |
| `ui-ux-review` | [trace](codex-runs/20261014T094206Z-activation-ui-ux-review-positive.jsonl#L5) — target read at L5 | [trace](codex-runs/20261014T094249Z-activation-ui-ux-review-negative.jsonl#L1) — target absent; none | [ ] Positive correct [ ] Negative correct |
| `ux-discovery` | [trace](codex-runs/20261014T093450Z-activation-ux-discovery-positive.jsonl#L6) — target read at L6 | [trace](codex-runs/20261014T093517Z-activation-ux-discovery-negative.jsonl#L1) — target absent; none | [ ] Positive correct [ ] Negative correct |
| `visual-hierarchy` | [trace](codex-runs/20261014T094755Z-activation-visual-hierarchy-positive.jsonl#L5) — target read at L5 | [trace](codex-runs/20261014T094814Z-activation-visual-hierarchy-negative.jsonl#L1) — target absent; none | [ ] Positive correct [ ] Negative correct |

## SHA-256 trace hashes

### `accessibility-inclusive-design`

- Positive `20261014T093957Z-activation-accessibility-inclusive-design-positive.jsonl` — `4dec17c79a07e50d50a50547e17ac0961842e056a689ee85345fef1bf3777a33`
- Negative `20261014T094040Z-activation-accessibility-inclusive-design-negative.jsonl` — `fd173dbab35927428f8fef1bb7b70d6c2b10b206c8387a6c2a922d81f1993bcc`

### `color-systems`

- Positive `20261014T094306Z-activation-color-systems-positive.jsonl` — `8079f7bc99b01eaa6afd8e54aba82af28221e77fabf0f53069deca5167c0c0c3`
- Negative `20261014T094412Z-activation-color-systems-negative.jsonl` — `48c6f8ad0f0ecad6dc9f6d6465b01e913d53b741a73361b28dd5afb800e05b15`

### `design-systems`

- Positive `20261014T093721Z-activation-design-systems-positive.jsonl` — `e6011487e4f02430d23854b87aae624651b80cb2f7b1e25b98ce1d7ae93c31f9`
- Negative `20261014T093831Z-activation-design-systems-negative.jsonl` — `366626fc3a875f701f3bc94dde7fe506a85b688d82b685ce56530f61b766cf94`

### `ethical-persuasion`

- Positive `20261014T094513Z-activation-ethical-persuasion-positive.jsonl` — `3240766861f94571c288eed81306990c208c6f7a9778237cb9978b1f9d81c184`
- Negative `20261014T094551Z-activation-ethical-persuasion-negative.jsonl` — `a30ad40ebb4cf6ae6aee49bb2413cdbe167554a938e7db478b77f8dd28b05f20`

### `forms-input`

- Positive `20261014T094953Z-activation-forms-input-positive.jsonl` — `1cc0a80df5467b9a5f6058c7d323ab345929cc2e29069f2b0e8566d7daac13a1`
- Negative `20261014T095028Z-activation-forms-input-negative.jsonl` — `fb4aee57ccb86c0ab15e3f93813cb5ccf07da4f04014cce23bc625ff4b71e201`

### `information-architecture`

- Positive `20261014T094833Z-activation-information-architecture-positive.jsonl` — `c0cda9ea80ff7e20d1aeb3ccc0dd4eb021677664c65664096349093f06476a57`
- Negative `20261014T094908Z-activation-information-architecture-negative.jsonl` — `05db7d13fcb45c8552b1f0ef6451807b9b37c38a6b0029a7120f827fcd54f41a`

### `interaction-patterns`

- Positive `20261014T093613Z-activation-interaction-patterns-positive.jsonl` — `cf82d98a2d992316db13c2f44dbafb237d799a79c1238a8ebdae779f18968326`
- Negative `20261014T093700Z-activation-interaction-patterns-negative.jsonl` — `bee4ff3dab585314512ed5cc7eddeca982b5d7c9bfd7501be6272ea43e01a90a`

### `interface-layout`

- Positive `20261014T093523Z-activation-interface-layout-positive.jsonl` — `c03f589c67e79cbae51dc2d05e83b19d4f663154e0bc55c3d6559a86805eaba4`
- Negative `20261014T093551Z-activation-interface-layout-negative.jsonl` — `10db0f6dacb59bd7da11a5308004e97778d3ff85d8726a5dfcbf1c921fa9bc87`

### `journey-mapping`

- Positive `20261014T095046Z-activation-journey-mapping-positive.jsonl` — `af3d12d1f882738eee1045a16a37cab08459c991096724b728055d54ef6bfea2`
- Negative `20261014T095107Z-activation-journey-mapping-negative.jsonl` — `6571827a5ad0724ea34b49a31ce9ecdd08f09b82033d251e48750b873e3fa678`

### `navigation-controls`

- Positive `20261014T094619Z-activation-navigation-controls-positive.jsonl` — `08fe60091c50c5a49b42982c0d52adaa3749d56fa35e38f0e36f4903d4e9ec48`
- Negative `20261014T094710Z-activation-navigation-controls-negative.jsonl` — `5e3602d14111dcfb1b734f33c6716d16638eca0730841d25008776d0fa1e42b3`

### `persian-rtl-localization`

- Positive `20261014T094047Z-activation-persian-rtl-localization-positive.jsonl` — `ba49290b295725fcb54b0ec818cba7028b45ab3546d12314946cfa59c325a3a7`
- Negative `20261014T094142Z-activation-persian-rtl-localization-negative.jsonl` — `a765112f9a9badf9cc398f2a8ab8671eaeb366718d7b795fa23a1cc0b6d9a976`

### `responsive-design`

- Positive `20261014T093841Z-activation-responsive-design-positive.jsonl` — `2a8adc27d7bd340ed4e4566dec6676a797e7ab4e358701d620fb483e3a4d3f48`
- Negative `20261014T093943Z-activation-responsive-design-negative.jsonl` — `227f4a716c2a1f60eb89874d7b0d5f8699a2f76984bbec062d7fcaa7946e833a`

### `ui-ux-review`

- Positive `20261014T094206Z-activation-ui-ux-review-positive.jsonl` — `72004fde45af3747481213b714455e77e9f86f0902ccd42032878360361aadf8`
- Negative `20261014T094249Z-activation-ui-ux-review-negative.jsonl` — `5845115cec06b5c1cfb52575920a3ef476964be3a51587764a3901b58daebd87`

### `ux-discovery`

- Positive `20261014T093450Z-activation-ux-discovery-positive.jsonl` — `62287a4085c942f81196d4fced09e1aa9cd4cd4ae9f44b198a5f7bfd8ed412e0`
- Negative `20261014T093517Z-activation-ux-discovery-negative.jsonl` — `af44f7d299e7140fee016a510f4408b1152563fff8edd1d167f0f4806f747c6e`

### `visual-hierarchy`

- Positive `20261014T094755Z-activation-visual-hierarchy-positive.jsonl` — `c8433419bef3c0c50f1a20cf5bb8c710a9e85939181296bc4d9c05d4bac43b90`
- Negative `20261014T094814Z-activation-visual-hierarchy-negative.jsonl` — `ec445d879680c2d54db7e7fed087ef8397063037b2544914f166357dc448a9d2`

## Attestation record

- Reviewer: ____________________
- Reviewed at (UTC): ____________________
- Scope: [ ] all 30 complete traces  [ ] selected cases only (list): ____________________
- Decision: [ ] all reviewed cases pass  [ ] issues found (list scenario IDs): ____________________
- Notes / corrective actions: ____________________

A reviewer must mark a case `PASS` only after independently checking the full prompt-to-output trace. If any event is ambiguous or a neighboring Skill appears unjustified, leave that case `NEEDS_REVIEW` and record the reason.
