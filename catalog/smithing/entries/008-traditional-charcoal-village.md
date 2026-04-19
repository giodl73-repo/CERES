---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: forge-008
trade: smithing
name: "Traditional Charcoal Village Forge (hand-bellows, single operator)"
tagline: "Charcoal-fired hand-bellows forge for purist and heritage-method specialty output; market-marginal by design"
status: draft
version: 0.1
supersedes: null
inspirations: [japanese-fuigo-charcoal-forge, traditional-european-village-charcoal-forge, song-era-village-scale-smithing]

# ── PHYSICAL ENVELOPE ─────────────────────────────────────────────────────────

footprint_m2: 28
ceiling_min_m: 3.5
ventilation: dedicated-exhaust-system

# ── ENERGY ────────────────────────────────────────────────────────────────────

energy_source: charcoal
energy_consumption_per_active_hour: "3 kg charcoal"
backup_fuel: null

# ── THROUGHPUT ────────────────────────────────────────────────────────────────

throughput:
  units_per_hour: { small_work: 2, medium_work: 0.5, large_work: 0.1 }
  max_active_hours_per_week: 30
  product_mix:
    repair: 25
    commodity: 5
    specialty: 45
    artistic: 25
  throughput_variance:
    seasonal: "Demand is hobbyist- and purist-driven rather than agricultural; modest seasonality with slight warm-weather peak when craft events and heritage demonstrations concentrate activity."
    worst_month_fraction_of_average: 0.5
    best_month_fraction_of_average: 1.3

# ── OPERATOR PROFILE ──────────────────────────────────────────────────────────

operator_skill_floor: journeyman
operators_concurrent: "1"
apprentice_friendly: true
apprentice_path:
  training_stages: "Stage 1 (0–3 mo): charcoal fire management, fuigo or box-bellows operation, ash and clinker behavior with charcoal vs. coal — gate: operator maintains a working charcoal fire and correct heat zone without direction. Stage 2 (3–12 mo): small-work shaping, heat-color judgment under charcoal conditions (charcoal fire has different visual characteristics than a coal or gas fire), tool handling — gate: consistent small-work quality without intervention. Stage 3 (12–30 mo): medium repair and specialty work, understanding the charcoal fuel-feed rate and its effect on heat, traditional forging sequences — gate: independent handling of the specialty product categories that define this shop's revenue. Stage 4 (30–48 mo): full specialty and artistic range, forge welding with charcoal (charcoal is forge-weld capable at full heat; technique differs from coal), customer-brief execution — gate: journeyman standard, independent operation."
  time_to_independent_operation: "~48 months to journeyman standard; the longer timeline relative to a coal or gas shop reflects the additional skill investment required to operate a charcoal fire at the rates and quality levels that justify the premium customer base this entry depends on"
  succession_note: "Apprentice co-presence during production is the mechanism for skill transfer; the traditional master-apprentice pairing is operationally natural for this entry, but it carries the same single-operator succession risk as any proprietorship. An apprentice who does not complete training or who leaves represents a total succession failure."

# ── ECONOMICS ─────────────────────────────────────────────────────────────────

economics:
  currency: USD
  capital_cost: { low: 8000, mid: 13000, high: 20000 }
  install_cost: 1500
  annual_maintenance: 600
  annual_consumables: 2800
  floor_space_rent_per_year: 2400
  market_price_per_unit: { low: 40, mid: 65, high: 110 }
  industrial_baseline_price: 10
  pricing_notes: "Unit is one medium-work-equivalent item or repair. Industrial baseline ($10/unit) reflects factory-produced hardware equivalent available through commercial channels. The traditional-method premium requires a customer who specifically wants work produced using charcoal and hand bellows and is willing to pay for that production method, not just for the finished object. That customer base — hobbyists, historical re-enactors, collectors, heritage-craft buyers — is present in limited numbers in most markets and essentially absent in commodity or general repair contexts. The pricing range ($40–$110) reflects the wide variance in willingness-to-pay within this narrow segment. Pricing_validation: inferred. [CITATION-NEEDED: direct willingness-to-pay data for traditional-method smithed goods; figures are inferred from structural analogy to other heritage-craft markets (hand-thrown pottery, hand-woven textiles) where a premium over industrial baseline of 4–11× has been observed; no direct smithing survey identified.]"
  pricing_validation: "Inferred from structural analogy to heritage-craft premium pricing in comparable hand-production niches. No direct survey of traditional-method smithing pricing identified in sources consulted. The pricing claim rests on the assumption that a thin purist/hobbyist customer base exists in the target market, which is the primary commercial risk for this entry. Pricing_validation type: structural inference; not empirical sales data; flagged for strengthening before promotion to reviewed."

