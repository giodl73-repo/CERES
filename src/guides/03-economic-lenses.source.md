# Economic Lenses

Every catalog entry is evaluated under three economic lenses. The same
design data is run through three different ownership models, each asking a
different viability question. The result is nine verdicts per entry
(3 scales × 3 lenses).

This guide explains each lens, the pass conditions, the verdict states, and
how to read the numbers. Full formulas: `corpus/program/ECONOMIC-LENSES.md`.
Scale thresholds: `corpus/program/SCALES.md`.

---

## Why three lenses?

No single ownership model captures the full range of ways a community might
restore local production. A design that only works as a private business has
different policy implications than one that only works as a cooperative or a
civic facility. The three lenses surface those differences explicitly.

| Lens | Ownership model | Viability question |
|------|-----------------|-------------------|
| **MARKET** | Private operator | Can one person recover capital and earn a living wage? |
| **COOPERATIVE** | Worker/member co-op | Can dues from a realistic membership pool close the economics? |
| **CIVIC** | Municipal / public | Can the per-household cost be justified alongside other civic services? |

A design that passes all three at all three scales is a generalist winner. Most
designs are specialists — strong in one lens, weak in others. The verdict grid
tells that story.

---

## Scale parameters

All lens thresholds are scale-dependent. The three scales and their key
parameters:

| Parameter | Village (500–2k) | Town (2k–15k) | Small city (15k–75k) |
|-----------|-----------------|---------------|---------------------|
| Population midpoint | 1,000 | 7,500 | 40,000 |
| Household count (pop × 0.40) | 400 | 3,000 | 16,000 |
| Median wage threshold (MARKET) | $48,000 / yr | $56,000 / yr | $62,000 / yr |
| Civic cost ceiling (CIVIC) | $120 / hh / yr | $100 / hh / yr | $80 / hh / yr |
| Feasible member pool (COOP, 2.5% / 2.0%) | 25 members | 188 members | 800 members |

---

## MARKET lens

The MARKET lens asks: can a private operator run this design profitably enough
to pay themselves a living wage and recover their capital?

### Formula

```proof:math width=60 align=left
\text{effective\_units} = \text{throughput} \times (1 - \text{downtime})
```

```proof:math width=60 align=left
\text{gross\_margin} = (\text{effective\_units} \times \text{price}) - (\text{effective\_units} \times \text{variable\_cost}) - \text{annual\_op\_cost}
```

```proof:math width=60 align=left
\text{payback\_years} = \frac{\text{capital} + \text{install}}{\text{gross\_margin}}
```

```proof:math width=60 align=left
\text{operator\_take\_home} = \text{gross\_margin} - (\text{capital} + \text{install}) \times 0.08
```

### Pass condition

Both sub-conditions must hold:

```
payback_years ≤ 8
AND operator_take_home ≥ scale_median_wage
```

A design that pays back quickly but leaves the operator below median wage is
not a viable business. A design that pays well but never recovers capital is
not financially sustainable.

### Inputs

| Input | Source in catalog entry |
|-------|------------------------|
| `capital_cost` | `economics.capital_cost.mid` |
| `install_cost` | `economics.install_cost` |
| `annual_op_cost` | maintenance + consumables + floor rent |
| `throughput` | `sim_params.throughput_units_equiv_per_year` |
| `variable_cost` | `sim_params.variable_cost_per_unit` |
| `price` | `economics.market_price_per_unit.mid` |
| `downtime` | `sim_params.downtime_fraction` |
| Cost of capital | 8 %/yr (default) |

---

## COOPERATIVE lens

The COOPERATIVE lens asks: can enough members join and pay dues to cover the
shared costs of the equipment, without requiring more members than the community
can realistically sustain?

### Formula

```proof:math width=60 align=left
\text{annual\_capital\_charge} = \frac{\text{capital} + \text{install}}{\text{lifespan\_years}}
```

```proof:math width=60 align=left
\text{total\_annual\_cost} = \text{annual\_capital\_charge} + \text{annual\_op\_cost}
```

```proof:math width=60 align=left
\text{break\_even\_members} = \left\lceil \frac{\text{total\_annual\_cost}}{\text{per\_member\_dues}} \right\rceil
```

### Pass condition

```
break_even_members ≤ feasible_member_pool
```

The feasible pool is `population × participation_rate` (2.5% for village/town,
2.0% for small city). The floor is 10 members regardless.

`per_member_dues` defaults to $200/yr for a tool-sharing cooperative. Authors
override with documented rationale if the specific cooperative structure
justifies a different figure.

### Note on the cooperative form

The COOPERATIVE lens evaluates whether the *economics* close with a realistic
membership pool. It does not evaluate whether the cooperative *governance* is
feasible. Governance design — rules, monitoring, graduated sanctions, conflict
resolution — lives in `lens_context.cooperative` and is evaluated qualitatively
by P-2 Commons Theorist during panel review.

---

## CIVIC lens

The CIVIC lens asks: if the municipal government funded and operated this
facility, could the annual per-household cost be justified relative to other
civic services?

### Formula

```proof:math width=60 align=left
\text{annual\_capital\_charge} = \frac{\text{capital} + \text{install}}{\text{amortization\_years}}
```

```proof:math width=60 align=left
\text{total\_civic\_cost} = \text{annual\_capital\_charge} + \text{annual\_op\_cost (excl. rent)}
```

