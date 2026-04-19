# CERES Pipeline

Five-phase workflow guide — from raw historical research to a fundable pitch.

**Cross-references:** spec `specs/2026-04-18-ceres-design.md` §§ 4, 7, 8, 10;
review-tier rules `.craft/roles/ROLE.md`; skills in `skills/`.

---

## 1. Five-Phase Overview

```
Phase 1           Phase 2              Phase 3              Phase 4           Phase 5
Research    →   Design Catalog ★  →  Evaluation Matrix  →  Simulation   →   Playbook + Pitch
   ↑                                                                               │
   └──────────── feedback: failed designs revised and re-evaluated ────────────────┘
```

**Phase 1 — Research** extracts *functional requirements* from historical forms
across 4–6 anchor cultures (medieval Northern Europe, Song-era China, Tokugawa
Japan, Islamic Golden Age, Andean ayllu, American frontier). The output is not
a history essay; it is a requirements spec. What must a forge do? Temperature
range, throughput, fuel options, mobility, operator skill floor. History supplies
the requirements; design supplies the answers. Artifacts: `research/cultures/*/`
chapter files and `research/trades/<trade>/REQUIREMENTS.md`.

**Phase 2 — Design Catalog (the star)** produces 20–40 equipment-variant files
per trade, each a single Markdown file with structured YAML frontmatter and prose
sections. Every entry spans a distinct point in the design-tradeoff space: size,
capital cost, energy source, throughput, specialization, shareability, and skill
floor. Entries begin as `draft`, pass through panel review, and may reach
`validated`. Artifacts: `catalog/<trade>/entries/*.md`.

**Phase 3 — Evaluation Matrix** runs every catalog entry through 9 evaluation
cells — three scales (village, town, small city) × three economic lenses (market,
cooperative, civic). The lenses apply the formulas in
`corpus/program/ECONOMIC-LENSES.md` using scale thresholds from
`corpus/program/SCALES.md`. Each cell produces a `win | marginal | fail` verdict
plus a primary numeric metric (payback years, break-even members,
per-household cost). Artifacts: populated `results:` block in each catalog entry.

**Phase 4 — Simulation** is the engine behind the matrix. Tier A runs
deterministic math for every cell. Tier B models the town as a system of
inter-trade dependencies. Tier C targets specific high-risk scenarios on demand.
Tier A can ship independently; Tier B waits for at least two trades; Tier C is
invoked only when Tier A/B flag a need. Artifacts: `simulations/tier-*/`.

**Phase 5 — Playbook + Pitch** distills the evaluation results into actionable
plans and a funder narrative. Per-trade, per-context playbook files identify the
top 3–5 winning designs, supply an implementation sketch, and state open risks.
The pitch narrative frames the whole project for funders: what changed when local
production declined, what the research found, and what a pilot program would cost. Artifacts:
`playbook/<trade>/<scale>.md` and `playbook/pitch/PITCH-NARRATIVE.md`.

---

## 2. Per-Phase Workflow

### Phase 1 — Research

| Dimension | Detail |
|-----------|--------|
| **Inputs** | Historical sources (cited via MAXIM reference base); blank culture and trade templates |
| **Outputs** | `research/cultures/<culture>/` chapter files; `research/trades/<trade>/REQUIREMENTS.md`, `HISTORICAL-FORMS.md`, `SOURCES.md` |
| **Review tiers that fire** | Panel (all 6) reviews the requirements document; Editorial E-2 (scope) checks for non-goal violations |
| **Promotion criteria** | `REQUIREMENTS.md` is declared complete when all functional parameters are cited, all falsifier tests (spec §2) are addressed, and panel R1 findings are resolved |

### Phase 2 — Design Catalog

| Dimension | Detail |
|-----------|--------|
| **Inputs** | `research/trades/<trade>/REQUIREMENTS.md`; `catalog/<trade>/SCHEMA.md`; `corpus/program/ECONOMIC-LENSES.md` |
| **Outputs** | `catalog/<trade>/entries/*.md` — each file carries complete YAML frontmatter and prose sections; `status` starts at `draft` |
| **Review tiers that fire** | Panel (all 6) on every draft entry; Editorial (all 3) on the promotion gate to `validated`; Board on demand for contested technical claims |
| **Promotion criteria** | Entry advances from `draft` → `reviewed` after panel R1 findings are addressed; from `reviewed` → `validated` after Editorial all-3-pass clears it (see §4 below) |

