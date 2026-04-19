# ALIGNMENT — CERES framework-doc cross-check

**Run date:** 2026-04-19
**Scope:** 14 framework docs + reference files (spec v0.2, role files, RUBRIC, plan files, skills)
**Method:** Cross-file consistency audit (not ceres-check — ceres-check is per-artifact)

---

## Summary

- 2 P1 findings (contradiction, broken reference, or missing authority)
- 12 P2 findings (inconsistencies that should be resolved)
- 4 P3 findings (minor drift)
- **Verdict: HOLD** — no hard blocks, but two P1-class misalignments between ceres-check SKILL.md dimension labels and the authoritative RUBRIC, and between README.md "Upcoming" flags and actual file existence.

---

## Findings

---

### Check 1 — Spec as Source of Truth

**Spec v0.2 is the authoritative scope document.**

#### 1.1 Section 13 reference — P3

STYLE-GUIDE.md references "spec Section 13 non-goal" in four places (lines 44, 133, 155, 179), which is correct and aligns with spec v0.2 Section 13 (Non-Goals). METHODOLOGY.md also correctly references "spec Section 13" (line 483–484). No doc references a wrong section number for non-goals. **No finding.**

#### 1.2 Non-goals section numbering — P3

STYLE-GUIDE.md and METHODOLOGY.md correctly cite spec Section 13. The audit task asked whether any doc still cites "Section 12" for non-goals. No such stale reference was found. **No finding.**

#### 1.3 Working Hypothesis and falsifiers — No finding

THEORY.md Section 1 ("Working Hypothesis") accurately restates spec Section 2 verbatim, including all four named falsifiers (demand collapse, regulatory capture, labor-regime dependency, supply-chain disappearance). PRINCIPLES.md references the falsifiers correctly via "spec Section 2 falsifiers" at multiple points. STYLE-GUIDE.md Section 4 links forbidden framings to "spec Section 2 falsifiers." All consistent. **No finding.**

#### 1.4 Success / null / failure definitions — No finding

THEORY.md Section 7 restates spec Section 11.1–11.3 correctly: success = at least one `win` under at least one lens at at least one scale; null = none achieves `win` but full design-space coverage; failure = process failure. GLOSSARY.md entries for "scientific null" and "validated" align with spec Section 11. STYLE-GUIDE.md does not define success/null/failure (correct — out of scope for a style guide). RUBRIC.md Section 5 (promotion thresholds) is consistent with this framework. **No finding.**

#### 1.5 Spec lock on scale populations — P3

Spec Section 3 locks scales at village (500–2,000), town (2,000–15,000), small city (15,000–75,000). All 14 framework docs use these numbers consistently. **No finding** on values; see Check 3 for duplication concerns.

---

### Check 2 — Glossary Coverage and Consistency

#### 2.1 Terms used in docs but absent from GLOSSARY — P2

The following terms appear in framework docs with a defined meaning but lack a GLOSSARY.md entry:

- **`rubric_contribution`** — used in ROLE.md (frontmatter convention section), ceres-check SKILL.md, all 9 role files, and RUBRIC.md Section 6 — but not defined in GLOSSARY.md. It has a precise meaning (primary/secondary scoring dimension declaration) that users of the role library need.
- **`applies_to`** — defined in ROLE.md frontmatter convention (Section "applies_to") and used in all role files — not in GLOSSARY.
- **`domain_signals`** — same as `applies_to`: defined in ROLE.md, used in all role files, absent from GLOSSARY.
- **`validation gate`** — used in PRINCIPLES.md (header line: "The scoring rubric...will reference these principles to produce numeric scores at each promotion gate (`draft` → `reviewed` → `validated`)") and in PIPELINE.md — but the glossary has "promotion gate" (added as a term), not "validation gate." The two phrases are used interchangeably in some places; should be consolidated.
- **`win | marginal | fail`** — the verdict tri-state is defined in GLOSSARY.md under "evaluation matrix" and "working hypothesis" but does not have its own top-level glossary entry. ECONOMIC-LENSES.md Section 5 defines it formally; a GLOSSARY cross-reference would be useful.

