---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: bake-002
trade: baking
name: "Heritage Grain Subscription Bakery"
tagline: "CSA-model subscription bakery sourcing einkorn, spelt, emmer, and red wheat from a local mill partner"
status: draft
version: 0.1
supersedes: null
inspirations:
  - pre-industrial-guild-subscription-bread
  - modern-csa-grain-share-programs
  - community-supported-agriculture-model

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 32
ceiling_min_m: 2.7
ventilation: mechanical-extraction-required

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: electric-deck
energy_consumption_per_active_hour: "5 kWh (electric deck at full load, two decks)" # [CITATION-NEEDED: typical electric-deck consumption per active bake hour at this scale]
backup_fuel: null

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  loaves_per_day: 45
  # Mid-range subscription output per primary bake day (two bake days per week).
  # Unit: 800g heritage-grain sourdough boule equivalent. See Key Assumptions.
  batches_per_day: 2
  batch_size_loaves: 22
  # Two deck loads per bake day; ~22 loaves per load on a standard two-deck oven.
  max_active_hours_per_week: 30
  # Two bake days + prep/admin. Subscription model does not run 5-day production;
  # levain maintenance, sourdough timing, and grain milling (if applicable) spread
  # across additional days but active oven-on hours are concentrated.
  product_mix:
    bread: 90
    confection: 5
    specialty: 5
    catering: 0

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: journeyman-baker
operators_concurrent: "1-2"
apprentice_friendly: true
apprentice_path:
  training_stages: >
    Stage 1 (0–4 mo): subscription logistics, levain maintenance, grain handling,
    basic shaping under supervision. Stage 2 (4–12 mo): independent bulk-fermentation
    management, oven loading, delivery coordination. Stage 3 (12–24 mo): heritage-grain
    formula development, subscription troubleshooting, full-cycle independent operation
    including community communication.
  time_to_independent_operation: "~24 months to journeyman standard on this equipment and subscription model"
  succession_note: >
    Apprentice participates in bake days from Stage 1 onward, building formula muscle
    memory through volume repetition rather than isolated instruction. Subscription
    predictability (fixed loaf count, fixed delivery day) provides a structured
    learning scaffold absent in walk-in retail bakeries.

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD
  capital_cost: { low: 25000, mid: 45000, high: 70000 }
  install_cost: 4500
  # Electrical service upgrade for 30-60A dedicated deck circuit; minimal plumbing
  # (hand-wash sink already assumed in commercial kitchen base build-out). [CITATION-NEEDED]
  annual_maintenance: 1800
  # Deck element inspection and replacement reserves; proofer maintenance; minor oven
  # door seal replacements. [CITATION-NEEDED]
  annual_consumables: 14400
  # Flour (heritage grain at premium pricing: ~$1.50-2.50/lb), salt, starter culture
  # maintenance, proofing bags, subscription boxes and labels. [CITATION-NEEDED]
  floor_space_rent_per_year: 5760
  # 32 m² × $180/m²/year estimated commercial rate; imputed even if space is owned
  # per catalog/SCHEMA.md §6. [CITATION-NEEDED: local commercial kitchen rental rates]
  market_price_per_unit: { low: 8, mid: 12, high: 18 }
  # Per 800g heritage-grain sourdough boule equivalent, sold via subscription.
  # Low = entry-level subscription (budget CSA towns); mid = typical premium artisan
  # market; high = urban-adjacent or premium heritage-grain positioning. [CITATION-NEEDED]
  industrial_baseline_price: 4
  # Price of a 800g commodity sandwich loaf at grocery retail (industrial baseline).
  # Heritage grain specialty bread at mass-market retail typically $6-9 [CITATION-NEEDED];
  # $4 is the commodity industrial baseline per entry parameters.
  pricing_notes: >
    Per 800g heritage-grain sourdough boule equivalent delivered via subscription.
    Premium of 3x–4.5x over industrial commodity loaf ($4 baseline) is supported by
    heritage-grain differentiation (einkorn, spelt, emmer, red wheat), sourdough
    fermentation, local-mill sourcing narrative, and subscription convenience.
    Customer segment: households willing to pay CSA-model premium for traceability and
    artisan quality, typically professional-class families and food-value households.
  pricing_validation: >
    [CITATION-NEEDED: comparable subscription bakery rate-card survey or CSA grain-share
    comparable operator financials. Evidence type required: direct subscription-bakery
    sales data, not cost-plus derivation. Comparable evidence: artisan CSA pricing
    surveys, regional bakery cooperative financials, or farmers-market premium-bread
    comparable data.]