### Phase 3 — Evaluation Matrix

| Dimension | Detail |
|-----------|--------|
| **Inputs** | `catalog/<trade>/entries/*.md` at `reviewed` or `validated` status; `corpus/program/ECONOMIC-LENSES.md`; `corpus/program/SCALES.md` |
| **Outputs** | Populated `results:` block (9 cells) in each catalog entry; summary tables in `simulations/tier-a-comparator/results/` |
| **Review tiers that fire** | Panel (all 6) reviews the Tier A results documentation; Editorial E-3 (numeracy) cross-checks the output before any result is cited in a playbook |
| **Promotion criteria** | All 9 cells filled with non-null verdicts; `corpus/program/VALIDATION.md` sanity checks pass; E-3 gate cleared |

### Phase 4 — Simulation

| Dimension | Detail |
|-----------|--------|
| **Inputs** | `catalog/<trade>/entries/*.md` (complete `sim_params` blocks); `simulations/tier-a-comparator/model.py` or equivalent |
| **Outputs** | Tier A: 9-cell verdicts per entry. Tier B: dependency maps + resilience scores (requires ≥2 trades). Tier C: targeted scenario outputs |
| **Review tiers that fire** | Panel (all 6) reviews the simulation model documentation; Board invited when a simulation assumption is trade-domain-specific |
| **Promotion criteria** | Tier A: all entries evaluated, results written back to frontmatter, `VALIDATION.md` sanity checks complete. Tier B: scaffolded in vertical slice; substantive runs deferred until trade #2 |

### Phase 5 — Playbook + Pitch

| Dimension | Detail |
|-----------|--------|
| **Inputs** | Validated catalog entries with fully populated `results:` blocks; Tier A output |
| **Outputs** | `playbook/<trade>/{village,town,small-city}.md`; `playbook/pitch/PITCH-NARRATIVE.md` |
| **Review tiers that fire** | Panel (all 6) and Editorial (all 3) on every playbook file and the pitch narrative |
| **Promotion criteria** | All three lens-winner files authored; pitch narrative cites catalog and playbook evidence; Editorial all-3-pass clears pitch before external circulation |

---

## 3. Review-Tier Firing Rules

Source: `.craft/roles/ROLE.md` — "When Each Tier Fires" table.

### Summary

| Artifact | Panel (all 6) | Editorial (all 3) | Board |
|---|---|---|---|
| Spec | fires | E-2 (scope) only | optional |
| Implementation plan | fires | E-2 (scope) only | optional |
| Catalog entry — draft | fires | — | — |
| Catalog entry — review → validated | — | fires | invited for expert claims |
| Playbook file | fires | fires | optional |
| Pitch narrative | fires | fires | — |

### Panel (6 voices — every artifact)

Panel fires on **every artifact** at draft stage. No exceptions. The six voices
(P-1 Market Economist, P-2 Commons Theorist, P-3 Civic Steward, P-4 Craft
Practitioner, P-5 Historian, P-6 Skeptical Funder) represent productive tensions:
private profit vs member commons, municipal stewardship vs market competition,
hands-on craft reality vs historical realism vs funder rigor.

Reviews land in `reviews/R{N}-P{N}-{voice}-{artifact-slug}.md`. Invoke via
`/ceres-panel` (see `skills/ceres-panel/SKILL.md` for HOW; this document
addresses WHEN).

### Editorial (3 lenses — promotion gate)

Editorial fires only on **artifacts about to be promoted** from `reviewed` to
`validated`. It is not a discussion; it is a checklist with teeth. The three
lenses are:

- **E-1 Citation Auditor** — every number cited, every historical claim
  verifiable. P1 finding if ≥3 uncited claims.
- **E-2 Scope Keeper** — no spec drift, no non-goal violations, no schema
  violations. P1 finding on any non-goal or schema breach.
