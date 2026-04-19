---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: bake-003
trade: baking
name: "Community Grain-Share Bakery"
tagline: "Coop-operated bakery where member grain contributions and local-mill flour flow into shared baking sessions and proportional bread distribution"
status: draft
version: 0.1
supersedes: null
inspirations: [medieval-european-banalite-oven, french-boulangerie-cooperative-form, contemporary-grain-csa-model]

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 50
ceiling_min_m: 3.0
ventilation: mechanical-extraction-required

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: electric-deck
energy_consumption_per_active_hour: "6 kWh"
backup_fuel: null

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  loaves_per_day: 80
  batches_per_day: 4
  batch_size_loaves: 20
  max_active_hours_per_week: 40
  product_mix:
    bread: 90
    confection: 5
    specialty: 5
    catering: 0
  throughput_variance:
    seasonal: "Moderate summer trough (July-August) as member participation drops; harvest-season peak (Sept-Nov) when grain contributions arrive and member engagement rises."
    worst_month_fraction_of_average: 0.60
    best_month_fraction_of_average: 1.45

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: journeyman-baker
operators_concurrent: "1-4"
apprentice_friendly: true
apprentice_path:
  training_stages: "Stage 1 (0–3 mo): safety orientation, equipment familiarization, dough handling basics under manager supervision. Stage 2 (3–9 mo): independent sourdough mixing and shaping with journeyman review of fermentation timing; oven loading under supervision. Stage 3 (9–24 mo): full sourdough session management, starter maintenance, basic supervision of other members. Stage 4 (24–36 mo): independent session management; capable of training Stage 1 members."
  time_to_independent_operation: "~24 months to journeyman standard on this equipment for members with consistent weekly participation; cooperative manager reaches full session-management capability by month 6."
  succession_note: "The coop manager role is the professional succession point. The apprentice path for members generates a pool of Stage 3-4 participants from which a future manager candidate can be recruited; succession is integrated into normal cooperative operations rather than requiring an outside hire."

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD
  capital_cost: { low: 35000, mid: 60000, high: 95000 }
  install_cost: 12000
  annual_maintenance: 3200
  annual_consumables: 8500
  floor_space_rent_per_year: 9600
  # market_price_per_unit omitted: lens_fit.market is poor; entry never evaluated on market lens.
  # industrial_baseline_price omitted: lens_fit.market is poor.

# ── TRADE-SPECIFIC ────────────────────────────────────────────────────────────