# ── TRADE-SPECIFIC FIELD ─────────────────────────────────────────────────────

flour_source_declaration: local-mill-partnership
# KEY DIFFERENTIATOR — this entry tests the "can you source local flour?" path.
# Success depends on finding a small-scale regional mill carrying heritage grain varieties
# (einkorn, spelt, emmer, red wheat). If no local mill exists, flour_source_declaration
# reverts to industrial-flour-purchased and the heritage-grain premium evaporates.
# See Mill Dependency note in Known Risks.

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:
  first_year_failures:
    - item: "Deck heating element (electric)"
      estimated_hours_to_failure: 2000
      replacement_cost: 650
      replacement_lead_time_days: 14
      serviceable_by: journeyman
      # Deck heating elements degrade under repeated thermal cycling; lead time
      # 7-21 days for non-stocked elements; replacement is journeyman-level. [CITATION-NEEDED]
    - item: "Proofer heating element or thermostat"
      estimated_hours_to_failure: 1500
      replacement_cost: 280
      replacement_lead_time_days: 10
      serviceable_by: operator
      # Proofer elements fail earlier than oven elements due to higher cycling frequency;
      # replacement is operator-serviceable on standard proofer cabinets. [CITATION-NEEDED]
    - item: "Stone grain mill motor or burr (if integrated grain mill is present)"
      estimated_hours_to_failure: 800
      replacement_cost: 450
      replacement_lead_time_days: 21
      serviceable_by: journeyman
      # IF APPLICABLE: only relevant when operator chooses to add a small stone mill
      # for on-site cracking or custom stone-ground flour. If no on-site mill is used
      # (local-mill-partnership supplies pre-milled flour), omit this item at runtime.
      # Burr wear and motor strain from high-extraction stone milling are the primary
      # failure modes. [CITATION-NEEDED]

  maintenance_schedule:
    daily:
      task: "Clean deck surfaces and crumb trays; check door seals; refresh levain culture; log subscription order counts"
      performed_by: operator
    weekly:
      task: "Deep clean proofer interior; inspect deck stone surfaces for thermal cracking; review grain flour inventory and reorder from mill partner"
      performed_by: operator
    quarterly:
      task: "Inspect electrical connections and element condition; calibrate oven thermostat; audit subscription list and churn rate; check proofer humidity sensor"
      performed_by: journeyman
    annual:
      task: "Full oven service: element inspection/replacement if indicated, door gasket replacement, deck stone assessment; review mill-partnership agreement and grain pricing"
      performed_by: specialist

  startup_shutdown_overhead_per_day_min: 45
  # Heritage-grain sourdough baking requires: levain check (10 min), deck preheat ramp
  # (20 min to full temperature from cold), post-bake cleanup and steam-injector descale
  # cycle (15 min). Total ~45 min/bake-day overhead.
  max_active_hours_realism_note: >
    30 hr/wk is a net estimate already accounting for non-bake days (levain maintenance,
    subscription admin, delivery prep). The two primary bake days each carry 45 min
    startup/shutdown overhead (~1.5 hr/week), reducing effective oven-on production to
    ~28.5 hr/wk. sim_params.throughput_units_equiv_per_year uses the derated figure.
  interruption_notes: >
    Subscription model reduces walk-in interruptions to near zero on bake days; however,
    subscription management (email, pickup logistics, substitutions) consumes ~2–3 hr/week
    outside active bake time. Heritage grain bulk fermentation requires monitoring checks
    every 30–60 minutes during bulk; operator is not continuously at oven during this window
    but must remain on-site. These interruptions are folded into the 30 hr/wk estimate.
  consumables_lead_time_days: { typical: 7, worst: 45 }
  # Flour from local mill: typical 7-day lead; worst-case 45 days if mill has grain
  # sourcing delay, equipment downtime, or seasonal harvest gap. Single-source risk.
  throughput_variance:
    seasonal: "Holiday peak (Nov-Dec) for gift subscriptions and holiday loaf specials; summer (July-Aug) moderate trough as subscriber households travel"
    worst_month_fraction_of_average: 0.65
    best_month_fraction_of_average: 1.35
  operator_impact:
    noise_db: 62
    # Electric deck oven; primary noise source is ventilation fan and proofer compressor.
    # Substantially quieter than wood-fired or gas-fired alternatives. [CITATION-NEEDED]
    heat_exposure: "Moderate; deck oven surface temperatures 230-290°C but operator exposure limited to brief loading/unloading intervals; kitchen ambient elevated 5-10°C above ambient during bake"
    emissions: "Near-zero on-site combustion emissions; electric deck produces no CO or particulate; steam from baking process is the primary effluent — mechanical extraction required to manage humidity"
    physical_demand: "Moderate; repeated lifting of proofing baskets and loaded deck peels (3-6 kg each); sustained standing on bake days; dough work is physically demanding but concentrated in 2-3 hr mixing windows"

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Commercial kitchen zoning required; electric-deck oven has the cleanest permit path of any baking energy source; residential zoning is insufficient unless cottage-food-law exemption applies (scale here exceeds cottage-food thresholds in most jurisdictions)"
  emissions: "Electric deck produces near-zero combustion emissions; no particulate or CO permit typically required; mechanical extraction for steam and humidity management is standard commercial kitchen requirement"
  other: "Food handler certification and commercial kitchen license required; cottage-food law does not cover subscription delivery at this volume; local health department inspection required; subscription delivery may require additional food-transport permit in some jurisdictions"

