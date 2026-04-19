# P-1 — The Market Economist — Review of ceres-design (R1)

**Overall:** The spec is disciplined about naming the market lens as one of three rather than the test. That's correct — CERES is explicitly not claiming every trade can be a market winner. But the spec leaves the market-viability *expectation* unstated, and the schema is missing the single field I most need to evaluate any entry: the assumed market price of the trade's output.

**What works:**
- Section 3 explicitly defines three economic lenses as parallel viability frames (market / coop / civic). The spec does not pretend market viability is the only meaningful test. Good.
- Section 6 MARKET lens rule is properly scoped: payback ≤ 8 years AND operator earns ≥ scale-appropriate median wage. Both conditions, not just one.
- Non-goals (Section 12) honestly state this is not due-diligence-ready procurement work. That framing prevents the reader from mistaking research-paper estimates for underwriting.
- The vertical-slice approach (Section 3, Section 10) is sound business discipline. Prove one trade's unit economics before scaling the method. I approve.

**What doesn't:**
- The catalog schema (Section 5) includes cost structure, throughput, and labor — but **no field for the market-clearing price of the trade's output**. You cannot compute payback or operator take-home without it. A forge producing 2,400 units per year at what price per unit? The `variable_cost_per_unit` is in the schema; the revenue per unit is implicit and uncited.
- Section 6 says "market price" as a MARKET lens input, but there is no corresponding frontmatter field in the schema (Section 5). A catalog entry could pass my review without ever declaring the price assumption.
- The spec never states the expected *distribution* of outcomes — how many of 15 entries are expected to pass the market lens? If zero pass, is that a finding or a failure? A project that quietly expects zero market winners but never says so is hiding its thesis.
- Section 2 "local production collapsed not because communities stopped needing it, but because the equipment didn't pencil out" — this is a claim, not a hypothesis. The spec treats it as established. A market economist wants this as a testable thesis, not a premise.

**The question I'd push on:**
What is the assumed end-market price for the output of each trade, where is it captured in the schema, and what distribution of market-lens verdicts across the 15 forge entries would count as *validating* versus *invalidating* the project's central claim?
