# ceres-check — CERES Design Specification

**Artifact:** C:\src\artisan\specs\2026-04-18-ceres-design.md
**Scope:** full
**Roles selected:** 6 of 9 individual roles in library
**Run date:** 2026-04-18

---

## Selection Plan

| Role | Tier | Relevance | Triggering signals |
|------|------|-----------|-------------------|
| P-1 Market Economist | panel | 9 | market, profit, ROI, payback, revenue, competition, wage, customer |
| P-2 Commons Theorist | panel | 10 | cooperative, coop, commons, member, governance, Ostrom, shared, tool-library, dues |
| P-3 Civic Steward | panel | 9 | civic, municipal, tax, library, fire-department, council, budget, zoning |
| P-4 Craft Practitioner | panel | 8 | operator, throughput, maintenance, consumables, apprentice, failure, skill |
| P-5 Historian | panel | 9 | history, historical, medieval, Song, Tokugawa, ayllu, precedent, culture |
| P-6 Skeptical Funder | panel | 10 | funding, pitch, viability, pilot, milestone, objection, risk, ask |

3 roles excluded (E-1, E-2, E-3 — editorial roles; `applies_to` does not include `spec`).

---

## Findings

| # | Role | Severity | Location | Issue | Suggested fix |
|---|------|----------|----------|-------|---------------|
| 1 | P-1 | P2 | section:6 Economic Lens Math | Schema requires `market_price_per_unit` with citations but no protocol verifies that cited prices reflect actual market-clearing demand rather than aspirational pricing; a trade survey is not the same as willingness-to-pay evidence. | Add a required `pricing_validation` sub-field or `METHODOLOGY.md` step that specifies what constitutes acceptable market-price evidence (e.g., comparable product sales data, survey, comparable operator financials). |
| 2 | P-1 | P2 | section:5 Catalog-Entry Schema | No required schema field mandates a competitive price comparison against industrial alternatives; `pricing_notes` example illustrates it informally but does not enforce it. | Add `industrial_baseline_price` as a required sub-field under `economics` for any entry where `lens_fit.market` is `good` or `marginal`; require a one-line justification for the premium. |
| 3 | P-2 | P3 | field:lens_context.cooperative.rules_source | `rules_source` records rule provenance but does not require that governance rules be calibrated to local conditions (village vs. town norms differ significantly in feasible participation levels and enforcement capacity). | Add a `scale_fit_note` or brief narrative prompt within the `cooperative` sub-block asking authors to confirm rules match the scale at which `lens_fit.cooperative` is `good`. |
| 4 | P-2 | P2 | field:lens_context.cooperative | No schema field requires documenting member amendment procedures; authors can satisfy `rules_source` with a label ("standard bylaws") without specifying how members change the rules. | Add a `member_amendment_process` field (e.g., "2/3 vote at annual meeting") to `lens_context.cooperative`, parallel to `graduated_sanctions` and `conflict_resolution`. |
| 5 | P-2 | P2 | field:lens_context.cooperative | No field captures the legal standing or regulatory recognition of the cooperative entity; an unregistered cooperative lacking municipal acknowledgment is a documented commons-failure mode (Ostrom principle 7 analog). | Add a `legal_form` field (e.g., "state-registered worker cooperative, LLC") to `lens_context.cooperative`; flag as required when `lens_fit.cooperative` is `good`. |
| 6 | P-3 | P2 | section:5 Catalog-Entry Schema / section:6 Civic Lens | No required field mandates a benchmark comparison of per-household civic cost against analogous public goods (library, rec center, tool library); P-3's sign-off criterion requires naming the comparable but the schema does not enforce this. | Add a `civic_benchmark_comparison` field to `lens_context.civic` (e.g., "Library: $42/HH/yr in peer towns; this facility: $18/HH/yr") so the comparison is schema-enforced, not author-discretionary. |
| 7 | P-3 | P2 | field:lens_context.civic | `governance_form` is a free-text label; no required field captures staffing model (wage, FTE, hours); omitting this makes per-household cost claims unverifiable. | Add a `staffing_model` sub-field to `lens_context.civic` with required sub-keys: `operator_fte`, `wage_assumption`, `source` (reference to `corpus/program/SCALES.md` wage tables). |
| 8 | P-3 | P2 | field:lens_context.civic | No required field documents civic externalities (apprentice pipeline, emergency production capacity, repair-culture resilience); this is the primary public-goods justification for civic funding but is absent from the schema. | Add a `civic_externalities` list field to `lens_context.civic` with at least one required entry; tie it to the CIVIC lens pass condition in §6. |
| 9 | P-4 | P2 | field:operations_reality | `first_year_failures` captures failure modes and lead times but no field distinguishes operator-serviceable repairs from those requiring a specialist; this distinction materially affects operating cost and downtime projections. | Add a `serviceability` field to each `first_year_failures` item (values: `operator`, `journeyman`, `specialist-required`) so the schema enforces this distinction. |
| 10 | P-4 | P3 | field:throughput / sim_params | No field captures intraday interruption patterns (customer walk-ins, tool changes, apprentice questions); `downtime_fraction` and `worst_month_fraction` address macro-level variance but not micro-interruption realism that affects single-shift throughput. | Add an optional `interruption_notes` prose field to `operations_reality`; update `docs/METHODOLOGY.md` to specify how intraday interruptions should be folded into `throughput_units_equiv_per_year` estimates. |
| 11 | P-4 | P2 | field:operations_reality | No field captures maintenance schedule (frequency, type) or who performs routine maintenance; this affects both `annual_maintenance` cost defensibility and `downtime_fraction` credibility. | Add a `maintenance_schedule` list field under `operations_reality` with sub-keys: `task`, `frequency`, `performer` (operator / contract service), `estimated_hours`. |
| 12 | P-4 | P2 | field:throughput.max_active_hours_per_week | `max_active_hours_per_week` appears to represent active production hours; no field accounts for startup, shutdown, and cleanup overhead, potentially making throughput math systematically optimistic. | Add a `setup_shutdown_hours_per_shift` field to `operations_reality`; clarify in `catalog/smithing/SCHEMA.md` whether `max_active_hours_per_week` is gross or net of setup/shutdown. |
| 13 | P-4 | P3 | field:apprentice_friendly | `apprentice_friendly` is a boolean; no field describes the apprentice path (training duration, skill gates, pathway to independent operator), leaving apprentice viability unverifiable. | Expand to a structured `apprentice_path` block (or at minimum a required prose sub-field when `apprentice_friendly: true`) documenting training stages and time-to-independence estimate. |
| 14 | P-5 | P3 | section:4.1 / research/trades schema | No formal research protocol step requires explicitly adjudicating "decline vs. restructuring" for each trade; without this step, research may default to a decline framing that obscures cases where local production was restructured (rather than lost). | Add a `decline_or_restructuring_verdict` field or required analytical step to `research/trades/<trade>/REQUIREMENTS.md` template, with options: `decline`, `restructuring`, `displacement`, `ambiguous` and a one-paragraph justification. |
| 15 | P-6 | P2 | section:11.3 Failure Criteria | §11.3 failure criteria address scope failure ("fewer than 15 entries") and evidence failure, but not the execution quality risk: 15 entries may be produced yet fail editorial review in aggregate due to systematic methodological weaknesses; no contingency or quality-gate milestone addresses this. | Add a §11.3 failure sub-criterion: "Systematic editorial review failure (3+ P1 findings per entry across more than half the catalog) triggers a methodology-halt review before continuing." |
| 16 | P-6 | P2 | section:10 Phase-1 Vertical Slice | The spec treats smithing as the template for all subsequent trades but does not acknowledge that smithing may be an easier-case first trade; generalizability of the pipeline pattern to harder trades (weaving, pottery, leatherwork) is the load-bearing assumption for the project design and is unaddressed. | Add a §10 note or §11.1 qualification acknowledging smithing was selected as a first slice because [stated reason]; identify one harder trade and note what would need to hold for the pattern to transfer. |
| 17 | P-6 | P3 | section:2 / section:9 | No section addresses what industrial producers or incumbent supply chains would likely do in response to a successfully demonstrated local-production pipeline (competitive counter-moves); this is relevant stress-testing for the pitch narrative. | Add a brief "competitive response" paragraph to the Pitch narrative template (§9) prompting authors to address the most plausible incumbent counter-move; leave the design spec as-is but flag for inclusion in Phase 5. |

