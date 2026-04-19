---
title: CERES Methodology
version: "1.0"
created: 2026-04-18
spec: specs/2026-04-18-ceres-design.md
companion: docs/STYLE-GUIDE.md
sections:
  - how-we-estimate
  - estimate-defense-standard
  - sanity-check-conventions
  - multi-currency-normalization
  - historical-claims
  - research-paper-vs-due-diligence
  - handling-cross-cultural-disagreement
---

# CERES Methodology

Estimation, cross-check, and validation conventions for all CERES catalog entries
and research documents. This document is the _how we work_ companion to
`docs/STYLE-GUIDE.md`, which covers _how we write_.

**Division of labor:**

- `docs/STYLE-GUIDE.md` — citation format, tone, forbidden framings, unit and
  currency writing rules.
- `docs/METHODOLOGY.md` (this document) — how estimates are constructed, how they
  are defended, what cross-checks are run, and how disagreements are documented.

Every rule below names an editorial enforcement owner (E-1 or E-3) and a severity
(P1 / P2 / P3) consistent with the severity definitions in those roles. Rules are
concrete enough for mechanical enforcement.

---

## 1. How We Estimate

### 1.1 Order-of-magnitude with ranges

CERES estimates are order-of-magnitude unit economics, not supplier quotes. The
correct mental model is: "I am confident this number is in the right $10^n bucket,
and I have a defensible range within that bucket."

Every estimate is expressed as a three-point range using the catalog schema's
`{ low: X, mid: Y, high: Z }` triple:

```yaml
capital_cost: { low: 18000, mid: 28000, high: 45000 }
```

- `low` — a plausible lower bound; favorable conditions, second-hand equipment, or
  the cheapest defensible sourcing scenario.
- `mid` — the central estimate; what a reasonably careful buyer would pay under
  normal conditions. This is the value used in `sim_params.cost_mean`.
- `high` — a plausible upper bound; new equipment, professional installation, cost
  overruns within a realistic range.

Do not collapse this triple to a single point estimate in catalog entry prose or
frontmatter. If you quote only one number, state explicitly that you are quoting
the midpoint: "approximately $28,000 (mid estimate; range $18,000–$45,000)."

**E-1 enforcement trigger:** A single point estimate in a frontmatter field that
schema defines as a triple is a P1 finding (missing range information).

### 1.2 Cite the source for each number

Every number in the `{ low, mid, high }` triple requires a source in the entry's
`sources:` block. The source must be specific enough to allow the reader to
reproduce the estimate:

- For equipment cost: cite a specific equipment listing, trade survey, or published
  cost study with date and table/page number.
- For throughput: cite an operational record, engineering estimate, or primary
  measurement with the conditions stated.
- For maintenance and consumables: cite a maintenance manual, trade-association
  survey, or operational case study.

The annotation pattern in prose is: "Capital costs in the range $18,000–$45,000
[Weisdorf 2018; ToolLibrary.org 2024 survey, Table 3]." Both bounds should be
traceable to the same source or to two sources that together cover the range.

**E-1 enforcement trigger:** Any frontmatter field in the `economics:` or
`sim_params:` block without a matching `sources:` entry is a P1 finding. Uncited
estimate = P1 editorial finding. No exceptions for "obvious" numbers.

### 1.3 High-uncertainty flags

When the estimate is based on limited evidence, analogy, or interpolation — rather
than direct observation — flag it explicitly in the entry's `## Key assumptions`
prose section using the labels `high`, `mid`, or `low` uncertainty matching the
catalog schema:

```markdown
## Key assumptions

- Capital cost ($18,000–$45,000): **mid uncertainty**. Based on two comparable
  community forge installations [sources]. Sparse data; only two comparators.
- Throughput (6 small-work units/hr): **low uncertainty**. Directly measured in
  three operating forges [sources]. Consistent across sources.
- Market price per unit ($32–$70): **high uncertainty**. No direct market survey
  for community forge output pricing. Derived from industrial pricing premium
  observed in comparable direct-to-consumer craft markets [sources]. Author's
  interpolation; independent verification needed before promotion.
```

