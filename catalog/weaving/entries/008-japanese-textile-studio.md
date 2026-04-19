---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: weave-008
trade: weaving
name: "Japanese-Style Textile Studio"
tagline: "Master-weaver small-city studio producing Japanese-aesthetic cloth via dobby-assisted 8-shaft floor loom — mon-weave patterns, geometric kasuri-adjacent, modern Tokugawa adaptation without draw loom"
status: draft
version: 0.1
supersedes: null
inspirations:
  - tokugawa-nishijin-mon-weave-silk
  - echigo-chijimi-ramie-crepe-tradition
  - meiji-era-jacquard-floor-loom-adaptation

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 40
ceiling_min_m: 2.7
ventilation: natural-sufficient

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: electric-lighting-only
energy_consumption_per_active_hour: "2 kWh (studio lighting + humidity management; no powered loom mechanism)"
backup_fuel: null

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  meters_per_day: 2.5
  warp_width_cm: 120
  pattern_complexity: pattern
  max_active_hours_per_week: 34
  product_mix:
    yardage: 60
    rugs_upholstery: 0
    tapestry_art: 0
    garments_accessories: 30
    instruction_open_studio: 10
  throughput_variance:
    seasonal: "Commission and gallery placement work is non-seasonal; retail yardage and accessories peak Oct-Dec and early spring for kimono-adjacent and gift markets."
    worst_month_fraction_of_average: 0.65
    best_month_fraction_of_average: 1.40

# ── TRADE-SPECIFIC ───────────────────────────────────────────────────────────

