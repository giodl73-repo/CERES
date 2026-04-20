---
facility_type: Type-A-heavy
trade: artisan-square
trades_served: [smithing, metalwork, pottery-kiln]
status: draft
version: "1.0"
review_status: {panel: pending, editorial: pending}
sources_count: 14
---

# Artisan Square — Type A Heavy-Trades Facility Research

## 1. Facility Context

A Type A studio in Artisan Square is a dedicated, individually rented production space for heavy trades: forge-based metalwork, bladesmith and ornamental ironwork, and pottery with kiln firing. "Type A" designates the wing whose infrastructure — floor loading, exhaust, electrical, fire suppression — must meet light-manufacturing code rather than the lighter commissary or fiber-arts standard of Type B.

Tenants are journeyman smiths, metalwork artists, bladesmiths, production potters, and ceramic artists operating as independent businesses at sub-commercial scale. These are the practitioners who appear in the CERES smithing and metalwork catalog as market-path or specialty-path winners — not hobbyists, and not industrial employees.

The structural distinction from a makerspace is exclusive-occupancy. A makerspace sells floor-time access to shared equipment. A Type A studio is dedicated: the tenant controls it around the clock, stores work-in-progress there, and operates on their own schedule. No shared floor-time, no equipment sign-up. This distinction has regulatory, insurance, and economic consequences that cannot be elided.

The governing IBC occupancy classification is Group F-2 (light manufacturing), not Group B (business). F-2 carries implications for fire suppression, occupancy load, noise ordinance exposure, and zoning eligibility. Both Artisan Square wings operate under a Section 508 Mixed Use Protected analysis; the Type A wing holds the F-2 classification.

---

## 2. The Forge and Metalwork Studio

Physical requirements per studio, derived from Artisan Square design spec §4.3:

**Floor:** Concrete slab, 150 lb/sq ft rated. Anvil-stand loads and leg-vise anchor bolts exceed wood-frame floor capacity; 150 lb/sq ft is the practical minimum, not aspirational.

**Ceiling:** 14 ft clearance minimum for long-stock manipulation (bar stock, billet, tube rotation). 16 ft preferred in purpose-built configurations.

**Electrical:** 200A 3-phase sub-panel with individual metering. A 10 kW induction forge on single-phase at 240V draws approximately 42A; the same load on 208V 3-phase draws approximately 28A per leg. 3-phase provides headroom without up-sizing wire runs and distributes concurrent studio loads across phases. Individual metering is operationally required: metalwork power bills are high and opaque apportionment drives tenant disputes.

**Exhaust:** 2,000 CFM minimum stub at shared industrial riser per studio. Both combustion forges (CO) and induction forges (metal oxide fumes during flux-welding) require capture-at-source exhaust. The Type A stack must be maintained separately from the Type B food-grade stack — health department licensing prohibits co-mingling.

**Sound isolation:** STC 55+ demising walls. A hammer-on-anvil strike produces approximately 100 dB at one meter [CITATION-NEEDED: measured noise level at one meter for typical blacksmith hammer-on-anvil strike, occupational-acoustics source]. STC 55 reduces adjacent-studio transmission to approximately 45 dB — within OSHA 8-hour TWA limits.

**Eye-wash station:** Required by OSHA 29 CFR 1910.151 for corrosive-material exposure environments [CITATION-NEEDED: OSHA 29 CFR 1910.151 — confirm applicability to commercial lease context vs. direct employer]. Relevant hazards: flying scale, quench splash, flux spattering.

A Type A tenant leasing this studio receives infrastructure that costs $80–150k to install at Location 1, amortized across the wing. A standalone commercial tenant absorbs that full cost plus the engineering and permitting risk of an F-2 forge application in a jurisdiction that may never have processed one.

**Benchmark — Artisans Asylum Boston:** Artisans Asylum (Somerville, MA) offers tiered metalwork shop membership ($45–75/month) with no dedicated studio tenancy option for heavy metalwork [CITATION-NEEDED: Artisans Asylum Boston current membership tiers — confirm from artisansasylum.com]. The absence of dedicated F-2 forge studios at Artisans Asylum is structural: the code and liability complexity of individually metered forge studios under one roof has not been resolved at scale. Artisan Square addresses this gap by design.

---

## 3. The Pottery and Kiln Studio

### Physical Requirements

Pottery and kiln studios share the Type A wing classification with forge studios — both are F-2 occupancy, both require industrial-grade exhaust — but their physical requirements differ materially from the forge.

