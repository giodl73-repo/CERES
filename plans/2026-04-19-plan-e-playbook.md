---
id: plan-e-playbook
name: Playbook and Pitch Narrative — Smithing Vertical Slice
description: Per-scale playbook files naming winning designs + pitch narrative for funders; incorporates Plan D matrix findings directly; pre-flight civic-lens diagnostic addresses the all-fail civic finding
status: draft
version: "1.0"
created: 2026-04-19
phase: 5
subsystem: playbook
trade: smithing
depends_on: [plan-a-scaffolding, plan-b-research-smithing, plan-c-catalog-smithing, plan-d-sim]
blocks: []
estimated_effort: 1-2 weeks focused
primary_artifact_type: playbook
success_signal: >
  Three per-scale playbook files (`playbook/smithing/village.md`, `town.md`,
  `small-city.md`) identify winning catalog entries for each scale with
  implementation sketch + capital ask + open risks. Pitch narrative at
  `playbook/pitch/PITCH-NARRATIVE.md` frames the CERES project for the
  declared funder archetype (civic-economic-development foundation per
  spec §11.5). Civic-lens anomaly from Plan D is either (a) resolved by
  formula correction and sim re-run, or (b) incorporated honestly as a
  project finding. All three per-scale playbooks cite specific entries
  and their Tier A verdicts.
spec: specs/2026-04-18-ceres-design.md
---

# Plan E: Playbook and Pitch Narrative — Smithing Vertical Slice

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans.

**Goal:** Convert the Plan D simulation matrix + Plan B research + Plan C catalog into the project's terminal deliverables: per-scale playbooks and a funder-facing pitch. Plan E is where CERES's evidence becomes a publishable argument.

**Architecture:** Authoring-heavy. Pre-flight diagnostic on Plan D's civic lens (the all-fail civic finding requires either formula correction OR honest framing). Three per-scale playbooks (parallel authoring). One pitch narrative (integrates all three). Closeout updates TRACKER and vertical-slice DoD.

**Tech Stack:** Markdown only. No code (unless pre-flight diagnostic requires a Plan D `lenses.py` edit + sim re-run).

**Source of truth:**
- `research/trades/smithing/DECLINE-VERDICT.md` — niche-targeting implications for the pitch
- `catalog/smithing/entries/*.md` — 15 entries with populated `results:` blocks
- `simulations/tier-a-comparator/results/SUMMARY.md` — matrix aggregate
- `corpus/program/ECONOMIC-LENSES.md` — authoritative lens rules (reference for the civic diagnostic)
- `specs/2026-04-18-ceres-design.md` §9 (Playbook + Pitch), §11 (Success Criteria + funder archetype)

---

## The Plan D Findings (summary for context)

Tier A produced 51 wins / 0 marginal / 84 fails across 135 cells:

| Cell | Wins / Fails | Key insight |
|---|---|---|
| market (all 3 scales) | 7 / 8 | Same 7 entries win at every scale — market viability is capital-sensitive, not scale-sensitive |
| coop (village) | 2 / 13 | Village member pool (~31) supports only the lowest-capital entries (forge-001, forge-014) |
| coop (town + small-city) | 15 / 0 | Every entry clears coop at town+ scale — member pool abundant |
| civic (all 3 scales) | 0 / 45 | **Every civic cell fails.** Requires diagnosis. |

The civic all-fail pattern is Plan E's first work item.

---

## Task Index

| # | Task | Creates |
|---|---|---|
| 1 | Civic-lens diagnostic | `simulations/tier-a-comparator/results/CIVIC-LENS-DIAGNOSTIC.md` (+ possible fix in `lenses.py` + sim re-run) |
| 2 | Village playbook | `playbook/smithing/village.md` |
| 3 | Town playbook | `playbook/smithing/town.md` |
| 4 | Small-city playbook | `playbook/smithing/small-city.md` |
| 5 | Pitch narrative | `playbook/pitch/PITCH-NARRATIVE.md` |
| 6 | Cross-artifact review | `reviews/PLAN-E-REVIEW.md` |
| 7 | Closeout | TRACKER + plans/README + Plan E frontmatter + spec DoD check |

