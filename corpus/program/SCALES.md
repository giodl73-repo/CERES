---
title: CERES Scale Parameters
version: "1.0"
created: 2026-04-18
spec: specs/2026-04-18-ceres-design.md §3 §6
companion_theory: corpus/canon/THEORY.md §4
companion_methodology: docs/METHODOLOGY.md §3
---

# CERES Scale Parameters

This document is the **single authoritative reference for scale-level parameters**
used throughout CERES simulation, evaluation, and playbook work. It defines the
three settlement scales as first-class variables, specifies the per-scale threshold
values used by the three economic lenses (MARKET, COOPERATIVE, CIVIC), and documents
the reasoning and sources behind every threshold.

**Division of labor:**

- This document — scale definitions, population ranges, derived household counts,
  all lens-threshold dollar values, member-pool formulas, and geographic assumptions.
- `corpus/program/ECONOMIC-LENSES.md` — the formulas that consume these thresholds
  (payback rule, break-even member count rule, per-household cost rule). Do not
  duplicate the formulas here; do not duplicate the thresholds there.
- `corpus/canon/THEORY.md` §4 — the conceptual role of scale as a first-class
  variable. Do not duplicate parameter values there.
- `docs/METHODOLOGY.md` §3 — the wage cross-check rule and how the labor cost in
  `sim_params` must match the scale-appropriate median wage defined here.

> **Illustrative anchors — to be refined before any simulation run that depends
> on them.** All threshold values in this document are order-of-magnitude anchors
> grounded in cited published data. They must be reviewed against the most current
> available BLS, ACS, ALA, and cooperative-literature sources before a simulation
> run is promoted from `draft` to `validated`. The methodology for that review is
> the same labeling protocol used in `corpus/program/CURRENCIES.md`: replace the
> anchor with a cited current value and log the change in the Appendix.

---

## 1. Three Scales

*(Spec Section 3; THEORY.md §4)*

CERES evaluates every catalog entry at three settlement scales. Scale is a
**first-class simulation variable**, not a post-hoc filter. An entry evaluated at
`town` scale uses the town parameters defined in this document for every lens
threshold.

| Scale | Population range | Shorthand used in code and frontmatter |
|---|---|---|
| Village | 500 – 2,000 | `village` |
| Town | 2,000 – 15,000 | `town` |
| Small city / district | 15,000 – 75,000 | `small_city` |

**Rationale for these ranges.** The ranges are drawn from spec Section 3 (locked
scope decision). They correspond roughly to:

- **Village (500–2,000):** A single-precinct rural or exurban settlement. Below 500
  the demand pool for artisan goods is too thin to evaluate meaningfully under any
  lens. Above 2,000 the settlement typically acquires a second commercial node and
  moves into town dynamics.
- **Town (2,000–15,000):** A small incorporated municipality or market town. Has a
  recognizable commercial district, some local services, and a labor pool large
  enough to staff a shared facility. The majority of US rural county seats fall in
  this range.
- **Small city / district (15,000–75,000):** A small regional center or a dense
  urban district within a larger metro. Has multiple civic institutions, a
  diversified labor market, and access to municipal financing. Above 75,000 the
  economics shift significantly toward metro patterns outside CERES scope.

These are **not** demographic cutoffs for project-scope filtering; they are the
ranges over which CERES parameterizes scale-dependent thresholds. A catalog entry
may also note real-world comparators within each range in its `## Historical lineage`
section.

---

## 2. Per-Scale Parameters Table

> All USD values are **illustrative anchors** as of 2026-04-18. See Section 3
> (median-wage thresholds), Section 4 (civic cost thresholds), and Section 5
> (member-pool formulas) for derivation and citations.

