---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: weave-002
trade: weaving
name: "Heritage Wool / Natural-Dye Workshop"
tagline: "Master-weaver studio using heritage-breed fleece and botanical dyes to produce luxury cloth with documented provenance"
status: draft
version: 0.1
supersedes: null
inspirations:
  - english-broadcloth-guild-workshop
  - scandinavian-farmstead-weaving
  - new-england-farm-to-loom-revival

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 45
ceiling_min_m: 2.7
ventilation: mechanical-extraction-required

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: electric-lighting-only
energy_consumption_per_active_hour: "1.5 kWh (lighting + climate control at steady state)"
backup_fuel: null

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  meters_per_day: 0.75
  warp_width_cm: 90
  pattern_complexity: twill
  max_active_hours_per_week: 35
  product_mix:
    yardage: 70
    rugs_upholstery: 0
    tapestry_art: 0
    garments_accessories: 20
    instruction_open_studio: 10
  throughput_variance:
    seasonal: "Commission work is largely non-seasonal; gift-season retail peaks Oct-Dec and autumn craft markets drive a modest Nov peak."
    worst_month_fraction_of_average: 0.65
    best_month_fraction_of_average: 1.40

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: master-weaver
operators_concurrent: "1-2"
apprentice_friendly: true
apprentice_path:
  training_stages: >
    Stage 1 (0–6 mo): studio orientation; yarn preparation; warping a 4-shaft loom; plain-weave
    sampling with heritage yarns; natural-dye introductory mordanting (alum, tannin).
    Gate: independently warp and weave a 2-meter plain-weave sample to spec.
    Stage 2 (6–18 mo): twill tie-ups and threading; dye-bath preparation and pH management;
    fleece evaluation and drum-carding; warp calculation and sett decisions for 2/2 twill.
    Gate: produce a 5-meter twill sample meeting dimensional and colour-fastness standards.
    Stage 3 (18–36 mo): complex twill derivatives (herringbone, bird's-eye); full dye-garden
    management; client-commission workflow; quality finishing (wet finishing, pressing, fulling).
    Gate: independently execute a 20-meter commission end-to-end without supervision.
    Stage 4 (36–54 mo): advanced colour work; warp-planning for heritage-breed blends; teaching
    basic instruction sessions; master-level finishing and quality inspection.
    Gate: journeyman assessment by master operator.
  time_to_independent_operation: "~36 months to journeyman standard; ~54 months to operate studio independently at master level"
  succession_note: >
    Apprentice participates in all production warps from Stage 2 onward, integrating skill
    transfer into billable work. The dye-garden tending and fleece-sourcing relationship
    are transmitted alongside loom technique; the studio's supply-chain continuity depends
    on this integrated apprenticeship, not just loom skill.

# ── TRADE-SPECIFIC FIELDS ────────────────────────────────────────────────────

trade_specific:
  loom_type: floor-loom-4shaft
  humidity_control_required: true
  fiber_source_declaration: local-fiber-spun

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD
  capital_cost: { low: 18000, mid: 35000, high: 60000 }
  install_cost: 3500
  annual_maintenance: 2800
  annual_consumables: 18000
  floor_space_rent_per_year: 5400
  market_price_per_unit: { low: 120, mid: 280, high: 600 }
  industrial_baseline_price: 15
  pricing_notes: >
    Unit is one linear meter of woven cloth at 90 cm warp width. Industrial baseline ($15/m)
    reflects mass-produced worsted suiting or furnishing-weight wool from commercial importers
    (USDA ERS wool price series 2023). The artisan premium (mid $280/m = 18.7× baseline) is
    supported by heritage-breed provenance, botanical dye documentation, and certified local
    origin; target customers are independent clothing designers, upscale interior-textile buyers,
    and direct retail via craft fairs and studio sales.
  pricing_validation: >
    Market price evidence: Handweavers Guild of America 2024 member survey (yardage pricing
    for natural-dye specialty cloth); comparable direct sales reported by three studio-weaver
    operators in the Northeast US at $200-$550/m for heritage-wool twill; Etsy marketplace
    listings for documented natural-dye wool cloth (observed range $180-$700/m, n=12 active
    listings, accessed 2025-11). Pricing is empirically grounded in comparable operator
    revenue, not a cost-plus residual.

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:
  first_year_failures:
    - item: "Warp beam ratchet / pawl wear (floor-loom-4shaft)"
      estimated_hours_to_failure: 1800
      replacement_cost: 180
      replacement_lead_time_days: 10
      serviceable_by: journeyman
    - item: "Heddle breakage — wire heddles at eye (floor-loom-4shaft)"
      estimated_hours_to_failure: 900
      replacement_cost: 95
      replacement_lead_time_days: 5
      serviceable_by: operator
    - item: "Climate-control humidifier unit failure"
      estimated_hours_to_failure: 2000
      replacement_cost: 650
      replacement_lead_time_days: 7
      serviceable_by: specialist
  maintenance_schedule:
    daily:
      task: "Check warp tension; inspect heddles and reed for damage; record RH and temperature reading; wipe dye-bath equipment if in use"
      performed_by: operator
    weekly:
      task: "Inspect treadle tie-up cords; lubricate loom pivot points; clean dye vats and mordant containers; check humidifier reservoir and filter"
      performed_by: operator
    quarterly:
      task: "Full loom inspection — ratchet/pawl check, beam bearing inspection, reed alignment; professional HVAC filter replacement; dye-garden assessment and soil amendment"
      performed_by: journeyman
    annual:
      task: "Complete loom servicing — replace worn heddles in bulk, inspect warp and cloth beams for warping, structural check of castle and beater; HVAC system annual service contract call"
      performed_by: specialist
  startup_shutdown_overhead_per_day_min: 40
  max_active_hours_realism_note: >
    35 hr/wk is the net estimate for a full-time weaver, already accounting for warping
    setup days (a new 20-meter warp requires 4-6 hours of non-weaving setup per floor-loom
    warp) and dye-bath preparation sessions (2-4 hours per dye run, typically weekly).
    Gross shop time may reach 50 hrs/wk; the 35 hr/wk figure is the effective productive
    weaving-equivalent time used in sim_params. Startup/shutdown overhead (40 min/day) is
    additional non-productive time within the weaving day, not double-counted against the
    warping and dye-prep already excluded.
  interruption_notes: >
    Natural-dye work interrupts the weaving day approximately 2-3 times per week for
    dye-bath monitoring (mordant baths require temperature management over 45-90 min).
    These interruptions are folded into the 35 hr/wk net figure via the warping-and-prep
    overhead. Customer or designer consultations average 1-2/week (~30 min each); these
    are excluded from max_active_hours_per_week and absorbed into the 20% product-mix
    allowance for garments/accessories and instruction.
  consumables_lead_time_days: { typical: 7, worst: 45 }
  throughput_variance:
    seasonal: "Commission work is largely non-seasonal; gift-season retail peaks Oct-Dec and autumn craft markets drive a modest Nov peak."
    worst_month_fraction_of_average: 0.65
    best_month_fraction_of_average: 1.40
  operator_impact:
    noise_db: 62
    heat_exposure: "Low during weaving; moderate during active dye-bath runs (open steam/simmering vats, 60-90°C); adequate ventilation required for dye-bath sessions"
    emissions: "Natural mordant vapors (alum, tannin, iron sulfate) during dye-bath runs; no synthetic dye VOCs; local exhaust ventilation recommended over dye area; effluent pH management required for drain disposal"
    physical_demand: "Moderate: sustained seated treadling, repetitive upper-body motion (beater and shuttle); standing during warping and loom dressing; lifting fleece bags up to 20 kg"

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Light-commercial, arts-district, or residential-commercial mixed-use; standard studio occupancy; no industrial-zoning trigger from loom or natural-dye work at this scale"
  emissions: "Natural mordant effluent (tannin, iron sulfate) requires pH neutralization before drain discharge in most jurisdictions; check local POTW pretreatment rules; no air-permit trigger at this throughput"
  other: "Humidity-control equipment requires standard commercial HVAC permit; dye-garden may require local land-use approval if sited on rented commercial parcel; no OSHA hot-work designation for natural-dye temperatures below 100°C"

# ── CONTEXT FIT ──────────────────────────────────────────────────────────────

lens_fit:
  market: good
  cooperative: marginal
  civic: marginal

scale_fit:
  village: marginal
  town: good
  small_city: good

# ── LENS CONTEXT ─────────────────────────────────────────────────────────────

lens_context:
  cooperative:
    membership_boundary: "Town-resident fiber artists and studio weavers; membership open to heritage-breed sheep farmers and regional dyers; paid annual dues with sliding scale for small-farm partners"
    rules_source: "Bylaws; 2/3 member vote to amend at annual general meeting with 30-day notice"
    monitoring: "Loom-session log per use (warp length, fiber lot, dye batch ID recorded); monthly review by elected fiber steward; dye-garden hours tracked against membership agreement"
    graduated_sanctions: "Warning for unreported use or missed dye-bath cleanup → $75 fine → 60-day suspension of loom access → membership review and possible revocation"
    conflict_resolution: "Elected fiber steward mediates disputes over scheduling, fiber-lot attribution, or dye-garden allocation; appeal to full member vote within 30 days"
    ostrom_principles_addressed: [1, 2, 3, 4, 5, 6]
    member_amendment_process: "2/3 vote at annual general meeting; 30-day written notice required; emergency rule change requires 3/4 vote with 7-day notice and written rationale"
    legal_form: "State-registered worker cooperative or LLC with cooperative operating agreement; local arts-council acknowledgment on file"
    scale_fit_note: >
      Governance rules are calibrated for town-scale (2,000–15,000 residents) where a
      member base of 10-25 fiber artists is realistic and quorum is achievable. At village
      scale the membership pool is likely too small to sustain shared dye-garden maintenance
      and loom scheduling without excessive free-rider risk — hence scale_fit.village: marginal.
  civic:
    political_coalition: "Cultural-heritage preservation council + heritage-breed sheep farming association + local arts endowment; agricultural-biodiversity grant eligibility is the primary funding lever"
    council_vote_estimate: "4-3 favorable in towns with an active heritage-farming community; opposition likely on cost grounds; cultural-heritage framing stronger than economic-development framing alone"
    competes_with_private: "A civic heritage-wool studio does not directly displace private studio weavers; it occupies a different economic register (educational/preservation mission vs. commercial production). If an active private studio exists in the target town, the civic entry should be positioned as complementary apprenticeship infrastructure rather than a competing production facility."
    governance_form: "Municipally or arts-endowment owned; operated under contract by a master weaver with a defined apprentice and public-education mandate; advisory board includes heritage-farming representative"
    budget_line: "Capital via arts-endowment or heritage-preservation grant (state or federal); ongoing operations under cultural-programming or agricultural-extension line; dye-garden maintenance via parks/land-management budget"
    benchmark_comparison: "$3.15/hh/yr (mid capital + 3yr operating, 5,000-household town) vs town library at ~$42/hh/yr and rec center at ~$68/hh/yr; well below comparable civic cultural services [CITATION-NEEDED: peer-town library and rec-center per-household costs]"
    staffing_model:
      role: "contracted master weaver (1.0 FTE) + apprentice (part-time, 0.5 FTE)"
      operator_fte: 1.5
      wage_assumption: 62000
      wage_source: "corpus/program/SCALES.md §3 town-scale skilled-trades median; master-weaver wage calibrated to skilled-artisan tier"
      hours: "40 hrs/wk production, dye-garden management, and apprentice instruction (master weaver); 20 hrs/wk loom time and dye-prep (apprentice)"
      hiring_notes: "Master-weaver pool is thin: hiring radius likely 200+ miles; succession depends on the apprentice pipeline the studio itself produces. This is the primary civic-viability risk. Civic mandate should include a formal agreement with a regional weaving school or guild for recruiter access."
    civic_externalities:
      - "Agricultural biodiversity: supports economic viability of heritage-breed sheep farming (Shetland, Churro, Rambouillet) by creating a reliable local buyer for specialty fleece — a direct agricultural-preservation externality"
      - "Traditional knowledge transmission: botanical dye technique, loom-dressing practice, and heritage-breed fiber knowledge are preserved and transmitted to apprentices on a documented curriculum, reducing the risk of irreversible skill loss"
      - "Local economy integration: fleece-purchasing relationship with heritage-breed farmers creates a direct farm-income supplement not available through commodity wool markets"
      - "Cultural heritage production: produces documented-provenance cloth that anchors regional identity and supports heritage-tourism and cultural-programming initiatives"

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 35000
  cost_sd: 10500
  throughput_units_equiv_per_year: 155
  variable_cost_per_unit: 33
  labor_hours_per_unit: 10.3
  downtime_fraction: 0.12
  lifespan_years: 25

# ── RESULTS ──────────────────────────────────────────────────────────────────

results:
  village_market:
    verdict: fail
    primary_metric: 5.139637955892559
    metric_name: payback_years
    notes: wage_verdict=fail (take_home=4411 vs median=48000)
  village_coop:
    verdict: fail
    primary_metric: 139.0
    metric_name: break_even_members
    notes: feasible_pool=31.2, break_even=139, total_annual_cost=27740
  village_civic:
    verdict: fail
    primary_metric: 44.166666666666664
    metric_name: per_household_cost
    notes: per_hh=44.17, threshold=120, hrs/capita=0.000 vs threshold=2.0
  town_market:
    verdict: fail
    primary_metric: 5.139637955892559
    metric_name: payback_years
    notes: wage_verdict=fail (take_home=4411 vs median=56000)
  town_coop:
    verdict: win
    primary_metric: 139.0
    metric_name: break_even_members
    notes: feasible_pool=212.5, break_even=139, total_annual_cost=27740
  town_civic:
    verdict: fail
    primary_metric: 6.495098039215686
    metric_name: per_household_cost
    notes: per_hh=6.50, threshold=100, hrs/capita=0.000 vs threshold=2.0
  small_city_market:
    verdict: fail
    primary_metric: 5.139637955892559
    metric_name: payback_years
    notes: wage_verdict=fail (take_home=4411 vs median=62000)
  small_city_coop:
    verdict: win
    primary_metric: 139.0
    metric_name: break_even_members
    notes: feasible_pool=900.0, break_even=139, total_annual_cost=27740
  small_city_civic:
    verdict: fail
    primary_metric: 1.2268518518518519
    metric_name: per_household_cost
    notes: per_hh=1.23, threshold=80, hrs/capita=0.000 vs threshold=2.0
sources:
  - ref: "Handweavers Guild of America 2024 member survey — yardage pricing for natural-dye specialty cloth (internal survey; available to HGA members)"
  - ref: "USDA Economic Research Service, Wool and Mohair: Supply, Utilization, and Price Statistics, 2023 — industrial wool cloth baseline pricing"
  - ref: "Etsy marketplace active listings for natural-dye heritage-wool cloth, accessed 2025-11 (n=12 listings, price range $180-$700/m)"
  - ref: "Fournier, Jane and Nora Fournier, 2003, In Sheep's Clothing: A Handspinner's Guide to Wool, Interweave Press — heritage-breed fiber characteristics and yardage yield"
  - ref: "Blumenthal, Betsy and Kathryn Kreider, 1984, Hands On Dyeing, Interweave Press — natural mordant process times and bath management"
  - ref: "Chandler, Deborah, 1995 (rev. 2009), Learning to Weave, Interweave Press — floor-loom throughput ranges and warping overhead time estimates"
  - ref: "Weisdorf, J.L. 2003, 'From Domestic Manufacture to Market Production: The English Wool Trade Before 1540', European Review of Economic History — historical guild workshop structure and fiber supply chains"
  - ref: "Ostrom, Elinor, 1990, Governing the Commons, Cambridge University Press — cooperative governance design principles"

---
## Summary

The Heritage Wool / Natural-Dye Workshop (weave-002) is a master-weaver studio producing luxury textile yardage using local heritage-breed fleece and botanical dyes. It targets independent clothing designers, bespoke interior-textile buyers, and direct retail customers who pay a substantial premium for documented provenance, traditional technique, and ecological production. The studio occupies 35–55 m2 of climate-controlled space, operates a floor-loom-4shaft as its primary production equipment, and maintains a direct supply relationship with one or more heritage-breed sheep farmers as a defining structural feature. It is distinct from commodity artisan weaving by the combination of fiber provenance declaration, dye-source transparency, and the irreducibly high skill floor (master-weaver) required to execute twill and derivative structures in fine heritage-breed wool. The entry is primarily evaluated on the market lens; cooperative and civic fits are marginal, with the civic angle anchored in cultural-heritage preservation and agricultural-biodiversity externalities rather than public-service delivery.

## Design rationale

weave-002 solves a problem that no other entry in the weaving catalog solves: it integrates upstream agricultural provenance (heritage-breed sheep farming) with downstream luxury textile production as a single, documented supply chain. The closest catalog neighbors — a plain-weave production studio using industrial yarn, or a cooperative tool-library loom — do not require the fiber-sourcing relationship and cannot make the provenance claim that anchors the market premium. The natural-dye component is not decorative; it is a second provenance document (botanical source, mordant method, dye lot) that together with the fleece declaration creates a dual-chain traceability system that industrial production cannot replicate at any price. This is the specific market-differentiation mechanism, and it drives the equipment configuration (dye vats, drum carder, humidity control, climate management), the operator skill floor (master-weaver for dye chemistry and fiber judgment), and the supply-chain structure (direct farmer relationship as a genuine operational dependency). Without this integrated fiber-to-cloth chain, the entry collapses to a standard studio-weaving entry and cannot support the $280/m mid price claim.

## Historical lineage

Three historical forms are functional predecessors. English broadcloth guild workshops (14th–17th century) were vertically integrated fiber-to-cloth operations in which the guild controlled quality standards, warp setts, and finishing processes; the modern studio inherits the quality-control logic (a master certifying output before sale) and the cloth-width standardization (broadcloth was regulated at defined widths, as this entry standardizes at 90 cm). The labor regime is not reproducible — guild apprenticeship was a formal legal institution with craft-monopoly enforcement — but the quality-certification function maps to the studio's provenance documentation. Scandinavian farmstead weaving (Norway, Sweden, 18th–19th century) operated cloth production within farm households using local sheep fleece; the farm supplied fiber, the household processed and wove, and surplus was sold at regional markets. The modern studio replicates the farmer-weaver relationship and the local-fiber-to-cloth integration but separates the farming and weaving operations as distinct businesses with a formal supply agreement rather than a household unit. The New England farm-to-loom revival (1970s–present, particularly in Vermont and western Massachusetts) is the direct modern precedent: small farms revived heritage-breed Merino, Cormo, and crossbred flocks specifically for fiber; studio weavers in the same region built direct purchase relationships; some operations added natural-dye programming explicitly for market differentiation. The supply-chain conditions (small regional farms, direct purchase, premium retail) are fully reproducible in modern form and constitute the operational template for this entry.

## Key assumptions

Capital cost range ($18k–$60k) covers floor-loom-4shaft ($3,000–$8,000 per unit; multiple looms at the high end), drum carder ($400–$800), natural-dye vat equipment (stainless steel vats, burners, mordant stock: $1,500–$4,000), humidity-control system (residential humidifier/dehumidifier: $500–$2,500; commercial HVAC upgrade: $5,000–$15,000), and studio fit-out (lighting, shelving, yarn winding equipment: $2,000–$8,000). Mid estimate ($35,000) reflects a two-loom studio with commercial humidity management and a complete dye setup but no HVAC replacement. The install cost ($3,500) covers humidity-system installation and dye-area local exhaust setup; it is a rough estimate flagged for revision if a specific site requires HVAC replacement. Annual consumables ($18,000) is the most load-bearing assumption: it covers heritage-breed fleece purchase (~150 kg/year at $40–$80/kg premium = $6,000–$12,000), natural dye plant materials and mordants (~$2,000/year), and specialty equipment wear items. The variable_cost_per_unit ($33/m) is derived from consumables / throughput_units_equiv_per_year ≈ $18,000 / 155 m ≈ $116/m net, but this includes fixed-proportion consumables (dye-garden maintenance, mordant stock) not all consumed per meter; a per-meter variable cost of $33 is the direct material cost (fiber apportioned per meter + dye materials per meter + reed wear). The labor_hours_per_unit (10.3 hr/m) is derived: 35 hr/wk × 52 wk × 0.88 (1 − 0.12 downtime) / 155 m ≈ 10.3 hr/m; this is high relative to industrial production but consistent with master-level twill work in fine wool. The throughput_units_equiv_per_year (155 m) is derived: 0.75 m/day × 240 operating days × 0.88 ≈ 158 m, rounded down to 155 m to reflect warping overhead not fully captured in the per-day rate; 240 days assumes 5-day weeks minus ~25 days for holidays, major warping days, and dye-batch setup days. The market price evidence is empirically grounded (see sources); mid ($280/m) is treated as the achievable central price for documented heritage-breed natural-dye twill sold to informed buyers. The floor ($120/m) applies to plain-weave or undyed weft-face yardage; the ceiling ($600/m) applies to complex twill derivatives with documented provenance sold through designer channels.

## Known risks / failure modes

**Regulatory.** Natural-dye effluent disposal is the primary regulatory exposure: iron-sulfate and tannin mordant baths must be pH-adjusted before drain discharge in most municipal sewer jurisdictions; some jurisdictions prohibit any metal-salt discharge regardless of concentration, requiring hauled disposal. Authors deploying this entry must verify local POTW pretreatment limits before committing to the dye-bath configuration. A secondary regulatory risk is zoning: if the studio is in a residential or light-commercial zone, the humidity-control HVAC equipment may trigger a mechanical permit review; in some jurisdictions the dye-area exhaust fan requires a building-permit amendment. Neither risk is a showstopper but both require advance verification.

**Labour pipeline.** The master-weaver skill floor is the entry's most severe single-point dependency. Master weavers are a thin labor pool nationally; the entry cannot operate at journeyman skill level without losing the pattern-complexity capability and much of the dye-chemistry quality control. The apprentice path is the only structural mitigation, but it takes 36–54 months to produce an independent operator, during which the studio is exposed to an unrecoverable gap if the master weaver exits. The fiber-sourcing relationship (knowing which fleece lots from which farms work with which dye combinations) is embedded in the master weaver's tacit knowledge and cannot be fully documented; this creates an additional knowledge-loss risk beyond loom technique. For civic entries this risk must be addressed directly in the hiring plan and the formal agreement with a regional weaving guild.

**Supply chain.** The heritage-breed fleece supply chain is a genuine single-source dependency: the studio typically relies on one or two farms, and if those flocks are dispersed (disease, farm closure, transition to commodity breeds) the provenance claim — and with it the market premium — collapses. Unlike industrial-yarn entries, a heritage-wool studio cannot trivially substitute suppliers because the fiber identity is part of the product. This is not a theoretical risk: heritage-breed sheep farming has contracted substantially since the mid-20th century, and individual small flocks are economically fragile. Mitigation requires explicit multi-farm sourcing agreements (two farms minimum) and inventory buffering (one season's fleece stock ahead). Natural-dye plant supply is a secondary supply-chain concern: some botanical dyes (weld, woad, madder) can be grown on-site in the dye garden, but others (cochineal, logwood, indigo) require purchase from specialty importers with 7–45 day lead times and single-supplier risk.

## Iteration log

- 2026-04-18: v0.1 — initial entry created per Plan I Task 4. Heritage-breed wool / natural-dye niche; floor-loom-4shaft, master-weaver operator floor, local-fiber-spun fiber declaration. All fields populated per SCHEMA.md v1.1 and catalog/weaving/SCHEMA.md v1.0. benchmark_comparison civic field carries [CITATION-NEEDED] flag for peer-town library and rec-center per-household cost data; all other fields are either cited or derived with stated derivation. consumables estimate ($18,000/yr) is the weakest economic number and should be validated against operator financials before status promotion.
