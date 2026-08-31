# CERES Invariants

## CERES-INV-01: Cargo Dependencies Resolve On Current Branches

**Status:** MITIGATED

**Claim:** CERES Rust dependencies resolve from live upstream branches or pinned
revisions before Tier A validation is counted.

**Why it matters:** A stale dependency branch makes every downstream simulation,
SCENARIUM packet, and RLINE facility projection non-reproducible.

**Enforcement:** Run `cargo test` and README CLI examples after dependency or
integration changes.

**Evidence:** `Cargo.toml`, `Cargo.lock`, and `cargo test`.

## CERES-INV-02: Rust Tier A Exercises The Smithing Matrix

**Status:** MITIGATED

**Claim:** The Rust Tier A path evaluates the smithing catalog matrix and emits
stable SCENARIUM/RALLY-style run and packet evidence.

**Why it matters:** The Rust path is the current executable proof that catalog
frontmatter becomes deterministic evaluation evidence.

**Enforcement:** Run the README `--catalog catalog\smithing` command and keep
generated event/packet outputs ignored unless intentionally published.

**Evidence:** `README.md`,
`cargo run -- --catalog catalog\smithing --jsonl simulations\tier-a-comparator\results\smithing-rust-events.jsonl --packet simulations\tier-a-comparator\results\smithing-rust.packet.json`,
and `docs/scenarium-adoption.md`.

## CERES-INV-03: Comparison Packets Preserve Baseline And Candidate

**Status:** MITIGATED

**Claim:** Comparison mode keeps baseline entry, candidate entry, scale, lens,
verdict, primary metric, and evidence packet provenance distinct.

**Why it matters:** A comparison can otherwise collapse into a recommendation
without showing what was compared and under which lens.

**Enforcement:** Run the README `--compare` command and Rust comparison tests.

**Evidence:** `cargo test` and
`cargo run -- --compare catalog\smithing\entries\001-backyard-propane-compact.md catalog\smithing\entries\002-induction-modular-small-repair.md --scale town --lens market --json --packet simulations\tier-a-comparator\results\smithing-comparison.packet.json`.

## CERES-INV-04: Citation Placeholders Block Validation Claims

**Status:** PARTIAL

**Claim:** `[CITATION-NEEDED]` and source-quality gaps stay visible and prevent
catalog or pitch claims from being described as validated.

**Why it matters:** CERES contains large research and catalog surfaces where
uncited numbers or historical claims can look precise before source review is
complete.

**Enforcement:** Editorial review, catalog principles, methodology rules, and
tracker status keep placeholder debt visible.

**Evidence:** `TRACKER.md`, `corpus/canon/PRINCIPLES.md`,
`docs/METHODOLOGY.md`, and `.roles/editorial/E-1-citation-auditor.md`.

## CERES-INV-05: CERES Does Not Become A Procurement Authority

**Status:** MITIGATED

**Claim:** Catalog entries, playbooks, pitch narrative, and simulation results
remain research estimates and funder-facing evidence, not supplier BOMs,
procurement plans, municipal approvals, or investment-grade feasibility studies.

**Why it matters:** A precise-looking catalog can invite real-world procurement
decisions that CERES explicitly is not licensed to support.

**Enforcement:** README non-goals, methodology, scope roles, and pitch reviews
preserve research-paper-level and no-procurement boundaries.

**Evidence:** `README.md`, `docs/METHODOLOGY.md`,
`.roles/editorial/E-2-scope-keeper.md`, and
`reviews/R1-P6-skeptical-funder-pitch-v2.md`.

## CERES-INV-06: Customer And Consumer Boundaries Are Testable

**Status:** MITIGATED

**Claim:** CERES keeps procurement, citation-validation, and downstream-reuse boundaries in a machine-readable contract that `tests/pitfall_policy.rs` parses directly.

**Why it matters:** CERES has real customer/funder and game-system pull, so its precise-looking estimates, catalog statuses, and scenario packets need explicit negative claims.

**Enforcement:** Run `cargo test --test pitfall_policy` before closing or weakening `CERES-PF-02`, `CERES-PF-03`, or `CERES-PF-04`.

**Evidence:** `docs/pitfall-boundaries.v1.json`, `tests/pitfall_policy.rs`, `README.md`, `docs/METHODOLOGY.md`, and `docs/scenarium-adoption.md`.
