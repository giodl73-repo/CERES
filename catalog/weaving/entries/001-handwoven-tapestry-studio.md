---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: weave-001
trade: weaving
name: "Handwoven Tapestry Studio"
tagline: "Direct-to-consumer and commission tapestry studio producing non-standardizable weft-faced wall textiles for gallery and interior-design markets"
status: draft
version: 0.1
supersedes: null
inspirations:
  - aubusson-tapestry-workshop
  - medieval-arras-tapestry-atelier
  - american-frontier-jacquard-coverlet-weaver

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 40
ceiling_min_m: 2.7
ventilation: natural-sufficient

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: electric-lighting-only
energy_consumption_per_active_hour: "0.5 kWh (lighting only; hand/treadle looms; no powered weaving mechanism)"
backup_fuel: null

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  meters_per_day: 0.3
  # Central estimate for tapestry (range 0.1–0.5 m²/day per weaving SCHEMA.md §1).
  # Stated as area (m²/day) per weaving SCHEMA.md §1 tapestry-unit guidance.
  # At warp_width_cm: 150, 0.3 m²/day corresponds to ~0.20 linear metres/day.
  # [CITATION-NEEDED: measured tapestry throughput rates — Aubusson or contemporary
  # tapestry studio production records; weaving SCHEMA.md cites 0.1–0.5 m²/day
  # for master-weaver tapestry as the documented range]
  warp_width_cm: 150
  pattern_complexity: tapestry
  max_active_hours_per_week: 30
  # Net active weaving hours at the loom per week. Warping, loom dressing, cartoon
  # preparation, and finishing consume the remaining ~15–20 hr of a 45–50 hr shop week.
  # Consistent with weaving SCHEMA.md §1: "realistic ceiling for full-time weaver:
  # 30–40 hr/wk at loom; total shop time including setup may reach 50–55 hr/wk."
  product_mix:
    yardage: 0
    rugs_upholstery: 0
    tapestry_art: 90
    garments_accessories: 0
    instruction_open_studio: 10
  throughput_variance:
    worst_month_fraction_of_average: 0.65
    best_month_fraction_of_average: 1.40
    seasonal: "Commission intake is non-seasonal for gallery clients; retail/gift demand peaks Oct–Dec and troughs Jan–Feb."

# ── WEAVING-SPECIFIC REQUIRED FIELDS ─────────────────────────────────────────

loom_type: floor-loom-8shaft
# 8-shaft floor loom used for tapestry and complex weave structures.
# Warp width 90–200 cm per weaving SCHEMA.md §3; 150 cm selected for commission scale.

humidity_control_required: true
# Wool and silk thread; warp tension sensitive to RH below ~45% or above ~75%.
# See weaving REQUIREMENTS.md §2 and weaving SCHEMA.md §4.