trade_specific:
  loom_type: floor-loom-8shaft
  humidity_control_required: true
  fiber_source_declaration: industrial-yarn-purchased

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: master-weaver
operators_concurrent: "1-2"
apprentice_friendly: true
apprentice_path:
  training_stages: "Stage 1 (0-6 mo): loom mechanics, warping protocol, plain weave and basic 4-shaft twill on studio equipment under direct supervision; humidity management and silk handling. Stage 2 (6-18 mo): 8-shaft threading and tie-up, standard mon-weave pattern execution, shuttle management for fine silk and Tencel; journeyman gate at 18 months requires independent warp setup and error-free 8-shaft plain-to-pattern transitions. Stage 3 (18-36 mo): full dobby sequence programming, repeat-pattern design adaptation, geometric kasuri-adjacent warp spacing calculations, customer commission workflow; independent operation gate at 36 months for production yardage; master-tier original pattern design requires additional 2-4 years post-journeyman."
  time_to_independent_operation: "~36 months to journeyman standard capable of independent production yardage on established patterns; master-tier original design vocabulary requires 5-8 years of total practice"
  succession_note: "Apprentice co-presence during production sessions integrates technical skill transfer into normal operations; pattern-design and Japanese aesthetic vocabulary require extended mentorship beyond journeyman production competence"

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD
  capital_cost: { low: 20000, mid: 40000, high: 70000 }
  install_cost: 4500
  annual_maintenance: 2800
  annual_consumables: 11000
  floor_space_rent_per_year: 10200
  market_price_per_unit: { low: 120, mid: 300, high: 800 }
  industrial_baseline_price: 20
  pricing_notes: "Per meter of woven cloth (120 cm width). Industrial baseline ($20/m) reflects imported Japanese-aesthetic fabric — machine-woven cotton or poly-blend fabric with printed mon or kasuri-style motifs at wholesale [CITATION-NEEDED: imported Japanese-aesthetic fabric wholesale price — confirm via textile importer price lists or wholesale fabric marketplace data, 2024-2025]. Low end ($120/m) represents standard dobby-pattern Tencel or cotton yardage to boutique wholesale or DTC; mid ($300/m) represents silk-blend or pure-silk mon-weave yardage to curated retail, gallery, or DTC; high ($800/m) represents complex-pattern fine-silk to high-end DTC, fashion designers, or ceremonial commissions. Customer segment: slow-fashion consumers, Japanese-aesthetic lifestyle buyers, independent fashion designers sourcing distinctive handwoven cloth, interior designers seeking feature-fabric yardage, and gift buyers in small-city cultural-retail markets."
  pricing_validation: "Market price evidence: Etsy and independent studio rate cards (2024-2025) for handwoven silk and Japanese-aesthetic cloth; comparable operator financials cited in Handweavers Guild of America member surveys (2023); Textile Society of America marketplace documentation for handwoven specialty cloth. Evidence type is comparable-sales and operator-financial — not cost-plus. The premium (15x at mid over industrial baseline) reflects hand-weaving provenance, custom pattern, and Japanese-aesthetic differentiation in a Western luxury category. [CITATION-NEEDED: Handweavers Guild 2023 survey; TSA marketplace data — confirm access and applicability]"

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:
  first_year_failures:
    - item: "Dobby mechanism malfunction (peg-and-lever lint accumulation)"
      estimated_hours_to_failure: 2200
      replacement_cost: 350
      replacement_lead_time_days: 14
      serviceable_by: journeyman
    - item: "Heddle breakage (texsolv, 8-shaft set)"
      estimated_hours_to_failure: 900
      replacement_cost: 90
      replacement_lead_time_days: 7
      serviceable_by: operator
    - item: "Climate-control / humidifier failure"
      estimated_hours_to_failure: 2500
      replacement_cost: 480
      replacement_lead_time_days: 7
      serviceable_by: journeyman
    - item: "Warp beam ratchet / pawl wear"
      estimated_hours_to_failure: 2000
      replacement_cost: 200
      replacement_lead_time_days: 12
      serviceable_by: journeyman

  maintenance_schedule:
    daily:
      task: "Check warp tension and humidity sensor reading; clear shed lint and broken ends; log meters woven and any defect incidents; verify shuttle and bobbin stock for next session"
      performed_by: operator
    weekly:
      task: "Inspect dobby peg sequence and lever action for sticking; check treadle tie-ups and lam cords; clean reed dents; inspect silk or fine-yarn warp for any tension irregularities caused by humidity fluctuation"
      performed_by: operator
    quarterly:
      task: "Full dobby mechanism cleaning (remove lint and fiber debris from peg board and lever pivots); inspect ratchet-and-pawl beam tensioning; oil moving joints; check brake band; verify humidifier reservoir and filter; inspect heddle condition across all 8 shafts"
      performed_by: journeyman
    annual:
      task: "Full loom inspection: castle bolts, beam bearings, treadle pivot points, dobby mechanism overhaul; replace worn heddle sets in bulk; recalibrate humidity sensor; full HVAC or humidifier service"
      performed_by: specialist

  startup_shutdown_overhead_per_day_min: 30
  max_active_hours_realism_note: "34 hr/wk is the theoretical active-weaving ceiling for a full-time studio weaver working 5 days per week with silk and fine-yarn warps; 8-shaft and dobby pattern setup is more demanding than plain weave and reduces net loom time. Warping and loom-dressing for a new fine-silk warp consumes 6-10 hours of setup per warp change (typically every 3-5 weeks), excluded from max_active_hours_per_week but included in the 235 annual operating-day estimate. Net of 30 min/day startup-shutdown overhead (5-day week), effective loom time ~31.5 hr/wk. sim_params.throughput_units_equiv_per_year uses 235-day × 2.5 m/day base rate derated by downtime_fraction."
  interruption_notes: "DTC and gallery channel management (photography, correspondence, order fulfillment, social media) consumes 5-8 hr/wk and is not reflected in max_active_hours_per_week, which counts loom time only. At 1-2 operators, administrative burden must be shared with production time or treated as additional operator contribution."
  consumables_lead_time_days: { typical: 10, worst: 60 }
  throughput_variance:
    seasonal: "Commission and gallery placement work is non-seasonal; retail yardage and accessories peak Oct-Dec and early spring for kimono-adjacent and gift markets."
    worst_month_fraction_of_average: 0.65
    best_month_fraction_of_average: 1.40

  operator_impact:
    noise_db: 63
    heat_exposure: "Ambient studio temperature; no heat hazard from weaving equipment; climate-control system may generate localized warm or cool airflow near humidifier unit"
    emissions: "Near-zero; no combustion; fine silk and Tencel fiber particulate in studio air requires routine ventilation; no regulatory emissions threshold triggered at this scale"
    physical_demand: "Moderate sustained seated posture; repetitive treadle and dobby motion; fine yarn handling requires precision hand work; ergonomic risk for wrist, shoulder, and neck with sustained production pace; standing during warping, loom dressing, and finishing"

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Light commercial, live-work, or mixed-use zoning sufficient; no industrial zoning required; DTC or gallery retail activity may trigger home-occupation or retail-permit requirements depending on jurisdiction"
  emissions: "No emissions permit required; fine fiber particulate is below regulatory thresholds for this studio scale; standard commercial building ventilation adequate"
  other: "Standard business registration and seller's permit required for DTC and wholesale; no weaving-specific occupational license in most jurisdictions; humidity-control equipment (residential-scale units) is standard building equipment with no special permit"

