---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: bake-005
trade: baking
name: "Mobile Pop-up Bakery (van-based, farmers-market and community-event route)"
tagline: "Solo operator bakes the night before, then sells direct at market — zero commercial-lease overhead, zero cold-chain"
status: draft
version: 0.1
supersedes: null
inspirations: [19th-century-travelling-market-baker, modern-farmers-market-artisan-vendor]

# ── PHYSICAL ENVELOPE ─────────────────────────────────────────────────────────

footprint_m2: 10
ceiling_min_m: 1.8
ventilation: natural-sufficient

# ── ENERGY ────────────────────────────────────────────────────────────────────

energy_source: convection-electric
energy_consumption_per_active_hour: "3.5 kWh (van-mounted convection oven on generator, or home-kitchen equivalent during night-before bake)"
backup_fuel: null

# ── THROUGHPUT ────────────────────────────────────────────────────────────────

throughput:
  loaves_per_day: 90
  # Unit: 800g sourdough boule equivalent. Range 60-120 per event depending on
  # product mix. 90 is the central estimate for a 2-event/week mature route.
  batches_per_day: 3
  # 3 convection-oven loads of approx. 30 loaf-equivalents each during the
  # 3-4 hr pre-bake window (night before or morning of event).
  batch_size_loaves: 30
  # Convection oven at van-scale: ~30 loaf-equivalents per load per
  # baking/SCHEMA.md §2 guidance for convection-electric [CITATION-NEEDED].
  max_active_hours_per_week: 16
  # Gross active hours: 2 market days/wk × 8 hr/day (4 hr bake night-before
  # + 4 hr travel + market setup + selling + breakdown). See
  # max_active_hours_realism_note for derating.
  product_mix:
    bread: 70
    confection: 15
    specialty: 10
    catering: 5
  throughput_variance:
    worst_month_fraction_of_average: 0.55
    # Summer (July-August) outdoor-market trough; heat reduces foot traffic and
    # loaf shelf life in-market. January post-holiday slowdown also significant.
    best_month_fraction_of_average: 1.40
    # Pre-holiday (November-December) and early-spring (April-May) peaks.
    seasonal: "Summer (Jul-Aug) and January troughs; spring and pre-holiday peaks dominate revenue."

# ── OPERATOR PROFILE ──────────────────────────────────────────────────────────

operator_skill_floor: journeyman-baker
operators_concurrent: "1"
apprentice_friendly: false

# ── ECONOMICS ─────────────────────────────────────────────────────────────────

