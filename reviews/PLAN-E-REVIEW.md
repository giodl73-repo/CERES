---
review_type: cross-artifact
artifacts:
  - playbook/smithing/village.md
  - playbook/smithing/town.md
  - playbook/smithing/small-city.md
  - playbook/pitch/PITCH-NARRATIVE.md
reviewer_lenses: [P-1-market, P-2-commons, P-3-civic, P-5-historian, P-6-skeptical-funder]
date: 2026-04-19
verdict: HOLD
p1_count: 0
p2_count: 6
p3_count: 5
---

# Plan E Cross-Artifact Review — Smithing Playbooks + Pitch Narrative

**Artifacts reviewed:** `playbook/smithing/village.md`, `playbook/smithing/town.md`,
`playbook/smithing/small-city.md`, `playbook/pitch/PITCH-NARRATIVE.md`

**Review type:** Pragmatic cross-artifact pass (research-doc artifact type; not formal
ceres-panel). Five lenses applied: P-5 Historian (anti-romanticism, decline citations),
P-6 Skeptical Funder (pitch objections, budget), P-1 Market / P-2 Commons / P-3 Civic
(lens rules, entry citations), cross-doc consistency, style-guide adherence (§4
forbidden framings, §7 voice).

**Overall verdict: HOLD** — no P1s blocking; 6 P2s require fix before external
circulation. Recommend fixing the payback-table errors in small-city.md (P2-01 through
P2-03) before proceeding. Remaining P2s and all P3s can be addressed in a fast
follow-up pass without architectural changes.

---

## Summary Counts

| Priority | Count |
|---|---|
| P1 (blocking) | 0 |
| P2 (should fix) | 6 |
| P3 (minor / nice-to-have) | 5 |

---

## P2 Findings (Should Fix Before External Circulation)

| ID | Location | Lens | Issue | Suggested Fix |
|---|---|---|---|---|
| P2-01 | `small-city.md` §Lens 1 Market table | P-1 Market | forge-002 payback listed as `0.67` yr but catalog `small_city_market.primary_metric` = 0.179. The 0.67 value is forge-006's payback. Table entries for forge-002 and forge-003 appear shifted by two rows. | Set forge-002 payback to `0.18`, forge-003 to `0.44` in the table. Verify remaining rows against `SUMMARY.md`. |
| P2-02 | `small-city.md` §Lens 1 Market table | P-1 Market | forge-003 payback listed as `0.88` yr; catalog `small_city_market.primary_metric` = 0.436. 0.88 is forge-010's value. | Set forge-003 payback to `0.44`. |
| P2-03 | `small-city.md` §Lens 1 Market table | P-1 Market | forge-012 payback listed as `0.88` yr; catalog `small_city_market.primary_metric` = 0.306. 0.88 is forge-010's value appearing twice. | Set forge-012 payback to `0.31`. |
| P2-04 | `small-city.md` §Lens 2 Cooperative table, body text | P-2 Commons | Break-even range stated as "77–134 members" in the table header but the body text says "break-even member count ranges from 15 to approximately 90 across the 15 catalog entries" — the town playbook uses that same 90-member ceiling. The civic-primary entries (forge-004, forge-011) are not production designs; using them as the low-end of a break-even range for the cooperative lens is misleading framing. The range 77–124 comes from the two civic entries and forge-009 specifically; general-catalog entries have lower break-evens. Clarify the denominator of the range. | Restate: "break-even member counts range from 15 (forge-001, forge-014) to 124 (forge-009) across all 15 entries; feasible pool 900 clears all with margin." Drop the 77–134 table row phrasing which conflates civic and cooperative entries. |
| P2-05 | `pitch/PITCH-NARRATIVE.md` §4 Finding 2, coop member pool | P-2 Commons | The pitch states "feasible pool is estimated at 2.5% of settlement population [corpus/program/SCALES.md §5]" for village (pool ~31) and town (pool ~213). But `small-city.md` §Lens 2 uses "2% participation rate of 45,000 midpoint population" = 900 members — inconsistently citing 2% where other docs use 2.5%. At 2.5% of 45,000 the pool would be 1,125 not 900. The pitch uses 900 (consistent with small-city.md) but attributes the formula to "2.5%" which gives the wrong number. | Either use 2.5% consistently (pool ~1,125 at small-city) or document that the small-city participation rate assumption is 2% (lower due to urban alternative-activity density). If the 2% figure is intentional, cite SCALES.md §5 accordingly or note the adjustment. |
| P2-06 | `town.md` §Civic table, forge-004 civic note | P-3 Civic | Town playbook's Sketch A states forge-003 "per_hh cost at town scale is $2.01 vs. the $100 threshold — it would clear civic if re-authored with annual_public_use_hours." The pitch (§4 Finding 3) does not mention this; it only names forge-004 and forge-011 as civic winners. No inconsistency in the win/fail count, but the town playbook's civic-compatibility note for forge-003 could mislead a reader into believing forge-003 is close to civic status. Clarify: forge-003 currently fails civic because it lacks the `annual_public_use_hours` field — and adding that field would be a catalog-authoring change (Plan F scope), not a finding of this slice. | Add a parenthetical: "This would require a Plan F catalog revision to forge-003; it is not a current civic win." |