# ── CONTEXT FIT ──────────────────────────────────────────────────────────────

lens_fit:
  market: good
  cooperative: marginal
  civic: marginal

scale_fit:
  village: poor
  town: marginal
  small_city: good

# ── LENS CONTEXT ─────────────────────────────────────────────────────────────

lens_context:
  cooperative:
    membership_boundary: "Practicing weavers and fiber artists in the small-city metro area with a demonstrated interest in Japanese-aesthetic or East Asian textile traditions; membership by annual dues plus portfolio review to ensure minimum journeyman-weaver competence on multi-shaft equipment; production access not available to rigid-heddle-novice members"
    rules_source: "Bylaws; member vote to amend at semi-annual meeting with 2/3 majority"
    monitoring: "8-shaft and dobby loom usage logged per session via sign-in; humidity management system checked and logged weekly; quarterly review by elected steward of equipment condition and scheduling conflicts"
    graduated_sanctions: "Verbal reminder → written warning → 30-day loom-access suspension → membership review and potential termination for equipment misuse or silk-yarn waste"
    conflict_resolution: "Elected steward mediates scheduling and equipment disputes; appeal to full member vote at next semi-annual meeting"
    ostrom_principles_addressed: [1, 2, 3, 4, 5, 6]
    member_amendment_process: "2/3 vote at semi-annual general meeting; 21-day advance notice required; emergency bylaw change requires 3/4 vote with 7-day notice"
    legal_form: "State-registered worker cooperative or LLC; cooperative form preferred to enable member equity and shared brand identity"
    scale_fit_note: "Rules calibrated for small-city scale with 5-10 active members sharing 1-2 floor looms; governance and quorum infeasible at village scale where member pool with master-level Japanese-textile skill cannot be sustained"

  civic:
    political_coalition: "Small-city arts and cultural-economy development office + Japanese-American cultural organization or Japan Society chapter (where present) + independent textile arts advocates; municipal small-business development grant as funding pathway"
    council_vote_estimate: "Likely 4-3 or 5-2 favorable in a culturally diverse small city; opposition argues niche audience size and public-subsidy appropriateness for a luxury-category trade"
    competes_with_private: "This entry is calibrated as market-primary; a civic version would need to operate as an education and cultural-access facility rather than a direct production competitor; no significant private Japanese-textile studio operator is likely in most small-city markets, so civic displacement risk is low"
    governance_form: "If civic: municipally sponsored cultural-arts studio; operated by contracted master weaver with apprentice program under arts and culture department; production yardage sales partially offset operating cost"
    budget_line: "Capital via cultural-infrastructure or arts-facility bond or grant; operations under arts and cultural programming line or workforce-development line with partial cost recovery from yardage sales and workshop fees"
    benchmark_comparison: "$3.80/hh/yr at small-city scale (20,000 households, $76,000 operating cost estimate including master-weaver salary at $62,000 + consumables + maintenance) vs. small-city arts center at $18-28/hh/yr and community library at $38-55/hh/yr in peer towns — substantially below comparable civic cultural services [CITATION-NEEDED: peer small-city arts facility cost-per-household — confirm with municipal budget data or arts council survey]"
    staffing_model:
      role: "contracted master weaver with 1 apprentice (part-time)"
      operator_fte: 1.2
      wage_assumption: 62000
      wage_source: "corpus/program/SCALES.md §3 small-city-scale skilled-trades and arts professional median; adjusted upward for master-weaver specialty skill scarcity [CITATION-NEEDED: confirm SCALES.md small-city arts-professional wage band]"
      hours: "40 hrs/wk production + instruction + administration; apprentice contributes 20 hrs/wk"
      hiring_notes: "Master-weaver with Japanese-textile specialty is a thin hiring pool; geographic radius for search is likely regional to national; apprentice hired locally from craft or textile arts program pipeline"
    civic_externalities:
      - "Cultural access and education: public workshop program provides accessible entry point to Japanese textile traditions and multi-shaft weaving skill for small-city residents without private-studio pricing barrier"
      - "Apprentice training pipeline: produces 1 journeyman weaver per 3-year cycle with Japanese-textile specialty, preserving a rare technical tradition in the regional craft economy"
      - "Cultural diplomacy and identity: visible Japanese-aesthetic studio in a small-city cultural district can support Japanese-American community identity and cultural exchange programming"

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 40000
  cost_sd: 12500
  throughput_units_equiv_per_year: 499
  variable_cost_per_unit: 48.00
  labor_hours_per_unit: 3.06
  downtime_fraction: 0.15
  lifespan_years: 20

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
  - ref: "Morris-Suzuki, Tessa. 1994. The Technological Transformation of Japan. Cambridge University Press. [Tokugawa and Meiji textile technology; Jacquard adoption in Nishijin; draw-boy elimination — primary historical reference for Japanese-loom lineage claims]"
  - ref: "Leupp, Gary P. 1992. Servants, Shophands, and Laborers in the Cities of Tokugawa Japan. Princeton University Press. [Nishijin labor regime; detchi-boko apprenticeship; ton'ya merchant control — primary reference for Nishijin organizational form]"
  - ref: "Kuhn, Dieter. 1988. Science and Civilisation in China, vol. V pt. 9: Textile Technology — Spinning and Reeling. Cambridge University Press. [Draw-loom mechanics and historical context — cross-reference for Japanese draw-loom lineage]"
  - ref: "Handweavers Guild of America, Member Studio Survey 2023 — income and pricing data for professional studio weavers [CITATION-NEEDED: confirm publication and access]"
  - ref: "Textile Society of America, Marketplace Pricing Documentation 2024 — handwoven cloth per-meter rates for specialty and luxury categories [CITATION-NEEDED: confirm publication and access]"
  - ref: "Ashford Wheels & Looms / Schacht Spindle Company / Leclerc Looms, dealer price lists 2024 — floor-loom-8shaft capital cost range; dobby attachment pricing [CITATION-NEEDED: current pricing confirmation from dealer sources]"
  - ref: "research/trades/weaving/REQUIREMENTS.md — throughput ranges, loom capability, operator skill definitions, footprint guidance, anti-romanticism framework for Japanese textile entries"
  - ref: "research/trades/weaving/HISTORICAL-FORMS.md — Tokugawa-period loom types, cloth standards (tan width), Nishijin organizational form, draw-loom vs. treadle-loom distinction"
  - ref: "research/trades/weaving/DECLINE-VERDICT.md — niche targeting; fiber-sourcing falsifier; Nishijin restructuring pathway and its conditions; commodity-cloth exclusion criteria"
  - ref: "[CITATION-NEEDED: imported Japanese-aesthetic fabric wholesale price — textile importer or wholesale marketplace data, 2024-2025; load-bearing for industrial_baseline_price claim]"
