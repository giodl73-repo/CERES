# CERES — Local Production Atlas

Can a town of five thousand restore a working forge, a bakery that sells
wholesale, a weaving co-op? CERES tests whether the answer is yes — and
why, for whom, and at what cost.

---

## What This Is

CERES is a catalog-driven design and evaluation project for modern
artisan-production equipment: forges, ovens, looms, kilns, and related
trades. Every design in the catalog is anchored in historical functional
requirements — what a forge actually had to do across medieval Northern
Europe, Song-era China, or Tokugawa Japan — and then evaluated under
realistic modern economic conditions across a matrix of settlement
scales and organizational forms.

The output is a fundable-quality plan: per-trade playbook files
identifying which equipment designs pencil out, at which scales, under
which economic models, plus a pitch narrative that frames the evidence
for funders.

---

## Working Hypothesis

The hypothesis is testable, not assumed:

> Local artisan production in industrialized economies declined largely
> because the equipment, scale, and organizational forms inherited from
> pre-industrial times no longer penciled out against industrial
> competition. Redesign the equipment for modern contexts, pair it with
> the right organizational form, match it to the right settlement scale,
> and a meaningful share of these trades becomes viable again.

Registered falsifiers run alongside the hypothesis. If Phase 1 research
reveals that the binding constraint for a given trade is not equipment
economics but demand collapse, regulatory capture, labor-regime
dependency, or supply-chain disappearance, the analysis for that trade
pivots to document what would actually be required. A rigorous null
result — showing that equipment is not the binding constraint — is as
valid a finding as a positive one.

---

## How It Works

A five-phase pipeline, driven end-to-end on smithing first, then
replicated trade by trade.

1. **Research.** Extract functional requirements from historical forms.
   What must a forge, oven, or loom actually *do*? Temperature range,
   throughput, fuel options, skill floor. History supplies the
   requirements spec, not the design.
2. **Design catalog — the star.** Per trade, 20–40 equipment variants
   spanning real tradeoffs (size, capital cost, energy source,
   throughput, shareability, skill floor). Each variant is one markdown
   file with structured frontmatter; simulation code ingests the
   frontmatter directly.
3. **Evaluation matrix.** Every catalog entry scored across nine
   contexts: three settlement scales × three economic lenses.
4. **Simulation.** Layered — a deterministic scenario comparator (Tier
   A) runs every cell; system dynamics (Tier B) handles inter-trade
   dependencies and cascade risk; agent-based modeling (Tier C) is
   reserved for targeted questions like succession failures or
   regulatory shocks.
5. **Playbook and pitch.** Per-trade, per-scale files naming the
   winning designs with implementation sketches, plus a single
   pitch-narrative document that frames the whole project for funders.

### Economic lenses

The same catalog entry is evaluated three ways, because the same forge
is a different thing under each model:

- **Market** — *Does this pencil out as a private business?* A single
  operator owns the forge and lives off the income. Pass condition:
  payback ≤ 8 years *and* the operator earns at least a scale-appropriate
  median wage.
- **Cooperative** — *Does this work as a member-owned commons?* Users
  jointly own and fund the forge, sharing capacity and cost. Pass
  condition: break-even member count fits the feasible pool at that
  scale, with a credible governance sketch (Ostrom-principle alignment,
  monitoring, sanctions, conflict resolution).
- **Civic** — *Does this work as town infrastructure, like a library or
  fire department?* The municipality owns and funds the forge as a
  public service. Pass condition: per-household annual cost and usage
  rate sit inside thresholds benchmarked against peer civic services.

### Settlement scales

- **Village** — 500–2,000 residents
- **Town** — 2,000–15,000
- **Small city / district** — 15,000–75,000

Scale is a first-class simulation variable. A design that wins in a
small city can easily fail a village on utilization, and vice versa.

---

## Quality Bar

- **Research-paper-level estimates.** Order-of-magnitude unit economics
  with citations.
- **Every number cited.** An uncited number blocks a catalog entry from
  reaching `validated` status.
- **Conceptual designs, not procurement plans.** No supplier BOMs, no
  vendor quotes, no due-diligence-grade engineering. The catalog is for
  evaluating viability, not buying equipment.
- **Panel and editorial review.** Six permanent reviewer voices create
  deliberate friction across the core tensions of local-production
  economics (profit vs. commons, civic vs. market, practitioner vs.
  investor, historical realism vs. narrative). A separate editorial gate
  — citation, scope, numeracy — is required before any artifact is
  promoted to `validated`.

---

## Project Sections

| Section | Path | Status |
|---|---|---|
| Design specification | [`specs/`](specs/) | Active |
| Implementation plans | [`plans/`](plans/) | Active |
| Historical research | [`research/`](research/) | Phase 1 |
| Design catalog | [`catalog/`](catalog/) | Phase 2 — smithing vertical slice |
| Framework and lens math | [`corpus/`](corpus/) | Active |
| Simulation tiers | [`simulations/`](simulations/) | Tier A in progress |
| Playbook and pitch | [`playbook/`](playbook/) | Planned (Phase 5) |
| Review roles | [`.roles/`](.roles/) | Active |
| Pipeline skills | [`skills/`](skills/) | Active |
| Quality rubric | [`scoring/RUBRIC.md`](scoring/RUBRIC.md) | Active |
| Progress tracker | [`TRACKER.md`](TRACKER.md) | Active |

Canonical entry points for new readers: [`corpus/canon/THEORY.md`](corpus/canon/THEORY.md)
for the local-production framework, and [`catalog/SCHEMA.md`](catalog/SCHEMA.md)
for the catalog-entry schema.

---

## Non-Goals

- **Not** real supplier BOMs or procurement plans. Research-paper
  estimates only.
- **Not** an argument that industrial production is bad. The claim is
  about restoring optionality and local capacity, not displacing
  industrial supply.
- **Not** a political manifesto. Analytical rigor first, narrative
  framing second.
- **Not** a global-reach model. Target context is developed-economy
  settlements; other contexts can be added later.
- **Not** exhaustive historical coverage. Four to six anchor cultures;
  more added only when the framework demands it.

---

## Name

Named for **Ceres**, Roman goddess of grain, harvest, and the
nourishment of settlements.

---

## Status

Early-stage. Phase 1 (smithing vertical slice) in progress. See
[`TRACKER.md`](TRACKER.md) for current progress.

---

## Author

Giovanni Della-Libera. Started 2026-04-18.

---

## License

[MIT](LICENSE) — © 2026 Gio Della-Libera.