economics:
  currency: USD
  capital_cost: { low: 20000, mid: 38000, high: 60000 }
  # Low: used cargo van + second-hand convection oven + small generator +
  # basic licensing. Mid: reliable van + commercial convection oven + mid-size
  # generator + full licensing and fit-out. High: newer van with full kitchen
  # conversion, commercial combi-oven, large generator, branded build-out.
  install_cost: 2500
  # Van interior fit-out: oven bracket, generator mounting, ventilation mod,
  # shelving, tie-downs. Estimated.
  annual_maintenance: 3200
  # Van service ($1,800/yr), generator service ($600/yr), oven maintenance
  # ($500/yr), miscellaneous ($300/yr). Estimated from comparable mobile-food
  # vendor operating costs [CITATION-NEEDED].
  annual_consumables: 6400
  # ~$0.80/loaf-equivalent × 7,956 loaves/yr ≈ $6,365, rounded to $6,400.
  # Covers flour, enrichments, salt, yeast/starter maintenance, and packaging.
  # See Key Assumptions for flour-cost breakdown.
  floor_space_rent_per_year: 0
  # No commercial kitchen lease assumed. Home kitchen licensed under cottage-
  # food or residential-commercial license; van parks at operator's home. If a
  # shared commissary kitchen is required (jurisdiction-dependent), add
  # ~$2,400–$6,000/yr in Key Assumptions.
  market_price_per_unit: { low: 6, mid: 9, high: 14 }
  # Per 800g loaf-equivalent at farmers-market or community-event direct sale.
  # Observed range across US regional artisan-market vendors [CITATION-NEEDED:
  # direct survey of farmers-market bread pricing; $6–$14/loaf range is
  # consistent with USDA AMS farmers-market price monitoring and practitioner-
  # reported pricing, but entry-specific citation required before promotion].
  industrial_baseline_price: 3
  # Nearest industrial equivalent: commodity pre-sliced sandwich loaf at
  # grocery-chain shelf price. $2.50–$3.50 range; $3.00 used as central
  # estimate [CITATION-NEEDED: USDA ERS retail bread price series].
  pricing_notes: "Unit is one 800g sourdough boule equivalent sold at farmers market or community event. Industrial baseline ($3/loaf) is commodity grocery-store sandwich bread; artisan market premium (2–5×) reflects handcraft differentiation, sourdough long-ferment process, and farmers-market experience economy. Customer segment: farmers-market regulars and food-aware consumers within the event footprint willing to pay a direct-producer premium. Premium is structurally consistent with the mobile-farrier analog from forge-007: demand is geographically anchored at market locations, the baker travels to where the customers aggregate, and the product is perishable and not available via mail-order. [CITATION-NEEDED: direct survey of farmers-market artisan-bread vendors confirming $6–$14/loaf range.]"
  pricing_validation: "Market price evidence is inferred from farmers-market vendor observations and USDA AMS farmers-market monitoring reports. No single peer-reviewed pricing survey for artisan bread at US farmers markets has been identified; USDA AMS reports price ranges by commodity category and region for some products [CITATION-NEEDED: USDA AMS Farmers Market Metrics or equivalent]. Evidence type: observed comparable-vendor pricing and structural inference from premium-food direct-sales literature; not a cost-plus residual. A direct vendor survey or USDA AMS price-monitoring citation is required before promotion to reviewed."

# ── OPERATIONS REALITY ────────────────────────────────────────────────────────

operations_reality:
  first_year_failures:
    - item: "Convection fan motor (bearing failure under repeated thermal cycling)"
      estimated_hours_to_failure: 2000
      replacement_cost: 350
      replacement_lead_time_days: 7
      serviceable_by: journeyman
    - item: "Oven door seal / gasket (heat loss and inconsistent bake)"
      estimated_hours_to_failure: 1800
      replacement_cost: 80
      replacement_lead_time_days: 5
      serviceable_by: operator
    - item: "Generator (carburetor or voltage regulator failure under weekly load cycle)"
      estimated_hours_to_failure: 1500
      replacement_cost: 400
      replacement_lead_time_days: 10
      serviceable_by: journeyman
    # Fan motor and gasket items from catalog/baking/SCHEMA.md §5 reference list.
    # Generator failure is mobile-van-specific; [CITATION-NEEDED: typical small
    # generator MTTF under weekly commercial load; 1,500 hr is a conservative
    # estimate for a residential-grade unit pressed into commercial use].

  maintenance_schedule:
    daily:
      task: "Post-market cleanup of van interior and baking surfaces; inspect oven door seal; wipe generator exhaust area; verify oven thermostat calibration against bake result"
      performed_by: operator
    weekly:
      task: "Generator oil check and air-filter inspection; oven interior deep-clean; van tire and fluid check; packaging inventory restock; sourdough starter health check"
      performed_by: operator
    quarterly:
      task: "Generator full service (oil change, spark plug, air filter); oven thermostat calibration with external probe; van service interval check; inspect van floor and tie-downs for wear"
      performed_by: operator
    annual:
      task: "Van full service (oil, filters, brakes, tires, commercial-vehicle inspection); oven interior inspection and element check; generator carburetor service; health-permit and mobile-food-vendor license renewal review"
      performed_by: specialist

  startup_shutdown_overhead_per_day_min: 90
  # Per market day: 30 min travel to market site + 30 min setup (tent, tables,
  # display, product layout) + 30 min breakdown and reload = 90 min. Bake
  # overhead (mixing, shaping, proofing) occurs the night before and is
  # captured in the max_active_hours_per_week ceiling, not here.

  max_active_hours_realism_note: "16 hr/wk is the gross ceiling for 2 market days × 8 hr/day (night-before bake session + travel + market setup + selling + breakdown). Startup/shutdown overhead of 90 min/day × 2 days = 3 hr/wk is subtracted to yield a net active production and selling time of ~13 hr/wk. sim_params uses the gross-event loaf count (90 loaves/event × 2 events/wk = 180 loaves/wk) derated by downtime_fraction (0.15), not the hours formula directly, because throughput is event-count-bounded before it is hours-bounded. The two calculations are reconciled in Key Assumptions."

  interruption_notes: "Market-day interruptions include customer conversation and payment handling (~15–20 min/market-day), product swap-out mid-market when early items sell out, and weather-related early breakdown. These are absorbed into the downtime_fraction and the conservative 2-event/wk base rate; a 2.5-event week is the upside case that requires a separate night-before bake session."

  consumables_lead_time_days: { typical: 2, worst: 10 }
  # Flour from warehouse distributor: typical 2-day reorder; worst-case 10 days
  # during supply disruptions or regional distribution shutdowns [CITATION-NEEDED].

  throughput_variance:
    seasonal: "Summer (Jul-Aug) and January troughs; spring and pre-holiday peaks dominate revenue."
    worst_month_fraction_of_average: 0.55
    best_month_fraction_of_average: 1.40

  operator_impact:
    noise_db: 65
    # Convection oven fan at operator position: ~60–70 dB(A); generator outside
    # van: ~70–75 dB(A) at 3m but van wall provides ~10 dB attenuation.
    # Market environment: ~60–70 dB(A) ambient. No industrial noise hazard.
    heat_exposure: "Moderate during bake session: convection oven in enclosed van raises ambient temperature; adequate cross-ventilation (van doors open during bake) required. At outdoor market: ambient temperature, no oven heat."
    emissions: "Near-zero on-site combustion during baking (electric convection oven). Generator exhaust (gasoline or propane): CO and combustion products — generator must be operated outside the van with exhaust directed away from operator; CO monitoring in bake space recommended. No particulate from baking process."
    physical_demand: "Moderate: repeated lifting of product trays and display equipment; sustained standing at market; van loading and unloading at each event. Physically more demanding than a fixed bakery due to the daily setup/breakdown cycle but less than a forge or smithing operation."

