---
# ── IDENTITY ──────────────────────────────────────────────────────────────────

id: weave-015
trade: weaving
name: "Artist-Designer Collaboration Studio"
tagline: "Professional-tier shared floor-loom studio for working artists and fashion designers who need equipment access without capital commitment"
status: draft
version: 0.1
supersedes: null
inspirations:
  - european-shared-printmaking-studio-model
  - nyc-garment-district-production-cooperative
  - scandinavian-textile-studio-collective

# ── PHYSICAL ENVELOPE ────────────────────────────────────────────────────────

footprint_m2: 55
# Mid of the 40–70 m² viable range. Accommodates 4–5 floor-loom-8shaft units
# in dedicated member bays (each bay ~8–10 m² including working zone, beam
# advance space, and selvedge-monitoring clearance), a shared warping area with
# sectional warping mill and paddle warping frame, a yarn winding station,
# and a climate-control unit. Tight at 40 m² (4 looms only); 70 m² permits
# 5 looms plus a small sample and finishing counter.
ceiling_min_m: 2.7
# Floor-loom-8shaft castle height (uprights + beater arc) typically 1.8–2.1 m;
# 2.7 m minimum provides adequate clearance for tall looms and comfortable
# working posture at the beater. No hoisting or overhead extraction required.
ventilation: natural-sufficient
# No combustion, no chemical process, no significant particulate source.
# Electric lighting and humidity-control HVAC are the only equipment-driven
# ventilation concerns; standard building fresh-air exchange is sufficient for
# a dry-loom studio with 4–5 occupants. If a dye station is added as an upgrade,
# this must be revised to mechanical-extraction-required.

# ── ENERGY ───────────────────────────────────────────────────────────────────

energy_source: electric-lighting-only
# The productive equipment (floor-loom-8shaft units) requires no powered drive.
# Energy consumption is limited to: studio lighting (professional-grade task and
# overhead lighting required for fine-fiber pattern verification), humidity-control
# HVAC (required for warp-tension stability with wool and silk warps), and
# auxiliary equipment (yarn winder, warping mill motor if motorized). No three-phase
# supply needed; standard commercial single-phase service is adequate.
energy_consumption_per_active_hour: "2–5 kWh (studio lighting + humidity control at steady state; higher at peak occupancy or during active humidification cycles)"
backup_fuel: null

# ── THROUGHPUT ───────────────────────────────────────────────────────────────

throughput:
  meters_per_day: 8.0
  # Facility-wide blended daily output across 4 active looms at professional
  # member-hours occupancy. Individual loom yields for floor-loom-8shaft at
  # journeyman-to-master level:
  #   pattern complexity (networked twill, 8-shaft structures): 1–3 m/day/loom
  #   twill and satin derivatives: 2–4 m/day/loom
  # Blended across 4 active looms at professional skill level, 2 m/day/loom
  # average (weighted toward pattern work as primary product-mix): 8 m/day.
  # [CITATION-NEEDED: floor-loom-8shaft throughput at pattern complexity —
  #  derived from weaving SCHEMA.md §1 ranges; practitioner-reported averages needed]
  warp_width_cm: 150
  # Representative warp width for floor-loom-8shaft in professional fashion and
  # textile-art applications. 150 cm supports garment-width fabric suitable for
  # most fashion-design cuts without seaming. Individual looms may be configured
  # at 90–180 cm depending on the member's project requirements; 150 cm is the
  # mid-point and the basis for throughput calculations.
  pattern_complexity: pattern
  # Primary production is 8-shaft pattern work: networked twill, M's and O's,
  # advancing twill, collapse weave, and supplementary-weft structures. This
  # is the defining capability of the 8-shaft floor loom over the 4-shaft
  # alternative; the equipment investment is justified only if members are
  # producing at pattern complexity level. Plain weave and 2/2 twill are within
  # scope but are not the primary design use case.
  max_active_hours_per_week: 40
  # Professional member-hours model: studio open 6 days/wk; members book
  # half-day or full-day blocks. Upper bound 40 hr/wk facility-wide (not per loom).
  # Warping and loom-dressing time (4–8 hr per new warp per loom) is significant
  # and is counted against member booking hours, not excluded. A realistic
  # full-time professional weaver uses 30–35 hr/wk at the loom; the 40 hr/wk
  # ceiling assumes high occupancy across 4 looms in a mixed half-day/full-day
  # booking pattern.
  product_mix:
    yardage: 40
    rugs_upholstery: 10
    tapestry_art: 15
    garments_accessories: 30
    instruction_open_studio: 5
    # yardage (40%): fashion designers producing woven cloth for their own
    #   garment collections; artist-weavers producing yardage for licensing.
    # garments_accessories (30%): finished woven garments, scarves, accessories
    #   produced by member weavers for their own commercial channels.
    # tapestry_art (15%): wall-hanging and art-textile work by artist-members.
    # rugs_upholstery (10%): high-end floor coverings and upholstery fabric
    #   for interior-design clients.
    # instruction_open_studio (5%): minimal; this is a professional studio,
    #   not an instruction facility. The master-weaver supervisor may mentor
    #   advanced members, but formal instruction is not the operating model.
    # Sum: 40 + 10 + 15 + 30 + 5 = 100.
  throughput_variance:
    seasonal: "Fashion-collection production cycles (spring/summer and fall/winter) create predictable demand peaks in August–October and January–March; tapestry and art-textile work is non-seasonal; January trough less pronounced than retail-oriented studios."
    worst_month_fraction_of_average: 0.65
    # Professional commission and collection work buffers against the worst
    # seasonal troughs; 0.65 reflects a slow summer or post-collection slack.
    best_month_fraction_of_average: 1.40
    # Pre-collection push (Sep–Oct for fall/winter) elevates occupancy and
    # member production hours above average.

# ── TRADE-SPECIFIC FIELDS ────────────────────────────────────────────────────

trade_specific:
  loom_type: floor-loom-8shaft
  # Professional-tier equipment. The 8-shaft floor loom provides the full pattern
  # range required for fashion-designer and artist-weaver work (networked twill,
  # advancing twill, 8-shaft structures, double weave, supplementary weft). The
  # investment premium over a 4-shaft floor loom ($4,000–$15,000 vs $1,500–$6,000)
  # is justified by the expanded pattern vocabulary and the wider warp width (up to
  # 180–200 cm) that fashion-designer members require.
  humidity_control_required: true
  # Wool, silk, and fine linen warps are expected as the primary fiber types for
  # professional fashion and art-textile work at this price point. Humidity variation
  # causes warp-tension instability and dimensional inconsistency in finished cloth,
  # both unacceptable at professional-production scale. Target RH 45–55%. Climate-
  # control capital cost is included in the capital_cost range; operating energy is
  # reflected in energy_consumption_per_active_hour.
  fiber_source_declaration: industrial-yarn-purchased
  # Members source their own fiber from commercial yarn distributors and specialty
  # suppliers appropriate to their product line; the studio facility itself does not
  # maintain fiber stock or operate a spinning program. Industrial yarn (commercially
  # spun, quality-graded, consistent count) is the default for professional
  # fashion-design work where dimensional consistency is a production requirement.
  # Individual members may use local-fiber-spun or heritage-fiber yarns for specific
  # projects; this is their supply-chain decision, not the studio's.