Execution waves:
- **Wave 0** (sequential): Task 1 — diagnostic; may trigger a sim re-run that invalidates Plan D outputs in-place
- **Wave 1** (parallel × 3): Tasks 2, 3, 4 — per-scale playbooks
- **Wave 2** (sequential): Task 5 — pitch narrative (consumes Wave 1 outputs)
- **Wave 3** (sequential): Task 6 review, Task 7 closeout

---

## Task 1 — Civic-Lens Diagnostic

**Files:**
- Create: `simulations/tier-a-comparator/results/CIVIC-LENS-DIAGNOSTIC.md`
- Possibly modify: `simulations/tier-a-comparator/src/tier_a/lenses.py`
- Possibly re-run: `python -m tier_a.cli --catalog catalog/smithing/ --results-dir .../results`
- Possibly update: 15 catalog entries' `results:` blocks

### The Question

The civic lens failed all 45 cells on the utilization sub-condition. The formula computes `facility_hours_per_capita_per_year = max_active_hours_per_week × 52 / population_midpoint` and requires ≥ 2.0 hr/capita/yr. Civic-oriented entries (forge-004, forge-011) have 25-30 hr/wk × 52 ÷ 8,500 pop = 0.15-0.18 hr/capita/yr — dramatically below threshold.

Three possible diagnoses:

1. **Formula bug — concurrency missing.** A civic makerspace hosts multiple users concurrently (4+ stations typical). Facility-hours are NOT the same as per-capita hours unless divided by concurrency. Correct formula might be: `(facility_hours × concurrent_users) / household_count` (NOT population; households use-based).
2. **Formula correct — catalog data wrong.** The entries' `max_active_hours_per_week` may reflect apprentice-only use, not the public-access scheduling a civic facility would actually offer (civic libraries run 60+ hr/wk).
3. **Formula correct, data correct — finding is real.** Smithing facilities of this scale genuinely don't support civic utilization (the 15-entry catalog is not designed as public-access civic infrastructure).

### Procedure

1. Read `simulations/tier-a-comparator/src/tier_a/lenses.py` civic_lens function. Identify the actual utilization computation.
2. Review catalog entries with civic-primary or civic-marginal claims (forge-003, forge-004, forge-011, forge-015) — what did the authors intend for public-access hours?
3. Reference `corpus/program/ECONOMIC-LENSES.md` §4 for the authoritative CIVIC lens rule.
4. Cross-check with real civic benchmarks: a public library serves ~7,000 visits/yr per branch (roughly 50-80 hr/wk × 52 / 10,000 pop = ~2-3 hr/capita nominal, with many concurrent users per hour).
5. **Choose a path:**
   - **Path A (formula fix):** if the formula is missing concurrency, add a `concurrent_capacity` field extraction (from `operators_concurrent` or a new sim_param), update the formula, re-run the CLI, commit updated catalog entries + new SUMMARY.md.
   - **Path B (data revisions):** if entries' `max_active_hours_per_week` is unrealistic for civic operation, flag those entries for Plan F (future) — Plan E does not rewrite catalog entries. Document the finding.
   - **Path C (accept finding):** if formula and data are both correct, the "smithing doesn't support civic lens as conceived" is a genuine project finding. Incorporate into pitch narrative.

### Output

`CIVIC-LENS-DIAGNOSTIC.md` with:
- The question
- Evidence from lenses.py code + catalog-entry data + authoritative ECONOMIC-LENSES rule
- Chosen path (A/B/C) with rationale
- If Path A: the code change + the re-run results (delta from original SUMMARY)
- If Path B: per-entry flags for future data revision
- If Path C: framing note for the pitch narrative

### Commit

- If Path A: two commits — one for the lens fix + tests, one for the re-run results + catalog updates
- If Path B or C: single commit with just the diagnostic doc

```bash
git add simulations/tier-a-comparator/results/CIVIC-LENS-DIAGNOSTIC.md [+ other files per path]
git commit -m "Plan E task 1: civic-lens diagnostic — path {A|B|C}"
```

---

## Task 2 — Village Playbook

**Files:**
- Create: `playbook/smithing/village.md`

### Content requirements

Based on the Tier A matrix at village scale (post-diagnostic if Path A), for each lens (market / coop / civic):

