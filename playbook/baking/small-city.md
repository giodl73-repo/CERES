---
trade: baking
scale: small_city
doc_type: playbook
version: "1.0"
status: draft
review_status: {panel: pending, editorial: pending}
derived_from:
  - simulations/tier-a-comparator/results/baking/SUMMARY.md
  - catalog/baking/entries/*.md
  - research/trades/baking/DECLINE-VERDICT.md
population_range: 15000-75000
---

# Baking Playbook — Small-City Scale (15,000–75,000 residents)

## Purpose

This playbook translates the Tier A simulation matrix into operational guidance for
small-city-scale baking projects. Readers are economic developers, cooperative founders,
civic planners, and market operators evaluating whether — and in what form — a baking
enterprise is viable for a settlement of 15,000–75,000 people.

Small-city scale is the richest context in the baking catalog. The cooperative lens
saturates: all 15 entries pass small_city_coop with abundant margin. The market lens
remains as selective as at smaller scales (same 5 wins, 2 marginals). The civic lens
narrows sharply: only bake-010 (Civic Neighborhood Bakery) clears small_city_civic;
bake-011 and bake-012, which win at town, fail at small-city on utilization grounds.

The scale framing for small-city baking: premium artisan, specialty confection, and
wholesale market designs find their deepest client base here; cooperative structures
are universally viable; but the civic model collapses to one design because the
utilization threshold the civic lens requires is difficult to clear at small-city
population scale with a single baking facility.

---

## The Matrix at Small-City Scale

Scale parameters used in simulation: population midpoint 45,000; household count 18,000;
feasible coop member pool 900 (45,000 × 2.0%); market wage threshold $62,000/yr;
civic per-household cost ceiling $80/yr.

| Lens             | Wins | Marginals | Fails | Win rate |
|---|---|---|---|---|
| small_city_market | 5    | 2         | 8     | 5/15     |
| small_city_coop   | 15   | 0         | 0     | 15/15    |
| small_city_civic  | 1    | 0         | 14    | 1/15     |

**Total: 21 wins across 45 cells.** Town scale produces 20 wins (6+11+3); small-city
produces 21. The cooperative saturation (15/15) is the defining feature. The civic
collapse (1/15) is the most significant departure from the town-scale pattern and
requires careful explanation.

---

## Market Lens — Winning Designs at Small-City Scale

Five entries win small_city_market; two are marginal. The market lens tracks capital
and revenue model, not population — the same 5–7 entries win at every scale. What
distinguishes small-city performance is that the client base for specialty and premium
designs is deep enough to sustain full throughput from local demand alone.

**bake-001 — Sourdough Artisan Micro-bakery** (capital mid $32,000; payback 0.19 yr;
single-operator; electric-deck)

Small-city scale is technically marginal for bake-001 on `scale_fit` grounds — the
entry records `scale_fit.small_city: marginal` because a small city of 15,000–75,000
introduces competition from established artisan bakeries with higher throughput and
lower unit costs. The payback calculation still clears, but the competitive landscape
changes: a solo micro-bakery at 115 loaves/day is a small operator in a market that
likely already has 1–3 established artisan bakeries. Viable at small-city scale only
if the operator has a distinctive product or sales channel that differentiates from
existing competition: a cultural specialty (overlap with bake-008), an exceptional
sourdough program with DTC subscription reach, or a niche product that fills a gap
in the local artisan market.

**bake-004 — Wholesale Artisan Loaf Bakery** (capital mid $100,000; 350 loaves/day;
2–3 journeyman operators; electric-deck multi-unit)

Small-city is where bake-004 operates most comfortably. A city of 15,000–75,000
can sustain 200–400 loaves/day in B2B wholesale accounts (restaurants, cafés, specialty
grocery, food-service distributors) from local demand with regional extension capacity.
The competition landscape changes: there are more potential wholesale accounts and
also more competing bakeries. Differentiation — sourdough fermentation, heritage grain,
or a specific cultural tradition — is the competitive moat. The $100,000 capital is
most easily financed at small-city scale through a combination of owner equity and SBA
commercial loan; the wholesale revenue base ($430,000–$620,000/year) supports standard
commercial debt service. `scale_fit: good`.

**bake-007 — Japanese-style Wagashi Confection Studio** (capital mid $48,000;
operator: wagashi-master; hybrid-wood-electric; small_city_coop: win)

Small-city scale is the primary operating context for bake-007. A city of 15,000–75,000
can sustain a wagashi studio from a combination of Japanese-diaspora community demand,
specialty retail, and gift-economy purchasing — even in the absence of a large diaspora
population, a well-sited specialty confection studio in a food-culture small city can
generate sufficient volume. The gift-economy differentiation (Tokugawa wagashi survived
industrialization through tea-ceremony patron relationships and seasonal gift-exchange
demand — DECLINE-VERDICT §2.3) is structurally durable: premium wagashi serves a
demand segment that industrial confectionery cannot replicate. The small-city cooperative
path is also open here (all 15 pass small_city_coop), enabling a wagashi studio
worker-cooperative with shared apprenticeship program.

**bake-008 — Ethnic / Cultural Specialty Bakery** (capital mid $45,000; operator:
journeyman-baker trained in specific tradition; electric-deck; small_city_coop: win)

Small-city is where bake-008 reaches maximum viability. Cultural specialty bakeries
that required a specific diaspora density to sustain at village or town scale can
draw from a larger community base here, and even modestly sized cultural communities
(500–2,000 households of a given background in a 45,000-person city) can sustain
a specialty bakery from local demand alone. The competitive advantage remains the
same at every scale: products unavailable from mainstream retail for which community
members have high embedded demand. Small-city scale adds the option of multiple
concurrent cultural-specialty operators serving different communities — a German
rye bakery and a Mexican panadería in the same city are not competitors.

**bake-006 — French-style Pastry / Viennoiserie** (capital mid $65,000; operator:
pastry-chef-master; combi-steam; small_city_market: win, small_city_coop: win)

Small-city is the primary scale for bake-006. The premium confection client base at
45,000 residents is deep enough for 100–150 units/day without regional extension.
The destination-retail model (customers will travel 10–20 miles for a credentialed
pastry shop) amplifies this further. The master pastry chef labor constraint remains
the primary binding limit; the economics at small-city scale justify a wage above
the $62,000 small-city median, which improves operator retention. At small-city scale,
bake-006 + bake-001 combined in a shared commercial space (combi-steam for pastry,
electric-deck for bread, shared proofing and mixing infrastructure) is a viable
dual-product operation that spreads overhead cost and provides the range of premium
products a food-culture small city can sustain.

**bake-009 — Custom Celebration Cake Studio** (marginal at small-city; capital mid
$28,000; operator: pastry-chef-master; event-calendar revenue model)

Marginal at small_city_market — the simulation records a marginal verdict because
take-home approaches but does not clearly exceed the small-city wage threshold.
A city of 15,000–75,000 generates 500–2,000 weddings and major celebrations per year
from local demand alone, which is sufficient for a full-time custom cake studio.
The marginal verdict reflects that the event-calendar revenue cycle (lead-time orders
with significant seasonal peaks) produces uneven monthly revenue that makes the annual
wage calculation marginal at the small-city median. In practice, a well-established
custom cake studio at small-city scale can sustain above-median operator income; the
marginal simulation verdict is a formula artifact of the irregular revenue pattern.

**bake-013 — Farm-to-Table Integrated Bakery** (marginal at small-city; capital mid
$55,000; wood-fired-deck; small_city_coop: win)

Marginal at small_city_market — bake-013's marginal verdict at small-city reflects
that at $62,000/year wage threshold, the take-home from wood-fired artisan bread at
current pricing levels ($9–$22/loaf) is marginal against the higher wage benchmark.
The marginal classification is close: take-home $71,464 vs. median $62,000 — actually
above median, but only a moderate margin. The cooperative path remains fully viable
(all 15 pass small_city_coop). At small-city scale, bake-013 is best structured as
a worker-cooperative rather than a solo market operation: cooperative ownership
distributes the capital and the grain-sourcing risk across 3–5 worker-members, and
the premium narrative (grain-to-loaf provenance) is stronger at small-city scale
where discerning food consumers are more numerous.

**Eight market-fail entries at small-city scale:** These fail for structural reasons
that do not reverse at any scale — cooperative-primary designs with no market revenue
(bake-002, bake-003, bake-010, bake-011, bake-012, bake-014, bake-015) and designs
with low throughput-to-capital ratios. The civic and cooperative entries are correctly
evaluated under their respective lenses.

---

## Cooperative Lens — All 15 Win at Small-City Scale

The cooperative lens saturates at small-city scale. Every catalog entry clears
small_city_coop. The feasible member pool of 900 (45,000 × 2.0%) exceeds the
break-even member count for every design in the catalog, including the highest-capital
entries.

| Break-even range | Entries | Pool margin |
|---|---|---|
| Lowest (9–17 members) | bake-014, bake-015 | 98–99% margin under pool |
| Mid (76–109 members) | bake-001, bake-002, bake-003, bake-004, bake-005, bake-013 | 88–91% margin |
| High (221–250 members) | bake-011, bake-012 | 72–75% margin |

Even the highest break-even entries (bake-011 at 221, bake-012 at 250) clear with
a 72–75% margin under the 900-member pool. The cooperative lens does not differentiate
entries at small-city scale — all pass with substantial margin. Differentiation
should be based on governance model, capital requirements, and operational fit.

**Cooperative richness at small-city scale:**

The 900-member feasible pool enables a density of cooperative organizations that
lower scales cannot sustain. A small city could support a community baking cooperative
(bake-015), a worker-cooperative artisan bakery (bake-001 or bake-008), a shared
commercial kitchen cooperative (bake-012, which fails town_coop but passes small_city_
coop), and a farm-to-table cooperative bakery (bake-013) simultaneously — serving
different demand segments from a common pool of potential members and bakers.
These cooperatives do not compete for members or customers in the same way that
competing private market operations do; their missions and member profiles are
sufficiently distinct to coexist.

**Featured cooperative design: bake-012 — Community Kitchen Collective**

bake-012 is the entry that most meaningfully gains from small-city cooperative
viability. At town scale, bake-012 fails town_coop (break-even 250 > pool 213);
at small-city, it clears comfortably (break-even 250, pool 900). A small-city shared
commercial kitchen collective with 250+ active booking members represents a genuine
food-business incubation platform: 20–40 concurrent cottage-food and micro-catering
operators using a well-equipped multi-oven facility, pooling health-code compliance
costs, and sharing access to commercial-grade equipment that each could not afford
individually. The $95,000 mid capital spread across 250 member shares is $380 per
member — or structured as founding equity versus dues, a $500–$1,000 founding
contribution per member covers the capital with room for an operating reserve.

---

## Civic Lens — One Design Wins at Small-City Scale

One entry clears small_city_civic:

| Entry | Name | per_hh/yr | Threshold | Formula margin |
|---|---|---|---|---|
| bake-010 | Civic Neighborhood Bakery | $0.88 | $80 | 99% |

Fourteen entries fail small_city_civic. This is the sharpest collapse in the catalog
from town to small-city on the civic lens, and it requires explanation.

**Why bake-011 and bake-012 fail at small-city despite winning at town:**

Both bake-011 and bake-012 pass the per-household cost test at small-city scale —
their per_hh costs are actually lower than at town, because the larger household
divisor reduces the cost-per-household further. They fail because the civic lens
applies a utilization test: hours-per-capita against a threshold. At small-city scale
(45,000 residents), the utilization threshold requires more facility-hours of public
use than a single training bakery (bake-011) or single shared kitchen (bake-012) can
generate from their scheduled operations. The facility is too small for the population.

This is not an economic failure; it is a scaling mismatch. A small city of 45,000
residents that wants a civic training bakery should build a larger facility — with 6–8
training stations and a 50-week schedule — rather than the 65 m² entry as specified.
At that expanded scale, the utilization test would clear. Alternatively, the small city
could support multiple bake-011-type facilities (one per district or per school), in
which case the combined utilization would clear.

**bake-010 wins because it clears both tests:**

bake-010 passes small_city_civic on both the per_hh cost ($0.88 vs. $80 threshold —
a 99% margin) and the utilization test. The civic neighborhood bakery's throughput
model (80 loaves/day, 32 hr/week, 5 days/week) produces enough person-hours to clear
the utilization threshold at 45,000 residents. The per-household cost drops to $0.88
at small-city scale — about what a vending machine coffee costs per household per year.

| Scale | per_hh cost | Threshold | Margin |
|---|---|---|---|
| Village | $31.64 | $120 | 74% |
| Town | $4.65 | $100 | 95% |
| Small-city | $0.88 | $80 | 99% |

The fiscal case for bake-010 at small-city is compelling. The operational case is more
nuanced: the staffing model (1 journeyman-baker-instructor) does not scale automatically
with the larger population. A civic neighborhood bakery at 45,000 residents is serving
a catchment area of perhaps 5,000–10,000 residents from one facility — a neighborhood-
level institution, not a city-wide service. The per-household cost calculation spreads
the cost across all 18,000 households, but the facility physically serves only the
households within walking or short-travel distance. A small city that wants city-wide
civic baking access would need 3–5 bake-010 facilities in different neighborhoods —
at which point the aggregate civic investment is $240,000–$400,000 mid capital plus
proportionally higher operating costs.

**The honest small-city civic verdict:** Build bake-010 as a neighborhood-level civic
institution in the highest-density or lowest-income neighborhood where food access and
baking education gaps are most acute. Do not represent it as a city-wide service when
it is a neighborhood service. The $0.88/hh/yr formula math covers the entire city,
but the facility's catchment coverage does not. Design the civic case around the
specific neighborhood served, not the aggregate population.

---

## Implementation Sketches

### Sketch A: Bake-004, Wholesale Artisan Loaf Bakery (Market-Primary, Multi-Operator)

**Context:** A small city of 20,000–50,000 with an active restaurant and specialty
grocery market. The founding operator has existing wholesale relationships from prior
employment or a built customer network. Capital financing through a mix of owner
equity and SBA commercial loan.

**Setup (months 1–4):**

- Lease 65 m² in a light-industrial or food-zoned commercial space with adequate
  ceiling height (minimum 3.0 m) and electrical service capacity for 2–3 deck units
  (3-phase service, 100–150A). Confirm commercial kitchen licensing, exhaust ventilation
  requirements, and floor drainage. Rent estimate: $1,200–$2,000/month.
- Equipment: 2–3 commercial electric deck units ($28,000–$54,000 for 2–3 mid-range
  new units), industrial spiral mixer ($8,000–$12,000), dedicated proofer room or
  large proofing cabinets ($6,000–$9,000), packaging and dispatch infrastructure
  ($3,000–$5,000). Total equipment: $45,000–$80,000 before fitout.
- Installation: 3-phase electrical service upgrade, ventilation ducting, floor drainage
  and steam-injection plumbing: $10,000–$16,000.
- Staff: 2 journeyman-baker operators from day 1. Hiring timeline: plan 3–6 months
  for qualified journeyman hiring at $56,000–$62,000/year each. Journeyman baker
  labor is scarce in small-city labor markets; competing employers include food-service
  operations at urban wages.

**Wholesale account development (months 3–6):**

A 350-loaf-per-day operation requires committed wholesale accounts before full-capacity
launch. Target: 5–8 restaurant accounts (20–40 loaves/week each), 2–3 specialty grocery
accounts (50–100 loaves/week each), and 1–2 café accounts (30–60 loaves/week each).
Begin with 200 loaves/day at 3–4 anchor accounts before adding operators for scale.
Direct-to-restaurant delivery is the highest-margin channel; distributor-mediated
sales reduce margin but increase volume reach. Both channels are viable at small-city
scale; most wholesale bakeries use both.

**Year-1 P&L sketch:**

| Item | Amount |
|---|---|
| Revenue (350 loaves/day × 285 days × $5.50/loaf × 0.65 ramp factor) | $356,906 |
| Annual consumables (flour, packaging, energy) | $62,000 |
| Annual maintenance (3 deck units) | $6,000 |
| Floor-space rent ($1,600/month) | $19,200 |
| 2 journeyman-baker wages | $116,000 |
| Total operating costs | $203,200 |
| Pre-capital gross margin | $153,706 |
| Capital amortization ($112,000 over 15 yr) | $7,467 |
| **Operator/owner draw available (year 1)** | **~$146,239** |

At full throughput (year 2), revenue at 350 loaves/day × $5.50 × 285 days = $549,825.
Against $203,200 operating costs and $7,467 amortization, year-2 net is approximately
$339,000 — supporting the two-operator wage floor, owner margin, and capital reinvestment.
The year-1 ramp assumption (65%) reflects the account-development period; year-2 should
reach 90%+ of capacity with 5–8 established wholesale accounts.

---

### Sketch B: Bake-012, Community Kitchen Collective (Cooperative, Small-City Primary)

**Context:** A small city where bake-012 becomes viable for the first time in the
catalog (it fails town_coop; it passes small_city_coop). A founding coalition of
30–50 food-business operators who currently lack access to licensed commercial kitchen
space: cottage-food bakers, micro-caterers, food-truck operators, and meal-prep
services who collectively need commercial kitchen licensing they cannot afford
individually.

**Why small-city scale unlocks this design:** The break-even member count (250) exceeds
the town feasible pool (213) but falls well within the small-city feasible pool (900).
A small city has enough cottage-food operators, food entrepreneurs, and catering
micro-businesses to populate a 250-member shared commercial kitchen cooperative.
At town scale, this demand does not exist in sufficient density. At small-city scale,
it does.

**Cooperative structure:**

- Register as a cooperative corporation or multi-member LLC before collecting dues
  or accepting booking fees. Adopt bylaws with: (1) defined membership categories
  (full-access member, limited-access member, associate member); (2) booking protocol
  (online reservation system, 2-hour minimum block, 1-week advance maximum); (3) dues
  structure ($400–$600/year full access, $200–$300/year limited access); (4) Ostrom-
  compliant graduated sanctions for booking violations, equipment damage, and cleaning
  failures; (5) steward or manager authority and term limits; (6) conflict-resolution
  pathway culminating in member-vote arbitration.

- Capital: $95,000 mid financed as $500 founding equity per 100 founding members
  ($50,000) plus a USDA Rural Business Development Grant or state food-business
  incubation grant ($30,000–$50,000) for the remainder. Alternatively: founding
  equity at $800–$1,000 per 100 founding members covers the full $95,000 mid capital.

**Operations model:**

Four commercial electric deck ovens in parallel, 3 independent prep stations, shared
proofing and cold storage, commercial spiral mixer, dedicated exhaust system. Average
facility-hours: 8–12 hours/day, 6 days/week, 50 weeks/year = 2,400–3,600 facility-
oven-hours/year. At 3 ovens in parallel average utilization, the facility produces
7,200–10,800 oven-hours/year available for member booking. At $30–$50/hour booking
fee, annual booking revenue: $216,000–$540,000 — well above operating costs.

**Mill dependency in the shared kitchen context:** Members using the shared kitchen
bring their own flour. The cooperative facility does not manage a flour supply chain;
each member is responsible for their own upstream ingredients. The mill-dependency
falsifier applies to individual member businesses, not to the cooperative facility.
Member orientation should include explicit guidance on flour sourcing practices and
inventory management: cottage-food bakers who run out of flour on a booked kitchen
day waste their booking fee and the facility's capacity. A recommendation (not a
requirement) to maintain a 14-day flour buffer is worth including in the member handbook.

---

### Sketch C: Bake-010, Civic Neighborhood Bakery (Civic-Primary, Neighborhood Scale)

**Context:** A small city of 20,000–50,000 with a specific high-priority neighborhood
— a food-access gap area, a low-income district with limited transportation to grocery
stores, or a neighborhood with a strong cultural community whose baking traditions
the city wants to preserve and develop. Municipal budget includes a workforce-
development or food-access line item.

**Siting and scale framing:**

At small-city scale, bake-010 is a neighborhood institution, not a city-wide service.
The facility physically serves the residents within 0.5–1.5 miles who can walk or
take short transit to the location. A civic bakery in a neighborhood of 5,000–8,000
residents is a proportionate institution; presenting it to the city council as serving
all 45,000 residents misrepresents the facility's reach. Present it honestly: this is
a neighborhood-level civic investment in food access and baking skill development
for a defined catchment area. The $0.88/hh/yr per-household cost spread across 18,000
households is the affordability argument; the impact argument should be localized.

**Capital path at small-city:**

At $80,000 mid capital spread across 18,000 households at $0.88/hh/yr, the fiscal
case is so strong that the obstacle is not budget — it is political will and siting.
A 25-year municipal bond at $80,000–$100,000 adds less than $0.05/hh/yr to the
annual cost at the small-city population base. The more significant budget item is
the instructor wage ($56,000–$62,000/year at small-city median) and direct operating
costs. A workforce-development grant covering 50% of instructor cost in years 1–3
is achievable through federal or state WFD channels. From year 4, the combination
of municipal appropriation and member access fees should sustain operations.

**Replication logic:** If the small city determines that food-access gaps or baking
education needs are city-wide, the appropriate response is to replicate bake-010
across 3–5 neighborhoods, not to build a single larger facility. The replication model
produces 3–5 neighborhood-embedded institutions, each with its own instructor and
community relationships, rather than a single large institution that serves no
neighborhood well. The per-unit capital cost ($80,000–$100,000) and per-unit operating
cost ($70,000/year including instructor) makes each facility independently budgetable.
The combined cost of 3 facilities ($300,000 capital, $210,000 annual operating) is
still under $5.00/hh/yr at 45,000 residents — still one-sixteenth of library cost.

---

## Capital Ask by Path

| Path | Design | Capital range | Primary funder |
|---|---|---|---|
| Market: artisan micro | bake-001 | $26k–$59k | Owner equity, SBA microloan |
| Market: wholesale | bake-004 | $72k–$172k | Owner equity, SBA 7(a) + WFD grant |
| Market: specialty confection | bake-006, bake-007 | $32k–$78k | Owner equity, SBA microloan |
| Cooperative: shared kitchen | bake-012 | $107k–$207k | Founding equity + USDA RBDG |
| Cooperative: worker-owned | bake-001, bake-008 | $26k–$55k | Member equity shares |
| Civic: neighborhood bakery | bake-010 | $88k–$138k | Municipal bond or CIP |

**Range across all viable small-city paths: $26,000–$207,000.** Small-city scale
supports the widest capital range in the catalog. Market-primary artisan entries
($26k–$59k) and civic neighborhood bakeries ($88k–$138k) are both within reach of
different financing mechanisms. The shared kitchen cooperative ($107k–$207k) is the
most capital-intensive cooperative design and requires either substantial founding
equity or grant support to launch.

---

## Open Risks at Small-City Scale

**Mill dependency at scale.** The mill-dependency falsifier (DECLINE-VERDICT §3) is
most consequential at small-city wholesale volumes (bake-004: $38,000/year in flour).
At this purchase volume, commodity wheat price volatility is a material financial
exposure — a 30% price spike adds $11,000–$12,000/year to consumables costs. A 12-month
fixed-price supply contract with a regional food-service distributor is worth negotiating
at this volume. The contract will limit exposure to price volatility while accepting
a small premium over spot pricing. For specialty-flour-dependent entries (bake-006,
bake-007, bake-008), supply diversification across two distributors reduces single-
supplier dependency risk, which is more acute for niche ingredients than for commodity
bread flour.

**Competitive intensity.** Small-city markets likely already have 1–3 established
artisan or specialty bakeries. A new entrant competes directly for the premium segment.
Market entries that succeed at small-city scale differentiate by product type (wagashi,
ethnic specialty, wood-fired heritage), by channel (wholesale-only vs. DTC-only vs.
combined), or by price tier (ultra-premium vs. accessible-premium). An operator who
enters the small-city artisan bread market as the third sourdough micro-bakery without
a differentiation strategy is not operating in a gap — they are competing with
established operators for the same customer segment.

**Cooperative governance at 150–250+ members.** bake-012 at small-city requires
250+ dues-paying members. A cooperative with 250 members has governance complexity
comparable to a small nonprofit: a board of directors, standing committees, a part-
time or full-time manager, annual member meetings with quorum requirements, and
formalized financial reporting. Founding members who expect informal consensus
governance at this scale will find the cooperative ungovernable within 18 months.
Budget for professional cooperative development assistance at founding ($5,000–$10,000
for a cooperative development consultant) — it is the cheapest insurance against the
governance failures that end most early-stage cooperatives.

**Zoning complexity.** Light-industrial and food-production zoning in small-city
contexts is often limited in area and may have lease premiums compared to town scale.
Wood-fired equipment (bake-013, bake-015) adds air-quality permit requirements.
Multi-deck commercial installations (bake-004, bake-012) require 3-phase electrical
service and dedicated exhaust ventilation that not all commercial buildings can
accommodate without significant infrastructure investment. Confirm zoning classification,
air-quality permit requirements, electrical service capacity, and ceiling height before
signing any lease.

**Labor market competition.** Small-city alternative wages are higher than at town
scale. The simulation uses $62,000/year as the small-city skilled-trades median
(SCALES.md §3). A journeyman baker considering a position at a small-city bakery
competes against food-service, hospitality, and specialty-retail wages in the same
labor market. Below $56,000/year, qualified journeyman bakers will consider
alternatives. The bake-004 two-operator model must budget $116,000/year in labor
before any owner draw; the bake-010 civic model must budget $56,000–$62,000/year
for the instructor-baker. These labor costs are the largest single expense line for
every design that employs a journeyman operator — budget them first, not last.

---

## Scale-Appropriate Framing

Small-city scale is the only scale in the baking catalog where the cooperative lens
fully saturates. At village scale, cooperative governance is viable for 2 of 15 entries;
at town scale, 11 of 15; at small-city, all 15. The 900-member feasible pool clears
every break-even threshold in the catalog with substantial margin. This does not mean
every baking design should be structured as a cooperative at small-city scale — it
means that no entry is excluded from the cooperative form by member-pool constraints.

The civic lens narrows sharply: 3 wins at town collapse to 1 win at small-city.
The reason is utilization: civic lens tests require that a single facility serve the
whole population at a minimum hours-per-capita threshold, and a single baking facility
cannot generate enough person-hours to pass that test for a 45,000-person population.
The civic path at small-city is available — bake-010 clears — but must be understood
as a neighborhood institution, not a city-wide service.

The market lens is as selective at small-city as at every other scale: 5 wins with
2 marginals. Premium artisan, specialty confection, and wholesale market designs find
their deepest client base here, but the competitive landscape is also more intense.
Market entries at small-city scale must differentiate by product, channel, or price tier.

The DECLINE-VERDICT framing applies at small-city exactly as at smaller scales:
commodity bread declined universally and is not the target; artisan bread revived
via premium segmentation and is the primary market-win niche; specialty and confection
baking survived via cultural identity and premium pricing; the mill is the binding
upstream constraint for every design. At small-city volumes, the mill constraint
operates at higher dollar exposure — a wholesale bakery's flour bill is $38,000/year,
not $8,500. Manage it accordingly.

---

## Sources

- `simulations/tier-a-comparator/results/baking/SUMMARY.md` — matrix verdicts for all
  15 entries at small_city_market, small_city_coop, and small_city_civic cells
- `catalog/baking/entries/001-sourdough-artisan-micro.md` — bake-001 scale_fit.small_city:
  marginal context, economics
- `catalog/baking/entries/004-wholesale-artisan-loaf.md` — bake-004 capital, throughput,
  scale_fit: good, staffing model
- `catalog/baking/entries/006-french-pastry-viennoiserie.md` — bake-006 small_city primary
  context, operator skill constraint, capital
- `catalog/baking/entries/007-japanese-wagashi-confection.md` — bake-007 gift-economy
  differentiation, small_city primary context
- `catalog/baking/entries/010-civic-neighborhood-bakery.md` — bake-010 small_city_civic
  win, per_hh $0.88, neighborhood-scale framing, scale table across all 3 scales
- `catalog/baking/entries/011-apprentice-training-bakery.md` — bake-011 small_city_civic
  fail context, utilization threshold analysis
- `catalog/baking/entries/012-community-kitchen-collective.md` — bake-012 small_city_coop
  win (break-even 250, pool 900), cooperative saturation, booking model
- `catalog/baking/entries/013-farm-to-table-integrated-bakery.md` — bake-013 small_city
  marginal market, small_city_coop win, mill-integration cooperative context
- `research/trades/baking/DECLINE-VERDICT.md §2.3, §3, §4, §5` — wagashi survival via
  gift-economy; mill-dependency falsifier; premium segmentation survival mechanisms;
  commodity decline
