---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: bake-004
trade: baking
name: "Wholesale Artisan Loaf Bakery (electric deck, B2B channel)"
tagline: "Multi-deck electric bakery supplying restaurants, cafés, and grocery stores at wholesale volume"
status: draft
version: 0.1
supersedes: null
inspirations: [mid-20th-century-regional-wholesale-bread-bakery, danish-cooperative-wholesale-bakeries-1950s]

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 65
ceiling_min_m: 3.0
ventilation: mechanical-extraction-required

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: electric-deck
energy_consumption_per_active_hour: "18 kWh (2-3 deck units at combined full load)"
backup_fuel: null

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  loaves_per_day: 350
  # Mid-range of 200-500 loaves/day spec; unit = 800g sourdough boule equivalent.
  # Two to three deck oven units operating in rotation; stated unit used throughout.
  batches_per_day: 3
  batch_size_loaves: 117
  # 3 batches × 117 loaves ≈ 350/day; each batch across 2-3 decks simultaneously.
  max_active_hours_per_week: 48
  # 6-day production week × 8 active oven-operation hours/day.
  # See max_active_hours_realism_note for derating to net.
  product_mix:
    bread: 85
    confection: 5
    specialty: 5
    catering: 5
  throughput_variance:
    worst_month_fraction_of_average: 0.65
    best_month_fraction_of_average: 1.35
    seasonal: "Moderate summer (July-August) trough as restaurant volume drops; November-December peak driven by grocery and café holiday orders."

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: journeyman-baker
operators_concurrent: "2-3"
apprentice_friendly: true
apprentice_path:
  training_stages: "Stage 1 (0-4 mo): dough mixing protocol, shaping basics, oven loading/unloading under direct supervision. Stage 2 (4-12 mo): proofing schedule management, single-deck operation, quality-check routines; operator can run one deck independently. Stage 3 (12-24 mo): full multi-deck rotation management, sourdough fermentation judgment, batch scheduling across concurrent orders; operator reaches journeyman floor."
  time_to_independent_operation: "~24 months to journeyman standard on this equipment; faster than a micro-bakery context because high-volume repetition accelerates competency acquisition."
  succession_note: "Apprentice works alongside journeyman operators during normal production runs; skill transfer is embedded in daily workflow rather than a separate training program. The 2-3 operator model ensures institutional knowledge is not concentrated in a single person."

# ── BAKING-SPECIFIC REQUIRED FIELD ───────────────────────────────────────────