# ── OPERATOR PROFILE ─────────────────────────────────────────────────────────

operator_skill_floor: master-weaver
# The master-weaver designation here refers to the studio supervisor, not to
# member skill requirements. Members are required to demonstrate journeyman-weaver
# competency as a condition of membership (floor-loom threading, tie-up, pattern
# draft execution, warp-tension management independently) — see lens_context.
# cooperative.membership_boundary. The studio supervisor must hold master-weaver
# competency to: (a) assess prospective member skill at intake, (b) diagnose
# loom-setup problems across the 8-shaft equipment configuration, (c) provide
# authoritative advice on complex pattern structures, and (d) ensure equipment
# safety in a multi-occupant professional studio. A journeyman-weaver supervisor
# cannot reliably perform the intake skill assessment for an 8-shaft pattern studio.
operators_concurrent: "1 supervisor + 1–4 members"
# Studio supervisor (master-weaver, part-time or fractional FTE) present during
# all open hours as safety monitor and equipment authority. 1–4 active member-
# weavers simultaneously (equipment ceiling: 4–5 loom bays; practical concurrent
# occupancy for focused professional work is 3–4 members).
apprentice_friendly: false
# This is a professional production-access model, not a training program.
# Members are admitted only upon demonstration of journeyman-weaver competency;
# the studio does not provide a structured path from novice to journeyman-weaver
# skill. The master-weaver supervisor's role is equipment safety and peer
# consultation, not formal skill instruction. Succession risk: the supervisor
# position requires a master-weaver in the local or regional hiring pool; this is
# a thin supply that must be named as a known risk (see Known Risks section).

# ── ECONOMICS ────────────────────────────────────────────────────────────────

economics:
  currency: USD

  capital_cost: { low: 25000, mid: 55000, high: 90000 }
  # Low ($25,000): 4 used floor-loom-8shaft units ($3,000–$4,000 each,
  #   second-hand) + basic warping equipment + residential humidifier + minimal
  #   studio fit-out. Feasible as a cooperative startup on constrained capital.
  # Mid ($55,000): 4–5 new or refurbished floor-loom-8shaft units ($5,000–$8,000
  #   each for mid-grade new: Macomber, Schacht Mighty Wolf 8-shaft, or equivalent)
  #   + sectional warping mill + powered yarn winder + commercial humidity-control
  #   system + professional studio lighting + equipment storage and fit-out.
  # High ($90,000): 5 professional-grade 8-shaft looms (AVL or Toika equivalent,
  #   $10,000–$15,000 each) + full warping infrastructure + dobby-equipped units
  #   + commercial HVAC with integrated humidity management + high-quality
  #   professional task lighting throughout + specialty storage and staging counter.
  # [CITATION-NEEDED: floor-loom-8shaft capital cost — equipment retailer pricing
  #  (AVL Looms, Macomber Looms, Schacht Spindle Co., Toika) for professional-grade
  #  8-shaft units, 2024–2025]

  install_cost: 5000
  # Covers: commercial humidity-control HVAC installation, professional studio
  # lighting (track lighting for pattern verification at warp face), electrical
  # service upgrade for climate-control load, loom bay layout and floor marking,
  # and studio signage. Rough estimate; varies with building condition and HVAC
  # scope. [CITATION-NEEDED: HVAC + lighting install cost estimate for professional
  # fiber arts studio; derived from comparable studio fit-out estimates]

  annual_maintenance: 2800
  # Multi-loom professional studio: heddle replacement and reed maintenance across
  # 4–5 floor-loom-8shaft units (professional members are lower-impact than multi-
  # user civic novice groups, but 8-shaft configurations have more heddle count and
  # dobby-mechanism exposure); HVAC filter replacements quarterly; warp-beam ratchet
  # service; general studio upkeep. Higher per-loom figure than a single-operator
  # studio due to multi-user turnover and the complexity of 8-shaft configurations.
  # [CITATION-NEEDED: annual maintenance estimate for professional shared weaving
  # studio; no published benchmark identified; derived from per-item replacement costs]

  annual_consumables: 3600
  # Heddle replacement across all looms (~$600/yr); reed replacement cycle
  # (~$400/yr); treadle and dobby tie-up cord/pegs (~$250/yr); studio supplies
  # (scissors, tapestry needles, shuttle sets, marking tape, paper draft rolls:
  # ~$800/yr); HVAC filters (~$300/yr); safety and cleaning supplies (~$250/yr);
  # miscellaneous studio stock (warp sticks, lease sticks, bobbin repair: ~$200/yr).
  # Members supply their own fiber; consumables here reflect equipment wear and
  # shared studio supplies only.
  # [CITATION-NEEDED: professional shared studio consumables estimate; derived from
  #  per-item pricing in weaving supply catalogs (Yarn Barn, WEBS, Halcyon Yarn)]

  floor_space_rent_per_year: 14400
  # Imputed commercial rent for 55 m² of light-commercial or arts-district space
  # in a small city. $22/m²/month × 55 m² × 12 = $14,520/yr; rounded to $14,400.
  # Professional studios typically require ground-floor or easy-access space with
  # adequate structural load capacity for loom weight (floor-loom-8shaft units
  # weigh 150–250 kg each; 5 looms ≈ 1,000 kg concentrated load).
  # [CITATION-NEEDED: light-commercial floor-space rent in small-city arts district
  #  2024–2025; $22/m²/month is an estimate; local market rate should be substituted
  #  at implementation]

# ── OPERATIONS REALITY ───────────────────────────────────────────────────────