- **E-3 Numeracy Checker** — throughput ↔ labor, payback ↔ implied revenue,
  currency normalization, order-of-magnitude sanity. P1 on any
  order-of-magnitude error or internal contradiction.

An artifact is cleared only if all three lenses return `pass` or
`fix-and-recheck-resolved`. Any single `block` verdict holds the artifact.

Reviews land in `reviews/CLEAN-E{N}-{lens}-{artifact-slug}.md`. Invoke via
`/ceres-editorial` (see `skills/ceres-editorial/SKILL.md`).

### ceres-check (cross-tier fast audit — any stage)

`ceres-check` (`skills/ceres-check/SKILL.md`) is not a separate review tier; it is a
structured cross-tier checklist tool available at any stage of the pipeline. It
dynamically selects applicable roles from the role library, runs each role's
`lens.verify` checklist against the artifact, and produces a findings table with
severity codes.

Use it for:

- Pre-promotion fast audits (before triggering a full editorial pass).
- Targeted scans on a single concern (e.g., citations only: `scope filter:citation`).
- Quick structural health checks on drafts before a full panel run.

`ceres-check` complements `ceres-panel` — panel does deep qualitative first-person
reviews; `ceres-check` produces a structured findings table. Use both in sequence for
a complete review. See `skills/ceres-check/SKILL.md` for the "When to Use ceres-check
vs. ceres-panel" guidance table.

### Board (per-trade — on demand)

Board fires when:

1. A panel reviewer flags a claim as beyond their expertise.
2. An author proactively requests adjudication of a contested technical or
   historical claim.

The board is assembled per claim (2–3 domain experts), not per trade wholesale.
Board members are defined in `.craft/roles/board/` using the template at
`.craft/roles/board/ROLE.md`.

Reviews land in `reviews/BOARD-B-{trade}-{slug}-{artifact-slug}.md`. Invoke via
`/ceres-board` (see `skills/ceres-board/SKILL.md`).

---

## 4. Catalog-Entry Lifecycle

Every catalog entry follows this state machine. Movement is earned, not assumed.

```
              author submits
                    │
                    ▼
               ┌─────────┐
               │  draft  │ ──── Panel review fires (all 6)
               └─────────┘
                    │
                    │  panel R1 findings resolved?
                    │  YES ──────────────────────────────────────┐
                    │  NO (major issues)                         │
                    ▼                                            ▼
              ┌──────────┐                               ┌──────────────┐
              │  revise  │ ── author revises ──────────▶ │   reviewed   │
              └──────────┘                               └──────────────┘
                                                                │
                                                                │  Editorial pass triggers
                                                                ▼
                                                       ┌─────────────────┐
                                                       │ Editorial gate  │
                                                       │  E-1 + E-2 + E-3│
                                                       └─────────────────┘
                                                          │           │
                                                          │ P1 found  │ all-pass
                                                          ▼           ▼
                                                       ┌──────┐  ┌───────────┐
                                                       │ held │  │ validated │
                                                       └──────┘  └───────────┘
                                                          │
                                                          │  unresolvable
                                                          ▼
                                                     ┌────────────┐
                                                     │ deprecated │
                                                     └────────────┘
```

### State definitions

| State | Meaning |
|-------|---------|
| `draft` | Author-submitted; panel review has not yet cleared it |
| `reviewed` | Panel R1 (and R2 if needed) findings addressed; entry is structurally sound; Editorial has not yet run |
| `validated` | Editorial all-3-pass cleared; all `sim_params` cited; `results:` block populated |
| `held` | Editorial found P1 issues; author must fix before re-running editorial |
| `deprecated` | Design is superseded or proven non-viable; entry retained in catalog for record, linked to what replaced it |

### Transition rules

**`draft` → `reviewed`**
- Panel R1 fires (all 6 voices).
- Author addresses all panel findings.
- If substantive changes: Panel R2 fires on revised entry.
- If only minor revisions: author documents resolution; R2 not required.
- Entry gains `status: reviewed` and increments `version`.

