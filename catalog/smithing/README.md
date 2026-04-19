---
trade: smithing
doc_type: catalog-overview
version: "1.0"
status: draft
entry_count: 15
---

# Smithing Catalog — Overview

## Purpose

This catalog is the primary artifact of Plan C. It contains 15 forge equipment-design
entries spanning the repair, specialty, and shared-civic niches identified as viable by
`research/trades/smithing/DECLINE-VERDICT.md`. Each entry is a schema-complete markdown
file with YAML frontmatter ingested by the Plan D Tier A simulation engine and prose
sections evaluated by the ceres-panel review process. The Plan E playbook draws on
simulation outputs and entry prose when constructing deployment guidance.

This catalog does not duplicate the top-level `catalog/README.md` overview of the
catalog subsystem. It extends that overview with the smithing-specific 15-entry manifest,
design-space rationale, and entry-status tracking. Readers unfamiliar with the catalog
subsystem should read `catalog/README.md` first.

Relationship to sibling documents: `research/trades/smithing/REQUIREMENTS.md` defines
the functional envelope every entry must address. `research/trades/smithing/HISTORICAL-FORMS.md`
supplies the anchor-culture inspirations entries may cite. `research/trades/smithing/DECLINE-VERDICT.md`
defines which niches are plausibly restorable and which are not.

---

## 15-Entry Manifest

### Group A — Repair-Focused (6 entries)

Repair smithing survived longest across all four anchor cultures because it is
location-bound and judgment-intensive. These entries test whether contemporary
repair-dominant operation is economically viable across scale and lens.

| ID | Name | One-line description |
|---|---|---|
| forge-005 | Frontier-Revival Coal Repair Shop | Single-operator coal forge targeting rural repair demand; market-primary; village/town. |
| forge-007 | Containerized Mobile Forge | 20-ft intermodal container conversion serving farm-repair circuits on rural routes; market-primary; village. |
| forge-012 | Farriery-Specialist Propane | Horseshoeing and hoof-care specialist; propane or vehicle-mounted; rural/village; market-primary. |
| forge-013 | Restoration-Specialist Heritage Shop | Historic-building and architectural repair; multi-fuel; small-city; market + civic. |
| forge-002 | Induction-Modular Small Repair | Modern induction-electric repair shop; compact urban footprint; tool and implement repair; market-primary. |
| forge-014 | Electric-Induction Gig Repair Micro | Minimum-capital part-time induction entry; village-only; stress-test of viability floor. |

### Group B — Specialty / Custom / Artistic (3 entries)

Low-volume, elastic-demand, high-margin work that resists industrial substitution.
These entries target premium-market segmentation per DECLINE-VERDICT §5.

| ID | Name | One-line description |
|---|---|---|
| forge-006 | Induction Bladesmith / Cutlery | Chef-knife and outdoor-blade specialty; induction-electric; small-city; market + coop. |
| forge-010 | Architectural Ironwork Bespoke | Custom gates, railings, and structural hardware for contractors and high-end residential; small-city; market-primary. |
| forge-008 | Traditional Charcoal Village | Purist historical-method shop; charcoal + traditional bellows; village; tests craft-preservation viability. |

### Group C — Shared / Civic / Cooperative (4 entries)

Per DECLINE-VERDICT §5, apprentice-training and civic externalities support cooperative
and civic lens viability where market economics are marginal. These entries test
shared-resource and institutional operating models.

| ID | Name | One-line description |
|---|---|---|
| forge-003 | Shared Tool-Library Coal | Member-booked shift coal forge; town scale; canonical cooperative reference design from spec §5. |
| forge-004 | Community Civic Makerspace | Town-owned library-model workshop; hybrid induction + propane; civic-primary + coop-good. |
| forge-011 | Municipal Civic Training Forge | Public high-school / community-college partnership; induction-electric; small-city; civic-primary. |
| forge-015 | Tool-Library Member-Access Induction | Member-subscription induction workshop; lower capital than coal shared model; town/city; coop-primary. |

### Group D — Training / Apprentice-Pipeline (2 entries)

Structurally distinct from Group C in their explicit focus on operator succession
and apprentice-intake as the primary function.

| ID | Name | One-line description |
|---|---|---|
| forge-009 | Co-op Apprentice Training Forge | Formal apprentice-pipeline workshop; coal + induction hybrid; multi-station; town/city; coop-primary. |
| forge-001 | Backyard Propane Compact | Minimum-footprint hobbyist / low-capital starter; village-only; tests entry-level cell of the matrix. |

---

## Design-Space Coverage

The 15 entries reflect DECLINE-VERDICT §5's guidance that the catalog should target
three restorable niches — repair, specialty/custom, and shared-civic/training — and
explicitly exclude commodity hardware manufacturing, where industrial displacement is
complete across all four anchor cultures.

The 6 / 3 / 4 / 2 group distribution is not arbitrary. Repair entries (Group A) are
the most historically durable segment and receive the largest allocation. Specialty
entries (Group B) test premium segmentation under varying conditions. Shared-civic
entries (Group C) test whether institutional and cooperative operating models can sustain
forges that market economics alone cannot. Training entries (Group D) test the
apprentice-pipeline and skill-transfer function that REQUIREMENTS.md §6 identifies as
a distinct economic form.

