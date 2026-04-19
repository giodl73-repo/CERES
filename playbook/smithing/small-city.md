---
trade: smithing
scale: small_city
population_range: 15000-75000
doc_type: playbook
derived_from:
  - simulations/tier-a-comparator/results/SUMMARY.md
  - simulations/tier-a-comparator/results/CIVIC-LENS-DIAGNOSTIC.md
  - catalog/smithing/entries/*.md
  - research/trades/smithing/DECLINE-VERDICT.md
  - specs/2026-04-18-ceres-design.md §9
version: "1.0"
status: draft
---

# Small-City Smithing Playbook

**Scale:** 15,000–75,000 residents (population midpoint used in simulation: 45,000)
**Household count used in simulation:** 18,000 (at 2.5 persons/household)

Small-city scale is the richest context in the catalog. All three economic paths —
market, cooperative, and civic — produce viable designs here. This is not the case
at village or town scale. The playbook presents each path with its winning entries,
implementation sketch, and constraints.

---

## Matrix at Small-City Scale

| Lens | Winners | Fails | Notes |
|---|---|---|---|
| market | 7 of 15 | 8 | Same 7 as every scale; market viability is capital-driven, not population-driven |
| cooperative | 15 of 15 | 0 | Every entry clears; feasible pool 900 members vs break-even 77–134 |
| civic | 2 of 15 | 13 | forge-004 ($0.80/hh/yr) and forge-011 ($1.22/hh/yr); 13 non-civic designs fail correctly |

**Total: 24 wins across 45 cells.** No other scale achieves this. Town produces 24 wins
on the same arithmetic (7 + 15 + 2), but small-city civic wins more convincingly on
the per-household cost metric, and specialty market designs (forge-006, forge-010,
forge-013) have their primary scale_fit here rather than at town.

---

## Lens 1: Market

### Winning designs

Seven entries clear the market lens at small-city scale. All seven also win at village
and town — market viability tracks capital cost and revenue model, not population.
The small-city distinction is that three specialty designs with `scale_fit.small_city: good`
find their most favorable operating context here.

| Entry | Name | Capital (mid) | Payback (yrs) | Notes |
|---|---|---|---|---|
| forge-002 | Induction-Modular Small Repair | $42,000 | 0.67 | Repair-dominant; lowest specialty capital |
| forge-003 | Shared Tool-Library Coal Forge | $28,000 | 0.88 | Coop-eligible too; lowest capital among coal designs |
| forge-005 | Frontier-Revival Coal Repair Forge | $22,000 | 0.35 | Fastest payback in the catalog |
| forge-006 | Induction Bladesmith | $70,000 | 0.67 | Specialty-primary; small-city is the target scale |
| forge-010 | Architectural Ironwork Bespoke | $95,000 | 0.88 | Custom gates/railings; contractor market requires small-city density |
| forge-012 | Farriery Specialist Propane | $22,000 | 0.88 | Mobile-capable; serves regional farriery demand |
| forge-013 | Restoration Heritage Forge | $75,000 | 0.42 | Heritage-district and contractor client base; small-city-primary |

The payback calculation is scale-invariant; all seven win at village and town too. What
changes at small-city is qualitative: the client base for forge-006, forge-010, and
forge-013 is thin at village and marginal at town, but sufficient here. The simulation
captures cost economics; market depth for specialty designs requires the client-base
argument the matrix alone cannot provide.

**Failing designs (8 of 15):** forge-001, forge-004, forge-007, forge-008, forge-009,
forge-011, forge-014, forge-015. These fail for structural reasons (low throughput,
training-primary purpose, negative gross margin) that do not reverse at any scale.

### Small-city specialty emphasis

Three designs are small-city-primary: their demand base requires a population large
enough to support commission-based work.

**forge-006 — Induction Bladesmith.** Custom kitchen and outdoor blades at $200–$800
direct-to-consumer. Capital $70,000 mid; payback 0.67 years. `scale_fit.village: poor`
because the commission pipeline is thin at 500–2,000 residents. Small-city supports a
sustainable commission base. Single master operator; 80% specialty product mix.

**forge-010 — Architectural Ironwork Bespoke.** Custom gates, railings, and structural
ironwork for contractors and residential clients. Capital $95,000 mid; payback 0.88 years.
The contractor market exists in meaningful volume at small-city scale; `scale_fit.town:
marginal` because the commission pipeline is thinner there. Highest capital ask among the
7 market winners; requires a deliberate capitalization path.

**forge-013 — Restoration Heritage Forge.** Multi-fuel specialist serving historic-building
restoration and architectural-hardware repair. Capital $75,000 mid; payback 0.42 years —
second-fastest in the market-win group. Small-city is appropriate: large enough to have
heritage-district stock worth preserving and a contractor ecosystem capable of commissioning
custom restoration work. `scale_fit.small_city: good`.

---

## Lens 2: Cooperative

### All 15 entries clear

At small-city scale (45,000 residents), the feasible member pool is approximately 900
members (2% participation rate of 45,000 midpoint population). Every entry's
break-even member count falls below 900.

| Entry range | Break-even members | Feasible pool | Margin |
|---|---|---|---|
| Lowest (forge-004, forge-011) | 77–117 | 900 | 87–89% margin |
| Highest (forge-009) | 124 | 900 | 86% margin |

The cooperative lens does not differentiate entries at small-city scale — all 15 pass
with abundant margin. Differentiation among coop designs should be made on the basis
of governance model, capital requirements, and operational fit, not on whether they
can reach break-even.

### Cooperative richness

Member pool 900 feasible vs 31 at village, 213 at town. Even the highest-capital
cooperative design (forge-009, break-even 124) clears with 87% margin. Hiring is
easier: the $62,000/yr instructor stipend is supportable where the member-fee revenue
base is larger. A small city could support a general-purpose forge cooperative and a
specialty training cooperative simultaneously; the niches do not overlap.

### Featured cooperative design: forge-009 — Co-op Apprentice Training Forge

forge-009 is the catalog's cooperative-primary training design. At small-city it
operates at its most favorable parameters: capital $130,000 mid (coal-induction hybrid
floor for 4–8 concurrent apprentices); break-even 124 members against a 900-member
feasible pool; $62,000/yr instructor stipend (SCALES.md §3 small-city median) supportable
where the member-fee base is large enough; output 2–4 journeyman-certified smiths per
36-month cohort cycle.

The cooperative is not a commercial shop; its market lens fails correctly. The viability
case rests on member dues ($12,000–$18,000/yr from 30+ members), ancillary craft-fair
sales (estimated $10,000–$20,000/yr), and workforce-development grants at launch.
The revenue gap versus instructor cost ($62,000/yr stipend alone) is real; grant
dependency at launch is a named risk, not a design flaw. forge-009 is where the
journeyman pipeline is built: the market-lens specialty winners (forge-006, forge-010,
forge-013) depend on master-level operators, and forge-009 produces them.

---

## Lens 3: Civic

### Two designs win

The post-diagnostic civic results (CIVIC-LENS-DIAGNOSTIC, Path A) show forge-004 and
forge-011 as the two civic wins at every scale. At small-city, both clear with the
largest margin in the catalog.

| Entry | Name | per-hh cost | Threshold | Margin |
|---|---|---|---|---|
| forge-004 | Community Civic Makerspace | $0.80/hh/yr | $80/hh/yr | 99% |
| forge-011 | Municipal Civic Training Forge | $1.22/hh/yr | $80/hh/yr | 98% |

The 13 failing entries fail the civic lens correctly: they are market or
cooperative-primary designs with no public-access mode. The civic lens does not apply
to them.

### Why civic wins here most convincingly

At small-city scale, the per-household cost is overwhelming: forge-011 at $1.22/hh/yr
against an $80 threshold. The $200,000 fixed cost spread across 18,000 households
produces the lowest per-household cost in the matrix. Utilization clears: 0.178 hr/capita
at 45,000 residents against the 0.15 specialized-equipment threshold (ECONOMIC-LENSES.md
§4.3). The 0.15 threshold reflects the physical constraint of a single forge with
concurrent users; the 2.0 default applies to high-traffic open-access facilities
(libraries, recreation centers) and is physically unachievable for any single-forge
civic operation.

### Featured civic design: forge-011 — Municipal Civic Training Forge

forge-011 is the catalog's school-district-owned CTE forge. It is designed for
small-city scale.

- **Capital:** $120,000–$280,000 (mid $200,000). School-shop fitout for 4–6 induction
  stations with instructor demonstration bay.
- **per-hh cost:** $1.22/hh/yr at small-city. $6.44/hh/yr at town (still under the
  $100 town threshold, but the town-scale calculation reflects the smaller household
  divisor). Small-city is the canonical operating scale.
- **Energy source:** induction-electric only. No coal or propane. The regulatory and
  safety profile for a school shop with combustion fuel is substantially more complex;
  induction is the correct choice for a CTE facility.
- **Governance:** school-district ownership. The operator is an instructor-cooperative
  contracting with the district, or a district-employed CTE instructor. Municipal
  governance authority rests with the school board, not a separate civic body.
- **Civic verdict:** win at small-city (hrs/capita 0.178 vs threshold 0.15; per_hh
  $1.22 vs threshold $80).

**The civic-private complementarity argument.** forge-011 feeds workers into the private
market; it does not compete with private shops. The CTE forge produces students who may
go on to work at forge-006, forge-010, or forge-013 operations in the same community.
The school-district ownership structure means the forge has no commercial revenue motive;
it takes no commission work that would displace a private operator. Municipal decision-
makers should be told this explicitly: the argument for funding forge-011 is that it
builds the skilled-trades pipeline that makes private-shop viability possible. A private
bladesmith or architectural ironsmith cannot sustain a formal apprenticeship program
alone; the CTE forge does it at public cost and lower per-student cost than comparable
community-college CTE programs.

forge-004 (Community Civic Makerspace, $0.80/hh/yr) is the alternative civic winner.
Where forge-011 is school-integrated and CTE-oriented, forge-004 is open to adult
hobbyists, small-batch producers, and repair users on a library-access model. Both
are viable; the choice depends on whether the municipality wants a school-integrated
apprenticeship pipeline or a broader community-access workshop.

---

## Implementation Sketches

### Sketch A: Market-primary — forge-010 Architectural Ironwork Bespoke

**Context:** A small city with a visible heritage district, active residential
construction, or access to a regional contractor market for custom metalwork.

**Setup:** Capital $60,000–$150,000 (mid $95,000). Propane forge system, induction
heat-treatment station, belt-grinder bank, and 65 m² light-industrial space with
dedicated exhaust. Ceiling minimum 4.5 m. Light-industrial zoning required; confirm
propane permitting before lease. Operator: 1 master smith — the quality level that
sustains $200–$800+ commission pricing requires master skill; a journeyman cannot
produce it.

**Revenue model:** Commission-based. Lead times 8–14 weeks on large gate work; shorter
for hardware and railings. Target 2–3 contractor relationships and 1–2 residential
referral clients before opening. Do not plan for steady-state revenue until month 9–12.
Payback 0.88 years once the pipeline is active; budget 12 months of operating costs
before expecting breakeven. Year 2: hire 1 helper for grinding and finishing; the
master smith concentrates on forge decisions and client management.

**Open risks:** Contractor relationships are the single largest variable. Launch without
at least one committed contractor project is high-risk. Capital at $95,000 requires
deliberate financing — owner equity, SBA loan, or member capital; do not assume grants
for a market-primary design.

---

### Sketch B: Cooperative-primary — forge-009 Co-op Apprentice Training Forge

**Context:** A small city that wants to build a regional smithing workforce and has a
community of 30+ people willing to pay $400–$600/year to support the mission.

**Setup:** Capital $80,000–$180,000 (mid $130,000). Founding capital from 30 member
subscriptions ($18,000 minimum) plus a workforce-development grant application
($15,000–$50,000 targeted). Register as a worker-cooperative corporation before taking
dues or paying an instructor. State apprenticeship-authority registration required before
paying apprentice stipends. Hire the master instructor as a worker-member before first
cohort intake; $62,000/yr stipend is the floor — below this, qualified candidates will
not accept. Budget journeyman-assistant coverage (1 part-time, $18,000–$22,000/yr)
from year 1. First cohort: 4–6 apprentices on the four-stage training path (0–42 months
to journeyman standard).

**Financial arc:** Revenue target is 40–50 paid members by end of year 2 ($20,000–$25,000
dues/yr) plus ancillary craft-fair sales. Operating costs are $72,000–$82,000/yr total;
the gap requires grants during the launch phase. The cooperative is not self-sustaining
in years 1–2. Year 3 primary deliverable: 2–4 journeyman-certified graduates.

**Open risks:** The master instructor is the single critical point of failure. If they
depart before the journeyman-assistant pipeline is established, the cooperative may not
survive. Mitigate structurally: federate with at least one peer cooperative in the region
for emergency instructor-sharing before first cohort. Grant-dependency through year 3 is
a structural risk; a cooperative that cannot transition to dues-dominant financing by
year 4 is fragile.

---

### Sketch C: Civic-primary — forge-011 Municipal Civic Training Forge (CTE / school partnership)

**Context:** A small city with a K–12 district or community college willing to host a
CTE metalworking program, and a school board that can authorize $120,000–$280,000
in capital investment.

**Political groundwork (year 0):** The school board votes on capital expenditure —
this is the entry's critical political gate. Prepare two arguments: (1) the fiscal-cost
case ($1.22/hh/yr against an $80 threshold; less than $1.50/household/year); and (2)
the workforce-development case (the forge produces graduates who feed private-market
operators the city cannot otherwise staff). Identify the instructor before the vote —
school boards approve facilities more readily when a qualified instructor is already
committed. Build the coalition: school board, workforce-development board, private
smiths or metal-trade employers in the region (net beneficiaries, not competitors),
and any trades unions with interest in skilled-trades development.

**Construction and first class (year 1):** Capital $120,000–$280,000 (mid $200,000)
for school-shop fitout: 4–6 induction stations, instructor demonstration bay, dedicated
exhaust, 100 m² within the school facility. Induction-electric only — no coal or propane.
The induction-only choice is deliberate: it reduces school-facility permitting to its
minimum and eliminates combustion-safety complexity. Forge welding is not a CTE
entry-level curriculum objective; the capability limitation is acceptable. First class:
6 students per period, 2–3 periods per day. Person-hours: 25 hr/wk × 40 weeks × 8
concurrent = 8,000/yr → 0.178 hr/capita at 45,000 residents, above the 0.15 threshold.

**Steady state (year 2+):** The civic forge does not accept commercial contracts. After
year 2, establish a formal referral relationship with any private smiths in the area:
the school refers commercial inquiries outward; private operators offer job-shadow
opportunities to graduates. This makes the forge-011 → forge-006/010/013 pipeline
visible to both institutions.

**Open risks:** School-board authorization is the first and highest-stakes gate. The
instructor hiring pool is thin — plan 6–9 months of recruiting before opening. Budget
separately for liability insurance; a school-operated hot-work shop carries higher
premiums than a commercial shop, and this cost is not in the per-household-cost figure.

---

## Capital Ask

| Path | Design | Capital range | Notes |
|---|---|---|---|
| Market: entry-level | forge-005 or forge-012 | $15,000–$35,000 | Fastest payback; lowest barrier |
| Market: specialty | forge-006 or forge-013 | $40,000–$100,000 | Small-city-primary designs |
| Market: high-capital specialty | forge-010 | $60,000–$150,000 | Highest capital; requires contractor-client commitment |
| Cooperative: training | forge-009 | $80,000–$180,000 | Member-dues + grant launch |
| Civic: CTE forge | forge-011 | $120,000–$280,000 | School-district capital vote required |

**Range across all viable small-city paths: $50,000–$300,000.**

Small-city supports larger facilities than village or town. The upper bound ($280,000
for forge-011) reflects a school-district capital project, not a private commercial
investment. Market-path operators should plan for $50,000–$100,000 for specialty designs.
Cooperative founding should target $130,000 mid for a full-featured training floor.

Grant eligibility varies by path. Market designs are not grant-eligible by default —
they are private enterprises. Cooperative designs may qualify for worker-cooperative
development grants and workforce-development funding if registered with the state
apprenticeship authority. Civic designs (forge-011) qualify for CTE capital grants
and school-construction bonding, subject to state CTE funding formulas.

---

## Open Risks

### Zoning complexity

Light-industrial zoning is required for all market-path designs. Small-city light-
industrial zones are often limited in area and may have waiting lists or lease
premiums compared to town scale. Coal combustion adds an air-quality permit
requirement in many jurisdictions that eliminates some otherwise suitable zones.
forge-013 (multi-fuel: coal, propane, induction) has the most complex zoning and
permitting profile of any market-win entry. forge-006 (induction-primary with propane
alcove) and forge-010 (propane-primary with induction secondary) are simpler but
still require dedicated exhaust and light-industrial classification.

Before signing a lease: confirm local hot-work ordinance classification, verify
coal or propane permitting requirements with the fire marshal, and check that the
ceiling height meets the minimum for the selected design (3.0 m for forge-006;
4.5 m for forge-010; 4.0 m for forge-013).

### Labor market competition

Small-city alternative wages are higher than at village or town scale. A master
smith considering an operator position at a small-city forge competes against
manufacturing, construction, and industrial-trade wages in the same labor market.
The operator wage assumption in the simulation is $62,000/yr (SCALES.md §3
small-city skilled-trades median). Below this, qualified operators will choose
alternatives. Designs that assume operator wages below this threshold will not
attract and retain qualified staff.

This is distinct from the village or town constraint, where the wage threshold is
lower ($48,000 and $56,000 respectively) and alternative-wage competition is less
intense. Small-city operators cost more; budget accordingly.

### Multiple-shop market dynamics

Small-city could support 2–3 concurrent market-path operations without saturating
demand — but only with niche differentiation. Two repair shops targeting the same
client base will undercut each other's margins; a farriery specialist and an
architectural-ironwork shop serving different clients can coexist. The matrix shows
7 viable designs across all small cities; in any specific small city, 1–2 market-path
shops is the realistic ceiling before competition erodes margins.

### Civic-private competition tension

forge-011 takes no commercial contracts and produces student credentials, not commercial
product. When a private-shop operator raises a competition objection during school-board
approval, the response is: the civic forge has a structural governance constraint against
commercial activity (school-district ownership), and its output feeds the private labor
market. Private operators gain access to a trained graduate pool they cannot generate
alone. Position private smiths in the region as coalition members in the approval
process, not as opponents. The competition objection conflates a CTE program with a
competing business; they are categorically different.

---

## Scale Framing

Small-city is the only scale where all three economic paths produce viable designs
simultaneously. At village scale, the cooperative lens is nearly closed (2 of 15
clear) and civic staffing risks outweigh the cost math. At town scale, all three paths
open but specialty market designs (forge-006, forge-010, forge-013) are marginal on
client-base depth. At small-city, the design space is fully open: specialty market
designs find their best operating context, cooperative training is financially supported
by a 900-member feasible pool, and civic investment clears the per-household threshold
with margins above 98%.

All three paths coexisting in the same small city is plausible but not automatic.
They require different governance structures, capital sources, and political coalitions.
The coordination relationships that add value — forge-011 feeding workers to forge-006
or forge-010, forge-009 graduates staffing or founding specialty shops — do not
self-organize. A community that wants to realize all three paths simultaneously needs
to manage those interfaces actively.

The DECLINE-VERDICT finding (mixed: repair and specialty niches persist; commodity
smithing does not) applies here as at every scale. All 7 market-win designs target
repair, specialty, or custom niches. Any operator who targets commodity hardware
production is entering a market segment industrial production dominates on price,
consistency, and availability. Small-city scale does not change that finding.

---

## Sources

- `simulations/tier-a-comparator/results/SUMMARY.md` — matrix aggregate, per-entry verdicts
- `simulations/tier-a-comparator/results/CIVIC-LENS-DIAGNOSTIC.md` — civic all-fail diagnosis, Path A fix, per-household cost table; IMLS Public Library Survey FY 2021 benchmark
- `catalog/smithing/entries/006-induction-bladesmith.md` — forge-006 capital, payback, scale_fit
- `catalog/smithing/entries/009-coop-apprentice-training.md` — forge-009 capital, break-even, feasible pool, instructor stipend
- `catalog/smithing/entries/010-architectural-ironwork-bespoke.md` — forge-010 capital, payback, scale_fit
- `catalog/smithing/entries/011-municipal-civic-training.md` — forge-011 capital, per_hh_cost, hrs/capita, scale_fit
- `catalog/smithing/entries/013-restoration-specialist-heritage.md` — forge-013 capital, payback, scale_fit
- `research/trades/smithing/DECLINE-VERDICT.md` — mixed verdict; repair/specialty persist; commodity does not
- `corpus/program/ECONOMIC-LENSES.md §4.3` — specialized-equipment exception (0.15 hr/capita threshold)
- `corpus/program/SCALES.md §3` — small-city median wage ($62,000/yr); household divisor