# ── REGULATORY NOTES ──────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "No fixed-site commercial zoning required; home kitchen requires residential-to-commercial licensing (cottage-food law or home-based food processor permit, jurisdiction-dependent); van parks at residential property; some jurisdictions require a licensed commissary kitchen as base of operations — verify local health-department rules before operating."
  emissions: "Generator exhaust is regulated by mobile-equipment noise and emissions rules; CO monitoring inside van required by OSHA-equivalent food-safety standards in some states; electric oven on shore power (at permitted events) eliminates generator emissions entirely."
  other: "Mobile food vendor license required (city/county, renew annually); health permit for mobile food unit (inspected annually in most US jurisdictions); commercial vehicle registration; farmers-market membership fee and/or booth fee (per-event or seasonal); cottage-food or home-kitchen license if pre-baking at home; food handler certification."

# ── CONTEXT FIT ───────────────────────────────────────────────────────────────

lens_fit:
  market: good
  cooperative: poor
  civic: poor

scale_fit:
  village: good
  town: marginal
  small_city: poor

# ── LENS CONTEXT ──────────────────────────────────────────────────────────────

# lens_context.cooperative and lens_context.civic are omitted: both are `poor`
# and no conditional block is triggered per catalog/SCHEMA.md §4 trigger rules.

# ── SIMULATION PARAMETERS ─────────────────────────────────────────────────────