Entries forge-001 and forge-014 are stress-tests of the viability floor: both
represent minimum-capital configurations that the catalog expects to perform poorly
across most cells of the context matrix. Their inclusion is methodologically necessary
because a catalog that only authors entries expected to succeed cannot produce the
variance required for meaningful Tier A simulation comparison.

Commodity hardware manufacturing (nails, standardized fasteners, mass-specification
fittings) is not represented. DECLINE-VERDICT §3 documents complete displacement across
all four anchor cultures; no equipment redesign changes that competitive position.

---

## Lens-Fit and Scale-Fit Distribution

Summary of claimed `lens_fit` and `scale_fit` values across the 15 entries. Values are
per-entry guidance from Plan C task specifications; individual entry authors must
populate the schema fields consistent with this summary. `good` / `marginal` / `poor`
per the schema tri-state.

| ID | Name | market | coop | civic | village | town | small-city |
|---|---|---|---|---|---|---|---|
| forge-001 | Backyard Propane Compact | marginal | marginal | poor | good | poor | poor |
| forge-002 | Induction-Modular Small Repair | good | marginal | marginal | marginal | good | good |
| forge-003 | Shared Tool-Library Coal | marginal | good | good | marginal | good | good |
| forge-004 | Community Civic Makerspace | poor | good | good | poor | good | good |
| forge-005 | Frontier-Revival Coal Repair | good | marginal | marginal | good | good | marginal |
| forge-006 | Induction Bladesmith / Cutlery | good | good | marginal | poor | marginal | good |
| forge-007 | Containerized Mobile Forge | good | poor | poor | good | marginal | poor |
| forge-008 | Traditional Charcoal Village | marginal | marginal | marginal | good | marginal | poor |
| forge-009 | Co-op Apprentice Training Forge | poor | good | marginal | poor | good | good |
| forge-010 | Architectural Ironwork Bespoke | good | poor | poor | poor | marginal | good |
| forge-011 | Municipal Civic Training Forge | poor | marginal | good | poor | marginal | good |
| forge-012 | Farriery-Specialist Propane | good | poor | poor | good | marginal | poor |
| forge-013 | Restoration-Specialist Heritage | good | poor | good | poor | marginal | good |
| forge-014 | Electric-Induction Gig Repair Micro | marginal | poor | poor | marginal | poor | poor |
| forge-015 | Tool-Library Member-Access Induction | marginal | good | marginal | poor | good | good |

Every cell of the 9-cell matrix (3 scales × 3 lenses) has at least one entry claiming
`good` or `marginal`. Tier A simulation is therefore expected to produce variance
across all cells; no cell is structurally starved of entries.

---

## Entry Status Tracking

Populated as entries are authored. Initially all entries are `draft`. Promoted to
`reviewed` after ceres-panel R1; to `validated` after Plan D simulation cross-check;
`deprecated` if an entry is superseded or dropped.

| ID | Name | Status | Last Modified |
|---|---|---|---|
| forge-001 | Backyard Propane Compact | draft | 2026-04-19 |
| forge-002 | Induction-Modular Small Repair | draft | 2026-04-19 |
| forge-003 | Shared Tool-Library Coal | draft | 2026-04-19 |
| forge-004 | Community Civic Makerspace | draft | 2026-04-19 |
| forge-005 | Frontier-Revival Coal Repair Shop | draft | 2026-04-19 |
| forge-006 | Induction Bladesmith / Cutlery | draft | 2026-04-19 |
| forge-007 | Containerized Mobile Forge | draft | 2026-04-19 |
| forge-008 | Traditional Charcoal Village | draft | 2026-04-19 |
| forge-009 | Co-op Apprentice Training Forge | draft | 2026-04-19 |
| forge-010 | Architectural Ironwork Bespoke | draft | 2026-04-19 |
| forge-011 | Municipal Civic Training Forge | draft | 2026-04-19 |
| forge-012 | Farriery-Specialist Propane | draft | 2026-04-19 |
| forge-013 | Restoration-Specialist Heritage Shop | draft | 2026-04-19 |
| forge-014 | Electric-Induction Gig Repair Micro | draft | 2026-04-19 |
| forge-015 | Tool-Library Member-Access Induction | draft | 2026-04-19 |

---

## Sources and References

| Document | Path | Role |
|---|---|---|
| Functional requirements (R-01 through R-24) | `research/trades/smithing/REQUIREMENTS.md` | Every entry must address each requirement or state inapplicability. |
| Historical forge forms and fuel variation | `research/trades/smithing/HISTORICAL-FORMS.md` | Anchor-culture inspirations; entries cite specific chapter passages. |
| Niche targeting and design constraints | `research/trades/smithing/DECLINE-VERDICT.md` | Binding guidance on which product categories are plausibly restorable. |
| Primary source bibliography | `research/trades/smithing/SOURCES.md` | Full bibliography; placeholder tracking. |
| Canonical catalog schema (v1.1) | `catalog/SCHEMA.md` | Machine-ingested schema; all entries must conform. |
| Smithing-specific schema extension | `catalog/smithing/SCHEMA.md` | Trade-level extensions (throughput block, energy-source enumeration, skill-floor enumeration); Task 2. |
