---
trade: weaving
doc_type: catalog-overview
version: "1.0"
status: draft
entry_count: 15
---

# Weaving Catalog — Overview

## Purpose

This catalog is the primary artifact of Plan I. It contains 15 weaving equipment-design
entries spanning the luxury-specialty, heritage/cultural-revival, community/therapeutic,
and training niches identified as viable by `research/trades/weaving/DECLINE-VERDICT.md`.
Each entry is a schema-complete markdown file with YAML frontmatter ingested by the
Plan D Tier A simulation engine and prose sections evaluated by the ceres-panel review
process. The Plan E playbook draws on simulation outputs and entry prose when
constructing deployment guidance.

This catalog does not duplicate the top-level `catalog/README.md` overview of the
catalog subsystem. It extends that overview with the weaving-specific 15-entry manifest,
design-space rationale (including the fiber-sourcing falsifier), and entry-status
tracking. Readers unfamiliar with the catalog subsystem should read `catalog/README.md`
first.

Relationship to sibling documents: `research/trades/weaving/REQUIREMENTS.md` defines
the functional envelope every entry must address. `research/trades/weaving/HISTORICAL-FORMS.md`
supplies the anchor-culture inspirations entries may cite. `research/trades/weaving/DECLINE-VERDICT.md`
defines which niches are plausibly restorable and which are not. The key DECLINE-VERDICT
falsifier for weaving is the **fiber-sourcing pathway**: every entry must declare its
yarn or fiber sourcing via the `fiber_source_declaration` field. Entries claiming
integrated spinning add significant capital and skill scope beyond the loom itself.

---

## 15-Entry Manifest

### Group A — Luxury / Specialty (5 entries)

High-margin, low-volume handwoven textiles that industrial production cannot replicate
at equivalent aesthetic or cultural quality. This group tests the premium-market
hypothesis for handwoven goods and commissions.

| ID | Name | One-line description |
|---|---|---|
| weave-001 | Handwoven Tapestry Studio | High-end tapestry for gallery and interior-design commissions; floor loom; small-city; market-primary. |
| weave-002 | Heritage Wool / Natural-Dye Workshop | Heritage-breed wool + natural dye; floor loom; town; market + civic; cultural-preservation angle. |
| weave-003 | Architectural Textile Studio | Large-format architectural textiles; wide floor loom; small-city; market-primary; commission model. |
| weave-004 | Natural Fiber Fashion Atelier | Luxury slow-fashion handwoven yardage and garments; floor loom; small-city; market-primary. |
| weave-005 | Custom Rug & Upholstery Studio | Custom furnishing textiles for residential and commercial interiors; frame + floor loom; town/city; market-primary. |

### Group B — Heritage / Cultural (3 entries)

Heritage and cultural-revival weaving traditions where the product is inseparable
from the cultural knowledge. Industrial substitution is structurally difficult because
authenticity and provenance are core to the value proposition.

| ID | Name | One-line description |
|---|---|---|
| weave-006 | Traditional / Ethnic Weaving Revival | Community-specific cultural textile revival; backstrap + frame; town; market + civic. |
| weave-007 | Coverlet & Americana Revival | American frontier double-weave coverlet tradition; 4-shaft floor loom; village/town; market-primary. |
| weave-008 | Japanese-style Textile Studio | Complex Japanese pattern-weave (kasuri, nishiki); drawloom/dobby; small-city; specialty market. |

### Group C — Community / Coop / Educational (5 entries)

Shared, institutional, and therapeutic weaving models. These entries test whether
cooperative and civic operating structures can sustain weaving operations that
market-primary models cannot.

| ID | Name | One-line description |
|---|---|---|
| weave-009 | Rigid Heddle Tool-Library | Low-capital shared rigid-heddle access; coop-primary; town; minimum-barrier cooperative entry. |
| weave-010 | Community Fiber Arts Center | Multi-member shared studio with floor looms and instruction; coop + civic; town/city. |
| weave-011 | Therapeutic Weaving Workshop | Hospital/rehab-center partnership; civic-primary; small-city; occupational-therapy weaving model. |
| weave-012 | Apprentice Training Loom Studio | Vocational weaving training; multi-station floor loom; coop + civic; town/city. |
| weave-013 | Production Weaving Cooperative | Multi-loom B2B specialty cloth cooperative; floor loom × 6; coop-primary; small-city. |

### Group D — Minimum-viable / Stress-test (2 entries)

These entries test the viability floor and the extreme ends of the capital range.
Their inclusion is methodologically necessary to produce the variance required for
meaningful Tier A simulation comparison.

| ID | Name | One-line description |
|---|---|---|
| weave-014 | Backstrap Home Studio | Minimum-capital backstrap home weaving; village-only; stress-test of viability floor. |
| weave-015 | Artist-Designer Collaboration Studio | Shared floor loom pairing weaver and textile designer; market + coop; small-city. |

---

## Design-Space Coverage

The 15 entries reflect DECLINE-VERDICT guidance that the catalog should target
luxury/specialty, heritage/cultural, and community/therapeutic niches, and explicitly
exclude commodity cloth production where industrial displacement is complete.

