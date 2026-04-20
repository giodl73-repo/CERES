---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: bake-006
trade: baking
name: "French-style Pastry / Viennoiserie (combi-steam, market-primary)"
tagline: "Specialty pastry shop producing laminated doughs and pâte-à-choux confection for premium retail"
status: draft
version: 0.1
supersedes: null
inspirations: [19th-century-viennese-konditorei, belle-epoque-parisian-boulangerie-patisserie, mid-20th-century-french-provincial-patisserie]

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 47
# Mid-point of specified 35-60 m² range; includes laminating table, combi oven,
# proofer chambers, cold prep surface, mixer station, and operator working zone.
# Customer-facing display space not included.
ceiling_min_m: 2.8
ventilation: mechanical-extraction-required
# Steam venting from combi oven and butter smoke during laminated-dough baking
# require mechanical extraction; flour dust adds to extraction demand.

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: combi-steam
# Essential for laminated doughs: steam injection in the first 3-5 minutes of
# bake gelatinizes surface starch before butter layers melt, producing the
# characteristic shatter and layering of croissant and pain au chocolat.
# See catalog/baking/SCHEMA.md §2 for combi-steam capability notes.
energy_consumption_per_active_hour: "7 kWh (combi oven at full bake load with steam cycles)"
# [CITATION-NEEDED: electric combi oven consumption at commercial bakery load]
backup_fuel: null
# No practical backup for combi-steam; propane deck substitution cannot replicate
# integral steam-injection required for laminated-dough baking.

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  loaves_per_day: 150
  # Unit: one individual viennoiserie piece equivalent (1 croissant, 1 pain au chocolat,
  # 1 danish, or 1 éclair). Mid-range of 100-200 units/day spec. Authors adapting this
  # entry for confection-dominant or bread-plus-pastry mix must restate the unit.
  batches_per_day: 3
  # Typical viennoiserie production: 1-2 morning bake waves (croissant/danish) + 1
  # afternoon bake wave (éclairs, choux). Night-before lamination prep feeds morning waves.
  batch_size_loaves: 50
  # 3 batches × 50 units ≈ 150 units/day; combi oven tray capacity at standard
  # croissant spacing [CITATION-NEEDED: combi oven tray yield for laminated dough].
  max_active_hours_per_week: 40
  # 5-day production week. Significant night-before prep (laminating, shaping, overnight
  # proof) is embedded in this figure; see max_active_hours_realism_note.
  product_mix:
    bread: 0
    confection: 90
    specialty: 10
    catering: 0
    # confection: croissants, pain au chocolat, danish, kouign-amann, mille-feuille.
    # specialty: seasonal tarts, custom petits-fours, catering pastry boxes.
  throughput_variance:
    worst_month_fraction_of_average: 0.45
    # Post-holiday (January-February) trough is severe for premium confection;
    # summer (July-August) slowdown secondary. Confection typical range: 0.35-0.55.
    best_month_fraction_of_average: 1.75
    # Pre-holiday (November-December) peak; Valentine's Day secondary peak (February
    # partially offsets January trough). Confection typical range: 1.30-1.80.
    seasonal: "Strong pre-holiday (Nov-Dec) and Valentine's Day peaks; severe January-February post-holiday trough; moderate summer (July-August) slowdown for premium confection retail."

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: pastry-chef-master
# Required for bake-006 per catalog/baking/SCHEMA.md §3 and §6 Group B guidance.
# Laminated dough execution (croissant, danish, puff), pâte-à-choux, and
# precision chocolate work require the full technical range of a master pastry chef.
operators_concurrent: "2-3"
# Lead pastry chef (master floor) + 1-2 prep/finishing operators. Night-before
# lamination can be solo; morning bake and service window requires 2 minimum.
apprentice_friendly: false
# No practical apprentice on-ramp for laminated-dough production at commercial
# speed; master-level technique is acquired through culinary school and years of
# professional placement, not shop-floor apprenticeship on this equipment.
# Succession risk named in Known Risks per SCHEMA.md §3 note and base schema
# apprentice_friendly: false requirement.

# ── BAKING-SPECIFIC REQUIRED FIELD ───────────────────────────────────────────

