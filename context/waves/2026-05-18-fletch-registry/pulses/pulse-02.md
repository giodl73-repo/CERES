# Pulse 02: PITFALL use-case retention

## Goal

Make CERES PITFALL entries executable enough for the portfolio second pass by
preserving catalog/procurement, citation-validation, and downstream-reuse
boundaries in retained tests.

## Changes

- Added use-case-first actor, task, surface, likely mistake, consequence, owner,
  and test fields to `CERES-PF-02`, `CERES-PF-03`, and `CERES-PF-04`.
- Added `tests/pitfall_policy.rs` to cite all three open CERES PITFALL entries.
- Kept the existing RALLY branch correction in the validation scope because
  `CERES-PF-05` covers upstream branch drift breaking the proof path.

## Validation

```powershell
C:\Users\giodl\.cargo\bin\cargo.exe fmt --check
C:\Users\giodl\.cargo\bin\cargo.exe test --test pitfall_policy
C:\Users\giodl\.cargo\bin\cargo.exe test
C:\Users\giodl\.cargo\bin\cargo.exe run -- --catalog catalog\smithing --json
C:\Users\giodl\.cargo\bin\cargo.exe run -- --compare catalog\smithing\entries\001-backyard-propane-compact.md catalog\smithing\entries\002-induction-modular-small-repair.md --scale town --lens market --json
C:\Users\giodl\.cargo\bin\cargo.exe run --manifest-path C:\src\TRACKER\repos\standards-protocols\pitfall\Cargo.toml -q -p pitfall-cli -- C:\src\TRACKER\repos\knowledge-systems\ceres --format json
python C:\src\TRACKER\repos\standards-protocols\pitfall\tools\check_pitfall.py C:\src\TRACKER\repos\knowledge-systems\ceres
git diff --check
```