**`reviewed` → `validated`**
- Editorial pass fires (E-1, E-2, E-3 — all three).
- All P1 editorial findings fixed.
- P2 findings tracked; author decides.
- All `sim_params` numbers carry citations in `sources:`.
- `results:` block fully populated (Tier A evaluation complete).
- Board invited if any expert claim was contested during panel review.

**`validated` → `held`**
- Not a normal transition. Occurs only if post-validation evidence undermines a
  cited source or a sim error is discovered.
- Treat as a P1 editorial finding on an already-validated entry; entry reverts
  to `held` pending a corrective revision.

**Any state → `deprecated`**
- A new entry supersedes this one (link via `supersedes:` field in the new
  entry).
- Research reveals the design premise is falsified.
- Deprecated entries remain in the catalog — they are a record of what was
  tested and why it failed.

---

## 5. Spec-Amendment Pathway

The spec (`specs/2026-04-18-ceres-design.md`) is the authoritative scope
document. When an artifact needs content the spec does not authorize, do not
silently expand the scope. Follow this pathway:

1. **Stop.** Identify the specific gap: what does the artifact need that the
   spec does not authorize?
2. **Write a short amendment.** Create `specs/AMENDMENT-{YYYYMMDD}-{slug}.md`
   with:
   - The specific section of the spec being extended.
   - The proposed addition (one paragraph or a short table).
   - The reason (what artifact, what new need).
3. **Link from the artifact.** In the artifact's frontmatter or prose, add a
   note: `Amendment: specs/AMENDMENT-{YYYYMMDD}-{slug}.md`.
4. **Submit the amendment for review.** Panel fires on spec amendments (see §3
   firing table: "Spec → Panel all 6, Editorial E-2 scope").
5. **Only after the amendment is accepted**, revise the artifact to include the
   expanded content.

This pathway exists because silent scope expansion is the most common way
research-grade projects drift into unfalsifiable narratives. The amendment log
is the audit trail.

---

## 6. Simulation Tier Escalation

Source: spec §7 (Simulation Tiers).

### Tier A — Scenario Comparator (runs on every cell)

- **What it is:** Deterministic math. Runs the applicable lens rule
  (`corpus/program/ECONOMIC-LENSES.md`) for every (entry × scale × lens) cell.
- **Trigger:** Every catalog entry at `reviewed` status or above.
- **Output:** `win | marginal | fail` verdict + primary metric for each of the
  9 cells. Results written back to the `results:` block in the catalog entry.
- **Validation:** Outputs sanity-checked against real-world parallels documented
  in `simulations/tier-a-comparator/VALIDATION.md`.

### Tier B — System Dynamics (requires ≥2 trades)

- **What it is:** Models the town as a system of inter-trade dependencies
  (miller → baker; tanner → cobbler; forge repairs everyone). Answers questions
  Tier A cannot: cascade risk, resilience under shocks, collapse dynamics.
- **Trigger:** Fires only after at least two trades have complete Tier A
  results. In the Phase-1 vertical slice (smithing only), Tier B is scaffolded
  — directory and README — but substantive runs are deferred.
- **Output:** Dependency maps and resilience scores per scenario in
  `simulations/tier-b-system-dynamics/results/`.
- **Escalation from Tier A:** Whenever Tier A reveals a design that is
  `marginal` or `fail` for a systemic reason (not just unit economics), flag
  it for Tier B analysis.

### Tier C — Agent-Based (targeted, on demand)

- **What it is:** Reserved for high-value specific questions: labor-pipeline
  failures (smith retires, no apprentice), regulatory shocks, energy-price
  shocks, generational succession.
- **Trigger:** Invoked only when Tier A or Tier B results flag a scenario
  that requires agent-level dynamics to resolve. Not run on every entry.
  Every Tier C run must have an explicit research question written before
  the model executes.
- **Output:** Per-run scenario analysis in `simulations/tier-c-agent-based/`.

### Escalation summary

| Tier | Runs on | Trigger | Deferred until |
|------|---------|---------|----------------|
| A | Every (entry × scale × lens) cell | Entry reaches `reviewed` | Never — always runs |
| B | Town-as-system scenarios | After ≥2 trades complete | Trade #2 Tier A complete |
| C | Specific targeted questions | Tier A/B flags a need | On demand only |