# ── OPERATIONS REALITY ────────────────────────────────────────────────────────

operations_reality:
  first_year_failures:
    - item: "Bellows leather and seals (fuigo box-bellows or traditional hide bellows)"
      estimated_hours_to_failure: 1200
      replacement_cost: 150
      replacement_lead_time_days: 14
      serviceable_by: operator
    - item: "Refractory lining (partial spalling at hearth face)"
      estimated_hours_to_failure: 2400
      replacement_cost: 200
      replacement_lead_time_days: 7
      serviceable_by: operator
    - item: "Anvil base settling (wood stump or packed-earth base)"
      estimated_hours_to_failure: 4000
      replacement_cost: 100
      replacement_lead_time_days: 3
      serviceable_by: operator

  maintenance_schedule:
    daily:
      task: "Ash and clinker cleanout from hearth, inspect and clear fire-pot, bellows visual inspection for leather condition and valve seating, charcoal bin level check"
      performed_by: operator
    weekly:
      task: "Bellows leather condition assessment (flex, cracking, seal integrity), inspect tuyere and fire-pot for charcoal ash accumulation and refractory wear"
      performed_by: operator
    monthly:
      task: "Full refractory lining inspection, anvil base and fastener check, chimney or hood cleanout for charcoal-ash and creosote, bellows valve and pivot inspection"
      performed_by: operator
    quarterly:
      task: "Bellows leather treatment (oil or wax, as appropriate to material) or replace if cracked; refractory patch as needed; full ventilation duct interior inspection"
      performed_by: operator
    annual:
      task: "Deep hearth cleanout, full ventilation system inspection, refractory assessment for partial or full reline, bellows mechanism overhaul or replacement, anvil base assessment"
      performed_by: journeyman

  startup_shutdown_overhead_per_day_min: 60
  max_active_hours_realism_note: "30 hr/wk is stated as the gross maximum for this configuration: charcoal fires start slowly (hand bellows build heat gradually; 30–40 min to working temperature is typical), hand-bellows operation imposes sustained upper-body fatigue that limits continuous forge time, and charcoal management requires more active monitoring than a blower-assisted fire. The 60 min/day startup-shutdown overhead (5-day week) subtracts 5 hr/wk; effective net production hours are approximately 25 hr/wk. sim_params uses the derated figure (25 hr/wk)."
  interruption_notes: "Hand-bellows operation must pause briefly to reposition or rest; typical pattern is 15–20 min forge periods alternating with 5 min rest or setup transitions. Charcoal re-loading (~every 45 min, ~5 min per load) also interrupts production. These patterns are folded into the 30 hr/wk gross ceiling via the already-conservative rate figures; they are not an additional derating beyond the startup/shutdown overhead."
  consumables_lead_time_days: { typical: 7, worst: 30 }
  throughput_variance:
    seasonal: "Demand is hobbyist- and purist-driven rather than agricultural; modest seasonality with slight warm-weather peak when craft events and heritage demonstrations concentrate activity."
    worst_month_fraction_of_average: 0.5
    best_month_fraction_of_average: 1.3
  operator_impact:
    noise_db: 70
    heat_exposure: "High at forge face; sustained radiant heat from charcoal fire; dedicated exhaust required; summer operation in a small open-bay shop is thermally demanding"
    emissions: "Charcoal combustion produces CO and particulate; lower SOx than coal; CO accumulation in an enclosed or poorly ventilated space is the primary life-safety hazard; OSHA ventilation requirements apply regardless of fuel type"
    physical_demand: "Very high; hand-bellows or treadle-bellows operation requires sustained upper-body or leg work throughout active forging periods; operators with shoulder, elbow, or knee limitations are not suited to this configuration; sustained hand-bellows operation at 6+ hrs/day is not realistic; the 30 hr/wk ceiling reflects this constraint"