The distribution is approximately 5 luxury / 3 heritage / 5 community / 2 stress-test.
This spans the major DECLINE-VERDICT niches. Entry weave-013 (Production Weaving
Cooperative) approaches the commodity-cloth boundary; it is included to test whether
a specialty-cloth positioning within a production-cooperative model is viable, and must
explicitly document its specialty pricing and positioning.

**Fiber-sourcing falsifier:** All 15 entries must carry a `fiber_source_declaration`
field. The catalog covers `industrial-yarn-purchased` (most entries),
`local-fiber-spun` (weave-002, weave-006, potentially weave-004), and
`heritage-fiber` (weave-006, weave-007, potentially weave-008). Entries claiming
`integrated-spinning` add significant capital and skill scope; this is flagged in
their Key Assumptions.

**Loom type and humidity control** are additional required fields specific to weaving,
capturing the substantial capital and environmental variance across entries
(backstrap $200 vs. multi-loom production cooperative $200,000; no-power vs.
electric-power-loom; humidity-controlled vs. uncontrolled).

Commodity cloth for mass-market textile production is not represented. DECLINE-VERDICT
documents complete industrial displacement in this segment.

---

## Lens-Fit and Scale-Fit Distribution

Summary of estimated `lens_fit` and `scale_fit` values across the 15 entries.
Values are guidance from Plan I task specifications; individual entry authors
must populate schema fields consistent with this summary. `good` / `marginal` / `poor`
per schema tri-state.

| ID | Name | market | coop | civic | village | town | small-city |
|---|---|---|---|---|---|---|---|
| weave-001 | Handwoven Tapestry Studio | good | marginal | poor | poor | marginal | good |
| weave-002 | Heritage Wool / Natural-Dye Workshop | marginal | marginal | marginal | poor | good | marginal |
| weave-003 | Architectural Textile Studio | good | poor | poor | poor | poor | good |
| weave-004 | Natural Fiber Fashion Atelier | good | poor | poor | poor | marginal | good |
| weave-005 | Custom Rug & Upholstery Studio | good | marginal | poor | poor | good | good |
| weave-006 | Traditional / Ethnic Weaving Revival | marginal | marginal | good | marginal | good | marginal |
| weave-007 | Coverlet & Americana Revival | marginal | poor | marginal | good | good | marginal |
| weave-008 | Japanese-style Textile Studio | marginal | poor | marginal | poor | marginal | good |
| weave-009 | Rigid Heddle Tool-Library | poor | good | marginal | poor | good | good |
| weave-010 | Community Fiber Arts Center | poor | good | good | poor | good | good |
| weave-011 | Therapeutic Weaving Workshop | poor | marginal | good | poor | marginal | good |
| weave-012 | Apprentice Training Loom Studio | poor | good | good | poor | good | good |
| weave-013 | Production Weaving Cooperative | marginal | good | poor | poor | marginal | good |
| weave-014 | Backstrap Home Studio | marginal | poor | poor | good | poor | poor |
| weave-015 | Artist-Designer Collaboration Studio | good | good | poor | poor | marginal | good |

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
| weave-001 | Handwoven Tapestry Studio | draft | 2026-04-19 |
| weave-002 | Heritage Wool / Natural-Dye Workshop | draft | 2026-04-19 |
| weave-003 | Architectural Textile Studio | draft | 2026-04-19 |
| weave-004 | Natural Fiber Fashion Atelier | draft | 2026-04-19 |
| weave-005 | Custom Rug & Upholstery Studio | draft | 2026-04-19 |
| weave-006 | Traditional / Ethnic Weaving Revival | draft | 2026-04-19 |
| weave-007 | Coverlet & Americana Revival | draft | 2026-04-19 |
| weave-008 | Japanese-style Textile Studio | draft | 2026-04-19 |
| weave-009 | Rigid Heddle Tool-Library | draft | 2026-04-19 |
| weave-010 | Community Fiber Arts Center | draft | 2026-04-19 |
| weave-011 | Therapeutic Weaving Workshop | draft | 2026-04-19 |
| weave-012 | Apprentice Training Loom Studio | draft | 2026-04-19 |
| weave-013 | Production Weaving Cooperative | draft | 2026-04-19 |
| weave-014 | Backstrap Home Studio | draft | 2026-04-19 |
| weave-015 | Artist-Designer Collaboration Studio | draft | 2026-04-19 |

---

## Sources and References

| Document | Path | Role |
|---|---|---|
| Functional requirements | `research/trades/weaving/REQUIREMENTS.md` | Every entry must address each requirement or state inapplicability. |
| Historical weaving forms and equipment variation | `research/trades/weaving/HISTORICAL-FORMS.md` | Anchor-culture inspirations; entries cite specific chapter passages. |
| Niche targeting and design constraints | `research/trades/weaving/DECLINE-VERDICT.md` | Binding guidance on which niches are plausibly restorable; fiber-sourcing falsifier. |
| Primary source bibliography | `research/trades/weaving/SOURCES.md` | Full bibliography; placeholder tracking. |
| Canonical catalog schema (v1.1) | `catalog/SCHEMA.md` | Machine-ingested schema; all entries must conform. |
| Weaving-specific schema extension | `catalog/weaving/SCHEMA.md` | Trade-level extensions (throughput block, loom_type, fiber_source_declaration, humidity_control_required, skill-floor enumeration); Plan I Task 2. |
