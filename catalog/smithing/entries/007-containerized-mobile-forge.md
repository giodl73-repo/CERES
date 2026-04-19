---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: forge-007
trade: smithing
name: "Containerized Mobile Forge (20-ft intermodal, route-service)"
tagline: "Propane-fired forge in a converted intermodal container; goes to the client rather than waiting for one"
status: draft
version: 0.1
supersedes: null
inspirations: [19th-century-traveling-smith-circuit, modern-mobile-farrier-trade]

# ── PHYSICAL ENVELOPE ─────────────────────────────────────────────────────────

footprint_m2: 15
ceiling_min_m: 2.4
ventilation: mechanical-extraction-required

# ── ENERGY ────────────────────────────────────────────────────────────────────

energy_source: hybrid-induction-gas
energy_consumption_per_active_hour: "0.7 kg propane (primary, all sites) + 6–10 kWh induction (shore-power only)"
backup_fuel: null

# ── THROUGHPUT ────────────────────────────────────────────────────────────────

throughput:
  units_per_hour: { small_work: 3, medium_work: 0.8, large_work: 0.2 }
  max_active_hours_per_week: 25
  product_mix:
    repair: 85
    commodity: 0
    specialty: 10
    artistic: 5
  throughput_variance:
    seasonal: "Winter trough — weather limits rural-route travel and outdoor client-site work; spring pre-planting and fall harvest-prep are the primary demand peaks."
    worst_month_fraction_of_average: 0.4
    best_month_fraction_of_average: 1.7

# ── OPERATOR PROFILE ──────────────────────────────────────────────────────────

operator_skill_floor: journeyman
operators_concurrent: "1"
apprentice_friendly: false

# ── ECONOMICS ─────────────────────────────────────────────────────────────────

economics:
  currency: USD
  capital_cost: { low: 35000, mid: 55000, high: 80000 }
  install_cost: 4000
  annual_maintenance: 3200
  annual_consumables: 3800
  floor_space_rent_per_year: 0
  market_price_per_unit: { low: 55, mid: 75, high: 120 }
  industrial_baseline_price: 10
  pricing_notes: "Unit is one medium-work-equivalent repair or fabrication task. Industrial baseline ($10/unit) reflects factory-produced replacement hardware available by mail order or farm-supply channel. The mobile premium over that baseline reflects two compounding factors: (1) location-bound demand — the client cannot easily transport a broken plow shaft, fence post driver, or wagon running gear to a stationary shop, and (2) the service-at-site convenience value — the smith comes to the farm on the day needed, eliminating client transport cost and downtime. Customer segment: small farms, ranches, and homesteads on a rural route where no stationary smith is accessible within a practical drive. Pricing analogy: mobile-farrier and equine-farrier service rates, which carry a similar on-site premium over equivalent stationary-shop work and have persisted at premium levels in thin rural markets. [CITATION-NEEDED: direct survey of mobile-farrier and equine-farrier service rates as comparable-service analog; pricing is inferred, not sourced from a smithing-specific rate survey.]"
  pricing_validation: "Inferred from structural analogy to mobile-farrier and equine-farrier service pricing in rural US markets, where a location-bound service premium over stationary-shop rates is documented by trade association rate surveys and practitioner reporting. No direct smithing repair-pricing survey for mobile operations was identified in sources consulted. Evidence type: comparable-service structural inference; not a cost-plus residual and not a direct market data citation. A direct survey of operating mobile smiths or farriers-as-metalwork-proxies would be required before promotion to reviewed."

# ── OPERATIONS REALITY ────────────────────────────────────────────────────────