---

## Summary

The Japanese-Style Textile Studio (weave-008) is a master-weaver studio producing Japanese-aesthetic cloth using an 8-shaft floor loom with a dobby attachment — mon-weave repeat patterns, geometric structures derived from kasuri-adjacent spacing logic, and simple warp-manipulation ikat effects achievable without a draw loom. The entry is calibrated for a small-city market-primary model: one to two operators, a studio footprint of 30-50 m², Japanese-spun silk thread, Tencel, and fine cotton sourced as industrial yarn. It is distinct from every other entry in the weaving catalog: weave-001 (Tapestry) produces art objects; weave-004 (Fashion Atelier) produces garment yardage in Western aesthetic traditions; weave-006 (Traditional Revival) is a civic-primary heritage entry for named indigenous traditions. Weave-008 is the only entry occupying the Japanese-aesthetic luxury-yardage niche, and it is designed as a modern-adaptation entry — not a historical recreation. Its economic viability rests on a premium 15x over imported industrial Japanese-print fabric, supported by handwoven provenance, custom pattern, and access to a small but deep Western luxury market for Japanese-aesthetic cloth.

## Design rationale

No other entry in the weaving catalog addresses the Japanese-aesthetic premium-yardage position. The design challenge this entry solves is: how to produce cloth that carries recognizable Japanese textile aesthetics — the structured repeat patterns of mon-weave, the spatial geometry of kasuri ikat — using an 8-shaft floor loom equipped with a mechanical dobby, without the draw loom that produced the historical Nishijin brocade form. The answer is a functional narrowing: this entry cannot produce the full figured-brocade output of a Nishijin draw loom, and it does not claim to. What it can produce is a class of Japanese-inspired geometric and mon-weave pattern cloth — structured, recognizable, premium-positioned — using technology that does not require a draw-boy, does not require a draw loom, and is achievable by a master weaver working a modern 8-shaft floor loom. The dobby attachment replaces the mechanical treadle-tie-up sequence for multi-shaft pattern weaves, reducing error rate and enabling more complex 8-shaft pattern cycling without requiring Jacquard-card automation. This is a genuine middle position between historical reproduction and generic handwoven cloth, and it is the position this entry claims. The market opportunity is a Western luxury consumer segment that purchases "Japanese textiles" as a lifestyle and aesthetic category; the entry's viability analysis must confront the fact that this is a Western construction, not a direct continuation of the Tokugawa trade.

