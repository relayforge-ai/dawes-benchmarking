# Changelog

All notable changes to the IUK benchmark are documented here.

## [Unreleased] — preparing v1.5 run

- 5-model warm pass against v1.5 banks (Claude Opus 4.7, Sonnet 4.6, GPT-5.5, Grok 4.3, Grok 3 Mini)
- 15-model full v1.5 run targeted for 2026-05-30/31
- T5 candidate review (40 surfaced; promotion gated on SME criteria)
- T1 Block 4 Networking SME completion (10 `[DRAFT]` placeholders remain)
- INST241 mastery PDF re-source (current copy is header-corrupt; only 2 questions extracted)

## [v1.5] — 2026-05-26 — Production methodology cut

Bank refactor and methodology tightening ahead of the v1.5 model run.

### Added

- **560-bank IUK upgrade — T1 Technician** (200 Q, Blocks 1–4: Loop Math, ISA Symbols, Electronics, Networking) with AI-drafted SME-style distractors (190/200 filled).
- **560-bank IUK upgrade — T2/T3/T4** (360 Q total) with SME-reviewed common-wrong-answer distractors.
- **Mastery-exam textualization track** — 31 questions rewritten from 4 INST mastery exam PDFs with verbal diagram descriptions, allowing visual content to be tested via text-only models (with documented caveat).
- **Contamination check** — empirical n-gram shingle overlap of 4 INST mastery PDFs against DAWES `training_pairs` corpus (23,417 active rows). Result: 1.79% overlap, all generic Kuphaldt curriculum boilerplate. Verdict: CLEAN. Full report at `docs/contamination_check_v1.5.md`.
- **T5 promotion candidate pipeline** — 40 T4 candidates scored and surfaced for SME promotion review. AI authoring still not permitted at T5.
- **Tier banks** (`banks/IUK_bank_T*.md`) — per-tier consolidated markdown bundles, one file per tier, ready for human review.
- **Public methodology document** (`methodology/IUK_Benchmark_Methodology_v1.5.md`) — production methodology for this run, with explicit v1.3 → v1.5 delta table.

### Changed

- **Pool format unified.** All T1–T4 questions are now in full IUK upgrade format (`iuk_upgrade_filled` or `full_iuk`). The earlier `simple_560q` format (raw Q+A pairs with no rubric) has been retired from production pools.
- **ID namespacing.** 560-bank upgrade IDs are namespaced as `IUK-Tn-560-XXX-NNN` to prevent collision with IUK v3 IDs that share the same `IUK-Tn-DIAG-NNN` scheme.
- **T4 safety bank expanded** to absorb the former IUK v3.1 T5 safety-critical-enhanced set (130 Q) as a safety-gate seed pool. T5 is now reserved exclusively for AI Ceiling content requiring SME authoring.
- **Pool count: 1,547 Q** across T1–T4 (vs. ~1,517 in the v1.3 era, after the upgrade and dedupe passes).

### Documented limitations

- **Visual reasoning is out of scope.** Diagram-dependent questions were textualized using a vision-capable model. Models that natively read drawings are not being measured on that capability here. See `docs/textualization_caveat.md`.
- **T5 empty.** Until SME-authored questions land, "Passing — AI Ceiling" cannot be awarded.
- **10 T1 Block 4 questions retain placeholder distractors** (Net 046–050) due to API timeouts during the AI-drafting pass. Flagged for SME completion before the v1.5 production run.

## [v1.3] — 2026-05-25 — Leaderboard run

15-model evaluation against the pre-upgrade question pool. Full results retained at `results/v1.3/`.

### Run notes

- T1 Foundation Screen (60 Q, seed 42): Claude Opus 4.7 led at 93.3%; 5 models cleared the 85% threshold to advance to T2.
- T2 Competency (80 Q, seed 42): Sonnet 4.6 led at 97.5%; Opus 4.7 second at 96.2%. Sonnet/Opus inversion the only tier inversion in the run.
- T3 Certification (100 Q, seed 42): Opus 4.7 led at 97.0%. Sonnet 4.6 had 30 API errors and only answered 70/100 — flagged for re-run.

### Methodology notes

- T1 pool was the pre-upgrade 560-bank Blocks 1–4 + IUK v3 T1 foundational.
- Question format was `simple_560q` for the 560-derived questions (no rubric, no distractors, no required_elements). v1.5 fixes this gap.
- No contamination check against the DAWES training corpus was published with v1.3 (now mandatory in v1.5).
- v1.3 results remain valid as a historical baseline. v1.5 results will supersede only after the full 15-model run.

## Versions before v1.3

Older internal versions (v1.0–v1.2) used the 560-bank in its raw block format. v1.3 was the first run under the IUK v3.0 human-difficulty tier architecture. Internal IUK methodology versions (v1.0, v2.0, v2.3, v3.0) describe the architectural evolution of the question framework; the v1.x runs describe the model evaluation runs against it.
