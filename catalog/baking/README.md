---
trade: baking
doc_type: catalog-overview
version: "1.0"
status: draft
entry_count: 15
---

# Baking Catalog — Overview

## Purpose

This catalog is the primary artifact of Plan G. It contains 15 baking equipment-design
entries spanning the artisan-bread, specialty-confection, community-bakery, and
training niches identified as viable by `research/trades/baking/DECLINE-VERDICT.md`.
Each entry is a schema-complete markdown file with YAML frontmatter ingested by the
Plan D Tier A simulation engine and prose sections evaluated by the ceres-panel review
process. The Plan E playbook draws on simulation outputs and entry prose when
constructing deployment guidance.

This catalog does not duplicate the top-level `catalog/README.md` overview of the
catalog subsystem. It extends that overview with the baking-specific 15-entry manifest,
design-space rationale (including the mill-dependency falsifier), and entry-status
tracking. Readers unfamiliar with the catalog subsystem should read `catalog/README.md`
first.

Relationship to sibling documents: `research/trades/baking/REQUIREMENTS.md` defines
the functional envelope every entry must address. `research/trades/baking/HISTORICAL-FORMS.md`
supplies the anchor-culture inspirations entries may cite. `research/trades/baking/DECLINE-VERDICT.md`
defines which niches are plausibly restorable and which are not. The key DECLINE-VERDICT
falsifier for baking is the **mill dependency**: every entry must declare its
flour-sourcing assumption via the `flour_source_declaration` field.

---

## 15-Entry Manifest

### Group A — Artisan Bread / Premium (5 entries)

The most durable historical baking niche. Premium differentiation via fermentation
technique, grain sourcing, and community relationship resists industrial displacement.
These entries test whether contemporary artisan-bread operations are economically viable
across scale and lens.

| ID | Name | One-line description |
|---|---|---|
| bake-001 | Sourdough Artisan Micro-bakery | Minimum-capital artisan sourdough bakery; wood-fired or electric-deck; village/town; market-primary. |
| bake-002 | Heritage Grain Subscription Bakery | Premium CSA/subscription model using heritage-grain sourcing; electric-deck; town/city; market + coop. |
| bake-003 | Community Grain-Share Bakery | Mill-integrated coop bakery addressing flour-sourcing falsifier directly; electric; town; coop-primary. |
| bake-004 | Wholesale Artisan Loaf Bakery | B2B artisan-bread wholesale to restaurants and specialty retail; electric-deck; small-city; market-primary. |
| bake-005 | Mobile Pop-up Bakery | Vehicle-based mobile bakery for farmers-markets and rural routes; convection-electric van; village/rural; market-primary. |

### Group B — Specialty Confection / Pastry (4 entries)

Low-volume, elastic-demand, high-margin work. Per DECLINE-VERDICT: survives via
premium-market and event-driven segmentation where commodity confection is
industrial-dominated. Operator skill floor is the primary viability constraint.

| ID | Name | One-line description |
|---|---|---|
| bake-006 | French-style Pastry / Viennoiserie | Premium laminated-dough pastry retail; combi-steam; small-city; market-primary. |
| bake-007 | Japanese-style Wagashi Confection | Cultural specialty confection (steam + low-bake); town/city; market + civic; cultural-preservation angle. |
| bake-008 | Ethnic / Cultural Specialty Bakery | Underserved ethnic-community bakery; variable fuel; any scale; market-primary with captive niche. |
| bake-009 | Wedding / Custom Cake Studio | Event-driven custom cake studio; electric; small-city; market-primary; high throughput variance. |

### Group C — Community / Civic / Cooperative (4 entries)

Per DECLINE-VERDICT: community-serving bakeries and training externalities support
coop and civic lens viability where market-primary operations cannot sustain themselves.
These entries test shared-resource and institutional operating models.

| ID | Name | One-line description |
|---|---|---|
| bake-010 | Civic Neighborhood Bakery | Community food-access mandate bakery; electric-deck; town; civic-primary. |
| bake-011 | Apprentice Training Bakery | Formal apprentice-pipeline bakery linked to culinary programs; electric-combi; town/city; coop + civic. |
| bake-012 | Community Kitchen Collective | Shared commercial kitchen for multiple small bakers; electric-deck; town; coop-primary. |
| bake-013 | Farm-to-Table Integrated Bakery | Vertically integrated farm-mill-bakery; wood-fired; village/town; market + civic; mill-dependency falsifier addressed. |

### Group D — Minimum-viable / Stress-test (2 entries)

These entries test the viability floor. Both are expected to perform poorly across
most cells of the context matrix. Their inclusion is methodologically necessary:
a catalog that only authors entries expected to succeed cannot produce the variance
required for meaningful Tier A simulation comparison.

| ID | Name | One-line description |
|---|---|---|
| bake-014 | Apartment/Home Micro-bakery | Minimum-capital home oven entry; village-only; tests cottage-food-law viability floor. |
| bake-015 | Wood-fired Community Oven | Traditional shared masonry oven; civic/coop; village/town; from Plan B medieval chapter tradition. |

---

## Design-Space Coverage

The 15 entries reflect DECLINE-VERDICT guidance that the catalog should target
artisan/premium, specialty-confection, community-bakery, and training niches, and
explicitly exclude commodity factory-bread production where industrial displacement
is complete.

The target distribution is approximately 5 artisan / 4 confection / 4 community / 2
stress-test, which spans the major DECLINE-VERDICT niches without duplication. Entries
bake-014 and bake-015 are stress-tests of the viability floor; both represent
minimum-capital configurations expected to perform poorly across most matrix cells.