sim_params:
  cost_mean: 38000
  cost_sd: 10000
  # cost_sd = (60,000 − 20,000) / 4 = 10,000. Within the 0.15–0.50 plausible
  # range: 10,000 / 38,000 = 0.263 ✓
  throughput_units_equiv_per_year: 7956
  # Event-based: 90 loaves/event × 2 events/wk × 52 wk × (1 − 0.15) = 7,956.
  # Hours cross-check: net 13 hr/wk × 52 × 0.85 × (90 loaves / 8 hr/day) =
  # 13 × 52 × 0.85 × 11.25 = 6,458. Discrepancy arises because throughput is
  # bounded by event-count capacity (3 batches × 30 loaves = 90/event) before
  # it is bounded by active hours; 7,956 is the binding event-count ceiling.
  # Hours formula represents a lower bound on utilisation; event formula is used.
  variable_cost_per_unit: 0.80
  # Per loaf-equivalent: flour ~$0.40 + salt/yeast/enrichments ~$0.20 +
  # packaging ~$0.15 + energy (generator fuel per loaf) ~$0.05 = $0.80.
  # Rounded; flour cost dominates. [CITATION-NEEDED: commodity bread-flour
  # warehouse price per kg × kg/loaf to confirm $0.40/loaf flour cost.]
  labor_hours_per_unit: 0.072
  # Net active hours / throughput: (13 hr/wk × 52 × 0.85) / 7,956 =
  # 574.6 / 7,956 ≈ 0.072 hr/loaf (~4.3 min/loaf). Cross-check:
  # 7,956 × 0.072 = 572.8 ≈ 574.6 ✓
  downtime_fraction: 0.15
  # Weather cancellations (~5% of scheduled market days), illness/personal
  # downtime (~4%), equipment failure weeks (~3%), low-season no-market weeks
  # (~3%). Total 0.15. Higher than a fixed bakery (no van/weather exposure)
  # but lower than forge-007 (simpler equipment, no CDL complexity).
  lifespan_years: 8
  # Van service life under commercial weekly use: 8–12 years typical.
  # Oven and generator could last longer; van is the binding asset. Using 8 as
  # the conservative base; actual horizon depends on van condition and
  # maintenance discipline.

# ── TRADE-SPECIFIC ────────────────────────────────────────────────────────────

trade_specific:
  flour_source_declaration: industrial-flour-purchased
  # Industrial flour purchased from warehouse distributor. At ~4,774 kg/yr this
  # volume is below the threshold at which a direct-mill relationship is
  # economically attractive; see Key Assumptions for sourcing rationale.

# ── RESULTS ───────────────────────────────────────────────────────────────────

results:
  village_market:
    verdict: marginal
    primary_metric: 0.8832512018758949
    metric_name: payback_years
    notes: wage_verdict=marginal (take_home=42613 vs median=48000)
  village_coop:
    verdict: fail
    primary_metric: 74.0
    metric_name: break_even_members
    notes: feasible_pool=31.2, break_even=74, total_annual_cost=14662
  village_civic:
    verdict: fail
    primary_metric: 21.9
    metric_name: per_household_cost
    notes: per_hh=21.90, threshold=120, hrs/capita=0.000 vs threshold=2.0
  town_market:
    verdict: fail
    primary_metric: 0.8832512018758949
    metric_name: payback_years
    notes: wage_verdict=fail (take_home=42613 vs median=56000)
  town_coop:
    verdict: win
    primary_metric: 74.0
    metric_name: break_even_members
    notes: feasible_pool=212.5, break_even=74, total_annual_cost=14662
  town_civic:
    verdict: fail
    primary_metric: 3.2205882352941178
    metric_name: per_household_cost
    notes: per_hh=3.22, threshold=100, hrs/capita=0.000 vs threshold=2.0
  small_city_market:
    verdict: fail
    primary_metric: 0.8832512018758949
    metric_name: payback_years
    notes: wage_verdict=fail (take_home=42613 vs median=62000)
  small_city_coop:
    verdict: win
    primary_metric: 74.0
    metric_name: break_even_members
    notes: feasible_pool=900.0, break_even=74, total_annual_cost=14662
  small_city_civic:
    verdict: fail
    primary_metric: 0.6083333333333333
    metric_name: per_household_cost
    notes: per_hh=0.61, threshold=80, hrs/capita=0.000 vs threshold=2.0