## Historical lineage

Three functional precedents inform this entry, and the lineage must be stated honestly per THEORY §6.

**Tokugawa Nishijin luxury-silk weaving** is the primary historical reference. Nishijin (Kyoto) produced the most technically sophisticated woven silk in Tokugawa Japan: *nishiki* (brocade), *rinzu* (figured satin), elaborate *obi* sash work. The production form used the *sorahiki-bata* draw loom with a draw-boy operating pattern heddles from above — a two-operator system requiring both a master weaver and an adolescent pattern operator [Leupp 1992]. The patronage base was samurai households, imperial court, and Buddhist institutions; the *ton'ya* wholesale merchants controlled raw-silk supply and distribution channels [Morris-Suzuki 1994]. **What this entry carries forward functionally:** the premium-per-meter pricing structure, the direct-to-customer and gallery sales channel, and the role of pattern complexity and Japanese aesthetic vocabulary in sustaining price premiums over commodity cloth. **What this entry explicitly does not carry forward:** the draw loom, the draw-boy labor, the *ton'ya* merchant credit dependency, the indenture-based *detchi-boko* apprenticeship, the Kyoto geographic concentration, and the samurai-patronage demand base. The Nishijin form required all of these to operate as it historically operated; none are reproducible in a modern small-city Western context. The iconic Nishijin brocade product — full figured-weave brocade with unlimited repeat complexity — cannot be produced on a modern floor loom. This entry makes a modern-adaptation claim, not a historical-reproduction claim.

**The Meiji-era Nishijin Jacquard transition** is the closer functional analogy. The 1872 Lyon mission and subsequent adoption of the Jacquard mechanism by Nishijin weavers replaced draw-boy pattern selection with punched-card automation, reduced the operator complement to one, and preserved Nishijin's market position through technological reorganization — not through preservation of the pre-Meiji form intact [Morris-Suzuki 1994]. This entry follows an analogous logic: a dobby attachment on an 8-shaft floor loom replaces the complex multi-shaft treadle-tie-up sequence, reducing error and enabling more complex pattern cycling. The analogy is not exact — the dobby is far less capable than a full Jacquard mechanism — but the principle of function-preserving technological substitution is the same. The Meiji adaptation is the correct precedent for what this entry is attempting; the Tokugawa draw-loom form is the historical lineage, not the operational model.

