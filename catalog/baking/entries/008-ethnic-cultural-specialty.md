---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: bake-008
trade: baking
name: "Ethnic / Cultural Specialty Bakery (community-serving, deck-oven baseline)"
tagline: "Baker from — or trained in — a specific bread tradition serves a diasporic or immigrant community whose baked staples are unavailable or unreliable from mainstream retail"
status: draft
version: "0.1"
supersedes: null
inspirations:
  - german-eastern-european-rye-bakery-tradition
  - ethiopian-injera-community-producer
  - south-asian-tandoor-naan-flatbread-production
  - mexican-pan-dulce-panaderia-tradition

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 32
# Mid-range of the 20-45 m² envelope specified for this entry. The actual
# footprint is tradition-dependent: injera production requires large flat
# griddles and staging space (lower bound ~20 m²); a German rye bakery with
# multi-loaf deck oven and proofing equipment sits comfortably at 28-35 m²;
# a panadería producing high-variety pan dulce may need 35-45 m² for shaping
# and cooling tables. 32 m² is the planning-level mid-range estimate. See Key
# Assumptions for tradition-specific footprint guidance.
# [Structural estimate; per entry parameter guidance 20-45 m² range; CITATION-NEEDED:
# commercial survey of ethnic specialty bakery floor areas by product type.]

ceiling_min_m: 2.7
# Electric deck oven stack (single or double deck) plus exhaust hood requires
# minimum 2.4-2.7 m clear ceiling; 2.7 m provides margin for hood installation
# and steam ventilation in flatbread operations where steam management is more
# critical. Tradition-specific equipment (tandoor pit, injera griddle) may have
# lower ceiling requirements but 2.7 m is a safe planning minimum.
# [Derived from commercial kitchen exhaust-hood installation standards; consistent
# with bake-001 ceiling requirement of 2.5 m; CITATION-NEEDED: code reference
# for commercial kitchen ceiling clearance with deck oven and exhaust hood.]

ventilation: kitchen-exhaust-hood-required
# Electric deck operation generates heat and steam requiring commercial exhaust
# hood. Tradition-specific variations: tandoor operations (if applicable) generate
# significant radiant heat and combustion products requiring dedicated exhaust;
# injera griddle produces steam at high rates requiring effective ventilation.
# The electric-deck baseline achieves near-zero combustion emissions; the primary
# ventilation driver is heat and steam management. Traditions that use wood-fired
# or gas-fired equipment require upgraded ventilation; such variants should be
# treated as separate entries with the appropriate energy_source value.

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: electric-deck
# Baseline energy source for this template entry. The electric deck oven is
# the most versatile commercial baking platform: it handles flatbreads (on a
# hot deck surface), enriched breads (temperature-controlled deck for pan dulce,
# challah, kulcha), and heavy loaves (rye, pumpernickel, injera-adjacent grain
# products). Tradition-specific alternatives exist and are noted in Design
# Rationale: Ethiopian injera is produced on a mitad (electric or gas flat
# griddle, not a deck oven); South Asian naan may be produced in a tandoor
# (gas or wood-fired cylindrical oven); authentic masonry-deck rye baking uses
# a deck-gas or wood-fired configuration. This entry uses the electric-deck
# baseline as the most flexible, cleanest-permit, and most commercially
# accessible starting point; operators whose tradition requires different
# equipment should treat this entry as a parametric template and adjust the
# energy_source accordingly.
energy_consumption_per_active_hour: "5.5 kWh"
# Per baking SCHEMA.md §2 electric-deck range of 3-8 kWh/batch. 5.5 kWh/active
# hour is consistent with a mid-range commercial electric deck oven (8-15 kW
# rated power) operating at sustained production temperature. Tradition-specific
# variation: an injera mitad (electric griddle, 3-6 kW per unit) running 2 units
# concurrently would be comparable; a tandoor (gas-fired, ~15-25 MJ/hr) would
# require a different energy_source entry.
# [Baking SCHEMA.md §2 electric-deck 3-8 kWh/batch; CITATION-NEEDED: manufacturer
# energy data for 8-15 kW commercial electric deck oven sustained operation; label: inferred.]

backup_fuel: null
# No backup fuel in the electric-deck baseline. Grid reliability is a noted risk
# (see Known Risks). A propane combi oven as backup would raise capital cost by
# ~$4,000-$8,000 and is a variant design consideration for operators in areas
# with grid instability.

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  loaves_per_day: 100
  # Net production output per full operating day. Unit: loaf-equivalent (see Key
  # Assumptions for unit definition — this entry uses a "community serving unit"
  # that varies by tradition; see below). 100 units/day is the mid-range planning
  # estimate for a full-time single-operator ethnic specialty bakery at town scale.
  # Tradition-specific ranges:
  #   German/Eastern European rye: 60-120 loaves/day (dense loaves, longer bake
  #     time; single-deck oven; 2-3 batches; unit = 750g rye loaf)
  #   Ethiopian injera: 80-200 flatbreads/day (fast griddle production; high unit
  #     count but lower equivalent mass; unit = 40cm injera round)
  #   South Asian naan/flatbread: 150-400 pieces/day (very fast production with
  #     tandoor or deck; unit = standard naan piece, ~150g)
  #   Mexican pan dulce: 80-200 pieces/day (mixed-shape; high labor per unit;
  #     unit = individual pastry/roll equivalent)
  # Per entry parameters: 100 units/day is used for the planning template;
  # tradition-specific implementations must restate the unit explicitly.
  # [Baking SCHEMA.md §1 loaves/day ranges; CITATION-NEEDED: empirical throughput
  # data for ethnic specialty bakeries by product type; label: inferred.]

  batches_per_day: 3
  # Three oven or griddle loads per operating day at moderate production scale.
  # Dense rye loaves may require 2 batches (longer bake time: 45-75 min/batch);
  # flatbread and enriched pastry may support 3-5 shorter batches. 3 batches/day
  # is the mid-range estimate for the electric-deck baseline.

  batch_size_loaves: 14
  # Mid-range for a standard commercial electric deck oven (0.5-0.9 m² deck area).
  # Dense rye loaves: 8-12/batch; flatbread equivalents: 18-30/batch depending
  # on size; pan dulce: 15-24 pieces/batch depending on size.
  # [CITATION-NEEDED: deck oven capacity per m² of deck area by product type;
  # commercial deck oven manufacturer specifications; label: inferred.]

  max_active_hours_per_week: 40
  # Gross weekly operator hours including prep, mixing, shaping, proofing (where
  # applicable), baking, cooling, packaging, and customer service. 40 hr/wk
  # represents a full-time single-operator operation at town scale. Some cultural
  # specialty items (injera batter fermentation: 24-72 hr standing ferment;
  # sourdough rye: overnight retard) add passive fermentation time that is not
  # included in active operator hours. See max_active_hours_realism_note.

  product_mix:
    bread: 30
    # Enriched and lean bread products that form the bakery's staple line.
    # For rye/pumpernickel bakeries: 80-90% of production. For injera producers:
    # 90-100% (injera is the staple). For pan dulce: 20-30% (the balance of
    # the product_mix.confection share). This default 30% reflects a mixed
    # specialty/staple bakery; tradition-specific variants will shift this ratio.
    confection: 30
    # Confection share: high for pan dulce panaderías (50-70%), zero or near-zero
    # for injera or rye-specialist bakeries. 30% default for a mixed operation.
    specialty: 40
    # Cultural specialty items specific to the tradition being served: specific
    # fermented grain preparations, holiday breads, ceremonial pastry, high-
    # complexity enriched doughs. This is the core differentiating production
    # category for ethnic specialty bakeries and the primary source of the premium
    # over industrial equivalents.
    catering: 0
    # No catering in the base configuration; direct retail and community sales
    # channel assumed. Catering (event bread, ceremony orders) is a natural
    # extension for this bakery type but adds scheduling complexity.
    # Sum: 100.

  throughput_variance:
    seasonal: "Holiday and religious-calendar peaks dominate (e.g., Ethiopian Christmas/Epiphany, German Christmas stollen season, Eid al-Fitr for South Asian bread, Día de los Muertos for pan dulce); summer trough moderate to mild since community-staple demand is less seasonally elastic than premium artisan retail"
    worst_month_fraction_of_average: 0.70
    # Community-staple demand is more stable than premium-artisan demand: a
    # diasporic community buying its weekly bread from this bakery does not
    # strongly reduce purchases in summer. The 0.70 floor reflects a mild
    # seasonal trough rather than the sharper drops seen in luxury confection
    # or artisan-only bread entries. Per baking SCHEMA.md §1 artisan bread
    # range 0.55-0.75; 0.70 is the upper end of that range (less volatile).
    # [Baking SCHEMA.md §1 throughput_variance; CITATION-NEEDED: empirical
    # seasonal demand data for ethnic specialty bakeries; label: inferred.]
    best_month_fraction_of_average: 1.45
    # Religious and cultural calendar peaks can be sharper than artisan-bread
    # peaks: a community ordering Christmas stollen, Eid sweets, or Día de los
    # Muertos pan de muerto en masse produces concentrated demand spikes.
    # 1.45 reflects a moderate peak consistent with a small-to-mid-size
    # diasporic community with concentrated holiday demand.
    # [Structural inference from cultural calendar demand patterns; CITATION-NEEDED.]

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: journeyman-baker
# Base skill floor for the template pattern. Per baking SCHEMA.md §3: journeyman-
# baker can manage full production cycles, run a deck oven without supervision,
# and execute standard enriched doughs independently. This is sufficient for
# rye and pumpernickel, standard flatbread, and most pan dulce production.
# Tradition-specific elevation: complex enriched doughs requiring multi-lamination
# (some Central Asian and Eastern European festive breads) require master-level
# skill. Injera production (24-72 hr teff fermentation management) requires
# specific fermentation judgment that maps to journeyman-baker capability applied
# to a non-wheat grain substrate. Pan dulce with complex pastry shapes requires
# at minimum journeyman-baker shaping skill.
# This template entry does not require pastry-chef-master skill floor because
# the primary value proposition is reliable staple and specialty production for
# a community, not competition-level pastry craft.
# [Baking SCHEMA.md §3 journeyman-baker definition]