These labels propagate to the review workflow: a `high`-uncertainty number in a
load-bearing position should receive explicit E-3 scrutiny before the entry is
promoted from `draft` to `reviewed`.

**E-3 enforcement trigger:** A `high`-uncertainty number used as a point estimate
in `sim_params` without a prose flag is a P2 finding.

---

## 2. Estimate Defense Standard

An estimate is **defensible** if and only if both of the following hold:

1. **The source is reachable.** A reader following the citation can locate the
   source — it exists, it resolves, it is not a dead URL or a misquoted journal
   article, and it contains the material cited.

2. **The source supports the claim.** The source's stated value, range, or
   methodology actually supports the number in the catalog entry. A source that
   contains a capital cost figure for a different type of equipment, at a different
   scale, in a different decade, without documented adjustment, does not support
   the claim even if it is findable.

These two conditions define the defense standard. An estimate that fails either
condition is not defensible, regardless of how plausible the number looks.

### 2.1 Uncited estimate = P1 editorial finding

An estimate with no source at all is automatically a P1 finding for E-1. There is
no threshold below which an estimate is "small enough not to need a source." If a
number appears in a frontmatter field or is used in a calculation, it has a source
or it is flagged P1.

This rule applies to:
- All fields in `economics:` (capital_cost, install_cost, annual_maintenance,
  annual_consumables, floor_space_rent_per_year, market_price_per_unit).
- All fields in `sim_params:` (cost_mean, cost_sd, throughput_units_equiv_per_year,
  variable_cost_per_unit, labor_hours_per_unit, downtime_fraction, lifespan_years).
- Any number that appears in the `## Key assumptions` prose section.

**Gate rule (from E-1):** Three or more P1 citation findings in a single entry hold
that entry from promotion to `reviewed` until resolved.

### 2.2 Source quality hierarchy

Sources are ranked in the order defined in `docs/STYLE-GUIDE.md` Section 2. For
catalog entry economics specifically:

1. **Primary:** peer-reviewed cost studies, government statistical series,
   trade-organization equipment surveys with stated methodology.
2. **Secondary:** academic books citing primary research; established economic
   history literature for historical cost comparisons.
3. **Grey literature (acceptable when primary/secondary unavailable):** industry
   association reports, NGO surveys — must be named explicitly with provenance.
4. **Not acceptable as sole support:** blog posts, Wikipedia, press releases,
   personal communications. These may appear as context but cannot be the sole
   citation for any number in the entry.

Using a source below the acceptable threshold as the sole citation for a
load-bearing economic figure is a P1 finding for E-1.

---

## 3. Sanity-Check Conventions

This section formalizes the cross-checks that E-3 (Numeracy Checker) runs on every
catalog entry. These are the working rules E-3 applies; METHODOLOGY.md makes them
explicit so authors can self-check before review.

The cross-checks fall into four families: **throughput ↔ labor**, **payback ↔
revenue**, **order-of-magnitude**, and **results-block consistency**. Currency
normalization is addressed separately in Section 4.

### 3.1 Throughput ↔ labor cross-check

**Formula:**

```
annual_throughput_implied =
    max_active_hours_per_week × 52 × (1 - downtime_fraction) / labor_hours_per_unit
```

This implied annual throughput must be approximately equal to
`sim_params.throughput_units_equiv_per_year`. "Approximately" means within the
same order of magnitude; a factor-of-2 discrepancy is a P2; a factor-of-10
discrepancy is a P1.

**Worked example** (forge-003 from spec Section 5):

```
max_active_hours_per_week = 45
downtime_fraction         = 0.12
labor_hours_per_unit      = 0.6

annual_throughput_implied = 45 × 52 × (1 - 0.12) / 0.6
                          = 45 × 52 × 0.88 / 0.6
                          = 2,059.2 / 0.6
                          = 3,432 units/year
```

