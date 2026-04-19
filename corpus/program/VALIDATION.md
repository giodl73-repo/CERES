---
title: CERES Validation Framework
version: "1.0"
created: 2026-04-18
spec: specs/2026-04-18-ceres-design.md §8
companion_editorial: skills/ceres-editorial/SKILL.md
status: skeleton  # Plan D fleshes out simulation-output validation procedures
---

# CERES Validation Framework

This document defines how CERES ensures its simulation outputs are trustworthy.
Two distinct validation streams run in parallel: **catalog-entry validation**
(editorial gates on the structured data that feeds the simulation) and
**sim-output validation** (sanity-checking the 9-cell `results:` block each
catalog entry produces after Tier A runs).

**Division of labor:**

- This document — philosophy, editorial gates, sim-output validation approach,
  known-parallel anchors (stubbed), and failure-flagging protocol. Authoritative
  on the structure and rules; Plan D populates the specific test cases and
  procedures.
- `skills/ceres-editorial/SKILL.md` — executable editorial protocol for
  E-1/E-2/E-3 lenses. Cross-reference rather than duplicate here.
- `simulations/tier-a-comparator/VALIDATION.md` — Plan D landing zone for
  specific Tier A test procedures, regression cases, and known-parallel
  comparisons. That file does not yet exist; Plan D creates it.
- `corpus/program/ECONOMIC-LENSES.md` — the lens formulas being validated.
- `corpus/program/SCALES.md` — the threshold values the lenses test against.

---

## 1. Validation Philosophy

**Sim outputs must be sanity-checkable against known real-world parallels.
Uncheckable outputs are untrustworthy.**

CERES produces order-of-magnitude economic estimates, not engineering
certificates. The appropriate standard is not precision but *defensibility*: can
a skeptical reader with domain knowledge look at the output and confirm it is in
the right neighborhood? If no such check is possible — because no real-world
parallel exists, because inputs are unanchored, or because the output is not
comparable to anything observable — then the result should not be published as a
finding. It should be flagged as unverifiable and held.

Three practical corollaries follow from this philosophy:

1. **Every sim_params number cites a source.** A catalog entry whose `sim_params`
   block contains uncited numbers cannot produce a trustworthy result, no matter
   how internally consistent the math is. Uncited numbers block `status: validated`
   at the editorial gate (see Section 2).

2. **Internal consistency is necessary but not sufficient.** A simulation that
   runs without errors and produces internally consistent numbers can still be
   wrong if its inputs were wrong. Internal consistency checks (E-3, Section 2)
   catch arithmetic errors; real-world comparison (Section 3) catches structural
   errors.

3. **Failure is a valid output.** A sim result showing `fail` under all nine
   cells is as trustworthy — and as valuable — as one showing `win`, provided
   the validation chain holds. Suppressing or discounting fail results undermines
   the project's stated commitment to null findings (spec §11.2).

---

## 2. Catalog-Entry Validation — Editorial Gates

Before simulation output can be trusted, the catalog entry feeding the simulation
must pass three editorial gates. These gates are formalized in
`skills/ceres-editorial/SKILL.md` and summarized here.

### Gate Structure

Editorial fires on **promotion**: `draft` → `reviewed` (panel), then
`reviewed` → `validated` (editorial). Simulation results in a catalog entry
with `status: draft` or `status: reviewed` are preliminary and must be clearly
labeled as such. Only entries at `status: validated` contribute to playbook
conclusions or pitch evidence.

### E-1 — Citation Auditor

Verifies that every numeric claim in `economics:`, `sim_params:`, and
`operations_reality:` cites a source in the entry's `sources:` block.

**Blocking conditions (P1):**

- Three or more fields with uncited numeric claims.
- A `sim_params.cost_mean` that cannot be traced to any listed source.
- FX conversion not anchored to `corpus/program/CURRENCIES.md`.

**Promotion impact:** Any P1 finding blocks promotion to `validated`.

### E-2 — Scope Keeper

Verifies that the catalog entry stays within its declared trade, scale, and lens
scope; that it does not duplicate another entry; and that it does not violate
CERES non-goals (spec §13).

**Blocking conditions (P1):**

- Entry claims a different trade than its directory path.
- `lens_fit.cooperative` or `lens_fit.civic` set to `good` without a
  corresponding `lens_context` block (schema violation).
- `market_price_per_unit` absent when `lens_fit.market` is `good` or `marginal`.

**Promotion impact:** Any P1 schema violation blocks promotion.

### E-3 — Numeracy Checker

Cross-checks the internal arithmetic of the catalog entry and flags
order-of-magnitude errors before simulation runs.

**Standard cross-checks run by E-3:**