operators_concurrent: "1-2"
# Single operator is the base; a part-time second operator or apprentice during
# peak production windows (holiday calendar spikes, community-event catering)
# is common and improves throughput without requiring full-time second hire.

apprentice_friendly: true
apprentice_path:
  training_stages: >
    Stage 1 (0-3 months): bakery safety, sanitation, equipment operation (mixer,
    deck oven, proofer, specialty equipment relevant to the tradition). Gate
    criterion: operates and cleans all equipment unassisted; understands the
    specific grain(s), leavening agent(s), and fermentation approach of the
    tradition being learned (teff fermentation for injera, rye sourdough for
    pumpernickel, yeasted enriched dough for pan dulce, etc.).
    Stage 2 (3-12 months): production assistance — mixing, shaping, baking under
    supervision. Gate criterion: produces 10 consecutive on-standard units of
    the bakery's core staple product without guidance on the final three; can
    state the fermentation protocol from memory and adjust for ambient temperature.
    Stage 3 (12-30 months): independent production of the core staple line; learns
    the holiday and specialty items specific to the tradition's calendar. Gate
    criterion: operates a full production day independently with journeyman review
    of output at end of day for five consecutive days; successfully executes at
    least two seasonal specialty items (e.g., injera for a specific feast, stollen,
    pan de muerto, Eid sweets).
    Stage 4 (30-48 months): full independence on the complete product range;
    community relationship management (understanding which community members
    order what, and why); tradition-specific troubleshooting. Approximate
    journeyman standard for this type of bakery.
  time_to_independent_operation: "~36-48 months to journeyman-baker standard on the tradition-specific product range; grain and fermentation diversity means the rate-limiting step is tradition-specific knowledge accumulation, not generic baking skill"
  succession_note: >
    The apprentice serves as a production assistant from Stage 2 onward,
    integrating skill transfer into daily operations without a separate training
    program overhead. The tradition-specific knowledge embedded in this bakery
    is the primary institutional asset: recipes, community relationships, and
    cultural calendar awareness. Succession planning requires that the apprentice
    has direct contact with the community the bakery serves — not merely technical
    baking instruction — because the demand signal is community-specific. An
    apprentice drawn from the diasporic community itself carries this cultural
    capital by default; an apprentice recruited from outside the community must
    acquire it through direct community engagement over the apprentice period.

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD

  capital_cost: { low: 18000, mid: 38000, high: 65000 }
  # Low: secondhand commercial electric deck oven ($8,000-$12,000), basic mixer
  # ($2,500), minimal proofing setup ($1,500), tradition-specific equipment
  # (mitad/griddle, specialty molds, etc.: $1,000-$2,000), initial smallwares.
  # Minimal commercial kitchen fitout; total ~$18,000 for a stripped-down viable
  # setup.
  # Mid: mid-range commercial electric deck oven ($14,000-$18,000 new), commercial
  # spiral mixer ($4,000), proofer with humidity control ($4,500), tradition-
  # specific specialty equipment at full commercial spec ($2,000-$4,000 depending
  # on tradition), full smallwares, point-of-sale setup, community signage.
  # Total ~$38,000 for a full-function commercial setup.
  # High: premium multi-deck commercial oven ($22,000-$28,000), heavy-duty mixer,
  # full proofing cabinet, walk-in proofer upgrade, complete tradition-specific
  # equipment set (e.g., full tandoor installation including masonry: $6,000-
  # $12,000; or multiple injera mitads at commercial spec), full commercial
  # kitchen fitout and exhaust hood upgrade. Total ~$65,000.
  # [CITATION-NEEDED: commercial electric deck oven pricing 2024-2026; tradition-
  # specific equipment costs (mitad, tandoor, panadería molds, rye baking forms);
  # label: inferred from bake-001 comparable capital ranges adjusted upward for
  # tradition-specific equipment overhead.]

  install_cost: 5000
  # Electrical service upgrade (30-60A dedicated circuit per deck unit), exhaust
  # hood installation and ductwork, health department commercial kitchen
  # certification, tradition-specific modifications (e.g., tandoor masonry,
  # griddle mount, injera ventilation). Range varies significantly by tradition
  # ($2,500 for standard electric-deck fitout to $8,000+ for tandoor installation
  # or specialized ventilation); $5,000 is the mid-range planning estimate.
  # [CITATION-NEEDED: commercial kitchen installation cost data including
  # tradition-specific equipment; general commercial kitchen contractor estimates;
  # label: inferred.]

  annual_maintenance: 1400
  # Deck oven element inspection and cleaning, mixer bowl and hook inspection,
  # proofer calibration, exhaust hood cleaning (quarterly health-code requirement),
  # tradition-specific equipment service (griddle surface, tandoor refractory,
  # etc.). Mid-range estimate; higher for traditions using combustion equipment.
  # [CITATION-NEEDED: annual maintenance cost data for commercial ethnic specialty
  # bakery operations; label: inferred from bake-001 maintenance baseline adjusted
  # upward for tradition-specific equipment.]

  annual_consumables: 9500
  # Flour and grain inputs dominate (~$6,000-$7,000/yr for 100 units/day × 280
  # days × ~0.6 kg grain/unit × $0.35-$0.55/kg specialty or commodity grain).
  # Tradition-specific variation is significant:
  #   Teff flour (injera): $1.50-$4.00/kg specialty import [CITATION-NEEDED];
  #     annual flour cost can be 3-5× higher than commodity wheat for same volume.
  #   Rye flour (dark rye/pumpernickel): $0.50-$1.20/kg depending on source;
  #     moderate premium over commodity wheat.
  #   All-purpose wheat (naan, pan dulce): $0.45-$0.70/kg commodity.
  # Enrichment ingredients (eggs, butter, sugar, lard, seeds, spices, chocolate
  # for confection-heavy traditions): $1,500-$2,000/yr at 100 units/day.
  # Packaging materials: $1,000-$1,500/yr (specialty cultural packaging for
  # holiday items may be a meaningful cost item).
  # The $9,500 estimate applies to a mixed-tradition bakery at commodity-to-
  # moderate specialty grain cost. A teff-primary injera operation would see
  # annual grain costs 2-3× higher and should recalculate consumables accordingly.
  # [CITATION-NEEDED: specialty grain pricing per kg for teff, dark rye, atta/maida,
  # masa harina, and equivalent specialty grains at US wholesale, 2024-2026;
  # commodity pricing from USDA ERS; specialty pricing from ethnic food distributors;
  # label: inferred.]

  floor_space_rent_per_year: 3840
  # Imputed at ~$120/m² per year for commercial kitchen or light-commercial space;
  # 32 m² × $120/m²/yr = $3,840. Same rate basis as bake-001; tradition-specific
  # bakeries often co-locate in immigrant-community commercial districts where
  # commercial rents may be below this estimate. Owner-operated space is common
  # for first-generation immigrant bakery operators; imputed at market rate for
  # consistent cross-entry comparison per catalog/SCHEMA.md §6.
  # [CITATION-NEEDED: commercial kitchen or light-commercial rental rates in
  # immigrant-community commercial districts; CoStar or local broker data, 2024;
  # imputed rate consistent with bake-001 basis; label: inferred.]

  market_price_per_unit: { low: 3, mid: 6, high: 12 }
  # Per community-serving unit equivalent (tradition-specific; see Key Assumptions).
  # Low ($3): commodity-competitive pricing for staple items in a cost-sensitive
  # diasporic community where the primary purchase motivation is product access,
  # not premium; e.g., basic injera at community price, standard rye loaf at
  # below-artisan pricing.
  # Mid ($6): standard community-market pricing for specialty cultural items that
  # are unavailable from mainstream retail; e.g., decorated pan dulce, specialty
  # rye loaf, naan at community bakery price.
  # High ($12): premium cultural specialty items for holiday or ceremonial purchase;
  # e.g., stollen, pan de muerto, Eid sweets, injera for feast events.
  # The price range reflects that this bakery sells to a community-defined market:
  # prices are set by community willingness-to-pay and the absence of mainstream
  # alternatives, not by competing artisan-bread premiums.
  # Industrial baseline: $2 (packaged mass-produced equivalent — frozen naan,
  # commercial pita, commercial rye bread at a major US grocery chain; see
  # industrial_baseline_price below).
  # [CITATION-NEEDED: pricing survey of ethnic specialty bakeries and community
  # food retailers by product type and community segment; USDA AMS or equivalent
  # survey; label: inferred from market observation.]

  pricing_notes: >
    Unit is a tradition-specific "community serving unit" — a rye loaf (750g),
    injera round (40cm), naan piece (~150g), or pan dulce individual item —
    defined in Key Assumptions per the specific tradition. Industrial baseline
    is $2/unit (packaged commercial equivalent: frozen naan at ~$0.50-$1.00/piece
    [CITATION-NEEDED: major US grocery chain frozen naan pricing], commercial
    rye bread at ~$3-$4/loaf ÷ ~2 serving-equivalents per loaf, commercial
    pita at ~$0.40-$0.60/piece). The artisan-community premium (3-6× industrial
    baseline at mid pricing) reflects: (1) product authenticity — a mass-produced
    frozen naan is not a functional substitute for fresh bakery naan for a South
    Asian household purchasing for family use; (2) product availability — the
    community may have no other access to fresh injera, stollen, or pan dulce of
    cultural standard outside this bakery; (3) community relationship — a known
    bakery operator from or trained in the tradition commands loyalty pricing from
    repeat community customers. The customer segment is not the premium artisan-
    bread consumer segment; it is the diasporic or immigrant community that has
    existing demand for specific baked goods and no convenient mainstream alternative.

  pricing_validation: >
    Pricing evidence: inferred from observation of ethnic specialty bakery pricing
    at US community markets, ethnic grocery stores, and bakery websites, circa
    2024-2026. No single published pricing survey for ethnic specialty bakeries
    across all traditions has been identified. Tradition-specific evidence should
    be sought separately: USDA AMS farmers-market pricing surveys, immigrant
    community business surveys, ethnic chamber-of-commerce trade data, or direct
    survey of operating ethnic specialty bakeries in comparable markets. This is
    a placeholder-inferred figure. Evidence type: structural inference from
    observed pricing and community-need argument; not a cost-plus residual.
    Verification required before promotion to reviewed.

  industrial_baseline_price: 2
  # Nearest industrial equivalent: packaged mass-produced equivalent of the
  # tradition-specific staple item available at major US grocery chains.
  # Examples: frozen naan ($0.50-$1.00/piece), commercial sliced rye bread
  # ($0.75-$1.00/serving equivalent), commercial pita ($0.40-$0.60/piece),
  # commercially-produced pan dulce from a large Mexican bakery chain (~$1.50-
  # $3.00/piece). $2.00 is the blended mid-range estimate across tradition types.
  # The industrial baseline is materially lower than the community-bakery price
  # primarily because: (1) industrial equivalents are often frozen or shelf-
  # stabilized and perceived as categorically different from fresh bakery products;
  # (2) the industrial equivalent may not match the specific cultural product
  # required (e.g., industrial rye bread in the US is often only superficially
  # similar to dense German pumpernickel; commercial injera is rare outside
  # Ethiopian-community retail).
  # [CITATION-NEEDED: US grocery chain shelf pricing for packaged ethnic bread
  # and flatbread equivalents by product type, 2024; label: inferred.]

