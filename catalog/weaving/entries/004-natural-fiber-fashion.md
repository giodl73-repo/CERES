---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: weave-004
trade: weaving
name: "Natural Fiber Fashion Atelier"
tagline: "Weaver-as-designer DTC studio producing handwoven garment fabric for slow-fashion retail and boutique wholesale"
status: draft
version: 0.1
supersedes: null
inspirations:
  - mid-century-studio-weaving-movement
  - japanese-tsumugi-silk-weaver-designer
  - scandinavian-handweaving-guild-tradition

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 40
ceiling_min_m: 2.7
ventilation: natural-sufficient

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: electric-lighting-only
energy_consumption_per_active_hour: "1.5 kWh (studio lighting + humidity management)"
backup_fuel: null

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  meters_per_day: 3.5
  warp_width_cm: 110
  pattern_complexity: twill
  max_active_hours_per_week: 35
  product_mix:
    yardage: 55
    rugs_upholstery: 0
    tapestry_art: 0
    garments_accessories: 35
    instruction_open_studio: 10
  throughput_variance:
    seasonal: "Holiday gift season (Oct-Dec) provides retail peak; Jan-Feb trough; commission work moderates variance year-round."
    worst_month_fraction_of_average: 0.60
    best_month_fraction_of_average: 1.45

# ── TRADE-SPECIFIC ───────────────────────────────────────────────────────────