trade_specific:
  flour_source_declaration: local-mill-partnership
  # Member farms supply grain to a contracted local mill; mill delivers flour to bakery coop.
  # The grain-contribution credit system converts grain weight (at agreed flour-conversion rate)
  # into member baking credits. Surplus flour beyond member credits is purchased commercially.
  # This is the direct implementation of the DECLINE-VERDICT mill-dependency falsifier path:
  # the mill is named, the relationship is contractual, and the entry does not assume
  # on-site milling. The supply-chain dependency is acknowledged and managed, not dissolved.

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:
  first_year_failures:
    - item: "Deck heating element (primary deck)"
      estimated_hours_to_failure: 1800
      replacement_cost: 950
      replacement_lead_time_days: 14
      serviceable_by: specialist
    - item: "Oven thermostat / temperature controller"
      estimated_hours_to_failure: 2500
      replacement_cost: 380
      replacement_lead_time_days: 7
      serviceable_by: journeyman
    - item: "Deck stones (thermal shock cracking from member handling)"
      estimated_hours_to_failure: 1200
      replacement_cost: 240
      replacement_lead_time_days: 5
      serviceable_by: operator
  maintenance_schedule:
    daily:
      task: "Wipe deck surfaces, clear crumb residue, inspect door seals, log session usage and flour consumption per member"
      performed_by: operator
    weekly:
      task: "Inspect deck stones for hairline cracks; calibrate thermostat against reference thermometer; clean steam injector nozzles; review member baking-credit ledger for accuracy"
      performed_by: operator
    quarterly:
      task: "Full thermostat calibration and element inspection by qualified technician; descale steam injector; inspect and clean exhaust extraction system; audit flour delivery weights against mill invoices"
      performed_by: journeyman
    annual:
      task: "Full deck oven service: element test, deck stone inspection and replacement if indicated, door gasket replacement, electrical safety certification; cooperative governance annual audit"
      performed_by: specialist
  startup_shutdown_overhead_per_day_min: 40
  max_active_hours_realism_note: "40 hr/wk is the theoretical ceiling across five operating days. Net of 40 min/day startup-shutdown overhead (5-day week = 200 min/wk = 3.3 hr/wk), effective production hours are approximately 36.7 hr/wk. sim_params.throughput_units_equiv_per_year uses the derated figure. An additional coordination overhead of approximately 15 min per member session change (averaging 2 session changes/day) is folded into the throughput variance via downtime_fraction."
  interruption_notes: "Member turnover between sessions (~15 min/changeover, 2 changeovers/day) is the primary intraday interruption not captured in startup_shutdown overhead. Manager instruction time during member sessions (~20 min/session-day average, higher for new members) is absorbed into normal operations and folded into the downtime_fraction. Mill delivery coordination (~30 min/delivery, approximately twice per month) occurs on non-peak days."
  consumables_lead_time_days: { typical: 3, worst: 21 }
  throughput_variance:
    seasonal: "Moderate summer trough (July-August) as member participation drops; harvest-season peak (Sept-Nov) when grain contributions arrive and member engagement rises."
    worst_month_fraction_of_average: 0.60
    best_month_fraction_of_average: 1.45
  operator_impact:
    noise_db: 62
    heat_exposure: "Moderate; electric deck ovens do not generate the radiant heat profile of gas or wood-fired alternatives. Multi-station layout distributes heat load. Adequate with mechanical extraction."
    emissions: "Near-zero on-site combustion emissions; electric deck source. Flour dust from mixing and shaping operations requires adequate ventilation per OSHA flour-dust thresholds. [CITATION-NEEDED: OSHA flour-dust PEL threshold for commercial bakeries]"
    physical_demand: "Moderate; repeated dough handling, loading and unloading oven decks, flour sack management (~25 kg bags). Member operators range in physical capacity; baker manager handles the most physically demanding tasks."

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Commercial or light-industrial zoning required for a shared commercial kitchen serving multiple operators; some jurisdictions permit coop bakeries in mixed-use zones with food-service occupancy classification."
  emissions: "Electric deck source produces no combustion emissions on-site; flour-dust ventilation requirements apply under commercial bakery regulations. Air-quality permit not typically required for electric-only baking. [CITATION-NEEDED: local commercial-kitchen ventilation code for flour dust]"
  other: "Cooperative corporation registration required (state-level); food handler certification for coop manager and potentially all member-operators depending on jurisdiction; shared commercial kitchen inspection applies to multi-user baking facilities; grain-credit ledger system may require commodity-exchange registration in some jurisdictions — legal review recommended before launch."

# ── CONTEXT FIT ──────────────────────────────────────────────────────────────

lens_fit:
  market: poor
  cooperative: good
  civic: marginal

scale_fit:
  village: poor
  town: good
  small_city: good

# ── LENS CONTEXT ─────────────────────────────────────────────────────────────