**Floor reinforcement:** An electric kiln in the 7–10 cubic foot range weighs 400–600 lbs loaded. A gas-fired car kiln or catenary arch kiln can exceed 1,000 lbs. The 150 lb/sq ft general floor rating handles distributed loads but does not address localized point loading from kiln feet. A kiln pad — a reinforced concrete pad poured on the slab, typically 4–6 inches over the base slab — is required at the kiln location to distribute point load and to provide a fire-rated surface [CITATION-NEEDED: structural engineering reference for kiln pad design — point load distribution requirements for electric kiln on concrete slab].

**Ventilation (separate circuit):** Kiln exhaust has a different chemical profile from forge exhaust. Electric kiln firing releases organic binder burnoff (in the early stages of firing), sulfur compounds from certain clay bodies, and carbon dioxide. Gas kiln firing produces combustion byproducts including carbon monoxide and nitrogen oxides. Clay dust — airborne during clay preparation and trimming — is a silica-exposure hazard (OSHA PEL: 50 micrograms/m³ respirable crystalline silica, 8-hr TWA [CITATION-NEEDED: OSHA silica PEL reference, 29 CFR 1910.1053 or equivalent]). The pottery studio ventilation circuit must handle both the dust-mitigation function (low-velocity capture at clay-work stations) and the kiln-exhaust function (high-temperature flue from kiln top). These differ enough in design that a single exhaust circuit cannot serve both well; purpose-built pottery studios typically run separate ductwork for clay-preparation areas and kiln exhausts.

**Electrical:** 240V 50A minimum for electric kilns in the 7–10 cubic foot range. Larger production kilns (18+ cubic feet) require 240V 60A or dedicated 240V 100A circuits. The Type A sub-panel (200A 3-phase) has sufficient capacity to serve both kiln circuits and studio lighting and equipment if sized correctly in the sub-panel design; this is not an afterthought — the electrician designing the sub-panel must know the kiln model before sizing breakers.

**Gas kiln option:** Production potters often prefer gas-fired kilns for thermal consistency and reduction firing atmospheres — surface qualities electric kilns cannot replicate and that the specialty ceramics market recognizes. Gas kilns require a propane or natural gas line and harder permitting (fire marshal review, pressure testing, combustion air calculations add 4–8 weeks [CITATION-NEEDED: permitting timeline difference for gas vs. electric kiln in US commercial building — fire code source or contractor experience]). The Artisan Square base design provides an electric-kiln stub; gas kiln is a per-studio upgrade. The operator should not foreclose gas-kiln tenants but should not assume gas capability at base build-out cost.

**Dedicated studio vs. shared kiln:** A production ceramicist fires one to three times per week on a schedule tied to drying time and customer orders. A shared kiln with four to six users cannot accommodate that cadence. The dedicated studio with tenant-owned kiln is the operational prerequisite for a production business, not a luxury option.

---

## 4. Type A Shared Infrastructure

**Industrial exhaust stack:** The vertical exhaust chase from studio level to roofline must be 2-hour fire-rated construction — required for any duct penetrating a fire-rated assembly in F-2 occupancy [CITATION-NEEDED: IBC Section 717 or equivalent — fire-rated duct and chase requirements for F-2 occupancy]. Each studio connection is controlled by a motorized fire damper that closes when the studio is unoccupied, preventing backdraft from the active main riser. Dampers require annual inspection.

**Makeup air:** Combustion forges and gas kilns consume oxygen. Without makeup air, a sealed studio will degrade ambient O₂ below OSHA's 19.5% deficiency threshold [CITATION-NEEDED: OSHA oxygen deficiency threshold and makeup-air guidance for combustion operations in enclosed commercial spaces]. The makeup air unit delivers 80–90% of exhaust volume in tempered outdoor air. The system must be designed for combustion tenants regardless of whether Day 1 tenants run induction forges only.

**3-phase electrical rationale:** The argument for 3-phase is headroom and flexibility, not code mandate. 3-phase delivers the same kilowatts at lower amperage per conductor than single-phase; a 3-phase sub-panel serves single-phase equipment from any leg, but the reverse — running 3-phase equipment from a single-phase panel — is not possible. The Artisan Square main service (1,000A 3-phase) is deliberately over-built: electrical service upgrades to an occupied building are extremely disruptive, and the cost delta at initial installation is modest.

