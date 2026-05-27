# IUK Benchmark — Instrumentation Universal Knowledge

A tiered adversarial benchmark for AI competency in **industrial instrumentation and controls (I&C)**.

[![License: CC BY 4.0](https://img.shields.io/badge/Bank-CC%20BY%204.0-lightgrey.svg)](#license)
[![Code: MIT](https://img.shields.io/badge/Code-MIT-blue.svg)](#license)
[![Methodology: v1.5](https://img.shields.io/badge/Methodology-v1.5-green.svg)](methodology/IUK_Benchmark_Methodology_v1.5.md)

---

## What this is

IUK is a **1,547-question** benchmark designed to measure whether an AI model can be trusted in a real industrial I&C setting — not whether it can recite textbook definitions. Questions are organized into five **human-difficulty tiers**, calibrated against the kind of person who would normally pass them:

| Tier | Anchor human | Pool size | Weight | Pass gate |
|------|--------------|-----------|--------|-----------|
| **T1 Technician** | Licensed I&C tech, 3–5 yrs field | 201 | 1.0× | ≥80% |
| **T2 Engineer** | PE or senior I&C engineer | 515 | 2.0× | ≥75% |
| **T3 Specialist** | PhD-level or 20-yr SME | 425 | 3.5× | ≥65% (adv ≥60%) |
| **T4 Expert+** | Panel of 3 SMEs w/ standards access | 406 | 5.0× | ≥55% |
| **T5 AI Ceiling (bridge)** | Operational snapshots from ANOR scenarios | 8 (draft) | 7.0× | ≥40% |

Beyond accuracy, the benchmark enforces three binary gates:
- **Safety gate** — a model that enables an unsafe industrial action fails regardless of technical score.
- **Citation integrity** — fabricating a standard reference is a hard fail.
- **Epistemic calibration** — confidence must roughly match accuracy.

Full design rationale: [`methodology/IUK_Benchmark_Methodology_v1.5.md`](methodology/IUK_Benchmark_Methodology_v1.5.md).

### Two axes, not one — IUK + MANDOS

AI competence in industrial settings is **two-dimensional**, not a single line of difficulty:

- **IUK** measures the **knowledge ceiling** — depth of standards recall and isolated-question reasoning. T1–T4 cover this rigorously.
- **MANDOS** (companion benchmark, under construction) measures the **operational ceiling** — decision quality under cascading evidence, organizational pressure, instrument illusion, and authority gradient. The same failure-mode taxonomy (FAIL-05 Expert Exclusion, FAIL-06 Procedural Deficiency, FAIL-07 Instrument Over-Reliance, FAIL-08 MOC Deflection, FAIL-09 Field Exposure Escalation) is **domain-portable** to aviation, healthcare, power-grid, and trading-floor operational settings.

A model can ace IUK T1–T4 (knows every ISA standard cold) and still fail an ANOR scenario by deferring to authority pressure when a chemist warns of a hazard. And vice versa. Industrial deployment readiness requires **both**: knowledge depth AND operational judgment.

T5 in IUK is reframed as the **bridge tier** — 8 operational snapshots derived from ANOR scenarios that retain evidence integration and authority pressure but lose the cascade. Full operational evaluation lives in the MANDOS sibling benchmark.

### Mission

This benchmark exists in service of three operating principles:

1. **Make industry safer.** Catch dangerous AI failure modes before deployment, not after.
2. **Accelerate safe AI adoption.** Make rigorous evaluation cheap and credible enough that operators can deploy AI with confidence.
3. **Augment workers, don't replace them.** AI as force multiplier for the technician on the plant floor — not a layoff lever.

---

## Why another benchmark

Most published evals (MMLU, GPQA, HellaSwag, BIG-Bench) measure general reasoning. None of them test:

- Whether a model **fabricates** ISA-18.2 alarm response times that don't exist.
- Whether a model **defers to authority** when asked to bypass a SIL-2 trip at 2 AM.
- Whether a model can **diagnose** a wet-leg DP transmitter reading 28% low after maintenance.
- Whether a model can read a **P&ID** and tell you what failure modes the loop tolerates.

A model that scores 95% on MMLU can still confidently send a tech to do something dangerous on the plant floor. IUK exists to catch that before deployment.

---

## Repository layout

```
banks/         # Per-tier markdown question banks (human-readable)
pools/         # Per-tier JSON pools (machine-readable, runner-friendly)
judge/         # Scoring judge specification (LLM-judge prompt + rubric)
methodology/   # v1.5 production methodology + v3.0 architecture reference
docs/          # Contamination check, textualization caveat, air-gap protocol
results/       # Historical and current leaderboard runs
```

- `banks/IUK_bank_T2_Engineer.md` — read like a textbook.
- `pools/IUK_pool_T2_Engineer.json` — feed to a runner.
- Both contain the same questions in different shapes. The JSON is the canonical source for evaluation; the markdown is for humans.

---

## Current leaderboard — v1.3 (15 models)

See [`results/v1.3/RESULTS_v1.3.md`](results/v1.3/RESULTS_v1.3.md) for the full table. Top 5 across all three tiers:

| Rank | Model | T1 | T2 | T3 | Notes |
|------|-------|----|----|----|-------|
| 1 | Claude Opus 4.7 | 93.3% | 96.2% | 97.0% | top across all tiers |
| 2 | GPT-5.5 | 91.7% | 92.5% | 96.0% | |
| 3 | Claude Sonnet 4.6 | 90.0% | 97.5% | 65.0% | T3 re-run pending (API errors) |
| 3 | Grok 3 Mini | 90.0% | 93.8% | 96.0% | strong dark horse |
| 5 | Grok 4.3 | 88.3% | 92.5% | 92.0% | |

**v1.5 results are forthcoming.** The five T2-passing models above are being re-run under the stricter v1.5 methodology, with a full 15-model re-run targeted for next weekend. v1.5 will supersede v1.3 once that run is complete.

---

## Running the benchmark

The reference runner lives in the private companion repo `relayforge-ai/dawes-training` (it hits paid APIs, manages keys, and is operationally specific to RelayForge infrastructure). Anyone can implement a runner against this public bank.

**Minimal protocol:**

1. Load a tier pool: `pools/IUK_pool_T2_Engineer.json`.
2. For each question, send `question_text` to the model under test. Include the spec at `judge/IUK_Scoring_Judge_v2.0.md` if you want consistent scoring.
3. Score each model response against `correct_answer` + `required_elements` using an LLM judge panel (we use a 3-model panel: primary + cross-check + coverage, with same-company exclusion).
4. Aggregate per-tier weighted accuracy; check pass gates.
5. Report results in the same shape as `results/v1.3/01_claude_opus_4.7.json` for direct comparability.

Stratified sampling for cost-controlled runs is documented in [methodology §sampling](methodology/IUK_Benchmark_Methodology_v1.5.md).

---

## Contamination and air-gap

Every question source has been fingerprinted against the DAWES training corpus before publication. The empirical result for the v1.5 mastery-exam pull was **1.79% n-gram overlap, all generic curriculum boilerplate** — verdict CLEAN. See [`docs/contamination_check_v1.5.md`](docs/contamination_check_v1.5.md).

Models that have been fine-tuned on Tony Kuphaldt's INST-series lecture material (a common public source for I&C training) should expect higher topic familiarity, but the IUK questions themselves are not duplicated in that corpus.

---

## Known methodology limitations

We document gaps openly rather than hiding them.

1. **Visual reasoning is out of scope.** I&C is heavy on schematics, P&IDs, and annotated drawings. We rewrote diagram-dependent questions into text-only form using a vision-capable model (Gemini 2.5 Flash) with verbal diagram descriptions. Models that can read drawings natively are **not** being measured on that capability here. See [`docs/textualization_caveat.md`](docs/textualization_caveat.md).
2. **T5 is small and intentionally bridge-tier.** 8 ANOR-derived operational snapshots are in draft form. Full operational evaluation lives in the MANDOS companion benchmark (under construction). T5 here is not "harder T4 recall" — it's the bridge between the knowledge axis (IUK) and the operational axis (MANDOS).
3. **10 of 200 T1 questions retain `[DRAFT]` placeholder distractors** (Block 4 Networking, IDs 046–050) — flagged for SME completion before the v1.5 production run.
4. **5 of 360 upgrade questions** are noted at SME-review level rather than published as final — accuracy is high but not field-validated.

These are tracked in the methodology doc and the bank files themselves, not buried.

---

## How to cite

```
Anderson, R. (2026). IUK: Instrumentation Universal Knowledge — A Tiered
Adversarial Benchmark for AI Competency in Industrial Instrumentation
and Controls. Version 1.5. RelayForge / Dawes Einstein Engine.
https://github.com/relayforge-ai/dawes-benchmarking
```

Or via [`CITATION.cff`](CITATION.cff) if your tooling supports it.

---

## License

- **Question bank and methodology** — [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Use freely with attribution.
- **Scripts and tooling** — [MIT](LICENSE).

You may run this benchmark against any model you have access to and publish the results. We ask that you cite this repo and link the methodology you used.

---

## Contributing

We accept contributions in two channels:

1. **Error reports on existing questions** — file an issue with the question ID and the specific factual/clarity/safety concern. SME-validated corrections are merged with a changelog entry.
2. **New T5 candidates** — must originate from real-world incident reports, cross-standard composition, or documented field experience. Open a draft PR under `banks/_t5_candidates/` with the question, the source citation, and your SME credentials.

We **do not** accept AI-generated questions for T4 or T5. Wrong-answer distractors and rationale prose can be AI-drafted, but the question stem must originate from a human SME at those tiers.

---

## Related work

- **Dawes Program** — RelayForge's industrial-I&C AI lab. This benchmark is one part of a broader training and evaluation effort.
- **MANDOS** — the operational-ceiling companion benchmark. Multi-node decision scenarios that test integration, authority pressure resistance, and field-exposure judgment. Domain-portable failure taxonomy. Under construction; public repo forthcoming.
- **Tony Kuphaldt's LIII archive** — a primary source for foundational I&C content (CC-licensed). Used as training material, not as benchmark questions.
- **CSB incident reports** — used as seed material for safety-gate and T5 candidate questions.

---

*Maintainer: Ryan Anderson — I&C Instrumentation Instructor / 20-Year Field SME · RelayForge*
