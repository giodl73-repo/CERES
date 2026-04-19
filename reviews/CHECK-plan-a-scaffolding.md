# ceres-check — Plan A: Scaffolding and Framework Docs

**Artifact:** `C:\src\artisan\plans\2026-04-18-plan-a-scaffolding.md`
**Scope:** full
**Roles selected:** 6 of 9 individual roles in library
**Run date:** 2026-04-18

---

## Selection Plan

| Role | Tier | Relevance | Triggering signals |
|------|------|-----------|-------------------|
| P-4 Craft Practitioner | panel | 6 | operator, throughput, consumables, apprentice, failure |
| P-5 Historian | panel | 6 | historical, guild, pre-industrial, precedent, culture |
| P-1 Market Economist | panel | 5 | market, ROI, payback, wage |
| P-2 Commons Theorist | panel | 5 | cooperative, coop, member, governance |
| P-3 Civic Steward | panel | 4 | civic, municipal, library |
| P-6 Skeptical Funder | panel | 3 | pitch, viability |

3 roles excluded (not applicable to this artifact type): E-1 Citation Auditor, E-2 Scope Keeper, E-3 Numeracy Checker — `applies_to` does not include `plan`.

---

## Findings

| # | Role | Severity | Location | Issue | Suggested fix |
|---|------|----------|----------|-------|---------------|
| 1 | P-6 | P2 | section:overall-plan | Plan does not name its strongest honest objection or acknowledge any risks. No "risks / objections" section exists anywhere in the 17-task body; the plan is entirely forward-looking. | Add a brief "Risks and Mitigations" section (or a P-6-style objection register in Final Self-Review) naming at minimum: schema drift risk, spec-changes-mid-execution risk, and inter-task consistency risk. |
| 2 | P-6 | P2 | section:overall-plan | No failure modes are described. What happens if Task 15 (SCHEMA.md) is authored inconsistently with the spec, and Plan C catalog entries are already in progress? The plan has no contingency path for this. | Add explicit failure paths for the two most likely failure modes: (a) spec changes mid-execution, (b) inter-task inconsistency discovered at Final Self-Review. Name the recovery action for each. |
| 3 | P-6 | P2 | field:spec | The plan's load-bearing assumption — that `specs/2026-04-18-ceres-design.md` is stable and authoritative — is unacknowledged as an assumption. The plan says "when spec and plan disagree, the spec wins" but does not note that the spec itself may still be evolving, which would invalidate multiple in-flight tasks simultaneously. | Add a note in the plan header (or Task 1 self-review) acknowledging spec-stability as a prerequisite. Reference the spec-amendment pathway defined in Task 7 (PIPELINE.md). |

---

## Dimension Aggregate

Using `rubric_contribution` from each selected role's frontmatter:

| Dimension | Primary contributors (1.0x) | Secondary (0.5x) | Rough score estimate |
|-----------|----------------------------|------------------|---------------------|
| D3 Operations Realism | P-4 | — | 0/8 checked (all N/A — plan defines docs that will contain ops data, not ops data itself) |
| D4 Market Viability | P-1, P-2, P-3 | P-2 (D4), P-3 (D4), E-3 (not selected) | 0/21 checked (all N/A — no economics in a scaffolding plan) |
| D5 Commons Fit | P-5 | P-6 | 2/7 PASS (anti-romanticism sections assessed; historical items N/A for a non-historical plan) |
| D6 Civic Value | P-6 | P-4, P-5 | 0/8 from P-6 (3 FAIL P2, 5 N/A); 0/2 from P-4/P-5 secondary (N/A) |

> Note: D1 (Schema Completeness), D2 (Citation Strength) — primary contributors E-2 and E-1 were excluded (not applicable to `plan`). These dimensions are not evaluated here.
>
> The very high N/A rate (39 of 41 evaluated items) is expected and correct. This plan is about *creating the docs that define* market viability, operations reality, and governance — not about demonstrating them in a catalog entry. Panel roles whose lenses target catalog-entry economics are structurally inapplicable here, though they remain selected because `plan` is in their `applies_to`.
>
> Dimension scores are rough (findings-count based). Use `scoring/RUBRIC.md` for formal scoring.

---

## Summary

- **0 P1 findings** — no promotion blockers
- **3 P2 findings** — should fix (all from P-6: missing risk acknowledgment, missing failure modes, unacknowledged spec-stability assumption)
- **0 P3 findings** — no style/optional items
- **39 N/A items** — not applicable to a scaffolding/authoring plan (expected; see note above)
- **2 PASS items** — P-5 items 5 and 6: plan actively encodes anti-romanticism and anti-anachronism conventions in Task 5 (Style Guide)

**Verdict:** PASS

**Verdict logic:** Zero P1 findings. Three P2 findings should be addressed before Plan A serves as the authoritative scaffolding for downstream Plans B–E, but they do not block use of the outputs. The 39 N/A items reflect the artifact type correctly: a framework-authoring plan cannot be evaluated against catalog-entry economics or equipment-operations checklists.

---

## Auditor Notes

**On N/A rate:** The 39/41 N/A rate is a feature, not a gap. The panel roles (P-1 through P-6) have `applies_to: [plan]` and are correctly selected. However, their `lens.verify` items target catalog-entry viability (payback, governance, per-household cost, equipment failure modes, historical trade claims). A Plan A that produced non-N/A results on most of those items would itself be scope-drifting — this plan should not contain economic projections or governance designs. The three P-2 findings that did fire are appropriate: they probe the plan's internal coherence as a plan, not its economic content.

**On the three P-2 findings:** All three come from P-6 (Skeptical Funder) items that apply to any plan regardless of type: "strongest objection acknowledged?", "failure modes named?", and "load-bearing assumption defensible?". These are genuinely missing. The plan's Final Self-Review checklist (17 items) does not include any P-6-style adversarial check. A short addition would resolve all three.

**Status note:** Plan A frontmatter shows `status: completed`, `completed: 2026-04-19`. This audit was run against the plan document itself (the authoring spec), not against the outputs it specifies. Outputs (CLAUDE.md, SCHEMA.md, etc.) are not evaluated here.