trade_specific:
  loom_type: floor-loom-4shaft
  humidity_control_required: true
  fiber_source_declaration: industrial-yarn-purchased

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: master-weaver
operators_concurrent: "1-2"
apprentice_friendly: true
apprentice_path:
  training_stages: "Stage 1 (0-6 mo): loom mechanics, warping, plain weave and basic twill on studio equipment under supervision. Stage 2 (6-18 mo): independent yardage production, garment-cloth finishing, basic pattern drafting; journeyman gate at 18 months. Stage 3 (18-36 mo): design development, customer communication, DTC channel management, wholesale sample preparation; independent operation gate at 36 months."
  time_to_independent_operation: "~36 months to journeyman standard capable of independent yardage production; master-tier design work requires additional 2-4 years of post-journeyman practice"
  succession_note: "Apprentice co-presence during production sessions integrates skill transfer into normal operations; design mentorship requires master-weaver availability for critique and client-facing practice"

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD
  capital_cost: { low: 15000, mid: 30000, high: 55000 }
  install_cost: 3500
  annual_maintenance: 2200
  annual_consumables: 8500
  floor_space_rent_per_year: 9600
  market_price_per_unit: { low: 80, mid: 200, high: 500 }
  industrial_baseline_price: 10
  pricing_notes: "Per meter of woven garment-grade fabric (110 cm width). Premium over industrial-imported woven fabric baseline ($10/m for standard shirting or dress fabric at wholesale) is supported by hand-weaving provenance, custom colorway, and slow-fashion DTC positioning. Low end ($80/m) represents twill-weave cotton or linen to boutique wholesale; mid ($200/m) represents wool or silk-blend twill to DTC or curated retail; high ($500/m) represents complex-twill or hand-dyed silk to high-end DTC or designer collaboration. Customer segment: slow-fashion consumers, independent garment designers, and boutiques with provenance-sourcing mandates."
  pricing_validation: "Market price evidence: Etsy and independent artisan-weaver studio rate cards (2024-2025) for garment yardage; comparable operator financials from Handweavers Guild of America member surveys (2023); Textile Society of America marketplace pricing documentation for handwoven cloth. Evidence type is comparable-sales and operator-financial — not cost-plus. [CITATION-NEEDED: Handweavers Guild 2023 survey; TSA marketplace data]"

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:
  first_year_failures:
    - item: "Warp beam ratchet / pawl wear"
      estimated_hours_to_failure: 2000
      replacement_cost: 180
      replacement_lead_time_days: 10
      serviceable_by: journeyman
    - item: "Treadle tie-up cord wear or breakage"
      estimated_hours_to_failure: 1200
      replacement_cost: 25
      replacement_lead_time_days: 2
      serviceable_by: operator
    - item: "Climate-control / humidifier failure"
      estimated_hours_to_failure: 2500
      replacement_cost: 450
      replacement_lead_time_days: 7
      serviceable_by: journeyman
    - item: "Heddle breakage (texsolv)"
      estimated_hours_to_failure: 800
      replacement_cost: 60
      replacement_lead_time_days: 5
      serviceable_by: operator

  maintenance_schedule:
    daily:
      task: "Check warp tension, clear shed of lint and broken ends, log meters woven and any defect incidents"
      performed_by: operator
    weekly:
      task: "Inspect treadle tie-ups and lam cords; check humidity sensor readings; clean reed dents with soft brush; wind yarn bobbins or shuttles for next warp"
      performed_by: operator
    quarterly:
      task: "Inspect ratchet-and-pawl beam tensioning; oil moving joints; check brake band condition; verify humidifier reservoir and filter"
      performed_by: journeyman
    annual:
      task: "Full loom inspection: castle bolts, beam bearings, treadle pivot points; replace worn heddles in bulk; recalibrate humidity sensor; service HVAC or standalone humidifier unit"
      performed_by: specialist

  startup_shutdown_overhead_per_day_min: 25
  max_active_hours_realism_note: "35 hr/wk is the theoretical active-weaving ceiling for a full-time studio weaver; warping and loom-dressing consume an additional 4-8 hr per warp change (typically every 2-4 weeks), which is excluded from max_active_hours_per_week but included in the 240 annual operating-day estimate. Net of 25 min/day startup-shutdown overhead (5-day week), effective loom time ~32.9 hr/wk. sim_params.throughput_units_equiv_per_year uses the 240-day × 3.5 m/day base rate derated by downtime_fraction."
  interruption_notes: "DTC channel management (email, social media, order fulfillment) consumes 5-10 hr/wk and is not reflected in max_active_hours_per_week, which counts loom time only. Authors using this entry for realistic financial modelling should add 0.5-1.0 FTE administrative burden or treat DTC as a part-time operator contribution."
  consumables_lead_time_days: { typical: 7, worst: 45 }
  throughput_variance:
    seasonal: "Holiday gift season (Oct-Dec) provides retail peak; Jan-Feb trough; commission work moderates variance year-round."
    worst_month_fraction_of_average: 0.60
    best_month_fraction_of_average: 1.45

  operator_impact:
    noise_db: 62
    heat_exposure: "Ambient studio temperature; no heat hazard from weaving equipment; climate-control system may generate localized warm airflow"
    emissions: "Near-zero; no combustion; lint and fine fiber particles in studio air require routine ventilation; no regulatory emissions threshold triggered"
    physical_demand: "Moderate sustained seated posture; repetitive treadle motion and shuttle throwing; ergonomic risk for wrist and shoulder with sustained production pace; standing during warping and finishing"

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Light commercial, live-work, or mixed-use zoning sufficient; no industrial zoning required; DTC retail activity may trigger home-occupation or retail-permit requirements depending on jurisdiction"
  emissions: "No emissions permit required; fine fiber particulate is below regulatory thresholds for this studio scale; standard building ventilation adequate"
  other: "Boutique wholesale may require seller's permit and resale license; DTC e-commerce requires standard business registration; no weaving-specific occupational license in most jurisdictions"

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
    membership_boundary: "Practicing weavers and fiber artists in the small-city metro area; membership by annual dues plus portfolio review to ensure minimum journeyman-weaver competence; production slots not available to rigid-heddle-novice members"
    rules_source: "Bylaws; member vote to amend at semi-annual meeting with 2/3 majority"
    monitoring: "Loom usage logged per session via sign-in book; shared humidifier and climate system maintenance logged weekly; monthly review by rotating steward"
    graduated_sanctions: "Verbal reminder → written warning → 30-day loom-access suspension → membership review and potential termination"
    conflict_resolution: "Elected steward mediates scheduling and equipment disputes; appeal to full member vote at next semi-annual meeting"
    ostrom_principles_addressed: [1, 2, 3, 4, 5, 6]
    member_amendment_process: "2/3 vote at semi-annual general meeting; 21-day advance notice required; emergency bylaw change requires 3/4 vote with 7-day notice"
    legal_form: "State-registered worker cooperative or LLC; cooperative form preferred to enable member equity and profit-sharing from shared-brand sales"
    scale_fit_note: "Rules calibrated for small-city scale with 6-12 active members sharing 2-3 floor looms; governance infeasible at village scale where member pool cannot sustain quorum or shared equipment utilization"

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 30000
  cost_sd: 10000
  throughput_units_equiv_per_year: 714
  variable_cost_per_unit: 28.50
  labor_hours_per_unit: 2.17
  downtime_fraction: 0.15
  lifespan_years: 20