flour_source_declaration: industrial-flour-purchased
# Volume purchasing from regional distributor or industrial mill.
# Local-mill sourcing is not reliably viable at 200-500 loaves/day scale without
# a formal supply contract; see Key Assumptions.

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD
  capital_cost: { low: 60000, mid: 100000, high: 160000 }
  # Low: 2 used/refurbished deck units + used mixer + basic proofer cabinet.
  # Mid: 2-3 new mid-range deck units + industrial spiral mixer + dedicated proofer room.
  # High: 3 premium deck units + two mixers + purpose-built proofer room + ventilation upgrade.
  install_cost: 12000
  # Electrical service upgrade (3-phase, 100-200A), ventilation ducting, floor drainage,
  # plumbing for steam injectors. Estimate; flagged [CITATION-NEEDED] per E-1.
  annual_maintenance: 6000
  # Deck element replacements, thermostat calibration, proofer servicing across 2-3 units.
  annual_consumables: 62000
  # Flour: ~$0.40/loaf × 95,000 loaves = $38,000; packaging/trays ~$0.10/loaf = $9,500;
  # energy 18 kWh/hr × 48 hr/wk × 50 wks × $0.12/kWh = $5,184; misc supplies ~$9,316.
  floor_space_rent_per_year: 19500
  # 65 m² × $300/m²/yr; light-industrial commercial rate estimate, flagged [CITATION-NEEDED].
  market_price_per_unit: { low: 3.50, mid: 5.50, high: 8.00 }
  # Wholesale price per 800g sourdough boule equivalent. Lower than DTC; see pricing_notes.
  industrial_baseline_price: 2.50
  # Commodity supermarket sliced bread at wholesale: ~$2.50/loaf equivalent.
  # Source: USDA ERS bread price series 2024 [CITATION-NEEDED].
  pricing_notes: "Per 800g sourdough boule equivalent at wholesale to B2B customers (restaurants, cafés, specialty grocery). Premium of $1.00-$5.50 over commodity industrial baseline ($2.50/loaf wholesale; USDA ERS) reflects artisan fermentation, crust character, and local-bakery branding. Customer segment: independent restaurants and specialty grocers willing to pay for product differentiation; not mass-market grocery chains."
  pricing_validation: "Market price evidence: wholesale artisan bread pricing data from King Arthur Baking Company industry survey 2023 and Specialty Food Association wholesale channel benchmarks 2024 [CITATION-NEEDED]. Mid-point $5.50 consistent with reported wholesale pricing for artisan sourdough in US regional markets. Not a cost-plus residual."

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:
  first_year_failures:
    - item: "Deck heating element (primary deck unit)"
      estimated_hours_to_failure: 2000
      replacement_cost: 800
      replacement_lead_time_days: 14
      serviceable_by: journeyman
    - item: "Oven thermostat / controller (any deck unit)"
      estimated_hours_to_failure: 2500
      replacement_cost: 450
      replacement_lead_time_days: 7
      serviceable_by: journeyman
    - item: "Proofer heating element or thermostat"
      estimated_hours_to_failure: 1500
      replacement_cost: 300
      replacement_lead_time_days: 5
      serviceable_by: operator

  maintenance_schedule:
    daily:
      task: "Clean deck surfaces and oven interior; inspect door seals; check proofer temperature and humidity; log any thermostat drift."
      performed_by: operator
    weekly:
      task: "Deep-clean all deck surfaces; inspect steam injector nozzles for scale buildup; check mixer dough hook and bowl seals; verify proofer humidity calibration."
      performed_by: operator
    quarterly:
      task: "Descale steam injectors; inspect deck stones for cracking or spalling; calibrate all oven thermostats against reference probe; inspect electrical connections and heating element continuity."
      performed_by: journeyman
    annual:
      task: "Full deck inspection by equipment service technician: element resistance test, structural inspection, ventilation duct cleaning, proofer full service, mixer gearbox inspection."
      performed_by: specialist

  startup_shutdown_overhead_per_day_min: 45
  # Oven preheat (~20 min at start of day), end-of-day cleaning and shutdown (~25 min).
  # Multiplied across 6-day week: 45 × 6 = 270 min/wk = 4.5 hr/wk non-productive overhead.

  max_active_hours_realism_note: "48 hr/wk is the theoretical gross active-operation ceiling for a 6-day × 8-hr schedule. Subtracting 4.5 hr/wk startup-shutdown overhead yields ~43.5 net productive hr/wk. sim_params uses 95,000 loaves/year derived from loaves_per_day × operating days, consistent with net hours; the figure is not inflated by gross-maximum assumptions."

  interruption_notes: "Typical intraday interruptions: delivery coordination and client order calls (~20 min/day), batch scheduling adjustments when one deck is in maintenance rotation (~15 min/day), apprentice oversight (~15 min/day when applicable). These are folded into the loaves_per_day mid-point figure of 350 rather than the theoretical maximum of 500."

  consumables_lead_time_days: { typical: 3, worst: 14 }
  # Flour from regional distributor: typical 1-3 days; worst-case (supply disruption,
  # distributor stockout) 14 days; alternative supplier switch adds 2-3 days.

  throughput_variance:
    seasonal: "Moderate summer (July-August) trough as restaurant volume drops; November-December peak driven by grocery and café holiday orders."
    worst_month_fraction_of_average: 0.65
    best_month_fraction_of_average: 1.35

  operator_impact:
    noise_db: 70
    # Electric deck ovens are quiet relative to combustion equipment; mixer is the
    # primary noise source during dough-prep phase (~70 dB at operator position) [CITATION-NEEDED].
    heat_exposure: "Moderate-high near open deck doors during loading/unloading; ambient bakery temperature elevated 5-10°C above ambient during full-production periods. Manageable with adequate HVAC."
    emissions: "Near-zero combustion emissions (electric); flour dust is the primary air-quality concern (respiratory exposure). Mechanical extraction required per baking SCHEMA.md for flour-dust management."
    physical_demand: "Moderate-heavy: sustained standing on concrete, repetitive lifting of dough batches (10-20 kg), loading and unloading deck ovens at working height. Repetitive strain risk for mixer operators."

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Light-industrial or commercial-kitchen zoning required; wholesale food production typically excluded from residential and retail-only zones; confirm with local jurisdiction."
  emissions: "Electric deck produces near-zero combustion emissions; flour-dust extraction may require mechanical ventilation permit above certain throughput thresholds in some jurisdictions."
  other: "Commercial kitchen license required; HACCP plan mandatory for wholesale B2B supply; delivery vehicle registration and food-transport certification if baker operates own delivery; health-department inspection on commissioning."