lens_context:
  cooperative:
    membership_boundary: "Town or small-city residents and surrounding agricultural township within practical grain-delivery distance (~30 miles). Annual paid membership dues required. Members may additionally contribute grain from partner farms (or purchase grain contribution credits from the coop pool) to earn baking-session credits above the base annual allocation. Non-contributing members receive a base annual allocation of baking sessions. Membership is open; no residency exclusions beyond geographic practicality."
    rules_source: "Cooperative corporation bylaws, adopted at founding and amendable by member vote. Operating rules (session booking, grain-credit conversion rate, distribution ratios) set by elected member council and updated annually. Bylaw amendments require 2/3 member vote; operating-rule changes require simple majority of member council with 14-day member notice period."
    monitoring: "Baking session bookings logged electronically; flour consumption recorded per session by manager; grain contributions weighed and invoiced at mill; member credit ledger maintained by elected treasurer and audited annually by independent member committee. Manager files monthly usage reports to member council."
    graduated_sanctions: "Overage on booked flour (>10% above session allocation without advance notice): formal warning. Second overage within 6 months: 10% credit deduction. Equipment misuse causing damage: repair cost charged to member account. Three formal warnings within one membership year: membership review by council. Non-payment of dues after 60-day grace period: membership suspension until dues current."
    conflict_resolution: "Disputes over session allocations, credit calculations, or equipment damage handled first by manager mediation (informal). Unresolved disputes escalate to elected grievance committee (3 members, not party to dispute). Grievance committee decision is final unless appealed to full member vote at next scheduled general meeting. External mediation available by mutual agreement."
    ostrom_principles_addressed: [1, 2, 3, 4, 5, 6, 7]
    member_amendment_process: "Bylaw amendments require 2/3 vote at annual general meeting (AGM) with 30-day written notice to all members. Emergency amendments (health/safety) require 3/4 vote at special meeting with 7-day notice. Operating rules (non-bylaw) may be amended by member council majority vote with 14-day member notice; members may petition for full membership vote on any operating rule by presenting signatures of 15% of active membership."
    legal_form: "State-registered cooperative corporation (per applicable state cooperative-corporation statute); registered with state Secretary of State; cooperative purpose and democratic governance provisions in articles of incorporation. Municipal food-enterprise acknowledgment recommended but not required for operation."
    scale_fit_note: "Rules calibrated for town-to-small-city scale (2,000–75,000 residents). The grain-contribution credit system requires a minimum viable member base of approximately 30–50 active baking members to sustain weekly session volume and justify the mill-partnership logistics. At village scale (<2,000), member density is insufficient to sustain the session throughput and mill delivery economics — hence scale_fit.village: poor. At town and small-city scale, a 30–100 active member base is plausible and the governance burden (monthly council meetings, annual AGM, credit ledger) is proportionate."

  civic:
    political_coalition: "Municipal food-security committee or similar body as anchor institutional supporter; local agricultural extension service as technical advisor for grain-contribution program; farmers-market association as outreach channel for member recruitment from existing local-food consumer base."
    council_vote_estimate: "4-3 favorable in a typical town council, assuming food-security framing; marginal because this is a cooperative structure requiring only light municipal engagement (zoning accommodation, possible small grant) rather than full civic ownership — council members may reasonably prefer the cooperative to manage itself. Main opposition argument: concerns about commercial-kitchen zoning precedent and grant use for what is essentially a private coop."
    competes_with_private: "Any existing artisan bakeries in the service area are potential grain-supply partners or customers, not direct competitors; the coop's primary output is for member consumption, not retail sale. If a functioning private bakery already supplies the community's artisan-bread demand, the civic case for supporting a competing coop is weakened — the civic pitch should emphasize food-security and grain-supply-chain resilience rather than bread supply as such."
    governance_form: "Member-owned cooperative corporation, self-governing per bylaws. Municipal engagement limited to zoning accommodation, possible one-time startup grant, and food-security partnership framing. Town does not own or operate the facility."
    budget_line: "No ongoing municipal budget line required under cooperative model. One-time startup support (grant or low-interest loan from municipal economic-development fund) is the primary civic engagement pathway. Ongoing operations are self-funded from member dues and session fees. If positioned as food-security infrastructure, an annual sustaining grant from municipal food-access or resilience budget is plausible."
    benchmark_comparison: "[CITATION-NEEDED: per-household annual cost comparison against named food-access programs in peer towns — e.g., community meal program, food-pantry grant levels, municipal farmers-market subsidy. Estimated at $1.50–$3.00/hh/yr for a one-time startup grant of $15,000–$30,000 in a town of 5,000–10,000 households, well below comparable food-access program per-household costs, but this estimate requires a named peer-town benchmark before promotion.]"
    staffing_model:
      role: "cooperative manager (journeyman baker, full-time)"
      operator_fte: 1.0
      wage_assumption: 52000
      wage_source: "corpus/program/SCALES.md §3 town-scale skilled-trades median; journeyman-baker wage adjusted to cooperative-manager role with administrative component [CITATION-NEEDED: verify against SCALES.md current figure]"
      hours: "40 hrs/wk: 28 hrs production/supervision of member sessions + 12 hrs administration (credit ledger, mill coordination, member communications, booking management)"
      hiring_notes: "Journeyman baker with cooperative-management experience or willingness to learn; hiring pool regional (75-mile radius for a journeyman baker with coop-management interest). Smaller than a standard bakery hiring pool due to the cooperative-management component; plan for 60–90 day search. Part-time assistant (paid or member-volunteer) recommended once membership exceeds 60 active members."
    civic_externalities:
      - "Food-security infrastructure: demonstrated local grain-to-bread pathway reduces community dependence on industrial flour supply chains during regional disruptions; the local-mill partnership is a documented supply-chain resilience asset."
      - "Grain-supply-chain integration: the coop creates a direct economic link between local farms, local milling, and local bread consumption; sustains demand for local grain varieties (heritage wheats, spelt, rye) that industrial flour markets do not incentivize."
      - "Cooperative skill formation: members gain fermentation, baking, and dough-management skills; the apprentice path produces journeyman-capable members who can sustain cooperative operations beyond founder turnover."
      - "Community food-culture anchor: a functioning community bakery with grain-share program provides a visible, participatory food-sovereignty institution that strengthens local food-system identity in ways a purely market-facing bakery does not."

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 60000
  cost_sd: 15000
  throughput_units_equiv_per_year: 18000
  # Derivation: 80 loaves/day × 260 operating days/year × (1 − 0.13 downtime) = ~18,096.
  # Unit: 800g sourdough boule equivalent. Consistent with loaves_per_day × batches/day logic.
  # Derated active hours check: 36.7 hr/wk net × 52 × 0.87 × ~11.1 loaves/hr ≈ 18,400 — consistent.
  variable_cost_per_unit: 0.92
  # Per loaf: flour ~$0.62 (local-mill-partnership premium over commodity), energy ~$0.18 (6 kWh/hr
  # ÷ ~11 loaves/hr × $0.33/kWh [CITATION-NEEDED: commercial electricity rate assumption]),
  # misc consumables ~$0.12. Member grain contributions reduce effective flour cost for credited
  # sessions; variable_cost_per_unit reflects the blended average across all sessions.
  labor_hours_per_unit: 0.105
  # Manager labor only (members provide their own baking labor). 36.7 net hr/wk × 52 × 0.87 / 18,000
  # = ~0.092 hr/unit. Rounded up to 0.105 to reflect manager coordination overhead not captured
  # in straight production hours (session changeovers, credit administration, mill liaison).
  downtime_fraction: 0.13
  # Slightly above typical artisan-bakery baseline (0.08–0.10) due to:
  # member session changeovers (~2/day), member-skill variability causing occasional batch
  # losses, seasonal participation trough (July–August). Consistent with
  # worst_month_fraction_of_average of 0.60 and first_year_failures profile.
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
  - ref: "Langdon, John. 2004. Mills in the Medieval Economy: England, 1300–1540. Oxford University Press. [Mill ownership, capacity, and upstream dependency — load-bearing for mill-dependency falsifier framing.]"
  - ref: "Kaplan, Steven L. 1984. Provisioning Paris: Merchants and Millers in the Grain and Flour Trade during the Eighteenth Century. Cornell University Press. [French grain-and-bread supply chain; cooperative and guild baking structures.]"
  - ref: "Kaplan, Steven L. 2006. Good Bread Is Back: A Contemporary History of French Bread, the Way It Is Made, and the People Who Make It. Duke University Press. [French artisan baking cooperative and boulangerie forms; community bread supply models.]"
  - ref: "Ostrom, Elinor. 1990. Governing the Commons: The Evolution of Institutions for Collective Action. Cambridge University Press. [Eight design principles for commons governance; authoritative basis for cooperative governance structure.]"
  - ref: "Davis, James. 2004. Baking for the Common Good: A Reassessment of the Assize of Bread in Medieval England. Economic History Review 57(3): 465–502. [Communal baking regulation and shared-oven economics.]"
  - ref: "research/trades/baking/DECLINE-VERDICT.md. 2026. [Mill-dependency falsifier; local-mill-partnership as the directly addressed supply-chain path; niche targeting for community-bakery forms.]"
  - ref: "[CITATION-NEEDED: commercial electricity rate for commercial bakery operations — current U.S. average commercial rate; EIA or comparable energy agency source needed for variable_cost_per_unit energy component.]"
  - ref: "[CITATION-NEEDED: OSHA flour-dust permissible exposure limit (PEL) for commercial bakeries — 29 CFR 1910.1000 Table Z-1 or updated OSHA flour-dust standard; load-bearing for emissions and regulatory notes.]"
  - ref: "[CITATION-NEEDED: per-household food-access program costs in peer towns — needed for civic lens benchmark_comparison; municipal budget documents or USDA food-access program per-household data required before promotion.]"
  - ref: "[CITATION-NEEDED: cooperative grain-share bakery operating precedents — contemporary examples (e.g., grain CSA with baking access programs, cooperative flour-share bakery models in the U.S. or Europe) needed to ground capital-cost and operating-cost estimates; no direct historical precedent exists at this specific integration level.]"