# ── TRADE-SPECIFIC FIELDS ────────────────────────────────────────────────────

trade_specific:
  flour_source_declaration: industrial-flour-purchased
  # Per baking SCHEMA.md §4 (required field). Base declaration for the template.
  # This bakery purchases specialty or commodity flour/grain from an industrial
  # mill, ethnic food distributor, or regional specialty supplier. No mill
  # infrastructure is owned or operated. The specific grain input varies by
  # tradition: teff from an Ethiopian-community importer, dark rye from a
  # specialty grain distributor, atta or maida flour from a South Asian food
  # distributor, masa harina from a Mexican foods distributor, etc.
  # Supply-chain risk: specialty grain imports are more exposed to supply
  # disruption and price volatility than commodity wheat. A teff importer
  # failure or tariff change affects injera producers directly; dark rye
  # availability is limited to fewer distributors than commodity bread flour.
  # See Known Risks for tradition-specific supply chain assessment.
  # Authors of tradition-specific implementations should declare the specific
  # grain and supplier type in Key Assumptions.

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:
  first_year_failures:
    - item: "Deck heating element (electric)"
      estimated_hours_to_failure: 2000
      replacement_cost: 600
      replacement_lead_time_days: 14
      serviceable_by: specialist
      # Electric deck heating elements degrade under repeated thermal cycling.
      # Per baking SCHEMA.md §5: 1,500-3,000 hr typical range. At 5 active
      # oven-hours/day × 280 operating days = 1,400 hr/yr, first element failure
      # is expected within year one or early year two. Specialist required;
      # factory-ordered element; 14-day lead time.
      # [Baking SCHEMA.md §5 reference; CITATION-NEEDED: commercial electric
      # deck oven element MTBF; label: inferred.]

    - item: "Oven thermostat / temperature controller"
      estimated_hours_to_failure: 3000
      replacement_cost: 350
      replacement_lead_time_days: 10
      serviceable_by: journeyman
      # Thermostat drift is the most common non-structural failure in deck ovens
      # per baking SCHEMA.md §5: 2,000-4,000 hr typical. At 1,400 hr/yr,
      # first thermostat failure is likely in year two but possible in year one
      # for a heavily-cycled deck. Journeyman-serviceable on most commercial
      # ovens; 10-day regional supply lead time for replacement controller.
      # [Baking SCHEMA.md §5; CITATION-NEEDED: label: inferred.]

    - item: "Tradition-specific specialty equipment (griddle surface, mold set, or injector — tradition-dependent)"
      estimated_hours_to_failure: 1500
      replacement_cost: 400
      replacement_lead_time_days: 21
      serviceable_by: journeyman
      # The specialty equipment used by ethnic bakeries carries higher first-year
      # failure risk than standard commercial baking equipment because (a) it is
      # more likely to be sourced from ethnic importers with less standardized
      # replacement part supply chains, and (b) operators may be adapting
      # consumer-grade or import equipment to commercial-use cycles. A mitad
      # electric griddle sourced from an Ethiopian import supplier; a tandoor
      # refractory lining; a panadería mold set made from thin-gauge aluminum —
      # all face early-use failure modes at commercial intensity. 21-day lead
      # time reflects potential overseas supplier lead time for specialty items.
      # [Structural inference from ethnic food equipment import supply patterns;
      # CITATION-NEEDED: empirical failure data for ethnic specialty baking
      # equipment at commercial use intensity; label: inferred.]

  maintenance_schedule:
    daily:
      task: "Clean deck oven interior and door seals; clean mixer bowl, hook, and work surfaces; clean/wipe specialty equipment (griddle, molds); feed/check leavening cultures (sourdough starter, teff batter, etc.) as applicable to tradition; log batch yields and fermentation timing"
      performed_by: operator
    weekly:
      task: "Deep-clean deck oven (deck surface, door, gasket seals); calibrate proofer temperature and humidity; inspect mixer motor base; clean exhaust hood filter; inspect tradition-specific equipment for wear or surface damage; reconcile flour and ingredient inventory"
      performed_by: operator
    quarterly:
      task: "Professional exhaust hood cleaning and grease trap service (health code); deck oven element and thermostat inspection; proofer full calibration; mixer motor inspection and lubrication; tradition-specific equipment full inspection (griddle surface condition, mold integrity, refractory inspection if applicable)"
      performed_by: journeyman
    annual:
      task: "Full deck oven professional service (element test, seal replacement, thermostat calibration); health department commercial kitchen re-inspection; proofing cabinet professional service; mixer motor overhaul assessment; tradition-specific equipment replacement evaluation (mitad surface, mold set replacement if worn)"
      performed_by: specialist

  startup_shutdown_overhead_per_day_min: 55
  # Overhead includes: (1) oven preheat — electric deck requires 30-45 min from
  # cold to operating temperature; (2) leavening culture check and feeding where
  # applicable (10 min for sourdough or teff batter); (3) end-of-day cleanup of
  # specialty equipment and production logging (15 min). Total: ~50-60 min/day;
  # 55 min used as mid-range. Cultural specialty items with longer passive
  # fermentation (injera batter: 24-72 hr standing time; rye sourdough: overnight
  # cold retard) carry additional passive time not counted in operator active hours.
  # [Structural inference from commercial deck oven preheat times and ethnic
  # specialty baking preparation protocols; CITATION-NEEDED; label: inferred.]

  max_active_hours_realism_note: >
    40 hr/wk is the gross ceiling including startup, shutdown, and culture
    maintenance overhead. Derating applied: 55 min/day overhead × 5 operating
    days/wk = 4.6 hr/wk non-productive overhead, leaving approximately 35.4
    hr/wk net active production time. sim_params.throughput_units_equiv_per_year
    uses a loaves_per_day figure (100 units/day) derived from oven-constrained
    output, not a linear function of active hours; this figure is consistent
    with the net 35.4 hr/wk active window across 280 operating days/yr.

  interruption_notes: >
    Community retail bakeries serving diasporic communities experience a distinct
    interruption pattern: the bakery often functions as a community social anchor,
    with regular customers staying to talk, community members placing custom
    orders verbally, and cultural calendar inquiries consuming operator time.
    This is qualitatively different from a farmers-market or DTC subscription
    bakery; the community relationship is a revenue asset (loyalty, repeat
    purchase, premium holiday ordering) but it consumes operator time beyond
    what a purely production-focused bakery would budget. Estimated 30-60 min/day
    of community-interaction overhead beyond the startup_shutdown_overhead is
    folded into throughput_units_equiv_per_year via the loaves/day figure.

  consumables_lead_time_days: { typical: 7, worst: 45 }
  # Typical: specialty grain orders from ethnic food distributors (teff, dark
  # rye, atta flour, masa harina) require 5-10 days in markets with adequate
  # ethnic food distribution coverage; 7 days used as mid-range.
  # Worst: specialty grain from overseas suppliers or small regional importers
  # can reach 30-60 days in supply-chain stress or importer stock-out; 45 days
  # reflects realistic worst-case for a tradition-specific grain with few US
  # domestic distributors (e.g., teff from Ethiopian importers; specialty
  # Turkish or Central Asian grains). This is the primary supply-chain
  # differentiation from commodity-wheat bakeries (bake-001 worst: 21 days).
  # [Structural inference from ethnic food import distribution patterns;
  # CITATION-NEEDED: empirical lead-time data for specialty ethnic grain
  # distributors in US markets; label: inferred.]

  throughput_variance:
    seasonal: "Cultural and religious calendar peaks dominate (tradition-specific); community-staple demand is moderately stable year-round with concentrated holiday spikes; summer trough is mild compared with premium artisan-bread entries"
    worst_month_fraction_of_average: 0.70
    best_month_fraction_of_average: 1.45

  operator_impact:
    noise_db: 62
    # Electric deck oven and mixer produce moderate ambient sound. Spiral mixer
    # during dough mixing: ~65-70 dB(A) intermittently. Ambient bakery environment
    # during normal production: 55-65 dB(A); 62 dB(A) average. Well below OSHA
    # 90 dB(A) PEL. Slightly higher than bake-001 estimate due to potential
    # additional equipment (griddle, mixer, exhaust fan for steam-intensive
    # production such as injera). [CITATION-NEEDED: sound level measurement at
    # operator position in ethnic specialty commercial bakery; label: inferred.
    # OSHA 29 CFR 1910.95.]
    heat_exposure: "Elevated ambient temperature near deck oven during baking cycles (deck surface 230-260°C; ambient near oven 28-35°C); injera production on open electric griddle increases localized radiant heat exposure above standard deck-oven level; adequate with commercial exhaust hood; operator rotation between baking and prep zones reduces sustained heat exposure"
    emissions: "Near-zero combustion emissions from electric-deck baseline; steam (especially during injera griddle operation and enriched dough baking) is primary emissions driver and is managed by kitchen exhaust hood; flour dust from specialty grains (teff, rye, atta) requires dust mask during extended mixing; no combustion particulate"
    physical_demand: "Moderate; sustained standing; repetitive dough shaping and forming tasks; tradition-specific physical demands include injera batter pouring (repetitive fine-motor task), large-volume dough dividing for pan dulce shapes, and heavy rye dough handling (dense dough requires higher effort per unit than wheat dough); 8-15 kg batch lifting; ergonomic anti-fatigue mats and proper oven tools recommended"

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Commercial kitchen or light-commercial zoning required; immigrant-community commercial districts often in mixed-use or commercial corridor zoning that accommodates food production; verify specific jurisdiction for bakery production vs. retail classification; home-kitchen cottage-food laws do not cover commercial-volume production"
  emissions: "No combustion emissions permit required for electric-deck baseline; kitchen exhaust hood requires local building permit and inspection; specialty grain flour dust (teff, rye flour) governed by OSHA 29 CFR 1910.1000 Table Z-1 flour-dust PEL; traditions using gas or wood-fired equipment require combustion emissions permit review"
  other: "Commercial food handler certification required; health department commercial kitchen inspection and licensing required; tradition-specific food safety considerations may apply (teff batter fermentation: pH and contamination control per FDA Food Safety Modernization Act; injera: gluten-free cross-contamination risk if serving celiac customers); halal or kosher certification may be a community requirement for some traditions and should be budgeted as a licensing cost"