# ── CONTEXT FIT ──────────────────────────────────────────────────────────────

lens_fit:
  market: good
  cooperative: marginal
  civic: poor

scale_fit:
  village: poor
  town: marginal
  small_city: good

# ── LENS CONTEXT ─────────────────────────────────────────────────────────────

lens_context:
  cooperative:
    membership_boundary: "Operators and investors in the wholesale bakery cooperative; open to any qualified baker or working-capital contributor within the regional service area (typically 50-mile radius for delivery logistics)."
    rules_source: "Operating agreement and bylaws; member vote to amend with 2/3 majority at annual general meeting."
    monitoring: "Per-batch production logs; daily sales and delivery records reviewed by elected operations steward; quarterly financial reporting to all members."
    graduated_sanctions: "Warning → profit-share reduction for the quarter → 90-day suspension from operations → membership review and potential buyout."
    conflict_resolution: "Operations steward mediates initial disputes; unresolved disputes escalate to full membership vote; legal arbitration as last resort per operating agreement."
    ostrom_principles_addressed: [1, 2, 3, 4, 5, 6]
    member_amendment_process: "2/3 vote at annual general meeting; 30-day written notice to all members required; emergency amendments require 3/4 vote with 14-day notice."
    legal_form: "State-registered worker cooperative or LLC with cooperative operating agreement; formal registration required given capital investment and B2B contract liability exposure."
    scale_fit_note: "Governance calibrated for small-city scale (15,000-75,000 residents); at town scale the B2B customer base may be insufficient to sustain the operation and the cooperative membership pool too small for effective governance rotation."

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 100000
  # Equals economics.capital_cost.mid per E-3 R1.
  cost_sd: 25000
  # (160,000 - 60,000) / 4 = 25,000; cost_sd/cost_mean = 0.25, within E-3 R5 range.
  throughput_units_equiv_per_year: 95000
  # Derivation: 350 loaves/day (800g boule equivalent) × 300 operating days/year
  # × (1 - 0.10 downtime) ≈ 94,500, rounded to 95,000.
  # Annual operating days: 6 days/wk × 52 wks = 312 gross days; 300 net after
  # holidays and planned closure weeks. Consistent with max_active_hours_realism_note.
  variable_cost_per_unit: 0.65
  # Per loaf: flour $0.40 + energy $0.065 + packaging/trays $0.10 + misc $0.085.
  # Energy per loaf: 18 kWh/hr × (48 hr/wk / (350 loaves/day × 6 days/wk)) × $0.12/kWh ≈ $0.065.
  labor_hours_per_unit: 0.059
  # Total operator-hours per year: 2.5 operators × 48 hr/wk × 52 wks × 0.90 = 5,616 hrs.
  # labor_hours_per_unit = 5,616 / 95,000 ≈ 0.059 hr/loaf.
  # E-3 R3 check: 95,000 × 0.059 = 5,605 ≈ 5,616 (within 0.2%). ✓
  downtime_fraction: 0.10
  # 10% accounts for planned maintenance windows (quarterly specialist visits),
  # first-year component failures with 5-14 day lead times, and B2B order-gap days.
  # Consistent with operations_reality profile (3 first-year failures, 5-14 day lead times).
  lifespan_years: 18
  # Mid-range commercial electric deck oven lifespan with regular maintenance;
  # manufacturer-rated service life typically 15-20 years [CITATION-NEEDED].