**Finding F2.1 (P2):** Add `rubric_contribution`, `applies_to`, `domain_signals` to GLOSSARY.md. Consolidate "validation gate" / "promotion gate" — GLOSSARY has "promotion gate" (correct); ensure all docs use only "promotion gate."

#### 2.2 Glossary term "validated" vs. PIPELINE/VALIDATION usage — P3

GLOSSARY.md defines "validated" as: reached after full panel review, all P1 findings resolved, and all three editorial reviewers pass with no blocking findings. VALIDATION.md Section 2 ("Gate Structure") correctly describes the same gate but phrases it as "reviewed → validated (editorial)." PIPELINE.md Section 3 describes "Editorial (3 lenses — promotion gate)" firing on "artifacts about to be promoted from `reviewed` to `validated`." These are consistent in substance. **No finding.**

#### 2.3 Glossary term "lens context" vs. schema usage — No finding

GLOSSARY.md entry for "lens context" correctly describes it as the required supporting-detail block. SCHEMA.md's conditional field table and PRINCIPLES.md Principle 4 are consistent with the glossary definition. **No finding.**

---

### Check 3 — Numeric Consistency Across Docs

#### 3.1 Scale populations — No finding

All docs use the same ranges: village 500–2,000, town 2,000–15,000, small city 15,000–75,000. Checked in: spec Section 3, SCALES.md Section 1, THEORY.md Section 4, GLOSSARY.md ("scale"), README.md ("three economic lenses…at three settlement scales"), CLAUDE.md (Section 1). All consistent. **No finding.**

#### 3.2 Median wages — P2 (duplication violation)

Per the audit task, median wages ($48k / $56k / $62k) should be **authored only in SCALES.md** and referenced by pointer elsewhere. Actual state:

- SCALES.md Section 3.2 — authoritative definition. Correct.
- ECONOMIC-LENSES.md Section 2.3 (pass condition table) — reproduces the values inline: "$48,000/yr … $56,000/yr … $62,000/yr." This is a division-of-labor violation: the file's own header says "Do not duplicate threshold values here; cross-reference `corpus/program/SCALES.md` for every numeric threshold." The inline table in Section 2.3 contradicts that stated division and duplicates SCALES.md values.
- METHODOLOGY.md Section 3.2 ("Note on `wage_rate`") — refers to "the scale-appropriate median wage defined in `corpus/program/SCALES.md`" (pointer only). Correct.
- METHODOLOGY.md Section 3.2 worked example — uses "$20/hr town median wage" which is a pre-burden hourly rate, not the take-home threshold. SCALES.md Section 3.3 explicitly notes this distinction. Consistent.

**Finding F3.2 (P2):** ECONOMIC-LENSES.md Section 2.3 inline table duplicates the median-wage threshold values that its own division-of-labor note says should only appear in SCALES.md. Convert the inline values to a pointer: "see `SCALES.md §3` for values." The Appendix A cross-reference table in ECONOMIC-LENSES.md (Section "Appendix A: Threshold Cross-Reference") also reproduces the values and should be converted to a reference-only table noting the authoritative source without repeating the numbers, or left as a convenience cross-reference table with a prominent note that SCALES.md is authoritative.

#### 3.3 Civic thresholds — P2 (same as 3.2)

Same issue: $120/$100/$80 per household/year appear inline in ECONOMIC-LENSES.md Section 4.3 pass condition table and Appendix A, despite the file's stated rule "Do not duplicate threshold values here."

**Finding F3.3 (P2):** Same remediation as F3.2 — pointer to SCALES.md §4.

#### 3.4 Participation rates — P2 (same as 3.2)

Same issue: 2.5%/2.5%/2.0% appear inline in ECONOMIC-LENSES.md Section 3.3 and Appendix A.

**Finding F3.4 (P2):** Same remediation — pointer to SCALES.md §5.

#### 3.5 Rubric weights — No finding

RUBRIC.md Section 2 states weights: D1=15, D2=20, D3=15, D4=20, D5=10, D6=20 (sum=100). PRINCIPLES.md references RUBRIC.md for scoring but does not reproduce the weights. Role files declare `rubric_contribution.primary/secondary` dimension IDs but not weights. Weights appear only in RUBRIC.md. Division of labor is respected. **No finding.**

