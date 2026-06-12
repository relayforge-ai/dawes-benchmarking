# Dawes Benchmarking V2 Upgrade Plan

Created from the 2026-06-12 continuous improvement audit.

## Current verified state

- Dawes Benchmarking publishes the IUK industrial I&C benchmark banks, JSON pools, methodology, judge specification, contamination notes, and historical v1.3 results.
- The repo is a public data/methodology corpus, not the private runner. README points operational runner work to `relayforge-ai/dawes-training`.
- Pools are canonical machine-readable evaluation inputs.
- Results include per-model run JSON and aggregate leaderboard metadata.
- No GitHub Actions workflow, data validator, or V2 upgrade plan existed before this audit pass.

## Linear tracking

- Portfolio parent: not linked in this repair pass.
- Dawes Benchmarking V2 follow-up: not created in this repair pass.

## V2 scope

1. Keep public data integrity guarded by CI: JSON parse, pool counts, unique question IDs, required question keys, result counts, and leaderboard result-file links.
2. Add schema docs for pool entries, result files, benchmark manifests, judge outputs, and contamination reports.
3. Preserve the distinction between public benchmark corpus and private paid-API runner infrastructure.
4. Add release checklist coverage for methodology version, citation metadata, contamination fingerprint, SME review status, and leaderboard supersession notes.
5. Keep benchmark claims tied to exact methodology/version files and known limitations.

## Done means

- Default branch has a green data-validation gate.
- Broken JSON, mismatched counts, duplicate IDs, and dangling leaderboard links block release.
- Public docs make clear which results are current, superseded, or forthcoming.
- Runner/private-infrastructure assumptions do not leak into the public corpus.