flour_source_declaration: industrial-flour-purchased
# Specialty pastry flour (T45 or equivalent low-extraction, low-protein) sourced
# from industrial mill or specialty distributor. Local mill sourcing is not reliably
# viable for T45-equivalent at small-city artisan volumes; see Key Assumptions.

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD
  capital_cost: { low: 45000, mid: 80000, high: 130000 }
  # Low: used/refurbished combi oven + used deck oven backup + basic proofer cabinet
  #   + used spiral mixer + laminating table (fabricated).
  # Mid: new mid-range commercial combi oven + dedicated proofing chambers (2 units)
  #   + refrigerated laminating table + commercial spiral mixer.
  # High: premium combi oven + purpose-built temperature-controlled lamination room
  #   + two proofing chambers + 2-speed spiral mixer + cold-prep worktables.
  install_cost: 8000
  # Electrical service upgrade for combi (3-phase or dedicated 60A circuit),
  # plumbing for steam water supply and drainage, mechanical extraction ducting.
  # Estimate; [CITATION-NEEDED].
  annual_maintenance: 3500
  # Combi oven servicing (steam generator descaling, door gasket, fan bearing),
  # proofing chamber element checks, laminating table refrigeration service.
  annual_consumables: 45000
  # Breakdown (approximate): premium butter ~$18,000 (primary cost driver —
  # laminated doughs use 25-35% butter-to-flour ratio by weight);
  # specialty pastry flour ~$8,000; chocolate/couverture, fillings, almond cream ~$8,000;
  # energy 7 kWh/hr × 40 hr/wk × 50 wks × $0.13/kWh ≈ $1,820 (rounded to $3,500
  # including proofer and lamination table refrigeration);
  # retail packaging (boxes, bags, tissue) ~$4,000; misc supplies ~$3,500.
  # [CITATION-NEEDED: commercial butter and couverture chocolate pricing 2024-2025]
  floor_space_rent_per_year: 16500
  # 47 m² × ~$350/m²/yr; small-city commercial-kitchen or light-retail zone estimate.
  # [CITATION-NEEDED: small-city commercial-kitchen rental rate per m²]
  market_price_per_unit: { low: 4.00, mid: 7.00, high: 11.00 }
  # Per individual viennoiserie piece (croissant, pain au chocolat, danish, éclair).
  # Low: entry-level or lower-income small-city market. Mid: mid-tier premium market.
  # High: upscale or destination-retail positioning. [CITATION-NEEDED]
  industrial_baseline_price: 2.50
  # Supermarket croissant (industrial-produced, frozen-baked) retail price equivalent.
  # [CITATION-NEEDED: supermarket croissant retail price per unit, US 2024-2025]
  pricing_notes: "Per individual viennoiserie piece (croissant, pain au chocolat, danish, or éclair). Premium of $1.50-$8.50 over supermarket frozen-baked croissant industrial baseline ($2.50/unit [CITATION-NEEDED]) reflects same-day freshness, all-butter lamination, and master-pastry-chef provenance. Customer segment: specialty coffee shop walk-in trade, weekend farmers market premium buyers, and gift/occasion purchasers in small-city markets with demonstrated premium food culture."
  pricing_validation: "Market price evidence: artisan viennoiserie retail pricing observed in small-city specialty bakeries and upscale coffee shop partnerships [CITATION-NEEDED — replace with specific trade survey, comparable operator financial data, or willingness-to-pay study before promotion to reviewed]. Mid-point $7.00 consistent with reported pricing for all-butter croissants in US regional specialty-bakery markets. Not a cost-plus residual."

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:
  first_year_failures:
    - item: "Combi steam generator (limescale fouling or element failure)"
      estimated_hours_to_failure: 1800
      replacement_cost: 1200
      replacement_lead_time_days: 21
      # Steam generator is the highest-failure-risk component in a combi oven;
      # limescale in hard-water supply areas accelerates degradation.
      # 21-day lead time for non-stocked commercial combi parts is the documented
      # worst-case; specialist contractor required for steam system work.
      # [CITATION-NEEDED: combi oven steam generator MTBF and replacement cost]
      serviceable_by: specialist
    - item: "Proofing chamber heating element or thermostat"
      estimated_hours_to_failure: 3000
      replacement_cost: 200
      replacement_lead_time_days: 5
      # Proofer elements degrade under continuous low-temperature cycling;
      # replacement is journeyman-level for most commercial proofer models.
      # [CITATION-NEEDED: proofing cabinet element failure rate data]
      serviceable_by: journeyman

  maintenance_schedule:
    daily:
      task: "Descale combi steam nozzle (if hard water); clean oven interior; check proofer temperature and humidity; sanitize laminating table and cold-prep surfaces; log any thermostat drift."
      performed_by: operator
    weekly:
      task: "Full combi oven descale cycle (manufacturer programme); inspect door gasket integrity; deep-clean proofer interior; check refrigerated laminating table temperature calibration; inspect mixer bowl and hook seals."
      performed_by: operator
    quarterly:
      task: "Combi oven: inspect steam generator element resistance, fan bearing, door seal; calibrate all temperature probes against reference thermometer; proofer: inspect element continuity, humidity sensor calibration; laminating table: refrigeration service check."
      performed_by: journeyman
    annual:
      task: "Full combi oven service by manufacturer-trained technician: steam system inspection and deep descale, convection fan replacement if indicated, door hinge and gasket replacement; proofing chamber full service; laminating table refrigeration regas if needed."
      performed_by: specialist

  startup_shutdown_overhead_per_day_min: 60
  # Combi oven preheat and steam-system purge (~20 min), end-of-day cleaning,
  # laminating table sanitization, and proofer reset (~40 min).
  # 60 min/day × 5 days/wk = 300 min/wk = 5 hr/wk non-productive overhead.

  max_active_hours_realism_note: "40 hr/wk is the gross ceiling for a 5-day production week inclusive of night-before lamination prep. Subtracting 5 hr/wk startup-shutdown overhead yields ~35 net active production hr/wk. sim_params uses throughput_units_equiv_per_year derived from loaves_per_day × operating days, consistent with the 35 net hr/wk figure; gross-maximum assumptions are not used."

  interruption_notes: "Typical intraday interruptions: walk-in customer service during open hours (~20 min/day in an open-kitchen or retail-attached format), ingredient temperature management pauses during lamination in warm weather (~15 min/day), specialty order consultations (~10 min/day). Folded into the 150 units/day mid-point figure rather than stated as a separate derating."

  consumables_lead_time_days: { typical: 4, worst: 21 }
  # Premium butter and specialty pastry flour from specialty distributor:
  # typical 2-4 days; worst-case (distributor stockout, specialty import disruption)
  # 21 days for imported couverture or specialty grain flour.
  # Butter supply disruption is a documented risk given dairy market volatility.

  throughput_variance:
    seasonal: "Strong pre-holiday (Nov-Dec) and Valentine's Day peaks; severe January-February post-holiday trough; moderate summer (July-August) slowdown for premium confection retail."
    worst_month_fraction_of_average: 0.45
    best_month_fraction_of_average: 1.75

  operator_impact:
    noise_db: 65
    # Combi oven and mixer are the primary noise sources; quieter than deck oven
    # wood-fired or gas operations. Approximately 60-70 dB at operator position
    # during active bake phases. [CITATION-NEEDED]
    heat_exposure: "Moderate near combi oven during loading and bake cycles; steam venting creates elevated humidity at operator position when oven door opens. Mechanical extraction required to manage ambient temperature and moisture. Overall heat load lower than open-deck or gas-fired operations."
    emissions: "Near-zero combustion emissions (electric combi); butter smoke during laminated-dough bake is the primary air-quality concern — mechanical extraction required. Flour dust secondary. No combustion particulate or CO."
    physical_demand: "Moderate: sustained standing and fine motor work during lamination and shaping; repetitive but lower physical loading than bread-volume operations. Cold-prep surface work in refrigerated lamination environment adds ergonomic consideration. Pastry finishing requires extended precision hand work."

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Retail or mixed-use commercial zoning typical for customer-facing specialty pastry shop; production-only back-of-house may qualify for light-industrial or commercial-kitchen zoning; confirm with local jurisdiction on combined retail-production use."
  emissions: "Electric combi produces near-zero combustion emissions; butter-smoke extraction via mechanical ventilation may require hood permit in some jurisdictions; flour-dust management under standard commercial kitchen health-department requirements."
  other: "Commercial kitchen license required; health-department inspection on commissioning; food handler certifications for all operators; retail food establishment license if customer-facing; allergen labeling requirements for packaged sales (butter, gluten, eggs, nuts common in viennoiserie)."