**Mill-dependency falsifier:** All 15 entries must carry a `flour_source_declaration`
field. The catalog deliberately includes entries across the full range:
`industrial-flour-purchased` (most entries), `local-mill-partnership` (bake-001,
bake-002, bake-010, bake-015), and `integrated-milling` (bake-003, bake-013). This
distribution tests whether mill integration is economically differentiating or
merely a supply-chain dependency that adds risk.

Commodity sandwich-loaf and industrial-scale factory bread are not represented.
DECLINE-VERDICT documents complete industrial displacement in this segment; no
equipment redesign changes that competitive position.

---

## Lens-Fit and Scale-Fit Distribution

Summary of estimated `lens_fit` and `scale_fit` values across the 15 entries.
Values are guidance from Plan G task specifications; individual entry authors
must populate schema fields consistent with this summary. `good` / `marginal` / `poor`
per schema tri-state.

| ID | Name | market | coop | civic | village | town | small-city |
|---|---|---|---|---|---|---|---|
| bake-001 | Sourdough Artisan Micro-bakery | good | marginal | poor | good | good | marginal |
| bake-002 | Heritage Grain Subscription Bakery | good | good | marginal | poor | good | good |
| bake-003 | Community Grain-Share Bakery | marginal | good | marginal | poor | good | marginal |
| bake-004 | Wholesale Artisan Loaf Bakery | good | poor | poor | poor | marginal | good |
| bake-005 | Mobile Pop-up Bakery | good | poor | poor | good | marginal | poor |
| bake-006 | French-style Pastry / Viennoiserie | good | marginal | poor | poor | marginal | good |
| bake-007 | Japanese-style Wagashi Confection | marginal | marginal | marginal | poor | good | good |
| bake-008 | Ethnic / Cultural Specialty Bakery | good | marginal | poor | marginal | good | good |
| bake-009 | Wedding / Custom Cake Studio | good | poor | poor | poor | marginal | good |
| bake-010 | Civic Neighborhood Bakery | poor | marginal | good | poor | good | good |
| bake-011 | Apprentice Training Bakery | poor | good | good | poor | good | good |
| bake-012 | Community Kitchen Collective | marginal | good | marginal | poor | good | good |
| bake-013 | Farm-to-Table Integrated Bakery | good | marginal | marginal | good | good | marginal |
| bake-014 | Apartment/Home Micro-bakery | marginal | poor | poor | marginal | poor | poor |
| bake-015 | Wood-fired Community Oven | poor | good | good | good | good | marginal |

Every cell of the 9-cell matrix (3 scales × 3 lenses) has at least one entry claiming
`good` or `marginal`. Tier A simulation is therefore expected to produce variance
across all cells; no cell is structurally starved of entries.

---

## Entry Status Tracking

Populated as entries are authored. Initially all entries are `draft`. Promoted to
`reviewed` after ceres-panel R1; to `validated` after Plan D simulation cross-check;
`deprecated` if an entry is superseded or dropped.

| ID | Name | Status | Tier A Sim | Last Modified |
|---|---|---|---|---|
| bake-001 | Sourdough Artisan Micro-bakery | draft | complete (2026-04-19) | 2026-04-19 |
| bake-002 | Heritage Grain Subscription Bakery | draft | complete (2026-04-19) | 2026-04-19 |
| bake-003 | Community Grain-Share Bakery | draft | complete (2026-04-19) | 2026-04-19 |
| bake-004 | Wholesale Artisan Loaf Bakery | draft | complete (2026-04-19) | 2026-04-19 |
| bake-005 | Mobile Pop-up Bakery | draft | complete (2026-04-19) | 2026-04-19 |
| bake-006 | French-style Pastry / Viennoiserie | draft | complete (2026-04-19) | 2026-04-19 |
| bake-007 | Japanese-style Wagashi Confection | draft | complete (2026-04-19) | 2026-04-19 |
| bake-008 | Ethnic / Cultural Specialty Bakery | draft | complete (2026-04-19) | 2026-04-19 |
| bake-009 | Wedding / Custom Cake Studio | draft | complete (2026-04-19) | 2026-04-19 |
| bake-010 | Civic Neighborhood Bakery | draft | complete (2026-04-19) | 2026-04-19 |
| bake-011 | Apprentice Training Bakery | draft | complete (2026-04-19) | 2026-04-19 |
| bake-012 | Community Kitchen Collective | draft | complete (2026-04-19) | 2026-04-19 |
| bake-013 | Farm-to-Table Integrated Bakery | draft | complete (2026-04-19) | 2026-04-19 |
| bake-014 | Apartment/Home Micro-bakery | draft | complete (2026-04-19) | 2026-04-19 |
| bake-015 | Wood-fired Community Oven | draft | complete (2026-04-19) | 2026-04-19 |

---

## Sources and References

| Document | Path | Role |
|---|---|---|
| Functional requirements | `research/trades/baking/REQUIREMENTS.md` | Every entry must address each requirement or state inapplicability. |
| Historical baking forms and fuel variation | `research/trades/baking/HISTORICAL-FORMS.md` | Anchor-culture inspirations; entries cite specific chapter passages. |
| Niche targeting and design constraints | `research/trades/baking/DECLINE-VERDICT.md` | Binding guidance on which niches are plausibly restorable; mill-dependency falsifier. |
| Primary source bibliography | `research/trades/baking/SOURCES.md` | Full bibliography; placeholder tracking. |
| Canonical catalog schema (v1.1) | `catalog/SCHEMA.md` | Machine-ingested schema; all entries must conform. |
| Baking-specific schema extension | `catalog/baking/SCHEMA.md` | Trade-level extensions (throughput block, energy-source enumeration, flour_source_declaration, skill-floor enumeration); Plan G Task 2. |
