---
id: plan-b-research-smithing
name: Research Corpus — Smithing Vertical Slice
description: Historical functional-requirements research for smithing across 4 anchor cultures, plus cross-cultural synthesis and decline verdict
status: completed
version: "1.1"
created: 2026-04-19
completed: 2026-04-19
last_modified: 2026-04-19
phase: 1
subsystem: research-corpus
trade: smithing
depends_on: [plan-a-scaffolding]
blocks: [plan-c-catalog-smithing]
estimated_effort: 2-3 weeks focused, 4-6 weeks part-time
primary_artifact_type: research
success_signal: >
  Research for smithing captures authentic historical functional requirements
  across 4 anchor cultures with serious economic-history and archaeology
  sources, an explicit decline-or-restructuring verdict per spec v0.3 §4.1,
  and a cross-cultural synthesis that gives Plan C catalog authors a
  defensible, anti-romantic functional specification. P-5 Historian review
  passes without P1 findings.
spec: specs/2026-04-18-ceres-design.md
---

# Plan B: Research Corpus — Smithing Vertical Slice

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Produce the historical research foundation that Plan C's catalog authoring depends on. Extract functional requirements from historical forms of smithing across 4 anchor cultures, synthesize cross-cultural patterns, and deliver an anti-romantic decline-or-restructuring verdict.

**Architecture:** Research-heavy authoring plan. Deliverables are markdown documents grounded in economic history, archaeology, and metallurgy. Each cultural chapter is substantive (~1500–2500 words). Synthesis documents compress patterns across cultures into the functional spec Plan C will consume.

**Tech Stack:** Markdown, YAML frontmatter. No code.

**Source of truth:** `specs/2026-04-18-ceres-design.md` (v0.3), especially:
- Section 2 (Working Hypothesis + 4 falsifiers — the research must test, not assume)
- Section 3 (anchor-culture scope: 4–6; this plan covers 4 of the 6)
- Section 4.1 (Phase 1 research requires `decline_or_restructuring_verdict` per trade)
- Section 13 (non-goals — anti-romanticism, not a political manifesto)

**Source quality bar:** `docs/METHODOLOGY.md` Section 5 (historical claims must cite serious economic-history or primary-source literature; Wikipedia-only citations are P1 for load-bearing claims). `docs/STYLE-GUIDE.md` Section 4 (forbidden framings: no "good old days", no implicit sustainability assumption, no labor-regime elision, no guild-as-craft-quality-only framing, no "lost knowledge" claims without documentation).

**Citation policy (this plan):** Use **bracketed-placeholder citations** in the form `[CITATION-NEEDED: <specific-claim>]` where a load-bearing claim needs a source the implementer is not highly confident exists. Prefer broadly-known works (Mokyr, Braudel, Thompson, Pomeranz, Ogilvie, Epstein, etc.) where model confidence is high. The author will verify and replace placeholders in a final pass before any chapter is promoted to `validated`. Inventing plausible-sounding citations is a P1 integrity failure.

**Anchor cultures (this plan, 4 of 6):**
- Medieval Northern Europe (ca. 1100–1500)
- Song-era China (ca. 960–1279)
- Tokugawa Japan (ca. 1603–1867)
- American frontier (ca. 1790–1890, trans-Appalachian + trans-Mississippi)

Andean ayllu and Islamic Golden Age are deferred to a later plan; the corpus structure supports slotting them in without re-architecture.

**Commit cadence:** One commit per task. Keeps history legible and allows Plan C to reference specific research commits when building catalog entries.

---

## Task Index

| # | Task | Creates |
|---|---|---|
| 1 | Medieval Northern Europe smithing | `research/cultures/medieval-northern-europe/smithing.md` |
| 2 | Song-era China smithing | `research/cultures/song-china/smithing.md` |
| 3 | Tokugawa Japan smithing | `research/cultures/tokugawa-japan/smithing.md` |
| 4 | American frontier smithing | `research/cultures/american-frontier/smithing.md` |
| 5 | Cross-cultural functional requirements | `research/trades/smithing/REQUIREMENTS.md` |
| 6 | Comparative historical forms | `research/trades/smithing/HISTORICAL-FORMS.md` |
| 7 | Decline-or-restructuring verdict | `research/trades/smithing/DECLINE-VERDICT.md` |
| 8 | Consolidated bibliography | `research/trades/smithing/SOURCES.md` |
| 9 | Closeout: TRACKER + plans/README + frontmatter | (updates only) |