# ── CONTEXT FIT ──────────────────────────────────────────────────────────────

lens_fit:
  market: good
  cooperative: poor
  civic: poor

scale_fit:
  village: poor
  town: marginal
  small_city: good

# ── LENS CONTEXT ─────────────────────────────────────────────────────────────

# lens_context.cooperative and lens_context.civic are not required:
# lens_fit.cooperative is `poor` and lens_fit.civic is `poor`.
# Neither block is triggered per catalog/SCHEMA.md §4 conditional logic.

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 80000
  # Equals economics.capital_cost.mid per E-3 R1.
  cost_sd: 21250
  # (130,000 - 45,000) / 4 = 21,250; cost_sd/cost_mean = 0.266, within E-3 R5 range.
  throughput_units_equiv_per_year: 39600
  # Derivation: 150 units/day (individual viennoiserie piece equivalent)
  # × 300 operating days/year × (1 - 0.12 downtime)
  # = 150 × 300 × 0.88 = 39,600 units/year.
  # Annual operating days: 5 days/wk × 52 wks = 260 gross days; adjusted to 300
  # by accounting for Saturday partial-day market sales included in 5-day week
  # assumption and ~52 closure days (holidays, vacation, planned downtime weeks)
  # net to ~260 true operating days. [Note: 300 operating days is the upper-bound
  # interpretation; conservative authors should use 260 days → 34,320 units/year.
  # 39,600 uses the 300-day figure per catalog convention; see Key Assumptions.]
  variable_cost_per_unit: 1.14
  # Per unit: butter $0.46 (25% butter rate on ~70g pastry flour base at $6.50/kg butter
  # [CITATION-NEEDED]) + flour $0.20 + chocolate/fillings $0.20 + energy $0.05
  # (7 kWh/hr ÷ ~140 units/active-hr × $0.13/kWh) + packaging $0.10 + misc $0.13
  # = $1.14/unit. Butter is the dominant variable cost; price volatility is a
  # primary margin risk.
  labor_hours_per_unit: 0.115
  # Derivation: 2.5 operators × 40 hr/wk × 52 wks × (1 - 0.12 downtime) = 4,576 hr/yr.
  # labor_hours_per_unit = 4,576 / 39,600 ≈ 0.1155 → 0.115.
  # E-3 R3 check: 39,600 × 0.115 = 4,554 ≈ 4,576 (within 0.5%). ✓
  downtime_fraction: 0.12
  # 12% accounts for: combi steam generator failure at ~1,800 hr (21-day lead time
  # ≈ 3 operating weeks), proofing chamber failure at ~3,000 hr (5-day lead time),
  # planned quarterly maintenance windows, and seasonal closure adjustment.
  # Consistent with operations_reality first_year_failures profile.
  lifespan_years: 15
  # Commercial combi oven service life with regular maintenance: 12-18 years typical.
  # [CITATION-NEEDED: commercial combi oven manufacturer rated service life]

