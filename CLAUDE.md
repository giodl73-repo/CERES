# CERES — House Rules

## 1. Project Identity

CERES is the **Local Production Atlas**: a catalog-driven design and
evaluation project for modern artisan-production equipment — forges,
ovens, looms, kilns, and related trades. Named for CeCe (Giovanni's
chicken) and Ceres (Roman goddess of grain, harvest, and settlement
nourishment). The mission: design equipment that hits price and
operational points enabling towns and small cities to restore meaningful
local production, evaluated under realistic economic conditions and
framed as a fundable-quality plan. Sibling projects: **LUCIA**
(`chronicle` — narrative encyclopedia of human cultures),
**FELICE/RMM** (`rmm` — theoretical framework and simulation),
**MAXIM** (`reference` — encyclopedic knowledge base). CERES is
fully independent — own schema, own playbook, own simulation code —
but borrows structural patterns from siblings and cites MAXIM for
domain material.

---

## 2. Directory Conventions

First-class top-level directories. Never use `docs/superpowers/...` paths.

| Directory / File | Purpose |
|---|---|
| `specs/` | Design specifications. Current: `specs/2026-04-18-ceres-design.md`. |
| `plans/` | Implementation plans. Current: `plans/2026-04-18-plan-a-scaffolding.md`. |
| `research/` | Phase 1 — functional requirements extracted from historical forms, organized by culture and trade. *(upcoming)* |
| `catalog/` | Phase 2 — THE STAR. One markdown file per equipment design. Canonical schema in `catalog/SCHEMA.md`; trade-specific extensions in `catalog/<trade>/SCHEMA.md` (not yet created; see Plan C). |
| `corpus/` | Framework material: `corpus/canon/` (theory, glossary, principles) and `corpus/program/` (lens math, scales, FX table, validation rules). |
| `simulations/` | Phase 4 — layered Tier A (scenario comparator), Tier B (system dynamics), Tier C (agent-based). *(upcoming)* |
| `playbook/` | Phase 5 — per-trade, per-scale winning-designs files and pitch narrative. *(upcoming)* |
| `.roles/` | Review organization. Role definitions in `.roles/`. See Section 5. |
| `agents/` | Chronicle-pattern agent definitions. *(upcoming)* |
| `skills/` | Reusable pipeline skills. See Section 6. |
| `reviews/` | Panel and editorial review outputs. Filenames identify artifact, round, and reviewer. |
| `scoring/` | Quality rubric (`scoring/RUBRIC.md`). |
| `sources/` | Raw citations and images. *(upcoming)* |
| `TRACKER.md` | Project-level progress tracking. |
| `docs/` | Pipeline, style-guide, and methodology docs (`docs/PIPELINE.md`, `docs/STYLE-GUIDE.md`, `docs/METHODOLOGY.md`). |

---

## 3. Quality Bar

- **Research-paper-level estimates.** Order-of-magnitude unit economics with citations.
- **Every number cited.** An uncited number in a catalog entry blocks promotion to `validated`.
- **No supplier BOMs.** No real vendor quotes, no due-diligence-grade procurement plans.
  Conceptual design specs only.
- **No hand-waving on economics.** If a lens result is `marginal` or `fail`, say so and explain why.

---

## 4. Authoring Discipline

- **Markdown with YAML frontmatter** for all catalog entries and plans. Simulation code
  ingests catalog frontmatter directly — malformed YAML breaks the pipeline.
- **Match existing patterns.** Read `catalog/SCHEMA.md` before authoring any
  catalog entry. Trade-specific fields are defined in `catalog/<trade>/SCHEMA.md`. Read
  an existing entry before authoring the next one.
- **Don't invent schema fields.** If a new trade-agnostic field is needed, amend
  `catalog/SCHEMA.md` and document the change. Trade-specific fields go in
  `catalog/<trade>/SCHEMA.md`. Silent additions break simulation ingestion.