Per-task structure: outline → draft chapter → anti-romanticism self-review → placeholder-citation audit → commit.

---

## Per-Cultural-Chapter Outline (Tasks 1–4)

Every cultural chapter MUST follow the same outline so cross-cultural synthesis is possible in Tasks 5–6. Variation in depth per section is fine; section omission is not.

### Required Sections

1. **Frontmatter** (YAML):
   ```yaml
   ---
   culture: {medieval-northern-europe | song-china | tokugawa-japan | american-frontier}
   trade: smithing
   period: {rough era with dates}
   geography: {regional scope}
   status: draft
   version: "1.0"
   review_status: {panel: pending, editorial: pending}
   sources_count: {integer}
   ---
   ```

2. **Period and Geography** (~100–200 words) — the era, the physical region, the economic system in broad strokes. Enough context that a reader unfamiliar with this culture can follow the rest.

3. **The Smith's Place** (~200–350 words) — who were smiths? How did they enter the trade? What was their household and social position? Were they also farmers (a common reality, per P-5's framing)? Their legal / guild / caste status.

4. **The Forge** (~250–400 words) — physical form. Construction, size, ventilation. Fuel: wood, charcoal, coal, coke. The bellows mechanism. The anvil. Hammers and tongs. Any auxiliary tools (drop hammers, trip hammers, water-powered forges, treadle bellows). Photographs/diagrams are fine but not required.

5. **Products** (~150–300 words) — what was made. Tools, nails, horseshoes, hardware, weapons, ornamental work, repair. Approximate scale (units per day or per year for a representative smith). Who the customers were.

6. **Labor Regime** (~200–350 words) — apprentices: recruitment, duration, obligations. Household labor: family members, spouses, servants. Guild structures where applicable (Europe especially). Journeyman mobility. Master's authority. This section MUST explicitly address the labor regime the historical form depended on — per spec v0.2 falsifier: "labor-regime dependency."

7. **Supply Chain** (~150–300 words) — iron/steel source (local bog iron, imported bar iron, merchant blacksmiths, domestic production). Fuel supply (forest management, coal trade, charcoal burners). Customer demand structure (village, regional market, state commissions). Did the smith depend on supply chains that cannot be reconstituted today? (per spec falsifier: "supply-chain disappearance.")

8. **Decline or Restructuring** (~200–400 words) — what happened to this form of smithing when industrialization arrived, or when the culture's political/economic structure changed? Did the trade vanish, migrate, specialize, consolidate? This is where the chapter directly feeds Task 7 (DECLINE-VERDICT.md) — make the verdict claim explicit.

9. **Functional Requirements Learned** (~150–300 words) — abstract from this culture's forge(s) what a forge MUST do, expressed in trade-agnostic terms: temperature range, throughput envelope, fuel flexibility, operator skill floor, footprint, supply-chain dependencies. These are the inputs to Task 5 (REQUIREMENTS.md).

10. **Sources** (numbered list) — all citations consolidated at the end. Bracketed placeholders are fine.

### Style Rules

- **No "good old days" framing.** STYLE-GUIDE.md §4.1.
- **No implicit sustainability assumption** (e.g., "local and sustainable by modern standards"). STYLE-GUIDE §4.2.
- **No labor-regime elision.** Household labor, apprentice servitude, and customary obligations MUST be named as material conditions. §4.3.
- **No guild-as-craft-quality-only framing.** Guilds protected members from competition as much as (or more than) they policed quality. §4.4.
- **No "lost knowledge" claims without specific documentation.** §4.5.
- **Write in third person, past tense, neutral voice.** No "the noble smith." No "the humble village forge." Description over romance.
- **Every load-bearing claim has a citation** (real or bracketed placeholder). METHODOLOGY.md §5.

### Anti-Romanticism Self-Review Checklist

Before committing each cultural chapter, the implementer runs this checklist:

