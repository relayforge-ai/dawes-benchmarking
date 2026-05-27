# IUK Benchmark — Production Methodology v1.5

**IUK (Instrumentation Universal Knowledge) Benchmark**
**Version:** 1.5 — Production methodology for the v1.5 model run
**Date:** 2026-05-26
**Author:** Ryan Anderson — I&C Instrumentation Instructor / 20-Year Field SME
**Underlying architecture:** [IUK_Benchmark_Methodology_v3.0.md](IUK_Benchmark_Methodology_v3.0.md)
**Status:** BENCHMARK PARTITION — DO NOT USE AS TRAINING DATA

---

## What v1.5 changes vs v1.3

v1.3 was a 15-model leaderboard run that exposed real weaknesses in the question bank: most T2 questions were AI-drafted with placeholder distractors (`[DRAFT — SME review required]`), and the bank was not air-gap-fingerprinted against the training corpus. v1.5 closes those gaps before the next run.

| Gap in v1.3 | Fix in v1.5 |
|---|---|
| 560-bank questions were in `simple_560q` format (no required_elements, no common_wrong_answers, no scoring rubric) | All 560 questions upgraded to full IUK markdown with **filled** SME-grade distractors (200 T1 + 200 T2 + 125 T3 + 35 T4) |
| No contamination check between mastery exam sources and DAWES training corpus | Empirical n-gram shingle check executed (1.79% overlap, all generic curriculum boilerplate — see `docs/contamination_check_v1.5.md`) |
| Mastery exam PDFs (image-heavy) were unparseable for text-only models | Two-pass extraction: literal OCR + textualization (verbal diagram descriptions) — limitation explicitly documented in `docs/textualization_caveat.md` |
| ID collisions between IUK v3 (`IUK-T3-DIAG-012`) and 560-bank upgrades using the same scheme | 560-bank upgrade IDs namespaced as `IUK-Tn-560-XXX-NNN` |
| `simple_560q` records sat in pools next to `full_iuk` records — uneven format | Pool builder explicitly drops raw 560 records covered by an upgrade.md, single canonical format per question |
| T5 was empty with no candidate pipeline | 40 T4 candidates auto-surfaced for SME promotion review (see `banks/IUK_T5_promotion_candidates.md` in the dawes-training repo) |

---

## Current bank size

| Tier | Total | Composition |
|------|-------|-------------|
| T1 Technician | 201 | 200 filled upgrade (Blocks 1–4) + 1 mastery |
| T2 Engineer | 515 | 200 filled upgrade (Blocks 5–8) + 298 IUK v3 (T1/T2 foundational) + 17 mastery |
| T3 Specialist | 425 | 125 filled upgrade (Blocks 9–11) + 296 IUK v3 (T3 diagnostic) + 4 mastery |
| T4 Expert+ | 406 | 35 filled upgrade (Blocks 12–13) + 371 IUK v3 (T4 adversarial + T5 safety-enhanced) |
| T5 AI Ceiling | 0 | Promotion candidates surfaced; SME authoring required |
| **Total** | **1,547** | |

Versus the 1,560 originally targeted, 1,547 reflects honest dedupe (collisions between IUK v3 inter-file IDs) and the textualization unrescuable drops (3 questions). The 13-question gap is documented rather than padded.

---

## Open gaps acknowledged for v1.5

1. **T5 is empty.** 40 T4 candidates have been scored against a safety + adversarial + cross-standard rubric and surfaced for SME review. Promotion is gated on three criteria stated below. Until populated, "Passing — AI Ceiling" cannot be awarded by any model.
2. **10 of 200 T1 questions retain `[DRAFT]` placeholders** in Block 4 Networking (IDs 046–050) because of API timeouts during the AI-drafting pass. They are filled with default placeholder distractors and flagged for SME completion before the v1.5 production run.
3. **INST241 mastery PDF had a corrupt header** and yielded only 2 text-extractable questions from 9 pages (most content is image-only). Re-sourced PDF would unlock additional questions; held for follow-up.

---

## Contamination protocol

Before the v1.5 run, the four INST mastery exam PDFs used as a candidate question source were checked against the DAWES `training_pairs` table (Supabase project `zteegqfuelxqvvhurbnr`, 23,417 active rows) using normalized 6-word shingle overlap. **Verdict: CLEAN.** 5 of 279 sampled shingles matched, all generic Kuphaldt curriculum boilerplate (e.g. "algebraically manipulate this formula to solve", "consider each fault one at a"). No question-specific content overlap. Full report: `docs/contamination_check_v1.5.md`.

The air-gap fingerprint protocol (`docs/airgap_fingerprint_protocol.md`) is mandatory before every training run on any model that will be subsequently re-evaluated against this benchmark.

---

## Textualization caveat (methodology limitation)

A significant portion of authentic industrial I&C assessment content is **visual** — circuit schematics, P&IDs, ladder logic, fault tables, annotated symbols (Ω, µ, ±). Text-only models cannot directly demonstrate visual reasoning. For v1.5 we accept this gap explicitly:

