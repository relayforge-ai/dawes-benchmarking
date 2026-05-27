# IUK Benchmark v1.3 — Results
**IUK (Instrumentation Universal Knowledge) | IC Benchmark v2.1**
**Lead Evaluator:** Ryan Anderson — I&C Instrumentation Instructor / 20-Year Field SME
**Run Date:** 2026-05-25
**Methodology:** `benchmark/methodology/IUK_Benchmark_Methodology_v3.0.md`

> **v1.4 Note:** T1 question pool is being updated as part of the IUK v3.0 restructure.
> T1 will draw from the verified 200-question graduation exam anchor + converted 560 Q bank Blocks 1–4.
> T2 will be re-run under v1.4 to reflect the new pool. Current v1.3 T1 results are valid and retained.
> T2 results from v1.3 should be treated as preliminary pending the v1.4 re-run.
> Sonnet 4.6 T3 result requires a re-run (30 API errors — only 70/100 answered).

---

## T1 — Foundation Screen (60Q · Seed 42 · Blocks 1–4)

All 15 models complete.

| Rank | Model | Provider | Score | Correct | T2 Eligible | Notes |
|------|-------|----------|-------|---------|-------------|-------|
| 1 | Claude Opus 4.7 | OpenRouter | **93.3%** | 56/60 | ✅ | |
| 2 | GPT-5.5 | OpenRouter | **91.7%** | 55/60 | ✅ | |
| 3 | Claude Sonnet 4.6 | OpenRouter | **90.0%** | 54/60 | ✅ | |
| 3 | Grok 3 Mini | xAI direct | **90.0%** | 54/60 | ✅ | |
| 5 | Grok 4.3 | OpenRouter | **88.3%** | 53/60 | ✅ | |
| 6 | Llama 4 Maverick | OpenRouter | 83.3% | 50/60 | — | |
| 6 | Kimi K2.6 | Fireworks | 83.3% | 50/60 | — | |
| 8 | Devstral 2 (2512) | OpenRouter | 81.7% | 49/60 | — | |
| 8 | Mistral Medium 3.5 | OpenRouter | 81.7% | 49/60 | — | |
| 10 | Qwen 2.5 32B | Ollama/Io | 80.0% | 48/60 | — | |
| 11 | Gemma 3 27B | Ollama/DAWES | 76.7% | 46/60 | — | |
| 12 | Llama 4 Scout | OpenRouter | 70.0% | 42/60 | — | |
| 13 | Codestral (2508) | OpenRouter | 66.7% | 40/60 | — | |
| 14 | Gemma 3 12B | OpenRouter | 53.3% | 32/60 | — | |
| 15 | Gemini 2.5 Pro | OpenRouter | 21.7% | 13/60 | — | ⚠ Under review |

**T2 eligible threshold:** ≥85% (51/60)

---

## T1 — Foundation Expansion (120Q · Seed 42)

Top 5 qualifiers only.

| Model | Score | Correct | Gate Pass |
|-------|-------|---------|-----------|
| Claude Opus 4.7 | 90.8% | 109/120 | ✅ |
| Claude Sonnet 4.6 | 90.8% | 109/120 | ✅ |
| GPT-5.5 | 90.8% | 109/120 | ✅ |
| Grok 4.3 | 90.8% | 109/120 | ✅ |
| Grok 3 Mini | 88.3% | 106/120 | ✅ |

---

## T2 — Competency (80Q · Seed 42 · Blocks 5–10)

5 models ran. **Preliminary — v1.4 re-run planned with updated question pool.**

| Rank | Model | Score | Correct | API Errors | Notes |
|------|-------|-------|---------|------------|-------|
| 1 | Claude Sonnet 4.6 | **97.5%** | 78/80 | 0 | |
| 2 | Claude Opus 4.7 | **96.2%** | 77/80 | 0 | |
| 3 | Grok 3 Mini | **93.8%** | 75/80 | 0 | |
| 4 | GPT-5.5 | **92.5%** | 74/80 | 4 | |
| 4 | Grok 4.3 | **92.5%** | 74/80 | 1 | |

Notable: Sonnet 4.6 leads Opus 4.7 at T2 — the only tier inversion in the run.

---

## T3 — Certification (100Q · Seed 42 · Blocks 9–10)

5 models ran. Sonnet 4.6 requires a re-run (30 API errors, only 70/100 answered).

| Rank | Model | Score | Correct | Answered | Notes |
|------|-------|-------|---------|----------|-------|
| 1 | Claude Opus 4.7 | **97.0%** | 97/100 | 100/100 | |
| 2 | GPT-5.5 | **96.0%** | 96/100 | 97/100 | 3 API errors |
| 2 | Grok 3 Mini | **96.0%** | 96/100 | 100/100 | |
| 4 | Grok 4.3 | **92.0%** | 92/100 | 100/100 | |
| 5 | Claude Sonnet 4.6 | 65.0% | 65/100 | 70/100 | ⚠ 30 API errors — re-run required |

Notable: Opus 4.7 holds the top position overall across all three tiers.
Grok 3 Mini surprises — ties GPT-5.5 at T3 and outperforms at T1.

---

## Score Thresholds

| Score | Designation |
|-------|-------------|
| ≥95% | Expert — fine-tuning candidate |
| 85–94% | Strong competency |
| 70–84% | Supervised assistant |
| <70% | Insufficient foundation |

---

## Judge Panel

| Role | Model | Company |
|------|-------|---------|
| Primary | Claude Opus 4.7 / Grok 4.3 (substituted for Opus self-evaluation) | Anthropic / xAI |
| Cross-check | GPT-5.5 | OpenAI |
| Coverage | Gemini 2.5 Pro | Google |

*Grok 4.3 substituted as primary judge when evaluating Claude Opus 4.7 (same-company exclusion).*

---

## Judge Divergence Flags

| Model | Questions Flagged | Resolution |
|-------|------------------|------------|
| Claude Sonnet 4.6 (T3) | 1 | Manual review pending |
| All others | 0 | — |

---

## Methodology Notes

- Temperature: 0 (deterministic gate run)
- Seed: 42 (same draw for all models)
- Judge: 3-panel adversarial (primary, cross-check, coverage — never same company as candidate)
- Correct threshold: ≥7/10 per question (5-dimension rubric)
- Cold context: no conversation history between questions
- SOP: Dawes Einstein Engine Lab SOP v1
- Hardware: DAWES RTX 3090 24GB / RTX 4060 Ti 16GB

**Reporting note:** T1 is a recall/definition screen only. T3 (Certification) results do not imply production readiness — the air-gap exam is the certification gate.

---

## Pending Actions

- [ ] Sonnet 4.6 T3 re-run (30 API errors — contact provider, retry with higher timeout)
- [ ] Gemini 2.5 Pro T1 manual review (13/60 — possible prompt format mismatch)
- [ ] v1.4 re-run: updated T1 pool (200Q graduation exam anchor + 560 Blocks 1–4)
- [ ] v1.4 re-run: T2 with updated Competency pool
- [ ] IRR computation once all models complete (`scripts/compute_irr.py`)

---

*RelayForge, Inc. · Anacortes, WA · Last updated: 2026-05-26*