- [ ] No phrase matching the forbidden list in STYLE-GUIDE §4.1 appears anywhere.
- [ ] The labor regime is explicitly described (who did the work, under what obligations).
- [ ] The forge is described as it actually was, including unpleasant or difficult aspects (heat, smoke, injury, noise, seasonal work).
- [ ] "Decline" language distinguishes actual decline from restructuring/specialization/migration.
- [ ] Citations are present for every load-bearing claim. Uncited claims are bracketed `[CITATION-NEEDED: ...]`.
- [ ] Word count is roughly 1500–2500. Substantially less is likely thin; substantially more is likely bloat.

---

### Task 1: Medieval Northern Europe Smithing

**Files:**
- Create: `research/cultures/medieval-northern-europe/smithing.md`

**Focus points for this culture:**
- Period: high medieval (~1100–1500). Regional scope: England, northern France, Low Countries, Rhineland, Baltic. Distinguish from Mediterranean (different supply chains, fuel, guild structures).
- The smith as village craftsman AND as townsman: the rural blacksmith serving peasant agriculture vs. the urban smith in a guild town. These are materially different economic positions.
- Fuel: charcoal dominant; forest management as load-bearing supply chain. Bloomery iron vs. imported Swedish/Styrian bar iron.
- Guild structures (mature by 1200s in German and Flemish towns): admission fees, apprenticeship duration, mobility (journeyman's years).
- Products: horseshoes, plowshares, nails, tools, hinges, chains. Weapons and armor by specialized smiths (armorer's guild), not the village smith.
- Household labor: the smith's wife and children as load-bearing labor; de Vries on household economies relevant.
- Decline: actually restructuring — rural smithies persisted well into the 19th century; what declined was the guild-town smith as scale manufacturing of nails, tools, and hardware centralized in workshops (then factories).
- Load-bearing authors to cite confidently: Sheilagh Ogilvie on guilds; S.R. Epstein on craft economics; Jan de Vries on household economies; Joel Mokyr on industrialization.

**Source consultation (implementer reads if available):**
- `docs/STYLE-GUIDE.md` §4 (forbidden framings)
- `docs/METHODOLOGY.md` §5 (historical-claim source standards)
- `corpus/canon/THEORY.md` §6 (function-vs-form distinction)
- `.roles/panel/P-5-historian.md` (the voice that will review this)
- Reference material: `reference\archaeology\`, `reference\architecture-history\`, `reference\cartography\` as relevant — cite them as `[MAXIM: <topic>]` when drawing from there.

**Commit:**
```bash
git add research/cultures/medieval-northern-europe/smithing.md
git commit -m "Plan B task 1: medieval Northern Europe smithing chapter"
```

---

### Task 2: Song-Era China Smithing

**Files:**
- Create: `research/cultures/song-china/smithing.md`

**Focus points for this culture:**
- Period: Song dynasty (960–1279). Key distinction: pre-modern China produced iron at a scale not matched in Europe until the 18th century. This matters — it breaks the Western default that "industrial" = "post-1800."
- Fuel transition: charcoal to coal/coke use in iron production predates Europe by centuries (Hartwell's work is foundational). Supply-chain and environmental implications.
- Organizational form: large-scale state-managed and merchant-managed ironworks alongside village smithies. Multiple coexisting scales — not a simple "local craft vs industrial" dichotomy.
- Products: agricultural tools (iron plowshares distributed by the state to improve rice-paddy productivity), weapons, coinage infrastructure, cast iron cookware, nails.
- Labor: a mix of corvée labor, state workers, hired workers, household workshops. The labor regime differs sharply from European guild apprenticeship.
- "Decline": the post-Song iron industry contracted after Mongol disruption; rebuilt under Ming but at smaller scale. Was this decline, displacement, or demand collapse? Hartwell argues demand collapse related to Mongol devastation and subsequent state policy changes — NOT technological failure.
- Load-bearing authors: Robert Hartwell (iron-industry paper, 1960s, foundational); Mark Elvin on Chinese economic history; Kenneth Pomeranz on comparative economic history (Great Divergence).

**Commit:**
```bash
git add research/cultures/song-china/smithing.md
git commit -m "Plan B task 2: Song-era China smithing chapter"
```

---

### Task 3: Tokugawa Japan Smithing

**Files:**
- Create: `research/cultures/tokugawa-japan/smithing.md`

**Focus points for this culture:**
- Period: Tokugawa / Edo (1603–1867). Socially stratified (samurai / farmer / craftsman / merchant), with the craftsman a formal estate (*shokunin*).
- Two streams of smithing worth distinguishing:
  1. **Sword smiths** (*katana-kaji*) — highly specialized, ritualized, tied to samurai class; represented a prestige craft. NOT the everyday smithing the catalog targets. Useful for contrast.
  2. **Utility smiths** — village smiths, castle-town craftsmen producing tools, nails, farm equipment, tools for carpentry (Japanese carpentry tools are a world of their own).
- Fuel: charcoal primary, with highly specialized *tamahagane* production for swords. Coal use minimal.
- Forge form: traditional Japanese forge with box bellows (*fuigo*) distinct from European bellows design.
- Labor: master-apprentice within the *shokunin* estate, with recognized master lineages. More formalized than European rural smithing, less corporate than European guild smithing.
- Supply chain: regional specialization (iron sand from specific regions, steel trade controlled by castle-town merchants).
- Decline: Meiji Restoration (1868) ended the *shokunin* system's legal basis. Industrial metallurgy displaced traditional smithing for commodity production but prestige sword-making persists as a licensed, regulated art form today — an interesting case of regulatory preservation. Anti-romantic reading: much commodity smithing DID vanish; what survived was the culturally prestigious subset.
- Load-bearing authors: Leupp on Japanese craft labor; Morris-Suzuki on Japanese economic history; Hanley on early modern Japanese standards of living.

**Commit:**
```bash
git add research/cultures/tokugawa-japan/smithing.md
git commit -m "Plan B task 3: Tokugawa Japan smithing chapter"
```

---

### Task 4: American Frontier Smithing

**Files:**
- Create: `research/cultures/american-frontier/smithing.md`

**Focus points for this culture:**
- Period: ca. 1790–1890, trans-Appalachian frontier moving west across the Mississippi and Great Plains. Intentionally post-industrial-revolution — this is the test case for "what does rural smithing look like when industrial production already exists and competes."
- Organizational form: independent proprietor, typically a single smith with household labor; no guilds (anti-monopoly ethos of American labor); apprentices but less formal.
- Fuel: charcoal in forested frontier, coal where rail reached. Coal-fueled smithing arrives with the railroads.
- Products: horseshoes (enormous demand — horses were the transport infrastructure), wagon fittings, plow repair, nails (competing with mass-produced cut nails by mid-century), tools, specialty repair. The smith as a repair shop as much as a maker.
- Supply chain: imported bar iron and steel from Pittsburgh and beyond; reliance on rail and waterway freight. The frontier smith was NEVER autonomous from industrial iron production — they were a last-mile service business.
- Labor: apprentice + family. The "village smithy" of American folklore — Longfellow's 1841 poem is load-bearing cultural reference but a romantic one (Longfellow's smith is a trope, not a research subject).
- Decline: three-stage: (1) nail and hardware mass production displaced non-repair work (mid-19th century); (2) horseshoe demand collapsed with automobile (1910s–1930s) — this is the main decline vector; (3) service stations and hardware stores displaced the remaining repair niche.
- Load-bearing authors: Anthony Wallace (*Rockdale* — industrial and rural mill life); Thomas Schlereth on material culture; general American economic history (Gordon, Atack and Passell).

**Commit:**
```bash
git add research/cultures/american-frontier/smithing.md
git commit -m "Plan B task 4: American frontier smithing chapter"
```

---

### Task 5: Cross-Cultural Functional Requirements

**Files:**
- Create: `research/trades/smithing/REQUIREMENTS.md`

This document synthesizes what a forge MUST functionally DO, abstracted from historical variation across the 4 cultural chapters. It is the direct input to Plan C (catalog authoring) — the catalog entries specify forge designs, this document specifies what those forges must accomplish.

**Required sections:**

1. **Frontmatter** (YAML) — trade: smithing, version, sources_count, derived_from: [list of 4 chapter paths].

2. **Purpose** (~100 words) — what this document is, how Plan C uses it. Be explicit that REQUIREMENTS.md is trade-agnostic-within-smithing (applies to any forge for any scale), not design-prescriptive.

3. **Temperature Envelope**:
   - Working temperatures for different operations: annealing (~750°C), forge welding (~1100–1300°C), basic shaping (~800–1000°C), heat treatment.
   - Which historical cultures' forges achieved which ranges and how (fuel, bellows, forced air, insulation).

4. **Throughput Envelope**:
   - Range of units/day for different product mixes (nails, horseshoes, tools, repair).
   - Realistic working hours (historically often 4–8 hours/day actual forging, not 10–12; smith's seasonality).
   - Variance across cultures — what was typical, what was exceptional.

5. **Fuel Regime Options**:
   - Charcoal (all cultures), coal (Song China, 19th-century Europe + America), coke (post-industrial), wood (fallback).
   - Trade-offs: heat intensity, sulfur content, supply-chain dependence, environmental impact.

6. **Physical Envelope**:
   - Footprint (m²), ventilation, height, foundation (anvil base mass requirement).
   - Auxiliary infrastructure (water source, storage for stock and products, fuel storage).

7. **Operator Profile**:
   - Skill floor (apprentice, journeyman, master) for different operation types.
   - Operators concurrent (1 smith + 0 to N assistants).
   - Apprentice-friendliness of the form.

8. **Supply-Chain Dependencies** (per falsifier):
   - Iron/steel: local, regional, or industrial? What the historical record says about each.
   - Fuel: local (charcoal, wood) vs. regional (coal).
   - Downstream: who buys the output, how (direct, merchant, contract).

9. **Product Category Matrix**:
   - Everyday hardware (nails, hardware, fasteners)
   - Tools (agricultural, carpentry, trade tools)
   - Repair (horseshoes, wagon parts, tool maintenance)
   - Specialty / artistic / armory
   - Each category has different throughput, skill, and market characteristics.

10. **Functional Requirements Summary Table** — a consolidated table listing ~15–25 requirements (temperature, throughput, fuel, operator, supply) with "typical historical value" and "required modern equivalent" columns. This is the handoff to Plan C.

11. **Sources** (list of unique sources cited across the 4 chapters; full bibliography in SOURCES.md).

**Style:** Technical, synthetic, comparative. Not narrative. The cultural chapters provide the stories; this document extracts the functional specification.

**Commit:**
```bash
git add research/trades/smithing/REQUIREMENTS.md
git commit -m "Plan B task 5: cross-cultural functional requirements for smithing"
```

---

### Task 6: Comparative Historical Forms

**Files:**
- Create: `research/trades/smithing/HISTORICAL-FORMS.md`

Parallel to REQUIREMENTS.md but focused on **forms**, not **functions**. Where REQUIREMENTS tells Plan C what a forge must do, HISTORICAL-FORMS tells it what historical forges actually looked like — their structural and organizational design choices.

**Required sections:**

1. **Frontmatter**, purpose (link to REQUIREMENTS.md and to the 4 cultural chapters).

2. **Physical Forge Comparison** — comparative table, one column per culture, rows for: hearth form, bellows type, anvil mass, auxiliary tools (trip hammers, water power), fuel feed, ventilation. Include trade-agnostic observations (e.g., "all four used some form of forced-air bellows").

3. **Organizational Form Comparison** — comparative table, rows for: ownership (independent / household / guild / state / proprietary), labor (apprentice structure, household involvement), legal recognition, regulatory constraints, succession path.

4. **Product-Mix Comparison** — what each culture's forges typically produced, and how that reflected the surrounding economy.

5. **Supply-Chain Comparison** — iron source, fuel source, market structure.

6. **Cross-Cultural Observations** — what patterns hold across all 4, what is culture-specific. Explicitly separate "universal to smithing" from "contingent on culture."

7. **Sources**.

**Style:** Descriptive, comparative, tabular-where-useful. Not prescriptive.

**Commit:**
```bash
git add research/trades/smithing/HISTORICAL-FORMS.md
git commit -m "Plan B task 6: comparative historical forms of smithing"
```

---

### Task 7: Decline-or-Restructuring Verdict

**Files:**
- Create: `research/trades/smithing/DECLINE-VERDICT.md`

Per spec v0.3 §4.1, Phase 1 research produces a `decline_or_restructuring_verdict` per trade. This document is that verdict for smithing.

**Required sections:**

1. **Frontmatter** — trade: smithing, verdict: {decline | restructuring | mixed}, confidence: {high | moderate | low}.

2. **Question** — restate: did smithing as a local trade actually decline, or did it restructure? The answer matters for the working hypothesis: if restructuring, the equipment-economics lever is different from if actual demand collapse.

3. **Evidence Per Culture** — one subsection per cultural chapter, ~150–250 words each, summarizing that culture's decline trajectory. Reference the chapters rather than duplicating.

4. **Cross-Cultural Pattern** — what's consistent:
   - Commodity smithing (nails, hardware, standardized products) did largely vanish as a local trade, replaced by industrial production.
   - Repair smithing survived longer in each culture, sometimes well into the 20th century, because it cannot be centralized easily.
   - Prestige / specialty smithing (swords in Japan, armor in Europe, artistic work) persists in every culture as a niche art form, often with regulatory or cultural protection.
   - Supply-chain dependence shifted from local to industrial in every culture; no historical smithing practice was truly autonomous from upstream metallurgy after the mid-19th century.

5. **Verdict** — explicit. Based on the evidence: smithing experienced a **mixed** decline (real loss of commodity work) + **restructuring** (surviving niches: repair, specialty). Which portions are addressable by CERES's equipment-economics hypothesis?

6. **Implications for CERES**:
   - Which categories of smithing are plausibly restorable (repair + specialty/custom)?
   - Which are probably not (commodity hardware against mass production)?
   - Does this falsify the working hypothesis for smithing specifically? No — but it DOES constrain what "restoration" means. CERES's catalog should target repair and specialty work, not attempt to compete on commodity hardware.
   - Per spec falsifiers: for smithing, "supply-chain disappearance" partially holds (local iron production did vanish in every culture), but the supply chain CAN be rebuilt via industrial-iron partnership for the restorable niches.

7. **Sources**.

**Style:** Analytical, evidence-based. Be explicit about confidence level for each claim.

**Commit:**
```bash
git add research/trades/smithing/DECLINE-VERDICT.md
git commit -m "Plan B task 7: decline-or-restructuring verdict for smithing"
```

---

### Task 8: Consolidated Bibliography

**Files:**
- Create: `research/trades/smithing/SOURCES.md`

**Required sections:**

1. **Purpose** — bibliography consolidated from Tasks 1–7.

2. **Sources by Category**:
   - Economic history (general)
   - Guild and labor regimes
   - Metallurgy and smithing specifically
   - Culture-specific (grouped by the 4 cultures)
   - Modern maker/practitioner references (when relevant)

3. **For each source:**
   - Full bibliographic citation
   - One-line note on what it's cited for
   - Citation tier (primary source / academic specialist / synthetic economic history / popular synthesis / unverified)
   - Confidence that the source exists (high / placeholder pending verification)

4. **Placeholder Audit** — list of `[CITATION-NEEDED: ...]` placeholders across all Plan B documents, with the specific claim each needs to cover. This is the author's to-do list for the verification pass.

**Style:** Reference document. Clean, complete, scannable.

**Commit:**
```bash
git add research/trades/smithing/SOURCES.md
git commit -m "Plan B task 8: consolidated bibliography and placeholder audit"
```

---

### Task 9: Closeout

**Files touched:**
- Update: `TRACKER.md` (Plan B status → completed; vertical-slice-progress row updates)
- Update: `plans/README.md` (plan B status in index table)
- Update: `plans/2026-04-19-plan-b-research-smithing.md` frontmatter (`status: completed`, add `completed: YYYY-MM-DD`, bump `version` to whatever was reached)

**Required actions:**
- In `TRACKER.md`: move Plan B row from `in_progress` to `completed` with today's date; update Section 3 "Vertical Slice Progress" to mark `research/trades/smithing/REQUIREMENTS.md`, `research/cultures/*/smithing.md` (4 cultures) as complete; note Andean + Islamic cultures deferred to future plan.
- In `plans/README.md`: update Plan B row status from `not-yet-authored` to `completed`.
- In this plan's frontmatter: `status: completed`, add `completed: YYYY-MM-DD`.
- Add a panel-review-queue entry in TRACKER.md: "research/cultures/*/smithing.md (×4) and research/trades/smithing/* (×4) awaiting panel R1 (especially P-5 Historian)."

**Commit:**
```bash
git add TRACKER.md plans/README.md plans/2026-04-19-plan-b-research-smithing.md
git commit -m "Plan B task 9: closeout (TRACKER, plans/README, frontmatter)"
```

---

## Final Self-Review (after Task 9)

Run these checks before declaring Plan B complete:

- [ ] 4 cultural chapters exist and each passes the anti-romanticism checklist.
- [ ] Each chapter has a `## Decline or Restructuring` section feeding into DECLINE-VERDICT.md.
- [ ] Each chapter has a `## Functional Requirements Learned` section feeding into REQUIREMENTS.md.
- [ ] REQUIREMENTS.md abstracts trade-agnostic-within-smithing requirements; no culture-specific language bleeds in.
- [ ] HISTORICAL-FORMS.md is comparative and descriptive; no design prescription.
- [ ] DECLINE-VERDICT.md makes an explicit claim with confidence level.
- [ ] SOURCES.md consolidates all citations across Tasks 1–7 with no duplicates; the placeholder audit is complete.
- [ ] No forbidden framings (STYLE-GUIDE §4) appear anywhere in Plan B outputs.
- [ ] No `docs/superpowers/...` paths.
- [ ] `[CITATION-NEEDED: ...]` placeholders are present where model confidence was low; no fabricated citations.
- [ ] TRACKER.md and plans/README.md reflect Plan B completion.
- [ ] This plan's frontmatter is marked `status: completed`.

## Retrospective: Risks and Assumptions (authored upfront per P-6 discipline)

### Risks and Objections

- **Citation hallucination.** Research authoring is high-risk for invented sources. Mitigation: bracketed placeholders for low-confidence claims; explicit placeholder audit in SOURCES.md; author verifies before promotion.
- **Anchor bias.** Selection of 4 of 6 cultures (skipping Andean, Islamic) risks a Western / East-Asian-heavy corpus. Acknowledged; deferred cultures can be added later without re-architecture (spec §3).
- **Romanticism creep.** The topic invites nostalgia. STYLE-GUIDE §4 and P-5 Historian's lens.verify provide the counter-discipline; each chapter's self-review must apply them.
- **Depth variance.** Cultural coverage may be uneven — stronger on Europe (best-documented) than on Andean / Islamic cultures even within this plan's four. Acknowledge in each chapter's `period and geography` and `sources` sections.

### Failure Modes (contingency paths)

- **If a chapter cannot be written with sufficient citation support:** Mark `status: placeholder-heavy` in frontmatter; do not promote. Flag in TRACKER.md; author verifies/adds sources before Plan C consumes that chapter.
- **If cross-cultural synthesis reveals contradiction:** Task 5 (REQUIREMENTS.md) should document the divergence (per METHODOLOGY §7: "document the divergence rather than collapsing to a consensus"). Do not force consensus.
- **If DECLINE-VERDICT.md verdict is "actual decline (not restructuring)":** This is a partial falsifier for the working hypothesis as applied to smithing. Per spec §2 pivot criteria, the analysis for smithing shifts: the catalog targets specifically the niches where restoration is plausible (repair, specialty), not commodity production.
- **If citation-verification pass finds the placeholders are pervasive and verification is slow:** Scope down — reduce to 3 cultures, promote what's verifiable, defer the fourth.

### Assumptions Now Made Explicit

- Spec v0.3 is stable for Plan B's duration. Schema changes in v0.4+ would affect catalog entries, not research documents.
- The 4 selected cultures cover sufficient variance for functional-requirements synthesis. Adding Andean and Islamic later will enrich, not invalidate, the synthesis.
- `docs/STYLE-GUIDE.md` and `docs/METHODOLOGY.md` are the authoritative style sources; P-5 Historian is the heaviest panel reviewer.
- Plan C will consume REQUIREMENTS.md and HISTORICAL-FORMS.md; DECLINE-VERDICT.md informs Plan C's scope (which restored-trade niches to target).
- Modern sources referenced via MAXIM (`reference`) are citable; don't duplicate, cite.

## Handoff

When Plan B completes:

1. TRACKER.md updated.
2. This plan's frontmatter marked `status: completed`.
3. Plan B artifacts are ready for panel review (especially P-5 Historian). Run `ceres-check` and `ceres-panel` against `research/trades/smithing/REQUIREMENTS.md` and the 4 cultural chapters before Plan C consumes them.
4. Plan C (catalog authoring for smithing) is now unblocked. Plan C authors should read REQUIREMENTS.md, HISTORICAL-FORMS.md, and DECLINE-VERDICT.md before authoring any catalog entry.
