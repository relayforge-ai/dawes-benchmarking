# INST Mastery PDF Contamination Check — Report

**Date:** 2026-05-26
**Target:** 4 INST mastery exam PDFs in `/home/ryan-sheldon/dawes/mastery_exams/`
**Reference corpus:** `training_pairs` table (Supabase project `zteegqfuelxqvvhurbnr`), 25,582 rows total, 23,417 active (cleanup_status ≠ 'dropped').

## Method

1. **Extracted** PDF text via `pdfplumber` with `pikepdf` repair fallback.
2. **Normalized** to lowercase, alphanumeric+apostrophe only, collapsed whitespace.
3. **Shingled** into 6-word phrases (excluding shingles dominated by ≤2-char math tokens and 5 explicit boilerplate fragments).
4. **Sampled** 75 random shingles per PDF (seed=42) for the contamination probe.
5. **Probed corpus** server-side: materialized the normalized concatenation of all active `question_text || ' ' || answer` (22 MB) and used `position(shingle in corpus)` for each probe shingle.

## Results

| PDF | Status | Shingles probed | Hits | % overlap |
|---|---|---|---|---|
| `INST200_x1_mastery_v01` | text OK (5,911 chars) | 64 | 1 | 1.6% |
| `INST200_x1_mastery_v02` | text OK (5,900 chars) | 72 | 3 | 4.2% |
| `INST241_x2_mastery_latest` | header corrupt; recovered via `pikepdf` (2,203 chars — partially image-based) | 75 | 0 | **0.0%** |
| `INST251_x2_mastery` | truncated trailer; recovered via `pikepdf` (4,635 chars) | 68 | 1 | 1.5% |
| **Total** | | **279** | **5** | **1.79%** |

## What the 5 hits actually are

All are **generic Kuphaldt-curriculum boilerplate**, not question-specific content:

| Phrase | Why it matched |
|---|---|
| `algebraically manipulate this formula to solve` | Standard formula-rearrangement question stem used across the INST200/240 series. |
| `wires connecting components together to form` | Standard circuit-sketching task intro. |
| `consider each fault one at a` | Standard fault-analysis instruction (boilerplate). |
| `this circuit to provide an output` | Generic phrasing. |
| `3 course specific mastery question determine` | Mastery-exam **section header** appearing in every mastery PDF — the literal label of the "course-specific" question slot, not the question itself. |

Zero of the 5 hits correspond to actual problem statements, distractors, or answer content from the mastery exams.

## Filename-level cross-check (parallel signal)

Looking at `source_file` matches in `training_pairs`:

| Token | Distinct source files | Total rows |
|---|---|---|
| `INST200` | 3 (sec1, sec1_instructor, Answers) | 1,573 |
| `INST241` | 4 (sec1–sec4) | 3,466 |
| `INST251` | 0 | 0 |

The mastery exam PDFs themselves (`*_x1_mastery_*.pdf`, `*_x2_mastery_*.pdf`) do **not** appear in the corpus by filename. Section/lecture PDFs from the same INST courses do — those share instrument tags like `TY-205a`, `XD_Scale`, `INST250 Review` with the mastery exams, but use different question wording.

## Verdict

**CLEAN** — all 4 mastery exams are safe to use as benchmark question sources.

Caveats:
- `INST241_x2_mastery_latest.pdf` was corrupt (no PDF header) but recoverable. Only 2,203 chars of text extracted from 9 pages — most content is image-based (circuit/loop diagrams). Parsing into IUK questions will require OCR or manual transcription for the diagram-heavy questions.
- `INST251_x2_mastery.pdf` was truncated but recovered cleanly.
- The 5 hits ARE worth noting in any methodology write-up as expected curriculum-style overlap, not evidence of contamination.

## Next steps (per the agreed (a)→(b)→(c) plan)

- (b) Parse these PDFs into IUK question candidates using `extract_mastery_pdfs.py` (already set up to handle this format). Output to `mastery_gate/master_qa_bank.json` keyed by course.
- (c) After review, promote the hardest INST241/INST251 questions as T4→T5 candidates if they exceed the existing T4 difficulty bar.

## Artifacts

- `extracted/*.txt` — raw text dumps per PDF
- `phrases.json` — 20-word ILIKE anchor phrases (initial probe)
- `shingles.json` — 1,920 normalized 6-word shingles across all 4 PDFs
- `extract_pdfs.py`, `phrase_anchors.py`, `build_shingles.py` — scripts