# ── CONTEXT FIT ──────────────────────────────────────────────────────────────

lens_fit:
  market: good
  cooperative: good
  civic: marginal

scale_fit:
  village: marginal
  town: good
  small_city: good

# ── LENS CONTEXT ─────────────────────────────────────────────────────────────

lens_context:
  cooperative:
    membership_boundary: >
      Subscription members within delivery radius (typically 10–20 miles from bakery).
      Membership = active subscription; members prepay weekly or monthly allotment.
      No explicit geographic restriction but delivery logistics naturally bound the catchment.
    rules_source: >
      Subscription agreement and cooperative bylaws (if formally registered);
      subscription terms set by operator and amended by operator with 30-day subscriber
      notice; member vote may be instituted once subscriber base exceeds 40 households.
    monitoring: >
      Subscription payments tracked via payment processor; loaf count logged per delivery;
      operator maintains subscriber ledger; fulfillment rate monitored weekly against
      subscription commitments.
    graduated_sanctions: >
      Late payment: 7-day grace → subscription pause → cancellation. Operator-side
      failure to fulfill: pro-rated credit → subscription discount → exit option for
      subscriber. No member-to-member sanction required at this governance scale.
    conflict_resolution: >
      Direct operator-subscriber communication as primary channel; disputed fulfillment
      resolved by operator credit or substitution; no formal arbitration body required
      at this scale; if formal cooperative is registered, member-elected board arbitrates.
    ostrom_principles_addressed: [1, 2, 3, 4, 5, 6]
    # Principle 7 (nested organisations) and Principle 8 (external recognition) are
    # not addressed at single-cooperative micro-scale; this is acceptable per
    # catalog/SCHEMA.md §6 semantics note on Ostrom principles.
    member_amendment_process: >
      Subscription terms amended by operator with 30-day written notice to all
      subscribers; if cooperative is formally registered: 2/3 vote at annual subscriber
      meeting with 21-day notice; emergency amendment requires 3/4 vote with 7-day notice.
    legal_form: >
      Subscription model does not require formal cooperative registration at launch;
      recommended path: sole proprietorship or LLC at start, with option to convert to
      state-registered consumer cooperative or worker cooperative once subscriber base
      exceeds 50 households and governance complexity warrants formal structure.
      [CITATION-NEEDED: state-specific cooperative registration guidance]
    scale_fit_note: >
      Governance rules are calibrated for town-scale (2,000–15,000 residents), where a
      subscriber base of 30–80 households is achievable within the delivery radius.
      At village scale (<2,000 residents), subscriber pool is too small to cover fixed
      costs reliably — see scale_fit.village: marginal. At small_city scale, logistics
      complexity may require additional delivery infrastructure beyond single-operator capacity.

  civic:
    political_coalition: >
      Food-access advocates + local agricultural network + town health board; heritage
      grain programs may qualify for agricultural development or local food system grants
      in some jurisdictions.
    council_vote_estimate: >
      4-3 marginal; civic investment in a subscription bakery is politically unusual;
      opposition argues that private operators should serve this function; strongest
      case requires framing as food-security or agricultural-heritage program.
    competes_with_private: >
      Where a functioning private artisan subscription bakery already exists, civic
      investment would directly displace it and is not justified under this entry.
      Civic lens is viable only where no private operator serves this niche — applicable
      in underserved towns lacking premium artisan bread access.
    governance_form: >
      Municipally supported but operator-run; most viable as public-private partnership
      where municipality provides subsidized kitchen space and the operator runs the
      subscription business; full municipal ownership is unusual for food production.
    budget_line: >
      Capital via community development grant or agricultural fund; operating subsidy
      via food-access or local-food-system program line; operator salary from subscription
      revenue supplemented by municipal subsidy if civic framing is maintained.
    benchmark_comparison: >
      [CITATION-NEEDED: per-household annual cost comparison vs. named analogous civic
      food-access program in peer towns. Estimated $3–8/hh/yr subsidy at town scale
      (if municipal kitchen space is provided at no cost); comparable food-bank
      operational costs are ~$15–35/hh/yr in peer municipalities — but direct comparison
      requires a named cited program.]
    staffing_model:
      role: "contracted journeyman baker + part-time subscription coordinator"
      operator_fte: 1.0
      wage_assumption: 42000
      # Journeyman baker annual wage at town-scale; lower than master baker wage
      # consistent with journeyman floor for this entry. [CITATION-NEEDED]
      wage_source: "corpus/program/SCALES.md §3 town-scale skilled-trades median — journeyman tier [CITATION-NEEDED: confirm value against SCALES.md when published]"
      hours: "25-30 hrs/wk active baking + 5 hrs/wk subscription administration and delivery"
      hiring_notes: >
        Journeyman baker required; hiring pool regional (50–75 mile radius for heritage-grain
        specialist); passion for grain-sourcing narrative is a soft requirement for subscription
        retention; local culinary program graduate or apprentice-path promotion are viable
        internal hiring paths.
    civic_externalities:
      - "Heritage grain agricultural preservation: subscription volume creates stable purchase commitment enabling small regional mills to maintain heritage variety cultivation that would otherwise be commercially unviable"
      - "Food-system resilience: local-mill-partnership plus fixed weekly demand creates a short, visible supply chain — grain provenance is traceable to regional farm level, reducing dependence on commodity flour distribution networks"
      - "Nutritional access: heritage grain varieties (einkorn, emmer) offer documented nutritional differentiation; subscription model makes these accessible to households that would not otherwise navigate specialty retail channels"

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 45000
  # Must equal economics.capital_cost.mid. E3-R1.
  cost_sd: 11250
  # Derived from (capital_cost.high - capital_cost.low) / 4 = (70000 - 25000) / 4 = 11250.
  throughput_units_equiv_per_year: 4212
  # Unit: 800g heritage-grain sourdough boule equivalent.
  # Derivation: 90 loaves/week (mid of 60-120 range) × 52 weeks × (1 - 0.10 downtime)
  # = 90 × 52 × 0.90 = 4,212 loaves/year.
  # Cross-check with derated hours: 30 hr/wk × 52 × 0.90 = 1,404 hr/year;
  # at 0.333 hr/loaf → 4,216 ≈ 4,212. Consistent. See Key Assumptions.
  variable_cost_per_unit: 3.42
  # Direct cost per loaf: heritage grain flour ~$2.50 (premium mill pricing, ~600g flour
  # per 800g loaf) + salt, starter, packaging ~$0.60 + energy ~$0.32 per loaf.
  # Total ~$3.42. [CITATION-NEEDED: heritage grain flour pricing per kg at small-mill rates]
  labor_hours_per_unit: 0.333
  # Artisan sourdough at subscription scale: 0.33 hr/loaf includes mixing, shaping,
  # loading/unloading, and proportionate startup/shutdown overhead.
  # Cross-check: 4,212 × 0.333 = 1,403 hr/year ≈ 30 hr/wk × 52 × 0.90 = 1,404. Passes E3-R3.
  downtime_fraction: 0.10
  # 10% downtime: first-year equipment failures (~3-4 weeks), subscription breaks
  # (holidays), and supply interruptions from mill partner. Conservative for a new
  # subscription bakery. Consistent with operations_reality failure profile. [CITATION-NEEDED]
  lifespan_years: 15
  # Electric deck oven lifespan under regular maintenance: 12-20 years; 15 years is the
  # central estimate for amortisation calculation. [CITATION-NEEDED]

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
  - ref: "[CITATION-NEEDED: electric-deck oven energy consumption benchmarks — commercial bakery equipment energy survey]"
  - ref: "[CITATION-NEEDED: artisan subscription bakery capital cost ranges — equipment vendor price lists or bakery startup cost surveys, 2023-2026]"
  - ref: "[CITATION-NEEDED: heritage grain flour pricing at small-mill scale — regional mill price lists or grain cooperative pricing, 2023-2026]"
  - ref: "[CITATION-NEEDED: subscription artisan bread market pricing — comparable CSA bakery rate cards or artisan bakery pricing surveys]"
  - ref: "[CITATION-NEEDED: industrial commodity bread baseline price — USDA retail food price data or BLS CPI food component, 2024-2026]"
  - ref: "[CITATION-NEEDED: deck heating element failure rates and replacement costs — commercial oven service manuals or repair industry data]"
  - ref: "[CITATION-NEEDED: commercial kitchen rental rates per m² — local commercial real estate survey or SBA small business facility cost guidance]"
  - ref: "[CITATION-NEEDED: electric deck oven lifespan under commercial use — manufacturer specifications or commercial kitchen equipment lifecycle surveys]"
  - ref: "Ostrom, E. 1990, Governing the Commons, Cambridge University Press — Ostrom design principles (Principles 1-8)"
  - ref: "[CITATION-NEEDED: CSA model subscription agriculture precedents — community-supported agriculture academic literature or USDA CSA program data]"
