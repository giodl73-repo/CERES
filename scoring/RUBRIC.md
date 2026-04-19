# CERES Scoring Rubric

**Version:** 1.0
**Date:** 2026-04-18
**Status:** canonical
**Directory note:** `scoring/` was created alongside this file; it is the designated home for
all quantitative evaluation instruments. The rubric is the first file in that directory.

---

## 1. Purpose

Panel voices and the rubric serve different functions. They must not be conflated.

**Panel voices** (P-1 through P-6) give qualitative, first-person, expert feedback. They argue,
challenge, and flag concerns. A panel review is a conversation between the entry and a
specialist perspective. Panel findings are expressed as P1 / P2 / P3 severity ratings attached
to specific claims or sections. They are inherently interpretive.

**This rubric** produces a single composite number — a 0–100 score — that feeds promotion
decisions. It is not a summary of the panel's opinions; it is a separate instrument that
operationalizes the 10 quality principles (`corpus/canon/PRINCIPLES.md`) into observable,
dimension-specific anchors. The rubric score is computed by a designated scorer (or scoring
committee) working from the entry alone, consulting the panel's qualitative notes to resolve
ambiguity but not deferring to them for the numeric result.

The separation matters because qualitative richness and numeric scores can diverge. A panel
may raise important concerns while the entry still clears the numeric threshold, or may be
largely satisfied while the entry sits at 58 and needs more work. Both signals are real.
Promotion decisions use both: the composite score determines whether the entry is eligible for
promotion, and the editorial gates determine whether the entry is blocked regardless of score.

Scoring is public to the author. Every dimension score must be accompanied by a one-sentence
reason. An unexplained number is not a rubric score; it is a verdict.

---

## 2. Scoring Scale

The rubric produces a **100-point composite score** across six dimensions. Within each
dimension, scores are expressed on a **0–100 sub-scale** and then weighted to produce the
composite.

**Composite formula:**

```
Composite = (D1 × 0.15) + (D2 × 0.20) + (D3 × 0.15) + (D4 × 0.20) + (D5 × 0.10) + (D6 × 0.20)
```

Where:

| Symbol | Dimension | Weight |
|--------|-----------|--------|
| D1 | Schema Completeness | 15 |
| D2 | Citation Strength | 20 |
| D3 | Operations Realism | 15 |
| D4 | Lens-Context Rigor | 20 |
| D5 | Historical Honesty | 10 |
| D6 | Design Rationale and Differentiation | 20 |
| | **Total** | **100** |

Sub-scores within each dimension are assigned in increments of 5 (0, 5, 10, … 100). Scorers
should choose the band (0–25, 26–50, 51–75, 76–100) first, then settle on the specific value
within the band. Avoid the gravitational pull of round numbers: 50 should mean "genuinely
mid-band," not "I could not decide."

---

## 3. Dimensions and Weights

### 3.1 D1 — Schema Completeness (weight: 15)

**What it measures:** Whether all required and conditional frontmatter fields are populated
correctly, free of placeholders, and internally consistent — as defined by `catalog/SCHEMA.md`.

**Principles covered:** P-1 (Schema-Complete), P-10 (Iteration Log Present).

**Editorial gates in play:** E-2 Scope Keeper (schema violations are P1 findings that block
promotion). E-3 Numeracy Checker (arithmetic consistency of `sim_params`).

**Scope note:** This dimension scores completeness and structural correctness, not the quality
of the content in those fields. A fully populated `operations_reality` block that contains
poor estimates is D3's problem, not D1's.

**Specific fields checked:**
- All Required fields from `catalog/SCHEMA.md` Section 4 present and non-null (except
  `supersedes` and `backup_fuel`, which accept null as valid).
- All Conditional fields present when their trigger condition is met: `market_price_per_unit`
  and `pricing_notes` when `lens_fit.market` is `good` or `marginal`; `operations_reality`
  block when any `lens_fit` value is `good` or `marginal`; `lens_context.cooperative` and
  `lens_context.civic` sub-blocks when the corresponding `lens_fit` values are `good` or
  `marginal`.
- `sim_params.cost_mean` equals `economics.capital_cost.mid`.
- All nine `results:` cells present (null is valid for unpromoted entries; absent cells are not).
- `status` field is consistent with the entry's actual state (no `validated` claim with
  unfilled required fields).
- Iteration log present with at least one dated entry; `version > 0.1` only if log records at
  least one revision beyond the initial creation note.

---

### 3.2 D2 — Citation Strength (weight: 20)