**Fire suppression:** NFPA 13 wet-pipe throughout. Standard sprinkler heads activate at approximately 155°F (68°C); kiln exteriors during cone 10 firing can reach 250°F at proximity [CITATION-NEEDED: surface temperature of standard 7–10 cu ft electric kiln exterior during cone 10 firing — manufacturer spec or safety data]. Pottery studios require high-temperature-rated heads (212°F+) positioned clear of the kiln. Class D metals (magnesium, titanium, zirconium powders) require a lease pre-approval clause rather than suppression-system accommodation — a fire suppression system designed for Class D metals is not compatible with a general metalwork tenancy.

---

## 5. Tenant Economics from the Operator's Perspective

The Artisan Square design spec (§5.3) sets Type A rents at $1,300–2,400/month for 300–350 sq ft studios (~$52–96/sq ft/year). This is above raw light-industrial market rate but below the infrastructure cost the tenant would absorb standalone.

Comparable: East End Maker Hub (Houston, TX) heavy-fabrication studio rates run $18–28/sq ft/year for raw industrial space without the metered 3-phase, exhaust, and compliance overhead [CITATION-NEEDED: East End Maker Hub current studio rates — confirm from eastendmakerhub.com or direct contact]. The Artisan Square premium is the infrastructure stack. Artisans Asylum Boston shared metalwork membership at $45–75/month provides shop access but not exclusive occupancy — a production business cannot operate on shared-access terms, making the dedicated studio at $1,500–2,400/month a functional requirement, not a premium option.

**Occupancy risk:** The Type A tenant pool is smaller than Type B. A suburban market's population of journeyman-level metalwork and pottery practitioners operating as independent businesses — not hobbyists, not industrial employees — is thin. The Artisan Square response: the anchor training studio produces the next cohort over 3–4 year cycles; the graduation path creates referral networks filling vacancies; and the Type A wing is sized conservatively at 6–8 studios rather than maximized.

---

## 6. Operator Risks Specific to Type A

**Zoning:** F-2 light manufacturing requires industrial or mixed-use zoning. Urban land-use trends have progressively rezoned former industrial parcels to residential or commercial use, shrinking the supply of F-2-eligible sites in desirable locations. Suburban adaptive-reuse targets (Location 1) carry lower zoning risk than urban infill; urban locations are feasible but require more permitting effort and higher land cost.

**Noise ordinance:** Power-hammer operations produce impulse noise in the 95–110 dB range at the operator position [CITATION-NEEDED: measured SPL for power hammer and hand hammer in a commercial metalwork studio — NIOSH or occupational-health source]. STC 55+ demising walls protect adjacent tenants, but the exterior noise ordinance is a separate compliance obligation. If the building's exterior envelope does not attenuate to municipal limits (typically 60–65 dBA daytime at property line for light-industrial zones [CITATION-NEEDED: representative municipal noise ordinance dBA limit for light-industrial daytime — cite a specific ordinance, Houston or equivalent]), the operator faces enforcement risk. The compliance playbook must include an exterior noise analysis for any Type A studio running power-hammer equipment; the lease should restrict high-impulse operations to daytime hours (7 AM–8 PM) without a specific variance.

**Safety certification clause:** Type A leases must require documented safety training as a lease condition prior to studio key delivery — not an employment clause, but parallel to the commissary compliance clause for Type B food tenants. For metalwork tenants: completion of an ABANA-affiliated forge safety course or equivalent [CITATION-NEEDED: ABANA forge safety course structure and affiliate network — confirm from artisanblacksmith.org]. For pottery tenants: documented kiln operation certification. The operator is not certifying craft skill, but is documenting that the tenant can operate exhaust, fire suppression, and emergency shutoff systems — a liability and insurance prerequisite.

---

## 7. Functional Requirements Learned

The following requirements, abstracted from Type A heavy-trades facility research, feed REQUIREMENTS.md for the artisan-square trade entry. Each is phrased as a discrete, numeric requirement.

