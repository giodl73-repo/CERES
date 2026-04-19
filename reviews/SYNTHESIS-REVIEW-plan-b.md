---
review_id: plan-b-synthesis-review
scope: 4 synthesis documents — REQUIREMENTS, HISTORICAL-FORMS, DECLINE-VERDICT, SOURCES
review_date: 2026-04-19
lenses: [P-4, P-5, P-6, E-1, E-2, E-3]
status: complete
overall_verdict: HOLD
---

# Plan B Synthesis Docs — Consolidated Review

**Review date:** 2026-04-19
**Scope:** REQUIREMENTS, HISTORICAL-FORMS, DECLINE-VERDICT, SOURCES
**Lenses:** P-4, P-5, P-6 + E-1, E-2, E-3 (pragmatic per-doc)

---

## Summary

| Document | P1 | P2 | P3 | Verdict |
|---|---|---|---|---|
| REQUIREMENTS.md | 2 | 4 | 3 | HOLD |
| HISTORICAL-FORMS.md | 0 | 3 | 3 | PASS-WITH-NOTES |
| DECLINE-VERDICT.md | 0 | 3 | 2 | PASS-WITH-NOTES |
| SOURCES.md | 1 | 2 | 2 | HOLD |
| Cross-document | 0 | 4 | 2 | — |
| **Overall** | **3** | **16** | **12** | **HOLD** |

**Overall: HOLD** — Two P1s in REQUIREMENTS.md and one P1 in SOURCES.md. Fix all three P1s and the flagged P2s before Plan C catalog authorship begins. HISTORICAL-FORMS.md and DECLINE-VERDICT.md are plan-C-ready with their P2 notes documented. REQUIREMENTS.md is the primary gate: it is the direct input specification for every Plan C catalog entry.

---

## Per-Document Findings

---

### REQUIREMENTS.md (Task 5)

**Primary lenses: P-4 Craft Practitioner, P-5 Historian, E-2 Scope Keeper, E-3 Numeracy Checker**

#### P-4 Craft Practitioner Findings

The document abstracts functional requirements a real smith would recognize. Temperature envelopes, throughput ranges, operator profiles, and supply-chain dependencies are all captured. The repair-dominance implication (§8) and the labor-regime falsifier (§6) are stated in practical, actionable terms. The 24-row summary table (§9) is the strongest deliverable in the document: it maps directly to what a catalog entry needs to populate.

**Strong points:** The "realistic active forging hours" constraint (4–8 hours, not 10–12) is exactly the kind of floor-reality P-4 demands. R-06 enforces `max_active_hours_per_week` with a startup/shutdown overhead requirement — this is precisely what distinguishes a real operational spec from a conference-room document. The failure-mode implication is present via the bellows-divergence note (§2) and the coal sulfur warning (§4), though these are not structured as explicit failure-mode fields.

**Findings:**

| # | Severity | Lens | Location | Issue |
|---|---|---|---|---|
| REQ-01 | P2 | P-4 | §9 / R-06 | `operations_reality.startup_shutdown_overhead_per_day_min` is required by R-06 but the document does not specify what the expected value range is from historical evidence. Plan C authors are told to populate the field but given no historical baseline to calibrate it against. The 4–8 active-hours-per-day figure is the throughput constraint; the startup/shutdown overhead that accounts for the remainder of the day is separately required by the catalog schema (per spec §5) but REQUIREMENTS gives no historical estimate for it. |
| REQ-02 | P3 | P-4 | §5 | The anvil-base-mass section states base mass "matters for energy efficiency" but does not name the failure mode (resonant base wastes hammer energy as vibration and fatigues the operator). For P-4, the functional requirement is incomplete without the failure-mode consequence. A Plan C author who misses the base-mass requirement will not understand why undercutting it is operationally significant. |
| REQ-03 | P3 | P-4 | §6 | The operator-profile table states "forge welding: journeyman to master" but does not note that forge welding requires temperature *judgment* (not just temperature achievement) — the junction must be held in a narrow window at the right instant. This is the kind of practical constraint that P-4 expects named. The temperature range is given in §2; the time-pressure-at-temperature constraint for welding is not. |

#### P-5 Historian Findings

Historical claims trace back to the four chapters accurately. Anti-romanticism is held throughout: the "autonomy myth" (§7) is sharp and well-sourced, the charcoal-sustainability caveat (§4) directly references STYLE-GUIDE §4.2, and the labor-regime falsifier (§6) is stated at appropriate force.

**Strong points:** The Hartwell tonnage caveat in §3 ("mandatory carry-forward") is present and explicit, naming von Glahn 2016 as the verification source — this is the resolution of CHN-01 from the chapters review. The `[CITATION-NEEDED]` brackets are honest: the temperature ranges are flagged as inferred from process logic rather than documented measurements. The guild/non-guild skill-transfer divergence (§10, DIV-03) correctly represents the four-culture spread without privileging any single model.

**Findings:**

