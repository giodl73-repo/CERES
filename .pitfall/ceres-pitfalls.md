# CERES Pitfalls

## CERES-PF-01: Local-Production Hypothesis Becomes Guaranteed Viability

**Status:** MITIGATED

**Pattern:** The catalog or pitch implies that modern equipment redesign will
make each trade viable rather than treating viability as a falsifiable result.

**Domain:** README, pitch narrative, playbooks, catalog summaries, and funder
conversations.

**Detection difficulty:** The project is intentionally optimistic and
fundable-facing, so null results can feel like a failure instead of evidence.

**Structural solution:** Preserve registered falsifiers, decline verdicts,
matrix failures, and explicit null-result language.

**Evidence:** `README.md`, `CLAUDE.md`, `TRACKER.md`, and
`simulations/tier-a-comparator/results/SUMMARY.md`.

## CERES-PF-02: Catalog Numbers Become Procurement Numbers

**Status:** OPEN

**Actor:** Catalog author, playbook author, funder-facing reviewer, municipal
reader, or future procurement-oriented adopter.

**Task:** Use CERES capital costs, throughput, wages, prices, maintenance, civic
costs, or simulation verdicts to decide what to investigate next.

**Surface:** Catalog frontmatter, playbooks, pitch narrative, methodology,
style guide, editorial roles, and public README examples.

**Likely mistake:** Treating research-paper-level estimates, ranges, or Tier A
verdicts as supplier quotes, due-diligence financial models, municipal
procurement estimates, or investment-grade feasibility.

**Consequence:** A reader can over-trust order-of-magnitude evidence and act on
numbers that explicitly require independent verification before buying,
approving, or funding equipment.

**Owner:** CERES owns research estimates and uncertainty labels; procurement,
due diligence, site approval, vendor selection, and investment decisions stay
with external owners.

**Pattern:** Order-of-magnitude capital costs, throughput, wages, prices,
maintenance, or civic costs are used as supplier quotes, due-diligence models,
or municipal procurement estimates.

**Domain:** Catalog entries, playbooks, pitch narrative, public-facing reports,
and external funder discussions.

**Detection difficulty:** YAML frontmatter and simulation outputs make rough
estimates look more exact than their source basis supports.

**Structural solution:** Keep research-paper-level estimate language,
uncertainty ranges, citation gaps, and no-procurement non-goals visible until
independent due diligence exists.

**Test:** `tests/pitfall_policy.rs` cites `CERES-PF-02` while checking README,
methodology, style-guide, and scope/numeracy role language that keeps CERES
numbers at research-paper estimate level rather than procurement authority.

**Evidence:** `docs/METHODOLOGY.md`, `docs/STYLE-GUIDE.md`,
`.roles/editorial/E-2-scope-keeper.md`, and `README.md`.

## CERES-PF-03: Citation Placeholder Becomes Validated Evidence

**Status:** OPEN

**Actor:** Catalog promoter, editorial reviewer, simulation operator, pitch
author, or external reader.

**Task:** Decide whether a catalog entry, research corpus, playbook, or pitch
claim is validated enough to circulate.

**Surface:** Catalog statuses, `[CITATION-NEEDED]` markers, reviews, source
audits, methodology, tracker status, simulation outputs, and pitch claims.

**Likely mistake:** Treating schema completeness, green simulation runs, or
structured catalog output as evidence validation while citation placeholders or
source-quality gaps remain.

**Consequence:** CERES can circulate precise-looking claims whose sources are
missing, unresolved, unverifiable, or mismatched to the claim.

**Owner:** CERES authors and editorial roles own citation closure; simulation
and schema validators only prove machine readability and arithmetic paths.

**Pattern:** Entries, trade corpora, or pitch claims containing
`[CITATION-NEEDED]` are treated as validated because the simulation or catalog
shape is complete.

**Domain:** Catalog promotion, research corpus, cross-entry audits, playbooks,
and external circulation.

**Detection difficulty:** Simulation can run over structured fields even when
the source support behind those fields is incomplete.

**Structural solution:** Keep editorial promotion, citation audits, and status
labels separate from mechanical schema completeness and simulation execution.

**Test:** `tests/pitfall_policy.rs` cites `CERES-PF-03` while checking
methodology, style-guide, citation-auditor role, and tracker/review language
that keeps citation placeholders and source-quality gaps out of validated
evidence claims.

**Evidence:** `TRACKER.md`, `corpus/canon/PRINCIPLES.md`,
`docs/METHODOLOGY.md`, and `reviews/CATALOG-AUDIT-plan-c.md`.

## CERES-PF-04: Downstream Game Or Economy Reuse Imports CERES Policy

**Status:** OPEN

**Actor:** Game-system maintainer, economy-system maintainer, PORTO/CANON/BANISH
integrator, RLINE/RALLY/SCENARIUM adopter, or portfolio dependency reviewer.

**Task:** Reuse CERES catalog, facility, result, or packet evidence in a
downstream product.

**Surface:** README reuse boundary, SCENARIUM adoption docs, capability map,
RLINE facility projection, RALLY event JSONL, and dependency reports.

**Likely mistake:** Treating CERES catalog schema, settlement scales,
market/cooperative/civic thresholds, or result packets as a generic economy,
crafting, facility, or game contract.

**Consequence:** Downstream repos can import CERES local-production policy and
mistake evidence compatibility for consumer-owned semantics or supported API
adoption.

**Owner:** CERES owns local-production research policy and bounded evidence;
neutral foundations own shared mechanics; consumers own their semantic tests and
adoption contracts.

**Pattern:** BANISH, PORTO, or another downstream system treats CERES catalog
schema, scales, market/cooperative/civic thresholds, or result packets as a
stable generic crafting/economy API.

**Domain:** Game-system support, portfolio reuse, RLINE/RALLY/SCENARIUM
integration, and external adopter contracts.

**Detection difficulty:** CERES intentionally helps worldbuilders and game
systems, and the Rust path now emits clean facility and packet evidence.

**Structural solution:** Require a named downstream manifest, versioned result
contract, and consumer-owned semantic tests before supported dependency adoption.

**Test:** `tests/pitfall_policy.rs` cites `CERES-PF-04` while checking README,
SCENARIUM adoption, capability-expansion, and RLINE projection wording that
separates CERES research policy from generic downstream economy or game APIs.

**Evidence:** `README.md`, `docs/scenarium-adoption.md`, and
`docs/capability-expansion.md`.

## CERES-PF-05: Upstream Branch Drift Breaks The Proof Path

**Status:** MITIGATED

**Pattern:** A Git dependency pins a branch name that no longer exists upstream,
so validation fails before tests can exercise the catalog and simulation path.

**Domain:** RALLY, RLINE, SCENARIUM, RUNE, and future shared dependency
adoption.

**Detection difficulty:** The stale branch is invisible in docs and only appears
when Cargo updates or a clean machine validates the repo.

**Structural solution:** Pin live branches or fixed revisions deliberately and
run Cargo validation during PITFALL adoption.

**Evidence:** `Cargo.toml`, `Cargo.lock`, `git ls-remote --heads https://github.com/giodl73-repo/RALLY.git`,
and `cargo test`.