---

## Summary

The Community Grain-Share Bakery (bake-003) is a cooperative-corporation bakery designed around a direct grain-supply-chain integration: member farms contribute grain to a contracted local mill, the mill delivers flour to the bakery coop, and members earn baking-session credits proportional to their grain contributions. It is not a market-facing business in the primary sense — its output flows to members, not retail customers — though surplus production may be sold locally. The design exists as a distinct catalog entry because it is the most direct test of the DECLINE-VERDICT mill-dependency falsifier: rather than treating commercial flour as a given input (the baseline for most other baking entries), bake-003 explicitly constructs the local-mill relationship that the falsifier identifies as the binding upstream constraint. If this model is viable, it demonstrates that the falsifier can be managed, not merely assumed away. It is designed for town-to-small-city scale where member density justifies the organizational overhead of coop governance, session booking, and grain-credit accounting, and where a local mill partner at viable delivery distance exists.

## Design rationale

Every other Group A entry in this catalog (bake-001, bake-002, bake-004, bake-005) treats commercial flour as a purchased input and focuses on oven economics and market positioning. This is historically supported — all four anchor cultures document that professional bakers were downstream of milling, not integrated with it. bake-003 is the single entry in the catalog that deliberately tests a different premise: what happens when a cooperative attempts to partially close the grain-to-loaf supply chain through a formal local-mill partnership and member grain-contribution program? The entry is not designed to demonstrate that mill-integration is superior to commercial-flour purchasing; it is designed to measure the cost, governance overhead, and supply-chain resilience gains of the integration path, and to determine whether the cooperative lens makes that path viable where the market lens would not. No other entry in this catalog directly tests this integration; removing bake-003 would leave the mill-dependency falsifier path documented but untested in the simulation matrix.