**Echigo-chijimi ramie crepe** is cited as a secondary precedent for the regional-specialty positioning logic: fine ramie cloth produced by skilled women weavers in the cold-climate Echigo region (now Niigata Prefecture), sold through Edo merchant networks at premium prices for its distinctive texture and regional origin identity. The functional inheritance is the role of regional-specialty identity (specific fiber, specific technique, identifiable origin) in supporting premium pricing against commodity cloth [CITATION-NEEDED: Echigo-chijimi production and market — specialist Japanese textile-history source]. This precedent is relevant to the marketing logic, not the loom technology; the entry uses an 8-shaft floor loom, not the Echigo narrow-cloth loom form.

**Anti-romanticism note (THEORY §6).** "Japanese textiles" as a Western luxury category is a modern construction. The Nishijin brocade form that anchors most Western consumers' image of Japanese luxury textile required full draw looms and draw-boy operators — labor and equipment forms that are historical, not modern. The kasuri (ikat) tradition that anchors Japanese folk-textile aesthetics required elaborate warp-resist dyeing with tight registration that a floor loom alone does not provide (kasuri dyeing must be done before weaving, as a separate upstream step). This entry does not reproduce either form. It produces Japanese-inspired geometric and mon-weave pattern cloth on modern equipment, positions it honestly as a modern adaptation, and claims the aesthetic category and premium-pricing position that that positioning supports — not historical authenticity it cannot deliver.

## Key assumptions

Capital cost range ($20,000-$70,000) derives from 8-shaft floor loom pricing (Ashford, Schacht, Macomber, or Leclerc 8-shaft models at $4,000-$12,000 base) plus dobby attachment ($1,500-$3,500 for mechanical dobby; $3,000-$8,000 for electronic), warping equipment, bobbin winder, humidity management (standalone humidifier/dehumidifier unit at $400-$1,200 for studio-scale; HVAC-integrated system at $3,000-$8,000), and studio build-out or improvement. Low end ($20,000) assumes a used quality 8-shaft loom with basic mechanical dobby and standalone humidity unit; high end ($70,000) assumes new top-tier loom, electronic dobby, full climate-control installation, and second smaller loom or warp-winding equipment. [CITATION-NEEDED: 8-shaft floor loom + dobby attachment current dealer pricing — confirm from Ashford, Schacht, or Leclerc dealer lists 2024.] Install cost ($4,500) covers electrical for studio lighting and humidity management, any floor reinforcement for loom weight, and initial setup labor. Annual consumables ($11,000) assume approximately $9,200 in yarn purchases (Japanese-spun silk thread, Tencel, and fine cotton at commercial wholesale rates for ~499 m/year production) plus $1,800 in warp-related materials (sizing, finishing agents, auxiliary materials). Variable cost per unit ($48/m) derives from yarn cost ($9,200 / 499 m ≈ $18.44/m) plus finishing and packaging ($4.50/m) plus energy and supplies ($2/m) plus downtime-adjusted labor overhead ($23/m at imputed $20/hr for master-weaver labor costing); this is the direct variable cost for simulation, not the full operator compensation. Annual maintenance ($2,800) covers loom servicing, dobby mechanism cleaning, humidity system maintenance, and heddle/tie-up replacement on normal wear schedule. Throughput (499 m/year) is derived from 2.5 m/day × 235 operating days × (1 - 0.15 downtime); 235 operating days accounts for warping setup days (approximately 22-28 days/year not spent weaving on 8-shaft fine-silk warps), holidays, and scheduled maintenance. The 2.5 m/day central estimate for pattern-complexity cloth on an 8-shaft floor loom with dobby is consistent with the SCHEMA.md throughput guidance for pattern/overshot weave (1-3 m/day) and reflects the additional time for dobby peg-board setup and silk warp management relative to simpler weaves. E-3 throughput cross-check: 2.5 m/day × 235 days × 0.85 = 499 m/yr. Labor cross-check: 499 × 3.06 = 1527 hr ≈ 34 hr/wk × 52 × 0.85 = 1502 hr (consistent to within rounding and warping-day exclusion). sim_params.cost_sd ($12,500) = (70,000 - 20,000) / 4 = 12,500, per base-schema default derivation. Cost_mean ($40,000) equals economics.capital_cost.mid. Industrial baseline price ($20/m) reflects imported Japanese-aesthetic woven fabric (machine-woven cotton or poly-blend with printed or jacquard-woven mon or kasuri-style motif) at wholesale. [CITATION-NEEDED: confirm industrial baseline via textile importer price lists.]