---

## Summary

The Heritage Grain Subscription Bakery (bake-002) is a CSA-model artisan operation built around a fixed subscriber base receiving weekly boxes of heritage-grain sourdough bread — einkorn, spelt, emmer, and red fife wheat loaves baked twice weekly and delivered or collected on a set schedule. The model is sized for 60–120 loaves per week (mid: 90), operated by 1–2 journeyman bakers in a 25–40 m² commercial kitchen with an electric-deck oven. Its defining characteristic is the `flour_source_declaration: local-mill-partnership` — sourcing directly from a regional small mill that carries heritage variety whole and stone-ground flours. This makes bake-002 the test case for the "can you source local flour?" decision branch in the CERES evaluation framework: the subscription price premium and the civic agricultural-preservation externalities are both contingent on that partnership being real and reliable.

## Design rationale

This entry exists as a distinct catalog entry because no other baking design tests the intersection of (1) subscription-lock revenue model, (2) heritage grain specialty positioning, and (3) explicit mill-partnership supply-chain dependency. Standard artisan bakeries (bake-001) use industrial flour and open retail; community bakeries (bake-010 through bake-013) optimize for access rather than premium grain sourcing. The subscription model restructures the economic logic entirely: subscribers prepay, eliminating week-to-week demand uncertainty; the fixed loaf count per week allows precise flour ordering from the mill partner; and the community connection is structural (subscribers know the baker, know the grain source) rather than incidental. The entry also introduces a specific failure mode — mill-partner dependency — that does not appear in any other baking entry. If the local mill closes, changes its variety offering, or raises prices to non-competitive levels, bake-002's heritage premium evaporates and the entry degrades to a standard industrial-flour subscription bakery with reduced pricing power.

