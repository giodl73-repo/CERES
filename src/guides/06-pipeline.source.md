# Pipeline — Five Phases from Research to Pitch

The CERES pipeline has five phases. Each phase has defined inputs, defined
outputs, and review-tier firing rules. An artifact does not enter the next
phase until the current phase's criteria are met.

Full reference: `docs/PIPELINE.md`.

---

## Phase overview

```proof:tree kind=org
Five phases
- Phase 1 — Research: extract functional requirements from historical forms
- Phase 2 — Design Catalog (the star): one file per equipment design variant
- Phase 3 — Evaluation Matrix: run 9 cells per entry (3 scales × 3 lenses)
- Phase 4 — Simulation: Tier A deterministic, Tier B system dynamics, Tier C targeted
- Phase 5 — Playbook + Pitch: identify winners, write implementation and funder narrative
```

There is a feedback loop from Phase 5 back to Phase 1: failed designs are
revised and re-evaluated. The loop runs forward; it does not run backward
through completed validation.

---

## Phase 1 — Research

**Purpose:** Extract *functional requirements* from historical forms. Not a
history essay; a requirements spec.

**Questions to answer:**
- What must this equipment do? (temperature range, throughput, precision)
- What were the real constraints? (fuel, space, skill, maintenance)
- Why did this trade decline? (which constraint became binding, when, why)

**Output artifacts:**

| Artifact | Path |
|----------|------|
| Culture chapters | `research/cultures/<culture>/<trade>.md` |
| Requirements | `research/trades/<trade>/REQUIREMENTS.md` |
| Historical forms | `research/trades/<trade>/HISTORICAL-FORMS.md` |
| Decline verdict | `research/trades/<trade>/DECLINE-VERDICT.md` |
| Sources | `research/trades/<trade>/SOURCES.md` |

**Review:** Panel (all 6) on `REQUIREMENTS.md`. E-2 (scope) checks for
non-goal violations.

**Completion criteria:** All functional parameters cited. All falsifier tests
from the spec addressed. Panel R1 findings resolved.

```proof:callout kind=warning label="The decline verdict is load-bearing"
The DECLINE-VERDICT.md file defines the binding constraints that caused the
trade to decline. Every catalog entry in that trade must address these
constraints explicitly. An entry that ignores the decline verdict will fail
P-6 (Skeptical Funder) at panel review.
```

---

## Phase 2 — Design Catalog

**Purpose:** Design 15–40 equipment variants per trade, each occupying a
distinct position in the design-tradeoff space.

**The tradeoff space dimensions:**
- Capital cost (low to high)
- Scale (village to small city)
- Energy source (electric, gas, propane, wood, human-powered)
- Throughput (micro to production scale)
- Operator skill floor (apprentice to master)
- Ownership model affinity (market / cooperative / civic)
- Mobility (fixed, semi-portable, mobile)

A good catalog does not cluster entries. It spreads them across the space so
that a reader can compare designs that differ on one dimension while holding
others constant.

**Output:** `catalog/<trade>/entries/*.md` — each file has complete YAML
frontmatter and prose sections; `status: draft`.

**Review:** Panel (all 6) on every draft entry. Editorial on the promotion
gate to `validated`. Board on demand.

**Entry lifecycle:**

| Step | What happens |
|------|-------------|
| Author submits | Entry at `status: draft` |
| Panel R1 fires | All 6 voices review |
| Author addresses findings | Fix P1s; document P2 decisions |
| Panel R2 (if substantive changes) | Re-review by affected voices |
| Advance to `reviewed` | `status: reviewed`; version incremented |
| Editorial gate fires | E-1, E-2, E-3 all run |
| Author fixes P1 findings | Re-run blocking lenses |
| Advance to `validated` | `status: validated`; results block populated |

Entries may also reach `held` (editorial P1 blocking) or `deprecated`
(superseded or falsified). Deprecated entries stay in the catalog — they are
a record of what was tested and why it failed.

---

## Phase 3 — Evaluation Matrix

**Purpose:** Run every catalog entry through 9 evaluation cells
(3 scales × 3 lenses) and populate the `results:` block in each entry.

**Input:** Catalog entries at `reviewed` or `validated` status with complete
`sim_params` blocks.

**The 9 cells:**

```proof:tree kind=org
Results grid
- village_market, village_coop, village_civic
- town_market, town_coop, town_civic
- small_city_market, small_city_coop, small_city_civic
```

Each cell produces:
- `verdict: win | marginal | fail`
- `primary_metric` (payback years / break-even members / per-household cost)
- `metric_name`
- `notes` (key numbers for `fail` and `marginal` cells)

**Review:** Panel (all 6) on the Tier A results documentation. E-3 cross-checks
output before any result is cited in a playbook.