## Known risks / failure modes

**Regulatory.** DTC retail and gallery consignment from a studio may trigger retail-permit and home-occupation compliance requirements in jurisdictions that restrict commercial activity in residential zones. Standard business registration and resale/seller's permit required for any wholesale or DTC channel. No unusual regulatory exposure at this studio scale.

**Labour pipeline.** This entry requires a master-weaver with Japanese-textile specialty — a skill combination requiring 8-12 years of weaving practice beyond initial training plus specific investment in Japanese pattern traditions and silk handling. This is a thin hiring pool in most Western small-city markets; a founding operator who is not already at this level cannot reach it on studio revenue alone within a viable launch timeline. The succession risk is real: a studio whose design identity depends on the founding weaver's personal aesthetic vocabulary does not automatically transfer to a successor even if a journeyman apprentice reaches production-level competence. Apprentice path (36 months to journeyman standard on production weaving) addresses technical succession but not design-identity succession. Named explicitly per Principle 9.

**Supply chain.** Japanese-spun silk thread and premium Tencel sourced for Japanese-aesthetic work may have longer lead times and higher price volatility than commodity yarn. Specialty Japanese silk thread (e.g., Habutai-weight or heavy crepe silk) may require international sourcing from Japanese specialty importers with 4-8 week lead times; worst-case lead time (60 days) reflects import shipping delays or supplier stock disruption. Maintaining a 2-3 month yarn inventory buffer is the primary mitigation; this requires working capital and storage space beyond the core studio footprint. A second fiber-supply risk is that the "Japanese-aesthetic" market positioning depends partly on using Japanese-spun or Japan-affiliated materials; if supply constraints force substitution to non-Japanese industrial yarn, the premium-pricing claim may weaken. This should be addressed in customer communication from the outset: the entry positions the claim on weave structure and aesthetic vocabulary, not on yarn-origin purity.

**Market fragility and category construction.** "Japanese textiles" as a Western luxury category is real but culturally constructed and fashion-dependent. The customer base is concentrated in urban and small-city arts-community markets with high sensitivity to Japanese-cultural programming and slow-fashion trends. A shift in Western consumer interest away from Japanese-aesthetic design would reduce addressable market size without warning. The 15x premium over industrial baseline is large; it is sustained only by a combination of hand-weaving provenance, pattern distinctiveness, and direct customer relationship. Boutique wholesale pricing (50% margin to retailer) requires a $600/m ex-factory price to achieve $300/m net at mid-market — making DTC the preferred channel for revenue quality but adding brand-building burden. The entry does not compete with actual Nishijin brocade or high-end Japanese textile imports; it occupies a price point below those ($300-$800/m vs. $1,000-$5,000+/m for authentic Nishijin) and above printed-fabric alternatives ($20/m). That middle position is viable but requires active positioning work.

## Iteration log

- 2026-04-18: v0.1 — initial creation for Plan I task 10. Entry authored per SCHEMA.md v1.1 and catalog/weaving/SCHEMA.md v1.0. Capital, throughput, and variable-cost figures are draft estimates pending citation confirmation on 8-shaft + dobby dealer pricing, Handweavers Guild survey data, and imported Japanese-fabric baseline price. Market price evidence flagged [CITATION-NEEDED] on three primary sources. Anti-romanticism note on Nishijin draw-loom vs. modern floor-loom capability distinction included in Design Rationale and Historical Lineage per THEORY §6. Throughput arithmetic: 2.5 m/day × 235 days × 0.85 = 499 m/yr; labor check: 499 × 3.06 = 1527 hr ≈ 34 hr/wk × 52 × 0.85 = 1502 hr (consistent to within rounding); cost_mean = capital_cost.mid = $40,000 (E-3 R1 satisfied); cost_sd = (70,000 - 20,000) / 4 = 12,500 (E-3 R5 satisfied at 12,500/40,000 = 0.31, within 0.15-0.50 range).
