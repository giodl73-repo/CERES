---
trade: smithing
scale: village
doc_type: playbook
version: "1.0"
status: draft
review_status: {panel: pending, editorial: pending}
derived_from:
  - simulations/tier-a-comparator/results/SUMMARY.md
  - catalog/smithing/entries/*.md
  - research/trades/smithing/DECLINE-VERDICT.md
population_range: 500-2000
---

# Smithing Playbook — Village Scale (500–2,000 residents)

## Purpose

This playbook translates the Tier A simulation matrix into operational guidance for
village-scale smithing projects. Readers are community organizers, rural-development
officers, and prospective operators evaluating whether a forge is viable for a
settlement of 500–2,000 people. The playbook extracts market, cooperative, and civic
verdicts from the 15-entry simulation, identifies which designs clear village-scale
thresholds, explains why most do not, and provides an implementation sketch for the
designs that do. It does not replace the per-entry catalog files; it synthesizes them
for someone who needs a decision, not a bibliography.

---

## The matrix at village scale

Out of 15 catalog entries evaluated under three lenses, village-scale performance is:

| Lens         | Wins | Marginals | Fails | Win rate |
|---|---|---|---|---|
| village_market | 7 | 0 | 8 | 7/15 |
| village_coop   | 2 | 0 | 13 | 2/15 |
| village_civic  | 2 | 0 | 13 | 2/15 |

The market lens is the workhorse at village scale. Seven designs clear it — all are
repair-dominant, low-capital entries whose payback timeline is driven by the
labor-premium repair market rather than volume production. The cooperative lens is
thin: only the two minimum-capital part-time designs (forge-001, forge-014) clear
it because their break-even member count (15) falls inside the village feasible pool
of 31 members. All higher-capital designs require more members than a village can
supply. The civic lens formally passes for two entries (forge-004, forge-011), but
both carry a `scale_fit.village: poor` qualification that the formula cannot capture;
see Section 6 for the full diagnosis.

---

## Market lens — winning designs at village scale

Seven entries win village_market. All have payback under one year on a return-on-capital
basis; what distinguishes them is capital level, operator skill requirement, and
whether the demand base is realistic in a thin rural market.

**forge-002 — Induction-Modular Small Repair** (capital mid $42,000; operator: journeyman;
energy: induction-electric 12 kWh/hr; payback 0.18 yr)

A single-operator induction forge optimized for tool and implement repair. Wins
village_market on payback but carries a `scale_fit.village: marginal` flag. Induction's
clean regulatory profile helps in village settings where combustion permits are
cumbersome, but the $42,000 capital cost requires a viable local repair customer base
before commitment. At village scale — 500 to 2,000 residents — weekly repair volume
may not fill a 35-hour work week for a full-time journeyman without drawing customers
from a wider radius. Pair with forge-012 (farriery) at an adjacent rural route to share
travel and service area.

**forge-003 — Shared Tool-Library Coal Forge** (capital mid $28,000; operator: journeyman;
energy: coal 8 kg/hr; payback 0.44 yr)

A cooperative-oriented coal forge with a `lens_fit.market: marginal` rating — it wins
village_market on the payback metric but is not designed for private-market operation.
The payback figure reflects the low capital cost ($28,000), not a robust revenue model.
At village scale the cooperative structure is infeasible (break-even 60 members vs.
feasible pool of 31); as a privately-owned market operation it is under-capitalized for
full-time employment. Best read as a transitional design: viable if operated part-time
or as a second forge in a multi-operator rural complex. Coal supply-chain risk at rural
village scale is real; verify a local supplier before committing to coal.

**forge-005 — Frontier-Revival Coal Repair Forge** (capital mid $22,000; operator: journeyman;
energy: coal 8 kg/hr; payback 0.26 yr)

This is the strongest market-lens candidate at village scale and the design most
directly matched to rural repair demand. It has `scale_fit.village: good`, `lens_fit.market:
good`, and the lowest capital of any full-function repair forge in the catalog. At
$22,000 mid capital with a repair-dominant mix (70% repair), it targets exactly the
demand segment DECLINE-VERDICT §5 identifies as "most durable" — agricultural equipment
repair, farm-implement maintenance, and bespoke rural hardware that cannot be shipped
to a factory. A journeyman smith serving a village catchment plus surrounding rural
area of 2,500–3,000 total service-area population is the viable configuration.

**forge-006 — Induction Bladesmith** (capital mid $70,000; operator: journeyman-to-master;
energy: induction-electric; payback 0.67 yr)

Wins village_market but has `scale_fit.village: poor`. The payback metric passes because
blade and precision edge-tool pricing is high; the underlying demand problem is that a
village of 500–2,000 residents cannot generate sufficient commission volume to sustain a
full-time specialty bladesmith without a regional mail-order or direct-to-consumer online
channel. Viable at village scale only if the operator explicitly plans a hybrid local-plus-
online revenue model. Do not rely on walk-in village demand alone.

**forge-010 — Architectural Ironwork Bespoke** (capital mid $95,000; operator: master;
energy: hybrid propane-induction; payback 0.88 yr)

Wins village_market with the longest payback of the seven winners. Has `scale_fit.village:
poor`. The client base for custom gates, railings, and bespoke architectural ironwork
does not exist at village scale — the contractor and high-end residential market requires
at minimum a town-scale population. This entry's village_market win is a formula artifact:
the market lens checks payback against capital, not against demand feasibility. Do not site
an architectural ironwork master shop in a village without documented regional contractor
demand.

**forge-012 — Farriery Specialist Propane** (capital mid $22,000; operator: journeyman
farrier; energy: propane 0.6 kg/hr; payback 0.31 yr)

Village scale is this design's primary habitat: `scale_fit.village: good`, `lens_fit.market:
good`. Farriery persisted because the service is physically location-bound — a structural
characteristic the historical record documents consistently [DECLINE-VERDICT §5]. At village
scale in a horse-keeping rural area, a mobile farrier serving a route of 80–120 horses
within a 30-mile radius is a self-sustaining single-operator practice. The 0.31-year
payback reflects the low capital ($22,000 for a mobile kit), recurring appointment-based
demand, and a price floor of $120–$185 per four-shoe set with no industrial substitute.
Seasonal demand variation is lower than other forge entries (worst month 0.7× average
vs. 0.45× for coal forges), making cash-flow management more predictable.

**forge-013 — Restoration Specialist Heritage Forge** (capital mid $75,000; operator:
master; energy: multi-fuel coal-propane-induction; payback 0.42 yr)

Wins village_market but has `scale_fit.village: poor`. Historic-preservation client base
requires proximity to heritage buildings, preservation societies, and state historic-
preservation office networks — concentrations found in larger settlements, not villages.
A restoration specialist operating from a rural village must rely on transportation of
removed elements and regional client relationships, which substantially raises logistics
cost. The market win is real but context-dependent; verify preservation project pipeline
before committing to this configuration at village scale.

**Summary of market winners at village scale:**

The two designs to build a village-scale program around are forge-005 (Frontier-Revival Coal
Repair, $22,000 capital, `scale_fit.village: good`) and forge-012 (Farriery Specialist
Propane, $22,000 capital, `scale_fit.village: good`). Both match the village demand structure.
Forge-002 (Induction Modular Repair, $42,000) is a defensible second choice where coal
permitting is problematic. The remaining four market winners (forge-006, forge-010, forge-013,
and forge-003) win on formula but face real demand-side constraints at village scale that the
Tier A simulation does not model.

---

## Cooperative lens — winning designs at village

Only forge-001 (Backyard Propane Compact, capital mid $3,500) and forge-014
(Electric-Induction Gig Repair Micro, capital mid $6,500) clear village_coop.

Both win for the same structural reason: their break-even member count is 15, which falls
below the village feasible pool of 31.2 members (SCALES.md §5 formula: 500–2,000 residents
× 2.5% participation rate = 13–50 members, midpoint ~31). Every other catalog entry has a
higher break-even — forge-005 requires 45 members, forge-003 requires 60, forge-006 requires
99, forge-013 requires 117, forge-004 requires 77 — all beyond what a village membership
pool can reach.

The cooperative win for forge-001 and forge-014 is narrow. These are part-time hobby-scale
designs, not full-production forges. Forge-001's market verdict is a fail (take-home $18,913
vs. village median $48,000); it cannot support a full-time operator. Forge-014 similarly
fails market on wage grounds. What the cooperative win means in practice: a village tool-
library that pools 15 members' dues to cover $2,830–$2,900/year in operating costs can
sustain shared access to a small induction forge for member use. This is a reasonable
community amenity — but it is not a smithing business.

Use the cooperative verdict honestly: forge-001 and forge-014 in cooperative mode are
skill-building and community-access platforms, not revenue-generating production forges.
If the goal is restoring local repair capacity, the market-primary designs (forge-005,
forge-012) are the correct instruments.

---

## Civic lens — winning designs at village

Forge-004 (Community Civic Makerspace) and forge-011 (Municipal Civic Training Forge)
both pass the village civic formula: forge-004 at $28.73/household/year against a $120
threshold (76% margin), forge-011 at $43.80/household/year against the same threshold.

However: both entries have `scale_fit.village: poor`. The formula passes; the qualitative
assessment does not. The civic diagnostic (CIVIC-LENS-DIAGNOSTIC §7) states this directly:

> "Civic forge math passes but village-scale civic forges face staffing viability risk
> that the formula does not capture."

The specific problems are:

**Forge-004** is a supervised multi-user makerspace requiring a full-time master smith-
instructor plus up to 4 concurrent members, capital $125,000, and a scheduling model
that requires 1,560 facility-hours per year across a 6-day operating week. At village
scale (400 households), the $125,000 capital amortization over 30 years plus operating
costs yields $28.73/hh/year — within threshold — but the supervisory staffing model
requires a full-time master smith whose wages ($68,000+) are difficult to justify
against a 400-household civic budget. A $28.73/hh/year levy on 400 households is
$11,500/year total — less than the master smith's salary alone.

**Forge-011** is a municipal CTE training forge designed for a school-adjacent institutional
context with 6 student stations, a 40-week academic year, and enrollment demand that
requires a town- or district-scale population to fill. At village scale, a 6-station
training forge cannot fill its class schedule from 500–2,000 residents. The diagnostic
notes forge-011 is "small_city-primary."

The honest village civic verdict: the formula wins are real but operationally fragile.
A village that genuinely wants civic forge access should look at forge-005 operated under
a part-time public-smith arrangement (county agricultural services or rural resilience
budget) rather than the full civic makerspace or CTE training model. That configuration
is not currently modeled as a civic entry, but the civic lens arithmetic for a
$22,000-capital forge-005 at $10.10/hh/year would pass the $120 village threshold with
substantial margin — and the staffing economics are achievable at a village scale.

---

## Implementation sketch — featured designs

### Design 1: Forge-005, Frontier-Revival Coal Repair Forge

**Context:** Rural village of 1,000 residents plus surrounding township (combined service
area ~2,500). No private smith within 30 miles. Agricultural community with active small-
farm and horse-keeping population.

**Pilot-year structure:**

- Months 1–2: Site selection. Identify light-industrial or agricultural-support zoning in the
  target township. Verify coal supplier within 50-mile radius; establish 4-week coal buffer
  inventory capacity. Secure building or bay lease ($3,600/year; ~$300/month for 32 m² rural
  light-industrial space). Obtain building permit for exhaust stack and forge installation.
- Months 3–4: Equipment order and installation. Coal forge hearth ($1,500–$4,000), anvil
  ($800–$2,500), blower motor, tooling set, chimney and extraction hood ($1,500–$3,500),
  coal bin and quench setup ($500–$1,500). Total installed $22,000–$25,500. Allow 6–8 weeks
  for stack fabrication and permit approval; do not plan production startup until the exhaust
  system passes inspection.
- Month 5: Operator hiring or confirmation. Journeyman smith with coal experience; regional
  search radius 100 miles. Wage $48,000/year (SCALES.md §3 village-scale skilled-trades
  median). If the founding operator is the journeyman (owner-operator model), salary is
  replaced by owner's draw — economic model changes but capital requirements do not.
- Month 6: Soft launch. Post repair intake form at feed store, farm bureau, and county
  extension office. First customers: local farmers needing plowshare repair and horse owners
  with shoeing needs. Target 10–15 repair tickets in month 6 to verify demand.
- Months 7–12: Production ramp. Build to 30–35 active forging hours per week by month 9.
  Accept informal apprentice by month 10 (Stage 1: fire management and basic safety).

**Staffing:**
- 1 full-time journeyman smith at $48,000/year
- 1 part-time apprentice (Stage 1–2) at $18,000–$24,000/year part-time equivalent; recruited
  locally from agricultural-community households or county vocational program

**Customer acquisition:**
- First 10 customers: county farm bureau referral list; horse owners who have been driving
  30+ miles for shoeing; welding-shop referrals for non-weldable repair jobs
- Next 10: word-of-mouth in the agricultural community; one targeted mailing to rural
  property owners within 10-mile radius; county extension office partner referral
- Year-2 goal: 80–120 recurring repair customers representing ~400–500 repair tickets/year

**Year-1 P&L sketch (order-of-magnitude):**

| Item | Amount |
|---|---|
| Revenue (2,430 units/yr × $50 mid-price × 0.50 year-1 ramp factor) | $60,750 |
| Variable costs ($1.25/unit × 1,215 units year-1) | $1,519 |
| Annual maintenance | $1,200 |
| Annual consumables (coal, flux, tooling) | $3,000 |
| Floor-space rent | $3,600 |
| Journeyman wage | $48,000 |
| Total operating cost | $57,319 |
| Year-1 net (pre-capital service) | +$3,431 |
| Capital ($22,000 over 25 yr = $880/yr amortized) | $880 |
| **Estimated year-1 net after amortization** | **+$2,551** |

Year-1 is breakeven-positive even on a ramp-up revenue assumption (50% of full-year
throughput). This is the key characteristic of low-capital repair smithing: the capital
charge is small relative to the labor cost, and the labor cost is covered by the repair-
premium pricing.

**Year-2 steady state:**
Full throughput of 2,430 units/year at $50/unit = $121,500 gross revenue. Operating costs
$57,319 plus capital amortization $880 = $58,199. Net: ~$63,300, which is the owner's
margin in an owner-operator model or split between wage floor and business profit in an
employed-operator model. This is a viable small business in a rural setting where no
competing repair option exists.

---

### Design 2: Forge-012, Farriery Specialist Propane (Mobile Route)

**Context:** Village of 800 residents in a horse-keeping rural area; 80–120 horses within
25-mile route radius (recreational riding, small-scale working ranch, 4-H programs).

**Pilot-year structure:**

- Months 1–3: Route development. Identify all horse-keeping operations within 25-mile radius
  using county agricultural census and equine-facility registrations. Establish a schedule of
  50–60 horses as the initial route. Secure used light truck and portable farriery kit
  ($15,000–$22,000 total).
- Month 4: AFA Certified Journeyman Farrier (CJF) credential confirmation (if not already
  held). Obtain equine-liability insurance (estimate $1,500–$2,500/year; required before
  first appointment). Register business with county.
- Months 5–12: Route operation. Target 8–10 horses per working day at 4–4.5 days/week.
  Billing at $150/four-shoe set for standard keg-shoe work; $200–$250 for corrective or
  performance-horse work. Seasonal demand — spring and fall are peak; winter requires route
  maintenance via trimming appointments at lower billing.

**Staffing:**
- 1 journeyman farrier (owner-operator typical)
- 1 apprentice by year 2 (rides the route, handles trimming and prep; formal CJF pathway
  starts from day 1 with riding-the-route model per farriery apprenticeship tradition)

**Customer acquisition:**
- First 10 horses: county agricultural extension referral; feed store bulletin board; 4-H
  program coordinator contact
- Next 10–20: referral from first clients (farriery is heavily word-of-mouth in horse
  communities); one appearance at local equine event or 4-H show

**Year-1 P&L sketch:**

| Item | Amount |
|---|---|
| Revenue (550 shoeing sets/yr × $185 mid-price × 0.70 year-1 ramp) | $71,225 |
| Variable consumables (shoes, rasps, propane) | $4,200 |
| Annual maintenance and vehicle | $1,500 |
| Floor-space rent (minimal: home-based tool storage) | $1,800 |
| Operator draw (owner-operator; no separate wage line) | — |
| **Year-1 gross margin before operator draw** | **$63,725** |
| Capital ($22,000 over 20 yr = $1,100/yr) | $1,100 |
| **Year-1 net after amortization** | **$62,625** |

This margin funds the operator draw at a viable level for a rural village context. Farriery's
low capital cost and high per-unit price ($185 vs. $50 for general repair work) produce
the best revenue-per-capital-dollar of any village-scale smithing design in the catalog.

**Year-2 steady state:**
Full route of 550 sets/year at $185 = $101,750 gross. Operating costs $7,500 plus amortization
$1,100 = $8,600. Operator draw: ~$93,150 (owner-operator model). This is above the village-
scale skilled-trades median; a mature farriery route at village scale with appropriate
horse-population density is financially attractive relative to the capital requirement.

---

## Capital ask

For a village planning to initiate or support local smithing capacity, the realistic capital
envelope is:

| Design | Capital (mid) | Install | Operating reserve (6 mo) | Total ask |
|---|---|---|---|---|
| Forge-005 (coal repair) | $22,000 | $3,500 | $14,400 | $39,900 |
| Forge-012 (farriery) | $22,000 | $2,000 | $3,750 | $27,750 |
| **Combined (both designs)** | **$44,000** | **$5,500** | **$18,150** | **$67,650** |

The $67,650 combined ask funds one general repair smith and one farrier serving the same
rural service area of 2,500–3,000 people. This doubles the coverage: the repair smith
handles agricultural equipment, bespoke hardware, and structural metalwork; the farrier
covers equine demand. The two practices do not compete; they serve different client segments
and can share a customer referral relationship.

Operating reserve is estimated at 6 months of operating costs: for forge-005, $57,319/yr
÷ 2 = $28,660, discounted to $14,400 excluding operator wage (which would be covered by
early revenue); for forge-012, $7,500/yr ÷ 2 = $3,750.

A village choosing only one design should choose based on local demand:
- Horse-keeping community with documented equine population: forge-012 first.
- Agricultural community with implement-repair gap and no horses: forge-005 first.
- Both demand types present: combined ask.

---

## Open risks at village scale

**Demand thinness.** A village of 500–2,000 residents generates thin and irregular repair
demand. Forge-005 at full throughput (2,430 units/year) implies roughly 7 repair jobs per
working day across a service area of ~2,500 people. That rate is achievable only if the
smith draws customers from surrounding rural townships, not from the village population
alone. Verify the service-area population, not just the village population, before
committing to a full-time operation. A smith who serves only 1,000 residents will not
fill a 35-hour work week.

**Apprentice pipeline.** A village of 500–2,000 has a thin pool of candidates willing to
undertake a 36-month informal apprenticeship at market wages. The frontier-revival model
(working alongside, not a classroom program) is the correct form for this scale — but even
informal apprenticeship requires one willing candidate per 3-year cycle. If no candidate
emerges from the first cycle, succession planning is unresolved. Plan for this explicitly
at founding: name the apprenticeship intake process and the wage structure before the
forge opens.

**Supply chain.** Coal availability is declining in rural US markets as local fuel dealers
close. Verify a coal source within 50 miles before committing to a coal-primary design.
Worst-case consumables lead time for forge-005 is 21 days; maintain a 4-week coal buffer.
Rural propane supply is more reliable but single-supplier dependency is common; maintain
a spare 100-lb tank. For farriery (forge-012), keg-shoe blank supply from regional farrier
distributors is generally reliable but specialty orthopedic shoes may require 7–14 day
lead times; carry a 4–6 week stock of the most common shoe sizes.

**Seasonality.** At village scale, seasonal demand variation is severe. Forge-005's worst
month is estimated at 50% of average; an agricultural repair forge in a village will see
near-zero activity in mid-winter and peak demand in March–April (pre-planting) and
October (post-harvest). Cash-flow management across a 2:1 seasonal swing requires a
working-capital buffer of at least 60 days of operating costs. Farriery (forge-012) has
a shallower seasonal curve (worst month 0.7× average) because horse care is year-round;
this is an argument for the combined design: the farrier's steadier income smooths the
combined practice's seasonal cash-flow risk.

**Operator retention.** A single-operator forge in a rural village has no succession if
the operator leaves. The journeyman hired for forge-005 may be recruited away by a
higher-paying urban or suburban repair shop after 2–3 years. Retention strategies include
owner-operator structure (operator has equity in the forge), below-market rent in exchange
for local-service commitment, and county or municipal operating subsidy contingent on
staying in the service area. These mechanisms are not modeled in the simulation; they are
soft factors that must be addressed in the operating agreement before launch.

---

## Scale-appropriate framing

Village smithing is feasible in specific cases. The two designs with genuine village-scale
fit (forge-005 and forge-012) are both repair-dominant, low-capital, single-operator
practices targeting demand that is inherently location-bound — you cannot ship a broken
plow or a horse's feet to a factory. DECLINE-VERDICT §5 identifies exactly this segment
as "most plausibly restorable via equipment redesign": repair and maintenance work that is
geographically bound and judgment-intensive.

The limits are equally clear. Thirteen of fifteen catalog entries either fail village_market
outright or win on formula while carrying `scale_fit.village: poor` flags. Cooperative
governance fails at village scale because the member pool is too thin to reach break-even
for any but the smallest hobby-scale designs. Civic governance passes the cost formula but
runs into staffing economics that the formula does not capture: a village of 400 households
cannot afford a full-time master smith-instructor without substantial external subsidy.

The correct framing for a village planning committee: assess whether you have documented
repair demand and either a horse population or an agricultural implement base. If yes,
forge-005 or forge-012 (or both) are financially viable with modest capital investment and
no ongoing subsidy. If the documented demand is not there, a village-scale forge will not
generate it — and the capital should stay in the budget. Most village designs in this catalog
need town-scale population (2,000–15,000) to clear all three lenses. The village niche is
real but narrow.

---

## Sources

- `simulations/tier-a-comparator/results/SUMMARY.md` — matrix verdicts for all 15 entries
  at village_market, village_coop, and village_civic cells
- `simulations/tier-a-comparator/results/CIVIC-LENS-DIAGNOSTIC.md` — diagnosis of civic
  wins for forge-004 and forge-011; village scale qualitative override
- `catalog/smithing/entries/005-frontier-revival-coal-repair.md` — forge-005 sim_params,
  economics, scale_fit, and lens_context blocks
- `catalog/smithing/entries/012-farriery-specialist-propane.md` — forge-012 sim_params,
  economics, and scale_fit
- `catalog/smithing/entries/002-induction-modular-small-repair.md` — forge-002 results block
- `catalog/smithing/entries/003-shared-toollibrary-coal.md` — forge-003 results block
- `catalog/smithing/entries/006-induction-bladesmith.md` — forge-006 scale_fit and results
- `catalog/smithing/entries/010-architectural-ironwork-bespoke.md` — forge-010 scale_fit
  and results
- `catalog/smithing/entries/013-restoration-specialist-heritage.md` — forge-013 scale_fit
  and results
- `catalog/smithing/entries/001-backyard-propane-compact.md` — forge-001 village_coop win;
  wage-fail note
- `catalog/smithing/entries/014-electric-induction-gig-repair.md` — forge-014 village_coop
  win; wage-fail note
- `catalog/smithing/entries/004-community-civic-makerspace.md` — forge-004 village_civic
  win; scale_fit.village: poor
- `catalog/smithing/entries/011-municipal-civic-training.md` — forge-011 village_civic win;
  scale_fit.village: poor
- `research/trades/smithing/DECLINE-VERDICT.md §5` — repair and specialty as restorable
  categories; commodity hardware and industrial-tool manufacturing as non-restorable
- `corpus/program/SCALES.md §3, §4, §5` — village-scale wage medians ($48,000/yr),
  civic cost threshold ($120/hh/yr), cooperative member-pool formula (2.5% of population)