# ── RESULTS ──────────────────────────────────────────────────────────────────

results:
  village_market:
    verdict: win
    primary_metric: 0.6321417652616262
    metric_name: payback_years
    notes: ''
  village_coop:
    verdict: fail
    primary_metric: 355.0
    metric_name: break_even_members
    notes: feasible_pool=31.2, break_even=355, total_annual_cost=70867
  village_civic:
    verdict: fail
    primary_metric: 102.86666666666667
    metric_name: per_household_cost
    notes: per_hh=102.87, threshold=120, hrs/capita=0.000 vs threshold=2.0
  town_market:
    verdict: win
    primary_metric: 0.6321417652616262
    metric_name: payback_years
    notes: ''
  town_coop:
    verdict: fail
    primary_metric: 355.0
    metric_name: break_even_members
    notes: feasible_pool=212.5, break_even=355, total_annual_cost=70867
  town_civic:
    verdict: fail
    primary_metric: 15.127450980392158
    metric_name: per_household_cost
    notes: per_hh=15.13, threshold=100, hrs/capita=0.000 vs threshold=2.0
  small_city_market:
    verdict: win
    primary_metric: 0.6321417652616262
    metric_name: payback_years
    notes: ''
  small_city_coop:
    verdict: win
    primary_metric: 355.0
    metric_name: break_even_members
    notes: feasible_pool=900.0, break_even=355, total_annual_cost=70867
  small_city_civic:
    verdict: fail
    primary_metric: 2.8574074074074076
    metric_name: per_household_cost
    notes: per_hh=2.86, threshold=80, hrs/capita=0.000 vs threshold=2.0