---

## P3 Findings (Minor — Address in Next Pass)

| ID | Location | Lens | Issue | Suggested Fix |
|---|---|---|---|---|
| P3-01 | `village.md` §Market section, forge-012 entry | P-5 Historian | Farriery described as "the one smithing niche that never went through industrial displacement because you cannot ship a horse's feet to a factory [DECLINE-VERDICT §2.4]." DECLINE-VERDICT §2.4 describes the American frontier Stage 2 (motorized agriculture demand collapse) and mentions farriery only in passing; the "never displaced" framing is not explicitly sourced to that section. The section number citation is imprecise. | Tighten to: "Farriery persisted because the service is physically location-bound — a structural characteristic the historical record documents consistently [DECLINE-VERDICT §5]." Remove the §2.4 citation for this specific claim. |
| P3-02 | `pitch/PITCH-NARRATIVE.md` §2 The Problem | P-5 Historian | Pitch states Birmingham hardware factories "undercut hand-forged nails by factors of three to ten [medieval-northern-europe §8]." The medieval-northern-europe chapter covers pre-industrial northern Europe, not Birmingham. The Birmingham factory displacement happened in the 18th–19th century, which is closer to the American frontier narrative. Citing the medieval chapter for a Birmingham claim is a period misattribution. | Cite `research/cultures/american-frontier/smithing.md` or `DECLINE-VERDICT §2.1` (northern Europe industrial transition) for the Birmingham factory claim; reserve medieval-northern-europe §8 for its correct period. |
| P3-03 | `small-city.md` §Scale Framing | P-5 Historian | Final paragraph states "All 7 market-win designs target repair, specialty, or custom niches. Any operator who targets commodity hardware production is entering a market segment industrial production dominates on price, consistency, and availability." This is accurate per DECLINE-VERDICT. However the sentence is presented without an inline citation. For a load-bearing pitch-supporting claim this is fine in a playbook, but the paragraph would be stronger with a DECLINE-VERDICT §5 cite. | Add `[DECLINE-VERDICT.md §5]` inline after "availability." |
| P3-04 | `pitch/PITCH-NARRATIVE.md` §6 Objection B | P-6 Skeptical Funder | Objection B response states "DECLINE-VERDICT carries 30 verified references with 6 remaining citation-needed gaps in specific sub-claims." This is a factual claim about the project's own citation state — and should be verified at review time rather than trusted as static. If DECLINE-VERDICT's source count has changed (or the 6 gaps have been closed), the pitch will be out of date. | Add a note to verify this count against DECLINE-VERDICT §6/Sources before external distribution. Consider replacing with "carries [N] verified references with [M] identified citation-needed gaps" where N and M are freshly verified. |
| P3-05 | `town.md` §Matrix Summary — market wage threshold | P-1 Market | Town playbook header states "Market lens wage threshold: $56,000 / yr." Village playbook uses $48,000. The small-city playbook uses $62,000. These scale-varying wage thresholds derive from SCALES.md §3 but none of the playbooks cite SCALES.md §3 for the specific wage threshold figure in the summary table. | Add `[SCALES.md §3]` to the wage threshold row in town.md's Matrix Summary table (village.md does cite SCALES.md §3, §4, §5 in its Sources section but not inline; small-city.md similarly). Low priority; sources section covers it but inline would be tighter. |

