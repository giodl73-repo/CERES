---
trade: baking
scale: village
doc_type: playbook
version: "1.0"
status: draft
review_status: {panel: pending, editorial: pending}
derived_from:
  - simulations/tier-a-comparator/results/baking/SUMMARY.md
  - catalog/baking/entries/*.md
  - research/trades/baking/DECLINE-VERDICT.md
population_range: 500-2000
---

# Baking Playbook — Village Scale (500–2,000 residents)

## Purpose

This playbook translates the Tier A simulation matrix into operational guidance for
village-scale baking projects. Readers are community organizers, rural-development
officers, and prospective operators evaluating whether an artisan bakery is viable
for a settlement of 500–2,000 people. The playbook extracts market, cooperative, and
civic verdicts from the 15-entry simulation, identifies which designs clear village-scale
thresholds, and provides implementation sketches for the designs that do. It does not
replace the per-entry catalog files; it synthesizes them for someone who needs a
decision, not a bibliography.

The honest framing for village scale: baking here is primarily about premium
direct-to-consumer sales. The cooperative lens barely opens (two entries only), and
the civic lens produces formula wins that do not survive qualitative scrutiny at this
population size. Anyone planning a village bakery should read the market section first
and treat the other lenses as supplementary.

---

## The Matrix at Village Scale

Out of 15 catalog entries evaluated under three lenses, village-scale performance is:

| Lens           | Wins | Marginals | Fails | Win rate |
|---|---|---|---|---|
| village_market | 7    | 1         | 7     | 7/15     |
| village_coop   | 2    | 0         | 13    | 2/15     |
| village_civic  | 4    | 0         | 11    | 4/15     |

The market lens carries almost all the weight at village scale. Seven entries win
outright; one is marginal. The cooperative lens is nearly closed: only the two
minimum-capital entries clear it, and both have wage-fails on the market lens —
they are community-access amenities, not businesses. The civic lens formally passes
for four entries, but two of those (bake-010 and bake-012) carry `scale_fit.village:
poor` qualifications and the other two (bake-011 and bake-015) require careful reading:
bake-015 (wood-fired community oven) is a genuine village-scale civic asset, while
bake-011 (apprentice training bakery) passes the formula but is stretched thin in a
village context. Section 6 addresses this directly.

---

## Market Lens — Winning Designs at Village Scale

Seven entries win village_market. All seven also win at town and most at small-city —
the market lens in this catalog is scale-invariant, tracking capital and revenue model
rather than population. What distinguishes performance at village scale is demand depth:
a village of 500–2,000 residents can support a premium direct-to-consumer bakery, but
the addressable customer base is bounded, and some entries that win on formula require
a regional draw to sustain full throughput.

**bake-001 — Sourdough Artisan Micro-bakery** (capital mid $32,000; operator:
journeyman-baker; energy: electric-deck; payback 0.19 yr)

The village-scale flagship entry. Single-operator naturally-leavened bread bakery at
115 loaves/day, $8/loaf mid pricing, direct-to-consumer or farmers-market channel. At
mid pricing and throughput, gross revenue is approximately $236,000 per year against
roughly $14,000 in cash operating costs — the margin is large. The binding constraints
are not economic; they are regulatory (commercial kitchen licensing required), skill
(sourdough fermentation judgment takes 36–42 months to form), and market (the premium
segment at village scale may not absorb 115 loaves/day from local customers alone; a
CSA delivery or subscription component is likely needed). `scale_fit.village: good`.
Mill dependency: industrial flour purchased from regional distributor; no milling
infrastructure assumed.

**bake-004 — Wholesale Artisan Loaf Bakery** (capital mid $100,000; operator:
journeyman-baker × 2–3; energy: electric-deck multi-unit; payback: market win)

Multi-deck wholesale operation at 350 loaves/day supplying restaurants, cafés, and
grocery accounts. Wins village_market on payback, but has `scale_fit.village: marginal`
because a village of 500–2,000 residents cannot generate sufficient B2B wholesale
accounts to sustain 350 loaves/day. This entry's village win is realistic only if the
operator serves a regional wholesale radius — multiple towns, not just the home village.
At $100,000 capital, it is the most capital-intensive market winner at this scale.
Not the first choice for a village-primary operation; better read as a town-scale entry
that can be sited in a village with good road access to a broader market.

**bake-006 — French-style Pastry / Viennoiserie** (capital mid $65,000; operator:
pastry-chef-master; energy: combi-steam; payback: market win)

Specialty laminated dough and pâte-à-choux shop at 150 units/day. Wins market on
payback at premium confection pricing ($8–$18 per unit). The operator skill floor
(pastry-chef-master for laminated doughs) is the binding constraint: finding or
being a master pastry chef in a village setting is the hard part, not the economics.
`scale_fit.village: poor` — the premium confection customer base in a 500–2,000
person village is thin; this entry needs either a destination-retail draw or a regional
delivery operation to sustain throughput. Viable at village scale only for an operator
with an established premium reputation or an online DTC channel.

**bake-007 — Japanese-style Wagashi Confection Studio** (capital mid $48,000;
operator: wagashi-master; energy: hybrid-wood-electric; payback: market win)

Specialist wagashi studio producing mochi, manjū, nerikiri, and yokan at premium
gift and specialty retail pricing. The market win reflects high per-unit confection
pricing and low variable cost of rice flour and sweet bean paste relative to wheat
flour. The demand base at village scale is niche: this entry requires an established
Japanese-diaspora community, a specialty food tourism market, or a well-developed
DTC gift-economy channel to sustain throughput. `scale_fit.village: poor` in standard
US village demographics; viable where the cultural demand base exists. Mill dependency
note: wagashi is not flour-dependent in the same way as bread; bean paste, rice flour,
and sugar are the upstream inputs, but all are purchased commodity inputs — the binding
upstream constraint is sugar and specialty-grain sourcing, not wheat milling.

**bake-008 — Ethnic / Cultural Specialty Bakery** (capital mid $45,000; operator:
journeyman-baker trained in a specific tradition; energy: electric-deck; payback:
market win)

Bakery serving a diasporic or immigrant community whose baked staples are unavailable
or unreliable from mainstream retail. Wins village_market on the same premium-pricing
logic as the other specialty entries. The demand base is defined by community identity:
a German-rye bakery needs a community of German-heritage customers; an Ethiopian injera
producer needs a local Ethiopian diaspora; a Mexican panadería needs a Spanish-speaking
neighborhood. Where that community exists in a village or adjacent township, this entry
is among the most sustainable in the catalog — demand is socially embedded, not trend-
contingent, and the price premium is substantial relative to supermarket substitutes.
Where the community does not exist at village scale, this entry does not work.
`scale_fit.village: good` when the matching community is present.

**bake-009 — Custom Celebration Cake Studio** (capital mid $28,000; operator:
pastry-chef-master; energy: convection-electric; payback: market win but marginal)

High-value custom cakes on lead-time order at $150–$900 per cake. Wins village_market
at mid pricing on payback, but has `scale_fit.village: poor` and the simulation records
a `marginal` verdict at several cells. The event-calendar revenue model (wedding and
birthday orders) is structurally dependent on event density: a village of 500–2,000
residents generates perhaps 30–80 weddings and larger celebrations per year — less
than one per week — which is insufficient to fill a full-time studio. At village scale,
this is a part-time or regional operation. Viable as a solo practice if the operator
draws from a 30-mile radius, or as a secondary offering within a multi-product pastry
shop (bake-006 + bake-009 combined is stronger than either alone).

**bake-013 — Farm-to-Table Integrated Bakery** (capital mid $55,000; operator:
journeyman-baker; energy: wood-fired-deck; payback 0.81 yr)

On-farm wood-fired bakery with co-located stone mill; the one entry in the catalog
that proposes to close the grain-to-loaf loop. Wins village_market, and `scale_fit.village:
good` because rural/agricultural siting is the natural context. This is the entry most
directly relevant to the DECLINE-VERDICT mill-dependency falsifier: the design
explicitly takes on milling as a co-equal challenge alongside baking, and the capital
cost reflects it ($55,000 mid includes a small stone mill). The mill is not a free
assumption here — it is an operational system requiring its own maintenance, flour
consistency management, and grain sourcing. Operators who want to differentiate on
grain provenance and command $9–$22/loaf pricing for heritage-grain hearth loaves are
the target. The 0.81-year payback is slower than bake-001 because both capital and
throughput reflect the wood-fired scheduling constraint (firing takes 2–3 hours before
baking can begin). Viable at village scale as an on-farm direct-market operation with
CSA or farm-stand channel.

**Summary of market winners at village scale:**

The two designs to anchor a village baking program around are **bake-001** (Sourdough
Artisan Micro, $32,000 capital, `scale_fit.village: good`) and **bake-008** (Ethnic
Cultural Specialty, $45,000 capital, `scale_fit.village: good` where community is present).
Both target premium segments with genuine demand. Bake-013 (Farm-to-Table, $55,000) is
a strong second choice for an agricultural community with direct-market infrastructure.
The remaining market winners — bake-004, bake-006, bake-007, bake-009 — win on formula
but require regional reach or specialist demand conditions that are not present in most
villages.

---

## Cooperative Lens — Winning Designs at Village Scale

Only two entries clear village_coop: **bake-014** (Apartment Home Micro-bakery,
break-even 9 members, feasible pool 31.2) and **bake-015** (Wood-fired Community
Oven, break-even 17 members, feasible pool 31.2).

Both win for the same structural reason: their break-even member count falls below
the village feasible pool of approximately 31 (500–2,000 residents × 2.5%
participation rate = 13–50 members, midpoint ~31). Every other entry in the catalog
requires more members than a village can reliably supply at a 2.5% participation rate.

**bake-014 — Apartment Home Micro-bakery:** Capital $5,500 mid. Cottage-food-law
home baking at 20 loaves/day maximum. The cooperative win here reflects shared
equipment costs across a handful of home bakers — the "cooperative" is really a
small group pooling a commercial mixer and proofing supplies to reduce per-person
startup cost. The market verdict for this entry is a wage fail at village scale
(take-home $8,890 vs. median $48,000): this is not a living-wage business, it is a
supplemental-income or hobby-scale activity. The cooperative win is real but must be
framed honestly: bake-014 in cooperative mode is a community baking club with shared
equipment, not a commercial operation.

**bake-015 — Wood-fired Community Oven:** Capital $18,000 mid. The communal dome
oven model — a shared masonry oven on the village commons where residents bring their
own dough and pay a firing fee. Break-even 17 members with annual dues of ~$192/year.
This entry is the most interesting cooperative design at village scale: it is historically
grounded in the *four banal* tradition (DECLINE-VERDICT §2.1) and in contemporary
community-oven revival projects, and it serves a genuine food-access and community-
cohesion function without requiring commercial kitchen licensing for users who bring
their own dough. It also passes village_civic (see below). The cooperative form here
is appropriate: 17–25 member households share firing costs, the fire-keeper receives
a modest stipend, and the oven is a community-owned resource rather than a private
business.

**On the cooperative lens at village scale:** The honest assessment mirrors the
smithing playbook's finding at village scale. Cooperative governance fails at village
scale for everything except minimum-capital designs because the member pool is too
thin. A village that wants the cooperative form should focus on bake-015 (community
oven) as the cooperative-primary option. Everything else requires town-scale population
to clear the break-even threshold.

---

## Civic Lens — Winning Designs at Village Scale

Four entries pass the village civic formula:

| Entry | Name | per_hh/yr | Threshold | Formula margin |
|---|---|---|---|---|
| bake-010 | Civic Neighborhood Bakery | $31.64 | $120 | 74% |
| bake-011 | Apprentice Training Bakery | $71.76 | $120 | 40% |
| bake-012 | Community Kitchen Collective | $51.80 | $120 | 57% |
| bake-015 | Wood-Fired Community Oven | $6.70  | $120 | 94% |

However, three of these four carry `scale_fit.village: poor`. The formula wins are
real; the qualitative assessment is different for each.

**bake-010 (Civic Neighborhood Bakery)** — $80,000 mid capital; requires a full-time
journeyman-baker-instructor at ~$52,000–$56,000/year. A village of 500–2,000 residents
(~400 households) levying $31.64/hh/yr generates approximately $12,600/year in civic
funding. That is less than a quarter of the instructor's annual wage alone, before
capital amortization. The formula passes because the civic lens checks per-household
cost against a threshold, not whether the household levy covers the staffing cost.
A civic neighborhood bakery at village scale requires substantial external subsidy or
a grant-funded foundation period to be staffable. Without that, the $80,000 capital
becomes a white elephant. Honest verdict: do not build bake-010 at village scale
without an identified funding source for the instructor wage that is not the household
levy alone.

**bake-011 (Apprentice Training Bakery)** — $85,000 mid capital; break-even 221
cooperative members against a village feasible pool of 31. The civic formula passes
at $71.76/hh/yr against $120 threshold, but this entry's apprentice intake model
requires a school or vocational program partnership to fill training cohorts — an
institutional density not present at village scale. Town-primary or small-city-primary.
The village civic formula win should not drive planning decisions.

**bake-012 (Community Kitchen Collective)** — $95,000 mid capital; a shared
commercial kitchen with multiple oven bays for member booking. Requires break-even
250 cooperative members against a village feasible pool of 31. Fails coop lens badly.
The civic formula passes at $51.80/hh/yr, but a shared commercial kitchen at village
scale cannot generate the booking volume needed to cover operating costs at a civic
levy alone. This entry is small-city-primary.

**bake-015 (Wood-fired Community Oven)** — $18,000 mid capital; the genuine
village-scale civic asset. Formula passes at $6.70/hh/yr against $120 threshold —
a 94% margin — and it also passes the utilization threshold (3.072 hrs/capita vs.
the 2.0 threshold). Unlike the other civic winners, bake-015 passes on both formula
and qualitative grounds at village scale. The capital is proportionate, the staffing
model (a fire-keeper, not a full-time instructor) is feasible on village-scale
civic budget, and the facility delivers real food-access value: residents can bake
their own bread in a communal oven for a per-use fee without acquiring commercial
kitchen licensing. `scale_fit.village: good` for both coop and civic modes.

**The honest village civic verdict:** The only civic design that genuinely fits village
scale is **bake-015**. The other three formula wins (bake-010, bake-011, bake-012) are
capital-intensive staffed facilities whose operating costs exceed what a village
household levy can cover. A village that wants civic baking infrastructure should start
with bake-015, which delivers community oven access at $18,000 capital and $6.70/hh/yr
— and can double as a cooperative (bake-015 wins both village_coop and village_civic).

---

## Implementation Sketches

### Sketch 1: Bake-001, Sourdough Artisan Micro-bakery (Market-Primary)

**Context:** Village of 1,000 residents in a food-culture-aware area with an active
farmers market or nearby town with weekend market. Operator is a journeyman baker
(36+ months sourdough experience) or is willing to apprentice for 12–18 months before
opening. Commercial kitchen space or cottage-food licensing pathway confirmed.

**Pilot-year structure:**

- Months 1–2: Regulatory pathway. Confirm state cottage-food exemption limits
  (varies $5,000–$75,000 by state). If cottage-food ceiling is insufficient for
  target revenue, identify a licensed commercial kitchen to lease ($300–$600/month
  for 15–20 hours/week share). Obtain commercial food handler certification. Confirm
  farmers-market vendor permit requirements.
- Months 3–4: Equipment acquisition and fitout. Electric deck oven ($12,000–$18,000
  new, or $8,000–$10,000 refurbished), proofing cabinet ($3,000–$5,000), commercial
  spiral mixer ($3,000–$4,000), smallwares (bannetons, lames, bench scrapers:
  $800–$1,500). Total $18,000–$28,000 at low-to-mid capital. Electrical service
  upgrade if required (30–60A dedicated circuit: $1,500–$3,500 installed).
- Month 5: Establish flour supply. Contact regional food-service distributor (US
  Foods, Sysco, or regional co-op) for commodity bread flour pricing and delivery
  schedule. Confirm 3-day typical lead time and establish 3-week flour inventory
  buffer (~$450 working capital at 115 loaves/day × $0.42/loaf flour cost).
- Month 6: Soft launch at farmers market. Begin at 60–80 loaves per market day
  (one market per week). Target sell-through on first three markets before scaling.
  Adjust dough hydration and proofing schedule for local ambient temperature.
- Months 7–12: Ramp to 2–3 market days per week plus a direct subscription list.
  Target 80 regular subscription households by month 12.

**Year-1 P&L sketch:**

| Item | Amount |
|---|---|
| Revenue (115 loaves/day × 285 days × $8/loaf × 0.60 ramp factor) | $157,740 |
| Annual consumables (flour, packaging, energy) | $8,500 |
| Annual maintenance | $1,200 |
| Floor-space rent (commercial kitchen share) | $4,800 |
| Operator wage (owner-draw model) | — |
| Total cash operating costs | $14,500 |
| Pre-draw gross margin | $143,240 |
| Capital amortization ($36,000 over 15 yr) | $2,400 |
| **Operator draw available (year 1)** | **~$140,840** |

Even at a 60% ramp-up revenue assumption, this exceeds the village-scale skilled-trades
median by a wide margin. The payback is legitimately fast (0.19 years at full throughput).
The risk is market absorption: 115 loaves/day × 285 days = 32,775 loaves/year is a lot
of bread for a 1,000-person village. If local demand absorbs only 50 loaves/day, annual
revenue at $8/loaf drops to roughly $114,000 — still workable, but the operator must
add a delivery or subscription channel to reach full throughput.

**Year-2 steady state:**
Full throughput, established subscription list, farmers-market regulars. Target 100+
weekly subscription households plus market walk-in. Introduce one specialty loaf per
season to sustain premium pricing.

---

### Sketch 2: Bake-015, Wood-Fired Community Oven (Civic and Coop dual-mode)

**Context:** Village of 800 residents with a commons, park, or churchyard available
for a permanent installation. Community interest in food sovereignty, local food
culture, or emergency preparedness is the organizing motivation. No commercial baking
licensing required for users who bring their own dough.

**Pilot-year structure:**

- Months 1–3: Community organizing and site selection. Identify a suitable
  outdoor or partially covered site with community ownership or long-term lease
  agreement. Form a founding steering committee of 8–12 households.
- Months 4–6: Construction. Masonry dome oven with insulating jacket and chimney
  ($8,000–$14,000 materials; labor is either volunteer or contracted masonry at
  $4,000–$8,000 additional). Covered wood-storage shed ($1,000–$2,000). Total
  installed: $13,000–$24,000 (mid $18,000). Obtain local air-quality permit for
  wood smoke (jurisdiction-specific; typically $200–$600 permit fee plus inspection).
- Month 7: Governance establishment. Register as a nonprofit or unincorporated
  cooperative association. Adopt membership agreement: dues structure ($150–$250/year
  per household member), booking protocol for firing days (typically 2–3 per week),
  fire-keeper role and stipend ($4,000–$6,000/year for part-time fire management),
  graduated-use rules and conflict resolution protocol.
- Months 8–12: Operating season. Target 15–20 dues-paying member households in
  year 1. Establish weekly or bi-weekly community bake days. Revenue from dues
  covers fire-keeper stipend and wood supply ($1,800–$2,400/year for dry hardwood
  at 25 kg/firing × 3 firings/week × 50 weeks).

**Capital ask:**

| Item | Amount |
|---|---|
| Masonry oven materials and construction | $14,000–$22,000 |
| Wood storage and site infrastructure | $1,500–$3,000 |
| Permits and legal establishment | $500–$1,500 |
| First-year operating reserve | $3,000–$5,000 |
| **Total first-year ask** | **$19,000–$31,500** |

Community fundraising, a small municipal grant, or a combination of member dues and
one-time capital pledges are the typical funding paths. At $18,000 mid capital spread
across 20 founding member households, the per-household capital share is $900 —
achievable as a one-time founding contribution.

---

## Capital Ask Summary

| Design | Capital (mid) | Install | 6-month reserve | Total ask |
|---|---|---|---|---|
| Bake-001 (sourdough micro) | $32,000 | $4,000 | $7,250 | $43,250 |
| Bake-013 (farm-to-table) | $55,000 | $6,000 | $10,875 | $71,875 |
| Bake-015 (community oven) | $18,000 | $2,000 | $2,500 | $22,500 |

The $43,250 ask for bake-001 funds one journeyman baker's solo commercial micro-bakery
serving a village plus surrounding township. The $22,500 ask for bake-015 funds a
community asset that serves any household that wants to bake. A village choosing between
them is choosing between a private commercial bakery (bake-001) and a civic/cooperative
food-access facility (bake-015); the right choice depends on the community's goals.

---

## Open Risks at Village Scale

**Mill dependency is the defining constraint.** The DECLINE-VERDICT mill-dependency
finding applies to every entry in this catalog (DECLINE-VERDICT §3, §4). No small-scale
commercial baking form in the historical record was autonomous from an upstream grain-
milling supply chain. Every market-win entry at village scale — bake-001, bake-004,
bake-006, bake-007, bake-008, bake-009 — either explicitly declares industrial-flour-
purchased dependency or depends on commodity specialty-ingredient supply. The one
entry that proposes to integrate milling (bake-013) treats the mill as a capital and
operational system requiring its own management, not a free assumption. Village bakery
operators should ask this question before launch: *What happens to my flour supply if
the regional distributor is disrupted for 3 weeks?* A 3-week flour buffer (roughly
$450–$600 working capital for bake-001 mid throughput) is the minimum prudent inventory
practice. Operators in remote rural areas with limited distributor coverage should
extend this to 6 weeks.

**Market thinness.** A village of 500–2,000 residents generates a bounded premium
customer base. At $8/loaf and 115 loaves/day, bake-001's full throughput requires
roughly 14,000 loaf-purchases per year from a local population of perhaps 400–800
households. That implies each household purchasing one loaf every 10–15 days on
average — plausible for a loyal customer base, but not universal. Most operators at
village scale will need to extend their market reach beyond the village boundary through
CSA delivery, farmers-market presence at a nearby town, or DTC subscription. Plan the
market before buying the oven.

**Regulatory complexity.** Commercial kitchen licensing, health-department inspection,
food-handler certification, and farmers-market vendor permits are not optional for any
entry except bake-015. The regulatory path is navigable but takes time: plan 2–4 months
for commercial kitchen licensing and health inspection in most US jurisdictions. Cottage-
food exemptions vary dramatically by state; verify the ceiling in your jurisdiction
before assuming home-kitchen sales cover your revenue target.

**Skill formation timeline.** Sourdough fermentation judgment — the rate-limiting skill
for bake-001 and bake-013 — takes 36–42 months to form through lived practice. This is
not a training problem that a weekend course solves. An operator who opens a sourdough
bakery without 3 years of hands-on fermentation experience will produce inconsistent
product for 12–18 months. Plan accordingly: either the operator is already at journeyman
level, or the launch timeline must accommodate a 12–18 month development phase at
smaller commercial volumes.

**Single-operator succession.** A one-person village bakery has no succession if the
operator leaves or is incapacitated. The apprenticeship path in bake-001 (36–42 months)
is the mitigation — but it is a long one. Name the apprentice intake process at founding.

---

## Scale-Appropriate Framing

Village baking is feasible in specific configurations. The market-primary artisan
micro-bakery (bake-001) and the community wood-fired oven (bake-015) are both genuine
village-scale designs — one a private premium business, the other a civic food asset.

The limits are equally clear. Thirteen of fifteen catalog entries either fail village_market
or win on formula while carrying `scale_fit.village: poor` flags. Cooperative governance
is viable only for bake-014 (hobby-scale) and bake-015 (community oven). The civic lens
produces formula wins that do not survive staffing-cost analysis for anything except
bake-015.

The correct framing for a village planning committee: *Is there a premium direct-to-
consumer market here for artisan bread, and is there an operator with journeyman
fermentation skill available?* If yes to both, bake-001 is financially viable with
$43,000 in total capital and no ongoing subsidy. If the community wants a shared food
asset regardless of commercial viability, bake-015 delivers genuine value at $22,500
with minimal operating overhead. Most higher-capital designs in this catalog — training
bakeries, community kitchens, wholesale operations — need town-scale population (2,000–
15,000) to clear all three lenses. The village niche for baking, like the village niche
for smithing, is real but narrow.

---

## Sources

- `simulations/tier-a-comparator/results/baking/SUMMARY.md` — matrix verdicts for all
  15 entries at village_market, village_coop, and village_civic cells
- `catalog/baking/entries/001-sourdough-artisan-micro.md` — bake-001 economics, scale_fit,
  sim_params, throughput, and flour_source_declaration
- `catalog/baking/entries/013-farm-to-table-integrated-bakery.md` — bake-013 results,
  scale_fit, mill-integration capital context
- `catalog/baking/entries/015-wood-fired-community-oven.md` — bake-015 results, scale_fit,
  cooperative and civic dual-win, per_hh_cost $6.70
- `catalog/baking/entries/014-apartment-home-micro-bakery.md` — bake-014 village_coop win;
  wage-fail note
- `catalog/baking/entries/010-civic-neighborhood-bakery.md` — bake-010 village_civic win;
  scale_fit.village: poor; per_hh $31.64 vs staffing cost analysis
- `catalog/baking/entries/011-apprentice-training-bakery.md` — bake-011 village_civic win;
  scale_fit.village: poor; break-even 221 vs pool 31
- `catalog/baking/entries/012-community-kitchen-collective.md` — bake-012 village_civic win;
  scale_fit.village: poor; break-even 250 vs pool 31
- `research/trades/baking/DECLINE-VERDICT.md §3, §4, §5` — mill-dependency falsifier;
  artisan/premium niche as restorable; commodity household baking as non-restorable