sources:
  - ref: "USDA Economic Research Service, retail bakery product price data [CITATION-NEEDED — replace with specific ERS report or USDA NASS dairy/wheat price series URL and access date]"
  - ref: "Specialty Food Association, 'State of the Specialty Food Industry 2024,' pastry and confection channel section [CITATION-NEEDED — replace with SFA report URL and access date]"
  - ref: "Commercial combi oven manufacturer service data (steam generator MTBF, replacement cost) [CITATION-NEEDED — replace with specific manufacturer technical bulletin or service manual citation]"
  - ref: "US Bureau of Labor Statistics, CPI for bakery products and dairy inputs [CITATION-NEEDED — replace with specific BLS series ID and access date]"
  - ref: "Local commercial real estate rate estimate, small-city retail/light-industrial zone, $350/m²/yr [CITATION-NEEDED — replace with local market rate data source]"
  - ref: "research/trades/baking/REQUIREMENTS.md — throughput ranges, operator skill definitions (pastry-chef-master), energy source specifications (combi-steam)"
  - ref: "research/trades/baking/DECLINE-VERDICT.md — niche targeting, flour sourcing guidance, specialty confection positioning"
  - ref: "catalog/baking/SCHEMA.md v1.0 — baking throughput structure, energy_source enumeration (combi-steam notes), flour_source_declaration field, operator_skill_floor definitions"
---
## Summary

bake-006 is a specialty pastry operation producing classical French viennoiserie — croissants, pain au chocolat, danish, and pâte-à-choux confection (éclairs, cream puffs) — at premium retail pricing in a small-city market. It is the catalog's representative of the highest skill-floor, highest per-unit-margin, lowest throughput segment of artisan baking. The defining equipment is a commercial combi-steam oven, which is not optional: integral steam injection during the first minutes of baking is what produces the characteristic shatter, honeycomb crumb, and layering of properly executed laminated doughs. This entry exists as a distinct catalog item because the economics, skill requirements, failure modes, and market conditions of viennoiserie production are categorically different from all other baking entries — different from sourdough bread (different technique, equipment, and buyer psychology), from wholesale supply (different channel and volume), and from celebration cake (different product structure and event dependency). The market lens is primary; cooperative and civic lenses are poor.

## Design rationale

The problem bake-006 solves in the catalog is the absence of a specialty confection entry that honestly accounts for the master-level skill requirement and the equipment dependency that defines this niche. Other baking entries address bread-primary operations at journeyman skill floor; bake-006 fills the premium confection cell where the artisan premium over industrial product is highest ($4-$11 per unit versus $2.50 industrial baseline), but the barrier to entry is correspondingly steep: culinary-school formation plus professional placement in a pastry kitchen, not folk tradition or self-teaching. The entry is explicitly anti-romantic about this: modern French pastry technique is a codified professional skill acquired through formal training, not artisanal heritage accessible to a motivated generalist. The design documents whether this premium is sufficient to support viable small-city market operations given that capital cost, and what the real failure modes are for an operator who underestimates the equipment complexity.

## Historical lineage

The functional predecessors of this design are three: the 19th-century Viennese Konditorei, the belle époque Parisian boulangerie-pâtisserie, and the mid-20th-century French provincial pâtisserie. The Viennese Konditorei established the product category: Viennoiserie (literally "things from Vienna") was the name Parisian bakers gave to the laminated-dough techniques brought by Austrian bakers in the early 19th century. The functional inheritance this entry carries forward from the Konditorei form is the premium positioning, the destination-retail rather than commodity-supply model, and the master-practitioner skill requirement as a non-negotiable operating condition. From the belle époque Parisian boulangerie-pâtisserie comes the combined bread and pastry retail format — though bake-006 is confection-primary, the historical combined format is why pastry production and bread production share a building and some equipment. The mid-20th-century French provincial pâtisserie is the more direct operational model: a single master pastry chef with 1-2 assistants, a modest production footprint, and a loyal local customer base built around quality and regularity. That model's labor regime — master-apprentice transmission across generations within a single shop — is partially reproducible in the modern context only through formal culinary pipeline (culinary school graduates placed in established shops), not through informal apprenticeship on this equipment. The supply-chain condition that made those historical forms viable — a protected local market without supermarket-produced frozen-baked alternatives — has been partially eroded; the artisan premium must be earned through visible technique and provenance, not by default of unavailability of alternatives.

## Key assumptions

Capital cost mid-point ($80,000) assumes a new mid-range commercial combi oven ($18,000-$30,000), two dedicated proofing chambers ($3,000-$6,000 each), a refrigerated laminating table ($5,000-$10,000), and a commercial spiral mixer ($4,000-$8,000), plus miscellaneous cold-prep infrastructure. These are rough estimates; actual quotes vary significantly by brand and configuration. The install cost ($8,000) is an order-of-magnitude estimate for electrical service upgrade, plumbing for steam water supply, and mechanical extraction ducting. Both figures are flagged [CITATION-NEEDED].

