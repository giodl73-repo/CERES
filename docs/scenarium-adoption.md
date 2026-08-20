# SCENARIUM adoption

CERES Tier A now uses SCENARIUM directly for deterministic catalog and
comparison runs, metrics, findings, comparison reports, provenance, and
versioned evidence packets. CERES retains all catalog schema, scale parameters,
verdicts, and market/cooperative/civic lens math. RALLY remains only for
beat/event JSONL mechanics.

## Removed neutral family

The adoption removes these CERES or RALLY-projected neutral surfaces:

- CERES `EvidencePacket`;
- CERES `ComparisonDeltaRow`;
- duplicated comparison subject, run IDs, status, improved-count, and delta
  projections from `EntryComparison`;
- RALLY `SimulationRun`, `SimulationMetric`, `ComparisonDelta`,
  `ComparisonReport`, `ValidationFinding`, `ValidationReport`, and
  `PacketManifest` use from CERES;
- packet conversion functions that rebuilt RALLY manifests from CERES records.

## Deletion measurement

Counting physical Rust production lines in `src/lib.rs` before `#[cfg(test)]`
plus all of `src/main.rs`:

| Measure | Added | Removed | Net |
|---|---:|---:|---:|
| CERES production Rust | 122 | 123 | -1 |

Tests, documentation, fixtures, generated files, and dependency-lock changes are
excluded. The command compares the pre-adoption `HEAD` sources with the working
sources using `git diff --no-index --numstat` after truncating `src/lib.rs` at
`#[cfg(test)]`.

The result deliberately clears the gate by only one line: the adoption is a
small simplification, not a claim that SCENARIUM eliminates CERES domain code.
The duplicated public evidence type family is gone, while the economic model
remains local.

## Role findings

| CERES lens | Decision | Finding |
|---|---|---|
| E-2 Scope Keeper | pass | Only the neutral evidence layer moved; catalog and economic policy remain CERES-owned. |
| E-3 Numeracy Checker | pass | Lens formulas and reference-result assertions are unchanged. |
| P-6 Skeptical Funder | pass_with_risk | The deletion gate passes by one production line, so claims are limited to removal of one duplicated public type family. |

## Proof

`cargo test` covers deterministic repeated comparison and packet serialization,
structured catalog failures, nine-cell execution, and unchanged economic lens
results. A real smithing comparison also emits byte-identical repeated JSON and
`scenarium.v1` packet documents.
