# IUK Textualization — Known Methodological Limitation

**Status:** Accepted limitation, documented openly.
**Applies to:** Any IUK benchmark question whose source material is diagram-heavy.

## The problem

A large fraction of authentic I&C (Instrumentation & Controls) assessment content is **visual**:
- Circuit schematics with component values labeled inline
- P&ID (Piping & Instrumentation Diagrams) loop drawings
- Ladder logic rungs
- Fault propagation tables
- Foundation/blueprint layouts with dimensions
- Annotated symbols (Ω, µ, °C, ±, integral/derivative operators)

A purely text-based benchmark **cannot directly test** a model's ability to read these artifacts. We have observed (v1.0 → v1.3) that even basic glyph rendering — the resistance symbol Ω, the micro prefix µ — breaks tokenization for some model APIs. Mathematical questions had to be scrubbed and rewritten plain-text in v1.3 for this reason.

## What we do

We accept this limitation explicitly. Two posture choices we considered:

1. **Drop diagram-dependent content.** Honest, but ~80% of authentic course material falls in this bucket. Coverage would collapse.
2. **Textualize diagram content via vision-capable model (Gemini 2.5 Flash), then human-verify.** Coverage preserved; verifiability preserved by SME review; testability preserved because the resulting question is text-only.

We chose (2) and explicitly mark the trade.

## What "textualized" means in practice

For every question whose source page contains a relevant diagram:

1. Gemini 2.5 Flash receives the page image and is prompted to write a bracketed **verbal description** at the start of the question text. Example:
   > `[Diagram: A parallel DC circuit with a 14.3 V generator connected through two wire resistances (0.01 ohm top, 0.03 ohm bottom) to a node where a 12 V battery is charging at 2.7 A and a load bank is drawing 12.4 A.] Given the above, calculate V_battery and V_loads.`
2. Where the diagram supplied **numerical values** needed to answer (component values, gauge readings, fault tag IDs), Gemini extracts them and embeds them in the question.
3. Where the original question asked the student to **sketch** something, Gemini rephrases it as "describe in words what you would sketch and why" — still gradable on a text-only model.
4. Where the rewrite is not possible without inventing content, the question is tagged `rescue_status: unrescuable` and a reason is recorded. These are dropped or held for human re-authoring.

Every textualized question is tagged:
- `textualized_from_diagram: true`
- `ai_textualization_confidence: high | medium | low`
- `rescue_status: rescued | native_text | unrescuable`

Native text-only questions are unaffected by this pass.

## What this is not

This methodology does **not** claim to measure visual reasoning. Models that can natively read P&IDs (e.g. GPT-5.5, Claude Opus 4.7, Gemini 2.5 Pro with vision inputs) are not being tested on that capability here. If we want to measure visual reasoning, that requires a separate vision-enabled IUK track — work for a future version.

## Why this is OK as a benchmark posture

- The textualization is **labeled at the question level**, not hidden.
- Every textualized question is **SME-reviewed before publication**.
- The benchmark scope is stated up front: "text-based reasoning over I&C assessment content."
- Visual reasoning is acknowledged as a deliberate **out-of-scope** axis.

We follow the principle (paraphrasing Dr. Alex Wissner-Gross): if you can't test something honestly, build the test that works, document the gap, and don't pretend the gap isn't there.

## Provenance

- First pass (raw OCR + IUK formatting): `extract_iuk_mastery.py` → `IUK_MASTERY_<stem>_candidates.md`
- Second pass (textualization rewrite): `extract_iuk_textualized.py` → `IUK_MASTERY_<stem>_textualized.md`
- Both raw JSON dumps are preserved for audit.
