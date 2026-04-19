---
scale: town
population_range: 2000-15000
trade: smithing
doc_type: playbook
plan_task: "Plan E Task 3"
authored: 2026-04-18
matrix_source: simulations/tier-a-comparator/results/SUMMARY.md
---

# Smithing Playbook — Town Scale (2,000–15,000)

## Purpose

This playbook translates the Tier A simulation matrix into implementation guidance for
smithing restoration at town scale. It draws on SUMMARY.md, CIVIC-LENS-DIAGNOSTIC.md,
the fifteen catalog entries, DECLINE-VERDICT.md, and SCALES.md.

Town scale is the sweet spot. The cooperative lens becomes broadly viable here for the
first time — all fifteen entries clear town_coop. The civic lens produces its first
template wins (forge-004, forge-011). The market lens remains as selective as at village
scale. The result: 15 coop wins + 7 market wins + 2 civic wins = 24 total lens-wins,
the densest option set in the study. The playbook is organized by lens, then by
implementation sketch for featured designs.

---

## Matrix Summary

**Scale parameters (SCALES.md §2)**

- Population midpoint used in simulation: 8,500 (range 2,000–15,000)
- Household count at midpoint: ~3,400 (population × 0.40)
- Feasible coop member pool: ~213 (8,500 × 2.5%)
- Market lens wage threshold: $56,000 / yr [SCALES.md §3]
- Civic lens per-household cost ceiling: $100 / yr

**Lens-win counts**

| Lens | Wins | Fails | Win rate |
|---|---|---|---|
| town_market | 7 / 15 | 8 / 15 | 47% |
| town_coop | 15 / 15 | 0 / 15 | 100% |
| town_civic | 2 / 15 | 13 / 15 | 13% |

---

## Cooperative Lens — All 15 Win

The defining feature of town scale is universal cooperative viability. Every catalog
entry clears town_coop. This is not a marginal result: the feasible member pool of ~213
at the 8,500-person midpoint comfortably exceeds the break-even member count for every
design (break-even ranges from 40 to 90 members across the catalog, depending on
capital structure; the pool is 2–5x break-even for all entries).

**Why coop works at town where it fails at village.** The cooperative lens passes when
the feasible member pool exceeds the break-even member count. At village scale (pool
~25), most designs fail — the pool is too thin. At town scale, the pool of ~213
comfortably underwrites every design in the catalog, including high-capital options
like forge-009 (~$120k). At town scale the cooperative form is not a fallback; it is
the primary viable structure for the majority of the catalog.

**Coop-primary highlighted designs.** Three entries are designed specifically as
cooperatives, not merely cooperative-capable:

- **forge-003 — Shared Tool-Library Coal Forge.** 35 m², coal-fired, member-booked.
  Capital $28k mid; break-even 60 members vs. feasible pool ~213. Ostrom principles
  1–6 addressed. The canonical cooperative design; town scale is its native scale.
- **forge-009 — Co-op Apprentice Training Forge.** 80 m², hybrid coal-induction.
  Training is the primary activity; apprentice stipends funded by member fees and
  specialty-output sales. The strongest succession-mechanism design in the catalog.
- **forge-015 — Tool-Library Member-Access Induction Forge.** 40 m², induction-
  electric, 3–4 simultaneous stations. Urban-compatible regulatory profile;
  subscription-access model; lower capital than coal designs.

---

## Market Lens — 7 Wins (Scale-Invariant)

The seven market winners at town scale are the same seven as at village and small_city
scale. The MARKET lens passes on payback_years against a wage threshold; the payback
calculation is scale-independent (capital, throughput, and unit price do not change
with settlement size in the model). Town population does not improve market viability.

**Market winners (town_market = win):** forge-002, forge-003, forge-005, forge-006,
forge-010, forge-012, forge-013.