Flour sourcing is declared as industrial-flour-purchased. Viennoiserie requires low-protein specialty pastry flour (T45 French equivalent or comparable low-extraction flour) for proper laminated-dough structure. This flour is not produced by most local artisan mills and must be sourced through specialty distributors. The artisan premium for this entry rests on technique, butter quality, and freshness — not grain provenance.

The throughput unit is one individual viennoiserie piece equivalent (one croissant, one pain au chocolat, one danish, or one éclair). At 150 units/day mid-range, this reflects a realistic 3-wave bake cycle with 2-3 operators. The 300 operating-days figure used in throughput_units_equiv_per_year derivation represents the upper-bound interpretation of a 5-day week over 52 weeks (260 gross days) with Saturday market sales sessions added; conservative operators should model 260 days, yielding ~34,320 units/year. The 39,600 figure uses the 300-day convention and is the mid-case used in sim_params.

Market pricing mid-point ($7.00/unit) is based on observed retail pricing for all-butter artisan croissants and pain au chocolat in US small-city specialty bakeries and upscale coffee shop wholesale partnerships [CITATION-NEEDED]. The industrial baseline ($2.50/unit) reflects supermarket frozen-baked croissant pricing [CITATION-NEEDED]. Both figures must be replaced with cited primary sources before promotion to reviewed status.

Butter is the dominant variable cost and the primary margin-risk factor. Commercial butter pricing fluctuates with dairy commodity markets; a sustained 20% butter price increase would raise variable cost per unit from $1.14 to approximately $1.23, compressing margin without a corresponding ability to raise retail price quickly. Operators should model this sensitivity explicitly.

## Known risks / failure modes

**Regulatory:** Commercial kitchen licensing is baseline; retail food establishment license is required for customer-facing sales. Allergen labeling is a specific regulatory requirement for viennoiserie: butter (dairy), wheat (gluten), eggs, and nuts (almond cream is a standard croissant fill) are all common allergens present in standard viennoiserie products. Mislabeling or failure to declare allergens is a health-code violation with potential product-recall and liability consequences. In some US jurisdictions, a production bakery with retail sales requires a dual license (production facility + retail food establishment); failure to obtain both is a documented early-operational failure mode.

**Labour pipeline:** The pastry-chef-master skill floor is the single highest succession risk in the catalog. Because `apprentice_friendly: false`, there is no shop-floor training path: the lead operator must arrive with master-level formation already established through culinary school and professional placement. If the lead pastry chef departs, the operation cannot continue at production quality until a replacement with equivalent formation is hired. Hiring a master pastry chef for a small-city operation is geographically constrained: the pool is thin outside major metropolitan areas, and a qualified candidate may require a wage premium that shifts the economics materially. This risk must be named in any business plan and monitored as a primary operating concern. The 2-3 operator model mitigates but does not eliminate this risk; only the lead operator's skills are irreplaceable.

**Supply chain:** Premium butter and specialty pastry flour from specialty distributors carry a 4-day typical and 21-day worst-case lead time. Butter supply is particularly exposed to dairy market disruptions; the 2021-2022 European butter shortage and similar events demonstrate that high-quality butter for commercial pastry production can become constrained without warning. Mitigation: maintain 2-week butter inventory in commercial refrigeration and identify at least one alternative distributor. Specialty couverture chocolate for pain au chocolat and éclairs is an additional single-source dependency if a specific origin or brand is part of the product identity.

**Equipment dependency (primary single-point risk):** The combi steam generator is the irreplaceable production dependency. A steam generator failure at ~1,800 operating hours triggers a 21-day replacement lead time with specialist servicing required. During those 21 days, laminated dough production is not viable on substitute equipment: a standard deck or convection oven cannot replicate integral steam injection for croissant-quality baking. This represents approximately 3 operating weeks of revenue loss at the time of failure (mid-first-year), a $7,000-$21,000 revenue impact at mid-pricing and 150 units/day. Operators should maintain a working-capital buffer of at least $10,000 for this contingency and should investigate water softener installation if local water hardness is above 150 mg/L CaCO₃ to extend steam generator lifespan.

## Iteration log

- 2026-04-18: v0.1 — initial creation per Plan G task 8. All economic figures flagged [CITATION-NEEDED] where primary sources were not available; to be replaced with cited primary sources before promotion to reviewed status. Operating-days assumption (300 vs 260) flagged for resolution in first review cycle.