| Parameter | Village (500–2,000) | Town (2,000–15,000) | Small city (15,000–75,000) |
|---|---|---|---|
| **Population midpoint** (used in sim when a single representative value is needed) | 1,000 | 7,500 | 40,000 |
| **Typical household count** (population × 0.40) | 400 | 3,000 | 16,000 |
| **Scale-appropriate median wage** (USD/yr, MARKET lens threshold) | $48,000 | $56,000 | $62,000 |
| **Per-household civic-cost threshold** (USD/yr, CIVIC lens pass ceiling) | $120 | $100 | $80 |
| **Feasible member-pool size** (% of population, COOPERATIVE lens) | 2.5 % | 2.5 % | 2.0 % |
| **Feasible member pool at midpoint** (people; pop × rate) | 25 | 188 | 800 |
| **Local supplier density assumption** | thin | moderate | dense |

**Column notes:**

- *Household count* uses a 0.40 multiplier (average ~2.5 persons per household),
  consistent with US Census Bureau average-household-size data for non-metro and
  small-metro communities. [US Census Bureau, American Community Survey 5-year
  estimates, Table B25010, ~2022–2023 release.]
- *Median wage* decreases as settlement size decreases, reflecting BLS Occupational
  Employment and Wage Statistics (OEWS) cross-tabulated with ACS place-size data.
  See Section 3 for derivation.
- *Per-household civic-cost threshold* decreases (becomes more stringent) as
  settlement size grows, because larger settlements have more expensive competing
  service demands on the municipal budget and a lower tolerance per-capita for
  single-facility costs. See Section 4.
- *Feasible member-pool percentage* is slightly lower for small cities because the
  larger absolute pool means break-even is easier to reach, and the fraction needed
  is less; simultaneously, urban anonymity tends to reduce cooperative participation
  rates relative to tight-knit town communities. See Section 5.
- *Supplier density* is a qualitative input to COOPERATIVE and MARKET lens
  narrative notes; it is not a numeric threshold but informs the `lens_context`
  competitive-environment text authors must write.

---

## 3. Median-Wage Thresholds (MARKET Lens)

### 3.1 Pass condition

The MARKET lens passes if the operator's annual take-home after all costs (including
capital service, consumables, maintenance, and floor-space rent, but before personal
income tax) is **≥ the scale-appropriate median wage** for that settlement size.
The formula lives in `corpus/program/ECONOMIC-LENSES.md`; the threshold values are
defined here.

### 3.2 Derivation

US median household income was approximately **$74,580** for all households in 2022
(US Census Bureau, Current Population Survey, 2023 Annual Social and Economic
Supplement; Table H-8). This is a household income figure. For CERES purposes the
relevant measure is **individual annual earnings** for a full-time worker in a
craft or skilled-trades occupation, which is lower, and which varies by settlement
size.

BLS Occupational Employment and Wage Statistics (OEWS, May 2023 release) for
skilled-trades occupations (SOC major group 47 — Construction and Extraction, and
SOC 51 — Production) shows national median annual wages in the $42,000–$58,000
range, varying by specific occupation, region, and establishment size.

US Census Bureau American Community Survey (ACS) 5-year estimates (2018–2022,
Table B20002) document median earnings for full-time, year-round workers by
place-size. Workers in places below 10,000 population earn roughly 15–25% less than
workers in places above 25,000 population, controlling broadly for occupation class.
The ACS microdata (PUMS) shows this gradient is strongest in the lower quartile of
occupational wages, which is the reference class for craft-production operators.

**Threshold values applied:**

| Scale | Median wage threshold | Derivation note |
|---|---|---|
| Village (500–2,000) | **$48,000 / yr** | Lower end of BLS OEWS trades median (~$42k–$50k range), discounted ~10% for small-place wage gradient vs. national median |
| Town (2,000–15,000) | **$56,000 / yr** | BLS OEWS trades median midpoint; approximately equals $20/hr × 2,080 hr/yr × 1.35 (to capture benefits / burden rate at operator-owner scale) — this is the $20/hr figure used in `docs/METHODOLOGY.md` §3 worked example |
| Small city (15,000–75,000) | **$62,000 / yr** | Upper portion of BLS OEWS trades median for skilled production/construction in communities 15k–100k; ~$30/hr at part-time equivalent or ~$22/hr FTE |