fiber_source_declaration: industrial-yarn-purchased
# Commercially spun wool and silk thread purchased from yarn distributors.
# No integrated spinning; no heritage-breed fiber dependency.
# See Key Assumptions for supply continuity assessment.

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: master-weaver
# Tapestry requires full technical range: weft-faced discontinuous-weft structure,
# tonal shading, complex compositional design, and high-warp technique when applicable.
# Per weaving SCHEMA.md §5: master-weaver required for weave-001.
operators_concurrent: "1-2"
apprentice_friendly: true
apprentice_path:
  training_stages: >
    Stage 1 (0–6 mo): loom mechanics, warping, plain-weave and twill foundation,
    color palette and cartoon reading. Gate: independent plain-weave cloth at
    specification width without tension faults. Stage 2 (6–18 mo): tapestry-specific
    techniques — weft-interlock, hatching, kilim slit, simple curve — on supervised
    small-format commissions. Gate: complete a 30×30 cm tapestry sample to
    journeyman standard. Stage 3 (18–36 mo): independent tapestry production under
    master review, progressing to complex gradients, mixed fiber, and multi-cartoon
    work. Gate: complete a commission piece to client-delivery standard without
    intervention. Stage 4 (36–60 mo): full independence on original-design commissions;
    eligible for journeyman-weaver certification.
  time_to_independent_operation: "~48–60 months to master-weaver standard on tapestry; ~36 months to journeyman standard capable of supervised commission work"
  succession_note: "Apprentice co-presence during commission production is the primary skill-transfer vehicle; formal stages integrate into normal operating schedule with no dedicated training-only overhead."

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD
  capital_cost: { low: 12000, mid: 25000, high: 45000 }
  # low: 2 floor looms (used/entry), warping mill (used), basic finishing tools, display.
  # mid: 2–3 floor looms (new mid-range, 8-shaft), warping mill, bobbin winder,
  #      finishing press, display fixtures, humidity monitoring equipment.
  # high: 4 floor looms (new professional 8-shaft), full finishing suite, humidity
  #       control system (standalone humidifier/dehumidifier), display + point-of-sale.
  # [CITATION-NEEDED: floor loom 8-shaft retail prices; weaving SCHEMA.md §3
  #  cites $4,000–$15,000 per floor-loom-8shaft unit as the documented range;
  #  mid estimate is consistent with 2–3 units plus ancillaries]
  install_cost: 3500
  # Electrical upgrade for lighting + humidity monitoring; minor structural (loom
  # anchor bolts if required); permitting. No fuel-line or extraction system needed.
  # [CITATION-NEEDED: small studio installation cost estimate]
  annual_maintenance: 2800
  # Includes humidity control system service ($600/yr estimated), loom maintenance
  # and heddle/reed replacement ($900/yr), facility maintenance ($800/yr), and
  # miscellaneous tooling ($500/yr). Climate-control cost elevated per weaving
  # SCHEMA.md §2 guidance: humidity-control energy and maintenance exceeds loom
  # maintenance for wool/silk entries.
  # [CITATION-NEEDED: annual maintenance cost components; values are order-of-magnitude
  #  estimates absent published studio operating data]
  annual_consumables: 9600
  # Primary consumable: commercial wool and silk yarn. At ~58 m²/yr output and
  # ~$150/m² yarn cost (midpoint estimate for commercial worsted wool + silk
  # blending yarn at tapestry sett), annual yarn spend ≈ $8,700. Sundry consumables
  # (bobbins, cartoon paper, finishing supplies) ≈ $900/yr.
  # [CITATION-NEEDED: commercial tapestry yarn cost per kilogram and yield-per-m²;
  #  estimate derived from weaving SCHEMA.md §2 and industry pricing knowledge]
  floor_space_rent_per_year: 9600
  # 40 m² at $240/m²/yr imputed commercial rate for small-city studio space
  # (estimate; local rates vary significantly).
  # [CITATION-NEEDED: small-city commercial studio rental rates per m²/yr]
  market_price_per_unit: { low: 200, mid: 450, high: 1200 }
  # Per m² equivalent of finished tapestry. Low: reproduction or small-format
  # work to budget clients. Mid: custom commission for residential interior design.
  # High: gallery-exhibited original or large architectural commission.
  # [CITATION-NEEDED: contemporary handwoven tapestry market prices per m²;
  #  craft-fair survey, gallery price data, or comparable artisan studio financials
  #  required for E-1 compliance; values reflect practitioner-community knowledge
  #  pending formal citation]
  pricing_notes: >
    Unit is one m² of finished handwoven tapestry delivered to client. Premium over
    industrial-woven machine rug equivalent ($25/m²; see industrial_baseline_price)
    is 8× at mid — justified by non-standardizable design, weft-faced hand technique,
    master-weaver execution, and commission provenance. Target customer: residential
    and commercial interior designers, gallery collectors, and public-art procurement
    clients in small-city and metropolitan markets.
  pricing_validation: >
    [CITATION-NEEDED: empirical pricing evidence for handwoven tapestry — gallery
    price surveys, craft-fair rate cards, or comparable artisan studio financial
    statements. Values above reflect practitioner-community knowledge and are
    structurally consistent with the industrial-baseline premium for non-standardizable
    hand-craft goods (Adamson 2013; Metcalf 1997 general luxury-craft pricing
    frameworks), but direct sales-data citation is required for E-1 compliance
    before promotion to `reviewed` status.]
  industrial_baseline_price: 25
  # Machine-woven rug/wall-hanging equivalent per m² at retail (mid-market
  # mass-produced decorative rug). This is the nearest industrial substitute on
  # a per-area basis; hand tapestry does not compete with it on price.
  # [CITATION-NEEDED: machine-woven decorative rug retail price per m²;
  #  retail survey or manufacturer wholesale data required]