| ID | Requirement | Target | Rationale |
|---|---|---|---|
| R-01 | Floor load rating | 150 lb/sq ft minimum (general); kiln pad to point-load spec | Anvil stands, equipment, kiln loading |
| R-02 | Ceiling clearance | 14 ft minimum | Long-stock manipulation, equipment dolly clearance |
| R-03 | Electrical power density | 200A 3-phase sub-panel per studio; minimum 57 kW available per studio at 208V | Concurrent induction forge + kiln + lighting loads |
| R-04 | Individual tenant metering | Required per studio | High-variance power consumption; cost transparency |
| R-05 | Exhaust capacity | ≥2,000 CFM per studio at industrial exhaust riser connection | Combustion and metal-oxide fume capture |
| R-06 | Makeup air provision | 80–90% of exhaust volume in tempered outdoor air | Combustion oxygen replacement; OSHA compliance |
| R-07 | Exhaust chase fire rating | 2-hour fire-rated vertical chase from studio to roofline | IBC requirement for F-2 occupancy |
| R-08 | Sound attenuation | STC 55+ demising walls (tenant-to-tenant) | Forge hammer impulse noise isolation |
| R-09 | Fire suppression class | NFPA 13 wet-pipe; high-temp heads in kiln proximity | F-2 occupancy; kiln surface temperature |
| R-10 | Occupancy classification | IBC Group F-2 light manufacturing | Regulatory classification for forge and kiln occupancy |
| R-11 | Kiln ventilation circuit | Separate from general metalwork exhaust; clay-dust capture at workstation level | Silica exposure control; chemical profile mismatch with forge exhaust |
| R-12 | Safety certification clause | Lease condition: documented forge or kiln safety training prior to studio occupancy | Liability control; emergency system familiarity |

---

## 8. Sources

1. Artisan Square Design Specification, §4.3 (Type A Studio Infrastructure) and §5.3 (Rent Ranges). Giovanni Della-Libera + Claude Sonnet 4.6. 2026-04-19. [Internal — direct source for physical specs cited throughout]
2. International Building Code (IBC), Section 508: Mixed Use and Occupancy. [CITATION-NEEDED: specific IBC edition year — 2021 or 2024 edition; confirm Section 508 citation for Mixed Use Protected analysis]
3. International Building Code (IBC), Group F-2 (Light Industrial Manufacturing) occupancy classification. [CITATION-NEEDED: IBC Group F-2 definition and requirements — confirm edition and section number]
4. NFPA 13: Standard for the Installation of Sprinkler Systems. [CITATION-NEEDED: NFPA 13 edition year; confirm applicability to F-2 metalwork occupancy and Class D guidance]
5. OSHA 29 CFR 1910.151: First Aid (eye-wash station requirement for corrosive-material exposure environments). [CITATION-NEEDED: confirm applicability to commercial lease (non-employer-employee) context — does OSHA 1910 apply to tenant-operator relationship or only direct employer]
6. OSHA 29 CFR 1910.1053: Respirable Crystalline Silica standard. PEL 50 micrograms/m³ 8-hr TWA. [CITATION-NEEDED: confirm this is the correct citation for general industry silica PEL as applied to pottery studio clay preparation]
7. OSHA Oxygen Deficiency guidance (below 19.5% O2): applicable to combustion forge operations in enclosed commercial spaces. [CITATION-NEEDED: specific OSHA document number for oxygen-deficiency threshold in combustion-equipment contexts]
8. Artisans Asylum, Somerville MA. Membership tiers and metalwork shop access. [CITATION-NEEDED: current pricing from artisansasylum.com — figures $45–75/month shared shop membership cited as of available data; confirm current]
9. East End Maker Hub, Houston TX. Heavy-fabrication studio rental rates. [CITATION-NEEDED: current rates from eastendmakerhub.com or direct contact — figures $18–28/sq ft/year cited; confirm current]
10. ABANA (Artist Blacksmiths Association of North America). Forge safety course structure and affiliate network. [CITATION-NEEDED: confirm ABANA affiliate safety course model — artisanblacksmith.org or contact ABANA directly]
11. IBC Section 717 (or current equivalent): Fire-rated duct and chase construction requirements for F-2 occupancy. [CITATION-NEEDED: confirm current IBC section for fire-rated duct penetration requirements]
12. Noise level at operator position for power hammer and hand hammer metalwork operations. [CITATION-NEEDED: NIOSH or peer-reviewed occupational-health measurement of forge hammer SPL at operator position — recommend NIOSH Hazard ID series or equivalent]
13. Kiln surface temperature during high-fire (cone 10) electric kiln firing. [CITATION-NEEDED: manufacturer safety data or independent test data for exterior surface temperature of standard 7–10 cubic foot electric kiln during cone 10 firing]
14. Municipal noise ordinance daytime dBA limits for light-industrial zone: representative jurisdiction example required. [CITATION-NEEDED: cite a specific municipal ordinance dBA limit for light-industrial zone daytime operations — varies by jurisdiction; Houston, Austin, or comparable suburban US market preferred for consistency with East End Maker Hub benchmark]
