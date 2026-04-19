# P-2 — The Commons Theorist — Review of ceres-design (R1)

**Overall:** The spec honors the cooperative lens in name and in review architecture, which is more than most projects do. But the catalog schema promotes coop viability to a tri-state label (`cooperative: good | marginal | poor`) without requiring any of the governance specification that actually determines whether a coop survives. A coop-good label without a governance sketch is exactly the romantic shorthand Ostrom spent her career dismantling.

**What works:**
- Section 3 treats the cooperative lens as genuinely first-class, not an afterthought to the market lens.
- Section 6 COOPERATIVE lens rule names break-even member count, per-member contribution, and utilization as the required outputs. These are the right metrics.
- Section 11 mentions borrowing "review/panel/scoring patterns" from sister projects — which includes the discipline of forcing multi-voice adjudication on every artifact. That's Ostrom-compatible governance for the artifact layer itself.
- Non-goals (Section 12) does not overclaim cooperative universalism. Good restraint.

**What doesn't:**
- The catalog schema (Section 5) has `lens_fit.cooperative: good | marginal | poor` with **no accompanying governance-sketch field**. A catalog entry can claim `cooperative: good` without specifying membership rules, usage rules, damage-handling, graduated sanctions, or conflict resolution — the things that actually distinguish a sustainable coop from a collapsing one.
- Section 6 COOPERATIVE lens pass condition is "break-even member count ≤ feasible member pool at that scale" — but the spec never defines what "feasible member pool" means. 1% of population? 5%? Based on what evidence? For a tool library in a town of 10,000, is 80 members feasible? 200? This is doing a lot of unspecified work.
- No requirement that coop entries address the eight Ostrom design principles, even as a lightweight checklist. I am not asking for a legal treatise; I am asking for five lines acknowledging: membership boundaries, rule legitimacy, monitoring, graduated sanctions, conflict resolution.
- The spec's framework doc (`corpus/program/ECONOMIC-LENSES.md`) is named but not drafted here. The coop-lens math might address this — but the spec needs to commit to it as a *schema requirement*, not hope that a formula file will catch it.

**The question I'd push on:**
Where in the catalog-entry schema is the governance structure of a coop-good entry captured? Without that field — even as a short structured block — `cooperative: good` is an aspiration, not a claim, and CERES will produce a catalog of well-intentioned labels rather than a catalog of specific governance designs.