sources:
  - ref: "catalog/baking/SCHEMA.md v1.0 (schema_base_version 1.1, 2026-04-19). Baking throughput block structure, convection-electric energy-source definition, operator skill-floor definitions, first_year_failures reference list, Group A author guidance for bake-005."
  - ref: "catalog/SCHEMA.md v1.1 (2026-04-19). Base schema: all required fields, conditional triggers, validation rules, and sim_params cross-check conventions."
  - ref: "catalog/smithing/entries/007-containerized-mobile-forge.md (forge-007). Structural analog: mobile-route model, no floor-space rent, solo-operator succession risk framing, vehicle-as-primary-capital convention."
  - ref: "[CITATION-NEEDED: USDA AMS Farmers Market Metrics or comparable USDA farmers-market pricing report — primary citation for market_price_per_unit range $6–$14/loaf for artisan bread at US farmers markets. Required before promotion to reviewed.]"
  - ref: "[CITATION-NEEDED: USDA ERS retail bread price series — citation for industrial_baseline_price $3/loaf commodity grocery bread. See USDA Economic Research Service food price tracking.]"
  - ref: "[CITATION-NEEDED: mobile food vendor operating cost survey — citation for annual_maintenance $3,200 estimate. No single published study identified; figure extrapolated from mobile-food-truck operating cost literature (IBISWorld mobile food services reports circa 2023–2025) and adjusted for smaller van-scale operation.]"
  - ref: "[CITATION-NEEDED: commodity bread-flour warehouse price per kg — citation for variable_cost_per_unit $0.40/loaf flour component. Consistent with USDA ERS flour price data but entry-specific commercial-purchase price not confirmed.]"
  - ref: "[CITATION-NEEDED: small generator MTTF under commercial weekly load — citation for first_year_failures generator item, estimated_hours_to_failure 1,500 hr for residential-grade unit in commercial use. Manufacturer specs and repair-service data required.]"
  - ref: "[CITATION-NEEDED: farmers-market booth fee ranges — supporting context for regulatory_notes farmers-market membership cost; ranges vary widely by market ($25–$100/day or $200–$800/season for most US regional markets; USDA AMS 2023 market survey data cited as approximate source).]"
  - ref: "[CITATION-NEEDED: 19th-century travelling market baker precedent — secondary social history sources documenting itinerant bread sellers at rural markets and fairs in Britain and North America; no single consolidated academic source identified at time of authoring.]"
---
## Summary

Bake-005 is a solo mobile bakery: an operator who pre-bakes at home (or a licensed commissary kitchen) the night before a market event, then loads the product into a cargo van and sells direct at farmers markets, community events, and pop-up locations on a 2–3-day-per-week circuit. The defining characteristic is the elimination of the commercial lease: capital goes into the van, oven, and generator rather than a fixed premises, and floor-space rent is zero. The entry targets village and rural-town markets where a permanent storefront cannot be supported by the resident population alone but a twice-weekly market presence captures the dispersed artisan-bread demand in the catchment area. It is the baking analog to forge-007 (Containerized Mobile Forge): the production capacity goes to where the customers aggregate rather than waiting for customers to come to a fixed address. Unlike forge-007, the mobile baker pre-produces inventory before the event rather than performing custom work on-site; the van is a delivery and selling platform, not a production platform.

## Design rationale

No other entry in the baking catalog addresses the zero-commercial-lease mobile model. Bake-001 through bake-004 (stationary artisan bakeries at various scales) all require a permanent commercial premises with oven installation, ventilation, and a lease. For operators who cannot afford commercial-lease overhead or who serve a population base too thin to sustain a walk-in shopfront five or six days a week, the mobile model is the only configuration that brings artisan bread directly to the customer at the moment and place of demand. The design-space cell this entry occupies — convection-electric, van-mounted, direct-to-consumer, market-primary, no apprentice, industrial flour — has no competitor among the catalog entries. The key trade-off relative to stationary entries is throughput ceiling (90 loaves/event vs. 200+ for a stationary deck-oven bakery) in exchange for zero commercial rent, low capital, and geographic flexibility. The flour source (industrial-flour-purchased) is declared honestly rather than obscured: at this volume and with this capital profile, a supply-chain relationship with a local mill is not economically realistic; the premium pricing is earned by craft process and market experience, not by grain sourcing differentiation. That constraint must be acknowledged in Key Assumptions per Group A guidance in the baking SCHEMA.

## Historical lineage