## Historical lineage

Two functional lineages inform bake-002. First, the pre-industrial European guild baker operated on an effective subscription model: households secured a weekly bread allotment through guild arrangements, often paying in advance or through seasonal grain contributions to the baker. The functional inheritance is the demand-predictability structure — the baker knows exactly how much flour to source and how many loaves to produce before beginning, which is the same economic logic as a modern CSA subscription. Second, the modern community-supported agriculture movement (CSA farming, originating in Japan and Switzerland in the 1960s-1980s and spreading to the United States through the 1990s) established the operational template: subscribers prepay for a "share" of production, accepting seasonal variation and supply risk in exchange for a direct relationship with the producer and a price discount or quality premium over retail. The functional inheritance is the governance structure — subscriptions are a simplified cooperative form where membership equals subscription and the break-even condition is covering fixed costs from subscriber count rather than from market price competition. The specific constraint that cannot be reproduced from historical form is the guild's grain-supply security: medieval guild bakers operated within a regulated grain-supply system enforced by municipal authority. Modern bake-002 operators must find and maintain their own mill partnership without that institutional backstop.

## Key assumptions

Capital cost range ($25,000–$70,000) is estimated from electric-deck oven retail pricing (single or double-deck, approximately $8,000–$20,000 depending on deck area), plus proofing cabinet ($2,000–$5,000), mixing equipment ($3,000–$8,000), grain storage, and kitchen fit-out. The low end assumes a used or refurbished oven in an existing commercial kitchen space; the high end assumes new equipment with full kitchen build-out. `[CITATION-NEEDED: equipment vendor price lists]`