# ── CONTEXT FIT ──────────────────────────────────────────────────────────────

lens_fit:
  market: good
  cooperative: marginal
  civic: marginal

scale_fit:
  village: poor
  town: good
  small_city: good

# ── LENS CONTEXT ─────────────────────────────────────────────────────────────

lens_context:
  cooperative:
    membership_boundary: >
      Members of the ethnic or cultural community served, defined by cultural
      self-identification and demonstrated community connection rather than
      geographic boundary alone. A cooperative producing Ethiopian injera, German
      rye bread, or South Asian naan may draw members from a broader metro area
      than a neighborhood bakery (diasporic communities are often geographically
      dispersed at town scale). Practical boundary: community members who use the
      bakery as their primary source for the tradition's staple bread products.
      Cultural competence is a functional membership requirement: members must
      understand the product tradition they are managing collectively.
    rules_source: >
      Bylaws or operating agreement adopted at founding by founding community
      members; member vote required to amend any production, pricing, or
      distribution provision; annual meeting reviews product mix, community
      demand, and dues schedule. Cultural authority over recipes and tradition-
      specific production methods should be explicitly vested in a named tradition-
      keeper role (elected or designated) to prevent rule-amendment drift away
      from cultural standards.
    monitoring: >
      Production volume and product mix logged per operating day; weekly sales
      reconciliation; monthly report to elected member committee; tradition-keeper
      oversight of product quality against community standard; health-department
      compliance log available to all members; specialty grain inventory monitored
      weekly due to longer lead times (see consumables_lead_time_days).
    graduated_sanctions: >
      Production deviation (product not meeting community quality standard):
      journeyman-review and documented correction protocol.
      Rules violation (booking overage, unauthorized product substitution):
      written warning and correction within 7 days.
      Second violation within 12 months: $75 fine and 30-day production-access
      suspension with mandatory re-training on affected protocol.
      Third violation within 24 months: membership review by elected member
      committee; possible termination with dues refund pro-rated.
      Per Ostrom Principle 5.
    conflict_resolution: >
      First-level disputes (scheduling conflicts, product quality disagreements,
      cultural standard interpretation): tradition-keeper role mediates with
      appeal to elected member committee. Second-level disputes: full membership
      vote at next scheduled meeting. Disputes that cannot be resolved internally
      are referred to the cooperative's legal operating agreement dispute-resolution
      provisions. Cultural standard disputes are referred to community elders or
      a named cultural authority body if one exists in the served community.
      Per Ostrom Principle 6.
    ostrom_principles_addressed: [1, 2, 3, 4, 5, 6]
    # Principle 1 (defined boundaries): cultural-community membership boundary above.
    # Principle 2 (rules fit local conditions): production rules calibrated to
    # the specific community's cultural standards and demand patterns.
    # Principle 3 (collective choice): member vote to amend operating agreement.
    # Principle 4 (monitoring): production logging, quality oversight, inventory.
    # Principle 5 (graduated sanctions): above.
    # Principle 6 (conflict resolution): above.
    # Principle 7 (external recognition): addressed via legal_form below.
    # Principle 8 (nested governance): not applicable at single-cooperative scale.
    member_amendment_process: >
      2/3 vote of all members at scheduled annual meeting with 30-day notice;
      emergency amendment (3/4 vote) with 7-day notice for health-code compliance,
      safety, or supplier-emergency situations only. Amendments to cultural
      production standards require affirmative recommendation from the tradition-
      keeper role before the general membership vote; this protects cultural
      integrity from drift by a majority of members who may be less
      tradition-knowledgeable than the original founding cohort.
    legal_form: >
      Multi-member LLC or state-registered worker cooperative (most accessible
      for immigrant community operators in US jurisdictions); alternatively, a
      community benefit corporation (CBC) or nonprofit where the cultural-preservation
      mission warrants it. LLC provides liability protection and external recognition
      (Ostrom Principle 7 analog) without cooperative-incorporation overhead.
      Some immigrant communities may benefit from a nonprofit structure if
      charitable food-access functions are combined with bakery operations.
      Specific jurisdiction filing required before launch.
    scale_fit_note: >
      Cooperative form is marginal for this entry at town scale: the coordination
      overhead of a multi-member cooperative producing tradition-specific cultural
      goods adds complexity beyond standard shared-equipment cooperatives. The
      primary cooperative value here is shared community ownership of a culturally-
      significant production facility, not primarily capital-cost reduction. At
      village scale (500-2,000 residents), the diasporic or immigrant community
      may be too small to support a viable cooperative membership base; town
      scale (2,000-15,000) is the minimum for a cooperative that can sustain
      3+ active members with sufficient community demand.

  civic:
    political_coalition: >
      Municipal cultural-heritage or immigrant-services grant programs + diaspora
      community association advocates + small-business development center allies.
      The cultural-heritage argument for civic investment in this type of bakery
      is real but narrow: civic investment is justified primarily on food-access
      grounds (a community that cannot obtain its staple baked goods locally is
      experiencing a food-access gap) rather than on aesthetic or heritage-
      preservation grounds alone. Political support depends on the size and
      political organization of the served community.
    council_vote_estimate: >
      3-4 favorable, 2-3 uncertain; likely to pass in towns with visible and
      organized immigrant or diasporic communities; likely to fail in towns where
      the served community is small or politically unorganized. Primary opposition
      argument: subsidy should not favor one cultural group over others, and the
      market should serve this demand if it exists. Counter-argument: the market
      has failed to serve this demand (no existing bakery), which is why civic
      investment is being considered.
    competes_with_private: >
      Civic investment is only appropriate when no viable private operator exists
      or is willing to enter the market. If a private ethnic specialty bakery is
      already serving the community, a civic facility would directly displace it
      and is not appropriate under this entry's lens_fit rationale. The civic form
      applies specifically to the gap case: a community with documented unmet
      demand and no functioning private operator. This must be verified before
      pursuing civic investment.
    governance_form: >
      Municipally funded but community-operated: capital grant or subsidized lease
      from the municipality, with day-to-day operations managed by a community
      nonprofit or cultural association. Full municipal operation of an ethnic
      specialty bakery is neither efficient nor culturally appropriate — the
      production skill and community knowledge are not transferable to generic
      municipal staffing. The appropriate civic form is a capital grant or
      subsidized space that enables community-driven operation, not a municipally-
      staffed facility.
    budget_line: >
      Capital grant via cultural-heritage, food-access, or small-business
      development municipal budget lines; operating costs covered by community
      operator (the civic contribution is the capital or lease subsidy, not
      ongoing operating subsidy). An ongoing operating subsidy creates dependency
      that undermines the economic viability of the community operator.
    benchmark_comparison: >
      Capital-grant cost per household: a $38,000 capital grant (mid-case capital
      cost) amortized over 15 years in a town of 5,000 households = $0.51/
      household/year — well below the $42/hh/yr town library benchmark or
      $15/hh/yr community center program comparison. Even a $65,000 capital grant
      = $0.87/hh/yr amortized. The case for civic investment on per-household
      cost grounds is strong if the community benefit is accepted; the primary
      political objection is cultural-specificity (who benefits), not per-
      household cost. [Benchmark: peer-town library cost $42/hh/yr from forge-003
      example; CITATION-NEEDED for local library or community center cost data;
      label: structural calculation from capital_cost.mid and assumed town population.]
    staffing_model:
      role: "community operator (cultural association or cooperative, contracted baker)"
      operator_fte: 1.0
      wage_assumption: 42000
      # At-or-below median wage for food-service and baking trades; appropriate
      # for a community-operator model where the operator is a community member
      # who draws non-monetary value from the cultural and community role.
      # Market-wage baker at journeyman level would be $45,000-$55,000; the
      # community-operator assumption of $42,000 reflects the below-market wage
      # that community operators often accept in exchange for cultural mission
      # alignment. This should be flagged as a subsidy risk if the operator
      # cannot sustain this wage from bakery revenue.
      wage_source: "corpus/program/SCALES.md §3 town-scale food-service and skilled-trades median; community-operator assumption below full skilled-trades median per cultural-mission context"
      hours: "40 hrs/wk production + community engagement + administration"
      hiring_notes: >
        Hiring pool is the diasporic or immigrant community itself: the operator
        must have both the technical baking skill and the cultural-tradition
        knowledge for the specific bread tradition. This dramatically narrows the
        hiring pool compared with a general artisan baker position. In towns with
        small diasporic communities, finding a qualified community-operator may
        be the binding constraint. At small-city scale, the community is large
        enough to provide a credible hiring pool. An apprentice pipeline that
        recruits from the community is the primary succession mechanism.
    civic_externalities:
      - "Food access: provides staple baked goods to a diasporic or immigrant community that has no mainstream retail alternative; addresses a specific food-access gap that the market has failed to fill"
      - "Cultural transmission: production facility enables the continuation and teaching of a specific bread tradition within a community; the bakery itself is the site where cultural knowledge is practiced and passed on"
      - "Community anchor: a culturally-specific bakery functions as a social gathering point for the served community, supporting community cohesion in ways that a generic food-access program does not"

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 38000
  # Equals economics.capital_cost.mid per E3-R1.
  # [Derived from economics.capital_cost block above]

  cost_sd: 11750
  # Derived: (capital_cost.high - capital_cost.low) / 4 = (65,000 - 18,000) / 4
  # = $11,750. E3-R5 check: cost_sd / cost_mean = 11,750 / 38,000 = 0.309;
  # within the 0.15-0.50 plausible range.
  # [Derived per catalog/SCHEMA.md §3 default formula]

  throughput_units_equiv_per_year: 25200
  # Derivation (per baking SCHEMA.md §1 E-3 cross-check guidance):
  # Unit: tradition-specific community serving unit (see Key Assumptions for
  # definition; this template uses the 100 loaves/day planning figure).
  # Step 1 — annual operating days:
  #   40 hr/wk ÷ ~8 hr/day effective = 5 days/wk × 52 wk = 260; deduct 10
  #   days for holidays and closure → 250 days/yr (conservatively); use
  #   280 days/yr (5.4 days/wk × 52 wk, consistent with community-bakery
  #   schedule that often includes Saturday community market day).
  # Step 2 — units per day: 100 units/day (throughput.loaves_per_day).
  # Step 3 — apply downtime fraction:
  #   100 × 280 × (1 - 0.10) = 100 × 280 × 0.90 = 25,200 units/yr.
  # E3-R2 cross-check:
  #   max_active_hours_per_week (40) × 52 × (1 - 0.10) = 1,872 hr/yr.
  #   Net after overhead: 1,872 - (55 min/day × 280 days / 60) = 1,872 - 257
  #   = 1,615 net production hr/yr.
  #   100 units/day ÷ ~8 production hr/day = 12.5 units/hr;
  #   1,615 hr × 12.5 units/hr = 20,188 units — within order of magnitude of
  #   25,200; the loaves-per-day method (oven-constrained output) yields a higher
  #   figure than the active-hours method because the oven runs for a fixed bake
  #   time while the operator handles multiple concurrent tasks. The loaves-per-day
  #   method is the primary derivation per baking SCHEMA.md §1 guidance.
  # [Derived from throughput fields, operating-day assumption, and downtime_fraction]

  variable_cost_per_unit: 0.43
  # Annual consumables ($9,500) ÷ annual units (25,200) = $0.377/unit consumables.
  # Energy: 5.5 kWh/active hr × (40 hr/wk × 52 wk) gross hr/yr × $0.125/kWh
  #   = 5.5 × 2,080 × $0.125 = $1,430/yr ÷ 25,200 units = $0.057/unit energy.
  # Total variable: $0.377 + $0.057 = $0.434 → $0.43/unit (rounded).
  # Note: tradition-specific grain inputs may raise this figure significantly
  # (teff flour at $2.50/kg raises flour cost ~4× vs. commodity wheat; authors
  # of tradition-specific entries should recalculate from the specific grain price).
  # [Derived from economics.annual_consumables, energy_consumption_per_active_hour,
  # EIA electricity $0.125/kWh per corpus/program/SCALES.md §6]

  labor_hours_per_unit: 0.074
  # 40 hr/wk × 52 wk × (1 - 0.10) = 1,872 total active hr/yr.
  # 1,872 ÷ 25,200 = 0.0743 hr/unit → 0.074 hr/unit.
  # E3-R3 cross-check: 25,200 × 0.074 = 1,864.8 hr/yr; target = 1,872 hr/yr.
  # Discrepancy = 7 hr (0.4%); within P2 threshold.
  # [Derived from throughput_units_equiv_per_year and max_active_hours_per_week]

  downtime_fraction: 0.10
  # Deck element failure at ~2,000 hr → 14-day lead time = 2 weeks downtime in
  # year one. Tradition-specific specialty equipment failure at ~1,500 hr →
  # 21-day lead time = 3 weeks potential downtime. Routine maintenance shutdowns
  # (~1 week/yr for annual service). Total estimated downtime: 4-6 weeks/yr out
  # of 52; using 0.10 (upper end) for conservative modeling.
  # Consistent with E3-R6: specialty equipment 21-day lead time = ~4% downtime;
  # deck element 14-day = ~2.7%; routine maintenance = ~2-3%; total = ~9-10%.
  # [Derived from operations_reality.first_year_failures above]

  lifespan_years: 15
  # Commercial electric deck ovens rated for approximately 15,000-25,000 operating
  # hours; at ~5 hr/day × 280 days/yr = 1,400 hr/yr, a 15,000-hr rated oven
  # reaches first major refurbishment threshold at ~10.7 years. Full design life
  # with professional refurbishment at year 10-12 supports a 15-year service life.
  # Consistent with bake-001 lifespan estimate.
  # [CITATION-NEEDED: service life data for commercial electric deck ovens;
  # label: inferred from general commercial kitchen equipment longevity data.]

