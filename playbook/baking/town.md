---
trade: baking
scale: town
doc_type: playbook
version: "1.0"
status: draft
review_status: {panel: pending, editorial: pending}
derived_from:
  - simulations/tier-a-comparator/results/baking/SUMMARY.md
  - catalog/baking/entries/*.md
  - research/trades/baking/DECLINE-VERDICT.md
population_range: 2000-15000
---

# Baking Playbook — Town Scale (2,000–15,000 residents)

## Purpose

This playbook translates the Tier A simulation matrix into operational guidance for
town-scale baking projects. Readers are community organizers, municipal planners,
cooperative founders, and prospective operators evaluating whether a bakery — in any
of its commercial, cooperative, or civic forms — is viable for a settlement of
2,000–15,000 people. The playbook extracts market, cooperative, and civic verdicts
from the 15-entry simulation, identifies which designs clear town-scale thresholds,
and provides implementation sketches for the priority designs.

Town scale is where the cooperative lens first opens meaningfully for baking. The
market lens remains as selective as at village scale — the same 6–7 entries win, and
the formula is scale-invariant. The civic lens wins for three entries designed as
civic or training facilities. The practical significance: a town of 2,000–15,000
can support a private artisan bakery, a shared-kitchen cooperative, and a civic baking
facility simultaneously. All three paths are live here for the first time.

---

## The Matrix at Town Scale

Scale parameters used in simulation: population midpoint 8,500; household count ~3,400;
feasible coop member pool ~213 (8,500 × 2.5%); market wage threshold $56,000/yr;
civic per-household cost ceiling $100/yr.

| Lens        | Wins | Marginals | Fails | Win rate |
|---|---|---|---|---|
| town_market | 6    | 1         | 8     | 6/15     |
| town_coop   | 11   | 0         | 4     | 11/15    |
| town_civic  | 3    | 0         | 12    | 3/15     |

The cooperative lens is the headline number: 11/15 win at town, up from 2/15 at village.
The feasible member pool of ~213 comfortably exceeds the break-even member count for
11 entries. Four entries fail town_coop because their capital structure drives break-even
above the town pool: bake-004 (wholesale multi-deck, high capital), bake-006 (combi-steam
pastry, high capital), bake-011 (training bakery, break-even 221 > pool 213), and
bake-012 (community kitchen, break-even 250 > pool 213).

The market lens wins for the same 6 entries as at village and small-city — the market
formula tracks capital and revenue model, not population. Bake-009 (custom cake studio)
remains marginal at town.

The civic lens produces 3 wins: bake-010 (Civic Neighborhood Bakery), bake-011
(Apprentice Training Bakery), and bake-012 (Community Kitchen Collective) — all three
of which pass town_civic with substantial formula margin.

---

## Market Lens — Winning Designs at Town Scale

Six entries win town_market, one is marginal. Town scale adds market-depth that village
cannot provide: a town of 2,000–15,000 can absorb a full artisan bakery's throughput
from local demand alone, making DTC regional extension less essential than at village.

**bake-001 — Sourdough Artisan Micro-bakery** (capital mid $32,000; payback 0.19 yr;
single operator; electric-deck)

Town scale is the sweet spot for bake-001. The artisan sourdough premium segment is
well-supported at 2,000–15,000 residents: a town of 8,500 with a food-culture
population can sustain 80–130 loaves/day from local direct-to-consumer and farmers-
market sales without regional extension. The economics are the same as at village
(payback is scale-invariant), but the market absorption problem largely disappears.
`scale_fit.town: good`. Mill dependency: industrial flour purchased from regional
food-service distributor; 30-day flour buffer inventory recommended to manage
supply-chain disruption risk.

**bake-004 — Wholesale Artisan Loaf Bakery** (capital mid $100,000; 350 loaves/day;
2–3 journeyman-baker operators; electric-deck multi-unit)

Town scale is the primary operating context for bake-004. A town of 2,000–15,000 can
generate enough B2B wholesale accounts (restaurants, cafés, grocery accounts) to
sustain 200–350 loaves/day throughput. At 350 loaves/day and $4.50–$6.50/loaf wholesale
pricing, gross revenue runs $430,000–$620,000/year. This is a multi-operator commercial
operation; the $100,000 capital requires deliberate financing. Note: bake-004 fails
town_coop (break-even exceeds the town feasible pool), so the cooperative path is not
available for this entry at town scale; it must be structured as a private market
business. `scale_fit.town: good`.

**bake-007 — Japanese-style Wagashi Confection Studio** (capital mid $48,000;
operator: wagashi-master; hybrid-wood-electric; town_coop: win)

Town scale supports bake-007 better than village. A town with a Japanese-diaspora
community, specialty food tourism, or a food-culture retail cluster can sustain a
wagashi studio at 80–120 units/day premium gift and specialty retail pricing.
bake-007 passes town_coop (break-even well under pool 213), meaning a wagashi studio
cooperative structure is viable here. The upstream binding constraint is specialty-
ingredient sourcing (sweet bean paste, mochiko rice flour, sugar) rather than wheat
flour; all are commodity inputs available from Asian-ingredient distributors in most
US markets with food-service distribution. `scale_fit.town: good` where cultural
demand base exists.

**bake-008 — Ethnic / Cultural Specialty Bakery** (capital mid $45,000; operator:
journeyman-baker trained in specific tradition; electric-deck; town_coop: win)

Town scale is the natural operating environment for bake-008. A town of 2,000–15,000
is large enough to sustain a diasporic specialty bakery from local cultural demand
alone. The demand base is structurally durable: customers for German rye bread,
Ethiopian injera, Mexican pan dulce, or South Asian flatbreads are community members
for whom these products are dietary staples, not trend shoppers. Town coop passes
(break-even under pool 213), enabling a worker-cooperative structure. `scale_fit.town:
good`. Mill dependency: the electric-deck baseline uses purchased flour in the same
supply chain as bake-001; tradition-specific specialty flours (rye, injera teff, etc.)
may require additional lead-time planning.

**bake-013 — Farm-to-Table Integrated Bakery** (capital mid $55,000; wood-fired-deck;
payback 0.81 yr; town_coop: win)

Town scale adds cooperative viability to bake-013's market win. The entry now passes
town_coop (break-even 109 vs. pool 213), enabling a worker-cooperative or CSA-with-
bakery-shares structure. The premium price point ($9–$22/loaf for heritage-grain wood-
fired bread) supports 2-operator economics at town scale. Mill integration is the
operational challenge: the co-located stone mill requires grain sourcing, consistency
management, and daily maintenance as a co-equal operational system alongside the
bakery. A multi-year grain supply contract with a heritage-wheat farm within 30 miles
is the essential prerequisite. `scale_fit.town: good`.

**bake-006 — French-style Pastry / Viennoiserie** (capital mid $65,000; operator:
pastry-chef-master; combi-steam; town_market: win but town_coop: fail)

Wins town_market on payback, but bake-006 fails town_coop (its high capital drives
break-even above the town feasible pool). It must be structured as a private market
business at town scale. The premium confection customer base at town scale is adequate
for a destination pastry shop, though small-city scale (15,000–75,000) is the stronger
operating context for commission-dependent confection volume. `scale_fit.town: marginal`.

**bake-009 — Custom Celebration Cake Studio** (marginal at town; capital mid $28,000;
operator: pastry-chef-master; event-calendar revenue model)

Marginal town_market verdict. A town of 2,000–15,000 generates more events than a
village, but the event-calendar model still requires a 20–30 mile regional draw to
fill a full-time studio. Viable as a part-time or regional specialty practice. The
marginal verdict reflects event-density, not a capital or pricing problem.

---

## Cooperative Lens — Winning Designs at Town Scale

Eleven entries pass town_coop. The feasible member pool of ~213 at the 8,500-person
midpoint exceeds the break-even member count for 11 of 15 entries. This is the defining
structural shift from village to town scale: at village, only 2 designs clear the
cooperative lens; at town, 11 clear it.

**Entries passing town_coop:** bake-001, bake-002, bake-003, bake-005, bake-007,
bake-008, bake-009, bake-010, bake-013, bake-014, bake-015.

**Four entries failing town_coop:** bake-004 (high-capital wholesale bakery, break-even
exceeds pool), bake-006 (high-capital combi-steam pastry, break-even exceeds pool),
bake-011 (training bakery, break-even 221 > pool 213), bake-012 (community kitchen,
break-even 250 > pool 213).

**Featured cooperative designs at town scale:**

**bake-015 (Wood-fired Community Oven)** — The most accessible cooperative design at
any scale. Capital $18,000; break-even 17 members against pool 213. A town of 8,500
can easily support 17–60 dues-paying member households sharing a communal wood-fired
oven. At town scale, the community oven cooperative can grow into a robust institution:
50+ members, weekly scheduled firing days, a part-time paid fire-keeper, and a training
program for members who want to develop wood-fired baking skill. Also passes town_civic
if the governing body adopts a public-access mandate.

**bake-001 (Sourdough Artisan Micro-bakery, cooperative structure)** — bake-001 passes
town_coop (break-even 76 vs. pool 213). At town scale, structuring the artisan micro-
bakery as a 2–3 person worker-cooperative distributes both capital burden ($32,000
mid ÷ 3 founders = ~$10,700 per person) and succession risk. Worker-cooperative
ownership also addresses the single-operator retention risk that makes a solo village
bakery vulnerable: a cooperative with 2–3 worker-owners has built-in redundancy when
one worker takes leave or departs. State worker-cooperative incorporation required
before pooling capital or paying wages from shared revenue.

**bake-008 (Ethnic Cultural Specialty Bakery, cooperative structure)** — Passes
town_coop and is a natural fit for community-owned cooperatives serving diasporic
or cultural communities. The cultural community that forms the bakery's customer base
can also form the cooperative's membership, creating alignment between ownership
and clientele that stabilizes the demand base. Governance: multi-member LLC or state
cooperative corporation; membership open to cultural-community residents and active
operators.

**Governance note for town-scale cooperatives:** A cooperative with 60–150 members
needs explicit written bylaws, a quorum mechanism, a member-elected steward or
manager with decision authority, and a documented conflict-resolution procedure.
Informal consensus governance fails at member counts above 40–50. The entries with
explicit Ostrom-compliant governance (bake-001 has a full cooperative lens_context
block; bake-015 specifies membership rules and graduated sanctions) have addressed
this. Cooperatives adapted from market-primary designs without an added governance
layer are at elevated risk when scheduling conflicts, maintenance disputes, or dues
disagreements arise.

---

## Civic Lens — Winning Designs at Town Scale

Three entries win town_civic:

| Entry | Name | per_hh/yr | Threshold | Formula margin |
|---|---|---|---|---|
| bake-010 | Civic Neighborhood Bakery | $4.65  | $100 | 95% |
| bake-011 | Apprentice Training Bakery | $10.55 | $100 | 89% |
| bake-012 | Community Kitchen Collective | $7.62  | $100 | 92% |

All three win with substantial margin. The per-household costs at town midpoint are
low relative to comparable civic facilities: a public library costs $100–$137/hh/yr
(IMLS FY 2021); a civic bakery at $4.65–$10.55/hh/yr costs one-tenth to one-twentieth
of library operating cost while delivering food-access and workforce-development
externalities.

**bake-010 (Civic Neighborhood Bakery)** — $80,000 mid capital; two-deck electric
oven; journeyman-baker-instructor; library-model access for community members.
At town scale ($4.65/hh/yr × 3,400 households = $15,810/year levy), the household
levy alone does not cover the instructor wage ($52,000–$56,000/year). The combination
of levy plus modest member access fees ($30–$60/year from 100–200 participants =
$3,000–$12,000/year) plus a workforce-development grant or municipal operating subsidy
closes the gap. This combination is achievable at town scale. The externalities
documented in the entry — food access, nutrition education, cultural baking traditions,
apprentice training pipeline — form the civic argument alongside the fiscal case.
`scale_fit.town: good`.

**bake-011 (Apprentice Training Bakery)** — $85,000 mid capital; three-deck training
floor; 1 master instructor + 2–3 apprentices; CTE or vocational partnership model.
Town is the first scale where bake-011 becomes operationally feasible: the civic
formula passes ($10.55/hh/yr), and the apprentice intake population is large enough
for a 4–6 trainee cohort. The model produces real bread for sale while training
journeyman bakers — combining instructional revenue from a vocational partner, bread-
sales revenue from training output, and civic subsidy for the workforce-development
externality. A school-district or community-college CTE partnership is the preferred
governance form. Note: bake-011 fails town_coop (break-even 221 > pool 213); it is
civic-primary. `scale_fit.town: good`.

**bake-012 (Community Kitchen Collective)** — $95,000 mid capital; multi-oven shared
commercial kitchen; member-booking model for cottage-food and catering operators.
The civic win reflects the food-business incubation externality: pooling commercial
kitchen compliance costs across 15–30 small food businesses is a genuine public-good
investment. Booking-fee revenue ($8,000–$18,000/year from utilization) partially offsets
the civic subsidy required. Note: bake-012 also fails town_coop (break-even 250 > pool
213), so it is civic-primary. `scale_fit.town: good`.

**Civic complementarity at town scale:** The three civic designs address different
needs. bake-010 serves bread access and basic baking education. bake-011 produces
credentialed journeyman bakers through a vocational pipeline. bake-012 incubates
food entrepreneurs. All three can coexist without competing; they require different
institutional relationships (municipality, school district, nonprofit or incubator
partner). Most towns will pursue one. The strongest political argument for any civic
baking design at town scale is the workforce-development case: a civic baking facility
that produces employable journeyman bakers is a net contributor to the private market
(bake-001, bake-004, bake-008 operations in the same town benefit from the graduate
pipeline), not a competitor.

---

## Implementation Sketches

### Sketch A: Bake-001, Sourdough Artisan Micro-bakery (Market-Primary or Worker-Cooperative)

**Context:** Town of 4,000–10,000 residents with a weekend farmers market and at least
one café or restaurant willing to take a wholesale bread account. Operator is a
journeyman baker with 3+ years sourdough experience, or a 2–3 person founding team
where at least one member has journeyman fermentation skill.

**Setup (months 1–3):**

- Confirm commercial kitchen licensing pathway. In most US jurisdictions: 60–90 days
  from application to health-department certificate. Identify commercial kitchen space
  or light-commercial lease ($400–$800/month for 20–25 m² in a town center or food-
  appropriate zone).
- Equipment: mid-range electric deck oven ($14,000–$18,000 new), proofing cabinet
  with humidity control ($4,000–$5,000), commercial spiral mixer ($3,500–$4,500),
  full smallware set ($1,500–$2,000). Total equipment: $23,000–$30,000. Electrical
  service upgrade if required: $1,500–$3,500 installed.
- Flour sourcing: establish account with regional food-service distributor. At
  115 loaves/day × 0.7 kg/loaf × 285 operating days = ~23,000 kg/year; negotiate
  volume pricing and confirm 3-day standard lead time. Build 30-day flour buffer
  inventory from day 1.

**Launch (months 4–8):**

- Begin at 60–80 loaves per market day, one market per week. Target sell-through for
  first three markets before scaling volume.
- Add 2–3 café/restaurant wholesale accounts (20–40 loaves per account per week).
- Build direct subscription list: weekly pickup or delivery at $8/loaf. Target
  50 subscription households by month 6.

**Year-1 P&L sketch (town-scale):**

| Item | Amount |
|---|---|
| Revenue (115 loaves/day × 285 days × $8/loaf × 0.70 ramp factor) | $184,030 |
| Annual consumables (flour, packaging, energy) | $8,500 |
| Annual maintenance | $1,200 |
| Floor-space rent ($600/month town commercial rate) | $7,200 |
| Total cash operating costs | $16,900 |
| Pre-draw gross margin | $167,130 |
| Capital amortization ($36,000 over 15 yr) | $2,400 |
| **Operator draw available (year 1)** | **~$164,730** |

At town scale, market absorption supports full throughput: 115 loaves/day at 8,500
residents implies each household purchasing one loaf roughly every 25–30 days on
average — achievable once subscriptions and wholesale accounts are established.

**Worker-cooperative variant:** If structuring as a 3-person worker-cooperative,
founding capital of $36,000 divided by 3 founders = $12,000 equity share each.
Register as a state worker-cooperative corporation before pooling capital; adopt
bylaws with quorum rules, steward authority, and graduated-sanction provisions
per Ostrom Principles 3–6.

---

### Sketch B: Bake-010, Civic Neighborhood Bakery (Civic-Primary)

**Context:** Town of 3,000–10,000 with a municipal budget for food-access or
workforce-development investment. A committed journeyman-baker-instructor candidate
already identified before the council vote. Coalition: food-access advocates,
workforce-development board, local food pantry, existing farmers-market or food-hub.

**Political groundwork (year 0):**

Prepare two arguments for the council. (1) The fiscal case: $4.65/hh/yr against a
$100 threshold — less than a streaming service subscription per household per year,
equivalent to one-twentieth of public library cost per household. (2) The food-access
and workforce case: the facility trains bakers who staff or found private market
bakeries; it distributes bread to food-access programs; it preserves cultural baking
traditions in the community. Identify the instructor-candidate before the vote.

**Capital structure:**

- Facility: town-owned or civic-rate lease. Rent imputed at $0 (municipal) or
  $3,600–$7,200/year (civic-rate lease).
- Equipment: $80,000 mid (two-deck commercial electric oven, proofing cabinet,
  spiral mixer, two member workstations, smallwares, curriculum materials).
- Installation: $8,000 (electrical service upgrade, exhaust hood, health certification).
- Year-1 operating reserve: $12,000 (6 months direct operating costs excluding
  instructor wage).
- **Total capital ask: $88,000–$100,000** via 25-year municipal bond or CIP
  line item.

**Annual operating budget (at 8,500-person town midpoint):**

| Revenue/subsidy source | Amount |
|---|---|
| Civic household levy ($4.65 × 3,400 hh) | $15,810 |
| Member access fees ($45/yr × 150 active members) | $6,750 |
| Workforce-development grant (year 1–3) | $15,000–$30,000 |
| **Total funding available** | **$37,560–$52,560** |
| Instructor wage ($52,000–$56,000/yr) | $52,000–$56,000 |
| Direct operating costs (consumables, maintenance, energy) | $14,200 |
| **Total operating cost** | **$66,200–$70,200** |
| **Gap covered by grant + any surplus levy** | **~$14,000–$32,600** |

In year 4+, as grant dependency decreases, the operating model should shift toward
levy + fees covering at least 60% of instructor wage. This is achievable if the
civic program builds a documented track record of apprentice graduates and loaves
distributed: funding bodies respond to outcomes, not cost formulas.

---

### Sketch C: Bake-013, Farm-to-Table Integrated Bakery (Cooperative with Mill)

**Context:** Town with an agricultural hinterland and at least one CSA farm within
30 miles willing to grow heritage wheat or ancient grains. Founding team includes
both baking and basic milling competencies — or a commitment to develop both.

**Why this design at town scale:** bake-013 passes town_coop (break-even 109 vs. pool
213), enabling worker-cooperative financing. A founding team of 4–5 worker-members
pools $55,000 mid capital at $11,000–$14,000 per person — feasible without institutional
financing. The wood-fired differentiation and grain-sourcing narrative support $9–$22/
loaf pricing that sustains multi-person economics.

**The mill as co-equal operational system (the DECLINE-VERDICT constraint applied
directly):** The DECLINE-VERDICT mill-dependency falsifier (§3) states that no
historical baking form operated without upstream grain-milling supply. bake-013 accepts
this constraint and addresses it by owning the mill — but owning the mill does not
eliminate the dependency; it internalizes it. The stone mill is a capital asset
($8,000–$15,000 for a 10–20 kg/hour unit) and an operational system requiring daily
maintenance, stone dressing every 60–90 days, grain moisture management, and flour
consistency monitoring. An operator who treats the mill as a background appliance
will produce inconsistent flour and inconsistent bread. Treat the mill as a first-
class production system — budget the maintenance time and capital accordingly.

**Grain-sourcing contract:** Establish a multi-year supply contract with a heritage-
wheat farmer before the mill is installed. Grain supply variability (seasonal harvest
quality, acreage changes) is the primary risk in the milling supply chain. A contract
that specifies minimum volume, moisture content at delivery, and price escalator
protects both parties. Without a contract, the integrated bakery is dependent on
spot-market grain purchasing, which reintroduces the supply-chain risk the mill was
meant to eliminate.

---

## Capital Ask by Path

| Path | Design | Capital range | Primary funder |
|---|---|---|---|
| Market-primary, solo | bake-001, bake-008 | $26k–$60k | Owner equity, SBA microloan |
| Market-primary, wholesale | bake-004 | $72k–$172k | Owner equity, SBA 7(a) loan |
| Cooperative, worker-owned | bake-001 or bake-008 | $29k–$55k | Member equity shares |
| Cooperative, integrated mill | bake-013 | $61k–$96k | Member equity + WFD grant |
| Civic, food-access bakery | bake-010 | $88k–$138k | Municipal bond or CIP + WFD grant |
| Civic, training bakery | bake-011 | $93k–$193k | School district CTE funds + WFD grant |
| Civic, shared kitchen | bake-012 | $107k–$207k | Municipal CIP + USDA RBDG |

Town scale supports larger facilities and higher capital loads than village scale
because the population base generates the member dues, tax base, or market revenue
to service the investment. The cooperative and civic paths require organizational
capacity that the market path does not: a worker-cooperative needs 3–5 committed
co-founders; a civic bakery needs a council vote and a municipal champion.

---

## Open Risks at Town Scale

**Mill dependency is the structural constraint.** All 11 cooperative-viable and
market-viable entries at town scale depend on an upstream grain or specialty-ingredient
supply chain (DECLINE-VERDICT §3). Entries purchasing industrial flour (bake-001,
bake-004, bake-007, bake-008) face commodity price volatility as the primary input
risk: the 2022 global wheat price spike added 30–50% to commodity flour costs within
12 months. At town-scale wholesale volume (bake-004: 95,000+ loaves/year, ~$38,000
in flour), negotiating a 12-month fixed-price supply contract with a regional
distributor is worth the administrative effort. At artisan-micro scale (bake-001:
23,000 loaves/year, ~$5,700 in flour), a 30-day buffer inventory is the minimum
prudent practice. bake-013 addresses this by integrating the mill but introduces
a different supply-chain dependency: grain supply consistency from the farm partner.
No entry in the catalog is upstream-supply-autonomous.

**Cooperative governance at 60–150 members.** The 11 cooperative-viable entries
require written governance before launching. Informal consensus governance fails
at member counts above 40–50 when scheduling conflicts, maintenance responsibilities,
or dues disputes arise. Required minimums: written bylaws with quorum rules, a
steward or manager with documented authority, graduated-sanction procedures for
rules violations, and a conflict-resolution pathway. Entries with Ostrom-compliant
governance blocks already authored (bake-001, bake-015) have this covered; cooperative
adaptations of market-primary entries must add the governance layer before pooling
capital or paying wages.

**Baker labor scarcity.** Journeyman bakers with sourdough experience are scarce
in town labor markets. A town of 8,500 may have no locally available journeyman
baker at the moment a cooperative or civic facility plans to launch. Plan 12–18 months
of development time before full commercial operation, or recruit from the nearest
urban center with above-median wages and equity participation as incentives.

**Seasonal revenue volatility.** Artisan bread has moderate seasonality (worst month
0.65× average for bake-001); specialty confection is sharper (0.45× for bake-006).
Civic facilities with annual dues structures (bake-015) have shallower seasonality.
All market-primary and cooperative-market entries should maintain a 60-day operating
reserve as a minimum, 90 days for confection-heavy operations.

**Civic political sustainability.** Civic designs pass the cost formula with margins
of 89–95%. That does not guarantee annual budget appropriations. A civic bakery that
cannot document measurable outcomes — loaves distributed to food programs, apprentices
trained, journeyman graduates placed in employment — is vulnerable to budget cuts in
any year with a new council majority. Define KPIs before launch; report against them
every annual budget cycle. A civic bakery that has produced 8–12 credentialed journeyman
bakers over 3 years and distributed 8,000–12,000 loaves/year to food-access programs
has an institutional record that is difficult to cut; one that operates informally
without documentation does not.

---

## Scale-Appropriate Framing

Town scale is where all three lenses are live simultaneously for baking — the first
scale at which this is true. Village scale is constrained by thin member pools and
bounded premium markets. Small-city scale adds financial depth and competitive
intensity. Town scale — 2,000–15,000 residents, a functioning commercial district,
a member pool adequate for 11 of 15 cooperative designs, and a tax base sufficient
for a civic facility — is where the baking catalog offers the most options.

The operative DECLINE-VERDICT framing for town scale: commodity bread declined and
will not revive at small-operator scale; artisan bread declined then revived through
premium segmentation and is the primary market-win niche at town; specialty and
confection baking survived via premium pricing and cultural identity; the mill is
the binding upstream constraint at every scale and must be acknowledged in every design.
A town of 8,500 has documented artisan bread demand, enough organizational capacity
for a cooperative, and enough tax base for a civic facility. The question is which
path has the organizational capacity and political will to pursue.

All three paths working simultaneously in the same town — a private artisan bakery
training apprentices, a cooperative community oven building shared food culture, and
a civic training bakery producing journeyman graduates — is feasible at town scale.
It requires deliberate coordination: the paths do not self-organize. A community that
wants all three paths working together must manage the interfaces actively.

---

## Sources

- `simulations/tier-a-comparator/results/baking/SUMMARY.md` — matrix verdicts for all
  15 entries at town_market, town_coop, and town_civic cells
- `catalog/baking/entries/001-sourdough-artisan-micro.md` — bake-001 economics,
  scale_fit, town_coop win, flour_source_declaration
- `catalog/baking/entries/004-wholesale-artisan-loaf.md` — bake-004 capital, throughput,
  scale_fit.town: good, town_coop fail context
- `catalog/baking/entries/010-civic-neighborhood-bakery.md` — bake-010 civic results,
  per_hh $4.65, scale_fit.town: good, staffing economics
- `catalog/baking/entries/011-apprentice-training-bakery.md` — bake-011 town_civic win,
  break-even 221 vs pool 213, CTE model, per_hh $10.55
- `catalog/baking/entries/012-community-kitchen-collective.md` — bake-012 town_civic win,
  per_hh $7.62, break-even 250, incubator externality
- `catalog/baking/entries/013-farm-to-table-integrated-bakery.md` — bake-013 town_coop win,
  break-even 109, mill-integration capital, grain-sourcing requirement
- `catalog/baking/entries/015-wood-fired-community-oven.md` — bake-015 town_coop win,
  break-even 17, governance model
- `research/trades/baking/DECLINE-VERDICT.md §3, §4, §5` — mill-dependency falsifier;
  artisan revival trajectory; commodity decline; specialty survival via premium segmentation
