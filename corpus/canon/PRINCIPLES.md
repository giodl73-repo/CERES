# CERES Catalog-Entry Principles

**Version:** 1.0  
**Date:** 2026-04-18  
**Status:** canonical  

---

## Purpose

These principles define what makes a "good" catalog entry. They are aspirational quality markers, not a checklist of minimum-viable compliance. The scoring rubric (`scoring/RUBRIC.md`, forthcoming) will reference these principles to produce numeric scores at each promotion gate (`draft` → `reviewed` → `validated`). The editorial gates (E-1, E-2, E-3) enforce the mechanical subsets of these principles — citation presence, scope compliance, arithmetic consistency — as promotion blockers. The panel voices (P-1 through P-6) apply the interpretive subsets: whether the governance sketch is actually adequate, whether the historical lineage is actually honest, whether the market price is actually defensible.

Every entry that earns `validated` status should satisfy all ten principles. Entries in `draft` or `reviewed` state may flag known gaps; they cannot conceal them.

---

## Principle 1 — Schema-Complete

**Statement:** Every required frontmatter field is populated per `catalog/SCHEMA.md`; no field is omitted, left as `null` without justification, or filled with a placeholder that has not been flagged for resolution.

**Rationale:** The simulation code ingests frontmatter directly. A missing or placeholder field is not a style problem — it produces a failed evaluation cell or a silently wrong one. The schema is the contract between the catalog author and the simulation layer.

**Enforces:** E-2 Scope Keeper (schema violation = P1 finding, blocks promotion); E-3 Numeracy Checker (sim_params must cross-check as a unit).

**Concrete test:** An entry fails this principle if any of the following are true: a required field is absent from the frontmatter; a numeric field contains text like "TBD" or "see notes"; a `results:` cell is `null` after the Tier A simulation has run for this entry; `status: validated` is claimed while required fields remain unfilled.

---

## Principle 2 — Every Number Cited

**Statement:** Every economic number in the frontmatter and prose has a corresponding entry in the `sources:` block; in-text `[Author YEAR]` attribution is used wherever the number originates from a single identifiable source.

**Rationale:** CERES's quality bar is research-paper-level estimates. A confident number with no source is a confident guess. A single fabricated citation discredits every honest one around it. The project's terminal deliverable is a fundable pitch; funders audit numbers.

**Enforces:** E-1 Citation Auditor (missing or unverifiable source = P1 finding, blocks promotion); P-1 Market Economist (uncited market price is a P1 editorial finding per spec Section 5).

**Concrete test:** An entry fails this principle if: `capital_cost`, `market_price_per_unit`, `annual_consumables`, or any `sim_params` field has no traceable source in `sources:`; a historical claim in the prose lacks a citation; a source is cited but does not support the specific claim made. Three or more P1 citation findings hold the entry from promotion.

---

## Principle 3 — Operations Reality Addressed

**Statement:** The `operations_reality` block is fully populated: first-year failures named with estimated hours-to-failure and replacement lead times; consumables lead time stated (typical and worst-case); throughput variance modeled with worst-month and best-month fractions; operator impact described (noise, heat, emissions, physical demand).

**Rationale:** Paper designs assume the average case. Real shops die in the tail. An operator making a business decision on the basis of average throughput and no failure data is being misled by the catalog. The difference between a February with 45% of average throughput and a November at 165% is cashflow survival — not an academic footnote. Operator impact shapes hiring, retention, apprentice recruitment, and who realistically applies to run this equipment for twenty years.

**Enforces:** P-4 Craft Practitioner ("what breaks first, and who fixes it?"); P-6 Skeptical Funder (downside analysis must survive the hardest-honest-question test).

**Concrete test:** An entry fails this principle if: `operations_reality` is absent or contains fewer than two named first-year failure items; `consumables_lead_time_days` omits a worst-case value; `throughput_variance.worst_month_fraction_of_average` is absent; `operator_impact` lacks noise or heat exposure values. An entry that states only average throughput without variance is incomplete regardless of how precise the average is.

---

## Principle 4 — Lens Context Addressed

**Statement:** If `lens_fit.cooperative` is `good` or `marginal`, the `lens_context.cooperative` block is present and covers membership boundaries, rules source, monitoring mechanism, graduated sanctions, and conflict resolution, with Ostrom principles addressed. If `lens_fit.civic` is `good` or `marginal`, the `lens_context.civic` block is present and covers political coalition, council vote estimate, relationship to any existing private operator, governance form, and municipal budget line.

**Rationale:** A `cooperative: good` label without a governance sketch is romantic shorthand, not a claim. Elinor Ostrom's design principles did not emerge from theory — they emerged from watching commons succeed and fail for centuries. An entry that applies the cooperative label without answering "what happens when a member breaks the tool?" is a trap. Similarly, a `civic: good` label without a named political coalition and a relationship to existing private operators is a research paper, not a program. These are the two questions that kill civic proposals at town council meetings.

**Enforces:** P-2 Commons Theorist (coop-good without governance sketch = unacceptable); P-3 Civic Steward (civic-good without political path and private-operator analysis = unacceptable).