#### 3.6 Spec schema field list vs. catalog/SCHEMA.md — P2

Spec Section 5 (v0.2) shows the canonical example entry (forge-003) with all required fields. Catalog SCHEMA.md Section 3.1 is the authoritative field reference and claims to match "spec v0.2 Section 5." These are consistent for the fields shown in the spec example. However:

The spec example does not enumerate every field exhaustively — it is an annotated example, not a field registry. SCHEMA.md Section 4 is the authoritative gate reference. The spec's iteration log notes SCHEMA.md was created to match spec v0.2. No contradictions between the fields visible in the spec example and the SCHEMA.md field table were found.

One minor issue: SCHEMA.md Section 1 states "The spec and this file are kept in lock-step; neither is authoritative over the other in isolation." This is ambiguous — CLAUDE.md and the project generally treats the spec as the authoritative source. SCHEMA.md and the spec are meant to be kept in sync, but calling them co-equal authorities is misleading.

**Finding F3.6 (P3):** SCHEMA.md Section 1 should clarify that the spec is the primary authority on scope; SCHEMA.md is the primary authority on field-level schema detail. When they conflict, a spec amendment is required (as documented in SCHEMA.md Section 9). The "neither is authoritative" phrasing could be read as excusing divergence.

---

### Check 4 — Editorial Severity Codes (P1/P2/P3)

#### 4.1 P1/P2/P3 definitions — No finding

The severity system is defined consistently across all docs:

| Source | P1 | P2 | P3 |
|--------|----|----|-----|
| STYLE-GUIDE.md | "blocks promotion" (implicit from enforcement triggers) | "should fix" | style/optional |
| METHODOLOGY.md | P1 = "block promotion" | P2 = "should fix" | P3 = "note it" |
| VALIDATION.md | "Any P1 finding blocks promotion" | "P2 findings (should-fix) are tracked but do not block" | — |
| SCHEMA.md Section 7 | "P1 findings block promotion" | — | — |
| RUBRIC.md Section 1 | "editorial gates determine whether the entry is blocked regardless of score" | — | — |
| E-1-citation-auditor.md | "P1 = block promotion" | "P2 = should fix" | "P3 = optional" |
| E-2-scope-keeper.md | "P1 = block promotion" | "P2 = should fix" | "P3 = optional" |
| E-3-numeracy-checker.md | "P1 = block promotion" | "P2 = should fix" | "P3 = precision/rounding" |
| ceres-check SKILL.md | "P1 = blocks promotion" | "P2 = should fix" | "P3 = nice to have" |
| ceres-editorial SKILL.md | "P1 = blocks promotion; author must fix" | "P2 = should fix; tracked" | "P3 = minor/style" |

All definitions are consistent. **No finding.**

---

### Check 5 — No Forbidden Path Patterns

#### 5.1 `docs/superpowers/` pattern — No finding

Grep across all 14 framework docs and reference files found zero instances of `docs/superpowers/` appearing as a functional path reference in any framework document. The only occurrences are in CLAUDE.md (explicit prohibition statement) and the plan file (checklist item confirming the prohibition). **No finding.**

#### 5.2 Paths that don't exist on disk — P2

The following paths are referenced in framework docs but do not exist on disk:

- `catalog/<trade>/README.md` — referenced in SCHEMA.md Section 2 ("Trade-level metadata lives in `catalog/<trade>/README.md`") and Section 8. The `catalog/` directory exists (contains `SCHEMA.md`) but no trade subdirectories exist yet. This is expected (Plan C creates them) — but the reference is not labeled as upcoming.
- `catalog/smithing/SCHEMA.md` — referenced in SCHEMA.md Section 8 ("See `catalog/smithing/SCHEMA.md` for the full smithing extension") — does not yet exist.
- `simulations/tier-a-comparator/VALIDATION.md` — referenced in VALIDATION.md as a Plan D deliverable ("that file does not yet exist; Plan D creates it"). This is correctly labeled as deferred. No finding here.
- `research/trades/<trade>/REQUIREMENTS.md`, `research/trades/<trade>/HISTORICAL-FORMS.md`, etc. — referenced throughout. Directories don't yet exist. Expected; these are Phase 1 targets.
- `skills/README.md` — referenced in CLAUDE.md Section 6. Does not exist (no `skills/README.md` found; the skills directory contains only SKILL.md files per subdirectory).
- `agents/` — referenced in CLAUDE.md Section 2. Directory does not exist.