> **Illustrative anchor — to be refined against actual sources before any
> simulation run that depends on it.** Recommended refinement: pull BLS OEWS
> May release for the target year, filter to SOC groups 47 and 51, and cross-tab
> against BLS QCEW establishment-size data or ACS place-size categories to
> anchor each threshold against a specific published percentile.

### 3.3 Hourly-rate equivalents (for sim_params labor_hours_per_unit field)

When catalog entry authors need an hourly rate rather than an annual figure:

| Scale | Annual threshold | Implied hourly rate (÷ 2,080 hr) |
|---|---|---|
| Village | $48,000 | ~$23 / hr |
| Town | $56,000 | ~$27 / hr |
| Small city | $62,000 | ~$30 / hr |

The `docs/METHODOLOGY.md` §3 worked example uses $20/hr for town; that figure
represents a pre-burden operator wage. The $27/hr figure here is the **take-home
threshold after costs**, which is the correct comparison for the MARKET lens pass
condition. Authors must not confuse the two: the `labor_hours_per_unit` cost in
`sim_params` uses the pre-burden wage rate; the MARKET lens pass condition compares
residual income to the annual threshold in this table.

---

## 4. Civic Cost Thresholds (CIVIC Lens)

### 4.1 Pass condition

The CIVIC lens passes if the **per-household annual cost** of the facility (capital
amortized over 25–40 years plus annual operating costs, divided by total households
in the settlement) is **≤ the threshold** for that scale. The formula lives in
`corpus/program/ECONOMIC-LENSES.md`; the threshold values are defined here.

### 4.2 Benchmark: public library per-capita cost

The American Library Association (ALA) tracks annual public library expenditure per
capita in its *Public Library Survey* (PLS), conducted annually by the Institute of
Museum and Library Services (IMLS). The most recently published full-cycle survey
data (IMLS, *Public Library Survey*, FY 2021, published 2023) reports:

- National median operating expenditure per capita: **~$40–$55** across all
  reporting libraries.
- Libraries in communities of 1,000–2,499 (village range): median ~$35–$50/capita.
- Libraries in communities of 2,500–9,999 (lower town range): median ~$40–$55/capita.
- Libraries in communities of 10,000–24,999 (upper town / lower small-city range):
  median ~$45–$65/capita.
- Higher-income jurisdictions and larger cities trend toward $70–$90/capita or more.

Per-household costs are approximately per-capita figures × 2.5 (average household
size). Therefore, a library in the mid-range per-capita band costs roughly
**$100–$162 per household per year** in operating expenditures alone, before capital
amortization.

The CERES CIVIC lens threshold asks whether a civic artisan facility can be
justified at **a lower per-household cost than a library**, given that libraries
serve a broader and more universal constituency. A manufacturing facility serves a
subset of residents and should face a tighter budget justification than a universal
service.

**Threshold values applied:**

| Scale | Per-household annual cost threshold | Derivation note |
|---|---|---|
| Village (500–2,000) | **$120 / household / yr** | Slightly above library operating-cost midpoint (~$100–$112/hh) to reflect that a shared-use production facility may have community-economic-development justification comparable to library services; gives some headroom over strict library parity |
| Town (2,000–15,000) | **$100 / household / yr** | Approximately at library operating-cost lower bound; production facilities in towns face more competing budget priorities than in villages where the facility may be the only economic anchor |
| Small city (15,000–75,000) | **$80 / household / yr** | Below library operating cost — cities have larger municipal budgets but also far more competing civic services; a production facility at city scale must be unusually cost-efficient to pass the CIVIC lens |