| # | Severity | Lens | Location | Issue |
|---|---|---|---|---|
| REQ-04 | P2 | P-5 | §2 | The temperature ranges (R-01 through R-05) are explicitly acknowledged as inferred from process logic, with a `[CITATION-NEEDED]` for archaeometallurgy confirmation. This caveat is appropriate — but the document also uses these ranges as the direct input for every Plan C catalog entry's R-01 through R-05 fields. A catalog entry that cites REQUIREMENTS.md as authority for these ranges is indirectly relying on an unverified claim. The caveat in §2 does not propagate to §9's summary table, where R-01 through R-05 appear as plain requirements without the inferred-not-measured caveat. Before Plan C begins, the summary table should note that R-01/R-02 values are inferred from process constraints (Placeholder #4 in SOURCES.md) and will carry a hedge until the archaeometallurgy source is verified. |
| REQ-05 | P2 | P-5 | §3 | The throughput figures in §3's small-scale table carry `[CITATION-NEEDED]` brackets and are honestly labeled "Author estimate from product-weight reasoning." But the note at the end of §3 ("Claiming 10–12 hours of active forging per day is not supported") frames a negative constraint without a positive figure: the historical record provides no verified throughput upper bound for horseshoes, only an unsourced estimate of 20–40 per day. This leaves the throughput floor for Plan C `sim_params` as structurally unconstrained. Placeholder #5 in SOURCES.md (Langdon 1986 verification) needs to be resolved before REQUIREMENTS.md can serve as the throughput anchor for catalog entries. |
| REQ-06 | P3 | P-5 | §4 | The statement that "the coal transition was demand-driven, not technically forced" is correct for both Song China and the American frontier and is appropriately sourced (Hartwell 1962; Atack and Passell 1994). However, the document does not apply this point to the modern design implication: that modern propane or induction forges represent equally valid supply-driven fuel choices — not a deviation from "authentic" practice. The anti-romantic point is stated for the historical cases but not extended to its modern equivalent. This would strengthen the document's usefulness as a Plan C spec. |

#### E-2 Scope Keeper Findings

The document correctly stays in "functional requirements" territory. It abstracts *what a forge must do* rather than *what a forge should look like*. The introduction explicitly states: "It is not design-prescriptive: it does not specify charcoal over coal, box bellows over bag bellows, or any particular organizational form." This anti-prescriptive stance is maintained throughout.

**Findings:**

| # | Severity | Lens | Location | Issue |
|---|---|---|---|---|
| REQ-07 | P1 | E-2 | §2 | Subsection "How each culture achieved the temperature envelope" goes beyond functional requirements into describing specific historical implementations. For a requirements document, the relevant output is the *requirement* (forge must reach X°C); the *how each culture met it* is HISTORICAL-FORMS.md territory. This subsection is 250+ words of descriptive content that duplicates material covered in HISTORICAL-FORMS.md §2 and §6 and should be either removed or compressed to a single cross-reference sentence: "Four bellows mechanisms achieved this requirement across cultures — see HISTORICAL-FORMS.md §2 for comparative forms." The current duplication risks requirements creep where Plan C authors treat the implementation examples as implicit prescriptions. |
| REQ-08 | P2 | E-2 | §5 | The physical envelope section (§5) includes "Auxiliary infrastructure" (quench trough, fuel storage, stock storage, water source). These are correctly identified as functional requirements. However, the prose under each auxiliary item describes historical implementation context ("charcoal could not be stored indefinitely; working inventory of 1–3 days' fuel was typical") that belongs in HISTORICAL-FORMS.md. The requirement itself (adjacent fuel storage for fire-safety reasons) is sound; the historical elaboration is scope drift into the forms document. Trim to requirement only. |

#### E-3 Numeracy Checker Findings

The document is a requirements specification, not a catalog entry, so full sim_params cross-checks do not apply. The relevant numeracy check is whether the numeric ranges in the summary table (§9) are internally consistent and trace back to the chapters.

**Findings:**

| # | Severity | Lens | Location | Issue |
|---|---|---|---|---|
| REQ-09 | P1 | E-3 | §3 | The large-scale Song throughput claim ("Northern Song iron output comparable in aggregate to early 18th-century British output [Hartwell 1962]") appears in §3 with the "scale caveat (mandatory carry-forward)" box — good. But the frontmatter states `sources_count: 28`, which includes three CITATION-NEEDED entries in the sources list (items 25–27). The claim "sources_count: 28" overcounts: it counts placeholders as sources. This is a minor precision error but is the same miscounting pattern that SOURCES.md (Task 8) was specifically tasked to audit. The frontmatter should read `sources_count: 24` (named sources) with a note that 4 additional placeholders are tracked. This is a data-quality issue for the frontmatter accuracy standard. |
| REQ-10 | P2 | E-3 | §3 / §9 | The footprint range "15–40 m²" appears in §5 and is required by R-10 in the summary table. The lower bound (15 m²) is attributed to the American frontier chapter (§9), which gave "15–30 m²" as its frontier-specific range. The upper bound (40 m²) is attributed to medieval northern Europe. The synthesis into a single 15–40 m² range is defensible as an envelope, but the summary table (R-10) states this as "baseline for Plan C's small-footprint catalog tier" without noting that the lower end is the frontier minimum and the upper end is the European maximum — these represent different scale contexts. A Plan C author who designs to 15 m² may be designing the smallest viable configuration; the document should make this explicit in R-10. |
| REQ-11 | P3 | E-3 | §3 | The throughput table (§3) mixes absolute production figures (horseshoes, plowshares, nails) with categorical figures ("Irregular; bursty" for the American frontier). The table format implies comparability across rows; the frontier row's categorical entry is not comparable to the other rows' numeric estimates. This should be flagged as structurally inconsistent — either all rows carry numeric estimates (with acknowledged uncertainty) or the table header should note that the frontier row is qualitatively different. |

#### Structural Assessment

- **24-row summary table (§9):** Coherent and well-organized. Requirements R-01 through R-24 cover all major functional areas. The "historical value(s)" and "modern-equivalent expectation" columns provide the handoff logic Plan C needs. Minor issue: R-01 through R-05 (temperature requirements) should carry a note that values are inferred from process physics (see Placeholder #4 in SOURCES.md), not directly measured from pre-industrial forge documentation.
- **6-item divergence log (§10):** All six divergences are genuine and load-bearing for Plan C. DIV-06 (regulatory preservation) correctly identifies that catalog entries must specify whether their viability depends on a mechanism that does not generically exist in modern contexts. This is strong.
- **Vocabulary:** Vocabulary is consistent with the harmonized standards from the chapters review. The temperature vocabulary uses the Europe chapter's two-tier (shaping / welding) framework as recommended. Decline vocabulary uses the canonical terms. The only vocabulary inconsistency is in §11's sources list: "sources_count: 28" in frontmatter vs. 24 named + 4 CITATION-NEEDED items in the list — see REQ-09.

**REQUIREMENTS.md verdict: HOLD** — P1s in E-2 (scope drift in §2 duplicating HISTORICAL-FORMS.md) and E-3 (sources_count overcounting). Four P2s. These are fixable; the document's core structure is sound and the 24-row summary table is ready for Plan C use once the P1s are resolved.

---

### HISTORICAL-FORMS.md (Task 6)

**Primary lenses: P-5 Historian, E-2 Scope Keeper**

#### P-5 Historian Findings

The four comparison tables capture genuine cross-cultural variance without projecting modern categories onto historical forms. The decline-pattern mapping table (§7) uses the canonical vocabulary ({`decline`, `restructuring`, `demand-collapse`, `regulatory-dissolution`, `mixed`}) consistently and correctly. The cross-cultural observation sections (§6) are the strongest part of the document: the universal/contingent/unique distinction is well-executed.

**Strong points:** The "autonomy myth" is present in §5's supply-chain observations ("No anchor culture's smith was supply-chain autonomous for iron stock"). The Song hydraulic bellows "preceding European equivalents by several centuries" is placed in the Unique/Anomalous category — correct, not used to oversell Chinese advantage as a replicable model. The regulatory-preservation analysis of post-Meiji sword smithing (§6, Unique/Anomalous section) is analytically precise: "managed scarcity" rather than "economic survival."

**Findings:**

| # | Severity | Lens | Location | Issue |
|---|---|---|---|---|
| HF-01 | P2 | P-5 | §2 (Table 1) | The bellows-type row for medieval northern Europe reads: "bag bellows (attested in northern European iconography); double-action box bellows possible but pre-1500 attestation requires confirmation [CITATION-NEEDED]." This correctly carries forward the JPN-05 resolution from the chapters review (hedging the "single-acting" European characterization). However, the document still uses the unresolved attestation question to populate Table 1 — the table implies four comparable entries per culture, but the Europe entry for bellows type is incompletely resolved. Until the iconographic confirmation arrives, Table 1's Europe/bellows cell should read: "Bag bellows (attested); double-action box bellows possible but unconfirmed before ca. 1500 — see Placeholder #26 in SOURCES.md." |
| HF-02 | P2 | P-5 | §7 (decline table) | The medieval northern Europe decline summary notes "guild-controlled urban smithing eroded earlier through proto-industrial competition" in the summary column but the canonical verdict is `mixed`. The summary correctly identifies three sub-trajectories (commodity decline, repair demand-collapse, specialty restructuring) but compresses these to `mixed — combining demand-collapse, decline, and restructuring`. This is accurate but may confuse Plan C authors who need to know *which segment gets which verdict* for the Known Risks section. Consider adding a parenthetical per-segment mapping: "(commodity hardware = `decline`; rural repair = `demand-collapse` [horse-agriculture]; specialty = `restructuring`)." |
| HF-03 | P3 | P-5 | §6 (Culturally Contingent) | The labor-regime entry in Culturally Contingent notes that "household unpaid labor was universal (see above)" but then treats the *institutional form* of non-household coercion as contingent. This framing is correct. However, the section does not make the implication explicit: that the universal finding (household labor as structural input) is the falsifier-relevant one, while the contingent forms (guild indenture vs. *jianghu* vs. *detchi-boko*) are historically interesting but not directly constraining for modern catalog entries. A one-sentence bridge to spec §2 would strengthen this section for Plan C authors. |

#### E-2 Scope Keeper Findings

The document is correctly descriptive-not-prescriptive. It describes historical forms without sliding into design prescription. It defers decline analysis to DECLINE-VERDICT.md appropriately (§7 is a mapping table with a cross-reference, not an analysis). It does not repeat REQUIREMENTS.md content at the functional-requirements level.

**Findings:**

| # | Severity | Lens | Location | Issue |
|---|---|---|---|---|
| HF-04 | P2 | E-2 | §6 (Universal) | The "Universal to Smithing" section contains the sentence: "Any forge design in a catalog entry must address each of these universals." This prescriptive language is a minor scope drift: HISTORICAL-FORMS.md is descriptive; the prescriptive directives belong in REQUIREMENTS.md (where they are already present as R-01 through R-24). Remove the prescriptive sentence; replace with: "REQUIREMENTS.md R-01 through R-24 encode these universals as the catalog entry specification." |
| HF-05 | P3 | E-2 | §4 (Table 3) | The product-mix table includes brief notes on industrial displacement timelines (cut nails from 1790s; wire nails from 1880s; McCormick implements). These displacement timelines belong in DECLINE-VERDICT.md §2 rather than in a comparative forms table. The table would be cleaner if the displacement notes were removed and the table limited to attested historical product-mix characteristics, with a cross-reference to DECLINE-VERDICT.md for the displacement analysis. |
| HF-06 | P3 | E-2 | §8 (Divergence Log) | Divergence 4 ("State involvement in production and demand") concludes with: "The CERES working hypothesis is implicitly tested against a market-demand context; the Song case shows that historical large-scale viability required a state demand anchor that market demand alone could not supply." This sentence introduces an analytical position that belongs in DECLINE-VERDICT.md (which makes this same argument explicitly in §2.2 and §5). The divergence log should document the divergence; the analytical implication for CERES belongs in the verdict document. |

#### Structural Assessment

- **Four comparison tables present:** Tables 1–4 cover Physical Forge, Organizational Form, Product Mix, and Supply Chain. All four are present and organized by culture column. The four-table structure is correct and covers the declared scope.
- **Universal / contingent / unique balance:** The §6 taxonomy is well-executed. The Universal findings are genuinely universal (forced air, anvil-and-hammer, high temperature, skilled-labor-as-constraint, supply-chain dependency, household labor). The Contingent findings are genuinely variable across cultures. The Unique/Anomalous section identifies four items that are one-offs without overclaiming their significance.
- **Divergence log items:** All five divergences (§8) are load-bearing for Plan C. Divergence 3 (labor-regime institutional form) is particularly strong: it prevents Plan C authors from treating "apprenticeship" as a single historical form.
- **Needham citation:** The document uses "Needham 1965, vol. IV pt. 2" consistently (§2 Table 1, §5, §6) — this is the corrected citation from the PARTIAL finding in CHECK-plan-b-citations.md. The correction has propagated correctly. One exception: the §9 sources list (item 3) reads "Needham, Joseph. 1958. *Science and Civilisation in China*, vol. IV" — the old incorrect citation is still present in the HISTORICAL-FORMS.md sources list. This must be corrected.

**HISTORICAL-FORMS.md verdict: PASS-WITH-NOTES** — No P1 findings. Three P2s (bellows-attestation Table 1 cell, decline sub-segment mapping, one prescriptive sentence in §6). Three P3s. Ready for Plan C use with these corrections documented.

---

### DECLINE-VERDICT.md (Task 7)

**Primary lenses: P-5 Historian, P-6 Skeptical Funder, E-2 Scope Keeper**

#### P-5 Historian Findings

The evidence-per-culture summaries (§2) accurately represent the chapters. Anti-romanticism is sustained throughout: the American frontier case opens with "the clearest documented decline sequence of any anchor culture" and the Song case correctly frames the Mongol collapse as demand-collapse-of-organizational-form rather than technological failure. The repair-segment survival argument is correctly framed as structural reasoning (geographic boundedness, judgment-intensiveness) rather than as a romantic survival narrative.

**Strong points:** The Hartwell tonnage caveat is present in §2.2: "specific tonnage figures must be treated as order-of-magnitude estimates pending von Glahn 2016 verification." This is the CHN-01 resolution carried forward correctly. The cross-cultural pattern section (§3) correctly distinguishes four mechanisms (commodity disappearance universal; repair survival structural; prestige survival regulatory; supply-chain dependence shifted). The supply-chain paragraph explicitly says dependence "never resolved" — this is the correct anti-autonomy framing.

**Findings:**

| # | Severity | Lens | Location | Issue |
|---|---|---|---|---|
| DV-01 | P2 | P-5 | §2.1 | The medieval northern Europe section states: "Guild-controlled urban smithing in major Rhineland and Flemish towns eroded earlier still, through the penetration of proto-industrial putting-out systems and unincorporated suburban craftsmen from the sixteenth and seventeenth centuries [medieval-northern-europe §8; Epstein 1998]. This institutional erosion preceded and was partly independent of technological competition." This is the MNE-02 resolution from the chapters review — the sub-distinction between Rhineland/Flemish urban and English rural trajectories. The resolution is present but the evidence is still thin: Epstein 1998 is cited as background context but is not a source for the specific Rhineland/Flemish timing claim. The SOURCES.md Placeholder #58 (guild decline in Rhineland metalwork towns, 16th–17th c.) remains unresolved. The verdict doc should acknowledge this evidence gap rather than relying on chapter cross-references alone. |
| DV-02 | P2 | P-5 | §2.2 | The sentence "The Ming dynasty rebuilt iron production at a smaller average scale with greater reliance on private operations [CITATION-NEEDED: Ming iron industry structure]" uses CITATION-NEEDED correctly. However, the paragraph frames this as a factual claim ("rebuilt... at smaller scale") rather than an inference ("the sources consulted suggest smaller scale, but Ming-era production is not directly attested here"). The framing should hedge: "The sources consulted here do not address Ming iron production levels; post-Yuan reconstruction scale and form remain an open question pending verification in von Glahn 2016 [CITATION-NEEDED: Ming iron industry structure]." This preserves evidential honesty. |
| DV-03 | P3 | P-5 | §4 (Verdict) | The verdict states "Confidence: moderate" and provides a confidence qualifier. This is appropriate. The "highest-confidence sub-claim" identified is the commodity smithing displacement — correct. However, the verdict does not identify the *lowest-confidence* sub-claim. From the evidence base, the lowest-confidence claim is the repair-segment restructuring (§3, "The repair-segment restructuring claim rests on survival evidence rather than on detailed economic documentation of its post-industrial form"). This gap should be explicitly flagged in the confidence discussion: "The lowest-confidence sub-claim is the repair-segment restructuring pathway; evidence is survival evidence, not documented post-industrial economics." This matters for Plan C because the repair-dominant catalog entries are the ones that the verdict is endorsing most directly. |

#### P-6 Skeptical Funder Findings

The falsifier analysis (§4, "On the spec §2 falsifiers") is the most funder-relevant section of the document, and it is well-executed. All four falsifiers are engaged, and the conclusion — "working hypothesis is not falsified for smithing overall, but is category-constrained" — is precisely the kind of scoped finding that a funder can act on.

**Strong points:** The vocabulary "category-constrained" rather than "falsified" is the right frame: it tells a funder that commodity hardware entries are not worth funding (demand has permanently migrated) but repair/specialty entries remain testable. The "implications for CERES" section (§5) explicitly separates plausibly-restorable from probably-not-restorable categories with clear reasoning. The demand-collapse falsifier for commodity hardware is stated honestly: "No equipment redesign changes this fundamental competitive position."

**Findings:**

| # | Severity | Lens | Location | Issue |
|---|---|---|---|---|
| DV-04 | P2 | P-6 | §5 (Implications) | The "categories plausibly restorable via equipment redesign" list includes "trade-education and apprentice-training contexts — civic or cooperative forges oriented toward skill transfer and workforce development." This category is described as "viable under the civic lens (spec §2) even if market-lens economics are marginal." This claim is reasonable but rests on an unexamined assumption: that civic funders can be found for forge-based apprentice training at a scale that makes the catalog entry functional. The "civic lens viable" claim requires a brief specification of what demand condition makes it true — otherwise it reads as the funder's equivalent of "if we build it, they will come." Add one sentence: "Civic viability depends on a municipality or institution committing the apprenticeship slots and workshop hours — not an assumed demand condition; Plan C entries targeting this segment must specify the institutional partner and demand threshold." |
| DV-05 | P2 | P-6 | §4 | The falsifier engagement correctly distinguishes the four falsifiers. However, it does not address a potential fifth constraint not in the spec's original four: *capital formation*. Historical forges were capitalized through guild admission fees, household accumulation, and patron investment — forms that had lower cost than modern financing. A modern smith starting a repair/specialty forge needs to capitalize the forge at modern equipment prices under modern lending conditions. The verdict should acknowledge this as a binding constraint for the *startup* scenario even where the ongoing economics are viable. This is not a fatal falsifier — it is a qualification — but ignoring it leaves a gap a funder will notice. |

#### E-2 Scope Keeper Findings

The document stays in "verdict" scope. It does not duplicate HISTORICAL-FORMS.md content or REQUIREMENTS.md content in any substantive way. The evidence-per-culture summaries (§2) cite back to chapters rather than restating forms. §5 (implications) stays appropriately prescriptive for Plan C without prescribing specific design choices.

No P1 or P2 E-2 findings.

Minor P3 (DV-06): The §5 "Recommendation to Plan C catalog authors" section ends with "Reviewers should use this verdict document to check whether an entry's targeted product category is plausibly restorable; if an entry implicitly assumes commodity competitiveness without justification, that is a P1 editorial finding." This is the right instruction, but it uses internal review vocabulary ("P1 editorial finding") that belongs in a review guide, not in a verdict document. Either remove the "P1" label and state the finding type in plain language, or add a forward reference to a review checklist.

#### Structural Assessment

- **Frontmatter verdict field:** `verdict: mixed` in frontmatter matches the "Overall verdict: mixed" in the §4 body. Consistent.
- **Confidence qualifier:** Present in frontmatter (`confidence: moderate`) and in §4 body. The word "moderate" is used consistently — it appears in frontmatter and in the relevant body paragraph. Correct.
- **Implications actionable for Plan C:** §5 is the strongest implications section in any of the four synthesis documents. The separation between "plausibly restorable" and "probably not restorable" categories is directly actionable: catalog entry authors can check their target product category against the list.
- **`derived_from` in frontmatter:** Includes both the four cultural chapters and the two prior synthesis docs (REQUIREMENTS.md, HISTORICAL-FORMS.md). This is the correct dependency chain for a verdict document.

**DECLINE-VERDICT.md verdict: PASS-WITH-NOTES** — No P1 findings. Three P2s (Rhineland trajectory evidence thin, Ming framing overconfident, civic viability conditionality unstated). Two P3s. Document is ready for Plan C consumption with the P2 caveats noted.

---

### SOURCES.md (Task 8)

**Primary lenses: E-1 Citation Auditor, E-3 Numeracy Checker**

#### E-1 Citation Auditor Findings

The consolidation work is thorough. Confidence tiers match the CHECK-plan-b-citations.md audit for all sources within that audit's scope. No new citations have been fabricated — the Self-Review Checklist (§ at end) confirms this, and the source list cross-checks against the chapters and synthesis docs.

**Strong points:** The two PARTIAL corrections from CHECK-plan-b-citations.md are carried forward correctly: Needham is listed as "1965, vol. IV, pt. 2: Physics and Physical Technology — Mechanical Engineering" with an explicit "NOTE: cited as '1958, vol. IV' in some derived documents — this is an error" — excellent. Wallace subtitle is corrected in the notes. The OSHA standard is correctly listed as UNVERIFIED-BUT-HIGH-CONFIDENCE (not VERIFIED) because it was not in the original citation audit scope.

**Findings:**

| # | Severity | Lens | Location | Issue |
|---|---|---|---|---|
| SRC-01 | P1 | E-1 | §Distribution Summary | The frontmatter states `verified_source_count: 26`. The body's "Source-Tier Distribution Summary" table shows 22 VERIFIED + 2 PARTIAL + 2 UNVERIFIED-BUT-HIGH-CONFIDENCE = 26 named sources. However, the table note reads: "`verified_source_count: 26` reflects named sources with any verification status." This mixes "named and verified" with "named with any status" — PARTIAL and UNVERIFIED-BUT-HIGH-CONFIDENCE are not the same as VERIFIED. A reader seeing `verified_source_count: 26` in frontmatter and then finding 4 sources that are not verified (2 PARTIAL + 2 UNVERIFIED-BUT-HIGH-CONFIDENCE) will distrust the audit. The frontmatter should read `verified_source_count: 22` (VERIFIED only) with a separate `partial_source_count: 2` and `unverified_high_confidence_count: 2`. The current frontmatter misrepresents verification status. |
| SRC-02 | P2 | E-1 | §Placeholder Audit | Placeholder #3 ("von Glahn 2016 verification of Hartwell tonnage — appears as its own placeholder") is noted as "(same as #1; deduplicated)." But the deduplication is not clean: #1 and #3 are in fact different gaps. #1 is the gap for the tonnage comparison claim itself (Hartwell's specific figures vs. British output). #3 is the gap for the blocking dependency called out explicitly in REQUIREMENTS.md §3 as "[CITATION-NEEDED: verification of Hartwell tonnage estimates against von Glahn 2016]." These are the same underlying task (read von Glahn 2016 against Hartwell), but they arise from different document contexts and may resolve with different textual fixes. Deduplicating them into a single row risks one being forgotten when the resolution is applied. Recommend keeping both rows but noting "(same research action; fixes #1 context in song-china chapter and #3 context in REQUIREMENTS.md §3 separately)." |
| SRC-03 | P2 | E-1 | §Metallurgy | The Mokyr 2002 citation (*The Gifts of Athena*) appears in the bibliography under "Economic History (General)" as VERIFIED, with the usage note "Pre-industrial technical knowledge and its economic context; background for guild and craft-knowledge claims." However, Mokyr 2002 does not appear as a citation in any of the four synthesis documents (REQUIREMENTS, HISTORICAL-FORMS, DECLINE-VERDICT, SOURCES itself) or as a named source in the four chapters that SOURCES.md consolidates from (only the medieval-northern-europe chapter lists it, in its sources section). A source that appears in the consolidated bibliography but is not cited in any synthesis document is either an orphan (should be removed from the synthesis bibliography) or an anticipated citation (should be labeled as such). Clarify status. |

#### E-3 Numeracy Checker Findings

The placeholder audit count is the key numeric claim in SOURCES.md.

**Findings:**

| # | Severity | Lens | Location | Issue |
|---|---|---|---|---|
| SRC-04 | P2 | E-3 | §Frontmatter / §Placeholder Audit | The frontmatter states `placeholder_count: 58`. The placeholder audit table contains exactly 58 numbered rows (items 1–58). The count is consistent. However, the Self-Review Checklist notes "Every [CITATION-NEEDED: ...] placeholder across the seven Plan B documents has a row in the placeholder audit." This claim should be spot-checked: the plan-b-citations.md audit found 117 total placeholder *lines* across the four chapters alone (47 + 19 + 32 + 19 = 117). SOURCES.md is consolidating seven documents but derives 58 distinct placeholder topics. The delta (117 lines → 58 topics) is explained by deduplication — multiple inline and sources-list occurrences of the same gap collapsed to one row. This deduplication is correct and useful. However, the methodology of deduplication is not described in the document. Add a note: "Placeholder topics are deduplicated across all occurrences; a single research gap that appears multiple times inline and in sources lists is counted once. Total distinct citation gaps: 58." |
| SRC-05 | P3 | E-3 | §Verification Priority | The verification priority list (8 items) does not include a timeline or sequencing dependency map. Items #1 and #3 (both requiring von Glahn 2016) could be resolved in a single read of von Glahn if the reader knows to look for both things simultaneously. Items #4 and #5 (archaeometallurgy for temperature ranges and charcoal kWh figure) could potentially be resolved by the same specialist literature search (Tylecote 1992 appendix, Crew & Crew experimental archaeology). A brief sequencing note — "Items 1+3 can be resolved in a single targeted read of von Glahn; items 4+5 require the same specialist literature search" — would make the priority list more actionable for a Plan C author who is allocating research time. |

#### Structural Assessment

- **26-source claim:** The claim "26 distinct named sources" is accurate: 22 VERIFIED + 2 PARTIAL + 2 UNVERIFIED-BUT-HIGH-CONFIDENCE = 26 named sources with any verification status. The claim is true but see SRC-01 for the frontmatter accuracy issue.
- **Category organization:** The six-category organization (Economic History General, Guild and Labor Regimes, Metallurgy and Technology, Medieval Northern Europe, Song China, Tokugawa Japan, American Frontier) plus the "Named in Placeholders" section is useful and usable as a Plan C verification queue.
- **Placeholder audit usability:** The urgency tier system (P1-BLOCKING, P2-LOAD-BEARING, P3-SUPPORTING, P4-POLISH) is well-calibrated. The 8 items in the verification priority section correctly identify the synthesis-blocking gaps. The Recommended Verification Priority section is actionable as a research queue.
- **Needham correction propagation:** The PARTIAL note for Needham correctly instructs: "Change all instances of `Needham 1958, vol. IV` to `Needham 1965, vol. IV pt. 2` across all seven documents." Note that HISTORICAL-FORMS.md §9 sources list still carries the old citation (item 3: "Needham, Joseph. 1958. *Science and Civilisation in China*, vol. IV") — this specific instance requires a fix before the correction is complete.

**SOURCES.md verdict: HOLD** — One P1 (frontmatter `verified_source_count` miscounts PARTIAL and UNVERIFIED-BUT-HIGH-CONFIDENCE as verified). Two P2s (deduplication methodology not described, #1/#3 deduplication incomplete). Two P3s. The bibliography is clean and the placeholder audit is the most useful operational document for Plan C. The P1 is a single-field frontmatter fix.

---

## Cross-Document Consistency

---

### Check 1: Vocabulary Consistency Across the Four Docs

**Temperature vocabulary:** REQUIREMENTS.md uses the two-tier (shaping: ~800–1000°C / welding: ~1100–1300°C) vocabulary consistently, as recommended by the chapters review. HISTORICAL-FORMS.md §2 and §6 use the same vocabulary. DECLINE-VERDICT.md does not discuss temperature (appropriate — it is a verdict document). SOURCES.md does not discuss temperature (appropriate — it is a bibliography). Vocabulary is consistent across all documents where it appears.

**Decline vocabulary:** REQUIREMENTS.md §8 product-category table uses "Displaced," "Partial," "Yes" in the "Survived?" column — not canonical decline vocabulary. The canonical vocabulary (`decline`, `restructuring`, `demand-collapse`, `regulatory-dissolution`, `mixed`) is used in HISTORICAL-FORMS.md §7, DECLINE-VERDICT.md throughout, and REQUIREMENTS.md §10 (DIV-05, DIV-06). The mixed vocabulary in the §8 product table is a minor inconsistency but does not create ambiguity. **P3 finding (cross-doc):** REQUIREMENTS.md §8 "Survived?" column should use canonical vocabulary labels in brackets (e.g., "`No — actual revenue loss` [`decline`]") to align with HISTORICAL-FORMS.md §7 and DECLINE-VERDICT.md.

**Assessment: PASS** — vocabulary is consistent where it matters; one minor inconsistency flagged.

---

### Check 2: Source Attribution — Synthesis Claims Tracing to Chapters

All major synthesis claims in REQUIREMENTS.md, HISTORICAL-FORMS.md, and DECLINE-VERDICT.md trace back to the four chapters by citation or logical abstraction. The document-level `derived_from` frontmatter fields correctly list the source chapters. Inline citations in synthesis documents use bracketed chapter-section references (e.g., `[american-frontier chapter §5 and §9]`, `[song-china §Decline or Restructuring]`) where the synthesis abstracts from chapter text rather than from a named source.

One exception: REQUIREMENTS.md §6's claim that "a minimum 3-year apprentice pipeline to sustain operator succession" is cited to `[medieval-northern-europe chapter §Functional Requirements Learned]` — this is the correct attribution. However, the three other chapters do not independently confirm this 3-year figure; it derives solely from the European chapter (which itself carries a bracket for the medieval-specific evidence — CITATION-NEEDED at MNE-10). A synthesis requirement derived from a single chapter that itself has an unresolved citation needs to be labeled as single-culture-derived. **P2 finding (cross-doc):** R-19's "3-year minimum pipeline" should note it derives from the European guild model and does not apply uniformly across all four cultures (the American frontier used shorter, variable apprenticeships; Tokugawa Japan used multi-year but non-standardized terms).

**Assessment: PASS-WITH-NOTES** — one attribution that overgeneralizes from a single-culture finding.

---

### Check 3: Hartwell Tonnage Caveat Propagation

This is the CHN-01 finding from the chapters review. Required fix: caveat must carry to REQUIREMENTS.md, HISTORICAL-FORMS.md, and DECLINE-VERDICT.md.

| Document | Caveat present? | Form |
|---|---|---|
| REQUIREMENTS.md §3 | YES | Full caveat box: "Scale caveat (mandatory carry-forward). Hartwell's specific tonnage figures must be treated as order-of-magnitude estimates... von Glahn 2016 is the recommended verification source... must not be treated as resolved until that verification is complete." |
| HISTORICAL-FORMS.md §8 (Divergence 1) | PARTIAL | Notes "Hartwell compared (with documented uncertainty)" and cites "scale caveat carried from Song chapter" — present but less explicit than REQUIREMENTS.md's treatment. Does not name von Glahn 2016 as the verification source. |
| DECLINE-VERDICT.md §2.2 | YES | Present: "specific tonnage figures must be treated as order-of-magnitude estimates pending von Glahn 2016 verification." |
| SOURCES.md §Song China | YES | Explicit: "MANDATORY caveat: tonnage figures are order-of-magnitude estimates; von Glahn 2016 is required verification." |

**Assessment: PASS** — caveat propagated to all four documents. HISTORICAL-FORMS.md §8's version is lighter but sufficient; recommend adding the von Glahn 2016 name for completeness (P3).

---

### Check 4: Falsifier Engagement Consistency

**REQUIREMENTS.md falsifiers:** The document addresses spec §2 falsifiers in §6 (labor-regime dependency in the operator profile section, with explicit "falsifier" language and a citation to `spec §2`), §7 (supply-chain dependency as a structural finding — no single falsifier, but demand-anchor analysis), and §8 (demand-collapse for commodity categories). The temperature requirements (§2) implicitly address "supply-chain disappearance" by noting that bar steel is commercially available.

**DECLINE-VERDICT.md falsifiers:** All four falsifiers are engaged in §4 with explicit "spec §2" cross-references. The engagement is more detailed and analytical than REQUIREMENTS.md's treatment — this is appropriate, since the verdict document is the authoritative falsifier analysis.

**Consistency check:** Are the falsifier implications consistent between the two documents?

- *Demand collapse:* REQUIREMENTS.md §8 states commodity hardware faces "actual revenue loss in all 4 cultures" (implies demand-collapse finding). DECLINE-VERDICT.md §4 states demand-collapse holds "strongly for the commodity-hardware segment" — consistent.
- *Labor-regime dependency:* REQUIREMENTS.md §6 states historical costs must be "adjusted upward" and names the modern-equivalent substitutions (electric blowers for bellows). DECLINE-VERDICT.md §4 states this "constrains cost estimates but not functional achievability" — consistent.
- *Supply-chain disappearance:* REQUIREMENTS.md §7 states "no anchor culture operated a supply-chain-autonomous forge" (framing the dependency as constant, not a collapse). DECLINE-VERDICT.md §4 states "bar steel is industrially available worldwide... the supply-chain falsifier is weaker for smithing" — consistent.
- *Regulatory capture:* REQUIREMENTS.md §10 (DIV-06) states regulatory preservation applies only to sword smithing and does not transfer to utility smithing. DECLINE-VERDICT.md §4 states regulatory constraints "are not the primary binding constraint" for modern utility smithing — consistent.

**Assessment: PASS** — falsifier analysis is consistent across both documents.

---

### Check 5: Scope Non-Overlap

| Document | Declared scope | Actual scope | Verdict |
|---|---|---|---|
| REQUIREMENTS.md | Functional requirements — what a forge must do | Mostly correct; §2's "How each culture achieved..." subsection drifts into forms territory (see REQ-07, P1 finding) | NEAR-PASS with P1 fix needed |
| HISTORICAL-FORMS.md | Descriptive comparative record — what historical forges looked like | Correct; one minor prescriptive sentence in §6 (see HF-04, P2) | PASS |
| DECLINE-VERDICT.md | Verdict on decline vs. restructuring | Correct; no duplication of forms or requirements content | PASS |
| SOURCES.md | Bibliography and placeholder audit | Correct; no analysis or prescription | PASS |

The primary scope overlap concern is the "How each culture achieved the temperature envelope" subsection in REQUIREMENTS.md §2, which describes bellows mechanisms, fuel types, and historical implementations at a level of detail that duplicates HISTORICAL-FORMS.md Table 1 bellows row content. This is the REQ-07 P1 finding. When that section is trimmed or moved, the scope non-overlap check will pass cleanly.

**Assessment: HOLD pending REQ-07 fix** — one P1 scope overlap; all other scope boundaries correct.

---

### Check 6: Plan C Readiness

**Can a Plan C author read these four docs and begin writing 15 catalog entries?**

Substantially yes, with the following conditions:

**Ready to use now:**
- HISTORICAL-FORMS.md — all four tables, the universal/contingent/unique taxonomy, and the divergence log are immediately usable as the historical context for `## Historical lineage` sections.
- DECLINE-VERDICT.md — the implications section (§5) is the most directly actionable document for Plan C: the plausibly-restorable vs. probably-not-restorable category list tells authors which product categories their entries should target.
- SOURCES.md — the placeholder audit is the verification queue; a Plan C author knows which citations are blocking and which are supporting.

**Requires fixes before use as specification:**
- REQUIREMENTS.md §9 summary table (R-01 through R-24) is the direct input specification. A Plan C author cannot reliably use R-01/R-02 (temperature) without the caveat that these values are inferred from process physics (see REQ-04). The sources_count frontmatter error (REQ-09) is minor but should be fixed before Plan C begins. The scope overlap in §2 (REQ-07) should be trimmed to avoid confusing authors about which document is the forms reference.

**Gaps that will affect catalog entries:**
- Throughput baselines (SOURCES.md P1-BLOCKING Placeholder #5: Langdon 1986 verification) remain unresolved. Plan C `sim_params.throughput_units_equiv_per_year` values will be based on author estimates, not sourced figures, unless this gap is closed.
- Archaeometallurgy temperature confirmation (Placeholder #4) is the highest-priority unresolved gap for the core specification (R-01/R-02).
- Horse population peak (Placeholder #2) is load-bearing for DECLINE-VERDICT's American frontier case; any catalog entry citing the frontier decline timeline needs this resolved.

**One-sentence Plan C readiness verdict:** Plan C catalog authorship can begin for the repair and specialty segments once REQUIREMENTS.md P1s are fixed (estimated: two edits); throughput `sim_params` must carry high-uncertainty flags until Langdon 1986 and horse-population are verified.

---

## Top 5 Findings (Priority for Plan C Unblocking)

**1. [P1] REQ-07 — REQUIREMENTS.md §2 scope drift duplicating HISTORICAL-FORMS.md**
The "How each culture achieved the temperature envelope" subsection in REQUIREMENTS.md §2 should be trimmed to a cross-reference. As written, it creates a parallel (and lower-quality) forms description that conflicts with HISTORICAL-FORMS.md Table 1. Plan C authors may treat it as a prescription rather than a requirement. *Fix: Replace subsection with a one-paragraph cross-reference to HISTORICAL-FORMS.md §2 and §6.* Estimated effort: 30 minutes.

**2. [P1] SRC-01 — SOURCES.md frontmatter `verified_source_count` miscounting**
`verified_source_count: 26` in SOURCES.md frontmatter includes 2 PARTIAL and 2 UNVERIFIED-BUT-HIGH-CONFIDENCE sources, which are not verified. Any downstream process that reads `verified_source_count` will believe there are 26 verified sources; there are 22. *Fix: Set `verified_source_count: 22`, add `partial_count: 2`, `unverified_high_confidence_count: 2`.* Estimated effort: 5 minutes.

**3. [P1] REQ-09 — REQUIREMENTS.md frontmatter `sources_count: 28` overcounts placeholders**
The frontmatter counts 4 CITATION-NEEDED entries (items 25–28 in §11) as sources. These are not sources; they are placeholders. *Fix: Set `sources_count: 24` (24 named sources); add a note that 4 additional placeholder gaps are tracked.* Estimated effort: 5 minutes.

**4. [P2] Cross-doc: R-19 "3-year minimum pipeline" overgeneralizes from a single-culture finding**
REQUIREMENTS.md R-19 states "3-year minimum pipeline in all 4 cultures for succession" — but this figure derives from the European guild model. The American frontier used shorter and more variable training. The claim is stated as universal when it is European-derived. *Fix: Add note to R-19: "The 3-year minimum reflects the European guild indenture model; all four cultures supported multi-year training pipelines, but duration varied (European guild: 3–7 years; Japanese detchi-boko: multi-year; American frontier: shorter and variable). The 3-year figure is a conservative minimum for the repair-dominant segment."* Estimated effort: 20 minutes.

**5. [P2] DV-05 — DECLINE-VERDICT.md missing capital formation constraint**
The verdict's falsifier analysis does not address the startup capital-formation barrier for modern forges. Historical smiths capitalized through guild fees, household accumulation, and patron investment — lower-cost mechanisms than modern commercial lending. Plan C catalog entries targeting the repair/specialty segment will face this constraint; the verdict should acknowledge it. *Fix: Add to §4 falsifier section: "A fifth constraint not in the original falsifiers — capital formation — is relevant to the startup scenario: modern forge capitalization at $18,000–$45,000 under commercial lending terms carries a debt-service burden absent from historical cost structures. This does not falsify the viability claim but affects the break-even timeline for new entrants without accumulated capital or institutional backing."* Estimated effort: 20 minutes.

---

## Needham Citation Fix Tracking

The Needham 1958 → 1965, vol. IV pt. 2 correction from CHECK-plan-b-citations.md requires propagation to specific locations. Current status across synthesis documents:

| Document | Location | Status |
|---|---|---|
| REQUIREMENTS.md §2 (hydraulic bellows) | Cites "Needham 1965, vol. IV pt. 2" | CORRECT |
| REQUIREMENTS.md §2 (fuigo paragraph) | No Needham citation | N/A |
| HISTORICAL-FORMS.md §2 Table 1 | Cites "Needham 1965, vol. IV pt. 2" | CORRECT |
| HISTORICAL-FORMS.md §6 (Song hydraulic bellows unique) | Cites "Needham 1965, vol. IV pt. 2" | CORRECT |
| HISTORICAL-FORMS.md §9 sources list item 3 | Reads "Needham, Joseph. 1958. *Science and Civilisation in China*, vol. IV" | **INCORRECT — fix required** |
| DECLINE-VERDICT.md §6 sources item 20 | Cites "Needham, Joseph. 1965. *Science and Civilisation in China*, vol. IV pt. 2" | CORRECT |
| SOURCES.md bibliography entry | Cites "Needham 1965, vol. IV, pt. 2: Physics and Physical Technology" | CORRECT |

One instance of the old citation remains: HISTORICAL-FORMS.md §9 sources list item 3. This must be corrected.

---

*Review complete. Four synthesis documents evaluated across P-4, P-5, P-6 (panel) and E-1, E-2, E-3 (editorial) lenses. Three P1 findings across two documents (REQUIREMENTS.md: 2; SOURCES.md: 1). Overall: HOLD pending P1 fixes. HISTORICAL-FORMS.md and DECLINE-VERDICT.md are Plan C-ready. REQUIREMENTS.md is Plan C-ready once P1s are resolved (estimated combined effort: ~1 hour of edits). SOURCES.md placeholder audit is immediately usable as the Plan C verification queue.*