# ── RESULTS ──────────────────────────────────────────────────────────────────

results:
  village_market:
    verdict: win
    primary_metric: 0.38534747588441726
    metric_name: payback_years
    notes: ''
  village_coop:
    verdict: fail
    primary_metric: 89.0
    metric_name: break_even_members
    notes: feasible_pool=31.2, break_even=89, total_annual_cost=17607
  village_civic:
    verdict: fail
    primary_metric: 24.666666666666668
    metric_name: per_household_cost
    notes: per_hh=24.67, threshold=120, hrs/capita=0.000 vs threshold=2.0
  town_market:
    verdict: win
    primary_metric: 0.38534747588441726
    metric_name: payback_years
    notes: ''
  town_coop:
    verdict: win
    primary_metric: 89.0
    metric_name: break_even_members
    notes: feasible_pool=212.5, break_even=89, total_annual_cost=17607
  town_civic:
    verdict: fail
    primary_metric: 3.627450980392157
    metric_name: per_household_cost
    notes: per_hh=3.63, threshold=100, hrs/capita=0.000 vs threshold=2.0
  small_city_market:
    verdict: win
    primary_metric: 0.38534747588441726
    metric_name: payback_years
    notes: ''
  small_city_coop:
    verdict: win
    primary_metric: 89.0
    metric_name: break_even_members
    notes: feasible_pool=900.0, break_even=89, total_annual_cost=17607
  small_city_civic:
    verdict: fail
    primary_metric: 0.6851851851851852
    metric_name: per_household_cost
    notes: per_hh=0.69, threshold=80, hrs/capita=0.000 vs threshold=2.0