> **Illustrative anchor — to be refined against actual sources before any
> simulation run that depends on it.** Recommended refinement: pull the most recent
> IMLS Public Library Survey for the target year (https://www.imls.gov/research-evaluation/data-collection/public-libraries-survey),
> filter to locale-code categories corresponding to each scale, and compute the
> median per-capita operating expenditure. Multiply by 2.5 for per-household
> equivalent. Use as the comparison benchmark; adjust thresholds with documented
> rationale if the current data has shifted materially from these anchors.

### 4.3 Capital amortization note

The CIVIC lens includes amortized capital in the per-household cost. The spec
(Section 6) uses a 25–40 year amortization window. Shorter windows (25 years)
produce higher per-year costs and are more conservative; longer windows (40 years)
are appropriate for purpose-built civic buildings. The `ECONOMIC-LENSES.md`
formula will specify the default; authors may override with justification.

---

## 5. Feasible Member-Pool Formulas (COOPERATIVE Lens)

### 5.1 Pass condition

The COOPERATIVE lens passes if the **break-even member count** (the minimum number
of members whose dues and labor contributions close the economics) is **≤ the
feasible member pool** at that scale. The formula for break-even member count is
in `corpus/program/ECONOMIC-LENSES.md`; the feasible pool formula is defined here.

### 5.2 Formula

```
feasible_member_pool = population × participation_rate
```

where `participation_rate` is the scale-specific fraction of residents who will
actively join and sustain membership in a tool-sharing or production cooperative
over a 3–5 year operating window.

### 5.3 Participation rate by scale

| Scale | Participation rate | Resulting pool at midpoint population |
|---|---|---|
| Village (pop midpoint 1,000) | **2.5 %** | 25 members |
| Town (pop midpoint 7,500) | **2.5 %** | 188 members |
| Small city (pop midpoint 40,000) | **2.0 %** | 800 members |

### 5.4 Derivation and citations

**Tool-library network evidence.** The North American Tool Library Network
(NATLN / Toronto Tool Library, Vancouver Tool Library, and peer organizations)
has reported membership levels of approximately **1–3% of surrounding neighborhood
or municipal population** in established operations (typically defined as 3–5 years
post-launch). A representative figure often cited in cooperative-sector reporting
is that tool libraries operating in urban neighborhoods of 10,000–50,000 residents
reach 200–800 active members, which implies 0.8–2% penetration in dense urban
areas and up to 3–4% in smaller, tight-knit communities.

**Cooperative literature.** General cooperative sector research (International
Co-operative Alliance annual reports; Zeuli and Radel 2005, *Journal of Agricultural
and Applied Economics*, on rural cooperative participation) documents that rural and
small-town cooperatives achieve higher participation rates as a share of the
addressable population than urban cooperatives, due to stronger social network
density and fewer competing services. This supports a modestly higher rate
(2.5% vs. 2.0%) for village and town relative to small city.

**Bolder Research / Sharing Economy context.** Botsman and Rogers (2010, *What's
Mine is Yours*) document early sharing-economy platform penetration rates in the
low single-digit percentages of local populations, consistent with the 2–3% range
used here. Later empirical research (PwC / OurSharingEconomy surveys, 2014–2019)
found platform participation rates of 1–5% in markets where the service had been
operating for 3+ years.

**Conservatism rationale.** CERES uses the **lower end of the 1–3% empirical range
plus a modest rural premium** rather than optimistic projections. A 2.5% rate for
villages and towns means that a village of 1,000 people must sustain 25 active
members — achievable but not trivial. Using 5% or higher would produce artificially
easy pass conditions for the COOPERATIVE lens and undermine the project's falsifier
integrity.

> **Illustrative anchor — to be refined against actual sources before any
> simulation run that depends on it.** Recommended refinement: obtain membership
> data from an established tool library or production cooperative in a comparable
> settlement (contact NATLN member organizations or query the US Federation of
> Worker Cooperatives directory). Use reported active membership ÷ municipal
> population as the empirical participation rate and replace these anchors with
> the result.

### 5.5 Floor constraint

The feasible member pool is always at least **10 members** regardless of the
population formula, because smaller cooperatives are operationally fragile and
governance literature (Ostrom 1990, *Governing the Commons*) suggests that
below approximately 10 active participants, graduated-sanction regimes become
ineffective. Any catalog entry whose break-even member count falls below 10 at
village scale should be flagged for review: if the economics work with fewer than
10 members, the entry may be more appropriately evaluated under MARKET than
COOPERATIVE.

---

## 6. Geographic Assumptions

These assumptions are fixed for the developed-economy context that CERES targets
(spec Section 13 non-goal: "not a global-reach simulation").

1. **Developed-economy settlement.** The target settlement is located in a
   country with functioning rule of law, standard property rights, access to grid
   electricity and fuel distribution networks, and a labor market with wage rates
   in the range defined in Section 3. Catalog entries intended for other economic
   contexts require separate scale parameters and are outside current scope.

2. **One or more neighboring settlements within a 30-minute drive.** Every target
   settlement is assumed to have at least one neighboring settlement of comparable
   or larger scale within a 30-minute driving radius. This affects:

   - **Supplier density.** Even a village (thin density) can source consumables and
     maintenance materials from a neighboring town within the same operating day. A
     thin-density village is not completely isolated; it is supply-constrained
     relative to a town, not supply-absent.
   - **Labor pool.** Operators and apprentices may commute from neighboring
     settlements. This is modeled as a 15–20% increase in the effective labor pool
     above the local population figures.
   - **Market reach.** Artisan-production output can reach customers in neighboring
     settlements via direct delivery or farmers-market / craft-market channels within
     the 30-minute radius. Catalog entries should not model demand as strictly
     local-population-only unless the specific design (e.g., a hyper-local food
     production unit) precludes regional sales.

3. **Supplier density qualitative levels.** The table in Section 2 assigns a
   qualitative supplier density to each scale:

   | Scale | Density | Operational meaning |
   |---|---|---|
   | Village | **Thin** | 1–2 local suppliers for key consumables; specialty items require 2–7 day lead time from regional distributors |
   | Town | **Moderate** | 3–6 local or nearby suppliers; most consumables available same-day or next-day; specialty items 1–3 days |
   | Small city | **Dense** | Multiple competing local suppliers; most consumables same-day; specialty items typically 1 day or less |

4. **No assumed municipal subsidy.** The CIVIC lens evaluates *whether* a civic
   subsidy is justifiable, so it cannot be assumed as a given in the base-case
   economic model for other lenses. MARKET and COOPERATIVE lens evaluations assume
   no grant, subsidy, or tax-increment financing unless a specific catalog entry
   documents a plausible subsidy pathway in its `lens_context` block.

5. **Infrastructure baseline.** Grid electricity is available and priced in the
   $0.10–$0.15/kWh range (US EIA, Electric Power Monthly, residential and small-
   commercial blended rate, 2023–2024). Natural gas is available for town and
   small-city scales; availability at village scale is uncertain and must be noted
   in the catalog entry's `regulatory_notes`. Propane is assumed universally
   available.

---

## 7. Non-Goals

This document is **not** intended to be:

- **A precise demographic model.** Household counts and population midpoints are
  order-of-magnitude inputs for simulation parameterization, not census projections.
  A real pilot would use actual municipal census data.

- **A labor-market forecast.** Median-wage thresholds are anchored to published
  BLS/ACS data at a point in time. They do not project future wage growth or
  regional variation. A simulation run that needs 10-year projections must adjust
  these thresholds with a documented inflation or wage-growth assumption.

- **A planning-law guide.** Geographic assumptions (neighboring settlement, supplier
  density) are stylized facts for simulation parameterization, not legal, zoning,
  or infrastructure standards.

- **A cooperative constitution.** The member-pool formula and floor constraint
  give simulation-level inputs. The actual governance design for a cooperative
  facility is in the `lens_context.cooperative` block of each catalog entry, not
  here.

- **Exhaustive.** If a catalog entry's specific context (e.g., an isolated mountain
  village with no 30-minute-drive neighbor) violates a geographic assumption here,
  the entry must document the deviation in its `## Key assumptions` section. The
  deviation does not make the entry invalid; it makes the departure explicit.