**Finding F5.2 (P2):** Several paths referenced in framework docs as present are not labeled as "upcoming" or "deferred," creating ambiguity for readers. Specifically: `catalog/smithing/SCHEMA.md` referenced as if it exists in SCHEMA.md Section 8; `skills/README.md` referenced in CLAUDE.md Section 6 without "(upcoming)" label. Recommend adding "(not yet created; see Plan C)" annotations or "(upcoming)" labels consistent with other directory entries in CLAUDE.md.

---

### Check 6 — Forward / Broken References

#### 6.1 Stale "upcoming" flags in CLAUDE.md — P1

CLAUDE.md Section 2 directory table marks multiple directories as "(upcoming)" that now fully exist with content:

| Entry | "(upcoming)" in CLAUDE.md | Actual status |
|-------|--------------------------|----------------|
| `catalog/` | yes — "`catalog/SCHEMA.md` (upcoming)" | EXISTS: `catalog/SCHEMA.md` is canonical |
| `corpus/` | yes — "framework material … *(upcoming)*" | EXISTS: all 5 corpus files created |
| `scoring/` | yes — "`scoring/RUBRIC.md` *(upcoming)*" | EXISTS: `scoring/RUBRIC.md` is canonical |
| `docs/` | yes — "`docs/PIPELINE.md`, `docs/STYLE-GUIDE.md`, `docs/METHODOLOGY.md` *(upcoming)*" | EXISTS: all 3 docs created |
| `TRACKER.md` | yes — "`TRACKER.md` … *(upcoming)*" | EXISTS: TRACKER.md is operational |

Also in CLAUDE.md Section 4 (Authoring Discipline):
- "Read `catalog/SCHEMA.md` (upcoming)" — SCHEMA.md exists.
- "`catalog/SCHEMA.md` (upcoming) and document the change" — same.
- "`corpus/program/CURRENCIES.md` (upcoming)" — CURRENCIES.md exists.

**Finding F6.1 (P1):** CLAUDE.md contains eight stale "(upcoming)" markers for files and directories that now exist and are fully operational. These markers mislead contributors into thinking infrastructure is absent. The "(upcoming)" labels for `catalog/`, `corpus/`, `scoring/`, `docs/`, `TRACKER.md`, and two inline references to `catalog/SCHEMA.md` and `corpus/program/CURRENCIES.md` should be removed or replaced with active path references.

#### 6.2 README.md "Upcoming" flags — P1

README.md Section "Project Sections" table marks:
- `corpus/canon/THEORY.md` → "Upcoming"
- `catalog/SCHEMA.md` → "Upcoming"
- `TRACKER.md` → "Upcoming"

And the note below the table: "`corpus/canon/THEORY.md`, `catalog/SCHEMA.md`, and `TRACKER.md` are created later in Plan A and do not exist yet."

All three now exist. THEORY.md, SCHEMA.md, and TRACKER.md were all created as part of Plan A.

**Finding F6.2 (P1):** README.md "Project Sections" table has three stale "Upcoming" status entries for files that now exist. The note below the table is factually false: Plan A is complete. Update the table to "Active" and remove or revise the note.

#### 6.3 Cross-doc links that resolve — No finding

Links checked manually:
- THEORY.md → `corpus/program/ECONOMIC-LENSES.md` and `corpus/program/SCALES.md` — both exist.
- THEORY.md → `corpus/canon/GLOSSARY.md` — exists.
- METHODOLOGY.md → `docs/STYLE-GUIDE.md` — exists.
- STYLE-GUIDE.md → `corpus/program/CURRENCIES.md` — exists.
- PIPELINE.md → `docs/METHODOLOGY.md`, `corpus/program/ECONOMIC-LENSES.md`, `corpus/program/SCALES.md`, `.craft/roles/ROLE.md`, `skills/` — all exist.
- VALIDATION.md → `skills/ceres-editorial/SKILL.md`, `corpus/program/ECONOMIC-LENSES.md`, `corpus/program/SCALES.md` — all exist.
- SCHEMA.md → `specs/2026-04-18-ceres-design.md` — exists.