## Historical lineage

Three historical forms functionally inform this design. First, the medieval French *four banal* (communal oven) and its associated grain-sharing obligations: under the *banalité* system, peasant households brought grain to the seigneurial mill and baked in the communal oven under a regulated proportional access system [Kaplan 1984; Davis 2004]. The functional inheritance is the proportional-contribution model — access to shared baking infrastructure is linked to upstream resource contribution. The modern cooperative corporation replaces seigneurial obligation with voluntary membership and democratic governance, but the operational logic (contribute grain, receive baking access, receive bread) is structurally continuous. The labor regime and compulsion are not reproduced; the proportional-access architecture is.

Second, the French cooperative *boulangerie* form that survived the industrial period: while most of these were market-facing rather than member-consumption oriented, the cooperative ownership and shared-oven access model provides a direct precedent for a member-governed bread production facility [Kaplan 2006]. The functional inheritance is the cooperative-corporation structure and the democratic governance of shared equipment.

Third, the contemporary grain CSA (community-supported agriculture) model, which establishes the precedent for pre-commitment grain contributions in exchange for proportional agricultural output access [CITATION-NEEDED: grain CSA operating precedents]. The functional inheritance is the pre-commitment mechanism — members commit to the grain supply chain ahead of the baking season, providing the coop with advance flour-sourcing certainty. This partially resolves the single-source mill-dependency risk: member grain commitments create a demand-pull on the local mill that provides a more stable supply relationship than a purely spot-market arrangement.

The labor regime of the historical forms — seigneurial compulsion, guild-regulated journeymen, unpaid household labor — is not reproduced and is not relevant to the modern design. The modern design pays a professional cooperative manager at market wages; member labor is voluntary and not costed as production labor.

## Key assumptions

**Capital cost ($35,000–$95,000, mid $60,000):** The range reflects a wide variation in buildout condition. The low estimate assumes an existing commercial kitchen space requiring minimal structural modification with two single-deck electric ovens and basic member-station equipment. The mid estimate assumes a purpose-fitted 50 m² multi-station space with three double-deck electric ovens, proofing cabinets, and professional-grade mixing equipment. The high estimate reflects custom millwork, commercial hood and extraction system installation, and high-end deck oven specifications. These are order-of-magnitude estimates; no directly comparable cooperative grain-share bakery buildout data is available in the literature — a `[CITATION-NEEDED]` applies to any more precise claim. The install cost ($12,000) covers electrical service upgrade (dedicated 30-60A circuits per deck unit), ventilation extraction, and initial fit-out labor; this is a rough estimate consistent with commercial kitchen buildout norms for electric-primary equipment.