---

## Sources

1. US Census Bureau. *American Community Survey 5-Year Estimates, Table B25010:
   Average Household Size of Occupied Housing Units by Tenure*. 2018–2022 release.
   https://data.census.gov/ (access Table B25010; filter by place size).

2. US Census Bureau. *Current Population Survey, Annual Social and Economic
   Supplement (ASEC), Table H-8: Median Household Income by Type of Household*.
   March 2023 supplement (income year 2022).
   https://www.census.gov/data/tables/time-series/demo/income-poverty/historical-income-households.html

3. US Census Bureau. *American Community Survey 5-Year Estimates, Table B20002:
   Median Earnings in the Past 12 Months by Sex for the Civilian Employed
   Population 16 Years and Over*. 2018–2022 release. https://data.census.gov/

4. US Bureau of Labor Statistics. *Occupational Employment and Wage Statistics
   (OEWS), May 2023 National and State Estimates*. SOC Major Groups 47
   (Construction and Extraction) and 51 (Production).
   https://www.bls.gov/oes/current/oes_nat.htm

5. Institute of Museum and Library Services (IMLS). *Public Library Survey, Fiscal
   Year 2021*. Published 2023. Data explorer and summary statistics at
   https://www.imls.gov/research-evaluation/data-collection/public-libraries-survey
   (See PLS data tables: operating expenditure per capita by locale code and
   population of legal service area.)