```proof:math width=60 align=left
\text{per\_household\_cost} = \frac{\text{total\_civic\_cost}}{\text{household\_count}}
```

Note: floor-space rent is excluded from the CIVIC lens — a civic facility owns
its building. `amortization_years` defaults to 30 years (range 25–40).

### Pass condition

Both sub-conditions must hold:

```
per_household_annual_cost ≤ civic_cost_threshold
AND hours_of_use_per_capita ≥ usage_rate_threshold
```

A cheap facility no one uses does not pass. A heavily used facility that
consumes an unreasonable share of the household budget does not pass.

The usage-rate threshold defaults to **2 hours/capita/year**. Entries with
specialized equipment may apply a lower threshold with documented rationale.

### Benchmark context

The civic cost thresholds are set relative to public library operating costs
(IMLS Public Library Survey, FY 2021). A production facility serves a subset
of residents and faces a tighter justification than a universal service like a
library. The thresholds reflect this:

- Village ($120/hh/yr): slightly above library parity, giving headroom for
  community-economic-development justification.
- Town ($100/hh/yr): approximately at library lower bound.
- Small city ($80/hh/yr): below library parity; city budgets face more competing
  service demands.

---

## Verdict states

Every (entry × scale × lens) cell receives one verdict.

| Verdict | Meaning |
|---------|---------|
| `win` | All pass-condition sub-conditions met AND primary-metric margin ≥ 20% |
| `marginal` | Passes narrowly (margin < 20%) OR passes only under optimistic inputs |
| `fail` | One or more sub-conditions not met under any reasonable scenario |

### Margin definitions

**MARKET** — margin on payback years:

```
payback_margin = (8 − payback_years) ÷ 8

win     : payback_margin ≥ 0.20  (payback ≤ 6.4 years)
marginal: payback_margin  < 0.20  (payback 6.4–8.0 years)
          OR operator_take_home within 20% below wage threshold
fail    : payback > 8 years OR take-home < wage threshold
```

**COOPERATIVE** — margin on member headroom:

```
headroom_ratio = (feasible_pool − break_even) ÷ feasible_pool

win     : headroom_ratio ≥ 0.20  (break-even uses ≤ 80% of pool)
marginal: headroom_ratio  < 0.20  (break-even uses > 80% of pool)
fail    : break_even > feasible_pool
```

**CIVIC** — margin on per-household cost:

```
cost_margin = (threshold − per_hh_cost) ÷ threshold

win     : cost_margin ≥ 0.20 AND usage-rate met
marginal: cost_margin  < 0.20 AND cost ≤ threshold AND usage-rate met
fail    : per_hh_cost > threshold OR usage-rate not met
```

When a lens has two sub-conditions, the **worse** of the two governs: a `win`
on one and `marginal` on the other → verdict is `marginal`.

### Optimistic-scenario cap

If a pass is achieved only by using optimistic inputs (e.g.,
`market_price_per_unit.high` instead of `.mid`), the verdict is capped at
`marginal` regardless of margin. The simulation run must document which inputs
were optimistic.

---

## Worked example — bake-001 at town scale

Using mid-case inputs:

**MARKET:**
```
effective_units = 29,500 × (1 − 0.10) = 26,550 loaves/yr
annual_revenue  = 26,550 × $8         = $212,400
annual_var_cost = 26,550 × $0.33      = $8,762
annual_op_cost  = $1,200 + $8,500 + $3,000 = $12,700
gross_margin    = $212,400 − $8,762 − $12,700 = $190,938
capital_service = ($32,000 + $4,000) × 0.08  = $2,880
take-home       = $190,938 − $2,880           = $188,058
payback_years   = $36,000 ÷ $190,938          ≈ 0.19 years
```

- Payback ≤ 8? **Yes** (0.19 yr). Margin = (8 − 0.19) / 8 = 98%. `win`.
- Take-home ≥ $56,000? **Yes** ($188,058). `win`.
- Verdict: **win**.

```proof:callout kind=note label="Why the numbers differ from the results block"
The `results:` block stores the Tier A simulation output, which uses the
sim_params fields directly and applies the downtime adjustment at evaluation
time. The worked example above applies the adjustment manually and uses
economics.market_price_per_unit.mid = $8. Minor rounding differences are
expected.
```

**CIVIC at town:**
```
annual_capital_charge = $36,000 ÷ 30  = $1,200/yr
annual_op_cost (civic) = $1,200 + $8,500 = $9,700/yr  (rent excluded)
total_civic_cost       = $1,200 + $9,700  = $10,900/yr
household_count (town) = 7,500 × 0.40    = 3,000
per_household_cost     = $10,900 ÷ 3,000 = $3.63/hh/yr
threshold (town)       = $100/hh/yr
```

Cost passes easily ($3.63 vs. $100). But the usage-rate test: a single-operator
private bakery generates no public access hours. Civic model fails the
usage-rate sub-condition. Verdict: **fail**.

This is correct. Bake-001 is a private business. It should pass MARKET and fail
CIVIC. The lens combination is the signal.

---

## Reading the full results grid

When you see bake-001's results:

| | Market | Cooperative | Civic |
|-|--------|-------------|-------|
| Village | win | fail | fail |
| Town | win | win | fail |
| Small city | win | win | fail |

This tells you: bake-001 works as a private business at all scales, works as a
cooperative at town and small-city scale (membership pool is large enough), and
does not work as a civic facility at any scale (usage-rate failure — it is not
designed for public access). That is a coherent and honest picture of the design.