1. **Winning designs:** which catalog entries cleared `good` verdict at village scale under this lens? Name the entry IDs and the metrics.
2. **Runner-ups / marginals:** borderline entries and why they fell short.
3. **Implementation sketch:** for the top 2-3 winning designs, what would a town-of-1000 actually do to establish this? Timeline (pilot year → steady state), hiring (who runs it), customer acquisition, first-year budget.
4. **Capital ask:** what does a village need to fund to operationalize these designs? Include both private-capital (market path) and grant/coop-contribution (coop/civic paths).
5. **Open risks:** regulatory (coal in some contexts), labor pipeline (apprentice sourcing at thin population), supply-chain (steel source), demand variance.

### Required sections

- Frontmatter: `trade: smithing`, `scale: village`, `doc_type: playbook`, `derived_from:` (matrix + catalog + research), `version: "1.0"`, `status: draft`
- Matrix summary (9-cell table: only 3 village cells populated) at top
- Per-lens sections (Market / Cooperative / Civic)
- Cross-lens synthesis (if market path works but coop doesn't at village, that's the message)
- Implementation sketches (2-3 designs detailed)
- Capital ask (order-of-magnitude)
- Open risks

Target length: 1500-2500 words.

### Style

Directive, actionable. STYLE-GUIDE §7 "clear directive voice for playbook files." No marketing.

### Commit

```bash
git add playbook/smithing/village.md
git commit -m "Plan E task 2: village playbook for smithing"
```

---

## Task 3 — Town Playbook

**Files:**
- Create: `playbook/smithing/town.md`

Same structure as Task 2 but for town scale. Expected to have RICHER matrix (more wins) — town-scale coop was 15/0 pre-diagnostic, market 7/8, civic 0/15 (pre-diagnostic).

Highlight: town scale is where coop viability kicks in across all entries. Playbook should explain why (member pool abundant). Implementation sketches should include at least one coop-primary entry.

### Commit

```bash
git add playbook/smithing/town.md
git commit -m "Plan E task 3: town playbook for smithing"
```

---

## Task 4 — Small-City Playbook

**Files:**
- Create: `playbook/smithing/small-city.md`

Same structure. Small-city has the most robust matrix — all 7 market winners, all 15 coop winners, and (if Path A or C resolves civic) some civic wins.

Implementation sketches should include a small-city-scale civic-partnership entry (forge-004 or forge-011) as the headline civic example.

### Commit

```bash
git add playbook/smithing/small-city.md
git commit -m "Plan E task 4: small-city playbook for smithing"
```

---

## Task 5 — Pitch Narrative

**Files:**
- Create: `playbook/pitch/PITCH-NARRATIVE.md`

Per spec §9 and §11.5. Target funder archetype: civic-economic-development foundation or municipal development office ($250k-$2M program-related investment or grant).

### Required sections (per spec §9)

1. **The problem** — what was lost when local smithing declined. Draw on DECLINE-VERDICT's mixed verdict. Avoid romanticism (STYLE-GUIDE §4).
2. **The approach** — catalog-driven design + evaluation matrix + simulation. Cite Plan B/C/D as the evidence base.
3. **What we learned** — the three structural findings (market scale-invariance, coop village-ceiling, civic all-fail OR the civic diagnostic finding). These are the pitch's load-bearing claims.
4. **The ask** — pilot program structure. Propose a 2-3 year pilot in 1-2 towns, testing 3-5 of the catalog's highest-confidence designs, with measurable outcomes. Budget envelope: $250k-$2M (spec §11.5 target).
5. **What success looks like** — mirror spec §11.1-11.3: validated hypothesis, scientific null as acceptable success, failure definition.
6. **Appendix: catalog excerpt** — point at specific entries as evidence; summarize top 3 per lens.

### Required sections (beyond the spec's list, for pitch integrity)