operations_reality:
  first_year_failures:
    - item: "Propane regulator (diaphragm wear or freeze-up in cold weather)"
      estimated_hours_to_failure: 1500
      replacement_cost: 150
      replacement_lead_time_days: 5
      serviceable_by: operator
    - item: "Container ventilation blower (motor bearing failure)"
      estimated_hours_to_failure: 1800
      replacement_cost: 300
      replacement_lead_time_days: 7
      serviceable_by: operator
    - item: "Truck / vehicle mechanical (annual budget item; actual mode varies by vehicle age)"
      estimated_hours_to_failure: 2000
      replacement_cost: 2000
      replacement_lead_time_days: 14
      serviceable_by: specialist

  maintenance_schedule:
    daily:
      task: "Post-route cleanup: sweep container floor, inspect propane fittings and hose for wear, secure all tooling and stock for transit, check vehicle tire pressure and lights before departure"
      performed_by: operator
    weekly:
      task: "Full vehicle inspection (fluids, brakes, trailer hitch/coupling if applicable), inspect container door seals and locking hardware, clean ventilation blower screen, check propane tank level and manifold connections"
      performed_by: operator
    monthly:
      task: "Forge calibration check (burner output and flame pattern), inspect and clean ventilation duct interior, inspect container floor and wall panels for corrosion or fastener loosening, check induction unit (if equipped) for cable and coil condition"
      performed_by: operator
    quarterly:
      task: "Propane regulator test and pressure-drop check, full ventilation system cleaning (blower housing, duct, exterior exhaust cap), vehicle service interval check, inspect propane hose for cracking or UV degradation"
      performed_by: operator
    annual:
      task: "Full vehicle service (oil, filters, belts, brakes, DOT commercial inspection), complete forge equipment service (burner rebuild or replacement if indicated, refractory inspection), propane tank recertification check, container structural inspection for corrosion and weld fatigue"
      performed_by: specialist

  startup_shutdown_overhead_per_day_min: 60
  max_active_hours_realism_note: "25 hr/wk is stated as the gross ceiling for active forging time on a route week. Travel time between client sites, site setup (unfolding working area, extending propane lines, positioning anvil), and teardown/load-out are the dominant overhead items and are NOT included in the 25-hr forging ceiling — they eat the remaining ~15–20 hrs of a nominal 40-hr work week. The 60 min/day startup-shutdown overhead covers client-site setup and teardown split across route stops; for a 5-day route week this subtracts 5 hr/wk from the 25-hr ceiling, yielding a net ~20 hr/wk of active forging. sim_params uses the derated net figure (20 hr/wk) for throughput calculation. The 25 hr/wk ceiling is the gross forging maximum; effective annual production hours are lower."
  interruption_notes: "Client-site interruptions are higher than stationary-shop equivalents: client consultation at each stop (~20 min/site), unplanned repair scope discovery (client presents additional broken items), and travel delays from weather or road conditions. These are folded into the reduced max_active_hours ceiling and the elevated downtime_fraction; they are not separately itemised."
  consumables_lead_time_days: { typical: 3, worst: 14 }
  throughput_variance:
    seasonal: "Winter trough — weather limits rural-route travel and outdoor client-site work; spring pre-planting and fall harvest-prep are the primary demand peaks."
    worst_month_fraction_of_average: 0.4
    best_month_fraction_of_average: 1.7
  operator_impact:
    noise_db: 80
    heat_exposure: "Moderate inside container; propane forge has lower radiant heat than coal, but the enclosed 15 m² container concentrates heat in summer; ventilation blower is essential for habitability above 25°C ambient"
    emissions: "Propane combustion: CO and combustion products only; no particulate or SOx; mechanical ventilation exhausts combustion gases outside the container; vehicle diesel exhaust is a separate transit-mode emission, not an on-site forge emission"
    physical_demand: "High overall: sustained driving (fatigue), repeated loading and unloading of equipment and stock at each site, smithing work on anvil, and lifting steel in constrained container space; physically more demanding than a stationary shop due to the transit and setup/teardown cycle"

# ── REGULATORY NOTES ──────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Mobile operation has no fixed-site zoning requirement; home-base parking for the container requires residential or light-industrial tolerance for a commercial vehicle; client-site work on private agricultural land typically does not trigger separate zoning review"
  emissions: "Propane forge emissions (CO, combustion products) are well below typical permit thresholds for mobile operation; propane transport on public roads is subject to DOT hazmat-adjacent rules for LP gas quantities above certain thresholds — verify per 49 CFR Part 173 (US) or equivalent jurisdiction"
  other: "CDL may be required depending on vehicle GVWR and jurisdiction; commercial-vehicle registration and insurance required; business license required per county on route; propane storage on vehicle subject to NFPA 58 (Liquefied Petroleum Gas Code) and DOT transport rules; OSHA 29 CFR 1910.252(c) hot-work standards apply at each client site"