For a market-primary path, the most accessible options are forge-002 (induction-electric,
lowest capital, simplest regulatory profile), forge-006 (bladesmith specialty premium),
and forge-005 (coal repair, lowest equipment capital). Since town_coop is universal,
all seven market winners can also be structured as cooperatives — useful when the
cooperative wants to pay its lead smith a market wage rather than rely solely on dues.

---

## Civic Lens — 2 Wins

The civic lens is selective. Two entries win town_civic: forge-004 (Community Civic
Makerspace) and forge-011 (Municipal Civic Training Forge). All other entries fail
civic correctly — they are commercial or cooperative designs with no public-access
mode, and a forge with no scheduled public hours cannot pass a utilization-based
civic test.

The two civic winners are purpose-designed civic infrastructure. Their per-household
costs at town scale are remarkably low:

| Entry | per_hh_cost / yr | Threshold | Margin |
|---|---|---|---|
| forge-004 Civic Makerspace | $4.23 | $100 | 96% |
| forge-011 Municipal Training Forge | $6.44 | $100 | 94% |

For comparison, a small-town public library costs ~$100–$137/hh/yr (IMLS FY 2021).
A civic forge at $4–7/hh/yr is one-fifteenth of library cost. The fiscal argument at
town scale is strong enough that the political obstacle is council coalition, not budget.

**Utilization threshold note.** The civic lens uses person-hours
(facility_hours × concurrent_users) with a 0.15 hr/capita specialized-equipment
exception threshold (ECONOMIC-LENSES.md §4.3), rather than the 2.0 hr/capita default
calibrated for libraries and recreation centers. Any new civic forge entry must invoke
this exception explicitly in sim_params (annual_public_use_hours and
usage_rate_threshold: 0.15); without it the lens defaults to 0 hours and fails.
See CIVIC-LENS-DIAGNOSTIC for the full analysis and worked examples.

---

## Implementation Sketches

### Sketch A — forge-003: Cooperative Coal Forge (Coop-Primary + Civic-Compatible)

**Design:** Shared Tool-Library Coal Forge, 35 m², coal-fired with propane backup,
member-booked sessions. Mid capital $28k + $6k installation = $34k total. Annual
operating costs ~$11,860 (maintenance $1,500 + consumables $4,200 + floor-space $4,800
+ minor overhead). Break-even at 60 dues-paying members; feasible pool ~213.

**Why this design at town scale.** The 60-member break-even is comfortable only at
town scale (scale_fit.village = marginal). Coal is the lowest-capital path to a full-
production shared forge; induction alternatives cost more and draw higher energy per
session. Coal's operational penalty (45-minute startup/shutdown, restricted zoning) is
manageable at the throughput volumes a 60–200 member cooperative generates.

**Governance.** Ostrom-compliant cooperative corporation or 501(c)(3). Steward-elected
monitoring, graduated sanctions (warning → $50 fine → 30-day suspension → membership
review), 2/3-majority amendment process. Mandatory apprentice slot: at least one
registered apprentice active whenever the forge operates ≥20 hr/wk. This last provision
is the succession mechanism — it institutionalizes skill transmission into normal
operations rather than segregating it into a separate program.

**Civic-compatibility note.** Forge-003's per_hh cost at town scale is $2.01 vs. the
$100 threshold — it would clear civic if re-authored with annual_public_use_hours and
a lens_context.civic block. (This would require a Plan F catalog revision to forge-003;
it is not a current civic win.) A municipal-partnership structure (cooperative operates,
municipality contributes facility or capital) is viable without converting the entity
to a civic facility.

**Capital path:** $34k via founding member dues (~$300/yr × 100 members) plus a
workforce-development grant for the gap. No municipal bond; no long-term debt.

**Risks.** Coal zoning restricts siting to light-industrial or mixed-use; site selection
is the critical gate. Journeyman labor scarcity is the Year 1–3 operational risk; the
mandatory apprentice slot mitigates this on a 3-year horizon. Coal supply-chain
thinning in many regions is managed by propane backup but not fully eliminated.

---

### Sketch B — forge-009: Co-op Apprentice Training Forge (Coop + Training)