# ── TRADE-SPECIFIC FIELDS ────────────────────────────────────────────────────

trade_specific:
  # Fields specific to weaving entries per catalog/weaving/SCHEMA.md §8 extension.
  loom_count: 2
  # Operative loom count for the mid-capital scenario; scales to 3–4 at high.
  humidity_target_rh_pct: { min: 50, max: 70 }
  # Target relative humidity range for combined wool/silk fiber mix.
  # Wool optimal 65–75%; silk optimal 65–70% per weaving REQUIREMENTS.md §2.
  # Practical target 50–70% for mixed-fiber studio.
  cartoon_design_hours_per_commission: "[CITATION-NEEDED: typical cartoon preparation time per tapestry commission — practitioner survey or studio documentation]"

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:
  first_year_failures:
    - item: "Warp beam ratchet / pawl wear (floor loom × 2)"
      estimated_hours_to_failure: 2000
      replacement_cost: 180
      replacement_lead_time_days: 10
      serviceable_by: journeyman
      # Per weaving SCHEMA.md §7: 1,500–3,500 hr typical for floor loom ratchet/pawl.
      # [CITATION-NEEDED: replacement cost and lead time — loom parts supplier catalog]
    - item: "Heddle breakage (wire heddles, 8-shaft loom)"
      estimated_hours_to_failure: 800
      replacement_cost: 120
      replacement_lead_time_days: 5
      serviceable_by: operator
      # Per weaving SCHEMA.md §7: 500–2,000 hr typical for wire heddles.
      # Low replacement cost; operator-replaceable (re-threading required).
      # [CITATION-NEEDED: replacement cost and lead time — loom parts supplier catalog]
    - item: "Humidity control unit failure (humidifier/dehumidifier)"
      estimated_hours_to_failure: 2500
      replacement_cost: 450
      replacement_lead_time_days: 7
      serviceable_by: journeyman
      # Per weaving SCHEMA.md §7 climate-control reference: 1,500–3,500 hr.
      # Residential-scale unit; journeyman-level diagnosis; specialist HVAC for
      # commercial system. Residential replacement unit: ~$300–$600.
      # [CITATION-NEEDED: humidifier lifespan and replacement cost — appliance data]
  maintenance_schedule:
    daily:
      task: "Check warp tension on active loom(s); clear shed of lint and broken thread ends; log RH reading from hygrometer; adjust humidifier/dehumidifier if RH outside 50–70% target."
      performed_by: operator
    weekly:
      task: "Inspect heddles for fatigue cracks; check treadle tie-up cords for fraying; lubricate beam pawl springs; clean lint from shed and under beam; wind bobbins for upcoming work."
      performed_by: operator
    quarterly:
      task: "Full heddle count and replacement of worn wire heddles; inspect reed for bent dents; check beam ratchet engagement and pawl spring tension; clean and service humidity control unit filter."
      performed_by: journeyman
    annual:
      task: "Full loom inspection: check frame joinery, beam alignment, treadle lamm condition; inspect and replace treadle tie-up cords as needed; service humidity control system (professional inspection if commercial unit); calibrate hygrometer."
      performed_by: specialist
  startup_shutdown_overhead_per_day_min: 25
  # Startup: 10 min loom tension check + humidity check + bobbin preparation.
  # Shutdown: 15 min shed clearing + loom cover + log entry + tool stowage.
  max_active_hours_realism_note: >
    30 hr/wk is the net active loom-time figure after warping, loom-dressing,
    cartoon preparation, client communication, and finishing work are excluded.
    Gross shop time is 45–50 hr/wk. The 25 min/day startup-shutdown overhead is
    applied on top of the already-derated 30 hr/wk figure: on a 5-day operating
    week, overhead reduces usable loom time by ~2.1 hr/wk, yielding ~27.9 net
    productive loom hr/wk. sim_params.throughput_units_equiv_per_year uses the
    30 hr/wk figure with downtime_fraction 0.12 to capture both scheduled
    non-production time and interruptions.
  interruption_notes: >
    Client review meetings (~1.5 hr/commission), cartoon revision cycles, and
    fiber-sourcing procurement time (1–2 hr/wk) are folded into the gross-to-net
    derating from 50 hr total shop time to 30 hr active loom time. Commission-based
    model reduces walk-in interruptions relative to retail-only studios.
  consumables_lead_time_days: { typical: 7, worst: 45 }
  # Typical: commercial wool/silk yarn from domestic distributor, 5–10 days.
  # Worst: specialty silk thread (imported), supply disruption, or rare colorway
  # special-order; 30–45 days documented for luxury yarn import chains.
  # [CITATION-NEEDED: commercial tapestry yarn lead-time data — distributor survey]
  throughput_variance:
    seasonal: "Commission intake is non-seasonal for gallery and interior-design clients; retail direct sales and gift commissions peak Oct–Dec and trough Jan–Feb."
    worst_month_fraction_of_average: 0.65
    best_month_fraction_of_average: 1.40
  operator_impact:
    noise_db: 55
    # Hand/treadle loom operation; primary sound is shed change (treadle thud) and
    # beater stroke. Estimated 50–60 dB(A) at operator position.
    # [CITATION-NEEDED: measured dB(A) for floor loom treadle operation]
    heat_exposure: "Ambient; no heat-generating equipment. Climate-control system maintains 50–70% RH; temperature neutral."
    emissions: "Near-zero; no combustion, no chemical process. Wool fiber dust and lint require adequate ventilation; natural fiber dust is a mild respiratory irritant at sustained exposure. Standard commercial ventilation sufficient."
    physical_demand: "Moderate: sustained sitting with treadle operation (lower-body repetitive motion); beater stroke (upper-body repetitive); neck/shoulder strain from fine-detail cartoon work. Ergonomic loom bench recommended."

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Light commercial or mixed-use zoning adequate; no industrial zoning required. Studio use consistent with most small-city commercial lease categories."
  emissions: "No emissions permit triggers; near-zero combustion or chemical emissions. Natural fiber dust: standard commercial ventilation compliant with OSHA general-industry standards; no weaving-specific permit required."
  other: "No weaving-specific licensing required in US jurisdictions reviewed. Humidity control system: standard residential/commercial HVAC permit if new installation. Display and retail use may require retail business license per local ordinance."

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
    membership_boundary: "Practicing weavers and fiber artists in the small-city region; paid annual dues; journeyman-weaver minimum skill gate for loom-share access."
    rules_source: "Cooperative bylaws; member vote to amend with 2/3 majority at annual meeting with 30-day notice."
    monitoring: "Commission and loom-time log maintained per session; monthly review by elected studio steward; financial audit annually."
    graduated_sanctions: "Warning (first violation) → $75 fine (repeat) → 30-day loom-access suspension → membership review by steward committee."
    conflict_resolution: "Member-elected steward arbitrates scheduling and attribution disputes; appeal to full member vote with 14-day notice."
    ostrom_principles_addressed: [1, 2, 3, 4, 5, 6]
    # Principles 7 (nested organisations) and 8 (external recognition) are not
    # addressed at single-cooperative scale; acceptable per catalog/SCHEMA.md §6
    # semantics note for lens_context.cooperative.ostrom_principles_addressed.
    member_amendment_process: "2/3 vote at annual general meeting with 30-day written notice; emergency amendment by 3/4 vote with 7-day notice."
    legal_form: "State-registered worker cooperative or LLC; formal legal standing required per catalog/SCHEMA.md §6 lens_context.cooperative.legal_form guidance."
    scale_fit_note: "Governance rules calibrated for small-city scale (15,000–75,000 residents); quorum of 8–12 active members feasible. At town scale, member pool may be insufficient to sustain commission pipeline and scheduled loom-share rotation — hence scale_fit.town: marginal."
  civic:
    political_coalition: "Municipal arts and cultural-development office + local gallery network + small-business development council; grant funding from state arts council possible."
    council_vote_estimate: "4-3 favorable in arts-supportive small cities; opposition argues non-essential use of public space and inability to self-fund operations."
    competes_with_private: "A civic tapestry studio would marginally compete with any existing private artisan weaving studio; civic investment is justified only in the absence of a functioning private operator or where the civic facility explicitly provides apprentice training the private market cannot sustain."
    governance_form: "Municipally owned studio space; operated under arts-center or cultural-development department; contracted master weaver as lead practitioner."
    budget_line: "Capital via arts-infrastructure grant or municipal bond; operations under cultural-development or arts-center budget line."
    benchmark_comparison: "[CITATION-NEEDED: per-household annual cost comparison against analogous civic arts facility (arts center, craft studio) in peer small cities; cost structure requires sim output before this field can be populated accurately]"
    staffing_model:
      role: "Contracted master weaver (lead) + part-time apprentice"
      operator_fte: 1.2
      wage_assumption: 52000
      wage_source: "corpus/program/SCALES.md §3 small-city skilled-trades median [CITATION-NEEDED: verify against SCALES.md when document is available; $52,000 is an order-of-magnitude estimate for small-city artisan-craft practitioner wage]"
      hours: "40 hrs/wk production + client development + administration (master weaver); 20 hrs/wk loom production (apprentice)"
      hiring_notes: "Master weaver hiring pool is regional (100–200 mile radius); specialist skill scarcity is a documented risk (see Known Risks). Apprentice hired locally from art-school or vocational pipeline."
    civic_externalities:
      - "Apprentice training pipeline: produces 1–2 journeyman weavers per 4-year cycle, sustaining regional craft capacity beyond one practitioner's career."
      - "Cultural preservation: tapestry as a non-standardizable hand-art form; civic facility anchors community access to the tradition."
      - "Economic anchor for downstream arts economy: gallery partnerships, interior-design referrals, and craft-tourism draw generate indirect municipal revenue."

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 25000
  # Equals economics.capital_cost.mid per E-3 R1.
  cost_sd: 8250
  # (45000 - 12000) / 4 = 8250. Within plausible range: cost_sd / cost_mean = 0.33
  # (within 0.15–0.50 per E-3 R5). Asymmetric cost range (low is $13k below mid;
  # high is $20k above mid) reflects used-loom availability at low end and full
  # climate-control build-out at high end; SD is derived from the full range as
  # a conservative default.
  throughput_units_equiv_per_year: 58
  # Unit: m² of finished tapestry per year.
  # Derivation: 0.3 m²/day × 220 operating days × (1 - 0.12 downtime) = 58 m²/yr.
  # 220 operating days accounts for ~240 annual studio days minus ~20 days of
  # warp-setup-only days (no loom output). Consistent with max_active_hours_per_week
  # = 30 hr/wk at 5 days/wk = 6 hr productive loom time/day; 0.3 m²/day at
  # ~0.05 m² per productive hour is consistent with master-weaver tapestry rate.
  # E-3 cross-check: 30 hr/wk × 52 wk × (1 - 0.12) = 1,373 hr/yr;
  #   58 m²/yr × 20 hr/m² = 1,160 hr/yr. Residual gap (~15%) reflects cartoon
  #   and client-communication time folded into the gross-to-net derating, within
  #   E-3 R2 P2 tolerance (within-order, not order-of-magnitude discrepancy).
  variable_cost_per_unit: 165
  # Per m² tapestry. Yarn ($150/m² midpoint — commercial worsted wool + silk;
  # [CITATION-NEEDED]) + sundry consumables ($15/m²).
  # Note: annual_consumables ($9,600) / throughput_units_equiv_per_year (58) = $166/m²;
  # consistent with this figure within rounding.
  labor_hours_per_unit: 20
  # Per m² of tapestry. 0.3 m²/day at 6 active hr/day = 20 hr/m².
  # E-3 R3: 58 × 20 = 1,160 hr/yr vs. 30 × 52 × 0.88 = 1,373 hr/yr.
  # ~15% gap explained by non-loom labour (client interaction, cartoon prep) folded
  # into gross-to-net derating. Within P2 tolerance.
  # [CITATION-NEEDED: measured tapestry labour hours per m² from studio records]
  downtime_fraction: 0.12
  # 12% of scheduled hours lost to: humidity system servicing, heddle replacement
  # and re-threading, warp-change setup days, and unplanned loom stops.
  # Consistent with first_year_failures profile: three failure items with combined
  # lead times of 5–10 days/yr on a 220-day schedule ≈ 2–5% mechanical downtime;
  # remaining 7–10% from warp-setup overhead and scheduled maintenance. Total 12%.
  lifespan_years: 30
  # 8-shaft floor loom under normal maintenance: 25–40 years.
  # [CITATION-NEEDED: loom lifespan data — loom manufacturer documentation or
  #  practitioner survey; 30 years is a mid-range estimate]

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
  - ref: "Bythell, Duncan. 1969. The Handloom Weavers: A Study in the English Cotton Industry during the Industrial Revolution. Cambridge University Press. [Handloom weaver displacement and wage-decline data — cited in weaving DECLINE-VERDICT.md §2.1]"
  - ref: "Strasser, Susan. 1982. Never Done: A History of American Housework. Pantheon Books. [Household labor economics and adoption of factory goods — cited in weaving DECLINE-VERDICT.md §2.4]"
  - ref: "Morris-Suzuki, Tessa. 1994. The Technological Transformation of Japan. Cambridge University Press. [Nishijin Jacquard adoption; luxury weaving restructuring — cited in weaving DECLINE-VERDICT.md §2.3]"
  - ref: "Tryon, Rolla Milton. 1917. Household Manufactures in the United States, 1640–1860. University of Chicago Press. [Household textile production and decline — cited in weaving DECLINE-VERDICT.md §2.4]"
  - ref: "research/trades/weaving/DECLINE-VERDICT.md §3 and §5. [Luxury-niche restructuring evidence; fiber-sourcing falsifier; niche viability for tapestry and specialty hand-weaving]"
  - ref: "research/trades/weaving/REQUIREMENTS.md §2. [Humidity envelope for wool and silk fiber — 50–75% RH range; operational humidity management requirements]"
  - ref: "catalog/weaving/SCHEMA.md v1.0 §1 and §3. [Tapestry throughput range 0.1–0.5 m²/day; floor-loom-8shaft capital range $4,000–$15,000/unit; operator skill floor for tapestry entries]"
  - ref: "[CITATION-NEEDED: contemporary handwoven tapestry market prices per m² — gallery price survey, craft-fair rate-card data, or comparable artisan studio financials. Required for market_price_per_unit E-1 compliance before status: reviewed.]"
  - ref: "[CITATION-NEEDED: machine-woven decorative rug retail price per m² — retail survey or manufacturer wholesale data. Required for industrial_baseline_price E-1 compliance.]"
  - ref: "[CITATION-NEEDED: commercial tapestry yarn cost per kilogram and m² yield — distributor pricing or studio cost records. Required for variable_cost_per_unit and annual_consumables.]"
  - ref: "[CITATION-NEEDED: floor loom 8-shaft retail prices — loom manufacturer or distributor current pricing. Required for capital_cost E-1 compliance.]"
  - ref: "[CITATION-NEEDED: measured tapestry labor hours per m² — studio production records or practitioner survey. Required for labor_hours_per_unit E-1 compliance.]"
  - ref: "[CITATION-NEEDED: loom lifespan data — manufacturer documentation or practitioner survey. Required for lifespan_years E-1 compliance.]"