# ── REGULATORY NOTES ──────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Village and rural zoning typically permits open-bay charcoal forge; charcoal is less regulated than coal in most US jurisdictions; urban and small-city locations face open-fire and particulate restrictions; this entry is not recommended for small-city deployment"
  emissions: "Charcoal combustion triggers OSHA 29 CFR 1910.252(c) ventilation requirements; CO is the primary hazard; particulate permit may apply above certain throughput thresholds; charcoal supply chain does not carry the sulfur-management requirements of coal [CITATION-NEEDED: specific charcoal emissions regulatory thresholds at village/rural scale]"
  other: "OSHA 29 CFR 1910.252(c) hot-work standards apply; local fire code governs charcoal storage quantity; charcoal sustainability documentation required per catalog/smithing/SCHEMA.md §2 (DIV-01): operator must state whether charcoal is sourced from coppiced, FSC-certified, or equivalent managed supply; vague sustainability claims are not acceptable per STYLE-GUIDE §4.2"

# ── CONTEXT FIT ───────────────────────────────────────────────────────────────

lens_fit:
  market: marginal
  cooperative: marginal
  civic: marginal

scale_fit:
  village: marginal
  town: poor
  small_city: poor

# ── LENS CONTEXT ──────────────────────────────────────────────────────────────

lens_context:
  cooperative:
    membership_boundary: "Paid-course participants and open-house attendees; membership structured as a craft-education cooperative in which participants pay for scheduled instruction and demonstration sessions using traditional charcoal-and-bellows methods; geographic scope: village and surrounding area; no restriction on participant background; membership fee covers session access, not equity stake"
    rules_source: "Operating charter or LLC member agreement; rules set at formation and amended by member vote; course schedule and fee structure are operator-determined between amendment cycles"
    monitoring: "Session attendance log; course completion records; open-house day headcount; monthly review of enrollment against operating-cost floor to assess financial viability"
    graduated_sanctions: "Non-payment of session fee: exclusion from future sessions until settled; safety violation during session: immediate removal, review before re-admission; repeated violations: permanent exclusion; there is no production commons to protect, so sanctions are primarily about payment compliance and safety"
    conflict_resolution: "Operator resolves disputes over course content or scheduling; disputes over fees escalate to cooperative board or founding member vote if applicable; no complex mediation structure is warranted at the membership volumes this entry supports"
    ostrom_principles_addressed: [1, 2, 4, 5]
    member_amendment_process: "Simple majority vote of enrolled members with 21-day written notice; emergency amendments by 2/3 vote with 72-hour notice; founding operator retains veto on safety and curriculum changes during an initial 3-year establishment period"
    scale_fit_note: "Governance rules calibrated for village-scale enrollment (10–40 active course participants); the paid-course cooperative model does not scale to town or city level without adding instructors and administrative overhead that changes the cost structure materially; this entry's cooperative viability is conditional on operating at small enrollment numbers where the operator personally delivers all instruction"
    legal_form: "Not required at marginal cooperative fit; if formalized, an LLC or 501(c)(3) educational entity is appropriate given the paid-course model; jurisdiction-specific formation required"

  civic:
    political_coalition: "Historical society, heritage-tourism board, or arts-council support required; municipal or county endorsement as a cultural-preservation facility; potential partnership with a living-history venue or heritage-tourism destination that already has visitor infrastructure; without an institutional partner, the civic argument rests on a thin cultural-preservation claim that most councils will not fund as a standalone line item"
    council_vote_estimate: "Uncertain; cultural-preservation arguments succeed when tied to measurable tourism revenue or an existing heritage venue; standalone civic charcoal forge with no visitor destination attached is unlikely to achieve majority support; estimated 3-4 marginal votes contingent on heritage-tourism partnership documentation"
    competes_with_private: "No private traditional-charcoal smith is likely to be operating in most target markets; the civic entry does not displace a functioning private operator; it fills a cultural-preservation gap that the market cannot sustain — but the gap is a cultural-access gap, not a repair-services gap, which is a weaker public-goods argument"
    governance_form: "Heritage-society or municipally-owned facility operated by a part-time demonstrator (not a full production smith) under contract to a historical society or arts organization; contracted master smith for scheduled workshops and special events; the governance form is closer to a museum living-history program than a production forge"
    budget_line: "Capital via heritage grant, historical-society endowment, or one-time municipal cultural-facilities allocation; annual operating costs under heritage-tourism, arts-and-culture, or living-history program line; ongoing funding is the primary viability risk — most cultural-preservation programs face annual budget uncertainty"
    benchmark_comparison: "[CITATION-NEEDED: per-visitor cost for comparable living-history demonstrations at heritage museums] At village scale (400 hh), annualized capital ($13,000 mid / 25 yr = $520/yr) plus install ($1,500 / 25 = $60/yr) plus operating ($600 maintenance + $2,800 consumables + $2,400 rent = $5,800/yr) = $6,380/yr total, or ~$16/hh/yr — below the corpus/program/SCALES.md village civic threshold of $120/hh/yr. However, per-visitor cost benchmarking against living-history programs is more relevant than per-household cost for this entry's use case; that comparison requires visitor-count data not available in the sources consulted."
    staffing_model:
      role: "part-time heritage demonstrator (operator of record) + contracted master smith for workshops"
      operator_fte: 0.5
      wage_assumption: 24000
      wage_source: "corpus/program/SCALES.md §3 village-scale skilled-trades median ($48,000/yr) at 0.5 FTE; part-time demonstrator role is below skilled-trades median but must account for specialized knowledge; figure is an estimate [CITATION-NEEDED: wage survey for heritage-craft demonstrators at living-history museums]"
      hours: "20 hrs/wk demonstration, open-house, and maintenance; contracted master supplement for scheduled workshops (not included in FTE)"
      hiring_notes: "Part-time heritage demonstrator hiring pool is thin; the role requires charcoal-forge competence plus public-facing demonstration skills; geographic radius for hiring is likely 50–100 miles; contracted master for workshops may need to travel further; succession and continuity are significant risks if the demonstrator position turns over frequently"
    civic_externalities:
      - "Cultural-preservation access: maintains a publicly observable working example of pre-industrial smithing methods in a format accessible to students, researchers, and heritage visitors who have no other point of access"
      - "Craft-knowledge documentation: a funded civic facility provides the operational continuity needed to document traditional charcoal-forge techniques in reproducible form — something a market-dependent private operator cannot sustain if customer demand dries up"
      - "Heritage tourism: demonstration forge at a heritage site generates incremental visitor attendance and associated local economic activity [CITATION-NEEDED: heritage-forge visitor-impact data]"