operations_reality:

  first_year_failures:
    - item: "Dobby mechanism malfunction (floor-loom-8shaft, first unit)"
      estimated_hours_to_failure: 2500
      # Mechanical dobby (peg-and-lever) mechanisms accumulate lint and develop
      # stick-and-release failures under sustained use; multi-member turnover
      # accelerates wear relative to single-operator use. Texsolv-cord dobbies
      # are somewhat more tolerant, but peg holes and lever pivots wear under
      # heavy pattern cycling. First failure expected in the first operating year
      # across a 4–5 loom bank with professional-level production intensity.
      replacement_cost: 350
      # Cleaning, adjustment, and partial peg or lever replacement; specialist
      # call-out for a mechanical dobby that requires full mechanism disassembly.
      replacement_lead_time_days: 14
      serviceable_by: specialist
      # Dobby mechanism disassembly requires familiarity with the specific loom
      # manufacturer's mechanism; a generalist journeyman can attempt cleaning
      # but full peg-track or lever replacement typically requires specialist.

    - item: "Warp beam ratchet / pawl wear (floor-loom-8shaft, first unit)"
      estimated_hours_to_failure: 2000
      # Professional-intensity warping cycles (frequent beam advance for
      # long warps in fashion yardage) wear ratchet-and-pawl tensioning
      # faster than light-use studio averages. Tension slippage mid-weave
      # creates a cloth defect line; professional-grade production cannot
      # tolerate this. First-unit failure expected within the first operating year.
      replacement_cost: 220
      replacement_lead_time_days: 10
      serviceable_by: journeyman
      # Ratchet pawl spring replacement and ratchet tooth inspection is
      # journeyman-level; full ratchet replacement is borderline journeyman/
      # specialist depending on the loom model.

    - item: "Climate-control humidifier component failure"
      estimated_hours_to_failure: 2800
      # Commercial-grade humidifier under continuous load in a 55 m² studio
      # with 4–5 active looms; first-year failure probability elevated by
      # startup-year calibration and heavy evaporative demand in dry climates.
      replacement_cost: 900
      # Commercial humidifier module or evaporator replacement; portable backup
      # unit (~$200) provides temporary continuity during repair lead time.
      replacement_lead_time_days: 10
      serviceable_by: specialist

  maintenance_schedule:
    daily:
      task: "Pre-session safety walkdown: check warp tension on active warps at all loom bays, inspect dobby cord or tie-up on active pattern looms, verify humidity reading and adjust control set-point, sign-in log reset"
      performed_by: operator
      # Supervisor (master-weaver, part-time) completes walkdown at studio open;
      # each member is responsible for warp-condition check on their own loom bay
      # at start of booking session.
    weekly:
      task: "Full loom inspection: dobby mechanism cleaning (lint removal and lever pivot check) on all units, reed alignment and bent-dent inspection, warp-beam ratchet function test, heddle inventory check per shaft, HVAC humidity-control filter and water-level check on humidifier unit"
      performed_by: operator
    quarterly:
      task: "Comprehensive loom service: ratchet/pawl lubrication and wear assessment on all beams, bulk heddle inventory and replacement order, professional HVAC filter replacement, dobby peg inventory assessment and damaged-peg replacement, reed replacement if dent wear exceeds tolerance threshold"
      performed_by: journeyman
    annual:
      task: "Full studio inspection: structural frame joint assessment on all looms, all warp and cloth beam axle play inspection, HVAC system annual service contract call, electrical panel review, lease/compliance walkthrough, insurance review for member liability coverage"
      performed_by: specialist

  startup_shutdown_overhead_per_day_min: 20
  # Professional shared studio with a structured booking model: 20 min/day total
  # for supervisor walkdown at open (10 min), loom-bay sign-off at close and
  # humidity log entry (10 min). Lighter than a civic multi-user facility because
  # members are self-competent and responsible for their own loom-bay setup and
  # teardown within their booking block; the supervisor's role is safety monitoring,
  # not member-by-member onboarding.

  max_active_hours_realism_note: >-
    40 hr/wk is the booking-ceiling gross target (6-day week × ~6.7 hr/day open
    hours, or 5-day × 8 hr). Net of 20 min/day startup-shutdown overhead on a
    5-day open week: effective hours ≈ 40 − (20 min × 5 / 60) ≈ 38.3 hr/wk net.
    sim_params.throughput_units_equiv_per_year uses the derated figure.
    Additionally, warping and loom-dressing (4–8 hr per new warp per loom) is
    counted within booking hours rather than excluded; the 8 m/day facility-wide
    throughput figure already reflects the blended mix of active weaving and
    warp-setup sessions within a member's booking block.

  interruption_notes: >-
    Professional-studio interruption profile is materially lighter than a civic
    open-studio. Typical intraday: supervisor consultation on loom setup or pattern
    structure issue (~10–15 min total per session across all active members),
    booking-transition handoff between outgoing and incoming member (~5–10 min per
    bay change), occasional equipment fault triage (~15–20 min for a dobby stick
    or tension issue). Total intraday interruption approximately 30–45 min per
    operating day; folded into the derated throughput figure in sim_params.

  consumables_lead_time_days: { typical: 7, worst: 28 }
  # Typical: standard weaving supplies (wire heddles, texsolv heddles, reeds,
  # tie-up cord, dobby pegs) from US weaving distributors with stock inventory.
  # Worst: specialty reeds (non-standard sett for fashion-weight fine silk),
  # manufacturer-specific 8-shaft dobby components, or HVAC commercial parts
  # with seasonal backorder; 28 days represents the realistic tail risk for
  # non-standard replacement parts.

  throughput_variance:
    seasonal: "Fashion-collection production cycles (spring/summer and fall/winter) create demand peaks Aug–Oct and Jan–Mar; tapestry and art-textile work is non-seasonal; trough is post-collection July and November."
    worst_month_fraction_of_average: 0.65
    best_month_fraction_of_average: 1.40

  operator_impact:
    noise_db: 62
    # Floor-loom-8shaft operation: rhythmic beater and treadle with dobby
    # mechanism actuation; ~60–65 dB at operator position. Well below OSHA
    # 85 dB action level; compatible with focused design-concentration work.
    # [CITATION-NEEDED: floor-loom-8shaft noise level measurement]
    heat_exposure: "Low at all loom positions; studio temperature maintained at 18–22°C for fiber stability and member comfort; humidity control (45–55% RH) is the primary environmental management requirement"
    emissions: "No combustion, no chemical process, no significant particulate emissions during loom operation; fine fiber dust from high-volume warping is a minor irritant; standard building ventilation adequate; no air-permit trigger"
    physical_demand: "Moderate: sustained seated treadling and upper-body shuttle-and-beater motion; standing during warping (4–8 hr/warp on new setup); supervisor role involves floor-walking and occasional loom-frame adjustment. Ergonomic risks: repetitive upper-limb motion, seated posture fatigue over long production sessions."

# ── REGULATORY NOTES ─────────────────────────────────────────────────────────