The entry states `throughput_units_equiv_per_year: 2400`. The implied value is
3,432 — a ratio of 1.43. This is within the same order of magnitude but is a P2
(within-order-of-magnitude discrepancy). The author should reconcile: either
`max_active_hours_per_week` is overstated, `labor_hours_per_unit` is too low, or
`throughput_units_equiv_per_year` needs a note explaining that the forge is not
run at full capacity for all active hours (e.g., setup, tool changes, heat-up
time). Document the reconciliation in `## Key assumptions`.

**E-3 severity:**
- Factor of 10 or more between implied and stated throughput: **P1** (block
  promotion).
- Factor of 2–10 discrepancy: **P2** (should fix; document reconciliation).
- Factor under 2 with a plausible explanation: **P3** (note it; no block).

### 3.2 Payback ↔ revenue cross-check

**Formula:**

```
annual_revenue           = throughput_units_equiv_per_year × market_price_per_unit.mid
annual_variable_costs    = throughput_units_equiv_per_year × variable_cost_per_unit
annual_labor_cost        = throughput_units_equiv_per_year × labor_hours_per_unit × wage_rate
annual_fixed_costs       = annual_maintenance + annual_consumables + floor_space_rent_per_year
annual_net               = annual_revenue - annual_variable_costs - annual_labor_cost
                           - annual_fixed_costs
payback_implied          = capital_cost.mid / annual_net
```

The `payback_implied` must be consistent with any payback figure stated in the
entry's prose or lens results. For the MARKET lens, the pass condition is payback
≤ 8 years (spec Section 6); an entry that claims MARKET=win with an implied payback
of 12 years is a P1 internal contradiction.

**Note on `wage_rate`:** Use the scale-appropriate median wage defined in
`corpus/program/SCALES.md`. This is the wage threshold that also appears in the
MARKET lens pass condition (operator earns ≥ scale-appropriate median wage). Using
a different wage for the payback formula than for the lens evaluation would produce
a circular inconsistency — E-3 checks for this.

**Worked example** (forge-003, using spec Section 5 values and the MARKET lens):

```
throughput_units_equiv_per_year = 2,400
market_price_per_unit.mid       = $45
variable_cost_per_unit          = $3.10
labor_hours_per_unit            = 0.6  → assume $20/hr town median wage
annual_maintenance              = $1,500
annual_consumables              = $4,200
floor_space_rent_per_year       = $4,800
capital_cost.mid                = $28,000

annual_revenue      = 2,400 × $45         = $108,000
annual_variable     = 2,400 × $3.10       =   $7,440
annual_labor        = 2,400 × 0.6 × $20   =  $28,800
annual_fixed        = $1,500 + $4,200 + $4,800 = $10,500

annual_net          = $108,000 - $7,440 - $28,800 - $10,500 = $61,260
payback_implied     = $28,000 / $61,260   ≈ 0.46 years
```

A payback of 0.46 years is implausibly short for a $28,000 capital investment. This
signals that either the market price ($45/unit) is too high relative to the cost
structure, or the throughput (2,400 units/year) is being compared against a price
set for a much lower-volume premium product. E-3 flags this as a P2 — the numbers
are internally consistent (no arithmetic error) but the conclusion demands scrutiny
and the author must document why the payback is this short and whether it holds under
the low-price scenario.

**E-3 severity:**
- Claimed payback contradicts formula by more than one order of magnitude: **P1**.
- Formula result inconsistent with lens verdict (e.g., implied payback 12 years but
  MARKET=win): **P1**.
- Formula result implausibly short or long without explanation in `## Key
  assumptions`: **P2**.

### 3.3 Order-of-magnitude sanity check

**Rule:** The capital cost of a catalog entry must sit in a plausible order-of-magnitude
bracket for the type, size, and complexity of equipment described. E-3 maintains
an informal order-of-magnitude reference:

| Equipment class | Expected capital range |
|---|---|
| Compact single-user forge (propane/induction) | $1,000–$10,000 |
| Medium shared forge (coal/induction, community scale) | $10,000–$100,000 |
| Large civic or industrial forge | $100,000–$1,000,000+ |
| Artisan bread oven (single baker) | $2,000–$20,000 |
| Community bread oven (shared, wood-fired) | $10,000–$80,000 |
| Floor loom (single weaver) | $500–$5,000 |
| Production loom (power, small-batch) | $5,000–$50,000 |

These ranges are indicative — a well-cited entry that falls outside them is not
automatically wrong. But an entry that falls outside the bracket without explanation
triggers an E-3 sanity check: "this entry claims $280,000 for a compact propane
forge — is there a decimal error?"

**E-3 severity:**
- Capital cost more than one order of magnitude outside the expected bracket with
  no explanation: **P1** (probable decimal/unit error).
- Capital cost at the edge of the expected bracket with no explanation: **P2**
  (author should document why).

### 3.4 Results-block consistency

The 9-cell `results:` block (3 scales × 3 lenses) must be internally consistent.
Consistency means:

- If `village_market: fail` and `small_city_market: win`, then `town_market` should
  not be `fail` unless the scaling dynamics cross a non-linear threshold that is
  documented in `## Design rationale` or the entry's `## Key assumptions` section.
  A monotonic improvement across scales without explanation is P3 (note it). A
  non-monotonic result without explanation is P2.
- The same entry cannot claim `cooperative: fail` at all scales while claiming
  `market: win` at all scales if the economics that drive the market verdict also
  make cooperative viable. If the verdicts diverge, the `## Design rationale` must
  explain why (e.g., "market lens benefits from single-operator efficiency; coop
  requires splitting revenue, which breaks the payback").
- Verdict labels (`win` / `marginal` / `fail`) must match the primary numeric metric
  as evaluated by the lens rule in `corpus/program/ECONOMIC-LENSES.md`. A `win`
  label with a payback of 14 years is a P1.

**E-3 severity:**
- Verdict label inconsistent with the numeric metric: **P1**.
- Non-monotonic scale progression without explanation: **P2**.
- Monotonic pattern without explanation (may be correct but undefended): **P3**.

### 3.5 Precision honesty

Order-of-magnitude estimates should carry order-of-magnitude precision. Do not
express an estimate that is accurate to ±50% with three significant figures:

- **Wrong:** `capital_cost.mid: 27,847` (implies precision of $1 on a figure that
  could plausibly be $18,000–$45,000).
- **Right:** `capital_cost.mid: 28000` (or `28,000` in prose; one significant figure
  in the $10,000s).

**Guideline:** Round to two significant figures for order-of-magnitude estimates.
Use three significant figures only when the cited source provides three-significant-
figure precision and the claim is about a narrow range.

**E-3 severity:**
- Three-or-more significant figures on an order-of-magnitude estimate: **P3**
  (style; does not block promotion, but should be noted).

---

## 4. Multi-Currency Normalization

Catalog entries are authored in the currency that best matches the source data
(declared in `economics.currency`). Cross-currency comparison happens only at
evaluation time using the FX snapshot table in `corpus/program/CURRENCIES.md`.

This section documents the process. Writing rules (declaration, prose currency,
no inline conversions) are in `docs/STYLE-GUIDE.md` Section 5.

### 4.1 The FX snapshot table

`corpus/program/CURRENCIES.md` is the single FX reference for the project. It
contains:
- A snapshot date (the date the rates were recorded).
- Exchange rates from each catalog currency to the project base currency (USD).
- The source for the rates (e.g., ECB reference rate, Federal Reserve H.10 release).

Authors do not maintain this table. It is updated as a deliberate project action
when:
1. A new currency enters the catalog (a new entry is authored in a new currency).
2. The existing snapshot is more than 12 months old and a new evaluation run is
   being performed.

When a rate is updated, the snapshot date changes and the prior rate is preserved
in the file's history (git log). Evaluation output that cites a specific snapshot
date remains valid for that rate; it is not silently invalidated by a rate update.

### 4.2 Evaluation normalization process

When Tier A simulation evaluates entries denominated in different currencies, the
process is:

1. Read `economics.currency` from each entry.
2. Look up the rate for that currency in `corpus/program/CURRENCIES.md` using the
   current snapshot.
3. Multiply all cost and revenue fields by the rate to get USD-equivalent values.
4. Record the snapshot date used in the simulation run's output metadata.
5. Compare normalized values across entries.

Do not perform this normalization manually in catalog entry prose or playbook files.
It happens only in simulation output.

### 4.3 Snapshot-date matters — cite it

Any simulation result that compares entries across currencies must cite the FX
snapshot date used. A result from a 2025 simulation run citing a 2023 snapshot is
not wrong, but the snapshot date must be visible so a reader can assess whether
currency movements are material to the verdict.

**E-1 enforcement trigger:** Cross-currency simulation output without a cited
snapshot date is a P2 finding. The snapshot date is a required piece of
reproducibility metadata.

### 4.4 Historical cost data in historical currencies

Historical costs cited in pre-modern or historical monetary units (shillings,
livres, thalers, koku, maravedís, or other non-decimal currencies) are a special
case:

1. State the value in the original unit as cited: "4 shillings per week
   [Dyer 2002, p. 214]."
2. If a modern-currency conversion is needed for comparison, use the methodology
   documented in `corpus/program/CURRENCIES.md`: CPI adjustment to a common year,
   then FX conversion to USD, with the CPI series cited.
3. Label the conversion explicitly: "approximately $X in 2024 USD (CPI-adjusted
   using [series], converted via [rate])."