| Check | Rule |
|-------|------|
| Throughput ↔ labor | `labor_hours_per_unit` × `throughput_units_equiv_per_year` must not exceed operator FTE implied by `operators_concurrent` |
| Payback ↔ implied revenue | Back-compute payback from `cost_mean`, `annual_maintenance`, `annual_consumables`, `market_price_per_unit`, and `throughput_units_equiv_per_year`; compare to any stated payback claim in prose |
| Downtime consistency | `downtime_fraction` × `max_active_hours_per_week` × 52 must exceed `first_year_failures` cumulative downtime estimate |
| Order-of-magnitude sanity | Capital cost range (`low`:`high`) must be within 5× of comparable equipment in sources; wider spreads require explicit justification |
| Currency normalization | `economics.currency` must be a code listed in `corpus/program/CURRENCIES.md`; if non-USD, FX conversion to project base currency must be shown |

**Blocking conditions (P1):** Order-of-magnitude error (>10× deviation from
cited parallel without justification) or internal arithmetic contradiction.

**Promotion impact:** Any P1 finding blocks promotion. P2 findings (should-fix)
are tracked but do not block.

### Promotion Decision Rule

An entry is cleared for `status: validated` only when all three lenses return
`pass` or `fix-and-recheck-resolved`. Any single `block` holds the entry. The
full protocol — including output file naming and consolidated summary format —
is in `skills/ceres-editorial/SKILL.md`.

---

## 3. Sim-Output Validation — Tier A

Once a catalog entry reaches `status: validated`, Tier A simulation runs and
populates the 9-cell `results:` block. Those results must themselves be
validated before being cited as findings.

Tier A output validation proceeds on three axes for every populated cell:

### 3a. Real-World Parallel Comparison

For each entry, identify whether a known real-world operation is comparable
(same trade, similar scale, similar organizational form). If one exists:

- Extract the parallel's key metric (e.g., payback years for a MARKET cell,
  break-even member count for a COOPERATIVE cell, per-household annual cost for
  a CIVIC cell).
- Compare to the sim output. Acceptable tolerance: within 2× for a strong
  parallel (same country, same decade), within 5× for a weak parallel (different
  country or era, adjusted for costs).
- Document the comparison in `simulations/tier-a-comparator/VALIDATION.md`
  (Plan D populates that file with specific cases; Section 4 of this document
  lists the anchors to use).

If no real-world parallel exists for a given cell, that cell is flagged
`unverified-parallel` in the validation record. It may still be published but
must carry that label in any playbook or pitch citation.

### 3b. Internal Consistency (E-3 Cross-Checks)

After sim runs, re-run the E-3 cross-checks from Section 2 against the
*populated* results block:

- `win` verdict on MARKET cell must be consistent with implied payback ≤ 8 years
  (per `corpus/program/ECONOMIC-LENSES.md §2`).
- `win` verdict on COOPERATIVE cell must be consistent with break-even member
  count ≤ the feasible pool for that scale (per `corpus/program/SCALES.md`).
- `win` verdict on CIVIC cell must be consistent with per-household cost ≤ the
  civic cost ceiling for that scale.
- A `win` at `village` scale that flips to `fail` at `town` scale should be
  examined: the direction of scale effects must match what the lens math predicts
  (larger scale reduces per-unit fixed-cost burden for CIVIC; may increase or
  decrease feasibility for COOPERATIVE depending on member-pool size).

Contradiction between a verdict and its primary metric is a P1-level finding
and blocks that cell from appearing in playbook conclusions.

### 3c. Order-of-Magnitude Sniff Test

For each populated cell, apply a quick-check heuristic before deep review:

| Lens | Sniff test |
|------|-----------|
| MARKET | Payback years in range 2–30? Operator take-home positive? |
| COOPERATIVE | Break-even member count between 5 and 500? |
| CIVIC | Per-household annual cost between $5 and $500? |

Results outside these ranges are not automatically wrong, but they require an
explicit narrative explanation in the catalog entry's prose before the cell can
be used as evidence. "This entry is unusual because..." is a valid response;
silent out-of-range results are not.

---

## 4. Known-Parallel Case Studies

These are the sanity-check anchors for sim-output validation. Real-world
operations whose economics are documented well enough to serve as comparison
points. Section 3a instructs reviewers to compare Tier A outputs against these
anchors.

**This section is a stub. Plan D will populate each entry with source citations,
key metrics, and explicit mapping to catalog entry IDs.**

### 4.1 Real Microbakery Economics

- **Anchor:** Small-batch artisan bakery, US context, single operator or
  2-person operation, wood-fired or deck-oven, direct-to-consumer sales.
- **Key metrics to populate:** capital cost range, payback years (MARKET),
  weekly throughput in loaves, operator annual take-home.
- **Status:** `[to be populated by Plan D: source real bakery operator surveys,
  SBA loan data, or trade-association cost benchmarks; target 2–3 concrete cases
  with published financials or cited estimates]`
- **Catalog entries this anchors:** baking/ entries (populated in later vertical
  slices after smithing).

### 4.2 Real Community Forge / Tool-Library Cooperative Cases

- **Anchor:** Existing community-forge or shared-tool-library operations, US
  or EU context, cooperative or nonprofit governance, member-funded.
- **Key metrics to populate:** member count, annual dues, equipment capital cost,
  utilization rate, governance form.