regulatory_notes:
  zoning: "Light-commercial, arts-district, or mixed-use zoning; no industrial-use trigger from floor-loom operation alone; ground-floor space preferred for structural load capacity (loom weight); confirm building structural loading rating before installation"
  emissions: "No air-permit trigger; no dye-station effluent requirement (dry-loom configuration only); standard commercial building code compliance; no OSHA special-process permit required for dry-loom weaving operation"
  other: "Member liability framework requires a formal membership agreement with waiver of personal-injury claims and assignment of loom-damage liability; cooperative legal registration (LLC or worker cooperative) is required for lens_fit.cooperative: good; IP and attribution clause in membership agreement is essential for commercial-output use cases (see Known Risks)"

# ── CONTEXT FIT ──────────────────────────────────────────────────────────────

lens_fit:
  market: poor
  # The studio facility itself does not sell commercial output; it provides
  # equipment access on a member-subscription model. Revenue is member fees
  # and off-hours rental, not product sales. Market lens evaluates the
  # facility's commercial output — which is zero by design. Members' own
  # commercial output is separate and not attributed to the facility.
  cooperative: good
  # Primary lens. Professional-member-hours model with formal membership
  # agreement, skill-based admission, booking system, graduated sanctions,
  # and Ostrom-compliant governance. The cooperative form is natural for a
  # shared high-value capital pool serving self-employed professionals who
  # cannot individually finance 8-shaft floor looms.
  civic: marginal
  # Secondary lens. A municipal or arts-council subsidy could reduce member fees
  # and expand access to emerging artists and fashion students; however, the
  # facility's professional-tier positioning and commercial-output orientation
  # make a full civic-public-goods case weaker than a community-education entry.
  # Marginal reflects viability under favorable civic-framing assumptions
  # (economic-development angle, creative-industries grant) rather than a strong
  # public-goods case.

scale_fit:
  village: poor
  # Professional-weaver and fashion-designer population too small at village scale
  # (500–2,000 residents) to sustain 15–25 member subscriptions at $1,500–$3,000/yr.
  # The addressable professional-practitioner pool at village scale is 0–2 individuals;
  # cooperative viability requires a minimum of 8–10 active members.
  town: marginal
  # Possible at larger end of town scale (10,000–15,000 residents) in craft-intensive
  # or design-culture communities; minimum member pool is borderline. Membership
  # recruitment would require drawing from a regional catchment (30–60 mile radius)
  # rather than town alone.
  small_city: good
  # Target scale: 15,000–75,000 residents. Sufficient professional-weaver and fashion-
  # designer population in a small city with an arts or design community (or proximity
  # to a design school or fashion program) to sustain 15–25 active members.

# ── LENS CONTEXT ─────────────────────────────────────────────────────────────