---

## Dimension Aggregate

Using `rubric_contribution` from each selected role's frontmatter:

| Dimension | Primary contributors (1.0x) | Secondary (0.5x) | Rough score estimate |
|-----------|----------------------------|------------------|---------------------|
| D2 Citation Strength | — | P-1, P-5 | 10/13 (roles P-1, P-5 items contributing to D2) |
| D3 Operations Realism | P-4 | — | 3/8 (3 PASS out of 8 P-4 verify items) |
| D4 Market Viability | P-1, P-2, P-3 | — | 11/21 (11 PASS across P-1, P-2, P-3 verify items) |
| D5 Commons Fit | P-5 | P-6 | 7/10 (PASS items from P-5 and P-6 verify sets) |
| D6 Civic Value | P-6 | P-1, P-2, P-3, P-4 | 3/8 (P-6 PASS items: 3 of 6 non-N/A items) |

Dimension scores are rough (findings-count based). Use `scoring/RUBRIC.md` for formal scoring.

---

## Summary

- 0 P1 findings — no promotion blockers
- 12 P2 findings — should fix (findings 1, 2, 4, 5, 6, 7, 8, 9, 11, 12, 15, 16)
- 5 P3 findings — optional (findings 3, 10, 13, 14, 17)
- 3 N/A items (P-2 item 8: nested governance out of scope; P-6 items 5 and 7: skin-in-game and TAM/SOM are pitch-narrative scope, not design spec)
- 23 PASS items

**Verdict:** PASS

**Verdict logic:** Zero P1 findings. Spec is structurally sound; 12 P2 findings are schema gaps and missing fields that should be addressed before catalog entries enter `reviewed` status, but none block the design spec from serving as the implementation-planning anchor. P3 findings are optional refinements.

**Notable themes (for author attention, not re-surfacing R1 issues):**

- **Schema completeness for civic lens** (findings 6, 7, 8): Three distinct P2 gaps in `lens_context.civic` — no benchmark comparison, no staffing model, no externalities field. These will generate P1/P2 findings at every individual catalog entry unless fixed at the schema level now.
- **Operations reality granularity** (findings 9, 11, 12): Three P2 schema gaps in `operations_reality` — serviceability level, maintenance schedule, and startup/shutdown overhead. The schema is good but not yet sufficient for P-4 sign-off on individual entries.
- **Generalizability assumption** (finding 16): The smithing-as-template assumption is the load-bearing design choice for the whole project; it is unacknowledged as an assumption, which P-6 will flag again at the pitch narrative stage unless named here.