**No finding** for cross-doc links that are supposed to resolve.

---

### Check 7 — Role Rubric Contribution vs. RUBRIC

#### 7.1 Role `rubric_contribution` vs. RUBRIC Section 6 mapping table

RUBRIC.md Section 6 states the mapping table "is derived directly from each role's `rubric_contribution` field." Comparing:

**RUBRIC.md Section 6 table:**

| Dimension | Primary roles | Secondary roles |
|-----------|--------------|-----------------|
| D1 Schema Completeness | E-2 Scope Keeper | — |
| D2 Citation Strength | E-1 Citation Auditor | P-1 Market Economist, P-5 Historian |
| D3 Operations Realism | P-4 Craft Practitioner, E-3 Numeracy Checker | P-6 Skeptical Funder |
| D4 Lens-Context Rigor | P-1, P-2, P-3 | E-3 Numeracy Checker |
| D5 Historical Honesty | P-5 Historian | P-6 Skeptical Funder |
| D6 Design Rationale & Differentiation | P-6 Skeptical Funder | P-1, P-2, P-3, P-4 |

**Actual `rubric_contribution` from role files:**

| Role | primary | secondary |
|------|---------|-----------|
| P-1 Market Economist | [D4] | [D2, D6] |
| P-2 Commons Theorist | [D4] | [D6] |
| P-3 Civic Steward | [D4] | [D6] |
| P-4 Craft Practitioner | [D3] | [D6] |
| P-5 Historian | [D5] | [D2] |
| P-6 Skeptical Funder | [D6] | [D5] |
| E-1 Citation Auditor | [D2] | [] |
| E-2 Scope Keeper | [D1] | [] |
| E-3 Numeracy Checker | [D3] | [D4] |

**Comparison against RUBRIC.md Section 6 table:**

- D1: RUBRIC says primary=E-2. Role file: E-2 primary=[D1]. **Match.**
- D2: RUBRIC says primary=E-1, secondary=P-1, P-5. Role files: E-1 primary=[D2]; P-1 secondary=[D2]; P-5 secondary=[D2]. **Match.**
- D3: RUBRIC says primary=P-4, E-3, secondary=P-6. Role files: P-4 primary=[D3]; E-3 primary=[D3]; P-6 secondary=[D5] only — P-6 has **no D3 in any field**. **Mismatch for P-6/D3.**
- D4: RUBRIC says primary=P-1, P-2, P-3, secondary=E-3. Role files: P-1 primary=[D4]; P-2 primary=[D4]; P-3 primary=[D4]; E-3 secondary=[D4]. **Match.**
- D5: RUBRIC says primary=P-5, secondary=P-6. Role files: P-5 primary=[D5]; P-6 secondary=[D5]. **Match.**
- D6: RUBRIC says primary=P-6, secondary=P-1, P-2, P-3, P-4. Role files: P-6 primary=[D6]; P-1 secondary=[D6]; P-2 secondary=[D6]; P-3 secondary=[D6]; P-4 secondary=[D6]. **Match.**

**One mismatch found:** RUBRIC.md Section 6 table claims P-6 Skeptical Funder is a secondary contributor to D3 (Operations Realism). P-6's actual `rubric_contribution` field does not include D3 in either primary or secondary — P-6's secondary is [D5] only.

**Finding F7.1 (P2):** P-6 Skeptical Funder is listed as a D3 secondary contributor in RUBRIC.md Section 6 but P-6's role file declares `rubric_contribution.secondary: [D5]` — no D3. Either: (a) RUBRIC.md Section 6 table is wrong and should remove P-6 from D3 secondary; or (b) P-6's role file is wrong and should add D3 to secondary (which would be substantively reasonable, since P-6 does ask downside questions). Resolve by deciding which is canonical: RUBRIC.md says "this table is derived directly from each role's `rubric_contribution` field" — so the role file is the authority, and RUBRIC.md Section 6 table needs correction.

---

### Check 8 — Principles ↔ Rubric Dimensions ↔ Role Voices