lens_context:

  cooperative:
    membership_boundary: >-
      Professional weavers and fashion designers who can demonstrate journeyman-
      weaver floor-loom competency at intake assessment. Intake assessment conducted
      by the master-weaver supervisor: candidate must thread a 4-shaft minimum draft
      independently, demonstrate warp-tension management, and execute a sample weave
      at pattern complexity appropriate to the studio's primary product-mix. Students
      and apprentices are not eligible for standard membership; a conditional
      student-membership tier (reduced hours, supervised access only, reduced fee)
      may be established by member vote. Geographic boundary: small-city local and
      regional catchment (up to 60-mile radius); remote membership is not meaningful
      for an equipment-access cooperative. Annual membership fee: $1,500–$3,000/yr
      (full professional tier); fee structure set by member vote at annual meeting.

    rules_source: >-
      Cooperative bylaws adopted at founding member meeting and registered with the
      cooperative's legal entity (see legal_form). Bylaws govern: membership eligibility
      and intake process, fee schedule and payment terms, booking system rules (advance
      booking window, maximum consecutive days, member-priority vs. guest-rental
      hierarchy), loom-assignment and warp-storage policies, IP and attribution clause
      for commercial outputs, loom-damage liability and cost-recovery procedure, guest
      and visitor policy, and access-suspension criteria. Bylaws published on the
      cooperative's member portal; hard copy posted in studio.

    monitoring: >-
      Digital booking system records all member sessions (member ID, loom bay, date,
      hours, warp project tag). Physical sign-in log at studio entry as backup.
      Master-weaver supervisor observes loom-condition at session open and close;
      loom-damage incidents logged immediately by the supervisor with photographic
      record. Monthly usage-pattern review by the cooperative board (3-member rotating
      committee from active membership); annual financial audit by full membership.
      Booking-utilization rates by loom bay reported to members quarterly to inform
      capacity-expansion or loom-retirement decisions.

    graduated_sanctions: >-
      Verbal warning (logged) for first minor infraction (late session overrun,
      failure to restore loom bay) → written notice + mandatory session-end protocol
      retraining for repeat minor infraction → booking privileges suspended 30 days
      pending board review for significant violation (loom damage unreported, warp
      left in disrepair for next member, unauthorized equipment modification) →
      membership suspended pending investigation for serious violation (deliberate
      damage, misrepresentation of intake skill level, commercial misuse of studio
      IP attribution) → membership terminated with opportunity for appeal at member
      meeting. Loom-damage cost-recovery charge assessed at replacement cost + 20%
      for supervisor time; waived on first incident if repair is minor and
      self-reported promptly.

    conflict_resolution: >-
      Day-to-day disputes (scheduling conflicts, loom-bay condition disputes,
      attribution questions) mediated by master-weaver supervisor as first instance.
      Member-vs-member disputes and appeals of supervisor decisions escalated to the
      3-member cooperative board; board decision issued within 21 days of formal
      written complaint. Board decisions are final subject to appeal to a full
      member vote (majority required to overturn board decision). IP and attribution
      disputes require referral to the cooperative's registered legal counsel before
      board adjudication if commercial damages are claimed.

    ostrom_principles_addressed: [1, 2, 3, 4, 5, 6, 7]
    # Principle 1 (clear boundaries): skill-based membership with documented
    #   intake assessment; professional-tier only; geographic boundary stated.
    # Principle 2 (congruence): rules calibrated to professional shared-equipment
    #   model; booking and liability rules congruent with commercial-output context.
    # Principle 3 (collective choice): bylaws amendment process below; members
    #   set fee schedule and booking rules at annual meeting.
    # Principle 4 (monitoring): digital booking system + supervisor log; quarterly
    #   board review of usage data.
    # Principle 5 (graduated sanctions): documented above.
    # Principle 6 (conflict resolution): supervisor → board → member vote pathway.
    # Principle 7 (nested enterprises): cooperative nested in legal entity with
    #   external recognition (see legal_form); board nested in full membership.
    # Principle 8 (external recognition): partially addressed by legal registration;
    #   not fully addressed where civic subsidy is absent. Named as a risk: an
    #   unsubsidized cooperative without municipal acknowledgment is more
    #   vulnerable to dissolution if membership drops below viable threshold.

    member_amendment_process: >-
      2/3 vote of active members at the annual general meeting; 30-day advance notice
      required for bylaw amendments. Emergency operational rule changes (booking
      system, loom-bay assignment, safety protocols) may be enacted by the
      3-member cooperative board with 14-day notice and ratification at the next
      member meeting by simple majority. Fee schedule changes require 2/3 vote
      at annual meeting; mid-year fee changes require 3/4 vote with 60-day notice
      to allow members to plan around cost changes.

    legal_form: >-
      State-registered limited liability company (LLC) with cooperative operating
      agreement, or state-registered worker cooperative, depending on jurisdiction.
      Registration required before equipment purchase; cooperative operating agreement
      must include the IP and attribution clause as a core governance document.
      An unregistered informal collective is not acceptable for a professional-tier
      commercial-output studio: legal liability for loom damage, commercial attribution
      disputes, and member-exit capital claims all require a registered entity. Local
      arts-council or economic-development office acknowledgment of the cooperative is
      recommended but not required at launch.

    scale_fit_note: >-
      Governance rules calibrated for small-city scale (15–25 active professional
      members). Minimum viable membership is approximately 10–12 active members to
      sustain 4 loom bays at adequate occupancy and cover fixed costs (rent, maintenance,
      supervisor fraction). At town scale, the minimum viable membership is borderline
      and requires regional catchment recruitment. At village scale, governance is
      infeasible due to insufficient professional-practitioner population.

  civic:
    political_coalition: >-
      Arts-council or creative-industries development office (economic-development
      framing: the studio enables professional creative workers to operate commercially
      without capital barrier); regional fashion or design school (partnership for
      student access tier and curriculum integration); small-business development
      center (shared-equipment model reduces startup cost for independent fashion
      designers). Secondary coalition: local gallery networks and independent
      retailers who carry member-produced work (commercial-output argument).

    council_vote_estimate: >-
      4-3 marginal in most small-city councils; civic investment in a professional-
      tier commercial-output facility faces opposition on the grounds that it
      subsidizes commercial activity rather than delivering public goods. The strongest
      counter-argument is the economic-development framing (reduces barriers for
      creative micro-businesses; retains professional creative talent in the city)
      rather than a cultural-access argument. Opposition will note that members are
      charging commercial prices for their output while benefiting from subsidized
      equipment access.

    competes_with_private: >-
      No direct private-sector equivalent exists in most small cities: a for-profit
      equipment-rental studio offering professional-grade 8-shaft floor looms is not
      a functioning market in most US small-city contexts. The cooperative fills an
      access gap that the market has not provided. In cities where a private studio
      does operate (rare), a civic subsidy to the cooperative would create an unfair
      competitive situation and would require explicit justification.

    governance_form: >-
      Cooperative-owned and member-governed with optional arts-council liaison
      seat on the cooperative board (non-voting). If civic subsidy is provided,
      a public-accountability provision in the bylaws (annual reporting to arts
      council, public financial audit) is required as a condition of subsidy receipt.
      Municipally owned operation is not the natural form for this entry; the
      professional-member-governance model is the appropriate structure even under
      civic subsidy.

    budget_line: >-
      If civic subsidy is pursued: arts-council creative-industries grant ($5,000–
      $20,000/yr range typical for small-city professional arts infrastructure)
      and/or one-time economic-development capital grant for equipment purchase
      (reduces founding capital requirement; supports the low-capital-cost scenario).
      Operating subsidy reduces member fees, making the studio accessible to
      emerging artists and recent design-school graduates. Without subsidy, the
      studio operates on member fees and off-hours rental income alone.

    benchmark_comparison: >-
      At small-city scale (20,000 households as mid-point), a direct annual arts-
      council grant of $15,000/yr ÷ 20,000 hh ≈ $0.75/hh/yr — well below the
      civic service cost threshold at which political scrutiny intensifies ($5/hh/yr
      for most small-city arts programming). No full municipal operating subsidy is
      assumed; the cooperative is designed to be self-sustaining on member revenue.
      Comparable civic support: arts-council grant funding for professional
      printmaking and ceramics studios in peer small cities runs $8,000–$25,000/yr
      as one-time or recurring equipment and operating support.
      [CITATION-NEEDED: arts-council grant amounts for professional shared studios
      in US small cities 2023–2025]

    staffing_model:
      role: "Part-time master-weaver supervisor (cooperative employee or contractor)"
      operator_fte: 0.4
      # 0.4 FTE: approximately 16 hr/wk for studio open hours and equipment
      # oversight. The master-weaver supervisor is not a full-time employee;
      # the position is typically filled by a working professional weaver who
      # takes the supervisory role as a fractional income supplement to their
      # own production work. Additional administrative tasks (booking system,
      # member communications, maintenance scheduling) add ~4–6 hr/wk, bringing
      # effective commitment to ~20 hr/wk for an active supervisor.
      wage_assumption: 42000
      # Annualized at 0.4 FTE: $42,000 × 0.4 = $16,800/yr direct supervisor cost.
      # Master-weaver full-time equivalent at $42,000/yr is at the lower bound of
      # skilled-artisan-tier wage for a small city; the fractional nature of the
      # role and the fact that the supervisor is typically a working professional
      # weaver with their own income stream makes this a plausible market rate for
      # the fractional position. Annualized FTE wage for reference comparisons.
      wage_source: "corpus/program/SCALES.md §3 small-city-scale skilled-trades median; master-weaver/artisan-instructor wage calibrated to upper skilled-artisan tier"
      hours: "~16 hr/wk studio supervision + ~4–6 hr/wk administrative (booking, member communications, maintenance scheduling); effective 20–22 hr/wk commitment"
      hiring_notes: >-
        Master-weaver with floor-loom-8shaft competency and pattern-work expertise
        is required; the hiring pool nationally is thin and concentrated in metro areas
        and design-school cities. Small-city hiring radius 100–200 miles is realistic.
        The fractional nature of the role (0.4 FTE) allows a working professional weaver
        to take the position without abandoning their own studio practice; this is the
        most plausible recruitment model. $16,800/yr for ~20 hr/wk effective commitment
        ($16–$17/hr effective rate) is modestly below what a master-weaver can earn
        from their own production work; compensation supplemented by free studio access
        and use priority may close the gap. [CITATION-NEEDED: master-weaver hourly
        rate survey; skilled-artisan tier wage data for small-city markets 2024–2025]

    civic_externalities:
      - "Creative-industry infrastructure: provides the capital foundation for independent fashion designers and artist-weavers to operate professionally without $25,000–$90,000 in personal equipment investment, enabling micro-business formation in the creative sector that would otherwise not occur — an economic-development externality that arts-council grants routinely target"
      - "Textile-skills preservation at professional tier: the studio maintains active 8-shaft floor-loom technique, complex pattern-weave knowledge, and production-weaving practice at professional level within the small-city creative economy; without shared infrastructure, these skills migrate to larger metro areas where capital access is less constraining"