**Flour cost and grain-credit conversion:** The `variable_cost_per_unit` of $0.92/loaf uses a flour component of ~$0.62/loaf, reflecting a local-mill-partnership premium over commodity flour (~$0.40–$0.50/loaf for commodity bread flour). The premium is a rough estimate; the actual premium depends on the specific mill and grain type. Member grain contributions reduce effective flour cost for credited sessions, but the blended average is used here because not all sessions are credit-funded. The conversion rate between raw grain weight and flour credit is a coop governance decision, not a physical constant; it must be negotiated with the mill and set in operating bylaws.

**Operating days and throughput:** 260 operating days/year (5 days/week × 52 weeks) is the gross figure; the downtime fraction of 0.13 (13%) reduces effective production days to approximately 226. The 80 loaves/day figure assumes three active stations, each handling approximately 27 loaves/session, with modest output per station reflecting the variable skill of member operators. Professional artisan bakeries at comparable footprint regularly produce 150–250 loaves/day; the lower figure here reflects the coop's non-optimized, member-session format. `throughput_units_equiv_per_year` (18,000) is directly derived: 80 × 260 × 0.87 ≈ 18,096.

**Downtime fraction (0.13):** Higher than a private single-operator artisan bakery (typically 0.08–0.10) due to: member-session coordination overhead, batch losses from member skill variability, and seasonal participation trough. This figure is an informed estimate; no empirical data for cooperative grain-share bakeries is available in the corpus.

**Wage assumption ($52,000):** References corpus/program/SCALES.md §3 town-scale skilled-trades median for a journeyman baker with a cooperative-management component. This figure requires verification against the current SCALES.md value; a `[CITATION-NEEDED]` applies if the file has been updated since this entry was authored.

## Known risks / failure modes

**Regulatory:** The primary regulatory risk is the multi-user shared commercial kitchen classification. Most food safety jurisdictions classify a shared baking facility serving multiple operators as a commissary or shared-use kitchen, which triggers commercial kitchen inspection requirements, potentially more stringent than a single-operator bakery. Member operators may be individually required to hold food-handler certifications. In some jurisdictions, the grain-credit system (exchanging grain for baking access and bread) may be considered a commodity exchange or barter transaction with legal implications. The cooperative corporation form itself is well-established but requires state-level registration; operating as an informal group before registration is a liability risk. Legal counsel before launch is strongly recommended.

**Labour pipeline:** The cooperative manager role requires a journeyman baker who is also willing and able to manage a cooperative organization — a non-trivial combination of skills with a narrower hiring pool than a standard bakery manager role. If the founding manager departs, the coop must recruit a replacement from a small regional pool. The apprentice path is designed to build the internal pipeline; however, members who develop to Stage 3–4 capability are often the most likely to leave for independent baking ventures. The succession risk is real but partially mitigated by the coop's member-development culture; naming it explicitly is required by Principle 8.

**Supply chain:** The single greatest supply-chain risk is mill-partner dependency. If the local mill closes, changes ownership, raises prices unilaterally, or loses capacity, the coop's flour supply is disrupted and its grain-contribution program loses its delivery mechanism. Unlike commercial-flour-purchasing entries that can switch suppliers, bake-003's local-mill relationship is the core of its operating model — losing the mill partner disrupts not just flour supply but the membership value proposition. Mitigation requires either a backup commercial flour supply agreement (explicitly acknowledged as a fallback in coop bylaws) or relationships with multiple mills. A single-mill arrangement with no backup is the highest-risk configuration and should be documented as such in the governance framework. Grain contributions from member farms also carry upstream weather and harvest variability; in a poor harvest year, member contribution credits may be low, increasing the coop's reliance on purchased commercial flour.

**The mill-dependency falsifier, directly engaged:** bake-003 is explicitly designed as the test of this path. The Ostrom-governance structure, the proportional-contribution model, and the local-mill-partnership declaration together address the falsifier by naming the mill relationship and managing it through cooperative governance rather than assuming it away. Whether this management is sufficient for the coop to achieve financial sustainability is an empirical question; the Tier A simulation is the appropriate tool to assess it. The entry should not be read as claiming the falsifier is resolved — it claims only that this design directly confronts the falsifier rather than bypassing it.

## Iteration log

- 2026-04-18: v0.1 — initial creation. Plan G task 5. Cooperative-primary entry directly testing the DECLINE-VERDICT mill-dependency falsifier via local-mill-partnership and grain-contribution-credit model. Civic-marginal block included per schema requirement (lens_fit.civic: marginal). Key `[CITATION-NEEDED]` flags on commercial electricity rate, OSHA flour-dust PEL, peer-town civic benchmark, and cooperative grain-share operating precedents.