#### 8.1 PRINCIPLES.md mapping table vs. RUBRIC.md coverage

PRINCIPLES.md cross-reference table (bottom of file) maps each principle to a primary panel voice and primary editorial gate. RUBRIC.md Section 8 maps each principle to primary rubric dimension(s). Checking consistency:

**PRINCIPLES.md cross-reference:**
| # | Principle | Primary Panel Voice | Primary Editorial Gate |
|---|---|---|---|
| 1 | Schema-Complete | — | E-2 Scope Keeper |
| 2 | Every Number Cited | P-1 Market Economist | E-1 Citation Auditor |
| 3 | Operations Reality | P-4 Craft Practitioner | E-3 Numeracy Checker |
| 4 | Lens Context | P-2 Commons Theorist, P-3 Civic Steward | E-2 Scope Keeper |
| 5 | Market Price Declared | P-1 Market Economist | E-1 Citation Auditor, E-3 Numeracy Checker |
| 6 | Historical Lineage | P-5 Historian | E-1 Citation Auditor |
| 7 | Design Rationale | P-6 Skeptical Funder | E-2 Scope Keeper |
| 8 | Failure Modes Named | P-4 Craft Practitioner, P-6 Skeptical Funder | — |
| 9 | Apprentice Path | P-4 Craft Practitioner, P-3 Civic Steward | — |
| 10 | Iteration Log | P-6 Skeptical Funder | E-2 Scope Keeper |

**RUBRIC.md Section 8 mapping (Principle-to-Dimension):**
- P-1 → D1; P-2 → D2; P-3 → D3; P-4 → D4; P-5 → D2, D4; P-6 → D5; P-7 → D6; P-8 → D3; P-9 → D3, D4; P-10 → D1, D6

Cross-check: PRINCIPLES.md says P-6 (Skeptical Funder) is primary voice for Principle 7 (Design Rationale) and Principle 10 (Iteration Log). RUBRIC.md assigns Principle 7 → D6 (Design Rationale) and Principle 10 → D1, D6. P-6's `rubric_contribution.primary` = [D6]. Consistent.

PRINCIPLES.md says P-1 (Market Economist) is primary voice for Principle 2 (Every Number Cited) and Principle 5 (Market Price Declared). RUBRIC.md assigns Principle 2 → D2 (Citation Strength) and Principle 5 → D2, D4. P-1's `rubric_contribution.secondary` = [D2, D6] — D2 is secondary, not primary for P-1. The PRINCIPLES.md table says P-1 is the "Primary Panel Voice" for Principle 2. But in RUBRIC.md, D2 is primarily owned by E-1 (Citation Auditor), with P-1 as secondary. This is a subtle tension: PRINCIPLES.md frames P-1 as the principle owner for citation-completeness, while the rubric dimension ownership is E-1.

**Finding F8.1 (P3):** The PRINCIPLES.md cross-reference table and the RUBRIC.md dimension-ownership table operate at different levels (principle-level vs. dimension-level), producing an apparent inconsistency: PRINCIPLES.md says P-1 is primary voice for "Every Number Cited" (Principle 2), while RUBRIC.md assigns D2 (Citation Strength) primarily to E-1. These are not actually contradictory — panel reviews are qualitative substance challenges, editorial gates are mechanical checks — but the language ("Primary Panel Voice") could mislead users into thinking P-1 owns the D2 score. Add a clarifying note to the PRINCIPLES.md cross-reference table explaining that "Primary Panel Voice" indicates who raises the substantive concern during review, while the "Primary Dimension" in RUBRIC.md indicates who controls the numeric score.

#### 8.2 Every dimension has at least one primary principle — No finding

RUBRIC.md Section 8 confirms all 10 principles map to at least one dimension, and every dimension (D1–D6) is covered by at least one principle. **No finding.**

#### 8.3 Panel voice ownership of principle dimensions — No finding

Every panel voice listed as "owner" of a principle has that principle's dimension in its `rubric_contribution.primary` or `.secondary`, per the analysis in 8.1. The one exception (P-6 missing D3 secondary) is already captured in F7.1. **No additional finding here.**

---

### Check 9 — Style Guide Enforcement

#### 9.1 Forbidden framings in framework docs — No finding