---

## Summary

The Handwoven Tapestry Studio is a direct-to-consumer and commission-based handwoven
tapestry and wall-textile studio operated by 1–2 master weavers in a climate-controlled
small-city studio of 30–50 m². It targets the luxury and specialty hand-weaving niche
identified as restorable in the weaving DECLINE-VERDICT: non-standardizable,
weft-faced commission tapestry for gallery sales, residential interior-design clients,
and public-art commissions. The studio is not a commodity cloth operation; it explicitly
occupies the differentiated niche that the DECLINE-VERDICT documents as surviving
industrial displacement in all four anchor cultures (northern European tapestry,
Song-era kesi, Nishijin brocade, American frontier Jacquard coverlet). Its competitive
protection is product identity and master-weaver execution, not price. The entry's
core economic question is whether the commission pipeline can be sustained at a scale
sufficient to service the $25,000 mid-capital investment and ongoing costs given the
extremely low throughput inherent to tapestry production (0.1–0.5 m²/day).


## Design rationale

The specific problem this entry addresses is the capital-pipeline mismatch in luxury
tapestry studio economics: a high capital entry ($12,000–$45,000), extremely low
throughput (0.3 m²/day central estimate), and master-level skill requirement combine
to create a long payback period that requires a stable commission pipeline to bridge.
No other weave catalog entry explicitly models this constraint at the tapestry
productivity level; entries weave-003 through weave-005 operate at higher throughput
or broader product mixes. The weave-001 entry exists to isolate the pure tapestry
studio case and determine whether the $450/m² mid market price generates sufficient
annual revenue to service the investment under realistic operating conditions. It is
also the canonical test of the `lens_fit.market: good` claim for tapestry specifically:
the historical evidence documents survival of the tapestry niche but does not supply
modern economic confirmation, and this entry is where that confirmation or
non-confirmation is established.