- **Status:** `[to be populated by Plan D: survey ToolLibrary.org network,
  North American community-forge directories, Fab City / makerspace networks;
  target 3–5 cases with verifiable financials or published case studies]`
- **Catalog entries this anchors:** smithing/ entries with
  `lens_fit.cooperative: good`, especially shared/tool-library designs.

### 4.3 Real Library Per-Capita Cost Benchmarks

- **Anchor:** Municipal public-library systems as a reference point for the CIVIC
  lens. Libraries are the cleanest real-world parallel for civic-lens evaluation:
  publicly funded, usage-measured, per-capita cost tracked annually.
- **Key metrics to populate:** per-capita annual operating cost (US range),
  per-household capital amortization, usage hours per capita per year, range
  across rural / small-town / urban contexts.
- **Status:** `[to be populated by Plan D: ALA (American Library Association)
  annual survey data; IMLS Public Libraries Survey; target median + quartile
  range for towns 2k–75k population to bracket all three CERES scales]`
- **Catalog entries this anchors:** all entries with `lens_fit.civic: good` or
  `marginal`, across all trades.

### 4.4 Additional Anchors (Reserved)

- Real small-scale textile / weaving cooperative economics.
- Real ceramics studio / community kiln cost data.
- Real municipal forge or smithing-apprenticeship program costs (rare but
  documented in some European cities).
- **Status:** `[to be populated by Plan D alongside respective trade vertical
  slices; do not populate smithing-slice anchors from baking or weaving data]`

---

## 5. Failure Flagging

Sim results that fail a sanity check are **marked and flagged for re-review**,
not silently accepted or silently discarded.

### Flagging Protocol

When a Tier A cell fails validation (any of 3a, 3b, or 3c above):

1. **Do not remove the result.** The `results:` block in the catalog entry
   retains the numeric output; removing it obscures what the simulation
   actually produced.

2. **Add a validation annotation.** In the catalog entry's `results:` block,
   append a `validation_flags:` sub-key alongside the affected cell:

   ```yaml
   results:
     town_market:
       verdict: fail
       payback_years: 47
       validation_flags:
         - type: sniff-test-outlier
           note: "Payback 47y exceeds 30y sniff-test ceiling; needs explanation"
           status: needs-author-review
   ```

3. **Log in the tier-a validation record.** Add a row to the validation table
   in `simulations/tier-a-comparator/VALIDATION.md` (Plan D creates that file)
   with: entry ID, cell, failure type, and resolution status.

4. **Block playbook citation.** A cell carrying an unresolved `validation_flags`
   entry must not appear in `playbook/` conclusions or in the pitch narrative
   as positive evidence. It may appear as a documented failure mode.

5. **Resolution path.** The author may resolve a flag by:
   - Correcting the input data and re-running simulation (most common).
   - Adding an explanatory prose note to the catalog entry justifying why the
     out-of-range value is correct and not an error.
   - Confirming the result is a genuine failure mode and updating the entry's
     `lens_fit` field accordingly.

   Once resolved, the flag is updated to `status: resolved` with a dated note.
   A resolved flag does not disappear; it remains as an audit trail.

### What Counts as a Sanity-Check Failure

| Failure type | Trigger |
|-------------|---------|
| `no-parallel` | No real-world parallel exists for this cell; result is unanchored |
| `parallel-deviation-2x` | Sim output deviates >2× from strong real-world parallel |
| `parallel-deviation-5x` | Sim output deviates >5× from weak parallel |
| `sniff-test-outlier` | Primary metric outside the Section 3c heuristic range with no explanation |
| `internal-contradiction` | Verdict inconsistent with primary metric per Section 3b |
| `uncited-input` | Catalog entry `sim_params` contained uncited values (should have been caught at E-1, but logged here if discovered post-run) |

---

## 6. Deferrals to Plan D

This document is a **skeleton**. The following elements are explicitly deferred
to Plan D, which runs alongside and after the Tier A simulation code is written:

| Deferred element | Plan D deliverable |
|-----------------|-------------------|
| Specific test cases for Tier A | `simulations/tier-a-comparator/VALIDATION.md` — test matrix with expected ranges per entry |
| Regression suite | Automated checks that re-run after any `sim_params` edit and flag drift from baseline |
| Known-parallel case study population | Section 4 entries above: sourced, cited, mapped to entry IDs |
| Validation annotation tooling | Convention or script for writing `validation_flags:` entries consistently across the catalog |
| Cross-entry consistency checks | Tier A outputs across all 15 smithing entries should show monotonic scale effects where the lens math predicts them; Plan D defines and runs these |
| Tier B / Tier C validation criteria | System-dynamics and agent-based outputs require different validation approaches not defined here; Plan D addresses them when those tiers are built |

Plan D does not rewrite this document's philosophy or gate structure. It
**operationalizes** them: it turns the rules in Sections 1–5 into specific
test procedures, populates the stub anchors in Section 4, and creates the
validation machinery in `simulations/tier-a-comparator/`. If Plan D reveals
that a rule in this document is unworkable, it proposes a spec amendment rather
than silently deviating.