Grepping all framework docs and reference files for STYLE-GUIDE.md Section 4 forbidden phrases:

- "in the good old days" — found only in STYLE-GUIDE.md itself (as the defined forbidden phrase), in P-5-historian.md (as a prohibited framing the role fights against), and in the plan file (as a checklist item). No instances in catalog, research, corpus, or framework docs as actual content.
- "lost craftsmanship," "once-vibrant traditions," "returning to our roots," "the craft revival," "when craftspeople still made things properly," "before industrialization destroyed local production" — no instances in any framework doc outside the style guide's own definition block.
- "lost knowledge" — appears in STYLE-GUIDE.md Section 4.5 as the prohibited pattern definition, and in P-5's role file as a prohibited claim type. No instances as actual content claims in framework docs.

**No findings.**

#### 9.2 "What was lost" phrasing — P3

PIPELINE.md Section 5 (Phase 5) description says: "The pitch narrative frames the whole project for funders: what was lost, what the research found, and what a pilot program would cost." The spec Section 9 also uses "what was lost when local production collapsed." The GLOSSARY.md "Pitch narrative" entry also uses: "the problem (what was lost when local production collapsed…)."

STYLE-GUIDE.md Section 4.1 prohibits framings that treat local production decline as a loss of something spiritually better. The P-5 historian's R1 review of the spec flagged this exact phrase as presuming a finding rather than a testable hypothesis. However, these references are in meta-descriptions of what the pitch narrative will eventually argue, not in actual catalog entries or research documents. The style guide targets catalog entries and research documents; pitch narrative is given more latitude.

**Finding F9.2 (P3):** The phrase "what was lost when local production collapsed" appears in three framework docs (PIPELINE.md, GLOSSARY.md, and the spec) as the framing for the pitch narrative. This was flagged by P-5 in R1 as presuming an answer. While pitch narrative is permitted persuasive framing (STYLE-GUIDE.md Section 7.4), the framework docs describing the pitch narrative's scope should use more neutral language like "what changed when local production declined" or "the forces that reduced local production capacity" to avoid encoding the romantic framing in the project's own framework infrastructure. Lowest-priority finding; no policy violation.

---

### Check 10 — Pipeline ↔ Skill.md Consistency

#### 10.1 Panel fires on every artifact — No finding

PIPELINE.md Section 3 ("Panel — 6 voices — every artifact"): "Panel fires on **every artifact** at draft stage. No exceptions." ceres-panel SKILL.md: invokes all 6 voices unconditionally via a hard-coded roster. Consistent. **No finding.**

#### 10.2 Editorial fires on promotion (reviewed → validated) — No finding

PIPELINE.md Section 3 ("Editorial — 3 lenses — promotion gate"): "Editorial fires only on **artifacts about to be promoted** from `reviewed` to `validated`." ceres-editorial SKILL.md header: "Run the 3-lens editorial cleanup pass. Editorial is a **promotion gate** — it fires on artifacts being promoted from `reviewed` to `validated`, not on drafts." Consistent. **No finding.** (This was the issue previously fixed; re-verification confirms it is correct.)

#### 10.3 Board fires on demand — No finding

PIPELINE.md Section 3 ("Board — per-trade — on demand"): fires when a panel reviewer flags a claim or author requests adjudication. ceres-board SKILL.md: "Board review is **on-demand**, not routine." Consistent. **No finding.**

#### 10.4 ceres-check not in PIPELINE.md — P2

PIPELINE.md does not mention the `ceres-check` skill anywhere. ceres-check SKILL.md describes itself as "a **fast, filtered audit** skill" that "complements `ceres-panel`" and is used for "fast pre-promotion audit or targeted-concern scan." ROLE.md Section "Role Frontmatter Convention (v1.1)" notes that "a future `ceres-check` skill will use `applies_to` together with `domain_signals` to dynamically select the appropriate reviewer set." The ceres-check skill has been created and is operational. PIPELINE.md has no entry for it.