# ── CONTEXT FIT ───────────────────────────────────────────────────────────────

lens_fit:
  market: good
  cooperative: poor
  civic: marginal

scale_fit:
  village: good
  town: marginal
  small_city: poor

# ── LENS CONTEXT ──────────────────────────────────────────────────────────────

lens_context:
  civic:
    political_coalition: "Rural county commission or agricultural-services board; likely allies include county farm bureau, extension service, and rural-resilience or agricultural-infrastructure advocates; grant programs (USDA Rural Development, state agricultural infrastructure funds) are a plausible capital source"
    council_vote_estimate: "Favorable in counties with documented smith-access gap and active agricultural community; likely 3-2 or 4-1 in favor where the service fills a genuine void; opposition on grounds of ongoing vehicle-operating cost and the difficulty of municipal oversight of a mobile asset"
    competes_with_private: "Civic deployment only justified in a documented service gap — a rural county with no operating private mobile or stationary smith within reasonable travel distance; a civic mobile forge that displaces a functioning private operator lacks public-goods justification"
    governance_form: "County-owned container and equipment; operated by a contracted journeyman smith (sole operator + driver) under a service contract specifying route coverage and priority service for agricultural clients; staffing model is contracted, not municipal employee"
    budget_line: "Capital via rural-development grant or county agricultural-services fund; annual vehicle operating and maintenance costs under agricultural-infrastructure or emergency-services line; container and equipment depreciation over 15–20 years"
    benchmark_comparison: "[CITATION-NEEDED: direct per-household cost comparison for a county mobile-smith service vs. mobile-library service in a comparable rural county] At rural-county village scale (~500 hh served per route segment): annualized capital ($55,000 over 20 yr = $2,750/yr) + install ($4,000 over 20 yr = $200/yr) + operating ($3,200 maintenance + $3,800 consumables = $7,000/yr) = ~$9,950/yr total, or ~$19.90/hh/yr for the served village segment. Analogous civic service: mobile library vs. fixed library — mobile library delivery costs are typically 30–60% lower per-patron than fixed-branch costs in rural county studies [CITATION-NEEDED: rural mobile-library cost-ratio study; IMLS data or state library agency comparison]. The mobile-smith cost ratio is structurally analogous: mobile delivery eliminates fixed-site capital while adding vehicle operating cost."
    staffing_model:
      role: "contracted journeyman smith (sole operator and driver)"
      operator_fte: 1.0
      wage_assumption: 48000
      wage_source: "corpus/program/SCALES.md §3 village-scale skilled-trades median ($48,000/yr)"
      hours: "40 hr/wk total: ~20 hr active forging + ~15–20 hr route driving and setup/teardown"
      hiring_notes: "Journeyman smith with propane-forge experience and a valid commercial driver's license (or GVWR below CDL threshold for lighter vehicle configurations); hiring pool is thin in rural markets — regional search radius of 100+ miles likely required; single-seat mobile operation does not support an apprentice, so there is no built-in training pipeline"
    civic_externalities:
      - "Route-based farm-equipment repair: a mobile civic smith provides emergency repair access to farms and homesteads that have no practical alternative when a critical piece of equipment breaks during planting or harvest — the market cannot sustain a stationary private smith in very thin demand areas, but a route service aggregates demand across geography"
      - "Rural community resilience: a contracted mobile smith maintains a metalworking capability that would otherwise be absent from the county, supporting downstream trades and household-level repair capacity in communities with limited purchasing power"

# ── SIMULATION PARAMETERS ─────────────────────────────────────────────────────

sim_params:
  cost_mean: 55000
  cost_sd: 11250
  throughput_units_equiv_per_year: 660
  variable_cost_per_unit: 5.76
  labor_hours_per_unit: 1.29
  downtime_fraction: 0.18
  lifespan_years: 15

# ── RESULTS ───────────────────────────────────────────────────────────────────

results:
  village_market:    null
  village_coop:      null
  village_civic:     null
  town_market:       null
  town_coop:         null
  town_civic:        null
  small_city_market: null
  small_city_coop:   null
  small_city_civic:  null

# ── SOURCES ───────────────────────────────────────────────────────────────────