- Diagram-dependent mastery exam questions were rewritten by a vision-capable model (Gemini 2.5 Flash) into text-only form with verbal diagram descriptions.
- Each textualized question is flagged in the bank with `textualized_from_diagram: true` and `ai_textualization_confidence: high|medium|low`.
- Questions Gemini could not rewrite (`rescue_status: unrescuable`) are dropped from the bank entirely (3 dropped).
- **Visual reasoning is intentionally out of scope for IUK v1.5.** A future track may evaluate model-native vision against the original PDFs; that is not what v1.5 measures.

Full rationale: `docs/textualization_caveat.md`.

---

## Pass gates (unchanged from v3.0)

| Gate | Threshold |
|------|-----------|
| T1 Technical Accuracy | ≥80% |
| T2 Technical Accuracy | ≥75% |
| T3 Technical Accuracy | ≥65% |
| T3 Adversarial Resistance | ≥60% |
| Safety Gate (T3+) | 100% (zero failures) |
| Citation Integrity | Zero fabricated citations |
| Epistemic Calibration | ≥65% |

## Grade levels

| Grade | Requirements |
|-------|-------------|
| **FAIL** | Any single pass gate not met |
| **Passing — Technician** | T1 gate passed; T2 gate not met |
| **Passing — Engineer** | T1 + T2 gates passed; T3 gate not met |
| **Passing — Specialist** | T1 + T2 + T3 + all safety/citation gates passed |
| **Passing — Expert** | All above + T4 ≥55% weighted |
| **Passing — AI Ceiling** | All above + T5 ≥40% weighted *(not awardable in v1.5 — T5 empty)* |

---

## T5 promotion criteria (when authoring resumes)

A T4 question may be promoted to T5 only if it meets **all three** of:

1. **Real-world incident provenance OR cross-standard composition** — drawn from a CSB report, OSHA accident review, or simultaneously invoking ≥2 standards from independent regulatory bodies.
2. **Multi-step reasoning where any earlier step blocks downstream credit** — a model that gets step 1 wrong cannot back into a correct final answer.
3. **Natural safety-critical or operational consequence to wrong answers** — the wrong-answer column is not a quibble but a real failure mode that would have plant-floor consequences.

The 40-candidate review document (in the private dawes-training repo) implements a scoring rubric (safety_gate +3 · adversarial +3 · long question_text +1/+2 · compound answer +1/+2 · cross-standard reference +1/+2 · multi-step diagnostic +1 · source pedigree +1) and flags candidates with combined score ≥6. SME promotion decision is human-only; AI is not authorized to author at T5.

---

## Run protocol for v1.5

1. **5-model warm pass (this weekend):** Re-run the 5 models that passed T2 in v1.3 (Claude Opus 4.7, Claude Sonnet 4.6, GPT-5.5, Grok 4.3, Grok 3 Mini) against v1.5 banks at stratified sample. Compare scores to v1.3 baseline to quantify the methodology delta.
2. **Full 15-model run (next weekend, target 2026-05-30/31):** Re-run all 15 models from v1.3 plus Gemma 3 27B fine-tuned variant (DAWES candidate) against v1.5. Publish as the new leaderboard.
3. **Air-gap fingerprint scan** of full DAWES training corpus against v1.5 banks before any new model fine-tuning is initiated.
4. **v1.3 results remain published** as historical record. v1.5 leaderboard supersedes only after the full 15-model run completes.

---

## Sampling for stratified runs

| Tier | Full pool | Sample | Sample % |
|------|-----------|--------|----------|
| T1 | 201 | 60 | 30% |
| T2 | 515 | 80 | 16% |
| T3 | 425 | 100 | 24% |
| T4 | 406 | 60 | 15% |
| T5 | 0 | 0 | — |
| **Total** | **1,547** | **300** | **19%** |

Sample sizes match v1.3 for direct comparability. Seed 42 for reproducibility.

---

## Repository layout (public)

This repo (`dawes-benchmarking`) is the public, transparent half of the IUK program. The training harness, training corpus, and fine-tuned model weights live in a separate **private** repo (`dawes-training`).

```
dawes-benchmarking/
├── banks/                 # Per-tier markdown banks (human-readable)
├── pools/                 # Per-tier JSON pools (machine-readable)
├── judge/                 # Scoring judge specification
├── methodology/           # This file + v3.0 architecture reference
├── docs/                  # Contamination check, textualization caveat, air-gap protocol
├── results/v1.3/          # Historical leaderboard (preserved)
└── results/v1.5/          # Forthcoming — current production leaderboard
```

The line between the two repos is sharp:
- **Public (this repo):** question content, methodology, judge, results.
- **Private (`dawes-training`):** training corpus, fine-tuning configs, runner scripts that hit paid APIs, training_pairs Supabase tooling.

This split exists to make the benchmark independently auditable (anyone can re-implement the runner against the public bank) while keeping the training side closed.

---

## How to cite

```
Anderson, R. (2026). IUK: Instrumentation Universal Knowledge — A Tiered
Adversarial Benchmark for AI Competency in Industrial Instrumentation
and Controls. Version 1.5. RelayForge / Dawes Einstein Engine.
https://github.com/relayforge-ai/dawes-benchmarking
```

---

*Instrumentation Universal Knowledge Benchmark*
*Methodology v1.5 — Production run prep, 2026-05-26*
*BENCHMARK PARTITION — DO NOT USE AS TRAINING DATA*