---

## Cross-Doc Consistency Audit

### Verdict consistency

The matrix win/fail counts are internally consistent across the four documents:

| Cell | village.md | town.md | small-city.md | pitch |
|---|---|---|---|---|
| market wins | 7/15 | 7/15 | 7/15 | 7/8 fail (consistent) |
| coop village | 2/15 | referenced (2 coop wins at village) | referenced | 2/15 |
| coop town | — | 15/15 | 15/15 | 15/15 |
| coop small_city | — | — | 15/15 | 15/15 |
| civic wins | 2/15 (forge-004, forge-011) | 2/15 | 2/15 | 2/15 |

All four documents agree on which entries win which cells. The seven market winners (forge-002, forge-003, forge-005, forge-006, forge-010, forge-012, forge-013) are consistently identified. The two civic winners (forge-004, forge-011) are consistently identified. No verdict contradictions found.

### Per-household cost consistency

| Entry | Scale | village.md | town.md | small-city.md | pitch |
|---|---|---|---|---|---|
| forge-004 | village | $28.73/hh | — | — | — |
| forge-004 | town | — | $4.23/hh | — | $4.23/hh |
| forge-004 | small_city | — | — | $0.80/hh | $0.80/hh |
| forge-011 | village | $43.80/hh | — | — | — |
| forge-011 | town | — | $6.44/hh | — | $6.44/hh |
| forge-011 | small_city | — | — | $1.22/hh | $1.22/hh |

All per-household cost figures are consistent across documents. The civic threshold values are consistent (village $120, town $100, small-city $80).

### Payback figure consistency

Market winners' payback figures are consistent between village.md, town.md, and the pitch. The three discrepancies are all in small-city.md's market table (P2-01 through P2-03 above). All other payback figures match the catalog source entries.

### DECLINE-VERDICT citation consistency

All four documents cite DECLINE-VERDICT §4 or §5 for the mixed verdict and restorable categories. Village.md cites §5 for repair being "most durable" (DECLINE-VERDICT uses "most durable segment" — close paraphrase, not a misquote). Pitch §2 correctly describes the three distinct decline trajectories: commodity hardware, repair/maintenance, specialty. No romanticism or false "golden age" framing detected in any of the four documents. P-5 Historian assessment: anti-romanticism standard maintained.

---

## P-5 Historian Assessment — DECLINE-VERDICT Framing

**Pass with one P3.** All four documents correctly state the mixed verdict. All avoid the STYLE-GUIDE §4 forbidden framings (no "golden age," "once-vibrant traditions," "lost craftsmanship"). The pitch's "The Problem" section (§2) is the highest-risk section for romanticism and passes: it explicitly states "the honest answer is not romantic" and frames the loss in economic-capacity terms, not cultural terms. The Birmingham factory citation has a period-attribution imprecision (P3-02) but does not introduce a false historical claim.

---

## P-6 Skeptical Funder Assessment — Pitch Narrative

**Solid with acknowledged gaps.** The pitch's three objections (Objection A — method scope; Objection B — data quality; Objection C — civic failure rate) are the correct objections and the responses are honest. Most importantly:

- Objection A acknowledges the generalizability gap directly and does not overclaim.
- Objection B admits the [CITATION-NEEDED] gaps and correctly frames the pilot as the mechanism to replace estimates with data.
- Objection C correctly explains why 13 civic fails are expected, not a problem.

The budget tables use phrase "order-of-magnitude figures derived from catalog entry economics, not supplier quotes" — appropriate research-paper-level qualification.