**What it measures:** Whether every economic number, simulation parameter, and historical claim
in the entry has a traceable, real, and appropriate source in the `sources:` block.

**Principles covered:** P-2 (Every Number Cited), P-5 (Market Price Declared — the cited-price
obligation), P-6 (Historical Lineage Honest — historical claims require sources).

**Editorial gates in play:** E-1 Citation Auditor (missing or unverifiable sources are P1
findings). P-1 Market Economist (uncited market price is a P1 panel finding per spec Section 5).

**Scope note:** Citation strength scores the verifiability and appropriateness of sources. A
source that exists but does not support the specific claim made scores the same as a missing
source for this dimension. Third-hand citations (blog-citing-blog) are a material downgrade.

**Specific checks:**
- `economics.capital_cost`, `economics.install_cost`, `economics.annual_maintenance`,
  `economics.annual_consumables`, `economics.floor_space_rent_per_year` — each traceable to
  `sources:`.
- `economics.market_price_per_unit` — explicitly cited, not derived residually from `sim_params`.
- All `sim_params.*` fields — traceable to cited sources or derivable from cited fields with
  the derivation stated in "Key Assumptions" prose.
- Every historical claim in prose — traced to a `sources:` entry.
- `sources:` entries are real, findable, and appropriate (E-1 Rule E1-R5).
- Estimates are labeled as estimates; ranges are labeled as ranges.

---

### 3.3 D3 — Operations Realism (weight: 15)

**What it measures:** Whether the `operations_reality` block is fully populated with
honest, specific, tail-risk data — not average-case assumptions.

**Principles covered:** P-3 (Operations Reality Addressed), P-8 (Failure Modes Named),
P-9 (Apprentice Path Present or Flagged).

**Panel voices in play:** P-4 Craft Practitioner ("what breaks first, and who fixes it?"),
P-6 Skeptical Funder (downside analysis must survive the hardest-honest-question test).
**Editorial gate:** E-3 Numeracy Checker (`downtime_fraction` must be consistent with
the failure profile).

**Scope note:** Average-case throughput figures without variance data are insufficient for
this dimension regardless of precision. An entry that states only "expected throughput: X
units/month" with no variance, no failure timeline, and no operator impact scores in the
0–25 band.

**Specific checks:**
- `first_year_failures` — minimum two named components with estimated hours-to-failure,
  replacement cost, and replacement lead time.
- `consumables_lead_time_days` — both `typical` and `worst` values present.
- `throughput_variance.worst_month_fraction_of_average` and
  `throughput_variance.best_month_fraction_of_average` — both present and realistic
  (not set to 1.0/1.0, which would represent no variance).
- `operator_impact` — `noise_db`, `heat_exposure`, `emissions`, and `physical_demand` all
  populated with specific, non-placeholder values.
- `sim_params.downtime_fraction` internally consistent with the first-year failure profile.
- "Known risks / failure modes" prose section covers all three failure categories:
  regulatory, labor pipeline, and supply chain.
- `apprentice_friendly` field is consistent with prose: if `true`, the path is described;
  if `false`, the succession risk and consequence are named.

---

### 3.4 D4 — Lens-Context Rigor (weight: 20)

**What it measures:** Whether every `good` or `marginal` lens label is backed by a substantive
governance sketch that earns the label — particularly the cooperative and civic lens contexts.

**Principles covered:** P-4 (Lens Context Addressed), P-9 (Apprentice Path — civic and
cooperative lenses require institutional continuity).

**Panel voices in play:** P-2 Commons Theorist (cooperative governance rigor),
P-3 Civic Steward (civic political-path and private-operator analysis).
**Editorial gate:** E-2 Scope Keeper (`lens_context` blocks absent when triggered are P1
findings).

**Scope note:** A lens label without a governance sketch is "romantic shorthand, not a claim"
(PRINCIPLES.md, Principle 4). This dimension scores the quality and completeness of the
governance argument, not just its presence. A `lens_context.cooperative` block that contains
only placeholders or generic text ("members will figure it out") scores in the 0–25 band
despite being technically present.

**Specific checks (cooperative lens, when triggered):**
- `membership_boundary` — specific about who may join and on what terms (geographic scope,
  dues structure, eligibility criteria).
- `rules_source` — names the governance instrument (bylaws, articles, etc.) and the
  amendment mechanism.
- `monitoring` — names the mechanism (equipment log, elected steward audit, etc.) — not
  a generic "we will monitor usage."