# ── RESULTS ──────────────────────────────────────────────────────────────────

results:
  village_market:
    verdict: win
    primary_metric: 0.3998407798208116
    metric_name: payback_years
    notes: ''
  village_coop:
    verdict: fail
    primary_metric: 110.0
    metric_name: break_even_members
    notes: feasible_pool=31.2, break_even=110, total_annual_cost=21975
  village_civic:
    verdict: fail
    primary_metric: 23.633333333333333
    metric_name: per_household_cost
    notes: per_hh=23.63, threshold=120, hrs/capita=0.000 vs threshold=2.0
  town_market:
    verdict: win
    primary_metric: 0.3998407798208116
    metric_name: payback_years
    notes: ''
  town_coop:
    verdict: win
    primary_metric: 110.0
    metric_name: break_even_members
    notes: feasible_pool=212.5, break_even=110, total_annual_cost=21975
  town_civic:
    verdict: fail
    primary_metric: 3.475490196078431
    metric_name: per_household_cost
    notes: per_hh=3.48, threshold=100, hrs/capita=0.000 vs threshold=2.0
  small_city_market:
    verdict: win
    primary_metric: 0.3998407798208116
    metric_name: payback_years
    notes: ''
  small_city_coop:
    verdict: win
    primary_metric: 110.0
    metric_name: break_even_members
    notes: feasible_pool=900.0, break_even=110, total_annual_cost=21975
  small_city_civic:
    verdict: fail
    primary_metric: 0.6564814814814814
    metric_name: per_household_cost
    notes: per_hh=0.66, threshold=80, hrs/capita=0.000 vs threshold=2.0
sources:
  - ref: "Handweavers Guild of America, Member Studio Survey 2023 — income and pricing data for professional studio weavers [CITATION-NEEDED: confirm publication and access]"
  - ref: "Textile Society of America, Marketplace Pricing Documentation 2024 — handwoven cloth per-meter rates [CITATION-NEEDED: confirm publication and access]"
  - ref: "Interweave Press / Long Thread Media, The Weaver's Companion (2nd ed., 2012) — loom setup times, throughput benchmarks, and studio-planning guidance"
  - ref: "Ashford Wheels & Looms, dealer price list 2024 — floor-loom-4shaft capital cost range [CITATION-NEEDED: current pricing confirmation]"
  - ref: "Leclerc Looms, dealer price list 2024 — floor-loom-4shaft capital cost range upper bound [CITATION-NEEDED: current pricing confirmation]"
  - ref: "US Bureau of Labor Statistics, Occupational Employment Statistics 2024 — textile and apparel workers wage baseline for variable cost per unit estimate"
  - ref: "research/trades/weaving/REQUIREMENTS.md — throughput ranges, loom capability, operator skill definitions, footprint guidance"
  - ref: "research/trades/weaving/DECLINE-VERDICT.md — niche targeting guidance; fiber-sourcing falsifier; commodity-cloth exclusion criteria"
---
## Summary