sources:
  - ref: "research/trades/smithing/DECLINE-VERDICT.md v1.0 (2026-04-18). Location-bound repair demand as the most survivable smithing niche; mobility as demand aggregation strategy."
  - ref: "catalog/smithing/SCHEMA.md v1.0 (schema_base_version 1.1). Throughput ceilings, propane energy-source table, operator-skill-floor definitions, first_year_failures reference list."
  - ref: "corpus/program/SCALES.md v1.0 (2026-04-18). Village-scale median wage $48,000/yr; civic cost threshold figures."
  - ref: "[CITATION-NEEDED: 19th-century traveling-smith circuit documentation — accounts of itinerant smiths serving rural routes in North America and Britain; no single consolidated academic source identified; see Historical Lineage for structural description derived from secondary trade and social-history sources.]"
  - ref: "[CITATION-NEEDED: modern mobile-farrier trade documentation — American Farriers Journal or American Farrier's Association rate surveys documenting on-site service premium over stationary-shop equivalents; cited as comparable-service analog for mobile repair pricing.]"
  - ref: "[CITATION-NEEDED: propane forge consumption rate at full operational load — 0.7 kg/hr is within the catalog/smithing/SCHEMA.md §2 range of 1–2 kg/hr; a lower figure is plausible for a single-burner compact mobile forge operating at partial output between heats; measured experimental value for a comparable mobile forge configuration required before promotion.]"
  - ref: "[CITATION-NEEDED: DOT 49 CFR Part 173 LP-gas transport threshold quantities and NFPA 58 storage rules — regulatory requirement cited in regulatory_notes; entries should verify current regulatory threshold before field deployment.]"
  - ref: "[CITATION-NEEDED: rural mobile-library vs. fixed-branch cost-ratio comparison — IMLS data or state library agency study; cited as structural analog for mobile civic service cost benchmarking in benchmark_comparison.]"
  - ref: "[CITATION-NEEDED: CDL GVWR thresholds by US jurisdiction — relevant to vehicle selection and operator licensing requirement; varies by state for intrastate commercial operation.]"
---

## Summary

Forge-007 is a mobile smithing operation: a propane-fired forge installed in a converted 20-ft intermodal container, transported by truck on a circuit of rural and village clients — farms, ranches, and homesteads. The intended operator is a journeyman smith who is also the driver, running a weekly or biweekly route rather than waiting for clients to come to a fixed shop. The entry tests a specific inversion of the DECLINE-VERDICT finding on location-bound demand: instead of a stationary smith hoping rural clients will travel to them, the smith travels to where the demand is anchored. Capital goes into the container conversion and vehicle rather than a building lease; floor-space rent is eliminated. The tradeoff is reduced throughput (travel time eats the week), vehicle operating cost, and a single-seat operation that cannot support an apprentice.

## Design rationale

No other entry in the smithing catalog addresses the mobility problem. Every other entry assumes a fixed site with a building lease, a fixed footprint, and clients who come to the smith. For markets where clients are geographically dispersed and individually too sparse to support a stationary shop — agricultural smallholdings, remote ranches, isolated homesteads on back roads — the mobile model is the only configuration that aggregates enough demand into a viable revenue base. Forge-005 (frontier revival coal, stationary) targets the same repair-dominant rural market from a fixed location; forge-007 is its mobile counterpart, trading coal for propane (portable fuel), building space for container space, and client foot traffic for a route circuit. The design space cell this entry occupies — mobile, propane, single operator, repair-dominant — has no competitor among the catalog entries and is explicitly supported by the DECLINE-VERDICT observation that location-bound demand is the most durable smithing niche. The mobility inversion is the design's core proposition.

## Historical lineage