- `graduated_sanctions` — Ostrom Principle 5 satisfied: an ordered sequence of specific
  consequences, not a single "expulsion" trigger.
- `conflict_resolution` — Ostrom Principle 6: a named mechanism, not "disputes will be
  resolved fairly."
- `ostrom_principles_addressed` — list present; un-addressed principles explained in Known
  Risks (Principles 7 and 8 are often NA at single-coop scale, which is acceptable if noted).

**Specific checks (civic lens, when triggered):**
- `political_coalition` — names specific stakeholders, not "community support."
- `council_vote_estimate` — includes a vote-count estimate and names the main opposition
  argument.
- `competes_with_private` — explicitly analyzes whether a civic facility displaces an
  existing private operator; silence is not acceptable.
- `governance_form` — names the ownership and management structure, not a generic description.
- `budget_line` — names the capital and operating funding mechanisms.

**Lens-fit consistency check:** `lens_fit.market` is `good` or `marginal` only if
`market_price_per_unit` is present and `pricing_notes` names the industrial-competitor
baseline and the customer segment (see also D2).

---

### 3.5 D5 — Historical Honesty (weight: 10)

**What it measures:** Whether the `inspirations:` field cites real historical or modern
precedents, and whether the prose "Historical Lineage" section explains functional (not
aesthetic) inheritance while honestly acknowledging the economic, labor, and supply-chain
conditions that made the historical form viable — including those that cannot be reproduced.

**Principles covered:** P-6 (Historical Lineage Honest).

