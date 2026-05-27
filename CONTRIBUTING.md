# Contributing to IUK

The IUK benchmark is open to SME-validated contributions in tightly scoped channels.

## What we accept

### 1. Error reports on existing questions

If you spot a factual error, ambiguity, safety concern, or stale standard reference, open an issue with:

- The question ID (`IUK-Tn-XXX-NNN`).
- The specific concern — what's wrong, what should it say, and which standard/source supports your correction.
- Your domain context — what role you work in (e.g. "20-year I&C tech, refining"; "PhD process control; ISA-84 working group member"; "first-year student, found the wording confusing").

We merge corrections that survive SME review. Each merged correction gets a `CHANGELOG.md` entry attributing the contribution.

### 2. New questions for T1–T3

T1, T2, and T3 questions can be drafted by anyone with relevant field experience. Open a draft PR under `banks/_draft_contributions/` with:

- The question in full IUK format (see `judge/IUK_Scoring_Judge_v2.0.md` for the schema).
- Your proposed tier classification and difficulty rationale.
- Citation to the standard or first-principles source the question tests.

We pair-review with at least one SME before promoting to the main bank.

### 3. New T4 / T5 candidates

T4 and T5 are reserved for hard-earned content. We **do not** accept AI-generated questions at these tiers. The question stem must originate from:

- A real-world incident report (CSB, OSHA, NTSB),
- Documented field experience that produced a non-obvious diagnostic or safety lesson, or
- Cross-standard composition that no single standard fully resolves.

Open a draft PR under `banks/_t5_candidates/` with:

- The question in full IUK format.
- The source citation (incident report, standards conflict, etc.).
- Why this meets the T5 promotion criteria (see methodology §5).
- Your SME credentials (so reviewers can weight the submission appropriately).

The wrong-answer distractor list and the difficulty rationale can be AI-drafted — those are mechanical. The question stem cannot.

## What we don't accept

- AI-generated question stems for T4 or T5.
- Questions sourced from copyrighted exam material (e.g. PE prep books, certification exams) without explicit permission.
- Questions that test a model's knowledge of a specific vendor product line (we test the standards and the physics, not vendor naming).
- "Gotcha" questions whose only difficulty is obscure pedantry without a real safety or operational stake.

## Disclosure expectations

If you are submitting on behalf of an organization, disclose it. If a question was developed while you were employed by a vendor, disclose it. We want to know what bias you're carrying so the SME review can compensate.

## Review timeline

We are a small team. Expect a first response within 2 weeks for issues; PRs may take longer if SME panel review is required.

## Code of conduct

This is a technical benchmark. Critique the question, not the contributor. Reproducible disagreement is welcome; ad hominem is not.

---

*Maintainer: Ryan Anderson — I&C Instrumentation Instructor / 20-Year Field SME · RelayForge*
