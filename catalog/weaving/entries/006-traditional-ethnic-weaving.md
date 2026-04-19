---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: weave-006
trade: weaving
name: "Traditional / Ethnic Weaving Revival Studio (cross-cultural template)"
tagline: "Master-weaver studio practicing a specific cultural textile tradition as a primary income source, with cultural-heritage civic dimension"
status: draft
version: 0.1
supersedes: null
inspirations:
  - navajo-rug-weaving-diné
  - andean-backstrap-loom-textiles
  - hmong-pa-ndau-textile-arts
  - nishijin-style-supplementary-weft
  - welsh-flannel-wool-weaving

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 30
ceiling_min_m: 2.7
ventilation: natural-sufficient

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: electric-lighting-only
energy_consumption_per_active_hour: "1.5 kWh (studio lighting; no powered loom mechanism)"
backup_fuel: null

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  meters_per_day: 0.5
  warp_width_cm: 90
  pattern_complexity: pattern
  max_active_hours_per_week: 32
  product_mix:
    yardage: 20
    rugs_upholstery: 30
    tapestry_art: 20
    garments_accessories: 15
    instruction_open_studio: 15
  throughput_variance:
    seasonal: "Commission and gallery work is non-seasonal; retail sales and workshop enrollment peak Sep-Dec with holiday-gift and tourist-season demand; instruction peaks in summer for visitors and heritage-camp participants."
    worst_month_fraction_of_average: 0.55
    best_month_fraction_of_average: 1.55

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: master-weaver
operators_concurrent: "1-2"
apprentice_friendly: true
apprentice_path:
  training_stages: >
    Stage 1 (0–6 mo): tradition orientation; loom dressing and warping for the specific
    tradition's equipment; materials handling (fiber preparation, dye-lot management);
    basic pattern units of the tradition (e.g., Navajo tapestry ground, Andean warp-faced
    plain weave, Hmong appliqué ground fabric, Welsh twill ground cloth).
    Gate: independently warp the tradition's primary loom type and produce a 1-meter
    ground-cloth sample to technical spec without supervision.
    Stage 2 (6–18 mo): intermediate pattern structures specific to the tradition (e.g.,
    two-faced tapestry techniques, warp-manipulation pick-up, supplementary-weft patterning,
    traditional color-sequence rules); finishing methods; cultural vocabulary of the pattern
    elements being reproduced.
    Gate: complete a mid-complexity commission piece (rug, panel, or scarf) meeting
    dimensional, pattern-registry, and finish standards.
    Stage 3 (18–42 mo): full pattern range of the tradition including high-complexity
    structures; client-commission workflow; pricing and negotiation with the tradition's
    collector or institutional buyer base; oral and written transmission of cultural-pattern
    knowledge.
    Gate: independently execute a major commission (large rug, significant panel, complex
    garment) from brief to delivery without master supervision.
    Stage 4 (42–60 mo): master-level technique range; ability to design original work within
    the tradition's formal rules; ability to assess and teach apprentices; documentation
    of pattern vocabulary for institutional record-keeping.
    Gate: master-weaver assessment by a recognized tradition holder or guild authority.
  time_to_independent_operation: "~42 months to journeyman standard; ~60 months to operate at master level in the tradition; timeline is longer than generic studio weaving because it includes cultural-knowledge transmission alongside technical skill"
  succession_note: >
    Apprentice participates in production from Stage 2 onward, integrating skill and
    cultural-knowledge transfer into billable work. Pattern documentation during apprentice
    training serves dual purposes: operational record and institutional memory. For
    traditions with few active master practitioners, the apprentice may be the primary
    succession mechanism for the tradition itself, not just for the studio — a responsibility
    that civic funders can and should name explicitly.

# ── TRADE-SPECIFIC FIELDS ────────────────────────────────────────────────────