The Natural Fiber Fashion Atelier (weave-004) is a single-operator or two-person DTC studio in which a master-weaver functions simultaneously as designer, producer, and brand. The output is handwoven garment-grade fabric — primarily twill-structure cloth in wool, silk, or fine-linen colorways — sold directly to consumers via studio sales and e-commerce, or wholesale to boutiques with verified provenance-sourcing policies. This entry is distinct from weave-001 (Tapestry Atelier, art-object output) and weave-003 (Architectural Textile Studio, large-format B2B output): it addresses the gap between those specialties and the commodity-yardage sector. Its economic viability depends entirely on the weaver's ability to build and maintain a direct customer relationship that supports a 20-40x premium over imported industrial cloth.

## Design rationale

No other entry in the weaving catalog addresses the weaver-as-fashion-designer model, in which the producer controls the full value chain from warp design to finished yardage sale. The cooperative entries (weave-009 through weave-013) are shared-access models; the architectural entry (weave-003) targets commercial specifiers; the tapestry entry (weave-001) produces art objects, not garment cloth. This entry fills the slow-fashion retail niche: a market that has grown substantially since approximately 2015 but which remains poorly served by artisan catalogues that conflate "handwoven" with either tapestry art or commodity utility cloth. The challenge for this entry — and its primary design-rationale claim — is that premium garment-fabric pricing is fragile: fashion markets are volatile, boutique wholesale channels concentrate power in buyers, and DTC requires sustained brand-building effort that does not reduce to weaving skill. These risks must be modelled, not suppressed.

## Historical lineage

Three functional precedents inform this design. First, the mid-twentieth-century studio weaving movement in North America and Western Europe (1940s-1970s), in which trained fine-arts weavers established independent studios producing custom yardage and domestic textiles for an emerging educated-consumer market. The functional inheritance is the DTC pricing model and the weaver-as-designer identity; the studio movement collapsed partly when its customer base moved to cheap imported synthetics in the 1970s, a failure mode directly relevant to the fragile-premium risk in this entry. Second, Japanese tsumugi silk weaving (particularly Yuki-tsumugi and Oshima-tsumugi traditions), in which individual or household-scale weavers produce premium silk fabric for kimono and high-fashion designers under a certified-provenance model. The functional inheritance is the premium-per-meter pricing structure, the direct-to-craftsperson sales channel, and the role of regional-origin certification in sustaining price premiums over imported silk; the labor regime (near-subsistence rural household production supported by regional guild infrastructure and government cultural preservation subsidy) cannot be reproduced in a contemporary Western small-city context and is explicitly not carried forward. Third, Scandinavian handweaving guild traditions (particularly Swedish and Norwegian guild-certified studio weavers, late nineteenth to mid-twentieth century), which developed standardized quality certification and pattern-licensing systems to support artisan weaver pricing against industrial competitors. The functional inheritance is the role of shared standards and identifiable design vocabulary in supporting premium pricing; the guild infrastructure that enforced those standards is absent from the contemporary context and must be partially substituted by DTC brand-building and customer education.

## Key assumptions

Capital cost range ($15,000-$55,000) is derived from dealer price lists for 4-shaft floor looms (Ashford, Schacht, Leclerc) plus warping board, bobbin winder, yarn winder, and basic cutting/sewing equipment for finished-goods production. Low end assumes a used loom in good condition; high end assumes two new looms plus full sewing kit. Install cost ($3,500) covers electrical for studio lighting and humidity management, minor built-environment modifications (loom-weight floor reinforcement if needed), and initial setup labor. Annual consumables ($8,500) assume approximately $7,000 in yarn purchases (wool, silk, fine linen at commercial wholesale rates) for ~714 m/year production plus $1,500 in warp-related materials (sizing, finishing agents). Variable cost per unit ($28.50/m) derives from yarn cost ($7,000 / 714 m ≈ $9.80/m yarn) plus finishing and packaging ($3.20/m) plus energy and supplies ($1.50/m) plus estimated downtime-adjusted labor overhead ($14/m at imputed $18/hr); this is not the full operator compensation — it is the direct variable cost for the simulation. Annual maintenance ($2,200) covers loom servicing, humidity-system maintenance, and heddle/tie-up replacement on a normal wear schedule. Throughput (714 m/year) is derived from 3.5 m/day × 240 operating days × (1 - 0.15 downtime); 240 operating days accounts for warping setup days (approximately 20-25 days/year not spent weaving), holidays, and scheduled maintenance. The 3.5 m/day central estimate for twill-complexity fabric on a 4-shaft floor loom is conservative relative to plain weave but realistic for garment-quality twill with color management. Market price range ($80-$500/m) is sourced from comparable-sales data from Handweavers Guild member surveys and textile marketplace observations; the mid-point ($200/m) is the central simulation price. Industrial baseline ($10/m) reflects imported plain-weave or twill shirting fabric at wholesale, a directly competitive substitute for buyers not committed to the artisan premium. The premium (20x at mid) is large; it is sustained only by a direct customer relationship, brand recognition, and provenance transparency — inputs that are real but not guaranteed.