# ── SIMULATION PARAMETERS ────────────────────────────────────────────────────

sim_params:
  cost_mean: 55000
  # Equals economics.capital_cost.mid per E3-R1.

  cost_sd: 16250
  # (high − low) / 4 = (90,000 − 25,000) / 4 = 16,250.
  # cost_sd / cost_mean = 16,250 / 55,000 = 0.296; within 0.15–0.50 acceptable
  # range per E3-R5.

  throughput_units_equiv_per_year: 1600
  # Derivation (per weaving SCHEMA.md §1 E-3 guidance):
  # Derated active hours: 40 hr/wk − (20 min/day × 5 days / 60) ≈ 38.3 hr/wk net.
  # Effective hours/yr: 38.3 × 52 × (1 − 0.10) = 38.3 × 52 × 0.90 ≈ 1,792 hr/yr.
  # Throughput rate: ~0.89 m/hr facility-wide (blended rate for pattern-complexity
  # work at 8 m/day × 8 hr/day effective ≈ 1.0 m/hr raw, derated to 0.89 m/hr to
  # reflect warping-setup sessions within booking blocks at ~15% of total hours).
  # Annual throughput: 1,792 hr × 0.89 m/hr ≈ 1,595 m/yr → rounded to 1,600.
  # Unit = 1 linear meter of woven cloth equivalent (90–150 cm width; stated per
  # Key Assumptions). [CITATION-NEEDED: floor-loom-8shaft pattern-weave throughput
  # rate; authorial estimate from SCHEMA.md §1 ranges]

  variable_cost_per_unit: 2.25
  # Direct variable cost per meter-equivalent:
  # annual_consumables ($3,600) / throughput_units_equiv_per_year (1,600) = $2.25/m.
  # This reflects per-unit equipment-wear and shared-supplies allocation.
  # Members supply their own fiber; fiber cost is not included here.

  labor_hours_per_unit: 1.12
  # Effective hours/yr (1,792) ÷ throughput_units_equiv_per_year (1,600) = 1.12.
  # Reflects supervisor labor-hours per output-equivalent meter across all active
  # member sessions; consistent with E3-R3 cross-check:
  # 1,600 × 1.12 = 1,792 ≈ effective annual hours.

  downtime_fraction: 0.10
  # Sources: equipment maintenance and first-year failure events (~4%; dobby
  # mechanism failure at ~2,500 hr = year 1.4 under 40 hr/wk, ~7-day lead time);
  # booking-gap and member-scheduling overhead (~3%); administrative and safety
  # incidents (~3%). Total 10%. Professional-user population reduces member-induced
  # damage risk relative to a civic multi-user facility; 10% is conservative relative
  # to forge-004 civic precedent (15%) and appropriate for a professional shared studio.

  lifespan_years: 20
  # Floor-loom-8shaft service life under regular maintenance: manufacturer-quoted
  # 15–30 years for professional-grade equipment; 20 years is the conservative
  # planning horizon appropriate for cooperative capital planning and reflects the
  # higher wear rate of a multi-member shared-use configuration versus single-
  # operator studio ownership. [CITATION-NEEDED: floor-loom-8shaft expected service
  # life; manufacturer documentation or comparable shared-studio operating records]

# ── RESULTS ──────────────────────────────────────────────────────────────────

results:
  village_market:
    verdict: fail
    primary_metric: -1.0
    metric_name: payback_years
    notes: market_price_per_unit absent or zero; entry not designed for market lens
  village_coop:
    verdict: fail
    primary_metric: 119.0
    metric_name: break_even_members
    notes: feasible_pool=31.2, break_even=119, total_annual_cost=23800
  village_civic:
    verdict: fail
    primary_metric: 16.8
    metric_name: per_household_cost
    notes: per_hh=16.80, threshold=120, hrs/capita=0.000 vs threshold=2.0
  town_market:
    verdict: fail
    primary_metric: -1.0
    metric_name: payback_years
    notes: market_price_per_unit absent or zero; entry not designed for market lens
  town_coop:
    verdict: win
    primary_metric: 119.0
    metric_name: break_even_members
    notes: feasible_pool=212.5, break_even=119, total_annual_cost=23800
  town_civic:
    verdict: fail
    primary_metric: 2.4705882352941178
    metric_name: per_household_cost
    notes: per_hh=2.47, threshold=100, hrs/capita=0.000 vs threshold=2.0
  small_city_market:
    verdict: fail
    primary_metric: -1.0
    metric_name: payback_years
    notes: market_price_per_unit absent or zero; entry not designed for market lens
  small_city_coop:
    verdict: win
    primary_metric: 119.0
    metric_name: break_even_members
    notes: feasible_pool=900.0, break_even=119, total_annual_cost=23800
  small_city_civic:
    verdict: fail
    primary_metric: 0.4666666666666667
    metric_name: per_household_cost
    notes: per_hh=0.47, threshold=80, hrs/capita=0.000 vs threshold=2.0