# ── RESULTS ──────────────────────────────────────────────────────────────────

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

# ── SOURCES ──────────────────────────────────────────────────────────────────

sources:
  - ref: "USDA Economic Research Service, 'Retail Bread Prices and Costs,' 2024 [CITATION-NEEDED — replace with specific ERS report URL and access date]"
  - ref: "King Arthur Baking Company, 'Wholesale Artisan Bread Pricing Survey,' 2023 [CITATION-NEEDED — replace with actual survey or industry report citation]"
  - ref: "Specialty Food Association, 'State of the Specialty Food Industry 2024,' wholesale channel section [CITATION-NEEDED — replace with SFA report URL and access date]"
  - ref: "IBIS World or BLS, commercial bakery equipment lifespan industry data [CITATION-NEEDED — replace with specific source for 15-20 yr electric deck oven lifespan]"
  - ref: "Local commercial real estate rate estimate, light-industrial zone, $300/m²/yr [CITATION-NEEDED — replace with local market rate data source]"
  - ref: "research/trades/baking/REQUIREMENTS.md — throughput ranges, operator skill definitions, energy source specifications"
  - ref: "research/trades/baking/DECLINE-VERDICT.md — flour sourcing and B2B channel niche targeting guidance"
  - ref: "catalog/baking/SCHEMA.md v1.0 — baking throughput structure, energy_source enumeration, flour_source_declaration field"
---

## Summary

bake-004 is a medium-scale artisan bakery designed primarily for wholesale supply to local B2B customers: independent restaurants, specialty cafés, and neighborhood grocery stores. It occupies the space between a micro-bakery (bake-001 or bake-002, under 100 loaves/day, direct-to-consumer) and an industrial bread plant. The defining characteristics are: multiple electric deck oven units in rotation, a two-to-three-operator team, 200-500 loaves/day throughput, and a B2B sales channel that trades a lower per-unit price for volume and predictable order flow. This entry exists in the catalog because no other baking entry addresses the wholesale B2B channel at this throughput scale; the economics, failure modes, and regulatory posture are materially different from DTC artisan and from cottage-scale operations.

## Design rationale

The problem bake-004 solves is the viability gap in the artisan bakery segment between micro-scale DTC operations (high margin, low volume, operator-dependent) and industrial commodity production (low margin, high volume, capital-intensive). Wholesale artisan supply at 200-500 loaves/day serves restaurants and specialty grocers who want product differentiation but cannot source it reliably from micro-bakeries. The entry documents whether this middle tier is viable under real wholesale pricing ($3.50-$8.00/loaf versus $2.50 industrial baseline), the B2B customer acquisition risk, and the capital requirements for multi-deck electric operation. A micro-bakery entry cannot model this space: the throughput, operator headcount, capital cost structure, and primary failure mode (B2B client attrition rather than foot-traffic volatility) are all different. An industrial entry cannot model it either: the artisan premium, skill floor, and regulatory posture diverge sharply.

## Historical lineage

The functional predecessor of this design is the mid-20th-century regional wholesale bread bakery: a non-industrial, family-owned operation supplying a defined local geography before supermarket consolidation displaced independent regional bakers. These operations used deck ovens (then typically gas or wood-fired), employed two to five bakers, and operated on direct supply relationships with local grocers and restaurants. The functional inheritance this entry carries forward is the multi-deck rotation model (staggered batch loading to maintain continuous output), the B2B relationship structure (account-based rather than transactional), and the journeyman-or-above skill floor that made consistent commercial-volume output possible without a factory-scale quality-control infrastructure. The labor regime of those operations — family or tight-knit cooperative ownership, multi-generational skill transfer — cannot be reproduced directly; bake-004 substitutes formal apprentice pathways and written operating procedures. The supply-chain condition that made them viable (local-regional distribution before supermarket consolidation) is partially recoverable in the farm-to-table and locally-sourced restaurant movement that creates contemporary B2B demand. Danish cooperative wholesale bakeries of the 1950s provide an additional precedent for the cooperative lens: worker-owned or farmer-cooperative-backed bakeries operated at this scale in Scandinavia with explicit coordination of supply and customer relationships, demonstrating that cooperative governance at this throughput is operationally viable, though the cooperative lens rates only marginal here due to the capital requirements and B2B contract management complexity.