6. American Library Association (ALA). *State of America's Libraries Report 2023*.
   https://www.ala.org/news/state-of-americas-libraries-report-2023
   (Annual summary citing IMLS PLS per-capita expenditure benchmarks.)

7. Ostrom, Elinor. 1990. *Governing the Commons: The Evolution of Institutions for
   Collective Action*. Cambridge University Press. (Chapter 3 on graduated sanctions
   and minimum viable group size in common-pool resource institutions.)

8. Zeuli, Kimberly A., and Robert Radel. 2005. "Cooperatives as a Community
   Development Strategy: Linking Theory and Practice." *Journal of Regional
   Analysis and Policy* 35(1): 43–54. (Rural cooperative participation rates as a
   share of local population.)

9. Botsman, Rachel, and Roo Rogers. 2010. *What's Mine is Yours: The Rise of
   Collaborative Consumption*. HarperBusiness. (Early sharing-economy participation
   rate data; Chapter 4.)

10. North American Tool Library Network (NATLN). Membership and operational data
    referenced from publicly available reporting by Toronto Tool Library
    (https://torontotoollibrary.com) and Vancouver Tool Library
    (https://vancouvertoollibrary.com), as cited in cooperative sector surveys
    (~2019–2023). Note: specific membership statistics require direct outreach to
    these organizations; public web publications give order-of-magnitude figures only.

11. US Energy Information Administration. *Electric Power Monthly, Table 5.3:
    Average Retail Price of Electricity, Residential and Commercial Sectors*.
    Monthly release. https://www.eia.gov/electricity/monthly/

---

## Appendix A: Parameter-Revision History

When a threshold value is updated (after refinement against current sources, or
as wage/cost data shifts materially), the prior value is archived here with its
date and the reason for the change. The values in the main body sections always
reflect the current anchors.

### Version 1.0 — 2026-04-18 (initial; current)

All values are at their initial illustrative anchor levels as defined in Sections
2–6 above. No prior values to archive.

| Parameter | Scale | Value | Source basis |
|---|---|---|---|
| Median wage threshold | Village | $48,000 / yr | BLS OEWS SOC 47+51 trades median, small-place discount |
| Median wage threshold | Town | $56,000 / yr | BLS OEWS SOC 47+51 midpoint; ~$20/hr pre-burden |
| Median wage threshold | Small city | $62,000 / yr | BLS OEWS SOC 47+51 upper range for 15k–100k places |
| Civic cost threshold | Village | $120 / hh / yr | ALA/IMLS library per-capita operating cost × 2.5 hh-size, +headroom |
| Civic cost threshold | Town | $100 / hh / yr | ALA/IMLS library per-capita lower bound × 2.5 |
| Civic cost threshold | Small city | $80 / hh / yr | Below library parity; stricter city-budget competition |
| Member pool participation rate | Village | 2.5 % | NATLN tool-library empirical range; rural coop premium |
| Member pool participation rate | Town | 2.5 % | NATLN tool-library empirical range |
| Member pool participation rate | Small city | 2.0 % | Lower urban participation; Botsman/Rogers sharing-economy data |