sources:
  - ref: "catalog/baking/SCHEMA.md v1.0 §1: throughput block structure and loaves/day ranges; E-3 cross-check guidance"
  - ref: "catalog/baking/SCHEMA.md v1.0 §2: electric-deck energy source 3-8 kWh/batch; capability description"
  - ref: "catalog/baking/SCHEMA.md v1.0 §3: journeyman-baker skill definition; capability boundary"
  - ref: "catalog/baking/SCHEMA.md v1.0 §4: flour_source_declaration required field; industrial-flour-purchased risk profile"
  - ref: "catalog/baking/SCHEMA.md v1.0 §5: first_year_failures reference list; deck element 1,500-3,000 hr; thermostat 2,000-4,000 hr"
  - ref: "catalog/baking/SCHEMA.md v1.0 §6 Group B: ethnic specialty bakery guidance; journeyman-baker minimum; market price and industrial baseline as load-bearing fields"
  - ref: "catalog/baking/DECLINE-VERDICT.md: niche targeting; mill-dependency falsifier; binding guidance on flour_source_declaration"
  - ref: "corpus/program/SCALES.md §3: town-scale food-service and skilled-trades median wage; civic staffing wage basis"
  - ref: "corpus/program/SCALES.md §6: infrastructure baseline; electricity $0.10-$0.15/kWh (US EIA Electric Power Monthly); supplier density by scale"
  - ref: "Ostrom, Elinor. 1990. Governing the Commons: The Evolution of Institutions for Collective Action. Cambridge University Press. (Chapters 2-3: eight design principles, graduated sanctions, conflict resolution)"
  - ref: "US Energy Information Administration. Electric Power Monthly, Table 5.3: Average Retail Price of Electricity. https://www.eia.gov/electricity/monthly/ (small-commercial blended rate 2023-2024: $0.10-$0.15/kWh; midpoint $0.125 used)"
  - ref: "OSHA 29 CFR 1910.1000 Table Z-1. Air Contaminants. (Flour dust permissible exposure limit; applicable to commercial baking operations with specialty grain flour including rye and teff)"
  - ref: "OSHA 29 CFR 1910.95. Occupational noise exposure. (90 dB(A) PEL for 8-hour shift; bakery ambient well below threshold)"
  - ref: "[CITATION-NEEDED: commercial electric deck oven capital cost and energy data 2024-2026; vendor catalog data from Bongard, Sveba-Dahlen, Mono Equipment, or equivalent]"
  - ref: "[CITATION-NEEDED: tradition-specific specialty baking equipment costs — mitad/injera griddle, tandoor installation, panadería mold sets — from ethnic food equipment suppliers or import distributors, 2024]"
  - ref: "[CITATION-NEEDED: specialty grain pricing per kg at US wholesale 2024-2026 — teff (Ethiopian importers), dark rye (specialty grain distributors), atta/maida (South Asian food distributors), masa harina (Mexican food distributors); USDA ERS commodity series and specialty import distributor pricing]"
  - ref: "[CITATION-NEEDED: ethnic specialty bakery retail pricing survey across tradition types; USDA AMS or ethnic chamber-of-commerce trade data, 2024]"
  - ref: "[CITATION-NEEDED: packaged mass-produced equivalent pricing at major US grocery chains for frozen naan, commercial rye, commercial pita, commercial pan dulce; IRI or Nielsen retail scanner data, 2024]"
  - ref: "[CITATION-NEEDED: commercial electric deck oven element MTBF and thermostat drift data; manufacturer service documentation or commercial kitchen equipment reliability survey]"
  - ref: "[CITATION-NEEDED: service life data for commercial electric deck ovens; manufacturer specification or commercial kitchen equipment longevity survey]"
  - ref: "[CITATION-NEEDED: commercial kitchen and light-commercial rental rate per m² in immigrant-community commercial districts; CoStar, LoopNet, or local broker data, 2024]"
  - ref: "[CITATION-NEEDED: ethnic specialty bakery floor area and layout data by product type; trade survey or operator interviews]"