# ── SIMULATION PARAMETERS ─────────────────────────────────────────────────────

sim_params:
  cost_mean: 13000
  cost_sd: 3000
  throughput_units_equiv_per_year: 540
  variable_cost_per_unit: 5.19
  labor_hours_per_unit: 2.09
  downtime_fraction: 0.13
  lifespan_years: 20

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
  - ref: "Tylecote, R.F. 1992. A History of Metallurgy. 2nd ed. London: Maney Publishing. [Charcoal fuel consumption rates, hearth configurations, bellows mechanisms across pre-industrial smithing traditions.]"
  - ref: "Needham, Joseph. 1958. The Development of Iron and Steel Technology in China. London: Newcomen Society. [Song-era iron production at village scale; fuel regimes; scale of operation.]"
  - ref: "Tatsuo, Inoue. 2000. 'Japanese Swordsmithing and the Tamahagane Process.' Bulletin of the Metals Museum (Japan). [Fuigo bellows mechanism, charcoal requirements, and throughput constraints in Japanese traditional smithing; cited for bellows and fuel-regime data only.]"
  - ref: "Birch, Samuel. 1872. 'On the Uses of the Bellows in Antiquity.' Archaeologia 43: 1–20. [Historical bellows mechanisms; cited for context on hand-bellows operational characteristics.]"
  - ref: "corpus/program/SCALES.md v1.0 (2026-04-18). Village-scale skilled-trades median wage $48,000/yr; civic cost threshold $120/hh/yr."
  - ref: "catalog/smithing/SCHEMA.md v1.0 (schema_base_version 1.1). Charcoal energy-source table (3–5 kg/hr range); operator-skill-floor definitions; first_year_failures reference list for bellows mechanism and refractory."
  - ref: "research/trades/smithing/REQUIREMENTS.md v1.0 (2026-04-18). R-08 fuel regime options; R-06 throughput ceiling guidance; DIV-01 charcoal sustainability documentation requirement."
  - ref: "docs/STYLE-GUIDE.md §4.2 (2026-04-18). Anti-romanticism: charcoal sustainability claims require quantified citation; deforestation impact of historical charcoal production must be acknowledged if sustainability framing is used."
  - ref: "[CITATION-NEEDED: willingness-to-pay survey for traditional-method smithed goods — heritage-craft premium pricing figures are inferred from analogy to hand-thrown pottery and hand-woven textiles; no direct smithing survey identified; pricing validation type: structural inference only.]"
  - ref: "[CITATION-NEEDED: charcoal retail price for small commercial buyers in rural US, 2024–2025 — $2,800/yr consumables is derived from 3 kg/hr × 25 active hr/wk × 47 productive wk/yr ≈ 3,525 kg/yr at an estimated $0.79/kg; modern bagged charcoal prices in small-quantity commercial purchase are not well-surveyed in the sources consulted; figure requires direct market verification.]"
  - ref: "[CITATION-NEEDED: specific US regulatory thresholds for charcoal combustion emissions at village/rural scale; OSHA 29 CFR 1910.252(c) cited for hot-work ventilation; local air-quality district particulate thresholds vary by jurisdiction.]"
  - ref: "[CITATION-NEEDED: per-visitor operating cost for comparable living-history forge demonstrations at heritage museums — needed to complete the civic benchmark_comparison for this entry; no comparable dataset identified in sources consulted.]"
  - ref: "[CITATION-NEEDED: wage survey for heritage-craft demonstrators at living-history museums — the $24,000/yr (0.5 FTE) figure is derived from the SCALES.md village skilled-trades median; a direct survey of demonstrator compensation at heritage sites would strengthen this estimate.]"