## Known risks / failure modes

**Regulatory.** DTC retail activity from a studio may trigger home-occupation permit requirements, retail seller's permits, or zoning compliance reviews in jurisdictions that restrict commercial activity in residential or light-commercial zones. Boutique wholesale adds sales-tax compliance complexity in multi-state e-commerce contexts. These are manageable but require proactive attention in the first year; failure to register appropriately can result in retroactive fines or forced relocation.

**Labour pipeline.** This entry requires a master-weaver at the operator position — a skill level that requires a minimum of 8-12 years of practice beyond initial training and is not achievable on an apprentice timeline within the studio's first operating cycle. The apprentice path (Stage 1-3, ~36 months to journeyman standard) addresses succession and can eventually produce a capable production weaver, but the founding operator must already be at master level. If the founding weaver exits, the studio's design identity — which is inseparable from the weaver's personal aesthetic vocabulary — does not automatically transfer to a successor. This is a structural succession risk that the apprentice_path does not fully mitigate; it is acknowledged here per Principle 9.

**Supply chain.** Yarn sourcing depends on commercial wholesale suppliers for fine wool, silk, and linen. Specialty silk and fine-merino wool have longer lead times and higher price volatility than commodity cotton or synthetic yarn; a disruption to a primary supplier can cause production gaps of 3-8 weeks. The consumables_lead_time_days worst-case value (45 days) reflects silk import lead times from primary suppliers. Maintaining a 2-3 month yarn inventory buffer is the primary mitigation; this requires working-capital discipline and storage space beyond the core studio footprint.

**Market fragility.** Fashion markets are fickle; slow-fashion as a consumer category emerged as a distinct marketing identity in the 2010s and has not been stress-tested through a sustained consumer-spending recession. A weaver who builds a brand on slow-fashion positioning and premium pricing is exposed to a category correction if the slow-fashion premium collapses. Inventory risk is real: fabric woven to a specific colorway or fiber combination that fails to sell becomes a write-off at near-zero liquidation value. DTC and boutique wholesale have substantially different margin structures: boutique wholesale typically requires 50% margin to the retailer, effectively doubling the required ex-factory price to achieve the same net revenue. Authors using this entry should model DTC and wholesale scenarios separately.

## Iteration log

- 2026-04-18: v0.1 — initial creation for Plan I task 6. Entry authored per SCHEMA.md v1.1 and catalog/weaving/SCHEMA.md v1.0. Capital, throughput, and variable-cost figures are draft estimates pending citation confirmation on Handweavers Guild survey data and current loom dealer pricing. Market price evidence flagged [CITATION-NEEDED] on two primary sources. Anti-romanticism note on "slow fashion" branding as contemporary marketing category, not historical tradition, included in Design Rationale and Historical Lineage. Throughput arithmetic: 3.5 m/day × 240 days × 0.85 = 714 m/yr; labor check: 714 × 2.17 = 1549 hr ≈ 35 hr/wk × 52 × 0.85 = 1547 hr (consistent to within rounding).