sources:
  - ref: "corpus/program/SCALES.md §3 — small-city-scale skilled-trades median wage and civic facility per-household cost benchmarks"
  - ref: "Ostrom, Elinor. 1990. Governing the Commons. Cambridge University Press — cooperative governance design principles"
  - ref: "Chandler, Deborah. 1995 (rev. 2009). Learning to Weave. Interweave Press — floor-loom throughput ranges, warping overhead, and loom operation fundamentals"
  - ref: "Black, Mary E. 1945 (rev. 1957). The Key to Weaving. Bruce Publishing Co. — 8-shaft loom pattern structures, networked twill, and professional production-weaving technique"
  - ref: "[CITATION-NEEDED: floor-loom-8shaft capital cost — equipment retailer pricing (AVL Looms, Macomber Looms, Schacht Spindle Co., Toika Looms) for professional-grade 8-shaft units, 2024–2025]"
  - ref: "[CITATION-NEEDED: floor-loom-8shaft pattern-weave throughput rates — practitioner-reported or measured meters-per-day for networked twill and 8-shaft pattern work; SCHEMA.md §1 ranges used as authorial estimate]"
  - ref: "[CITATION-NEEDED: professional shared weaving studio consumables and annual maintenance estimate — no published benchmark identified; derived from per-item pricing in weaving supply catalogs (Yarn Barn, WEBS, Halcyon Yarn)]"
  - ref: "[CITATION-NEEDED: light-commercial floor-space rent in small-city arts district 2024–2025; $22/m²/month is an authorial estimate; local market rate should be substituted at implementation]"
  - ref: "[CITATION-NEEDED: floor-loom-8shaft noise level at operator position — acoustic survey or practitioner measurement; 62 dB estimated from comparable floor-loom noise data]"
  - ref: "[CITATION-NEEDED: floor-loom-8shaft expected service life — manufacturer documentation (AVL, Macomber, Schacht); 20-year conservative estimate used pending confirmation]"
  - ref: "[CITATION-NEEDED: arts-council grant amounts for professional shared creative studios in US small cities 2023–2025 — no published survey identified at authoring date]"
  - ref: "[CITATION-NEEDED: master-weaver hourly rate and skilled-artisan tier wage data for small-city markets 2024–2025 — $42,000/yr FTE estimate requires confirmation from practitioner compensation survey]"
  - ref: "Scandinavian textile studio collective model — European shared-studio precedent for professional-tier craft infrastructure; functional inheritance of booking-system governance and equipment-access model [CITATION-NEEDED: primary source on Nordic textile cooperative studio models]"
  - ref: "NYC garment district production cooperative model — functional precedent for shared high-value equipment access in commercial fashion production context [CITATION-NEEDED: academic or trade documentation of NYC garment-district cooperative production models]"
---
## Summary

The Artist-Designer Collaboration Studio (weave-015) is a professional-tier shared floor-loom studio providing equipment access to working artist-weavers and fashion designers who need production-capable 8-shaft floor looms but cannot or will not commit the $25,000–$90,000 required to own and maintain equivalent equipment individually. The studio operates on a member-subscription model: professional weavers and designers pay $1,500–$3,000/yr for booking access to a bank of 4–5 floor-loom-8shaft units, shared warping infrastructure, and climate-controlled workspace. Revenue is member subscriptions supplemented by off-hours equipment rental to non-members. The facility itself produces no commercial output; members' own work — fashion yardage, art textiles, garments, tapestry — remains theirs to sell or license under their own commercial identity. A master-weaver supervisor (fractional FTE, ~0.4) provides equipment-safety oversight and peer-consultation at intake assessment; the studio is not a teaching facility. Governance is cooperative with documented Ostrom-compliant bylaws, skill-based membership admission, digital booking, and a graduated-sanctions framework that includes an IP and attribution clause as a core governance element. Target scale is small city; viable under cooperative lens, marginal under civic, poor under market.

## Design rationale

This entry solves a problem no other entry in the weaving catalog solves: it models the professional-infrastructure case for shared weaving equipment — not community education (weave-010), not a single-operator studio (weave-004), not a heritage preservation program (weave-006 through weave-008). weave-010 (Community Fiber Arts Center) is the entry most superficially similar, but the distinction is precise and commercially significant. weave-010 is a civic multi-user educational facility: its primary output is instruction and supervised open-studio access; its member base is residents of all skill levels; its floor equipment is 4-shaft; its supervisor is a journeyman-weaver. weave-015 is a professional production facility: its output is weaving hours for commercially active weavers and designers; its member base is admitted only upon demonstrated journeyman-level competency; its floor equipment is 8-shaft; its supervisor is a master-weaver assessing technical peers. The cooperative form is also distinct from the market-primary entries (weave-001 through weave-005): those entries model a single-operator studio generating revenue from product sales; this entry generates no commercial output at the facility level and is structured around shared capital access, not shared production revenue. The IP and attribution clause in the membership agreement is the entry's distinctive governance element — it directly names and addresses the primary failure mode for professional collaboration studios (ownership disputes over commercially valuable output that was produced using shared equipment). This failure mode is not named in any other weaving catalog entry.

## Historical lineage

Three precedents inform this design.

**Scandinavian textile studio collective model.** Nordic countries (Sweden, Denmark, Norway, Finland) developed shared professional textile-studio models in the 20th century that combined high-quality shared equipment access with cooperative governance for working artist-weavers. The functional inheritance is: booking-system governance, equipment-access as the primary membership value, professional-tier admission standard, and collective maintenance of capital equipment that no individual member could sustain alone. What the design cannot reproduce: the Nordic model was embedded in a strong artisan-craft cultural tradition with state-backed applied-arts infrastructure (Konstfack, Statens Håndverk og Kunstindustriskole, etc.) that provided institutional legitimacy and cross-subsidy unavailable in the US small-city context. The cooperative governance model and the booking-system operational form are the inheritance; the state-subsidy scaffold and cultural-tradition embeddedness are not.

**NYC garment district production cooperative (20th century).** The New York garment district sustained shared-equipment production models for independent fashion producers through the mid-to-late 20th century, in which small designers accessed specialized cutting, sewing, and finishing equipment under cooperative or rental arrangements that would have been individually unaffordable. The functional inheritance is: the separation between equipment ownership (collective) and commercial output ownership (individual member); the member-as-professional framing (the facility serves working practitioners, not learners); and the commercial-context IP discipline (attribution and brand separation in a commercially active shared workspace). What the design does not inherit: the garment district model depended on geographic concentration (Manhattan) and the density of the fashion industry supply chain; the weaving-studio equivalent in a small city must function with a thinner local professional pool and longer catchment radius.

**European shared printmaking studio (contemporary).** Contemporary shared printmaking studios (Edinburgh Printmakers, Peacock Visual Arts Aberdeen, Lawrence Batley Printmakers) operate on professional-membership models that are a close structural analog to this entry: high-capital specialist equipment (etching presses, screen-printing beds, lithography stones) shared among working artists on subscription-membership terms; master-level technical oversight; IP-separated individual commercial output. The functional inheritance is: the subscription-membership revenue model, the intake skill-assessment gate, the supervisor-as-technical-authority (not instructor) role, and the cooperative governance form with clear IP separation. The printmaking-studio model demonstrates commercial viability of the professional-tier shared-equipment cooperative across several decades in comparable small-city and urban contexts; it is the most direct operational precedent for weave-015.

## Key assumptions