---

## 7. Pipeline Diagram

Adapted from spec §4.1.

```
┌────────────────────────────────────────────────────────────────────────────┐
│                          CERES PIPELINE                                    │
└────────────────────────────────────────────────────────────────────────────┘

  PHASE 1          PHASE 2           PHASE 3           PHASE 4      PHASE 5
 ┌──────────┐    ┌──────────────┐  ┌────────────────┐  ┌────────┐  ┌────────┐
 │          │    │              │  │                │  │        │  │        │
 │ Research │───▶│ Design       │─▶│ Evaluation     │─▶│  Sim   │─▶│Playbook│
 │          │    │ Catalog  ★   │  │ Matrix         │  │        │  │  +     │
 │ 4–6      │    │              │  │ 9 cells per    │  │ Tier A │  │ Pitch  │
 │ cultures │    │ 20–40 entries│  │ entry          │  │ Tier B │  │        │
 │ per trade│    │ per trade    │  │ (3 scales ×    │  │ Tier C │  │        │
 │          │    │              │  │  3 lenses)     │  │        │  │        │
 └──────────┘    └──────────────┘  └────────────────┘  └────────┘  └────────┘
      │                │                                                 │
      │                │     REVIEW TIERS                                │
      │                │     ┌────────────────────────────────────┐      │
      │                │     │ PANEL (6)   — every artifact       │      │
      │                └────▶│ EDITORIAL   — promotion gate only  │      │
      │                      │ BOARD       — on demand            │      │
      │                      └────────────────────────────────────┘      │
      │                                                                   │
      │          feedback loop: failed designs revised and re-evaluated   │
      └───────────────────────────────────────────────────────────────────┘


  CATALOG ENTRY STATE MACHINE (Phase 2 detail)
  ┌───────┐  panel R1   ┌──────────┐  editorial  ┌───────────┐
  │ draft │────────────▶│ reviewed │─────────────▶│ validated │
  └───────┘             └──────────┘              └───────────┘
      ▲                      │ P1 found                 │ evidence
      │  author revises      ▼                          │ overturned
      └──────────────── ┌──────┐         ┌────────────┐ │
                        │ held │─────────▶ deprecated │◀┘
                        └──────┘         └────────────┘


  SIMULATION TIER ESCALATION (Phase 4 detail)
  ┌────────────────────┐
  │  Tier A            │ ← runs every (entry × scale × lens) cell
  │  Scenario Compar.  │
  └────────┬───────────┘
           │ systemic signals / ≥2 trades complete
           ▼
  ┌────────────────────┐
  │  Tier B            │ ← models town-as-system; deferred to trade #2
  │  System Dynamics   │
  └────────┬───────────┘
           │ targeted question flagged
           ▼
  ┌────────────────────┐
  │  Tier C            │ ← agent-based; on demand only
  │  Agent-Based       │
  └────────────────────┘
```

---

## Appendix: Phase-1 Vertical Slice Definition of Done

Source: spec §10.

The vertical slice (smithing trade end-to-end) is complete when:

| Deliverable | Target |
|---|---|
| `research/trades/smithing/REQUIREMENTS.md` | written, cited |
| `research/cultures/*/smithing.md` | 4–6 cultures, short chapters each |
| `catalog/smithing/SCHEMA.md` | finalized |
| `catalog/smithing/entries/*.md` | ~15 forge designs, all schema-complete |
| `corpus/program/ECONOMIC-LENSES.md` | three lens rules formalized |
| `simulations/tier-a-comparator/` | all 15 × 9 = 135 cells evaluated |
| `simulations/tier-b-system-dynamics/` | scaffolded only (deferred to trade #2) |
| `playbook/smithing/{village,town,small-city}.md` | three files written |
| `playbook/pitch/PITCH-NARRATIVE.md` | first draft, smithing-only evidence |

15 catalog entries is a deliberate floor: enough variety to make the catalog
meaningful; few enough that the vertical slice does not stall. After the slice
completes, subsequent trades replicate the same structure — the slice is the
template.