Two functional precedents inform this design. The first is the 19th-century travelling market baker and itinerant confectionery seller who served rural fairs and periodic markets across Britain and North America. [CITATION-NEEDED: secondary social-history sources on itinerant bread and confectionery sellers at periodic rural markets; see REQUIREMENTS note on pre-industrial market-day supply forms.] These operators baked in a home or rented hearth the night before, loaded product onto a cart, and set up at market for the day. What this entry carries forward is the functional logic: the baker is an event-day seller, not a shop operator; inventory is pre-produced; the transport vehicle is the capital; and revenue is event-bounded. What it does not carry forward: the horse-drawn cart and the informal home-hearth permit environment are replaced by a cargo van, a commercial convection oven, and a formal mobile-food-vendor licensing regime. The informal credit-and-barter pricing of periodic market bread is replaced by a cash-and-card farmers-market pricing structure. The second functional precedent is the modern farmers-market artisan-food vendor, which has operated as a recognized commercial form in the United States since the USDA AMS farmers-market infrastructure buildout of the 1980s–2000s. [CITATION-NEEDED: USDA AMS historical farmers-market census data; number of farmers markets grew from ~1,755 in 1994 to ~8,600+ by 2019 per AMS tracking.] Modern mobile-bakery operators in this format represent a continuous functional lineage from the periodic-market baker: direct-to-consumer, event-based selling, pre-produced inventory, and pricing premiums that reflect craft differentiation over the industrial grocery alternative. The operational form is well-established enough to constitute evidence that the model works at small scale and does not require validation by simulation alone.

## Key assumptions

Capital-cost range ($20,000–$60,000, mid $38,000) covers three components: (1) van — used cargo van ($8,000–$25,000 depending on age and mileage); (2) baking equipment — commercial convection oven rated for 30+ loaves per load ($2,000–$8,000 new or $800–$3,000 used), generator ($600–$2,500 for a 3–5 kW unit), proofing trays and basic tools ($400–$800); (3) licensing and fit-out — interior shelving and tie-downs ($500–$1,500), mobile-food-vendor license + health permit + commissary arrangement ($300–$1,500 first year), commercial vehicle registration and insurance uplift ($500–$1,500/yr). [CITATION-NEEDED: commercial convection oven pricing and generator pricing at van-scale; van pricing is consistent with used cargo-van marketplace listings circa 2024–2025 but not verified against a formal commercial survey.] The mid figure ($38,000) represents a reliable but not new van with a refurbished commercial oven and a mid-size generator. The cost_mean skew: mid ($38,000) is close to the arithmetic mean of low and high ($40,000), with a slight downward asymmetry reflecting that capable operators can source a viable used van and oven below the midpoint with patience. cost_sd = (60,000 − 20,000) / 4 = 10,000 (ratio 0.263, within the 0.15–0.50 plausible range).

Throughput calculation: the entry uses an event-count-bounded formula rather than a pure hours formula because the convection oven capacity (3 batches × 30 loaves = 90 loaves/event) is the binding constraint before active hours are exhausted. Annual throughput: 90 loaves/event × 2 events/week × 52 weeks × (1 − 0.15 downtime) = 7,956 loaves/yr. Hours cross-check: net 13 hr/wk (16 hr/wk gross minus 90 min/day × 2 days overhead) × 52 × 0.85 × 11.25 loaves/hr = 6,458 loaves/yr. The event formula yields a higher figure because each market event delivers a full 90-loaf pre-baked inventory regardless of the precise active-hour count; the hours formula undercounts by treating all 8 hr/day as uniformly productive at the selling rate. The event formula is used in sim_params; the hours cross-check confirms the order of magnitude is consistent, and the discrepancy (7,956 vs. 6,458) is documented here per E-3 transparency requirements.