**Design:** 80 m², hybrid coal-induction, 4–8 concurrent apprentice stations plus
master demonstrator bay. Capital ~$120k mid. Annual operating ~$22,000. Training-
primary product mix (30% training_output, 30% specialty, 30% artistic, 10% repair).
Break-even member count higher than forge-003 due to capital scale; still comfortably
within the ~213 feasible pool.

**Why this design at town scale.** Forge-009 is the succession-first cooperative:
training is the primary activity and production is secondary. Choose this when the
goal is producing journeyman smiths over 3–6 years rather than delivering repair
services in year one. The hybrid fuel choice (coal for forge-welding, induction for
precision heat-treat) is pedagogical — both skill sets require their own fuel type.

**Capital path:** $80k–$200k requires a financing mix: founding dues alone are
insufficient. Target $50k workforce-development grant + $30k–$50k municipal
co-investment (facility or land contribution) + dues reserve for operations. The
cooperative structure can accommodate a municipal co-investor seat without converting
to a civic facility.

**Risks.** Governance at 50–200 members requires explicit bylaws; apprentice stipends
are the contentious budget line (members who do not use the training program resist
funding it). Master-smith dependency is the primary catastrophic risk — the hiring
pool for masters is thinner than journeymen, and losing the master smith in Year 2
is the most common failure mode for training-primary cooperatives. Summer cohort
transitions produce a 0.4× worst-month throughput fraction; operating reserves are
required across transition months.

---

### Sketch C — forge-004: Civic Makerspace Forge Module (Civic-Primary)

**Design:** Town-owned, 65 m², hybrid induction-gas, supervised multi-user model
(1 master smith-supervisor + up to 4 members per shift). Capital ~$75k–$120k typical.
Annual civic cost ~$14,400 (capital charge + maintenance + consumables, excluding
floor-space rent which the municipal facility owns). Per-household cost at town scale:
$4.23/hh/yr — a 96% margin under the $100/hh threshold.

**Why this design at town scale.** Forge-004 is designed as civic infrastructure in
the same sense that a public library is civic infrastructure: owned by the municipality,
staffed by a contracted professional, and open to all residents on a scheduled basis.
The "library model" framing is in the catalog entry's tagline for good reason. The
per-household cost argument is the entry's strongest asset: at $4.23/hh/yr, the civic
forge costs less per household than a streaming music subscription and provides a
physical fabrication resource with no commercial alternative within the town.

The induction-primary fuel choice is appropriate for a public-access facility: no
combustion at the forge station reduces on-site emissions, simplifies the permitting
profile, and reduces the safety complexity of a multi-user supervised environment.
Propane backup for high-temperature operations is retained.