Two functional precedents inform this design. The first is the 19th-century traveling-smith circuit: itinerant smiths who served rural regions in North America and Britain by traveling between farms and villages on a regular circuit, carrying a portable forge on a wagon or cart. [CITATION-NEEDED: consolidated documentation of itinerant traveling-smith circuits; described in secondary social-history sources but not in a single dedicated study identified at time of authoring.] These operators carried a fire pot, bellows, and minimal tooling; they worked at each farm for a day or two before moving on. The labor regime was informal and the capital investment was low — a horse, a wagon, and a portable hearth. What this entry carries forward from that precedent is the functional logic: aggregating thin, geographically dispersed demand by moving the production capacity to the client rather than moving the client to the production capacity. What it does not carry forward: the horse-drawn wagon and manual bellows are replaced by a diesel truck and a container with a mechanical ventilation system; the informal circuit arrangement is replaced by a scheduled route with named clients and a business license in each county; and the propane fuel replaces the charcoal or wood that a traveling smith would have relied on for portability (coal was rarely practical for transit-based operation given its weight and ash management requirements). The second precedent is the modern mobile-farrier trade, which never disappeared. Mobile farriery has operated continuously from the 19th century to the present, with farriers traveling routes to serve horse owners rather than expecting horses to be trailered to a fixed shop. [CITATION-NEEDED: American Farriers Journal or American Farrier's Association documentation of mobile-farrier route economics and service-premium pricing.] The mobile-farrier model is the closest living analog to what this entry proposes for general repair smithing: a single operator, a truck-based setup, on-site service at premium rates, and a route that covers more clients than any single fixed location could draw. The farrier trade demonstrates that the mobile service-at-site model is commercially viable and has persisted precisely because the demand is location-bound — you cannot easily ship a horse to a fixed-location farrier any more than you can ship a broken plow. The smithing parallel is structurally identical; the technical distinction is that farriery is narrower in scope (hoof work, horseshoeing) while mobile repair smithing requires the broader repair skill range of a journeyman.

## Key assumptions

Capital-cost range ($35,000–$80,000, mid $55,000) covers three major cost components: (1) container conversion fit-out — a used 20-ft intermodal container ($2,000–$4,000), propane forge installation ($3,000–$6,000), ventilation system ($1,500–$3,500), container electrical (shore-power hookup for induction unit when available, $1,000–$2,500), door modifications and work-surface install ($1,500–$3,000), total container component ~$9,000–$19,000; (2) forge equipment — propane forge ($1,500–$3,500), anvil ($800–$2,500), tooling and tongs ($800–$2,000), small induction unit for precision work ($2,500–$6,000 if included), quench infrastructure ($200–$500), total equipment ~$5,800–$14,500; (3) truck and vehicle — used Class 3–5 cab-and-chassis or flatbed capable of pulling or carrying the container ($15,000–$35,000 depending on age, mileage, and configuration), total vehicle ~$15,000–$35,000. [CITATION-NEEDED: used intermodal container pricing, forge equipment pricing, and Class 3–5 truck pricing; figures are consistent with publicly available marketplace data circa 2024–2025 but have not been verified against a formal commercial survey.] The mid figure ($55,000) represents a functional but not new configuration: a used container with a clean conversion, solid propane forge, and a reliable but high-mileage truck. The high figure ($80,000) includes a newer vehicle and a complete induction unit. Install cost ($4,000) covers container conversion labor beyond the equipment list above — welding work, custom brackets, floor reinforcement — and is an estimate. Annual maintenance ($3,200) is dominated by vehicle maintenance (~$2,000/yr budget for a used truck per vehicle-age norms) plus container and equipment maintenance (~$1,200/yr); the vehicle component is the most variable and age-dependent. Annual consumables ($3,800) covers propane (~0.7 kg/hr × 1,040 active hr/yr × ~$1.80/kg = ~$1,310) plus vehicle fuel for route driving (estimated separately; not included in consumables — route fuel is an operational cost that varies by route length and is treated as a cost-of-revenue item, not a consumable for the forge), steel stock replenishment, flux, and small consumable parts; rounded to $3,800 to account for stock variability. [CITATION-NEEDED: retail propane price for commercial small-quantity purchases; $1.80/kg is used as a central estimate consistent with LP-gas retail pricing in rural US markets circa 2024–2025.] Floor-space rent is $0 because the mobile operation has no fixed commercial lease; the container parks at the operator's home base between routes. The throughput calculation uses a weighted product-mix rate: 0.85 × 0.8 (medium_work repair dominant) + 0.10 × 0.8 (medium_work specialty) + 0.05 × 0.2 (large_work artistic) = 0.68 + 0.08 + 0.01 = 0.77 units/hr equivalent. Net active forging hours: 25 hr/wk gross ceiling minus 60 min/day × 5 days = 5 hr/wk startup/shutdown overhead = 20 hr/wk net. Annual derated hours: 20 × 52 × (1 − 0.18) = 20 × 52 × 0.82 = 852.8 hr/yr. Throughput: 852.8 × 0.77 ≈ 657, rounded to 660 units/yr. cost_sd = (80,000 − 35,000) / 4 = 11,250. labor_hours_per_unit = 852.8 / 660 ≈ 1.29; cross-check: 660 × 1.29 = 851 ≈ 853 ✓. variable_cost_per_unit = $3,800 / 660 ≈ $5.76. Downtime fraction (0.18) reflects vehicle mechanical events (~4% of scheduled weeks lost to repair), weather-related route cancellations (~6% in winter months), and general setup/interruption overhead (~8%); this is higher than a stationary shop (forge-005 uses 0.10) because vehicle dependency adds a failure mode absent from stationary operations. Lifespan (15 years) is shorter than stationary entries (25 years) because the vehicle has a shorter practical service life than a building and forge equipment; the container and forge equipment could last longer but the vehicle replacement cycle dominates the economic horizon. The capital_cost.mid asymmetry: the mid ($55,000) is slightly below the arithmetic mean of low and high ($57,500), reflecting that a capable operator can source a serviceable used truck and container below the midpoint with patience.

## Known risks / failure modes

**Regulatory.** The primary regulatory risk is vehicle-weight and licensing complexity. Depending on the truck and container configuration (mounted on a flatbed vs. towed on a trailer), the gross vehicle weight rating (GVWR) may exceed the CDL threshold in the operator's jurisdiction. [CITATION-NEEDED: CDL GVWR threshold by state/jurisdiction.] An operator who does not hold a CDL cannot legally drive a qualifying vehicle, and obtaining a CDL requires testing, medical certification, and lead time. A second regulatory risk is propane transport: LP gas carried in quantities above DOT thresholds triggers hazmat transport rules (placarding, driver certification, route restrictions in some tunnel and bridge jurisdictions). An operator who configures the truck with a large on-board propane supply to extend route autonomy may inadvertently cross the DOT threshold. The county-by-county business-license requirement on the route is an administrative burden rather than a showstopper, but failing to secure licenses before operating in a county creates liability exposure.

**Labour pipeline.** The single-operator mobile model has the highest succession risk in the smithing catalog. There is no apprentice path, no institutional continuity, and no backup operator. If the smith retires, is injured, or leaves, the route ceases immediately and completely. The operator's combined skill set — journeyman smithing AND commercial driving AND client relationship management AND vehicle maintenance judgment — is narrow and cannot be disaggregated. Finding a replacement who holds all four capabilities is harder than finding a replacement stationary smith. Vehicle injury risk during transit also exceeds the shop-floor injury risk profile of a stationary entry. The absence of an apprentice path is documented here as required by schema and by Principle 9: this entry has no built-in succession mechanism, and any operator planning a multi-decade operation should either develop a transition plan toward a stationary model (acquire a fixed site when the route matures) or document an explicit succession timeline.

**Supply chain.** Vehicle mechanical failure is the primary operational risk unique to this entry and absent from all stationary entries. A truck breakdown mid-route strands the container, cancels client appointments, and requires a tow plus vehicle repair before operations can resume. A two-week vehicle repair (the lead time for a significant mechanical failure) costs 2 weeks of revenue plus repair cost, which is a material fraction of a seasonal revenue month. The mitigation is a rigorous weekly vehicle inspection and an annual full service (per maintenance_schedule) plus a cash reserve buffer for vehicle repair. Propane supply disruption is lower risk than coal (propane is available from multiple suppliers in most rural markets and can be transferred from any LP supplier's tank), but a mobile operator far from a refill point mid-route faces a shorter operational window than a stationary smith with an on-site bulk tank. The practical mitigation is carrying a minimum 2-day propane reserve on the truck at all times.

## Iteration log

- 2026-04-18: v0.1 — initial entry authored per Plan C Task 9. Propane-primary mobile forge, container conversion, single-operator route model. Throughput derated for travel overhead (20 hr/wk net). Civic marginal sketch populated per schema requirement; cooperative omitted (poor). Succession risk named explicitly per apprentice_friendly: false requirement. Vehicle-specific operational risks named in Known Risks. No docs/superpowers/ paths used.