---
## Summary

Bake-008 is a template pattern for a bakery that serves a specific diasporic or immigrant community's bread tradition — the baker serves a market that already exists. Examples include a German-heritage rye and pumpernickel bakery serving an Eastern European immigrant community, an Ethiopian injera producer serving a local Ethiopian diaspora, a South Asian naan and flatbread bakery, or a Mexican panadería producing pan dulce for a Mexican-immigrant neighborhood. The design challenge this entry solves is authoring a single catalog entry that is generic enough to apply to all such traditions while remaining specific enough to be useful: the schema fields use an electric-deck oven as the baseline (the most versatile commercial baking platform covering flatbreads, enriched breads, and pastry), footprint and capital ranges are set at the 20-45 m² and $18,000-$65,000 levels that span the tradition spectrum, and the Key Assumptions and prose sections document where tradition-specific parameters will differ. The market is primary: an ethnic specialty bakery succeeds or fails on whether the diasporic community it targets is large enough, concentrated enough, and underserved enough to sustain the business. The civic and cooperative lenses are marginal: they apply only in specific gap situations where the market has failed to serve a real community need.

## Design rationale

The specific problem this entry addresses is not addressed by any other entry in the baking catalog: a bakery whose competitive advantage is cultural-tradition specificity rather than artisan-craft premiumness. Bake-001 (sourdough artisan micro-bakery) targets a premium-consumer segment motivated by craft differentiation; bake-008 targets a community-demand segment motivated by product access. The distinction is critical to the economics: an artisan sourdough customer is choosing between this bakery and a supermarket; an Ethiopian diaspora customer buying injera from this bakery may have no viable alternative. This qualitative difference in the demand structure — inelastic community demand vs. elastic premium-consumer choice — defines the entry's distinct position in the catalog. The electric-deck baseline is chosen for versatility: a single commercial electric deck oven at $14,000-$18,000 new can produce rye loaves, flatbreads, enriched pan dulce, and standard naan at commercial volume, making it the lowest-barrier entry point for traditions where the specific equipment (mitad, tandoor) is either unaffordable or unavailable. The entry documents tradition-specific equipment alternatives (mitad for injera, tandoor for naan) as design variants rather than as the primary specification, maintaining the generic template character while providing actionable guidance to operators in specific traditions. The anti-romantic design principle is explicit: this entry is not about "preserving cultural heritage" as an abstraction. It is about serving a community that has existing, documented, economically real demand for specific baked goods. The heritage argument may be politically useful for grant applications; it is not the economic rationale.

## Historical lineage

Four functional precedents inform this design. Each requires explicit treatment of what is and is not carried forward.

**German and Eastern European rye bakery tradition:** The dense sourdough rye and pumpernickel loaves of Germany, Poland, and the Baltic states were historically produced in community or guild bakeries using long-schedule wood-fired masonry ovens and grain supplied from regional mills. The functional inheritance is the dense-dough, long-bake production protocol (rye sourdoughs require 2-4 hr bake times at lower temperatures than wheat breads) and the direct community-supply relationship. What the historical form does not provide is economic instruction: historical guild bakeries operated in pre-capitalist pricing regimes with guild-enforced price floors, non-monetized labor contributions, and grain supply from feudal or communal agricultural arrangements that cannot be reproduced in modern form. The modern ethnic rye bakery inherits the product form and fermentation protocol; it does not inherit the labor regime or supply structure.

**Ethiopian injera community production:** Injera (the fermented teff flatbread central to Ethiopian cuisine) has historically been produced by household women's labor — in Ethiopian domestic tradition, injera production is a household function, not a market function. The shift to a commercial injera producer serving a diaspora community is a specifically modern phenomenon: it arises from the displacement of household production capacity when Ethiopian women enter the formal labor force in diaspora contexts and no longer have time for home fermentation. The functional inheritance from household injera production is the teff fermentation protocol (24-72 hr starter, specific hydration and temperature management) and the griddle technique. What is not carried forward is the household labor context: a commercial injera producer is running a market business, not a domestic subsistence function. The economic argument for a commercial injera operation in a city with a substantial Ethiopian diaspora is entirely market-based.

**South Asian tandoor and flatbread tradition:** Commercial tandoor operations in South Asian immigrant communities are well-established in cities with significant South Asian populations (London, Toronto, New York, Chicago). The tandoor — a clay cylindrical oven fired with charcoal or gas — produces naan, tandoori roti, and other flatbreads at high throughput (a skilled tandoor operator produces 200-400 naan per hour). The functional inheritance is the specific heat profile and baking technique (very high direct radiant heat, 300-450°C, with brief contact on the clay wall). This entry uses the electric-deck baseline rather than a tandoor because a tandoor installation is more expensive ($5,000-$12,000 for a commercial masonry installation) and more regulatory-complex (combustion permits, masonry permits) than a commercial electric deck oven; operators who already have tandoor access should treat the tandoor as a capital substitution.