The `flour_source_declaration: local-mill-partnership` assumes the operator has identified and negotiated with a local or regional stone mill carrying at least two heritage grain varieties. The pricing model depends on this partnership: heritage grain whole-wheat flour from regional mills is estimated at $1.50–$2.50/lb versus $0.50–$0.90/lb for commodity all-purpose flour. `[CITATION-NEEDED: regional mill pricing data]` If no local mill exists within a commercially viable sourcing radius (~150 miles), the declaration reverts to `industrial-flour-purchased` at commissioning time. Operators in mill-poor geographies must re-evaluate whether heritage positioning is defensible at their price point.

The throughput unit is an 800g heritage-grain sourdough boule equivalent. Mid throughput is 90 loaves/week (subscription capacity for ~45–90 households depending on household subscription size). Annual throughput of 4,212 loaves is derived from 90 loaves/week × 52 weeks × 0.90 (10% downtime). The `labor_hours_per_unit` of 0.333 hr/loaf passes the E3-R3 cross-check: 4,212 × 0.333 ≈ 1,403 hr/year ≈ 30 hr/wk × 52 × 0.90 = 1,404 hr/year.

Market pricing ($8–$18/loaf mid $12) is based on the subscription artisan bread segment; the industrial baseline ($4) is the commodity bread retail price. `[CITATION-NEEDED: USDA retail food price data; subscription bakery rate-card survey]` The $12 mid price implies a 3× premium over industrial baseline, consistent with heritage grain and sourdough positioning in comparable artisan subscription programs. Pricing validation evidence is flagged `[CITATION-NEEDED]` throughout, as no internal sales data is available at catalog authoring time.

## Known risks / failure modes

**Regulatory.** A subscription bakery at 90 loaves/week exceeds cottage-food-law thresholds in most U.S. jurisdictions (typically capped at $25,000–$50,000 annual gross revenue, which this model approaches or exceeds at the mid price point). Commercial kitchen zoning and food-handler licensing are non-negotiable. Some jurisdictions additionally require a commercial baking license, commercial liability insurance, and delivery-vehicle food-transport permits. The primary zoning risk is that affordable commercial kitchen space in towns and small cities may be scarce; the operator may need to share or lease a shared commercial kitchen, which conflicts with bake-day scheduling for subscription consistency.

**Labour pipeline.** `operator_skill_floor: journeyman-baker` means the entry cannot run on an untrained operator. Heritage grain sourdough management — managing the longer fermentation times of einkorn and emmer relative to modern wheat, adjusting hydration for varying extraction rates from stone-milled flour, handling the weaker gluten structure of ancient grains — requires formed fermentation judgment. The apprentice path is viable but takes 24 months to full independence. The key succession risk is mill-knowledge dependency: if the baker who built the mill relationship departs, the incoming baker must rebuild that relationship from scratch, and the mill may not offer the same terms to an unknown new operator.

**Supply chain.** The mill-partnership dependency is the single most consequential supply-chain risk in this entry. A local-mill-partnership is a single-source dependency: if the mill experiences grain sourcing failures (poor heritage-variety harvest, supply gap from regional farms), equipment failure (stone mill burr replacement takes weeks), or business closure (small mills are financially fragile operations), the subscription bakery loses its differentiating input and must either substitute industrial flour (losing the heritage premium) or suspend subscriptions. Authors commissioning this entry in a specific geography must verify that at least one regional mill within the sourcing radius carries the target heritage varieties before declaring `flour_source_declaration: local-mill-partnership`. If no such mill exists, this field reverts to `industrial-flour-purchased` and the pricing model, the civic externalities, and the cooperative differentiation argument all require revision downward. The `consumables_lead_time_days.worst: 45` captures the tail risk of mill disruption.

## Iteration log

- 2026-04-18: v0.1 — Initial creation per Plan G Task 4 (bake-002). Heritage grain subscription bakery, CSA model, local-mill-partnership flour_source_declaration, electric-deck energy source. All economic figures flagged [CITATION-NEEDED] pending source validation. Mill-dependency failure mode documented in Known Risks. sim_params cross-checked: E3-R1 passes (cost_mean = capital_cost.mid = 45000); E3-R3 passes (4,212 × 0.333 ≈ 1,404 hr/year = 30 hr/wk × 52 × 0.90); cost_sd = 11,250 = (70,000 - 25,000) / 4 (E3-R5 in range). civic lens_context populated with [CITATION-NEEDED] on benchmark_comparison pending SCALES.md publication.