- **Status lifecycle:** `draft` → `reviewed` → `validated` → (`deprecated` | `superseded`).
  Deprecated entries stay in the catalog, linked to what replaced them.
- **Multi-currency:** declare `currency:` in every entry. FX conversion uses
  `corpus/program/CURRENCIES.md`. Do not normalize manually.

---

## 5. Review Tiers

Role definitions: `.roles/ROLE.md`

| Tier | Voices | When |
|---|---|---|
| **Panel** (`.roles/panel/`) | 6 permanent — P-1 Market Economist, P-2 Commons Theorist, P-3 Civic Steward, P-4 Craft Practitioner, P-5 Historian, P-6 Skeptical Funder | Every artifact: spec, plan, catalog entry, playbook file, pitch narrative |
| **Editorial** (`.roles/editorial/`) | 3 permanent — E-1 Citation Auditor, E-2 Scope Keeper, E-3 Numeracy Checker | Validation gate: required before any artifact advances to `validated` |
| **Board** (`.roles/board/`) | Per-trade domain experts, assembled on demand | Expert claims needing domain defense; not permanent |

The six panel voices create deliberate friction across the core productive
tensions of local-production economics (profit vs. commons, commons vs.
civic, civic vs. market, practitioner vs. investor, historical realism vs.
narrative, craft vs. history). No catalog entry or claim is complete
until it survives all six.

Editorial is a form gate, not a substance gate: citation completeness,
scope drift, and numeracy sanity. It runs after panel, before promotion.

---

## 6. Review Skills

Skills operationalize the review tiers. Each lives in `skills/<name>/SKILL.md`.

| Skill | Tier |
|---|---|
| `skills/ceres-panel/` | Panel — run 6-voice review on any CERES artifact |
| `skills/ceres-editorial/` | Editorial — promotion gate from `reviewed` to `validated`; citation / scope / numeracy pass (panel review must come first) |
| `skills/ceres-board/` | Board — trade-specific domain expert review on a contested claim |
| `skills/ceres-check/` | Cross-tier fast audit — structured findings table; complements panel; can run at any stage |

Additional authoring and orchestration skills are planned for Phase 2
(`ceres-catalog-entry`, `ceres-sim-tier-a`, `ceres-playbook`, `ceres-pitch`,
`ceres-promote`, `ceres-e2e`). See `skills/ceres-check/SKILL.md` for fast-audit
usage guidance. *(A `skills/README.md` index is not yet created; see Plan B.)*

---

## 7. Scope Discipline

- **Keep artifacts in their box.** A catalog entry describes and evaluates one
  equipment design. A playbook file identifies winning designs and sketches
  implementation. A research file extracts functional requirements. Do not
  blend these concerns.
- **If an artifact grows beyond its spec scope, propose a spec amendment.**
  Don't silently expand. Add a dated note to the artifact flagging the scope
  question and open a discussion; do not proceed until the spec is updated.
- **The working hypothesis is testable, not assumed.** If Phase 1 research
  reveals that the binding constraint for a trade is not equipment economics
  (demand collapse, regulatory capture, labor-regime dependency,
  supply-chain disappearance), the analysis for that trade pivots to
  document what is actually required. A rigorous null result is success;
  silent scope expansion to rescue a failing hypothesis is not.

---

## 8. Sibling Project References

| Project | Path | Relationship |
|---|---|---|
| LUCIA | `chronicle` | Structural pattern source: "many instances, consistent schema" catalog model; panel/scoring patterns |
| FELICE/RMM | `rmm` | `corpus/canon` + `corpus/program` framework structure; simulation-design discipline |
| MAXIM | `reference` | Primary citation source for domain material (archaeology, ceramics, architecture-history, chemical engineering, agriculture, etc.) |

**Cite MAXIM for domain material; do not duplicate it here.** If MAXIM has
a relevant entry, reference it. If no MAXIM entry exists, add the citation
to `sources/` and note the gap.

CERES borrows patterns from siblings, not authority. Own rules apply here.