Flour source: industrial-flour-purchased from a warehouse or regional distributor. At 7,956 loaves/yr × ~600g flour/loaf = ~4,774 kg flour/yr ≈ ~10,500 lb/yr. This volume is below the threshold at which a direct-mill relationship is economically attractive to the mill partner; industrial wholesale purchase is the realistic supply option. Flour cost: ~$0.40/loaf (800g loaf at ~$0.50/kg commodity bread flour [CITATION-NEEDED]). The lack of a local-mill sourcing story means the premium pricing must be justified on craft-process and customer-experience grounds alone, not on grain provenance. This is acknowledged as a pricing vulnerability: if a direct competitor in the same market can credibly claim local grain and match the craft quality, the premium position is eroded.

Floor-space rent: $0 for the commercial-lease line, reflecting the no-fixed-premises model. In jurisdictions that require a licensed commissary kitchen as the base of operations for mobile food vendors, an additional $2,400–$6,000/yr in shared-kitchen rental should be added to the cost model before simulation. This entry uses the home-kitchen licensing assumption (cottage-food law or equivalent) as the base case; the commissary-required scenario is the high-risk variant and should be modeled separately if the operator's jurisdiction mandates it.

## Known risks / failure modes

**Regulatory.** The primary regulatory risk is jurisdictional variation in mobile-food-vendor and home-kitchen licensing. Many US states permit home-based commercial baking under cottage-food laws but with gross revenue caps (often $25,000–$50,000/yr) or product-category restrictions (some jurisdictions exclude yeast-leavened bread from cottage-food exemption, requiring a licensed commercial kitchen). An operator who crosses the revenue threshold mid-season or who discovers their jurisdiction requires a commissary kitchen faces an immediate compliance event: either limit sales (forfeit revenue) or secure a commissary arrangement quickly (add $2,400–$6,000/yr fixed cost). A second regulatory risk is the farmers-market membership and booth-fee structure: popular markets in urban-adjacent areas have waitlists for vendor slots; a new mobile bakery cannot simply appear at any market without applying months in advance. Rural and village markets are more accessible but have lower foot traffic. The mobile-food-vendor license must be renewed annually and may require a re-inspection; failing inspection during a peak season is a revenue event.

**Labour pipeline.** The single-operator solo model has the same succession risk as forge-007: no apprentice, no backup operator, and no institutional continuity. If the operator is ill, injured, or exits, all revenue ceases immediately. Unlike a fixed bakery where a hired journeyman can run a single market day, the mobile model's integration of driving, baking, and selling in one person makes substitution harder than for a stationary shop. The operator's combined skill set — journeyman baker AND commercial driver AND direct sales AND business administration — is narrow. The `apprentice_friendly: false` status is documented here as required by schema and Principle 9: this entry has no built-in succession mechanism. Any operator planning a multi-year operation should either develop a second-operator arrangement (a partner who shares driving and selling duties on alternate market days) or document a transition-toward-fixed-premises plan when revenue justifies a commercial lease.

**Supply chain.** Industrial flour from a warehouse distributor is available from multiple suppliers in most North American markets, but the volume (approximately 4,800 kg/yr) is too small to justify a long-term supply contract with price protection. Commodity flour prices are volatile and tied to wheat spot markets; a 30% flour-price increase would raise variable_cost_per_unit from $0.80 to approximately $0.92, compressing the $9/loaf mid-price margin materially. The mitigation is a 2–3 week flour reserve (low-cost given warehouse pricing) and flexibility to pass flour-cost increases through to market pricing, which farmers-market customers have historically tolerated for craft bread. Generator fuel (gasoline or propane) is a secondary supply dependency; disruption is short-term (refuel from any retail station) but a generator failure on a market morning with a full pre-baked inventory already loaded is a total revenue loss for that event — the income from the pre-baked loaves cannot be recovered if they cannot be transported and sold in time (day-old artisan bread sells at a steep discount or must be donated/disposed).

## Iteration log

- 2026-04-18: v0.1 — initial entry authored per Plan G Task 7. Van-based mobile convection-electric model, 2 market days/week, industrial-flour-purchased, solo operator, market-primary lens. Throughput event-count formula used and reconciled with hours cross-check in Key Assumptions. Cooperative and civic lenses omitted (both poor). Succession risk named explicitly per apprentice_friendly: false requirement. Regulatory cottage-food-law jurisdictional risk named as primary risk. forge-007 cited as structural analog. No docs/superpowers/ paths used.