**E-1 enforcement trigger:** A historical-currency conversion without a stated
methodology is a P1 finding.

---

## 5. Historical Claims

Historical claims — assertions about how things worked, what they cost, what
throughput was achievable, what labor was required — require citation to serious
economic-history or primary-source literature.

### 5.1 Acceptable source types for historical claims

In order of preference:
1. Primary sources: archaeological records, administrative documents, guild accounts,
   price series (e.g., Phelps Brown and Hopkins, Allen wage series, Broadberry GDP
   estimates), court records, estate inventories.
2. Economic-history literature: peer-reviewed journals (_Economic History Review_,
   _Journal of Economic History_, _European Review of Economic History_, _Journal of
   Global History_, and similar), established economic-history monographs.
3. Specialist archaeology and materials-science literature for claims about physical
   processes (furnace temperatures, metallurgical requirements, kiln chemistry).

### 5.2 Unacceptable as sole support

The following source types are **not acceptable as the sole citation** for any
load-bearing historical claim:

- Wikipedia.
- General popular-press books or articles (journalism, trade-press history, popular
  nonfiction) unless they directly cite and quote a primary or peer-reviewed source,
  in which case cite the primary source, not the popular account.
- Personal communications or unpublished manuscripts.
- YouTube documentaries, podcasts, or blog posts, regardless of author credentials.

**E-1 enforcement trigger:** A load-bearing historical claim supported only by
Wikipedia or popular-press citation is a **P1 finding**. This applies to:
- Any historical per-unit cost, throughput figure, or labor requirement cited in
  `## Historical lineage` or used to calibrate `sim_params`.
- Any claim about what historical craftspeople could or could not do that is used
  to justify a catalog design choice.
- Any claim about historical guild structure, labor regime, or market conditions
  cited in research documents.

### 5.3 Strength-of-evidence labeling

When the historical evidence base is thin, say so explicitly. Thin evidence is not
disqualifying — much of economic history rests on fragmentary records — but
undisclosed thinness is a form of overconfidence.

Use explicit hedges:
- "The archaeological record for X is thin before [date]; the following figures
  derive from [source type] and should be treated as order-of-magnitude estimates."