**Capital cost ($25,000–$90,000, mid $55,000):** No published benchmark for a professional shared weaving studio of this configuration was identified at authoring date. The estimate is derived from equipment pricing: floor-loom-8shaft units at $5,000–$15,000 each (new professional-grade: Macomber B4, Schacht Mighty Wolf 8-shaft, AVL production dobby) × 4–5 units = $20,000–$75,000; warping equipment (sectional warping mill, paddle warping frame) = $800–$2,500; humidity-control HVAC = $1,500–$8,000; studio lighting and fit-out = $2,000–$8,000. The mid estimate ($55,000) reflects 4–5 mid-grade new looms with commercial humidity management and professional lighting. The range is wide because 8-shaft loom quality varies substantially between mid-grade production looms and high-end AVL or Toika units. All figures flagged [CITATION-NEEDED]; equipment procurement quotes required before status promotion.

**Revenue model (not reflected in sim_params):** Member subscriptions at $1,500–$3,000/yr × 15–20 active members = $22,500–$60,000/yr; off-hours rental at $25–$50/hr × 200 hr/yr (conservative estimate for off-peak access) = $5,000–$10,000/yr; total facility revenue $27,500–$70,000/yr. Mid-scenario: 18 members × $2,250/yr avg = $40,500 + $7,500 rental = $48,000/yr. Annual operating costs: supervisor ($16,800 at 0.4 FTE) + maintenance ($2,800) + consumables ($3,600) + rent ($14,400) = $37,600/yr. Mid-scenario operating surplus ~$10,400/yr before capital amortization. Capital amortization (20-yr lifespan on $60,000 mid-capital + install): ~$3,000/yr. Net feasibility: positive at mid-scenario. Margin is thin; the coop is financially sensitive to member count falling below 12–14 active members. This revenue model is the author's estimate; all figures flagged [CITATION-NEEDED].

**Throughput unit (1,600 m/yr):** The throughput metric for this entry is equipment-utilization hours converted to woven-meter equivalents; it does not represent the commercial output of member work (which is theirs). The 0.89 m/hr blended rate for pattern-complexity work on an 8-shaft floor loom reflects a conservative estimate derived from SCHEMA.md §1 ranges (1–3 m/day for pattern weave at 8 hr/day = 0.125–0.375 m/hr; 8 m/day facility-wide across 4 active looms = 2 m/day/loom average; at 8 hr effective production = 0.25 m/hr per loom raw, or ~1.0 m/hr facility-wide). The derivation is internally consistent but requires practitioner-reported data for validation.

**Downtime fraction (0.10):** Lower than the civic multi-user facility (0.13) because professional members are less likely to mishandle equipment and less likely to leave loom bays in poor condition. The dobby-mechanism failure (14-day lead time at ~2,500 hr) contributes the largest single downtime event; the humidifier failure (10-day lead time at ~2,800 hr) is secondary. 10% is defensible given the professional-use population but is an authorial estimate pending comparable shared-studio operating data.

## Known risks / failure modes

**Regulatory.** The primary regulatory risk is the membership agreement and IP-attribution clause: in the absence of a well-drafted cooperative operating agreement, commercial-output attribution disputes between members (who produced the piece, whose design, whose IP if the designer provided a commission draft and the weaver executed it) are a documented failure mode for professional collaboration studios. Standard cooperative bylaws do not contain an IP and attribution clause; it must be custom-drafted by a lawyer familiar with craft and design practice. A secondary regulatory risk is the structural load capacity of the building: floor-loom-8shaft units weigh 150–250 kg each; five looms plus beamed warps in a concentrated bay layout can approach 1,500 kg. A building designed for office use may not have adequate floor loading; structural assessment is required before signing a lease. Building permit for humidity-control HVAC is routine but must be obtained.

**Labour pipeline.** The master-weaver supervisor position is the cooperative's single point of failure for quality, safety, and member intake assessment. The master-weaver competency pool nationally is thin and disproportionately concentrated in large metro areas. The fractional nature of the role (0.4 FTE, ~$16,800/yr) makes it attractive only to a working professional weaver who values studio access over compensation; at the point where such a person retires, relocates, or increases their own production load, the cooperative faces a difficult replacement search. There is no apprentice pipeline to mitigate this risk (`apprentice_friendly: false`). The cooperative should document the intake-assessment protocol in enough procedural detail that a newly hired master-weaver can execute it consistently without depending on the departing supervisor's tacit judgment. A secondary labour risk is the minimum-viable-membership threshold: below 10–12 active members, the cooperative's financial model does not cover fixed costs; member attrition for reasons unrelated to the studio (members relocating, retiring, pivoting careers) is a systemic risk that governance cannot fully prevent.

**Supply chain.** The studio's supply chains for consumables (heddles, reeds, dobby pegs, tie-up cord) are serviceable but not commodity: weaving supplies from US distributors have 7-day typical lead times but 28-day worst-case for specialty 8-shaft dobby components or non-standard reeds. A modest safety-stock policy for critical consumables (one replacement heddle set per loom per shaft, spare reed sets in the two most common sett configurations used by members) is essential. The humidity-control system is a secondary supply-chain concern: commercial HVAC components can have 10–28-day lead times; a portable backup humidifier unit ($200–$400) provides continuity during repair and should be kept in the studio. The primary upstream supply-chain risk sits with members, not the facility: members source their own fiber, and a member whose specialty-yarn supplier fails or raises prices significantly will either reduce their studio use (reducing cooperative revenue) or request fiber-stock support from the cooperative (creating a capital and storage commitment outside the studio's design scope). The membership agreement should explicitly exclude fiber-sourcing as a cooperative obligation.

## Iteration log

- 2026-04-18: v0.1 — initial creation; weave-015 Artist-Designer Collaboration Studio. Professional-tier shared floor-loom cooperative per Plan I Task 17 specification. COOPERATIVE-PRIMARY / CIVIC-MARGINAL entry. All lens_context blocks populated (market poor; cooperative good with all required Ostrom fields, IP/attribution clause as defining governance element, Principle 8 named as only partially addressed; civic marginal with staffing_model, benchmark_comparison, two civic_externalities). `apprentice_friendly: false` with succession risk named in Known Risks. Anti-romantic framing applied throughout: this is professional production infrastructure, not a craft-revival gesture; members are commercially active professionals, not community learners. Thirteen [CITATION-NEEDED] flags placed over fabricated estimates for capital cost, throughput rates, consumables, wages, rental rates, and historical lineage sources. Explicit differentiation from weave-010 (Community Fiber Arts Center) in Design rationale: professional vs. community-education model, 8-shaft vs. 4-shaft, master-weaver vs. journeyman supervisor, commercial-output vs. civic-access orientation.