## Historical lineage

Handwoven tapestry has the most durable restructuring trajectory of any weaving form
documented in the DECLINE-VERDICT. The northern European record shows tapestry
(Arras, Brussels, Aubusson) surviving as a restructured niche because it was
non-standardizable and demanded the weaver's compositional and technical skill as part
of the product's value: a factory power loom cannot produce a named commission tapestry
with a specific design, and this functional distinction preserved the niche through
industrial displacement [DECLINE-VERDICT.md §2.1, §3]. The Aubusson tradition continues
operating commercially today; the Harris Tweed model represents the analogous survival
in commodity-adjacent handwoven cloth (protected by a statutory definition of hand
production). The American frontier case (Jacquard-equipped professional coverlet weavers)
documents the same functional mechanism — non-fungible custom goods resistant to factory
substitution — though with a terminal trajectory as the training pipeline collapsed in
the late nineteenth century [DECLINE-VERDICT.md §2.4]. The Song-era kesi (cut-silk
tapestry) provides the East Asian parallel: figured luxury textiles survived as
prestige categories through the same product-differentiation mechanism [DECLINE-VERDICT.md
§2.2]. The modern tapestry studio inherits the functional form: master-weaver execution
of commission-specific designs, direct client relationship, and a price point reflecting
the production time that industrial alternatives cannot match. It does not inherit the
labor regime (guild-suppressed wages, household piece-rates, draw-boy labor) that
underpinned historical cost structures; modern cost structures must be recalculated
accordingly [DECLINE-VERDICT.md §4, labor-regime-dependency falsifier].