**Completion criteria:** All 9 cells filled with non-null verdicts.
`corpus/program/VALIDATION.md` sanity checks pass. E-3 cleared.

---

## Phase 4 — Simulation

Three simulation tiers with different escalation triggers:

### Tier A — Scenario Comparator

**What:** Deterministic math. Applies lens formulas
(`corpus/program/ECONOMIC-LENSES.md`) to every (entry × scale × lens) cell.

**Trigger:** Every catalog entry at `reviewed` status or above.

**Output:** `win | marginal | fail` verdict + primary metric for each of the
9 cells, written back to the catalog entry's `results:` block.

**Never deferred.** Tier A runs on every entry. It is the minimum viable
evaluation.

### Tier B — System Dynamics

**What:** Models the town as a system of inter-trade dependencies. Answers
questions Tier A cannot: cascade risk, resilience under shocks, what happens
when the forge closes and the mill cannot get its millstone refit.

**Trigger:** Fires only after at least two trades have complete Tier A results.
In the current three-trade slice (smithing + baking + weaving), Tier B is
available. The scaffolding is in `simulations/tier-b-system-dynamics/`.

**Output:** Dependency maps and resilience scores in
`simulations/tier-b-system-dynamics/results/`.

**Escalation from Tier A:** Whenever Tier A reveals a `marginal` or `fail`
verdict for a systemic reason (not just unit economics), flag it for Tier B
analysis.

### Tier C — Agent-Based

**What:** High-specificity models for targeted scenarios: labor-pipeline
failures, regulatory shocks, energy-price shocks, generational succession.

**Trigger:** On demand only. Every Tier C run must have an explicit research
question written before the model executes. Do not run Tier C speculatively.

**Output:** Per-run scenario analysis in `simulations/tier-c-agent-based/`.

### Escalation summary

| Tier | Runs on | Trigger |
|------|---------|---------|
| A | Every (entry × scale × lens) cell | Entry reaches `reviewed` |
| B | Town-as-system scenarios | After ≥2 trades' Tier A complete |
| C | Specific targeted questions | Tier A/B flags a need |

---

## Phase 5 — Playbook + Pitch

**Purpose:** Distill evaluation results into actionable plans (playbook) and a
funder narrative (pitch).

### Playbook files

One file per (trade × scale) combination — nine files for three trades:

```
playbook/smithing/village.md
playbook/smithing/town.md
playbook/smithing/small-city.md
playbook/baking/village.md
...
```

Each file:
1. Identifies the top 3–5 winning designs from the catalog (by catalog id)
2. Explains why these designs win at this scale
3. Provides an implementation sketch (not a supplier BOM)
4. States open risks and what would change the verdict

### Pitch narrative

`playbook/pitch/PITCH-NARRATIVE.md` is the funder-facing document:

- What changed when local production declined (the problem)
- What the research found (the evidence base)
- What a pilot program would cost and what it would prove
- Honest responses to the three most likely funder objections

The pitch is persuasive but rigorous. It cites catalog entry ids and playbook
evidence. It does not make claims that are not supported by validated entries.

**Review:** Panel (all 6) and Editorial (all 3) on every playbook file and the
pitch narrative. Editorial clearance is required before the pitch goes to any
external audience.

---

## Spec amendment pathway

When an artifact needs content the spec does not authorize, do not silently
expand scope. Follow this pathway:

```proof:tree kind=org
Spec amendment steps
- Step 1: Stop. Identify the specific gap.
- Step 2: Write specs/AMENDMENT-{YYYYMMDD}-{slug}.md (section, proposed addition, reason).
- Step 3: Link from the artifact frontmatter ("Amendment: specs/AMENDMENT-...").
- Step 4: Submit for review (Panel all 6, Editorial E-2 scope).
- Step 5: Only after acceptance, revise the artifact.
```

```proof:callout kind=warning label="Silent scope expansion is the most common failure mode"
Research-grade projects drift into unfalsifiable narratives through incremental
scope expansion. The amendment log is the audit trail. Every expansion is
visible and reviewed. There are no exceptions.
```

---

## Current project status

As of 2026-04-19, Plans A–J are complete:

| Phase | Status |
|-------|--------|
| Phase 1 — Research | Complete for smithing, baking, weaving, artisan square |
| Phase 2 — Catalog | 15 entries per trade (45 total); all at `draft` or `reviewed` |
| Phase 3 — Evaluation | Tier A results populated for all 135 cells (3 trades × 15 entries × 9 cells) |
| Phase 4 — Simulation | Tier A complete; Tier B scaffolded; Tier C on demand |
| Phase 5 — Playbook + Pitch | All 9 playbook files authored; pitch narrative complete; pending final panel review |

Check `TRACKER.md` for current per-artifact status.