- "No direct throughput figures survive for this trade in this culture; the estimate
  below is derived by analogy from [comparable trade / culture / period] and labeled
  accordingly."

Undisclosed thin evidence in a load-bearing position is a P2 finding for E-1
(missing provenance disclosure).

---

## 6. Research-Paper Level vs. Due-Diligence Level

CERES is **not** a due-diligence exercise. This non-goal is stated explicitly in
spec Section 13 and is restated here because the distinction has practical
consequences for how estimates are constructed and defended.

### 6.1 What this project is

CERES produces **research-paper-level estimates**: order-of-magnitude unit
economics with citations, intended to inform decisions about what is worth
investigating further. The intended use is:

- A funder deciding whether local forge viability is worth a pilot investment.
- A municipality assessing whether a civic forge would pencil out before commissioning
  a feasibility study.
- A researcher testing the hypothesis that equipment economics were the binding
  constraint on local production decline.

The numbers are designed to be right at the order-of-magnitude level. A playbook
recommendation of "forge-003 achieves payback in approximately 6 years under the
market lens at town scale" means: "our analysis, based on cited order-of-magnitude
estimates, puts payback in the range of 3–10 years; we do not know whether it is
5.3 or 7.8 years."

### 6.2 What this project is not

CERES does **not** produce:
- Real supplier BOMs (bill of materials with actual vendor quotes).
- Real procurement plans (sourcing strategy, vendor qualification, lead times).
- Due-diligence-grade financial models (auditable, with verified cost data, signed
  contracts, or engineer's estimates).
- Investment-grade feasibility studies (site-specific, regulatory-cleared, with
  professional sign-off).

Any catalog entry that implies procurement-ready precision — exact vendor pricing,
specific lead times stated as facts rather than estimates, specific site assessments
— has overstepped the project's scope.

**E-2 enforcement trigger:** A catalog entry that implies due-diligence precision
(e.g., "Installation cost: $6,247.50" presented as an actual quote rather than an
estimate) is a P2 scope finding. The precision misrepresents what CERES numbers are.

### 6.3 The numbers inform; they do not book procurement

This distinction is not a hedge — it is a constraint on how the numbers may be used
and how they should be presented. A CERES playbook recommendation is an invitation
to investigate further, not a procurement authorization. Any reader who acts on CERES
numbers without independent verification is misusing the catalog.

This constraint also defines the quality floor: order-of-magnitude estimates that
are defensibly cited and cross-checked internally are good CERES numbers. They are
not good numbers for booking a $28,000 equipment purchase without independent
verification. Both statements are true simultaneously.

---

## 7. Handling Disagreement Across Anchor Cultures

CERES uses 4–6 anchor cultures as research foundations. These cultures operated
under different resource constraints, organizational forms, regulatory environments,
and demand patterns. When their functional requirements diverge, the correct
response is to **document the divergence**, not to collapse it to a consensus.

### 7.1 The divergence-first principle

When two or more anchor cultures produce functionally incompatible requirements for
the same trade, document both requirements and their sources. Do not:
- Average them into a synthetic requirement that neither culture actually had.
- Silently pick the requirement that makes the catalog design work and omit the
  other.
- Treat one culture's requirement as the "default" without argument.

**Example:** Medieval Northern European smithing was coal- and charcoal-intensive
(mature iron technology, cold climates, abundant forest cover). Song-era Chinese
smithing was coke- and blast-intensive at industrial scale (Needham documents
large-scale iron production from the 11th century). These functional requirements
differ in fuel type, scale, and technology level. A catalog entry for a "historical
forge design" that silently picks one culture's model over the other's has made a
design choice without documenting it.

**What to write instead:** Document both in `## Historical lineage`, name the
cultures, cite the sources, and state which model the catalog entry follows and why.
If the design is a modern synthesis that draws on neither historical form directly,
say so.

### 7.2 Fuel-type divergence

Fuel-type divergence is a common and important case. The anchor cultures used:
- Coal (medieval Northern Europe, industrial Britain, American frontier)
- Charcoal (most pre-coke iron cultures; default for high-quality iron)
- Wood (lower-temperature applications across cultures)
- Coke (Song-era China in certain periods; modern industrial default)
- Dung / peat (lower-resource contexts; some pre-industrial peripheries)

A catalog entry for a forge must declare its fuel type and explain why that fuel
was chosen for the modern design, not because "that's what was historically used"
(which suppresses the divergence) but because "the modern context has the following
characteristics that make this fuel appropriate: [reasons]."

When functional requirements across cultures diverge on fuel type, document all
observed fuel types with citations and record the divergence in the trade's
`research/trades/<trade>/REQUIREMENTS.md` file, not just in individual catalog
entries. This file is the canonical record of cross-cultural functional requirements.

### 7.3 Scale and organizational divergence

Cultures also diverge on production scale and organizational form:
- Shared civic forge vs. family forge vs. guild-controlled forge vs. itinerant
  smith all appear in different anchor cultures.
- The same trade may have operated at radically different scales under different
  organizational forms within the same culture.

Document these divergences in `research/trades/<trade>/HISTORICAL-FORMS.md`. When
a catalog entry is inspired by one specific historical form, name that form and its
culture explicitly in `## Historical lineage`. When it synthesizes across forms,
name all contributing forms.

### 7.4 When divergence is the finding

Sometimes the divergence itself is the finding: the fact that Song-era Chinese
smithing operated at industrial scale while simultaneously Tokugawa Japanese
smithing was small-scale and guild-controlled may be more informative than any
single requirement extracted from either culture. In this case, the correct output
is a note in the trade's `REQUIREMENTS.md` documenting the divergence as a finding,
with the implications for the CERES working hypothesis spelled out.

A disagreement that is documented and analyzed is a contribution. A disagreement
that is suppressed in favor of a convenient consensus is a distortion.

---

## Self-Review Checklist

Before committing any catalog entry or research document, the author confirms:

**Estimation (Section 1)**
- [ ] All economic estimates use `{ low, mid, high }` triples; no collapsed point
      estimates without explicit labeling.
- [ ] Every number in the triple has a source in the `sources:` block.
- [ ] High-uncertainty estimates are flagged in `## Key assumptions` using the
      `high` / `mid` / `low` labels.

**Estimate defense (Section 2)**
- [ ] Every `sources:` entry is a real, findable source.
- [ ] Every source supports the specific claim it is cited for.
- [ ] No frontmatter economic field is uncited.

**Cross-checks (Section 3)**
- [ ] Throughput ↔ labor formula runs within acceptable tolerance (see 3.1).
- [ ] Payback ↔ revenue formula is consistent with lens verdicts (see 3.2).
- [ ] Capital cost sits in the expected order-of-magnitude bracket, or the
      deviation is explained (see 3.3).
- [ ] 9-cell results block is internally consistent across scales and lenses
      (see 3.4).
- [ ] Precision is honest: order-of-magnitude estimates use two significant figures
      (see 3.5).

**Currency (Section 4)**
- [ ] `economics.currency` is declared.
- [ ] No cross-currency comparisons in prose.
- [ ] Historical currency conversions cite the conversion methodology.

**Historical claims (Section 5)**
- [ ] Every load-bearing historical claim cites peer-reviewed or primary-source
      literature.
- [ ] No load-bearing historical claim is supported only by Wikipedia or popular
      press.
- [ ] Thin evidence is disclosed with an explicit hedge.

**Scope (Section 6)**
- [ ] No numbers imply due-diligence or procurement precision.
- [ ] No entry presents order-of-magnitude estimates as supplier quotes.

**Cross-cultural divergence (Section 7)**
- [ ] Where anchor cultures disagree on functional requirements, the divergence is
      documented, not suppressed.
- [ ] The entry's `## Historical lineage` names its source culture(s) explicitly.