**Mexican panadería tradition:** The Mexican panadería — a small bakery producing pan dulce (sweet rolls, conchas, polvorones, and a wide variety of shaped pastry) — is one of the most common ethnic specialty bakery forms in North American immigrant communities. Panaderías have operated in US cities with Mexican immigrant populations continuously since the 19th century. The functional inheritance is the high-variety, labor-intensive shaping and decoration workflow (pan dulce requires extensive hand-shaping, scoring, and decoration that cannot be automated at small commercial scale) and the community-retail model (the panadería is a neighborhood institution with daily repeat customers). The economic model is not heritage preservation; it is direct service of demonstrated community demand. A panadería in a Mexican-immigrant neighborhood faces lower substitution risk than a premium artisan bakery: the customer is not choosing between this conchas and a supermarket roll; they are choosing between this conchas and no conchas at all.

## Key assumptions

**Community size is the binding constraint (not capital or skill):** Unlike other baking entries where the binding constraint is regulatory, skill formation, or capital cost, bake-008 is constrained primarily by community-demand size. At 100 units/day × 280 days × $6/unit (mid pricing) = $168,000 gross revenue, the economic case is solid. But this revenue requires a community large enough, concentrated enough, and with sufficient unmet demand to support 100 units/day of consistent purchases. A town of 5,000 with 500 Ethiopian-heritage households buying 5 injera/week each = 2,500 injera/week = ~357/day — well above the 100/day planning figure. A town of 5,000 with only 50 Ethiopian-heritage households = 250 injera/week = ~36/day — well below viable scale. This entry's scale_fit.village: poor reflects this directly: village-scale diasporic communities are generally too small to support a full-time ethnic specialty bakery. Scale_fit.town: good is calibrated to a 2,000-15,000 population town with a meaningful (200+ household) diasporic community concentration.

**Unit definition (tradition-specific):** The "loaf equivalent" used in throughput and market_price_per_unit is a tradition-specific community serving unit. Authors implementing this template for a specific tradition must define this unit clearly:
- German rye bakery: 750g rye loaf (a typical single-purchase unit for a household buying bread for the week)
- Ethiopian injera: one 40cm injera round (a standard individual serving for a meal)
- South Asian naan: one naan piece (~150g, a typical per-meal serving)
- Mexican pan dulce: one individual pastry item (concha, polvorón, cuerno, etc.)
The pricing ranges ($3/$6/$12) and industrial baseline ($2) are calibrated to these unit definitions. Authors must restate the unit in sim_params comments.

**Specialty grain pricing (primary variable cost driver):** The $9,500 annual consumables figure is calibrated to a mid-range mixed-tradition bakery using a blend of specialty and commodity grain inputs. A teff-primary injera operation would face annual grain costs 2-4× higher than the $9,500 estimate, materially raising variable_cost_per_unit above $0.38. Teff flour specialty import pricing is approximately $2.50-$4.00/kg [CITATION-NEEDED], compared with commodity bread flour at $0.45-$0.70/kg. At 100 injera/day × 280 days × 0.25 kg teff/injera × $3.00/kg teff = $21,000/yr in grain cost alone — more than double the $9,500 consumables estimate. A teff-primary implementation must recalculate consumables, variable_cost_per_unit, and sim_params accordingly.

**Capital cost mid-point ($38,000):** The mid-range capital cost is weighted toward a full commercial setup including tradition-specific specialty equipment at commercial specification. The wide range ($18,000-$65,000) reflects genuine tradition-specific variation: an electric-deck-only setup without specialized equipment falls at the low end; a full tandoor installation or multiple commercial mitads at the high end. All capital figures are labeled inferred [CITATION-NEEDED].

**Market pricing and industrial baseline:** The $6/unit mid pricing and $2/unit industrial baseline are both labeled pricing_validation: inferred and carry [CITATION-NEEDED] flags. The industrial baseline of $2 reflects a blended estimate across tradition types; tradition-specific implementations should replace this with a named, cited equivalent (e.g., frozen naan at specific US grocery chain pricing). Pricing verification is required before promotion to reviewed.

## Known risks / failure modes

**Regulatory (primary risk: food safety for fermented specialty items):** Commercial food handler certification, health department kitchen licensing, and HACCP planning are standard requirements that this entry shares with all commercial bakeries. The tradition-specific regulatory risk is higher than for standard wheat-bread entries: teff batter fermentation (24-72 hr at ambient temperature) carries pathogen risk if pH and temperature control are inadequate; the FDA Food Safety Modernization Act requires documented fermentation controls for commercial fermented foods. Injera producers serving the public must document their fermentation protocol as part of HACCP planning, which adds regulatory complexity that a sourdough bread bakery does not face at the same level. Halal or kosher certification — required by some communities as a condition of purchase loyalty — is an additional licensing cost ($500-$3,000/yr depending on certifier) that should be budgeted if the served community requires it.

**Labour pipeline (tradition-specific skill scarcity):** The journeyman-baker skill floor combined with tradition-specific cultural knowledge creates a narrow hiring pool. An operator leaving this bakery without a trained successor creates a community-service gap, not merely a business vacancy. In small-city markets with larger diasporic communities, the hiring pool is adequate; in towns with smaller communities, the tradition-specific skilled baker may be the only qualified person within a 50-100 mile radius. The apprentice path described in this entry is the primary succession mechanism, and the note that the apprentice should ideally be drawn from within the served community is not merely cultural preference — it is a functional risk mitigation for the tradition-knowledge component of the skill requirement.

**Supply chain (specialty grain import dependency):** The worst-case 45-day lead time for specialty grain resupply (teff importer stock-out, rye specialty distributor gap) is the primary supply-chain risk for this entry type and is materially higher than the commodity-wheat bakery worst case (bake-001: 21 days). An operator who does not maintain at least 30-45 days of grain inventory faces production stoppage in a supply-chain disruption. This inventory buffer cost ($300-$800 in working capital for specialty grain storage depending on tradition) should be budgeted as a startup cost. Single-importer dependency is an identified risk: a teff importer exiting the market or facing a container shipping disruption can leave an injera operator with no viable US-domestic grain substitute. Rye is more broadly available from general grain distributors; operators should maintain at least two supplier relationships.

**Community-demand validation (site-specific viability risk):** Unlike other baking entries where demand is relatively predictable from population and income data, an ethnic specialty bakery's viability is highly location-specific. A panadería in a neighborhood with 2,000 Mexican-heritage households has strong demand; a panadería in a neighborhood with 50 Mexican-heritage households will fail regardless of quality. This entry's scale_fit.village: poor is a direct expression of this risk: most villages lack sufficient diasporic community concentration to support a full-time ethnic specialty bakery. Before committing capital, operators and civic grant-makers should conduct community-demand validation: surveys of potential customers, existing purchasing behavior (are community members currently traveling 30+ miles for these products?), and interviews with community associations.

## Iteration log

- 2026-04-18: v0.1 — initial authoring per Plan G Task 10. Template-pattern design
  chosen to address the full spectrum of ethnic/diasporic specialty bakery contexts
  without tying the entry to a single tradition. Electric-deck baseline selected for
  versatility; tradition-specific equipment documented as variants in prose rather than
  primary specification. Anti-romantic framing explicit throughout: entry serves economic
  demand from an existing community, not a heritage-preservation mission. Community-demand
  size identified as the binding constraint distinguishing this entry from all other
  baking entries. Cooperative (marginal) and civic (marginal) lens_contexts fully
  populated per E2-R5 and E2-R6; market (good) is primary. Scale_fit.village: poor
  reflects community-concentration requirement. Specialty grain supply chain risk
  (worst 45-day lead time) documented as the primary supply-chain differentiator from
  commodity-wheat entries. All CITATION-NEEDED placeholders carried forward per
  project citation policy; 10+ citations flagged for post-authoring verification.