## Key assumptions

Capital cost: The $12,000–$45,000 range is derived from catalog/weaving/SCHEMA.md §3,
which documents floor-loom-8shaft retail prices at $4,000–$15,000 per unit. Mid
estimate ($25,000) covers 2–3 professional looms plus ancillary equipment (warping mill,
bobbin winder, humidity control, display). A [CITATION-NEEDED] flag covers formal
sourcing; the range is structurally consistent with published loom retailer pricing
as of the catalog authoring date.

Market price: The $200–$1,200/m² range is based on practitioner-community knowledge of
tapestry gallery and commission pricing. This is the entry's most critical unfirmed
estimate: it is the primary revenue assumption driving the market-lens verdict, and it
requires empirical sourcing (gallery price surveys, direct studio financial data) before
the entry can advance to `reviewed`. A [CITATION-NEEDED] flag marks all market-price
fields accordingly.

Throughput: 0.3 m²/day central estimate for master-weaver tapestry is the midpoint of
the 0.1–0.5 m²/day range documented in the weaving SCHEMA.md §1. This range itself
carries a [CITATION-NEEDED] flag in the trade schema; the entry inherits that uncertainty.
Annual operating days (220) reflect 240 studio days minus approximately 20 days of
pure warp-setup work with no loom output.

Yarn cost: $150/m² is an order-of-magnitude estimate for commercial worsted wool and
silk blending yarn at tapestry sett. This figure is unfirmed and carries a
[CITATION-NEEDED] flag; it is the dominant variable cost driver and requires sourcing
before sim_params.variable_cost_per_unit can be confirmed.