7. **Strongest honest objection + response** (per spec §11 P-6 skeptical-funder framing): the one thing a skeptical funder would challenge — and the honest response. E.g., "commodity smithing is dead; your catalog doesn't address it. Response: correct; we target repair + specialty + coop/civic niches explicitly per DECLINE-VERDICT."
8. **Competitor counter-move** — what would industrial competitors do if this pilot succeeded? (likely: nothing — these niches don't threaten them)

### Style

Persuasive but rigorous (STYLE-GUIDE §7 "persuasive but rigorous"). NOT marketing speak. Numbers over adjectives.

Target length: 2500-4500 words.

### Commit

```bash
git add playbook/pitch/PITCH-NARRATIVE.md
git commit -m "Plan E task 5: pitch narrative (smithing vertical slice)"
```

---

## Task 6 — Cross-Artifact Review

**Files:**
- Create: `reviews/PLAN-E-REVIEW.md`

Run a panel-style review on the 4 Plan E artifacts (3 playbooks + pitch). Focus:
- P-5 Historian: anti-romanticism check; decline-verdict citations accurate
- P-6 Skeptical Funder: is the pitch fundable? What objection would kill it?
- P-1 Market / P-2 Commons / P-3 Civic: do the playbook recommendations align with their lens rules?
- Cross-doc consistency: do the 3 playbooks + pitch tell the same story?

Produce findings list (P1/P2/P3). Fix any P1s in a follow-up (or skip fixes if closeout is the next call).

### Commit

```bash
git add reviews/PLAN-E-REVIEW.md
git commit -m "Plan E task 6: cross-artifact review of playbooks + pitch"
```

---

## Task 7 — Closeout

**Files:**
- Update: `plans/2026-04-19-plan-e-playbook.md` frontmatter (status: completed)
- Update: `TRACKER.md`
- Update: `plans/README.md`
- **Critical:** Update `specs/2026-04-18-ceres-design.md` §11 success-criteria check — has the vertical slice met its definition-of-done per spec §10?

### Spec DoD check

From spec §10, the smithing vertical slice is complete when:
- ✅ `research/trades/smithing/REQUIREMENTS.md` written
- ✅ `research/cultures/*/smithing.md` × 4-6
- ✅ `catalog/smithing/SCHEMA.md` finalized
- ✅ `catalog/smithing/entries/*.md` × ~15
- ✅ `corpus/program/ECONOMIC-LENSES.md` three lens rules formalized
- ✅ `simulations/tier-a-comparator/` all 135 cells evaluated
- ✅ `simulations/tier-b-system-dynamics/` scaffolded only
- ✅ `playbook/smithing/{village,town,small-city}.md` three files (Plan E Tasks 2-4)
- ✅ `playbook/pitch/PITCH-NARRATIVE.md` first draft (Plan E Task 5)

Plan E closes the vertical slice. TRACKER Section 7 should record this as a major milestone.

### Commit

```bash
git add TRACKER.md plans/
git commit -m "Plan E task 7: closeout + vertical-slice DoD complete"
```

---

## Retrospective: Risks (upfront)

- **Civic-lens diagnostic may reveal formula bug.** If so, re-running sim invalidates the Plan D SUMMARY — acceptable but visible. Document the delta clearly.
- **Playbook may read as promotional if authoring drifts.** STYLE-GUIDE §7 "clear directive voice" is the discipline; cite specific entries + verdicts as evidence, avoid adjectives.
- **Pitch narrative carries the project's most visible claim.** P-6 skeptical-funder audit will be rigorous. Expect revision cycles.
- **The matrix findings imply a narrower success envelope than the spec's hypothesis.** The pitch must honestly frame this (market path = 7 of 15 designs, capital-driven; coop path = village-inaccessible; civic = TBD after diagnostic). This is the scientific null → success pathway per spec §11.2.

## Failure Modes

- **If civic diagnostic reveals formula bug but fix is non-trivial:** publish the bug + proposed fix in the diagnostic doc; flag Plan F to implement; proceed with playbook/pitch using current results + caveat.
- **If playbook cannot identify enough winning designs per scale:** the vertical-slice catalog may not have spanned the design space as intended; flag for Plan F (Phase 2 catalog expansion) and write an honest "sparse" playbook.
- **If pitch fails a P-6 skeptical-funder simulated review:** loop through revision before committing.

## Handoff

When Plan E completes:
- Vertical slice (Phase 1-5 for smithing) is formally complete per spec §10
- Pitch narrative is ready for external circulation (subject to final author review)
- Project can now: (a) expand to a second trade (Plan F?), (b) run Tier B/C simulations, (c) seek actual funding, or (d) stabilize as a publishable research artifact.