**Concrete test:** An entry fails this principle if: `lens_fit.cooperative` is `good` or `marginal` and `lens_context.cooperative` is absent or missing any of {membership_boundary, graduated_sanctions, conflict_resolution}; `lens_fit.civic` is `good` or `marginal` and `lens_context.civic` is absent or missing any of {political_coalition, competes_with_private, budget_line}. Placeholder text ("TBD" or "members will figure it out") in these blocks constitutes absence.

---

## Principle 5 — Market Price Declared

**Statement:** If `lens_fit.market` is `good` or `marginal`, `economics.market_price_per_unit` is populated with a cited range, and `pricing_notes` explains the premium over the relevant industrial baseline and names the customer segment expected to pay it.

**Rationale:** The MARKET lens cannot evaluate without a revenue assumption. An entry that claims `market: good` without declaring the price at which the output will sell is asking the simulation to produce a payback number from a missing input. More importantly, the market price is a claim about the world — that a real customer segment exists, at a stated price, with evidence — not a residual that falls out of a viability calculation. Demand at premium prices must be argued, not assumed.

**Enforces:** P-1 Market Economist ("is there a real market — not a wished-for market — at the claimed price?"); E-1 Citation Auditor (uncited market price = P1 finding); E-3 Numeracy Checker (price must be consistent with the payback implied by sim_params).

**Concrete test:** An entry fails this principle if: `lens_fit.market` is `good` or `marginal` and `economics.market_price_per_unit` is absent or null; the pricing_notes do not name the industrial-competitor baseline price; the claimed premium is not justified by any cited evidence of customer willingness to pay; the market price assumed in pricing_notes is inconsistent with the payback implied by `sim_params`.

---

## Principle 6 — Historical Lineage Honest

**Statement:** The `inspirations:` field cites actual historical or modern precedents; the prose explains which *function* is carried forward from each precedent (not only the aesthetic); labor regimes, supply chains, and property structures that made the historical form viable are named, and any that cannot be reproduced in modern form are acknowledged.

**Rationale:** A catalog built on romanticized history will fail in ways a historian can predict. The village forge ran four hours a day, six months a year, and the smith was often also a farmer. The coop that appears in the inspirations list may have been sustained by customary obligations that cannot be reproduced ethically. Function, not form, is what the modern design must carry forward. An entry that borrows aesthetic from history while silently dropping the economics, labor regime, or supply chains that made the historical form work is a decoration, not a design.

**Enforces:** P-5 Historian ("is the historical precedent you are invoking the actual precedent, or a modern myth of it?"); E-1 Citation Auditor (historical claims require sources).

**Concrete test:** An entry fails this principle if: `inspirations:` contains entries for which no prose explanation of functional inheritance exists; the historical lineage section claims viability without citing the labor or supply-chain conditions that enabled it; a historical precedent is cited whose viability rested on household labor, apprentice servitude, or guild exclusion — and this is not acknowledged; the word "sustainable" is applied to a pre-industrial precedent without qualification.

---

## Principle 7 — Design Rationale Explicit

**Statement:** The "Design rationale" section states the specific problem this entry solves that no other entry in the same trade's catalog solves, and justifies its presence as a distinct entry rather than a variant of an existing one.

**Rationale:** The catalog's value is in the diversity of genuinely distinct design choices — different tradeoffs among capital cost, energy source, throughput, shareability, and skill floor — not in accumulating similar entries under slightly different names. Redundant entries dilute the evaluation matrix without adding coverage of the design space. The spec sets a target of 20–40 entries per trade; that target is only meaningful if the entries span the space. An entry that cannot articulate what it offers that no other entry offers is a candidate for merger or deprecation. Avoiding catalog bloat is a quality discipline, not an aesthetic preference.

**Enforces:** E-2 Scope Keeper (redundant entries that duplicate others = scope drift); P-6 Skeptical Funder (every element of the catalog must justify its resource cost to produce and maintain).

**Concrete test:** An entry fails this principle if: the design rationale section is absent or generic ("this entry explores a coal-fired forge"); the entry's combination of {energy_source, scale, shareability, skill_floor} is not distinguishable from an existing entry in the same catalog without a stated tradeoff reason; a reviewer finds two entries that could be merged and neither has a documented reason for remaining separate.

---

## Principle 8 — Failure Modes Named

**Statement:** The "Known risks / failure modes" section explicitly names at least one failure mode in each of the following categories: regulatory (zoning, emissions, licensing), labor pipeline (succession, skill scarcity, apprentice path), and supply chain (input availability, lead time, single-supplier dependencies).

**Rationale:** An entry that names only what works is incomplete. An entry whose risks are buried in hedged prose or confined to a regulatory-notes footnote misleads the operator who acts on it. Regulatory failures close shops. Labor pipeline failures kill trades generationally — a forge with no apprentice path is a forge that lasts one operator's career. Supply chain failures are the failure mode most often discovered in year three, not year one. All three categories of failure are structurally different from unit economics; none of them is captured by the simulation's average-case model.

