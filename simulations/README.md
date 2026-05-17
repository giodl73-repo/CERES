# simulations/

Phase 4 simulation code and results, organized in three independent tiers of
increasing complexity and computational cost.

- `tier-a-comparator/` — deterministic scenario comparator; Python reference plus
  Rust/RALLY-backed CLI at the repo root
- `tier-b-system-dynamics/` — town-as-system model; inter-trade dependencies
- `tier-c-agent-based/` — targeted agent-based runs on specific questions

Tiers are independent: Tier A ships without Tier B or C existing.

Populated by Plan D (economic lens formalization + simulation code). The Rust
Tier A path keeps RALLY as a neutral run/report/evidence dependency while CERES
retains all local-production economics.