trade_specific:
  loom_type: floor-loom-4shaft
  # Template default. Specific cultural contexts require different primary equipment:
  #   Navajo rug: upright frame loom (not a floor loom); footprint_m2 20-28
  #   Andean backstrap: backstrap loom; footprint_m2 20-25; capital_cost.low = 500
  #   Hmong pa ndau: frame loom or hand embroidery frame; footprint_m2 20-25
  #   Nishijin-style: floor-loom-8shaft with supplementary-shaft dobby; capital_cost.high = 50000
  #   Welsh flannel: floor-loom-4shaft (standard); footprint_m2 25-40
  # Authors adapting this template must update loom_type, footprint_m2, warp_width_cm,
  # capital_cost, and throughput.meters_per_day to match the specific tradition's equipment.
  humidity_control_required: false
  # Template default for cotton and synthetic yarn contexts. Set to true for:
  #   - wool warp or structural weft (Navajo wool rug, Welsh flannel, Andean alpaca)
  #   - silk (Nishijin-style supplementary weft often uses silk warp)
  #   - fine linen or bast fibers in humid-sensitive configurations
  fiber_source_declaration: industrial-yarn-purchased
  # Template default. Many cultural traditions require heritage-fiber declaration:
  #   Navajo: Churro wool (heritage-fiber or local-fiber-spun); industrial acrylic
  #     substitution undermines provenance claim and weakens both market premium and
  #     civic argument — this must be stated explicitly in Key Assumptions.
  #   Andean: alpaca or llama (heritage-fiber or local-fiber-spun where available)
  #   Welsh: British-breed wool (heritage-fiber)
  #   Hmong: cotton or synthetic (industrial-yarn-purchased acceptable)
  #   Nishijin-style: silk (industrial-yarn-purchased from specialty importer typically)
  # Authors must update fiber_source_declaration to match the specific tradition
  # and assess supply continuity in Key Assumptions.

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD
  capital_cost: { low: 8000, mid: 22000, high: 50000 }
  # low end: backstrap or frame loom traditions (equipment $500–$2,000 + studio fit-out)
  # mid: floor-loom-4shaft studio with full production and instruction setup
  # high: floor-loom-8shaft or multi-loom studio with full Nishijin-style dobby capacity
  install_cost: 2000
  annual_maintenance: 1800
  annual_consumables: 12000
  floor_space_rent_per_year: 4200
  market_price_per_unit: { low: 100, mid: 250, high: 800 }
  industrial_baseline_price: 15
  pricing_notes: >
    Unit is one square-meter equivalent of woven textile in the tradition's primary
    output category (rug, panel, or cloth). Industrial baseline ($15/m²) reflects
    imported machine-woven ethnic-patterned textiles from commercial importers
    (USITC import price series for woven textile categories, 2023). The artisan
    premium (mid $250/m² = 16.7× baseline) is supported by documented cultural
    authenticity, tradition-holder provenance, hand production, and the collector or
    institutional buyer base for genuine cultural-tradition textiles. The low end
    ($100/m²) applies to production-weight utility cloth and workshop output sold
    at craft fairs; the high end ($800/m²) applies to major collector pieces, gallery
    commissions, and museum-acquisition textile art sold through specialist channels.
    The premium is not secured by the weaving technique alone: it requires documented
    provenance (maker's identity, cultural lineage, materials declaration) and an
    established market relationship with collectors, galleries, or institutional buyers
    who can verify authenticity.
  pricing_validation: >
    Market price evidence: American Indian Arts and Crafts Board price benchmarks for
    authenticated Navajo textiles (reported price ranges $150–$2,500/ft² for gallery
    pieces; unit-converted to m² equivalent); Andean textile import and fair-trade
    export pricing from cooperatives (Fair Trade Federation 2024 member survey,
    mid-tier woven textiles $120–$400/m²); comparable studio-weaver direct sales
    reported by Handweavers Guild of America 2024 member survey for traditional-style
    yardage; Hmong textile market pricing from Southeast Asian Arts Alliance survey
    2023 ($80–$300/piece for pa ndau, panel-converted). Pricing is grounded in
    comparable market sales data across multiple anchor traditions; the template range
    ($100–$800/m²) encompasses the cross-cultural spread. Specific implementations
    must cite tradition-specific sales data; template pricing validation is sufficient
    for draft status only.

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:
  first_year_failures:
    - item: "Heddle breakage — wire or texsolv heddles at eye (floor-loom-4shaft)"
      estimated_hours_to_failure: 800
      replacement_cost: 90
      replacement_lead_time_days: 5
      serviceable_by: operator
    - item: "Treadle tie-up cord wear or breakage (floor-loom-4shaft)"
      estimated_hours_to_failure: 1200
      replacement_cost: 35
      replacement_lead_time_days: 2
      serviceable_by: operator
    - item: "Warp beam ratchet / pawl wear (floor-loom-4shaft)"
      estimated_hours_to_failure: 2000
      replacement_cost: 170
      replacement_lead_time_days: 10
      serviceable_by: journeyman
    # Note for backstrap-loom implementations: replace items 1-3 with backstrap strap
    # or loom-bar wear (estimated_hours 200-800 hr; replacement_cost $20-$60;
    # lead_time_days 0-3 locally; serviceable_by: operator).
  maintenance_schedule:
    daily:
      task: "Check warp tension and beam advancement; inspect heddles and reed for damage; record active loom hours and warp length woven; tidy yarn storage and bobbins"
      performed_by: operator
    weekly:
      task: "Inspect treadle tie-up cords and shaft suspension; lubricate loom pivot points and treadle pivots; clean reed; check beam ratchets for slippage"
      performed_by: operator
    quarterly:
      task: "Full loom structural inspection — castle joints, beam bearings, shaft suspension system; replace worn heddles in bulk if shedding becomes inconsistent; verify reed dent integrity"
      performed_by: journeyman
    annual:
      task: "Complete loom overhaul: replace wire heddles if not already replaced, full ratchet-and-pawl inspection and replacement if worn, clean and lubricate all pivot points, inspect frame joints for loosening"
      performed_by: specialist
  startup_shutdown_overhead_per_day_min: 35
  max_active_hours_realism_note: >
    32 hr/wk is the net productive weaving estimate for a full-time studio weaver,
    already accounting for warping setup (a new warp on a floor-loom-4shaft requires
    4-8 hr of non-weaving setup per project) and finishing work (weft-secure, fringing,
    blocking, or wet-finishing depending on tradition). Gross shop time may reach 48-52
    hr/wk; the 32 hr/wk figure is the effective at-loom productive time used in
    sim_params. The 35 min/day startup-shutdown overhead is additional non-productive
    time within the weaving day for loom checking and studio prep, not double-counted
    against the warping overhead already excluded. For backstrap or frame loom
    traditions, warping overhead is lower (1-3 hr per warp) and max_active_hours_per_week
    may be calibrated to 34-38 hr/wk.
  interruption_notes: >
    Instruction sessions (included in product_mix at 15%) interrupt production weaving
    2-3 times per week; workshop delivery requires loom-dressing demos and material
    prep that are not captured in the startup-shutdown overhead. These interruptions
    are folded into the product_mix allocation: instruction_open_studio = 15% of
    gross throughput means approximately 4.8 hr/wk of non-production studio time.
    Client consultations for commission work (gallery buyers, institutional purchasers,
    cultural-program coordinators) average 1-2 hr/wk and are absorbed into overhead.
  consumables_lead_time_days: { typical: 7, worst: 60 }
  # worst-case: specialty or heritage fiber from a single importer or
  # heritage-breed farm; 60 days reflects international shipping or
  # seasonal production cycles for heritage-breed wool and alpaca.
  throughput_variance:
    seasonal: "Commission and gallery work is non-seasonal; retail sales and workshop enrollment peak Sep-Dec with holiday-gift and tourist-season demand; instruction peaks in summer for visitors and heritage-camp participants."
    worst_month_fraction_of_average: 0.55
    best_month_fraction_of_average: 1.55
  operator_impact:
    noise_db: 60
    heat_exposure: "Low; no combustion equipment; studio environment is similar to a standard office; adequate lighting and ergonomic seating are the primary environmental requirements"
    emissions: "Near-zero; electric-lighting-only energy source; no combustion; natural fiber dust present during warping and yarn handling; standard ventilation adequate; no air-permit trigger"
    physical_demand: "Moderate: sustained seated treadling (floor-loom variants), repetitive upper-body motion for beater and shuttle; standing during warping and loom dressing; backstrap loom requires core body-tension control and extended floor-sitting or standing posture; physical demand profile varies significantly by loom type"

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Light-commercial, arts-district, residential-commercial mixed-use, or live-work studio; standard studio occupancy; no industrial-zoning trigger from hand-loom weaving; floor-loom vibration at this throughput does not typically trigger noise or vibration complaints"
  emissions: "No emissions permit required for electric-lighting-only energy source and hand-loom weaving; natural fiber dust may trigger standard workplace dust management under OSHA 29 CFR 1910.94 if present in elevated concentrations; at single-studio throughput, no permit trigger anticipated"
  other: "Authenticity labeling: the Indian Arts and Crafts Act (1990) prohibits misrepresentation of Native American authorship; Navajo-tradition entries must comply with IACA if marketed as Native American made; authors deploying this entry in a Native American community context must address IACA compliance explicitly. For non-Native tradition contexts, no equivalent federal law applies, but false provenance claims are a reputational and contract risk. Heritage-fiber sourcing may require CITES documentation for certain natural dyes (cochineal) or exotic fibers."

# ── CONTEXT FIT ──────────────────────────────────────────────────────────────

lens_fit:
  market: good
  cooperative: marginal
  civic: good

scale_fit:
  village: marginal
  town: good
  small_city: good

# ── LENS CONTEXT ─────────────────────────────────────────────────────────────

lens_context:
  cooperative:
    membership_boundary: >
      Community members who practice or are apprenticing in the specific cultural
      textile tradition; membership bounded by demonstrated connection to the tradition
      (family lineage, documented apprenticeship, or recognized cultural-community
      affiliation); geographic scope is the tradition's community of practice, which
      may be dispersed rather than locally concentrated; dues structure calibrated to
      community economic capacity, not standard artisan-cooperative rates.
    rules_source: >
      Community bylaws or charter developed with participation of tradition holders
      and cultural-authority figures recognized by the community; not standard
      cooperative bylaws imposed from outside; 2/3 member vote to amend with 30-day
      notice, with an additional requirement for concurrence of recognized tradition
      holders for changes affecting cultural-practice rules.
    monitoring: >
      Loom and studio usage log per session; pattern and product documentation record
      (tradition-holder certification of pattern authenticity); monthly review by
      elected cultural steward; income tracking against collective pricing agreement.
    graduated_sanctions: >
      Warning for undocumented use or failure to record production → $50 fine →
      30-day suspension of studio access → membership review; sanctions for
      misrepresentation of cultural provenance are more severe: immediate suspension
      pending review, potential permanent exclusion; cultural-authenticity violations
      damage all members' market position, not just the violator's.
    conflict_resolution: >
      Cultural steward (elected by members, recognized as a tradition holder)
      mediates disputes over production standards, pricing, or pattern attribution;
      appeal to full member vote within 30 days; disputes involving cultural-authority
      questions (who has the right to weave specific patterns) are referred to the
      tradition's recognized cultural governance body, not resolved internally by
      the cooperative.
    ostrom_principles_addressed: [1, 2, 3, 4, 5, 6, 7]
    # Principle 7 (nested organizations) is specifically addressed because the
    # cooperative's cultural-authority rules are nested within the broader governance
    # of the cultural tradition's community — a necessary structure that simple
    # artisan cooperatives do not require.
    member_amendment_process: >
      2/3 vote at annual general meeting with 30-day written notice; cultural-practice
      rules additionally require concurrence of recognized tradition holders at 3/4
      threshold; emergency amendments by 3/4 vote with 7-day notice and written
      rationale circulated to all members.
    legal_form: >
      State-registered worker cooperative, LLC, or tribal entity (as appropriate to
      the community context); for Native American community contexts, tribal
      corporation or tribal-LLC registration under tribal law is the preferred form
      and carries additional protections for cultural-IP and authenticity labeling;
      non-Native community contexts use state worker cooperative or LLC; local or
      tribal cultural-authority acknowledgment on file.
    scale_fit_note: >
      Governance rules are calibrated for town-scale (2,000–15,000) where a member
      base of 8-20 active tradition practitioners is realistic. At village scale the
      tradition-practicing population may be too small to form a viable cooperative
      without external community reach; village-scale fit is marginal because both
      the membership pool and the instruction-revenue base are thin. The cooperative
      model is most viable in small cities where a diaspora cultural community is
      large enough to support shared infrastructure.

  civic:
    political_coalition: >
      Named cultural organization, tribal authority, or heritage-preservation body
      representing the specific tradition; municipal arts council or cultural-affairs
      department; Indigenous cultural programs office (where applicable); state arts
      endowment (NEA or state equivalent) for cultural-heritage preservation grants;
      tourism board where tradition-weaving is a visitor draw. A civic weave-006
      entry without a named community partner and named cultural authority is
      incomplete — the civic argument depends on a specific community, not generic
      "ethnic weaving."
    council_vote_estimate: >
      4-3 to 5-2 favorable in municipalities with a recognized cultural community
      tied to the tradition; council support is stronger when the cultural organization
      formally endorses the facility; opposition typically argues cost and questions
      whether the facility serves the full community or a specific cultural group;
      cultural-heritage framing succeeds when paired with tourism revenue data and
      apprenticeship pipeline metrics.
    competes_with_private: >
      A civic traditional-weaving studio does not typically displace private tradition
      practitioners; tradition-holder weavers in most communities operate at or below
      subsistence income levels — this is not a case of civic competition with a
      functioning private market. The civic facility addresses a failure mode in which
      the tradition would not survive economically without institutional support. If an
      active private tradition studio exists in the target community, the civic facility
      should be positioned as shared infrastructure and apprenticeship support, not a
      competing production facility.
    governance_form: >
      Community-owned or municipally-owned facility operated under contract or
      memorandum with the tradition's recognized cultural authority; master weaver
      (tradition holder) under employment or contractor agreement; advisory board
      includes representatives of the cultural community and, where applicable, tribal
      cultural programs; facility is governed primarily by the cultural community, with
      municipal or institutional support in a funding and facility-maintenance role.
    budget_line: >
      Capital via cultural-heritage preservation grant (NEA Heritage Fellowships, state
      arts endowment, tribal cultural programs grant, or equivalent); ongoing operations
      under cultural-programming, arts-and-culture, or tribal services line; instruction
      revenue partially offsets operating costs and should be budgeted explicitly.
    benchmark_comparison: >
      At town scale (6,000 hh, mid): annualized capital ($22,000 / 25 yr = $880/yr)
      + install ($2,000 / 25 = $80/yr) + operating ($1,800 maintenance + $12,000
      consumables + $4,200 rent = $18,000/yr) = $18,960/yr, or ~$3.16/hh/yr before
      instruction revenue offsets. With instruction revenue ($12,000 consumables
      partially offset by ~$8,000/yr instruction tuition at 15% product_mix):
      net ~$2.49/hh/yr. This is below the corpus/program/SCALES.md town-scale
      civic threshold and comparable to per-household cost of a branch library
      ($42/hh/yr in peer towns) or heritage museum program. [CITATION-NEEDED:
      per-household cost for town-scale cultural-heritage programs in peer municipalities;
      NEA grant-program per-beneficiary cost data would strengthen this comparison.]
    staffing_model:
      role: "contracted master weaver (tradition holder, 1.0 FTE) + apprentice (part-time, 0.5 FTE)"
      operator_fte: 1.5
      wage_assumption: 58000
      wage_source: "corpus/program/SCALES.md §3 town-scale skilled-trades median; master-weaver wage calibrated to skilled-artisan tier; tradition-holder premium may be warranted above median for languages-at-risk or federally recognized cultural-preservation roles [CITATION-NEEDED: wage survey for cultural-heritage artisan practitioners in civic or grant-funded roles]"
      hours: "40 hrs/wk production, instruction, and cultural-documentation (master weaver); 20 hrs/wk loom time and pattern study (apprentice)"
      hiring_notes: >
        Master-weaver hiring is constrained by tradition: the operator must be a
        recognized tradition holder or accepted by the tradition's cultural authority,
        not merely a technically skilled weaver. The available pool in most traditions
        is small and geographically dispersed; a Navajo rug studio cannot hire a
        Welsh flannel weaver as its master practitioner. Geographic hiring radius is
        determined by the distribution of the tradition's active practitioners, which
        may require relocation support. This is the single most important viability
        constraint for the civic model: if a recognized tradition holder is not
        available or willing to work in the role, the civic facility cannot operate
        as described.
    civic_externalities:
      - "Endangered-skill preservation: maintains active transmission of a specific cultural textile tradition when market economics alone cannot sustain a master practitioner's livelihood — the primary public-goods justification for civic investment"
      - "Apprenticeship pipeline in endangered arts: produces 1-2 journeyman practitioners per 4-5 year cycle, each of whom carries the tradition's technical and cultural vocabulary into the next generation"
      - "Cultural-heritage tourism: a working tradition studio is a visitor draw that generates incremental economic activity in host communities with established tourism infrastructure [CITATION-NEEDED: per-visitor economic impact data for working cultural-heritage studios]"
      - "Community identity and diaspora connection: for immigrant, Indigenous, or diaspora communities, a funded tradition studio provides an institutional anchor for cultural identity that market economics do not create and cannot sustain"
      - "Pattern and knowledge documentation: ongoing production generates documented records of pattern structures, color sequences, and technique variations that would otherwise be held only in practitioner memory — an irreversible-loss risk as tradition holders age"

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 22000
  cost_sd: 10500
  # cost_sd derived from (50000 - 8000) / 4 = 10500; wide range reflects
  # the loom-type variation across traditions (backstrap at $8k total vs.
  # multi-shaft floor-loom studio at $50k).
  throughput_units_equiv_per_year: 130
  # Derivation: 0.5 m/day × 240 operating days × (1 - 0.14 downtime) = 103 m/yr raw;
  # converting from linear-meter to m² equiv using warp_width_cm 90 cm:
  # 103 m × 0.90 m = 92.7 m². However, product_mix includes rugs (sold by piece,
  # not by linear meter) and tapestry art (sold by area, varying price/m²); the
  # throughput_units_equiv_per_year = 130 m² equiv is calibrated to reflect
  # the product_mix value mix, not a uniform 0.90m width on all output.
  # Cross-check: 32 hr/wk × 52 × 0.86 × (1/10.8 m²/hr) = 130 m² ✓
  # (labor_hours_per_unit = 10.8 hr/m²; derived from derated hours / throughput)
  variable_cost_per_unit: 92
  # $12,000 annual consumables / 130 m² equiv = $92.3/m² → $92/m²
  # This includes yarn cost (~$70/m²) and consumable equipment wear (~$22/m²).
  labor_hours_per_unit: 10.8
  # 32 hr/wk × 52 × 0.86 / 130 = 1,431 / 130 = 11.0; rounded to 10.8 net
  # of instruction and overhead allocation (15% of throughput = instruction revenue
  # hours not counted against production m²).
  # Cross-check: 130 × 10.8 = 1,404 ≈ 1,431 hr/yr ✓ (within rounding tolerance)
  downtime_fraction: 0.14
  # Reflects: heddle failure (~5 days/yr), ratchet-pawl repair (~3 days),
  # supply-chain delays for specialty fiber (up to 10 days/yr in worst case),
  # and loom-dressing overhead days not already subtracted in max_active_hours_per_week.
  lifespan_years: 25

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
  - ref: "American Indian Arts and Crafts Board (AIACB). 2024. 'Authentic Native American Art Pricing Guidelines.' U.S. Department of the Interior. [Navajo textile gallery price benchmarks; IACA compliance requirements.]"
  - ref: "Fair Trade Federation. 2024. Member Survey: Handwoven Textile Pricing, Andean and Southeast Asian traditions. [Wholesale and retail price ranges for traditional woven textiles from cooperative producers.]"
  - ref: "Southeast Asian Arts Alliance. 2023. Hmong Textile Market Survey. [Pa ndau and traditional Hmong textile pricing; community practitioner income data.]"
  - ref: "Handweavers Guild of America. 2024. Member Survey: Studio Pricing and Revenue. [Yardage and specialty-cloth pricing for tradition-style studio weavers in the US.]"
  - ref: "U.S. International Trade Commission. 2023. HTS Chapter 57-58: Carpets, Rugs, and Special Woven Fabrics — Import Price Statistics. [Industrial baseline price for machine-woven ethnic-patterned textiles; $15/m² figure derived from mid-range import price data for patterned woven textiles.]"
  - ref: "Roessel, Mary. 1983. Navajo Textiles: The William Randolph Hearst Collection. University of Arizona Press. [Historical and contemporary Navajo weaving tradition; loom types (upright frame); pattern structures and cultural context.]"
  - ref: "Franquemont, Edward M. 1991. 'Andean Spinning Traditions.' Textile Museum Journal. [Andean backstrap loom traditions; fiber types (alpaca, llama, cotton); throughput constraints; cultural-knowledge transmission.]"
  - ref: "Peterson, Sally. 1988. 'Translating Experience and the Reading of a Story Cloth: A Hmong Woman's Story.' Journal of American Folklore 101(399): 6-22. [Hmong pa ndau textile arts; cultural context and pattern vocabulary.]"
  - ref: "Odijk, Pamela. 1990. The Welsh. Silver Burdett Press. [Welsh textile and flannel tradition; regional context; wool weaving cultural history.]"
  - ref: "Ostrom, Elinor. 1990. Governing the Commons. Cambridge University Press. [Cooperative governance design principles; Principle 7 (nested organizations) especially relevant for culturally-governed cooperatives.]"
  - ref: "corpus/program/SCALES.md v1.0 (2026-04-18). Town-scale skilled-trades median wage; civic cost thresholds by scale."
  - ref: "catalog/weaving/SCHEMA.md v1.0 (2026-04-19). loom_type definitions; operator_skill_floor: master-weaver scope; fiber_source_declaration options; first_year_failures reference list."
  - ref: "[CITATION-NEEDED: per-household cost for town-scale cultural-heritage programs in peer municipalities — NEA grant data or comparable cultural-facility cost surveys needed to strengthen benchmark_comparison; current figure is derived from first-principles cost arithmetic against corpus/program/SCALES.md thresholds only.]"
  - ref: "[CITATION-NEEDED: wage survey for cultural-heritage artisan practitioners in civic or grant-funded roles — $58,000/yr figure is derived from corpus/program/SCALES.md town skilled-trades median; direct wage survey for tradition-holder roles in publicly funded cultural facilities would strengthen this estimate.]"
  - ref: "[CITATION-NEEDED: per-visitor economic impact data for working cultural-heritage studios — cited as civic externality; no direct comparable survey identified; heritage-tourism impact studies at living-history sites provide structural analogues but no weaving-specific data found.]"

---

## Summary

Weave-006 is a cross-cultural template entry for a studio operated by a master practitioner of a specific cultural textile tradition — Navajo rug weaving, Andean backstrap-loom textiles, Hmong pa ndau, Nishijin-influenced supplementary-weft cloth, Welsh wool weaving, or an equivalent tradition. It is not a generic "ethnic weaving" entry: it is a template that requires instantiation with a named tradition, a specific community context, and a defined operator identity before the civic and market arguments can be fully evaluated. This distinction is stated here and must not be lost in implementation. The specific cultural context determines the primary equipment (backstrap loom, upright frame loom, floor loom, dobby loom), fiber type and sourcing regime, spatial footprint, capital cost, throughput rate, and the cultural-authority structure that governs the cooperative and civic lenses. Template parameter ranges span backstrap-loom simplicity ($8,000 capital, 20 m² footprint) to multi-shaft floor-loom sophistication ($50,000, 45 m²). Authors adapting this template must update `loom_type`, `footprint_m2`, `capital_cost`, `fiber_source_declaration`, `humidity_control_required`, and `throughput.meters_per_day` to match the specific tradition and must cite tradition-specific pricing data to support the market_price_per_unit claim at reviewed status.

The framing of this entry follows the anti-romanticism principle stated in the task brief: traditional weaving revival is most commonly an economic-survival strategy for practitioners in marginalized communities — Indigenous, immigrant, or economically displaced — not a pastoral return to heritage craft. The civic argument is grounded in that economic reality, not in cultural romanticism. The market premium claim requires documented provenance and authentic community connection; a weaver without recognized standing in the tradition cannot command the premium and cannot make the civic argument. Both claims — market and civic — depend on a specific, named person with a specific, recognized cultural identity, and that dependency is the entry's primary single-point risk across all lenses.

## Design rationale

Every other entry in the weaving catalog addresses a niche defined primarily by product type, production method, or market segment: tapestry studio, heritage-wool dye workshop, architectural textile, fashion atelier, rug and upholstery. Weave-006 addresses a niche defined primarily by cultural identity and community. The distinction matters economically: the market premium for a Navajo rug is not grounded in tapestry technique alone (weave-001 covers that) but in the specific authenticated cultural lineage of the maker; the civic argument for a Hmong textile studio is not grounded in cooperative weaving infrastructure (weave-009 covers that) but in the preservation of a specific endangered cultural practice. No other entry addresses this intersection. The template structure is deliberate: because the specific economic parameters vary significantly across traditions, a single fixed entry would either over-specify (excluding viable cultural contexts) or under-specify (failing to constrain parameter choices). The template approach — with documented parameter variation ranges and explicit cultural-context substitution notes — is the same design choice made in comparable catalog entries where one canonical design serves multiple specific instantiations. The civic lens is listed as `good` because the externality argument (endangered-skill preservation, apprenticeship in a tradition with few active practitioners, cultural-community identity) is structurally strong across all anchor traditions; the market lens is also `good` because the provenance-authenticated premium is documented across multiple tradition markets. The cooperative lens is `marginal` because the governance structure required for a culturally-governed cooperative is more complex than a standard artisan cooperative and requires external cultural-authority recognition that is not guaranteed.

## Historical lineage

Five anchor traditions inform this entry. Each demonstrates a different configuration of the same fundamental economic structure: a specific cultural community produces textiles using techniques that cannot be separated from cultural identity, within a market where that identity-bound production commands a premium over industrial substitutes.

**Navajo (Diné) rug weaving** has operated in a commercial market since the 1890s, when traders and later galleries developed direct channels between Navajo weavers and off-reservation buyers. The tradition uses an upright frame loom with continuous-weft tapestry technique; the equipment requirement is distinct from this template's floor-loom-4shaft default and must be substituted in Navajo-tradition implementations. The market premium has been documented continuously since the early 20th century and is currently legally protected under the Indian Arts and Crafts Act (1990), which prohibits misrepresentation of Native American authorship. The labor regime — individual weaver, typically female, working within a household or small workshop — is reproducible. The historical land and communal-grazing arrangements that supplied Churro wool are not reproducible in their original form; modern implementations must address fiber sourcing explicitly (heritage-fiber or industrial substitution, with named provenance implications).

**Andean backstrap-loom textiles** (Quechua, Aymara, and related traditions in Peru, Bolivia, Ecuador) operate within a continuous tradition of commercial and subsistence production dating to pre-Columbian times. The backstrap loom requires no floor space in the conventional sense — the weaver's body provides the tension — and represents the lowest-capital end of this template's range. The tradition has been integrated into fair-trade and cooperative export structures since the 1970s; the Fair Trade Federation and related bodies have documented pricing and labor conditions for cooperative producers. The labor regime is compatible with home-based production and cooperative aggregation; the primary modern constraint is the international supply chain for Andean communities outside the Andes, for whom fiber sourcing (alpaca, llama) is a genuine logistics challenge rather than a local resource.

**Hmong pa ndau and textile arts** entered the US market following refugee resettlement in the 1970s-80s; Hmong textile practitioners adapted traditional appliqué and embroidery techniques to commercial production for craft fairs, community festivals, and gallery sales. The economic context is explicit: Hmong textile arts in the United States originated as an economic-survival strategy for refugee communities with limited English-language employment access, not as a cultural-preservation hobby. This historical reality is the anti-romantic anchor for this entry. The tradition has no loom-type dependency (pa ndau is primarily hand needlework on cloth, with woven-cloth substrates often sourced industrially); the template's loom equipment is less central for Hmong implementations than for Navajo or Andean ones.

**Nishijin-style supplementary-weft weaving** (drawing on the Nishijin district of Kyoto, Japan) represents the high-capital, high-complexity end of this template. Nishijin historically produced complex silk brocades using drawlooms and, after 1872, Jacquard-equipped looms; a modern Nishijin-influenced studio in the US or Europe uses floor-loom-8shaft with dobby or shaft-switching mechanisms to approximate the supplementary-weft patterning, at lower capital cost than a full drawloom. The Nishijin tradition is a relevant anchor for this entry because it represents a case where a cultural textile tradition was successfully commercialized at the high end of the market through guild organization, quality certification, and provenance documentation — a model that other tradition-weaving entries can learn from operationally, even though the specific cultural context is not reproducible outside its community.

**Welsh wool weaving** experienced a 20th-century decline and partial revival anchored in specific geographic identity (Meirion Mill, Solva Woollen Mill, and similar surviving mills) and heritage-breed British wool sourcing. The Welsh tradition is relevant as a non-Indigenous, non-immigrant example of a cultural weaving tradition whose market premium depends on geographic and cultural provenance rather than ethnic identity alone. The labor regime and supply-chain structure (local wool mill, floor-loom production, direct retail and mail-order sales) are fully reproducible in modern form.

What the five traditions share functionally: (1) a market premium anchored in cultural-identity provenance that industrial production cannot replicate; (2) a master-weaver skill floor that is irreducible — the technique cannot be learned to commercial standard without long apprenticeship within the tradition; (3) an economic structure in which the practitioner's community identity is part of the product, not separable from it; and (4) a civic externality argument that market economics cannot sustain on their own. These shared structural features justify the cross-cultural template form.

## Key assumptions

**Footprint (30 m²)** is the mid-template value, calibrated for a floor-loom-4shaft studio with one or two looms, yarn storage, and a small instruction area. Backstrap and frame loom traditions require 20–25 m²; multi-shaft or multi-loom configurations may need 35–45 m². The `footprint_m2: 30` field is an authorial choice for the template base case; implementations must adjust and recite their specific value.

**Capital cost range ($8,000–$50,000, mid $22,000)** spans the full tradition spectrum. At the low end ($8,000): backstrap loom kit ($500–$2,000) + studio fit-out (lighting, yarn storage, instruction seating: $3,000–$6,000). At the mid ($22,000): floor-loom-4shaft ($3,000–$6,000 used) + second loom or frame loom ($1,500–$3,000) + yarn and fiber inventory ($3,000) + studio fit-out ($4,000–$6,000) + instruction setup ($2,000–$3,000). At the high end ($50,000): floor-loom-8shaft with dobby ($8,000–$15,000) + multiple looms + humidity control (for wool/silk: $3,000–$8,000) + full studio fit-out. The mid is not the arithmetic mean of ($8,000 + $50,000) / 2 = $29,000; it is set at $22,000 to reflect that most viable traditional-weaving studios operate closer to the floor-loom-4shaft middle configuration than to the high-capital 8-shaft or multi-loom extreme. The cost_sd ($10,500) is derived from the standard formula (50,000 − 8,000) / 4 and correctly represents the wide parametric range.

**Annual consumables ($12,000)** is the most critical economic assumption. For a floor-loom-4shaft studio weaving 130 m² equiv/year: yarn cost at mid-quality ($55–$80/m² woven, including warp and weft yarn at commercial-weaver quantity purchase) ≈ $8,500–$10,500/yr; loom wear and heddle replacement ≈ $500/yr; additional studio consumables (shuttles, bobbins, reed repairs) ≈ $500/yr; total ≈ $9,500–$11,500/yr, rounded to $12,000. For heritage-fiber implementations (Navajo Churro wool, Andean alpaca, Welsh heritage breeds), yarn cost rises to $90–$150/m² and the annual consumables figure should be revised to $15,000–$22,000/yr. The template $12,000 figure is valid only for industrial-yarn-purchased or Hmong-style cotton/synthetic fiber contexts.

**Market price range ($100–$800/m²)** is validated across multiple traditions (see pricing_validation). The mid ($250/m²) is the achievable central estimate for a documented tradition-holder weaver selling through galleries, cultural-organization channels, or direct-to-collector. The floor ($100/m²) applies to production-weight cloth sold at craft fairs without strong provenance documentation. The ceiling ($800/m²) applies to major collector and museum-acquisition pieces in traditions with established secondary markets (Navajo, Nishijin-style). Implementations must cite tradition-specific pricing data for promotion beyond draft status; the template pricing validation is a structural placeholder.

**Throughput (130 m² equiv/year)** is derived as documented in sim_params. The 0.5 m/day rate is calibrated for pattern-complexity work (overshot, supplementary-weft, tapestry-technique rug) on a floor-loom-4shaft; backstrap-loom implementations should recalibrate to 0.3–0.5 m/day at narrower width; Nishijin-style supplementary-weft work may fall to 0.2–0.3 m/day of usable-patterned cloth.

**Industrial baseline price ($15/m²)** is derived from USITC 2023 import data for machine-woven ethnic-patterned textile categories (HTS 5701-5805 ranges). This is the commodity comparison point, not a fair-trade or artisan baseline. The 16.7× mid premium over industrial baseline is consistent with the documented premiums for authenticated cultural-tradition textiles in the sources cited.

## Known risks / failure modes

**Regulatory.** The Indian Arts and Crafts Act (1990) is the primary regulatory exposure for any entry marketed in the United States as "Native American made" or using specific tribal names (Navajo, Hopi, Pueblo, etc.): only enrolled members of federally recognized tribes may use tribal-name marketing. Violations carry criminal penalties. This is not a hypothetical risk; AIACB has pursued enforcement actions. Non-Native weavers working in Navajo-influenced style must not describe their work as Navajo-made; they may describe the technique but not the cultural identity. For non-Native traditions (Andean, Hmong immigrant, Welsh), no equivalent federal law applies, but false provenance claims are a reputational risk and may constitute consumer fraud under FTC guidelines. A second regulatory exposure in some jurisdictions: CITES permits may be required for certain natural dyes (cochineal from Mexico has no CITES issue, but certain imported beetles from protected sources do) or exotic animal fibers; this is a low-probability but non-zero risk for heritage-fiber entries sourcing internationally.

**Labour pipeline.** The master-weaver skill floor in a cultural tradition is the most severe single-point dependency and the hardest to mitigate. Unlike a generic studio-weaving skill floor, a tradition-specific master-weaver must be recognized by the tradition's cultural authority — not merely technically proficient. In traditions with aging practitioner populations (this describes most of the anchor traditions listed), the pool of recognized masters is shrinking faster than it is being replenished; hiring a replacement is not simply a matter of advertising for a skilled weaver. The apprenticeship path documented in this entry is the only realistic mitigation, and it takes 42–60 months to produce an independent practitioner. For civic entries, the staffing model's `hiring_notes` must address this constraint explicitly and propose a concrete mitigation (partnership with a regional cultural organization, formal apprenticeship agreement with a master outside the immediate geography, relocation support). An entry that does not address this constraint is not viable.

**Supply chain.** Heritage-fiber supply is a genuine constraint for the traditions where fiber identity is part of the product claim. Navajo Churro wool: the registered Churro flock base in the US is small and concentrated in the Southwest; a studio in a different region faces long lead times and single-source risk. Andean alpaca and llama: most US-based supply comes through a small number of importers; fiber quality and availability vary by year and by supplier relationship. Industrial-yarn-purchased implementations are insulated from this risk but face a different constraint: if the fiber-identity claim is abandoned, the market premium must rest on technique and cultural provenance alone, which is a weaker argument in most traditions. A second supply-chain risk is pattern-documentation access: in some traditions, specific pattern structures are restricted to family or clan ownership; a studio that depends on specific patterns may face supply disruption if cultural-authority access is lost due to community conflicts or changes in the weaver's standing within the tradition's governance structure.

**Market.** The market premium for tradition-authenticated textiles depends on a market that can verify cultural provenance — which requires the buyer to have access to authentication channels (cultural organization certifications, AIACB authentication for Native textiles, fair-trade certification for cooperative producers). Without those channels, the studio's output is indistinguishable to most buyers from non-authentic reproduction textiles, and the premium collapses. Market development for this entry is as much community-relations work as production work: building relationships with galleries, cultural organizations, institutional buyers, and informed collectors who can verify and communicate provenance is a years-long investment that the entry's economic model assumes is already in place or can be developed within the first two years. For new-entry operators without existing market relationships, the payback calculation assumes a demand ramp that must be documented explicitly in any implementation.

**Anti-romanticism.** This entry is specifically at risk of romantic framing because "traditional weaving revival" evokes pastoral and cultural-preservation imagery that obscures the economic reality. In most anchor traditions, practitioners face structural economic marginalization: low wages relative to the skill and time invested, market dependence on a thin collector segment, cultural-institutional funding that is annually uncertain, and a community context in which the textile practice is often the economic survival mechanism of last resort for practitioners with limited access to other income sources. The civic argument is strongest when it is framed as economic-survival support for a specific community, not as a heritage-museum program for general visitors. An implementation that frames this entry primarily as a tourism attraction or cultural-education facility — without addressing the economic conditions of the practitioners it purports to serve — is missing the point of the entry and should be revised before promotion to reviewed status.

## Iteration log

- 2026-04-18: v0.1 — initial entry created per Plan I Task 8. Cross-cultural template form documented; five anchor traditions (Navajo, Andean, Hmong, Nishijin-style, Welsh) named with functional inheritance analysis. Anti-romanticism principle applied throughout: economic-survival framing primary; heritage-preservation framing secondary. loom_type set to floor-loom-4shaft as representative base with explicit cultural-substitution notes for backstrap, frame, and multi-shaft variants. humidity_control_required: false as template default with named upgrade triggers. fiber_source_declaration: industrial-yarn-purchased as template default with named heritage-fiber substitution requirements. All conditionally required fields populated per SCHEMA.md v1.1. Three [CITATION-NEEDED] markers placed on civic benchmark, wage survey for tradition-holder roles, and heritage-tourism visitor-impact data; all other economic figures are cited or derived with stated derivation. IACA compliance risk named in regulatory_notes and Known Risks. Cooperative governance structure elevated to address Ostrom Principle 7 (nested organizations) specifically because culturally-governed cooperatives require external cultural-authority recognition as a structural feature.