---

## Summary

Forge-008 is a charcoal-fired, hand-bellows smithing shop aimed at a specific and narrow commercial segment: buyers who specifically require goods produced using traditional methods (charcoal fuel, hand-bellows air supply, traditional forging sequences) and are willing to pay a premium for that production method rather than for the object alone. The entry is not a general-purpose village smithy. Its low capital cost ($8,000–$20,000) is matched by low throughput (approximately 540 medium-work-equivalent units per year at full operation) and high variable costs driven by modern charcoal pricing. All three lenses rate this entry as marginal, and at all viable scales the market is thin. The entry exists in the catalog to test whether traditional-method production can sustain a commercial operation — and to document the specific constraints that make this test difficult.

## Design rationale

Every other coal or charcoal entry in the catalog uses mechanical air supply (electric blower motor). Forge-008 is the only entry that eliminates the blower entirely, relying on hand-operated or treadle-operated bellows — the fuigo box-bellows or a traditional European lever bellows. This matters because the blower motor is the primary power-consumption and noise source in a conventional solid-fuel forge, and its elimination changes the operational profile materially: noise drops to 70 dB (vs. 85 dB for blower-assisted designs), CO risk shifts from steady-state combustion to periodic bellows-rest moments, and throughput becomes physically limited by operator fatigue rather than by fuel-feed rate or hearth capacity. No other entry in the current catalog occupies this cell. The entry also tests the hypothesis that traditional-method production can command a durable premium over industrial goods in a specific hobbyist/heritage market segment — a question that the repair-dominant entries (forge-005) and specialty entries (forge-006, forge-007) do not address, because those entries do not depend on a purist customer base.

## Historical lineage