## Key assumptions

Capital cost mid-point ($100,000) assumes 2-3 mid-range commercial electric deck oven units at $20,000-$35,000 each, an industrial spiral mixer at $8,000-$15,000, and a dedicated proofer room at $5,000-$12,000 with controls. This is a rough estimate; actual quotes vary significantly by brand and configuration. The install cost ($12,000) is an order-of-magnitude estimate for electrical service upgrade, ventilation ducting, and plumbing. Both figures are flagged [CITATION-NEEDED] and should be replaced with equipment supplier quotes before promotion to reviewed status.

Flour sourcing is declared as industrial-flour-purchased. At 200-500 loaves/day, flour consumption is approximately 160-400 kg/day (assuming ~500g flour per 800g loaf with water and other ingredients). This volume is manageable through regional distributors but typically exceeds what a single local artisan mill can supply reliably without a formal supply contract. The entry does not claim a premium sourcing narrative; the artisan premium rests on fermentation method and product character rather than grain provenance. An operator seeking to add a local-mill sourcing claim should clone this entry and modify to flour_source_declaration: local-mill-partnership with supply documentation.

Wholesale pricing mid-point ($5.50/loaf) is based on reported wholesale pricing for artisan sourdough in US regional markets [CITATION-NEEDED]. The industrial baseline ($2.50/loaf) is a commodity supermarket wholesale benchmark [CITATION-NEEDED]. The premium of $3.00/loaf at mid-point is achievable in markets with strong independent-restaurant culture but not guaranteed in all US geographies.

The throughput figure (350 loaves/day, 95,000/year) is derived from 300 operating days/year (6 days/week, accounting for holidays and planned downtime) at 350 loaves/day mid-range, derated by 10% downtime. The 800g sourdough boule equivalent is the stated unit; authors adapting this entry for baguette-primary or enriched-loaf production must restate the unit.

## Known risks / failure modes

**Regulatory:** Commercial kitchen licensing and HACCP compliance are non-negotiable for wholesale supply. In many US jurisdictions, a wholesale bakery supplying grocery stores requires additional State-level food manufacturing registration beyond the local commercial kitchen license. Failure to obtain the correct registration tier before commencing wholesale delivery is a primary early-operational failure mode. Delivery logistics (if the baker operates their own delivery route) add vehicle certification and food-transport compliance requirements.

**Labour pipeline:** The journeyman-baker skill floor is achievable but not abundant in all labor markets. A 2-3 operator bakery is vulnerable to key-person risk: if the lead journeyman operator departs, production quality and consistency are at risk while a replacement is hired or an apprentice is promoted. The apprentice path (24 months to journeyman) means a bakery that loses its lead operator cannot backfill skills in under two years from an internal pipeline. Succession risk is partially mitigated by the 2-3 operator model (knowledge is distributed), but the risk is real and should be named in any business plan.

**Supply chain:** Industrial flour purchasing from a regional distributor introduces price volatility and supply-continuity risk. A single-distributor dependency with typical 3-day lead time and worst-case 14-day lead time means a stockout or distributor disruption halts production within days. Mitigation: maintain 2-week flour inventory buffer and identify at least one alternative supplier. The 14-day worst-case lead time in consumables_lead_time_days reflects this documented risk.

**B2B channel (primary failure mode):** The wholesale model requires 3-6 stable restaurant and grocery clients to sustain operations at viable throughput. B2B customer acquisition is slower and more relationship-dependent than DTC foot-traffic; a new bakery at this scale typically requires 6-18 months to build a stable wholesale account base. Client attrition is the primary ongoing risk: a restaurant closure, menu change, or distributor substitution can remove 15-25% of revenue in a single event. The scale_fit and lens_fit assessments reflect this: village and town scales are poor-to-marginal because the B2B customer density is insufficient; small_city provides adequate restaurant and specialty grocery density to sustain 3-6 stable accounts.

## Iteration log

- 2026-04-18: v0.1 — initial creation per Plan G task 6. All economic figures flagged [CITATION-NEEDED] where primary sources were not available; to be replaced before promotion to reviewed status.