**Panel voice in play:** P-5 Historian ("is the historical precedent you are invoking the
actual precedent, or a modern myth of it?").
**Editorial gate:** E-1 Citation Auditor (historical claims require sources).

**Scope note:** This dimension is lower-weighted (10) because not every entry has complex
historical precedents. Entries with few or no `inspirations:` entries are not penalized for
brevity, but they cannot score in the 76–100 band without demonstrating genuine engagement
with historical context. Entries whose historical sections are superficial but not dishonest
score in the 51–75 band.

**Specific checks:**
- Every entry in `inspirations:` has a corresponding prose explanation in "Historical
  Lineage" that addresses functional inheritance (capability, economics, operational form),
  not only aesthetic similarity.
- Labor regimes, supply-chain conditions, and property structures that made the historical
  form viable are named.
- Conditions that cannot be reproduced in modern form (household labor, apprentice servitude,
  guild exclusion, customary obligations) are acknowledged rather than silently dropped.
- The word "sustainable" applied to a pre-industrial precedent is qualified.
- Historical claims in prose are cited in `sources:`.

---

### 3.6 D6 — Design Rationale and Differentiation (weight: 20)

**What it measures:** Whether the entry can articulate the specific problem it solves that no
other entry in the same trade's catalog solves, and whether its combination of design
parameters is genuinely distinct rather than a variant that should be merged with an existing
entry.

**Principles covered:** P-7 (Design Rationale Explicit), P-10 (Iteration Log Present — the
revision history supports the differentiation argument by showing what changed and why).

**Panel voice in play:** P-6 Skeptical Funder ("every element of the catalog must justify
its resource cost to produce and maintain").
**Editorial gate:** E-2 Scope Keeper (redundant entries that duplicate others = scope drift).

**Scope note:** This dimension requires the scorer to consult the trade's catalog context —
what other entries exist in the same trade, and whether this entry's design-parameter
combination is genuinely distinct. An entry scored in isolation cannot score above 50 for
this dimension; the scorer must check for overlap.

**Specific checks:**
- "Design rationale" prose section is present and names the specific problem this entry
  solves that no other entry in the same trade's catalog solves.
- The rationale is not generic ("this entry explores a coal-fired forge").
- The entry's combination of {energy_source, scale, shareability, skill_floor} is
  distinguishable from other entries in the same catalog, with a stated tradeoff reason
  where distinctions are subtle.
- No entry in the same catalog could be merged with this one without material information
  loss (or, if it could, a documented reason for keeping them separate exists).
- The "Iteration Log" is present, dated, and records design decisions that illuminate the
  rationale — demonstrating that the current design emerged from deliberate choices, not
  defaults.

---

## 4. Per-Dimension Rubric Anchors

Each dimension is scored on a 0–100 sub-scale with four bands. Read the entry against all
anchor descriptors in the applicable band; the entry should match the majority of descriptors
to score in that band. When evidence spans two bands, score in the lower band and note what
is needed to reach the higher one.

---

### D1 — Schema Completeness Anchors

**76–100 (Complete and consistent)**
All required fields present and correctly typed. All conditional fields present when triggered;
no conditional field absent without a documented exception. `sim_params.cost_mean` equals
`economics.capital_cost.mid` exactly. `status` field accurately reflects the entry's state.
Iteration log has at least one dated entry and, if `version > 0.1`, records every material
revision with a date. The nine `results:` cells are present (values may be null for
unpromoted entries, but the cells are not absent). No field contains a placeholder string
(`TBD`, `todo`, `see notes`, etc.) that has not been flagged for resolution with a dated
action item in the iteration log.

**51–75 (Mostly complete with minor gaps)**
All required fields present; one or two conditional fields absent or placeholder-filled under
a triggered condition. The absences are minor in scope (e.g., a single `ostrom_principles_addressed`
list missing while the rest of `lens_context.cooperative` is complete) or have been
explicitly flagged in the iteration log as known gaps. `sim_params.cost_mean` matches
`economics.capital_cost.mid` or the discrepancy is small and explained in "Key Assumptions."
Iteration log present but may lack entries for one or two minor revisions.

**26–50 (Partial; multiple gaps)**
Multiple required or conditional fields absent or placeholder-filled. The entry is structurally
recognizable but incomplete in ways that would prevent a simulation run or produce a
silently incorrect result. `operations_reality` block may be entirely absent despite `lens_fit`
values of `good` or `marginal` being set. `sim_params` fields have unexplained discrepancies
with `economics.*`. Iteration log may be absent or contain only a creation note with no dates.
The `status` field may not reflect reality (e.g., `reviewed` claimed without citation clean-up).

**0–25 (Structural failure)**
The entry is missing fundamental required fields (e.g., `id`, `trade`, `economics`,
`sim_params` block, or `results` block). The frontmatter cannot be ingested without errors.
`status: validated` is claimed while required fields are absent or null. No iteration log
present. The entry represents a skeleton or draft that has not been revised since initial
creation.

---

### D2 — Citation Strength Anchors

**76–100 (Research-paper standard)**
Every field in `economics.*` (capital cost, install cost, maintenance, consumables, rent,
and market price when present) traces to a specific, findable, appropriate source in
`sources:`. Every `sim_params.*` field traces to a cited source or is derived from cited
fields with the derivation explicitly stated in "Key Assumptions" prose. All historical claims
in prose are cited. `market_price_per_unit`, when present, is explicitly cited as a market
observation — not derived from the payback calculation. No third-hand citations. Estimates
are labeled as estimates. Ranges are labeled as ranges. A reader could verify every number
independently within a day of research.

**51–75 (Solid citations with minor gaps)**
The major economic fields (capital cost, market price) are cited. One or two secondary
fields (e.g., `floor_space_rent_per_year` or `annual_consumables`) carry a labeled estimate
without a formal source. Historical claims are mostly cited; one or two minor prose assertions
are uncited but not load-bearing (not central to the viability argument). `sim_params`
derivations are partially explained. No fabricated or unresolvable sources. A diligent reader
could verify the core claims; peripheral claims require trust.

**26–50 (Partial citation; material gaps)**
Several load-bearing economic numbers lack citations (e.g., `capital_cost` with a
single-point estimate and no source, or `market_price_per_unit` present but uncited).
Historical claims in prose have no citations. `sim_params` fields are not connected to
any stated sources or derivations. The entry may have a `sources:` block with entries, but
the entries do not clearly correspond to specific field values. A funder auditing the numbers
would find multiple unverifiable claims within 30 minutes.

**0–25 (Citation failure)**
The `sources:` block is absent, empty, or contains generic or fabricated entries that do not
support specific claims. Multiple load-bearing fields — including `capital_cost` or
`market_price_per_unit` — have no traceable sources. Historical claims are asserted without
any sourcing. The entry cannot pass an E-1 audit at any severity level. Three or more P1
E-1 findings are present or foreseeable.

---

### D3 — Operations Realism Anchors

**76–100 (Honest and specific tail-risk data)**
`first_year_failures` lists at least two named components with specific hours-to-failure
estimates, replacement costs, and lead times drawn from cited service data or plausible
engineering estimates. `consumables_lead_time_days` provides both `typical` and `worst`
values where `worst` reflects a documented supply-chain stress scenario (single supplier,
overseas shipping, seasonal shortage), not just "a few extra days." `throughput_variance`
provides `worst_month` and `best_month` fractions that reflect realistic seasonality
rather than symmetry around the average. `operator_impact` is specific: `noise_db` is a
measured or estimated value, not a category; `heat_exposure` names the workstation
conditions; `emissions` names the specific pollutants; `physical_demand` describes actual
ergonomic demands. `sim_params.downtime_fraction` is consistent with the failure profile.
"Known risks / failure modes" prose covers regulatory, labor pipeline, and supply chain with
at least one specific, named risk per category. `apprentice_friendly` is consistent with
prose treatment.

**51–75 (Adequate realism with gaps)**
`first_year_failures` is present with two items but one or more fields (hours-to-failure,
replacement lead time) is an order-of-magnitude estimate without sourcing. `consumables_lead_time_days`
has both values but `worst` may equal `typical × 2` without a specific scenario. `throughput_variance`
fractions are present and non-trivial (worst < 0.9, best > 1.1). `operator_impact` is
present; some fields (e.g., `noise_db`) may be categorical rather than specific. "Known
risks" section is present but may treat one of the three categories (regulatory, labor
pipeline, supply chain) superficially. Apprentice path is addressed.

**26–50 (Partial operations data)**
`first_year_failures` is present but may list only one item, or items lack replacement lead
times and costs. `consumables_lead_time_days` is present but the `worst` value is absent or
equal to `typical`, indicating no supply-chain stress scenario was considered.
`throughput_variance` fractions may be absent or trivial (worst = 0.95, best = 1.05).
`operator_impact` may be partially populated or contain generic language ("moderate heat").
"Known risks" section may cover only one or two of the three required failure categories.
`sim_params.downtime_fraction` may be suspiciously low (under 0.05) without explanation.

**0–25 (Operations reality absent or nominal)**
`operations_reality` block is absent despite `lens_fit` values of `good` or `marginal`.
Or the block is present but contains fewer than two `first_year_failures` items. Throughput
variance fields are absent. `operator_impact` fields are absent or filled with placeholder
text. The entry describes only the average case with no tail-risk data. "Known risks" section
is absent, or is present but contains only a single generic sentence with no category
breakdown. The entry could mislead a prospective operator who acts on it.

---

### D4 — Lens-Context Rigor Anchors

**76–100 (Earned governance labels)**
Every `good` or `marginal` lens label is backed by a substantive governance sketch.
For `cooperative: good` or `marginal`: all six sub-fields (`membership_boundary`,
`rules_source`, `monitoring`, `graduated_sanctions`, `conflict_resolution`,
`ostrom_principles_addressed`) are present and specific. `membership_boundary` names actual
eligibility criteria; `monitoring` names an actual mechanism (not "we will track usage");
`graduated_sanctions` is an ordered sequence of at least three distinct consequences; the
Ostrom principles list is specific about which are addressed and which are not applicable
(with a note on NA ones). For `civic: good` or `marginal`: all five sub-fields are present
and specific. `political_coalition` names actual stakeholders; `council_vote_estimate` names
a vote margin and the main opposition argument; `competes_with_private` is explicitly
analyzed, not silently omitted. The governance description would hold up to scrutiny from
a cooperative development practitioner or a municipal budget analyst.

**51–75 (Present governance with quality gaps)**
All sub-fields are present for each triggered lens context. However, one or two are generic
rather than specific: `monitoring` says "usage will be tracked" without naming the mechanism;
`political_coalition` lists stakeholders by category rather than by name; `council_vote_estimate`
is a rough percentage without a named opposition argument. The governance sketch is
recognizable and not dishonest, but a practitioner would ask follow-up questions before
endorsing the label. `ostrom_principles_addressed` list is present but does not explain
un-addressed principles.

**26–50 (Partially populated governance blocks)**
The `lens_context` block(s) are present but missing one or more required sub-fields.
Or sub-fields are present but consist of placeholder text ("TBD", "members will figure it
out"). For cooperative: `graduated_sanctions` is a single consequence rather than a
sequence; `conflict_resolution` is absent or is "disputes will be settled fairly." For civic:
`competes_with_private` is absent or silent; `budget_line` describes a general aspiration
rather than a specific funding mechanism. The label (`good` or `marginal`) is not convincingly
earned by the governance sketch present.

**0–25 (Missing or cosmetic governance)**
One or more triggered `lens_context` sub-blocks are entirely absent — a `cooperative: good`
label with no `lens_context.cooperative` block, or a `civic: good` label with no
`lens_context.civic` block. Or the blocks exist but contain only a single sentence each with
no specifics. This is the "romantic shorthand" failure the rubric exists to prevent. A P1
E-2 finding is foreseeable or already present. The lens label is decorative rather than
analytical.

---

### D5 — Historical Honesty Anchors

**76–100 (Functional, honest historical analysis)**
Every `inspirations:` entry has a corresponding "Historical Lineage" prose section that
explicitly states what function (capability, economics, operational form) the modern design
carries forward from the precedent — not merely what it resembles aesthetically. Labor
regimes, supply-chain conditions, and property structures that made the historical form
viable are named. Conditions that cannot be reproduced ethically or practically in modern
form (household labor, apprentice servitude, guild exclusion, customary obligations) are
explicitly acknowledged. The section does not romanticize. Historical claims are cited.
"Sustainable" applied to any pre-industrial precedent is qualified with specifics
(sustainable by what measure, under what conditions). A historian reading this section would
not find a myth posing as history.

**51–75 (Adequate historical context with gaps)**
`inspirations:` entries are covered in prose; the functional inheritance is stated, if not
deeply developed. Labor and supply-chain conditions of the historical form are mentioned but
may not be fully analyzed. One or two conditions that cannot be reproduced in modern form
may be acknowledged without consequence-drawing. Historical claims are cited for the main
assertions; minor supporting claims may be uncited. The section is not dishonest but is
somewhat shallow — a historian would want more depth but would not flag an error.

**26–50 (Superficial or partially honest historical section)**
`inspirations:` entries are listed but the prose section addresses only aesthetic similarity
("this design resembles the village forge") without stating what function is carried forward.
Labor regimes or supply-chain conditions that made the historical form viable are not
mentioned. The historical viability claim is asserted without acknowledgment of the
conditions that enabled it. Historical citations may be absent for some claims. The entry
invokes historical precedent as rhetorical support rather than as analytical grounding.

**0–25 (Absent or dishonest historical section)**
`inspirations:` entries are listed but no "Historical Lineage" prose section exists. Or the
section exists but its central claim is a historical myth ("the village forge was a community
hub where every neighbor was welcome") without qualification or acknowledgment of the
economic, social, and labor conditions that bounded the historical reality. "Sustainable"
is applied to pre-industrial forms without qualification. Historical claims are uncited. The
entry would produce false confidence in a reader who takes the historical framing at face
value.

---

### D6 — Design Rationale and Differentiation Anchors

**76–100 (Distinct and justified entry)**
The "Design rationale" prose section states, specifically and without generic language, what
problem this entry solves that no other entry in the same trade's catalog solves. The entry's
combination of {energy_source, scale, shareability, skill_floor} is distinct from other
entries in the catalog; if distinctions are subtle, the stated tradeoff reason is clear and
defensible. A reviewer who reads this entry alongside all others in the same trade would not
find a merge candidate without material information loss. The iteration log records deliberate
design choices — showing the current design was reached through reasoning, not defaults. The
entry adds genuine coverage of the design space.

**51–75 (Adequate differentiation with weaknesses)**
"Design rationale" is present and specific enough to distinguish this entry from most others
in the catalog. One or two design parameters overlap with an existing entry, but the rationale
explains a tradeoff reason for maintaining both (e.g., different scale fit or different
ownership model at similar energy source and throughput). The entry is not clearly a duplicate,
but a merge case could be argued for it against one other entry; the counter-argument exists
and is stated, if not forcefully. Iteration log is present but may not illuminate design
choices deeply.

**26–50 (Weak or generic differentiation)**
"Design rationale" is present but generic ("this entry explores a coal-fired forge at
community scale"). The entry's design parameters overlap significantly with at least one other
entry in the catalog without a documented tradeoff reason. A reviewer could identify a merge
candidate and the current entry does not preemptively address the merger case. Or the
rationale section is present but focuses on what the entry is rather than why it is distinct.
Iteration log is present with creation date but records no design reasoning.

**0–25 (Absent or redundant entry)**
"Design rationale" section is absent or is a single generic sentence. The entry's
{energy_source, scale, shareability, skill_floor} combination is not distinguishable from
at least one other entry in the same catalog, with no documented tradeoff reason. The entry
is a candidate for merger or deprecation with no self-defense argument. Iteration log is
absent. The entry does not justify its resource cost to produce and maintain.

---

## 5. Promotion Thresholds

### Draft → Reviewed: composite ≥ 60

An entry in `draft` state may advance to `reviewed` when:

1. **Composite score ≥ 60.** No individual dimension sub-score may be below 25 (a single
   dimension at 0–25 signals a structural failure that a 60 composite cannot overcome — the
   entry needs targeted repair, not promotion).
2. **No active P1 E-1 findings** (missing or unverifiable sources that block promotion under
   the Citation Auditor gate).
3. **No active P1 E-2 findings** (schema violations or absent required fields as per the
   Scope Keeper gate).
4. **No active P1 E-3 findings** (arithmetic inconsistencies as per the Numeracy Checker gate).

The editorial gates are independent of the score. An entry scoring 75 with three unresolved
P1 E-1 findings is blocked regardless of score. An entry scoring 62 with no P1 findings may
advance.

**Revision notes requirement:** If the composite is below 60, the scorer must provide
per-dimension notes identifying what is needed to reach the 60 threshold. Notes should be
specific: not "improve citations" but "add a source for `capital_cost` (D2 currently 30;
needs at least 50 to move the composite above 60)." The entry returns to `draft` with these
notes appended to the iteration log.

### Reviewed → Validated: composite ≥ 80 AND all editorial gates pass

An entry in `reviewed` state may advance to `validated` when:

1. **Composite score ≥ 80.** No individual dimension sub-score below 50.
2. **All three editorial gates pass** (no unresolved P1 findings from E-1, E-2, or E-3).
3. **All nine `results:` cells are populated** by the Tier A simulation (not null). Validated
   status requires that the simulation has run and produced output.
4. **Panel review complete:** at least one signed panel review on record; any P1 panel
   findings resolved and documented in the iteration log.

The `validated` bar is intentionally higher than the `reviewed` bar. A `validated` entry is
the project's public-facing quality signal. It represents CERES's claim that the entry is
reliable enough to act on.

### Below 60: back to draft with revision notes

An entry that scores below 60 on re-scoring (whether from initial review or from a re-review
following promotion back to draft) is returned to `draft` status with:

- A per-dimension score breakdown (not just the composite).
- A one-sentence reason per dimension.
- A prioritized list of actions needed to reach 60, ordered by dimension weight (the
  highest-weight dimensions with the largest score gap from band minimum are the highest
  priority).
- A new dated entry appended to the iteration log noting the score and the return to draft.

The author is not penalized for a draft score below 60 if the entry is new; all entries
start in `draft` by definition. The goal of the below-60 protocol is to give actionable
direction, not a verdict.

### Summary table

| Promotion gate | Composite threshold | Dimension floor | Editorial gates | Simulation |
|---|---|---|---|---|
| Draft → Reviewed | ≥ 60 | None below 25 | No P1 findings | Not required |
| Reviewed → Validated | ≥ 80 | None below 50 | All gates pass | All 9 cells populated |
| Below 60 | N/A | N/A | N/A | Return to draft + revision notes |

---

## 6. Aggregating Role Findings into Dimension Scores

This section is **forward-looking**. Scoring is currently performed manually by a scorer
consulting panel and editorial findings. This schema prepares for future scripted aggregation
once tooling is in place to read role `rubric_contribution` fields automatically.

### Aggregation model

Each role file declares `rubric_contribution.primary` and `rubric_contribution.secondary`
lists (added in v1.1). For each dimension D1–D6, the scorer (or future script) aggregates
findings from all roles that contribute to that dimension:

- **Primary contributors** (weight 1.0): roles whose `rubric_contribution.primary` includes
  this dimension. These roles dominate the dimension score.
- **Secondary contributors** (weight 0.5): roles whose `rubric_contribution.secondary`
  includes this dimension. These roles add partial signal.

### Aggregation formula (per dimension)

```
dimension_score = (sum of primary_finding × 1.0 + sum of secondary_finding × 0.5)
                  / (count_primary × 1.0 + count_secondary × 0.5)
```

Where each `finding` is the severity-to-score mapping of the role's highest-severity finding
for that dimension (P1 → 0–25 range; P2 → 26–50; P3 → 51–75; no finding → 76–100 implied
unless the scorer has independent evidence otherwise).

**Special case — zero primary contributors:** If a dimension has no primary contributor but
one or more secondary contributors, the dimension score is set to the highest-severity
secondary finding (i.e., the most critical finding wins rather than an average). This prevents
secondary signals from inflating a dimension that has no domain owner.

### Role-to-dimension mapping (from role v1.1 frontmatter)

| Dimension | Primary roles | Secondary roles |
|-----------|--------------|-----------------|
| D1 Schema Completeness | E-2 Scope Keeper | — |
| D2 Citation Strength | E-1 Citation Auditor | P-1 Market Economist, P-5 Historian |
| D3 Operations Realism | P-4 Craft Practitioner, E-3 Numeracy Checker | P-6 Skeptical Funder |
| D4 Lens-Context Rigor | P-1, P-2, P-3 (market/cooperative/civic sub-lenses) | E-3 Numeracy Checker |
| D5 Historical Honesty | P-5 Historian | P-6 Skeptical Funder |
| D6 Design Rationale & Differentiation | P-6 Skeptical Funder | P-1, P-2, P-3, P-4 |

This table is derived directly from each role's `rubric_contribution` field. If a role file
is updated, this table should be regenerated; the role files are the authoritative source.

---

## 7. Rubric Evolution

### When to raise the bar

The rubric anchors defined in Section 4 represent the current quality floor for each band.
They are not permanent. When an entry demonstrably and repeatedly exceeds the 76–100 anchor
descriptions — when reviewers consistently find that the "76–100" language undersells what
the best entries achieve — the rubric's top band should be raised to reflect the new
exemplary standard.

This ties directly to the Chronicle's "evolving quality" pattern: quality standards are
not fixed externally but emerge from the best work the project has produced. The rubric is
the instrument that translates that pattern into a reviewable, versioned record.

### Protocol for raising an anchor

1. **Identify the exemplar.** An entry (or small set of entries) is cited as clearly
   exceeding the current top-band anchor for one or more dimensions. The scoring committee
   documents specifically what made it exceptional: a narrative explanation, not just a
   score.

2. **Draft revised anchor language.** The new 76–100 descriptor for the relevant dimension
   is drafted to reflect what made the exemplar special. The old 76–100 language becomes the
   floor of the 76–100 band (i.e., it describes the minimum for the top band, not its
   ceiling). The new language describes the aspirational ceiling.

3. **Review for orphan effects.** Before adopting the new language, verify that no existing
   `validated` entry would be downgraded to `reviewed` under the new standard. If any would
   be, those entries are flagged for re-scoring — but they are not automatically demoted.
   The project documents the gap and gives the author a revision window.

4. **Bump the rubric version.** This file's version number (at the top) is incremented. A
   dated entry is added to the rubric iteration log (see below). The change is logged as the
   reason for the version bump.

5. **Communicate the change.** All active entry authors are notified of the anchor change
   and its effective date. Entries already in `reviewed` status are re-scored on their next
   promotion attempt; they are not retroactively demoted based on the new standard.

### Rubric iteration log

- 2026-04-18: v1.0 — initial rubric created. Six dimensions, 100-point composite. Promotion
  thresholds set at 60 (draft → reviewed) and 80 (reviewed → validated). Anchors written
  against the initial corpus of principles and schema documentation; expected to evolve as
  first entries reach `validated` status.

---

## 8. Principle-to-Dimension Coverage Map

The table below confirms that all ten quality principles from `corpus/canon/PRINCIPLES.md`
are covered by at least one rubric dimension. No principle is an orphan.

| Principle | Statement (abbreviated) | Primary Dimension(s) |
|-----------|--------------------------|----------------------|
| P-1 | Schema-Complete | D1 |
| P-2 | Every Number Cited | D2 |
| P-3 | Operations Reality Addressed | D3 |
| P-4 | Lens Context Addressed | D4 |
| P-5 | Market Price Declared | D2, D4 |
| P-6 | Historical Lineage Honest | D5 |
| P-7 | Design Rationale Explicit | D6 |
| P-8 | Failure Modes Named | D3 |
| P-9 | Apprentice Path Present or Flagged | D3, D4 |
| P-10 | Iteration Log Present | D1, D6 |

Panel voice and editorial gate alignment:

| Dimension | Panel Voices | Editorial Gates |
|-----------|--------------|-----------------|
| D1 Schema Completeness | — | E-2 Scope Keeper, E-3 Numeracy Checker |
| D2 Citation Strength | P-1 Market Economist | E-1 Citation Auditor |
| D3 Operations Realism | P-4 Craft Practitioner, P-6 Skeptical Funder | E-3 Numeracy Checker |
| D4 Lens-Context Rigor | P-2 Commons Theorist, P-3 Civic Steward | E-2 Scope Keeper |
| D5 Historical Honesty | P-5 Historian | E-1 Citation Auditor |
| D6 Design Rationale | P-6 Skeptical Funder | E-2 Scope Keeper |

All six panel voices (P-1 through P-6) are mapped to at least one dimension. All three
editorial gates (E-1, E-2, E-3) are mapped to at least one dimension. No voice or gate is
an orphan.