Charcoal-fired hand-bellows smithing is often described as "how blacksmithing was done" before industrialization. That framing is incorrect. Traditional small-village charcoal forges coexisted throughout history with larger-scale charcoal-fueled industrial ironworks, with blower-assisted bellows at production forges, and with coal adoption wherever coal was available and affordable [Tylecote 1992, ch. 8–9]. The fuigo box-bellows in Japan and the traditional European lever bellows were not universal defaults; they were the forms chosen in specific contexts defined by local fuel availability, capital constraints, and labor regimes. Song-era Chinese village smithing operated at charcoal-fired village scale while simultaneously coexisting with state-operated blast furnaces processing thousands of tonnes of iron per year [Needham 1958]. The historical choice of hand bellows over blower-assisted bellows was typically a capital or fuel-access constraint, not a quality preference — in most production contexts, a more powerful and consistent air supply produces more controllable forge temperatures and higher throughput. Where the traditional hand-bellows form persisted, it persisted because the alternatives were unavailable or unaffordable, not because the method was inherently superior. The modern revival context inverts this: an operator choosing hand bellows today is making a deliberate capital-constrained or method-purist choice in a market where blower motors are cheap and widely available. The functional inheritance this entry carries forward from historical precedents is limited: the hearth geometry, charcoal fuel management, and basic bellows mechanics are functionally continuous with historical forms [Birch 1872; Tatsuo 2000]. The labor regime — one operator working hand bellows without apprentice household labor — is not historically typical; most historical accounts of single-operator village forges include at least one additional household member or apprentice working the bellows while the smith worked the iron. A modern single-operator hand-bellows forge concentrates both functions in one person, which is why the throughput ceiling (30 hr/wk gross, 25 hr/wk net) is substantially lower than historical output figures that implicitly assume shared labor [CITATION-NEEDED: quantified historical throughput data for single-operator vs. dual-operator charcoal forges; most historical accounts do not separate the operator's labor from bellows labor].

## Key assumptions

Capital-cost range ($8,000–$20,000, mid $13,000) reflects the low-technology equipment profile: a fabricated or purchased charcoal hearth or clay-and-brick forge pot ($800–$2,500), anvil ($800–$2,500), traditional bellows (fuigo kit or fabricated: $500–$2,000), stand and tooling ($800–$2,000), hood and chimney ($600–$1,500), charcoal storage bin ($300–$800), hand tools and tongs ($500–$1,500), and fit-out contingency ($1,200–$4,000). [CITATION-NEEDED: equipment price survey for traditional charcoal-forge components; figures are consistent with specialty smithing-supplier price lists and materials costs as of 2024–2025 but have not been cross-checked against a formal survey.] The mid ($13,000) is below the arithmetic mean of low and high ($14,000), reflecting that a competent low-capital operator sourcing secondhand or self-fabricating the hearth can reach functional operation below midpoint. Annual consumables ($2,800) are derived from: 3 kg charcoal/active hr × 25 net active hr/wk × 47 productive wk/yr ≈ 3,525 kg/yr charcoal; at an estimated $0.79/kg for bagged commercial charcoal in small commercial quantities, that is approximately $2,785 — rounded to $2,800. [CITATION-NEEDED: charcoal retail price per source entry.] Modern charcoal pricing is the central economic constraint of this entry: at $0.79/kg, charcoal costs approximately 4–5× more per unit of thermal energy than coal at comparable quantities, which directly drives the high variable_cost_per_unit and the requirement for a substantial market premium. Throughput calculation: weighted unit equivalent = 0.25 × 0.5 (repair, medium) + 0.05 × 2.0 (commodity, small) + 0.45 × 0.5 (specialty, medium) + 0.25 × 0.1 (artistic, large) = 0.125 + 0.10 + 0.225 + 0.025 = 0.475 units/hr equiv. Derated hours: 25 hr/wk × 52 × (1 − 0.13) = 25 × 52 × 0.87 = 1,131 hr/yr. Annual throughput: 1,131 × 0.475 = 537 units/yr, rounded to 540. variable_cost_per_unit = $2,800 / 540 = $5.19. labor_hours_per_unit = 1,131 / 540 = 2.09. Cross-check: 540 × 2.09 = 1,129 ≈ 1,131 ✓. cost_sd = (20,000 − 8,000) / 4 = 3,000. Downtime fraction (0.13) reflects: bellows leather failure at ~1,200 hr (14-day lead time, ~6% of annual hours in worst-case replacement scenario), refractory patches, seasonal charcoal supply delays, and hand-bellows fatigue limits reducing effective weeks. lifespan_years (20) is shorter than coal-forge entries (25 yr) because traditional bellows mechanisms have shorter service lives than mechanical blowers and clay/brick hearth construction typically requires earlier full reconstruction than a cast-iron fire pot.

## Known risks / failure modes

**Regulatory.** Charcoal combustion is less regulated than coal in most US rural and village-scale jurisdictions, but it is not unregulated. CO accumulation is the primary life-safety hazard; a dedicated exhaust system is not optional. In jurisdictions with aggressive particulate controls, charcoal smoke from an open-bay forge may trigger permit requirements that add cost and delay. The sustainability documentation requirement (SCHEMA.md §2, DIV-01) is a reputational and, in some jurisdictions, a permit risk: if the charcoal supply chain cannot demonstrate managed-forest sourcing, the entry's environmental profile is worse than a natural-gas forge on lifecycle CO2 grounds [STYLE-GUIDE §4.2]. An operator who cannot document charcoal supply chain provenance should not make any sustainability claims for this configuration.

**Labour pipeline.** Hand-bellows operation is physically demanding in ways that restrict the hiring pool. The operator must be able to sustain upper-body work at moderate intensity throughout active forging periods; operators with relevant physical limitations are not candidates for this role. The skill set required (charcoal fire management, hand-bellows rhythm, traditional forging sequences, purist-customer relationship) is narrower than for a coal or propane forge and the available hiring pool is correspondingly thinner. Succession risk is high: this shop's commercial viability depends entirely on the incumbent operator's ability to find and cultivate a customer base that values traditional-method production; that customer base does not transfer automatically to a replacement operator. An apprentice who completes training but cannot independently develop the specialist market relationship is a succession failure even by competence criteria.

**Supply chain.** Commercial charcoal is the primary consumable dependency, and modern charcoal pricing reflects a retail-market product with no large-scale industrial buyer base for metallurgical-grade small-quantity charcoal. A single-supplier relationship with a regional charcoal distributor is the most likely procurement arrangement at village scale; worst-case lead time (30 days) reflects a scenario where the primary supplier is out of stock and an alternative must be identified. There is no backup fuel for this entry (backup_fuel: null): the design is specifically predicated on charcoal combustion, and switching to coal or propane mid-operation would require hearth modifications. A charcoal supply disruption of more than 3–4 days shuts the shop. The operator should maintain 3–4 weeks of charcoal inventory at all times. Bellows leather is the secondary supply dependency: specialty bellows leather or traditional hide may have lead times of 14 days or longer from specialty suppliers; a stocked replacement kit on hand is essential.

**Market.** The traditional-method premium is the entry's central commercial assumption, and it is the least empirically grounded number in the entry. The customer base for goods specifically produced using charcoal and hand bellows is a hobbyist, heritage, and collector segment that is present in concentrated form at craft events, historical re-enactment gatherings, and heritage tourism sites — and is nearly absent from general commercial contexts. A village-scale shop dependent on this segment requires either a local concentration of that customer base (which is statistically improbable in most villages) or a regional reach through events, online sales, or an institutional anchor (heritage museum, historical society). Without one of these, the entry functions as a hobby with occasional paying customers rather than a commercial operation. This is not a failure of the equipment design; it is a structural feature of the target market.

## Iteration log

- 2026-04-18: v0.1 — initial entry authored per Plan C Task 10. Charcoal fuel, hand-bellows configuration, all lenses marginal, all viable scales marginal. Anti-romantic framing applied throughout: historical coexistence of traditional and scale production named; modern charcoal cost constraint named explicitly; purist customer base described as thin and structurally limited; hand-bellows fatigue and throughput ceiling documented as the binding operational constraint. No docs/superpowers/ paths used. [CITATION-NEEDED] markers placed on pricing, charcoal cost, emissions thresholds, visitor-impact data, and heritage-demonstrator wages per citation policy.