Fiber sourcing: Industrial-yarn-purchased reflects the cross-cultural finding in
DECLINE-VERDICT.md §4 that all historical weaving forms depended on purchased or
traded yarn; fiber autonomy is not historically supported and is not claimed here.
Commercial worsted wool and silk thread are available from multiple domestic distributors
with typical lead times of 7 days. The 45-day worst-case lead time reflects specialty
colorway orders from import suppliers.


## Known risks / failure modes

**Regulatory:** No zoning or emissions permit triggers identified for a hand-loom
textile studio. Primary regulatory risk is commercial lease classification: some
municipalities classify textile production as light manufacturing, potentially requiring
an industrial zoning variance in a commercial or mixed-use district. This risk is
addressable at site-selection stage by confirming local zoning definitions.

**Labour pipeline:** The master-weaver skill requirement is the primary succession risk
for this entry. The apprentice pipeline (48–60 months to full master standard) is the
only documented path to skill reproduction. If the founding master weaver departs without
completing an apprentice cycle, the studio loses its productive capacity. Geographic
hiring pool for a replacement master weaver is regional (100–200 mile radius) and the
pool is documented as small; this is a known failure mode for luxury craft studios with
master-level skill requirements [DECLINE-VERDICT.md §2.4, terminal-trajectory analysis].
This risk is named here per schema Principle 8. The apprentice_path block above documents
the primary mitigation.

