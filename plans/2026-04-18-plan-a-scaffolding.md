---
id: plan-a-scaffolding
name: Scaffolding and Framework Docs
description: Non-trade-specific infrastructure every downstream plan depends on
status: completed
completed: 2026-04-19
last_modified: 2026-04-19
version: "1.1"
created: 2026-04-18
phase: 0
subsystem: scaffolding
trade: null
depends_on: []
blocks: [plan-b-research-smithing, plan-c-catalog-smithing, plan-d-sim, plan-e-playbook]
estimated_effort: 1-2 weeks focused, 2-3 weeks part-time
primary_artifact_type: framework-docs
success_signal: >
  All trade-agnostic framework files exist with cited content and no TODO/TBD
  placeholders. A reader unfamiliar with CERES can open the repo and
  understand what the project is, how it works, and where every artifact
  type lives.
spec: specs/2026-04-18-ceres-design.md
---

# Plan A: Scaffolding and Framework Docs

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create the trade-agnostic framework files every downstream plan depends on.

**Architecture:** Authoring-heavy, not code-heavy. Produces markdown documents that define conventions (CLAUDE.md, STYLE-GUIDE, METHODOLOGY, PIPELINE), framework content (THEORY, GLOSSARY, PRINCIPLES), lens parameters (SCALES, CURRENCIES, ECONOMIC-LENSES definitions), the canonical catalog-entry schema, the quality rubric, a status dashboard, and directory scaffolding for downstream plans.

**Tech Stack:** Markdown, YAML frontmatter. No code in this plan. Code starts in Plan D.

**Source of truth:** `specs/2026-04-18-ceres-design.md`. Every content requirement in this plan traces back to a spec section. When spec and plan disagree, the spec wins — flag the discrepancy.

**Commit cadence:** One commit per task (one file per task). Keeps history legible and lets Plan B/C/D/E authors cherry-pick or review individual foundation docs.

---

## Task Index

| # | Task | Creates |
|---|---|---|
| 1 | Project house rules | `CLAUDE.md` |
| 2 | Directory skeleton with README stubs | `research/`, `catalog/`, `simulations/`, `playbook/`, `agents/`, `sources/` — each with a README |
| 3 | Project entry README | `README.md` |
| 4 | Status dashboard | `TRACKER.md` |
| 5 | Style guide | `docs/STYLE-GUIDE.md` |
| 6 | Methodology | `docs/METHODOLOGY.md` |
| 7 | Pipeline | `docs/PIPELINE.md` |
| 8 | Glossary | `corpus/canon/GLOSSARY.md` |
| 9 | Theory | `corpus/canon/THEORY.md` |
| 10 | Principles | `corpus/canon/PRINCIPLES.md` |
| 11 | Currencies | `corpus/program/CURRENCIES.md` |
| 12 | Scales | `corpus/program/SCALES.md` |
| 13 | Economic lenses (definitions) | `corpus/program/ECONOMIC-LENSES.md` |
| 14 | Validation | `corpus/program/VALIDATION.md` |
| 15 | Catalog schema (canonical) | `catalog/SCHEMA.md` |
| 16 | Scoring rubric | `scoring/RUBRIC.md` |
| 17 | Plans index | `plans/README.md` |

Per-task structure: create file → write content per outline → self-review for placeholders / unresolved refs / contradictions with neighbors → commit.

---

### Task 1: Project House Rules

**Files:**
- Create: `CLAUDE.md`

Required sections:

1. **Project identity** — one paragraph. CERES = Local Production Atlas. Named for CeCe (chicken) and Ceres (Roman goddess). Sibling projects (LUCIA, FELICE/RMM, MAXIM).
2. **Directory conventions** — `specs/`, `plans/`, `research/`, `catalog/`, `corpus/`, `simulations/`, `playbook/`, `.roles/`, `skills/`, `reviews/`, `scoring/`, `sources/`, `TRACKER.md`. One line per. Never use `docs/superpowers/...` — user preference.
3. **Quality bar** — research-paper-level estimates, every number cited, no supplier BOMs.
4. **Authoring discipline** — markdown with YAML frontmatter for catalog entries and plans. Match existing patterns. Don't invent schema fields; amend `catalog/SCHEMA.md` if the schema needs to change.
5. **Review tiers** — `.roles/panel/` (6 voices, every artifact), `.roles/editorial/` (3 voices, validated-promotion gate), `.roles/board/` (per-trade, on-demand). Point at `.roles/ROLE.md`.
6. **Review skills** — point at `skills/ceres-panel/`, `skills/ceres-editorial/`, `skills/ceres-board/`.
7. **Scope discipline** — keep artifacts in their box; if an artifact grows beyond its spec scope, propose a spec amendment (don't silently expand).
8. **Sibling project references** — LUCIA at `C:\src\chronicle`, FELICE/RMM at `C:\src\rmm`, MAXIM at `C:\src\reference`. Cite MAXIM for domain material; don't duplicate.

Self-review:
- No forward references to docs that don't exist yet (or flag them as "upcoming").
- Consistent with spec Section 1 (Project Identity) and Section 4.2 (directory structure).

Commit:
```bash
git add CLAUDE.md
git commit -m "Plan A task 1: add project house rules (CLAUDE.md)"
```

---

### Task 2: Directory Skeleton with README Stubs

**Files (all new, one-line READMEs explaining "this directory is populated by plan X"):**
- Create: `research/README.md`
- Create: `research/cultures/README.md`
- Create: `research/trades/README.md`
- Create: `catalog/README.md`
- Create: `simulations/README.md`
- Create: `simulations/tier-a-comparator/README.md`
- Create: `simulations/tier-b-system-dynamics/README.md`
- Create: `simulations/tier-c-agent-based/README.md`
- Create: `playbook/README.md`
- Create: `playbook/pitch/README.md`
- Create: `agents/README.md`
- Create: `sources/README.md`

Content per stub: one paragraph stating (a) what this directory holds, (b) which plan populates it, (c) one-line schema/convention pointer.

Example (`research/README.md`):
```markdown
# research/

Phase 1 artifacts: functional requirements for each trade, extracted from
historical forms across anchor cultures.

- `cultures/` — anchor-culture chapters (per-trade)
- `trades/` — per-trade REQUIREMENTS / HISTORICAL-FORMS / SOURCES

Populated by Plan B (smithing) and parallel plans for later trades.
```

Self-review:
- Each stub names the right plan.
- Tree matches spec Section 4.2.

Commit:
```bash
git add research/ catalog/README.md simulations/ playbook/ agents/README.md sources/README.md
git commit -m "Plan A task 2: scaffold directory skeleton with README stubs"
```

---

### Task 3: Project Entry README

**Files:**
- Create: `README.md` (repo root)

Required sections:

1. **Project name + tagline** — CERES — Local Production Atlas
2. **What this is** — one paragraph: catalog-driven design of modern artisan-production equipment evaluated under market/coop/civic lenses across village/town/small-city scales, testing whether historical local production can be restored.
3. **Named after** — CeCe (chicken, alive) + Ceres (Roman goddess, not alive). Tie to sibling-project naming: LUCIA from Lucy, FELICE from Felix.
4. **Project sections** — quick-links to `specs/`, `plans/`, `.roles/`, `skills/`, `corpus/canon/THEORY.md`, `catalog/SCHEMA.md`, `TRACKER.md`.
5. **Status** — "Early-stage. Phase 1 (smithing vertical slice) in progress."
6. **Author + credit line** — Giovanni Della-Libera; developed with Claude Opus 4.7 (1M context); started 2026-04-18.

Self-review:
- Every linked path exists (or will exist by end of Plan A).
- Consistent with spec Section 1.

Commit:
```bash
git add README.md
git commit -m "Plan A task 3: add project entry README"
```

---

### Task 4: Status Dashboard

**Files:**
- Create: `TRACKER.md`

Required sections:

1. **Current phase** — which plan is in flight; which trade's vertical slice.
2. **Plan status table** — rows for Plans A-E, columns: status, owner, ETA, notes. Pull status from each plan's frontmatter.
3. **Vertical slice progress (smithing)** — one row per Section-10 deliverable (the 9 from the spec's DoD table), with status column.
4. **Panel review queue** — artifacts awaiting or in review.
5. **Editorial promotion queue** — artifacts awaiting the 3-lens validated-promotion gate.
6. **Board consult queue** — contested domain claims awaiting board review.
7. **Recent findings / decisions** — date-stamped list of notable findings (e.g., "2026-04-18: panel R1 on spec surfaced schema gaps → spec v0.2 addressed themes 1 + 3").

Self-review:
- All section counts match current repo reality.
- No plan status inconsistent with its frontmatter.

Commit:
```bash
git add TRACKER.md
git commit -m "Plan A task 4: add status dashboard (TRACKER.md)"
```

---

### Task 5: Style Guide

**Files:**
- Create: `docs/STYLE-GUIDE.md`

Required sections (drawn from spec Section 1 quality bar + panel R1 P-5 review):

1. **Quality bar** — research-paper level; every number cited; ranges labeled as ranges; estimates labeled as estimates.
2. **Citation format** — inline `[Author YEAR, short-ref]` with a `sources:` block in frontmatter (catalog entries) or a `## Sources` section (research docs). Include page / section when available. Prefer primary sources over third-hand blog summaries.
3. **Tone** — analytical first, narrative second (per spec Section 12 non-goal #3). Avoid political advocacy framing. Don't romanticize pre-industrial life.
4. **Forbidden framings** — anti-romanticism list (from P-5 historian review of spec): no "in the good old days"; no implicit assumption that pre-industrial life was sustainable; no elision of household/apprentice labor regimes; no guild-as-craft-quality-only framing; no "lost knowledge" claims without specific documentation.
5. **Multi-currency conventions** — catalog entries declare `currency`; prose uses the declared currency without conversion; cross-currency comparison lives only in simulation output.
6. **Unit conventions** — SI for physical (m, kg, kWh); explicit per-unit for throughput (e.g., "small_work unit equivalent"); explicit timeframes on rates (per-hour, per-week, per-year).
7. **Voice and point-of-view** — catalog entries in neutral technical voice; playbook files in clear directive voice; pitch narrative in persuasive but rigorous voice (not marketing speak).

Self-review:
- Every rule is specific enough to be enforced mechanically by E-2 / E-3.
- Cross-check with spec Section 12 non-goals.

Commit:
```bash
git add docs/STYLE-GUIDE.md
git commit -m "Plan A task 5: add style guide"
```

---

### Task 6: Methodology

**Files:**
- Create: `docs/METHODOLOGY.md`

Required sections:

1. **How we estimate** — order-of-magnitude with ranges; cite source for each number; flag high-uncertainty with `high` / `mid` / `low` triples (per catalog schema).
2. **Estimate defense standard** — an estimate is defensible if a reader can reach the source and the source supports the claim. Uncited estimate = P1 editorial finding.
3. **Sanity-check conventions** — for unit economics: payback cross-check, throughput-vs-labor consistency, order-of-magnitude comparison to known parallels. These are the E-3 numeracy-checker's working rules.
4. **Multi-currency normalization** — process for evaluating entries authored in different currencies; FX snapshot table in `corpus/program/CURRENCIES.md`; snapshot-date matters.
5. **Historical claims** — require citation to serious economic-history or primary-source literature. Popular-press or Wikipedia-only citations = P1 editorial finding for any load-bearing claim.
6. **Research-paper level vs due-diligence level** — project is explicitly not due-diligence; numbers are intended to inform decisions, not to book procurement. Restate spec Section 12 non-goal.
7. **Handling disagreement across anchor cultures** — when functional requirements diverge across cultures (e.g., coal vs charcoal vs wood forges), document the divergence rather than collapsing to a consensus.

Self-review:
- Consistent with spec Section 8 (Validation) and Section 12 (Non-Goals).
- Gives E-1 / E-3 concrete rules to enforce.

Commit:
```bash
git add docs/METHODOLOGY.md
git commit -m "Plan A task 6: add methodology"
```

---

### Task 7: Pipeline

**Files:**
- Create: `docs/PIPELINE.md`

Required sections:

1. **5-phase overview** — Research → Catalog ★ → Evaluation Matrix → Simulation → Playbook + Pitch. One paragraph each linking to the artifacts each phase produces.
2. **Per-phase workflow** — for each phase: inputs, outputs, review tiers that fire, promotion criteria.
3. **Review-tier firing rules** (from `.roles/ROLE.md` "When Each Tier Fires" table): panel on every artifact; editorial on validated-promotion; board on demand.
4. **Catalog-entry lifecycle** — `draft` → panel review R1 → revise → panel review R2 (if needed) → editorial 3-lens pass → `validated` (or held / deprecated).
5. **Spec-amendment pathway** — if an artifact needs content the spec doesn't authorize, don't silently expand — open a short amendment to the spec and link it from the artifact.
6. **Simulation tier escalation** — Tier A runs on every cell; Tier B requires ≥2 trades; Tier C is targeted.
7. **Pipeline diagram** — ASCII block diagram showing phase flow + feedback loop (from spec Section 4.1).

Self-review:
- Matches spec Section 4.1 (Architecture), Section 7 (Simulation Tiers), Section 10 (Phase-1 DoD).
- Cross-checked against `.roles/ROLE.md` firing table.

Commit:
```bash
git add docs/PIPELINE.md
git commit -m "Plan A task 7: add pipeline workflow guide"
```

---

### Task 8: Glossary

**Files:**
- Create: `corpus/canon/GLOSSARY.md`

Required terms (alphabetical; each entry 1-3 sentences):

- **Anchor culture** — one of the 4-6 historical cultures whose forms inform functional-requirements extraction.
- **Break-even (cooperative)** — the member-count threshold at which coop dues + shared labor cover total costs.
- **Catalog entry** — a single markdown file under `catalog/<trade>/entries/` describing one equipment design per the canonical schema.
- **Civic lens** — viability evaluation under municipal / library / fire-dept mental model; per-household cost and per-capita utilization as metrics.
- **Cooperative lens** — viability evaluation under member-ownership / commons model; governance structure required.
- **Everyday trade** — trade producing essential goods at inelastic demand (bread, meat, cloth, tools).
- **Evaluation matrix** — 3 scales × 3 economic lenses = 9 contexts applied to each catalog entry.
- **Falsifier** — a specific condition under which CERES's working hypothesis (Section 2) is invalidated. Four pre-registered: demand collapse, regulatory capture, labor-regime dependency, supply-chain disappearance.
- **Functional requirement** — a trade-specific capability that any design must achieve (e.g., "forge must reach 1100°C sustained for forge-welding").
- **Lens** — one of market / cooperative / civic; each scores an entry's viability under different rules.
- **Local production** — production of goods for local consumption by operators living in the same town or region.
- **Market lens** — viability evaluation under private-profit model; payback and operator take-home as metrics.
- **Operations reality** — catalog-entry frontmatter block capturing first-year failures, consumables lead-time, throughput variance, operator impact.
- **Playbook** — per-trade, per-scale markdown file naming winning catalog entries and an implementation sketch.
- **Scale** — one of village (500–2,000), town (2,000–15,000), small-city / district (15,000–75,000).
- **Specialty trade** — trade producing low-volume, elastic-demand goods (armory-grade metalwork, tapestries, fine ceramics, bespoke garments).
- **Tier A / B / C simulation** — scenario comparator / system dynamics / agent-based, in increasing fidelity and cost.
- **Validated** — catalog-entry promotion status after panel + editorial review passes.
- **Vertical slice** — first pass of the full pipeline on one trade (smithing), producing all five phase artifacts as a template for subsequent trades.
- **Working hypothesis** — spec Section 2 claim under test: equipment redesign is the binding constraint for restoring local production.

Self-review:
- Every term referenced elsewhere in framework docs appears here.
- Definitions consistent with how terms are used in the spec and role files.

Commit:
```bash
git add corpus/canon/GLOSSARY.md
git commit -m "Plan A task 8: add canonical glossary"
```

---

### Task 9: Theory

**Files:**
- Create: `corpus/canon/THEORY.md`

Required sections:

1. **Working hypothesis** — state spec Section 2 working hypothesis verbatim (or near-verbatim) + four falsifiers + pivot criteria.
2. **Why equipment** — one paragraph on why the equipment redesign frame is worth testing: equipment is a clear, addressable, fundable lever; demand/regulatory/labor levers are harder and slower.
3. **Three economic lenses as parallel viability frames** — brief; formal math in `ECONOMIC-LENSES.md`.
4. **Three scales as first-class variable** — brief; parameters in `SCALES.md`.
5. **Catalog as living artifact** — designs iterate; failed entries stay with `status: deprecated`; the catalog is the evidence for the hypothesis, not a recommendation list.
6. **Relationship to historical precedent** — historical forms inform *functional requirements*, not adopted templates. Modern designs carry forward the function, not the form. Per spec Section 11 / sibling MAXIM citation pattern.
7. **Success vs. null vs. failure** — mirror spec Section 11.1-11.3.

Self-review:
- Every claim traceable to a spec section.
- Doesn't introduce new concepts not in the spec or glossary.

Commit:
```bash
git add corpus/canon/THEORY.md
git commit -m "Plan A task 9: add theory document"
```

---

### Task 10: Principles

**Files:**
- Create: `corpus/canon/PRINCIPLES.md`

Required sections — what makes a "good" catalog entry:

1. **Schema-complete** — every required frontmatter field populated per `catalog/SCHEMA.md`.
2. **Every number cited** — source in `sources:` block; in-text `[Author YEAR]` where useful.
3. **Operations reality addressed** — first-year failures named; consumables lead-time stated; throughput variance modeled; operator impact described. (per Panel R1 / P-4)
4. **Lens context addressed** — if `lens_fit.cooperative: good | marginal`, governance sketch present; if `lens_fit.civic: good | marginal`, political-coalition and competition-with-private notes present. (per Panel R1 / P-2 and P-3)
5. **Market price declared** — if `lens_fit.market: good | marginal`, `economics.market_price_per_unit` populated and defensible. (per Panel R1 / P-1)
6. **Historical lineage honest** — inspirations cited; function-vs-form distinction respected; anti-romantic. (per Panel R1 / P-5)
7. **Design rationale explicit** — the problem this entry solves that no other entry does. Avoid catalog bloat: redundant entries get merged or deprecated.
8. **Failure modes named** — regulatory, labor pipeline, supply chain; not buried.
9. **Apprentice path** — entries that have no apprentice path are flagged; operator-succession is first-class.
10. **Iteration log** — dated notes as the entry evolves.

Self-review:
- Each principle maps to a panel-voice concern + an editorial-gate finding type.
- Principles are enforceable (scoring rubric will reference them).

Commit:
```bash
git add corpus/canon/PRINCIPLES.md
git commit -m "Plan A task 10: add canonical principles"
```

---

### Task 11: Currencies

**Files:**
- Create: `corpus/program/CURRENCIES.md`

Required sections:

1. **Base currency** — USD for sim-normalization (pick once, state it).
2. **FX snapshot table** — columns: currency, USD per 1 unit, snapshot date, source. Populate with: USD, EUR, GBP, JPY, CAD, AUD, CHF, CNY, INR, MXN, BRL, ZAR. Use a single snapshot date (e.g., 2026-04-18) and name the source (ECB reference rates, OECD, or similar — cite).
3. **Update cadence** — document when rates get re-snapshotted (e.g., quarterly; or when any catalog entry uses a new currency); track snapshot history as an appendix.
4. **Normalization rule** — sim converts all amounts to base currency using the snapshot-date rate; prose keeps the declared currency.
5. **Ambiguity handling** — historical cost data cited in pre-2020 currencies is brought forward via CPI + FX; cite the CPI series used.

Self-review:
- Table parses as markdown; numbers traceable to cited source.
- Consistent with spec Section 5 multi-currency note.

Commit:
```bash
git add corpus/program/CURRENCIES.md
git commit -m "Plan A task 11: add currency FX table and normalization rule"
```

---

### Task 12: Scales

**Files:**
- Create: `corpus/program/SCALES.md`

Required sections:

1. **Three scales** — village (500–2,000), town (2,000–15,000), small-city/district (15,000–75,000). Population definitions from spec Section 3.
2. **Per-scale parameters table** — columns: scale, population range, households (pop × 0.4 typical), scale-appropriate median wage (USD, cited; use US BLS ACS-style breakdown), per-household civic-cost threshold for passing CIVIC lens, feasible member-pool size as % of population (for passing COOP lens), local supplier density assumption (thin / moderate / dense).
3. **Median-wage thresholds** — the MARKET lens passes only if operator take-home ≥ this threshold. State dollar value + cite.
4. **Civic cost thresholds** — the CIVIC lens passes only if per-household annual cost ≤ this threshold. State dollar value + cite (library-per-capita cost as a benchmark; ALA data).
5. **Feasible member-pool formulas** — member pool at a scale is population × participation_rate. Document the participation rate used (e.g., 2-5%) and cite tool-library/coop literature.
6. **Geographic assumptions** — developed-economy settlement; one or more neighboring settlements within 30-minute drive (affects supplier density and labor pool).
7. **Non-goals** — not a precise demographic model; numbers are order-of-magnitude for sim parameters.

Self-review:
- Every threshold has a source.
- Numbers sanity-checkable against published library/municipal budgets.

Commit:
```bash
git add corpus/program/SCALES.md
git commit -m "Plan A task 12: add scale parameters and lens thresholds"
```

---

### Task 13: Economic Lenses (Definitions)

**Files:**
- Create: `corpus/program/ECONOMIC-LENSES.md`

Required sections:

1. **Three lenses overview** — market / cooperative / civic. Each evaluates the same catalog entry under different viability rules.
2. **MARKET lens** — inputs (capital, annual costs, throughput, market_price_per_unit, cost_of_capital), outputs (payback years, ROI, operator annual take-home after wage), pass condition (payback ≤ 8 years AND operator earns ≥ scale-appropriate median wage from `SCALES.md`).
3. **COOPERATIVE lens** — inputs (capital split N members, member dues, shared labor, governance from `lens_context.cooperative`), outputs (break-even member count, per-member contribution, utilization), pass condition (break-even member count ≤ feasible member pool at that scale from `SCALES.md`).
4. **CIVIC lens** — inputs (capital amortized 25-40 years, tax cost per resident, public use hours, `lens_context.civic`), outputs (per-household annual cost, hours-of-use per capita), pass condition (per-household cost ≤ scale threshold from `SCALES.md` AND usage rate ≥ scale threshold).
5. **Verdict states** — `win` / `marginal` / `fail` per cell. Definitions: `win` = clear pass with ≥20% margin; `marginal` = passes with <20% margin OR relies on optimistic assumptions; `fail` = does not pass.
6. **Primary numeric metric per lens** — what number to record alongside the verdict (payback years / break-even members / per-household cost).
7. **Deferrals** — formal mathematical expression lives in Plan D's sim code; this doc defines the rules, not the implementation.

Self-review:
- Consistent with spec Section 6 and with the corrected MARKET lens "scale-appropriate median wage" language (spec v0.2).
- Sub-components (thresholds, member-pool) reference `SCALES.md` correctly.

Commit:
```bash
git add corpus/program/ECONOMIC-LENSES.md
git commit -m "Plan A task 13: add economic lens definitions"
```

---

### Task 14: Validation

**Files:**
- Create: `corpus/program/VALIDATION.md`

Required sections (skeleton; Plan D fleshes out simulation-output validation):

1. **Validation philosophy** — sim outputs must be sanity-checkable against known real-world parallels; uncheckable outputs are untrustworthy.
2. **Catalog-entry validation** — editorial (E-1/E-2/E-3) gates promotion to `validated`. Cross-reference `skills/ceres-editorial/SKILL.md`.
3. **Sim-output validation (Tier A)** — cross-check each catalog entry's 9-cell `results:` against: (a) comparable real-world operation (if known), (b) internal consistency (E-3 cross-checks), (c) order-of-magnitude sniff test.
4. **Known-parallel case studies** — list (to be populated by Plan D): real microbakery economics, real community-forge coop cases, real library per-capita cost benchmarks. These are the sanity-check anchors.
5. **Failure flagging** — sim results that fail a sanity check are marked and flagged for re-review, not silently accepted.
6. **Deferrals** — specific test cases and procedures land in Plan D alongside sim code.

Self-review:
- Consistent with spec Section 8 (Validation Strategy).
- Skeleton is honest — flags what Plan D will expand.

Commit:
```bash
git add corpus/program/VALIDATION.md
git commit -m "Plan A task 14: add validation framework skeleton"
```

---

### Task 15: Catalog Schema (Canonical)

**Files:**
- Create: `catalog/SCHEMA.md`

This file is the **canonical** schema. The spec's Section 5 shows an example; this file is the authoritative specification. The two must match; if the spec changes, this file updates, and vice versa (with a spec amendment). Trade-specific extensions (smithing-specific `throughput` sub-structure) go in `catalog/<trade>/SCHEMA.md` and extend this base.

Required sections:

1. **Purpose** — one paragraph: what a catalog entry is, how it's used, why schema matters.
2. **File layout** — one markdown file per entry under `catalog/<trade>/entries/{id}-{slug}.md`. YAML frontmatter + prose sections.
3. **Full YAML frontmatter schema** — exactly as in spec v0.2 Section 5 (post-revision), with all fields documented:
   - Identity: `id`, `trade`, `name`, `tagline`, `status`, `version`, `supersedes`, `inspirations`
   - Physical envelope: `footprint_m2`, `ceiling_min_m`, `ventilation`
   - Energy: `energy_source`, `energy_consumption_per_active_hour`, `backup_fuel`
   - Throughput: `throughput:` (per-trade sub-structure)
   - Operator: `operator_skill_floor`, `operators_concurrent`, `apprentice_friendly`
   - Economics: `economics:` (with `currency`, `capital_cost`, `install_cost`, `annual_maintenance`, `annual_consumables`, `floor_space_rent_per_year`, `market_price_per_unit`, `pricing_notes`)
   - Operations reality: `operations_reality:` (with `first_year_failures[]`, `consumables_lead_time_days`, `throughput_variance`, `operator_impact`)
   - Regulatory: `regulatory_notes:` (three-line cap)
   - Context fit: `lens_fit:`, `scale_fit:`
   - Lens context: `lens_context.cooperative:` (conditional — required when lens_fit.cooperative in {good, marginal}), `lens_context.civic:` (conditional — required when lens_fit.civic in {good, marginal})
   - Sim params: `sim_params:` (flat numeric block for sim code)
   - Results: `results:` (9 cells, start null)
   - Sources: `sources[]`
4. **Required vs optional fields** — table listing each field as required / conditional / optional.
5. **Prose sections** — Summary / Design rationale / Historical lineage / Key assumptions / Known risks / Iteration log. One-paragraph target per section.
6. **Field semantics** — for each non-obvious field, one-sentence definition (e.g., "operator_skill_floor: apprentice | journeyman | master; the minimum competence level that can safely operate this equipment at rated throughput").
7. **Validation rules** — which fields are required under which conditions; errors E-1/E-3 catch (missing conditional field, inconsistent sim_params, uncited market_price_per_unit).
8. **Extending per trade** — if a trade needs fields not in this base (e.g., a fermentation schedule for brewing), add them under `trade_specific:` namespace and document in `catalog/<trade>/SCHEMA.md`.
9. **Versioning** — if this schema changes, bump its own version in its frontmatter and require all existing entries to be re-validated under the new version.

Self-review:
- Matches spec v0.2 Section 5 exactly (no invented fields; no missing fields).
- `lens_context` conditional requirements match the lens-context memo from P-2/P-3 panel feedback (now in spec).

Commit:
```bash
git add catalog/SCHEMA.md
git commit -m "Plan A task 15: add canonical catalog-entry schema"
```

---

### Task 16: Scoring Rubric

**Files:**
- Create: `scoring/RUBRIC.md`

Required sections:

1. **Purpose** — scoring is separate from panel review; panel voices give qualitative feedback, rubric scoring produces a number for promotion decisions.
2. **Scoring scale** — 100-point composite across six dimensions.
3. **Dimensions and weights** (each weight sums to 100):
   - Schema completeness (15)
   - Citation strength (20) — ties to E-1
   - Operations realism (15) — ties to P-4
   - Lens-context rigor (20) — ties to P-2 / P-3
   - Historical honesty (10) — ties to P-5
   - Design rationale & differentiation (20) — ties to P-6 / design-novelty
4. **Per-dimension rubric anchors** — 0-25 / 26-50 / 51-75 / 76-100 descriptors per dimension.
5. **Promotion thresholds** — draft → reviewed: composite ≥ 60; reviewed → validated: composite ≥ 80 AND all editorial gates pass; below 60 = back to draft with revision notes.
6. **Rubric evolution** — when an artifact clearly exceeds the rubric (exemplary work), document what made it special and raise the bar. Ties to Chronicle's "evolving quality" pattern.

Self-review:
- Dimensions map to panel voices + editorial gates without orphans.
- Thresholds are defensible and not arbitrary.

Commit:
```bash
git add scoring/RUBRIC.md
git commit -m "Plan A task 16: add scoring rubric"
```

---

### Task 17: Plans Index

**Files:**
- Create: `plans/README.md`

Required sections:

1. **Purpose of the plans directory** — implementation plans for CERES, one per subsystem.
2. **Plan frontmatter convention** — full documented schema:

```yaml
---
id: plan-{letter}-{slug}         # plan-a-scaffolding, plan-b-research-smithing, ...
name: {human-readable title}
description: {one-line summary}
status: draft | in_progress | completed | deferred | superseded
version: "X.Y"
created: YYYY-MM-DD
phase: 0 | 1 | 2 | 3 | 4 | 5     # 0 = infra, 1-5 = CERES pipeline phases
subsystem: scaffolding | research-corpus | catalog | simulation | playbook
trade: null | smithing | baking | ...
depends_on: [plan-id, ...]
blocks: [plan-id, ...]
estimated_effort: "{duration}"
primary_artifact_type: framework-docs | research | catalog | code | playbook
success_signal: >
  {one or two sentences describing done}
spec: {path to authoring spec}
---
```

3. **Current plan index** — table with columns: id, name, status, phase, trade, depends_on, success_signal. Rows: Plan A (this plan), Plan B (research — smithing), Plan C (catalog — smithing), Plan D (sim), Plan E (playbook).
4. **How to add a new plan** — file-name convention `YYYY-MM-DD-plan-{letter}-{slug}.md`; populate full frontmatter; update upstream plans' `blocks:` arrays; add row to the index table.
5. **Status flow** — draft → in_progress → completed. `deferred` means accepted-but-parked; `superseded` means replaced by another plan (link in body).
6. **Relationship to `TRACKER.md`** — the plans index shows plan-level status; TRACKER.md shows finer-grained artifact progress.

Self-review:
- Frontmatter schema matches Plan A's own frontmatter exactly.
- Index entries match frontmatter on each plan (when they exist — B/C/D/E are forthcoming, so their index rows describe intent not current state).

Commit:
```bash
git add plans/README.md
git commit -m "Plan A task 17: add plans index and frontmatter convention"
```

---

## Final Self-Review (after Task 17)

Run these checks before declaring Plan A complete:

- [ ] Every framework file referenced in the spec (Section 4.2 directory structure) exists or has a README stub pointing at the plan that creates it.
- [ ] `CLAUDE.md` forbids `docs/superpowers/...` paths.
- [ ] No file contains TODO / TBD / "implement later" placeholders.
- [ ] `GLOSSARY.md` defines every term used in `THEORY.md`, `PRINCIPLES.md`, `ECONOMIC-LENSES.md`, `SCALES.md`, `VALIDATION.md`, `SCHEMA.md`, `RUBRIC.md`.
- [ ] `SCHEMA.md` matches spec v0.2 Section 5 (all fields present, all conditional requirements captured).
- [ ] `ECONOMIC-LENSES.md` uses the corrected "scale-appropriate median wage" language (not "local median wage").
- [ ] `TRACKER.md` reflects Plan A's actual state (completed when done).
- [ ] `plans/README.md` frontmatter schema matches this plan's frontmatter.
- [ ] Spec is unchanged (this plan implements, not amends, the spec).

## Retrospective: Risks and Assumptions (added 2026-04-19 per P-6 audit)

Plan A is complete (17/17 tasks). This section records what P-6 would have raised at kickoff had it been solicited then. Future plans should open their own equivalent section at authoring time, not retrospectively.

### Risks and Objections

- **Spec stability risk.** The working hypothesis, schema fields, and lens definitions were all live in spec v0.2 during execution. Any mid-plan spec change would have invalidated multiple in-flight tasks simultaneously (SCHEMA.md, ECONOMIC-LENSES.md, SCALES.md at minimum).
- **Schema-divergence risk.** Plans B/C/D/E depend on fields defined in `catalog/SCHEMA.md`. If those fields were revised after downstream authors had already drafted entries against the v1.0 schema, silent divergence would accumulate.
- **Authoring-heavy scope risk.** 17 markdown files dispatched as subagent tasks creates cost and consistency pressure. Each file is authored in a separate context; cross-file coherence depends on self-review checklists, not a shared working memory.
- **Premature lock-in risk.** Framework docs authored in one pass may encode early decisions (e.g., field names, threshold values) that would have benefited from iterative refinement against real catalog entries.

### Failure Modes (contingency paths)

- **If spec revises mid-plan:** stop all in-flight tasks, re-ingest the revised spec section, diff against already-authored files, update affected files, then resume. The spec-amendment pathway in `docs/PIPELINE.md` governs this.
- **If schema divergence is discovered** (e.g., Plan C entry schema does not match Plan A canonical): treat as a spec-amendment trigger — open a short amendment, update `catalog/SCHEMA.md`, and re-validate affected entries. Do not patch entries silently.
- **If authoring cost spirals:** switch to reduced-review mode (one self-review pass instead of two), batch commits by logical group rather than one per task, and defer polish to a v1.1 pass after all tasks are drafted.
- **If premature lock-in surfaces:** use the v1.1-style refactor pattern (as applied to `.roles/` when RMM's dynamic-discovery pattern informed a role revision) — add fields, bump the schema version, document migration steps in the schema changelog.

### Assumptions Now Made Explicit

- Spec v0.2 was stable for Plan A's entire duration. This held — no mid-execution spec changes occurred.
- `catalog/SCHEMA.md` is the canonical base schema; trade-specific extensions in `catalog/<trade>/SCHEMA.md` add fields under `trade_specific:` and never override or rename base fields.
- Plans B/C/D/E will adopt the frontmatter convention documented in `plans/README.md` (Task 17 output); they do not define their own competing frontmatter conventions.
- Chronicle/RMM/Marathon patterns will continue to inform CERES evolution (e.g., the v1.1 role refactor absorbed RMM's dynamic-discovery and Marathon's weighted-axes insights). Future spec amendments should cite which sibling-project pattern they are absorbing and why.

---

## Handoff

When this plan is complete:

1. Update `TRACKER.md`: Plan A status → completed.
2. Update this plan's frontmatter: `status: completed`.
3. Plan B (research — smithing) and Plan D (sim) are now unblocked and can begin in parallel. Plan B produces the functional requirements Plan C's catalog needs; Plan D produces the sim code that evaluates catalog entries.