The one structural concern for a funder: the Executive Summary states a budget envelope of "$450,000–$1.8M over two years" but §5 Budget tables show a range of "$410,000–$530,000 (low)" to "$1,450,000–$2,000,000 (high)." The exec summary upper bound ($1.8M) is below the high-version high ($2.0M). This is a minor presentation inconsistency — the exec summary rounds $2.0M down to $1.8M without explanation. A funder cross-referencing the exec summary against the detailed tables will notice. This is a P3 presentation issue, already captured implicitly in the P3 findings above; noting it here for completeness.

---

## P-1 Market / P-2 Commons / P-3 Civic Lens Rule Compliance

### Market lens (P-1)

All three playbooks correctly apply the market lens: payback ≤ 8 years AND operator take-home ≥ scale-appropriate wage median. The seven winners (forge-002, forge-003, forge-005, forge-006, forge-010, forge-012, forge-013) are consistently identified. Scale_fit qualifications (village: poor, good, marginal) are cited and correctly used to distinguish formula wins from operationally viable wins. No market-lens rule violations found beyond the payback-table errors in small-city.md (P2-01 through P2-03).

### Cooperative lens (P-2)

The cooperative lens correctly applies "feasible member pool ≥ break-even member count." Village ceiling (2/15) and town-open (15/15) finding is correctly stated in all documents. The P2-04 and P2-05 findings note clarifications needed in the break-even range description (small-city.md) and the participation-rate inconsistency (pitch vs. small-city.md). No instances of Ostrom-principle compliance being overstated or understated.

### Civic lens (P-3)

The civic diagnostic outcome (Path A: add `annual_public_use_hours` to purpose-designed civic entries; non-civic entries remain fail) is correctly represented across all four documents. The specialized-equipment exception (0.15 hr/capita vs. 2.0 default, ECONOMIC-LENSES.md §4.3) is cited in all three playbooks and the pitch. The P2-06 finding (forge-003 civic-compatibility note) is presentational rather than a lens-rule violation. No civic-lens rule violations found.

---

## Style Guide §4 Forbidden Framings Check

| Framing | §4 Prohibition | Status in artifacts |
|---|---|---|
| "golden age" / nostalgia | §4.1 | None found |
| Sustainability as implicit assumption | §4.2 | None found |
| Elision of labor regimes | §4.3 | Village.md correctly notes apprentice pipeline as a concrete operational constraint, not romanticized |
| Guild-as-craft-quality framing | §4.4 | None found (guilds not prominently featured in playbooks or pitch) |
| "Lost knowledge" without documentation | §4.5 | None found; skills described as "thin labor pool" not "lost knowledge" |

**All §4 prohibited framings absent from all four artifacts.**

---

## Style Guide §7 Voice Check

| Artifact | Required voice | Actual voice | Assessment |
|---|---|---|---|
| village.md | Directive (playbook) | Directive; uses imperative constructions ("Verify the service-area population before committing"); cites specific entries by ID | Pass |
| town.md | Directive (playbook) | Directive; organized by implementation sketches; uses "choose this when" framing | Pass |
| small-city.md | Directive (playbook) | Directive; implementation sketches with setup, year-0 groundwork, open risks | Pass |
| PITCH-NARRATIVE.md | Persuasive-but-rigorous (pitch) | Persuasive-but-rigorous; leads with numbers; qualifies estimates as order-of-magnitude; objections section maintains rigor | Pass |

---

## Verdict

**HOLD** — 6 P2s must be fixed before external circulation. No P1s.

The three payback-table errors in small-city.md (P2-01 through P2-03) are the highest-priority fixes: a reader cross-referencing the table against the catalog will immediately flag them. The participation-rate inconsistency (P2-05) will be caught by any funder whose analyst checks the cooperative-pool arithmetic.

All four documents pass anti-romanticism, voice, and lens-rule checks. The cross-doc consistency on verdicts and per-household cost figures is clean. The pitch narrative's three objections and responses are honest and appropriately rigorous.

After fixing the 6 P2s, the artifact set is ready for ceres-panel R1 on the pitch narrative and external circulation subject to that review.