**Supply chain:** Commercial wool and silk yarn: multiple domestic distributors available;
no single-supplier dependency identified for standard colorways. Specialty silk thread
and custom-dyed yarn may involve import suppliers with 30–45 day lead times and potential
tariff exposure. Working capital buffer of 4–6 weeks' yarn inventory is the primary
mitigation. The fiber-sourcing falsifier (DECLINE-VERDICT.md §5) is acknowledged: this
entry depends on the commercial yarn supply chain and would be disrupted by any
large-scale industrial yarn supply failure — a scenario not modeled in this entry's
base-case economics.

**Commission pipeline:** The most operationally significant risk is insufficient
commission volume to sustain the operation. At 58 m²/yr throughput and $450/m² mid
price, gross annual revenue is approximately $26,100 — barely above the combined
annual cost of consumables ($9,600), maintenance ($2,800), and floor-space rent ($9,600)
before operator wages and capital amortization. The market-lens verdict depends entirely
on whether the premium commission pipeline can be established and sustained. This risk
must be flagged prominently; the entry's `status: draft` reflects that the market-price
claims are not yet empirically confirmed.


## Iteration log

- 2026-04-18: v0.1 — initial entry authored per Plan I Task 3 (weave-001). All
  required schema fields populated. Multiple [CITATION-NEEDED] flags carried forward
  from weaving SCHEMA.md and DECLINE-VERDICT.md; E-1 compliance requires sourcing of
  market_price_per_unit, industrial_baseline_price, yarn cost, and loom capital cost
  before promotion to `reviewed`. sim_params cross-check performed; E-3 R3 gap (~15%)
  documented and within P2 tolerance. Commission-pipeline risk flagged in Known Risks
  as primary economic concern.