**Enforces:** P-4 Craft Practitioner (operational failure modes); P-1 Market Economist (supply-chain and labor risk affect the economic case); P-6 Skeptical Funder ("what is the failure mode nobody in the proposal wants to think about?").

**Concrete test:** An entry fails this principle if: the failure modes section is absent; any of the three categories (regulatory, labor pipeline, supply chain) is missing; failure modes are mentioned only as brief hedges in passing prose without a dedicated treatment; the entry claims `apprentice_friendly: false` without naming the succession risk in the failure modes section.

---

## Principle 9 — Apprentice Path Present or Flagged

**Statement:** Every entry either (a) describes a realistic apprentice path — how a journeyman becomes capable on this equipment and how the skill transfers to a successor — or (b) explicitly flags the absence of an apprentice path as a named risk, with a consequence statement.

**Rationale:** An operator who cannot train a successor is an operation that ends when the operator does. Operator-succession is a first-class viability concern, not a footnote. A catalog full of one-person-shop designs that die with their operators is a catalog that describes a generation of local production, not a restored trade. The civic and cooperative lenses specifically require institutional continuity; an entry marked `civic: good` or `cooperative: good` with no apprentice path and no succession plan has an unresolved contradiction.

**Enforces:** P-4 Craft Practitioner ("an entry with no apprentice path is a dead-end, however clever"); P-3 Civic Steward (civic investments require institutional continuity); P-6 Skeptical Funder (a business without succession is a terminal-risk investment).

**Concrete test:** An entry fails this principle if: the frontmatter field `apprentice_friendly` is present but no prose section addresses how the skill is transmitted; `apprentice_friendly: false` is set but the consequence (trade dies with operator; estimated operator-career lifespan as runway) is not stated; an entry is marked `lens_fit.civic: good` or `lens_fit.cooperative: good` while `apprentice_friendly: false` and no succession plan appears in the failure modes section.

---

## Principle 10 — Iteration Log Present

**Statement:** Every entry contains an "Iteration log" section with at least one dated entry recording the design decision or revision history; subsequent revisions add dated entries rather than overwriting prior ones.

**Rationale:** A catalog that evolves without a trace of its evolution cannot be audited, cannot be compared to earlier versions, and cannot support the `status` + `version` + `supersedes` chain that the schema defines. The iteration log is the human-readable record of why the entry is in its current state — what was changed from version to version, what triggered a revision, and what assumptions were reconsidered. It is also the record that distinguishes a genuinely revised entry from one that has been silently corrected. An entry marked `version: 0.3` with no log explaining what changed between 0.1 and 0.3 has broken the version-tracking commitment.

**Enforces:** E-2 Scope Keeper (version and status fields must be consistent with the actual state of the entry); P-6 Skeptical Funder (a plan that cannot account for its own revision history cannot be trusted to account for its assumptions).

**Concrete test:** An entry fails this principle if: the "Iteration log" section is absent; the section is present but has no dated entries; the `version` field in frontmatter is greater than `0.1` but the log contains only the initial creation note; a revision is recorded in the log without a date; a `supersedes:` value is set but no log entry explains the reason for superseding the predecessor.

---

## Cross-Reference: Principles, Panel Voices, and Editorial Gates

| # | Principle | Primary Panel Voice | Primary Editorial Gate |
|---|---|---|---|
| 1 | Schema-complete | — | E-2 Scope Keeper |
| 2 | Every number cited | P-1 Market Economist | E-1 Citation Auditor |
| 3 | Operations reality addressed | P-4 Craft Practitioner | E-3 Numeracy Checker |
| 4 | Lens context addressed | P-2 Commons Theorist, P-3 Civic Steward | E-2 Scope Keeper |
| 5 | Market price declared | P-1 Market Economist | E-1 Citation Auditor, E-3 Numeracy Checker |
| 6 | Historical lineage honest | P-5 Historian | E-1 Citation Auditor |
| 7 | Design rationale explicit | P-6 Skeptical Funder | E-2 Scope Keeper |
| 8 | Failure modes named | P-4 Craft Practitioner, P-6 Skeptical Funder | — |
| 9 | Apprentice path present or flagged | P-4 Craft Practitioner, P-3 Civic Steward | — |
| 10 | Iteration log present | P-6 Skeptical Funder | E-2 Scope Keeper |

---

## Self-Review Checklist

Before promoting an entry from `draft` to `reviewed`, the author should verify:

- [ ] All ten principles addressed (or gap explicitly flagged)
- [ ] P1 editorial findings resolved (E-1: citations; E-2: scope/schema; E-3: arithmetic)
- [ ] `operations_reality` block not empty
- [ ] `lens_context` blocks present for every `good` or `marginal` lens label
- [ ] `market_price_per_unit` present and cited if `lens_fit.market` is not `poor`
- [ ] `inspirations:` entries each have a prose explanation of functional (not aesthetic) inheritance
- [ ] "Known risks / failure modes" section addresses regulatory, labor pipeline, and supply chain
- [ ] Apprentice path described or absence flagged with consequence
- [ ] Iteration log has at least one dated entry
- [ ] `design_rationale` explains what this entry offers that no other entry in the same catalog does