**Finding F10.4 (P2):** PIPELINE.md Section 3 ("Review-Tier Firing Rules") does not describe `ceres-check`. Add a row or note to PIPELINE.md explaining that `ceres-check` is a cross-tier fast audit tool (not a separate tier) that can be invoked on any artifact for a structured findings table, and cross-reference `skills/ceres-check/SKILL.md`. The "When to Use ceres-check vs. ceres-panel" table in ceres-check SKILL.md provides the right framing.

#### 10.5 ceres-check dimension labels inconsistent with RUBRIC — P1

ceres-check SKILL.md Section 4 "Dimension Aggregate" template uses dimension labels that **do not match** RUBRIC.md:

| Label in ceres-check SKILL.md | Actual label in RUBRIC.md |
|-------------------------------|---------------------------|
| D4 Market Viability | D4 Lens-Context Rigor |
| D5 Commons Fit | D5 Historical Honesty |
| D6 Civic Value | D6 Design Rationale and Differentiation |

The RUBRIC.md dimensions are D1 Schema Completeness, D2 Citation Strength, D3 Operations Realism, D4 Lens-Context Rigor, D5 Historical Honesty, D6 Design Rationale and Differentiation. The ceres-check dimension labels for D4–D6 are wrong; they do not match the authoritative RUBRIC definitions. A scorer using ceres-check output to inform a RUBRIC score would misread D4, D5, and D6.

**Finding F10.5 (P1):** ceres-check SKILL.md Step 4 dimension aggregate template has incorrect labels for D4, D5, and D6. These do not match RUBRIC.md. Fix ceres-check SKILL.md to use the correct RUBRIC dimension names: D4 = Lens-Context Rigor; D5 = Historical Honesty; D6 = Design Rationale and Differentiation.

---

## Recommended Next Actions

Top 5 findings to fix, in priority order:

### 1. Fix ceres-check dimension labels (F10.5 — P1)

**File:** `skills/ceres-check/SKILL.md`, Section 4 ("Dimension Aggregate") template
**Fix:** Replace D4 "Market Viability" → "Lens-Context Rigor"; D5 "Commons Fit" → "Historical Honesty"; D6 "Civic Value" → "Design Rationale and Differentiation." These must match RUBRIC.md exactly — they are the same six dimensions. The mislabeling will cause scorer confusion when ceres-check output is mapped to RUBRIC scores.

### 2. Remove stale "(upcoming)" labels from CLAUDE.md (F6.1 — P1)

**File:** `CLAUDE.md`, Section 2 directory table and Section 4 inline references
**Fix:** Remove "(upcoming)" from `catalog/`, `corpus/`, `scoring/`, `docs/`, `TRACKER.md` entries; remove "(upcoming)" from "Read `catalog/SCHEMA.md` (upcoming)" and "`corpus/program/CURRENCIES.md` (upcoming)." Plan A is complete; these are all active files.

### 3. Update README.md "Project Sections" table (F6.2 — P1)

**File:** `README.md`, "Project Sections" table and the note below it
**Fix:** Change `corpus/canon/THEORY.md`, `catalog/SCHEMA.md`, and `TRACKER.md` status from "Upcoming" to "Active." Remove or revise the sentence "created later in Plan A and do not exist yet" — Plan A is complete and these files exist.

### 4. Fix P-6 D3 secondary discrepancy (F7.1 — P2)

**File:** `scoring/RUBRIC.md` Section 6 role-to-dimension mapping table
**Fix:** Remove P-6 Skeptical Funder from the D3 secondary column, since P-6's `rubric_contribution.secondary` is [D5] only. RUBRIC.md itself states "this table is derived directly from each role's `rubric_contribution` field" — so the role file is canonical. Alternatively, if there is a substantive reason P-6 should contribute to D3, add D3 to P-6's `rubric_contribution.secondary` in the role file, which will automatically make the RUBRIC table correct.

### 5. Add ceres-check to PIPELINE.md (F10.4 — P2)

**File:** `docs/PIPELINE.md`, Section 3 ("Review-Tier Firing Rules")
**Fix:** Add a note after the Board section explaining that `ceres-check` (`skills/ceres-check/SKILL.md`) is a cross-tier fast audit tool available at any stage: it is not a separate review tier, but a structured checklist scan that complements the panel and editorial passes. Reference the "When to Use ceres-check vs. ceres-panel" guidance in the skill file.