**Political coalition.** The typical town council vote is 5–2 favorable when framed
around workforce development and repair culture, not economic subsidy. If a private
smith exists within 20 km, shift to training-pipeline framing (the civic forge trains
the private forge's future employees). Opposition argues tax burden; the $4.23/hh
figure — less than a cup of coffee per household per month — is the most effective
direct response.

**Civic-market complementarity.** Forge-004 and forge-002 (market private) are
complementary layers, not competitors: forge-004 takes residents from zero to
journeyman; forge-002 or forge-003 employs those journeymen commercially. This
division of function is the strongest structural argument for civic investment.

**Capital path:** 25-year municipal bond or CIP line item. At $75k–$120k, smaller
than a road repaving. Annual operating (~$14k for contracted smith + direct costs)
fits under parks-and-recreation or workforce-development. Workforce-development and
rural-infrastructure grants can reduce the bond amount.

**Risks.** Council coalitions shift; institutionalize through dedicated budget line
and annual outcomes report. If a private smith enters the market post-launch, the
gap-filling justification weakens — proactively reframe as training pipeline before
this happens. Master-smith contracting carries moderate retention risk; stable salary
with no capital exposure is the retention advantage over private employment.

---

### Sketch D — forge-002: Market-Primary Private Forge (Single-Operator Balance)

**Design:** Induction-Modular Small Repair, 27 m², single-operator, induction-electric.
Capital ~$22k–$35k. Market lens win at town scale; low regulatory complexity.

**Why include a market sketch.** A town may not yet have the social capital for a
cooperative or the political coalition for a civic facility. A single operator running
forge-002 on a market basis provides repair service immediately, builds demonstrated
demand, and creates the conditions that make a cooperative or civic follow-on viable.
The market-primary path is not a consolation prize; it is often the fastest first step.

**Capital path:** $22k–$40k via SBA microloan or USDA Rural Business Development Grant.
Operational within 60–90 days vs. 6–18 months for a cooperative or civic launch.

**Risks.** Single-operator failure risk: no succession pipeline. If the smith leaves
or closes, service ends. This is the explicit limitation relative to cooperative and
civic alternatives, which have institutional continuity built in.

---

## Capital Ask by Path

| Path | Design example | Capital range | Primary funder |
|---|---|---|---|
| Market-primary, solo | forge-002, forge-005 | $22k–$50k | SBA microloan, operator equity |
| Cooperative, production | forge-003, forge-015 | $30k–$70k | Member dues, workforce grant |
| Cooperative, training | forge-009 | $80k–$200k | WFD grant + municipal co-investment |
| Civic, library model | forge-004 | $75k–$120k | Municipal bond or CIP |
| Civic, CTE partnership | forge-011 | $100k–$200k | School district + CTE state funds |

Town scale supports larger facilities and higher capital loads than village scale
because the population base is large enough to generate the member dues, tax base,
or market revenue to service the debt. The $80k–$200k range for training-oriented
cooperative and civic designs is realistic at town scale in a way that it would not
be at village scale.

---

## Open Risks

**1. Coop governance at 50–200 members.** A 150-member town cooperative needs
explicit quorum rules, written conflict-resolution procedures, and a steward with
real authority — informal resolution fails at this scale. Entries that specify
Ostrom-compliant governance (forge-003 explicitly) have this addressed; entries
adapted from market-primary designs without the governance layer are at higher risk.

**2. Municipal politics for civic designs.** The 96% cost margin does not guarantee
a council vote. Budget-cycle risk is recurring; the civic forge must demonstrate
measurable outcomes (apprentices trained, repair services delivered, cost-per-household)
each annual cycle. A champion on the council and a compelling narrative framing are
required as much as favorable unit economics.

**3. Competition among paths in the same town.** A town with forge-003 (cooperative)
and forge-002 (private market) operating simultaneously is a realistic scenario. They
draw from the same customer base. Assess local market structure before recommending
a path: if a private smith already operates within 20 km, the cooperative path has a
more defensible niche than a second competing forge; if no smith exists, all three
paths are viable and the choice depends on organizational capacity and goals.

**4. Labor scarcity across all designs.** Skilled smithing labor is scarce in
small-town markets and does not improve at town scale relative to village scale —
there are more potential employers competing for the same thin pool. Succession
mechanisms (mandatory apprentice slot in forge-003; training-primary design in
forge-009) are the only sustainable mitigation; they operate on a 3–6 year horizon.

---

## Scale Framing

Town scale is where all three lenses are live simultaneously. Village scale is
constrained by a thin member pool and limited demand. Small-city scale adds financial
depth but approaches urban conditions where industrial alternatives are more accessible.
Town scale — 2,000–15,000 residents, a functioning commercial district, a member pool
large enough for any cooperative design — is where the CERES catalog has the most to
offer and where path choice is genuinely open.

The DECLINE-VERDICT for smithing is "mixed": repair and specialty work restructured
into viable niches; commodity hardware declined to industrial substitution. A town of
8,500 has enough repair demand for a market forge, enough organizational capacity for
a cooperative, and enough tax base for a civic facility. The question is not whether
smithing can work here — the simulation says it can under any lens — but which path
the community has the organizational capacity and will to pursue.
