---
title: CERES Economic Lens Definitions
version: "1.0"
created: 2026-04-18
spec: specs/2026-04-18-ceres-design.md §6
companion_scales: corpus/program/SCALES.md
---

# CERES Economic Lens Definitions

This document defines the three economic lenses used to evaluate every catalog
entry: **MARKET**, **COOPERATIVE**, and **CIVIC**. Each lens applies a different
viability rule to the same catalog entry data. The result for each (entry × scale ×
lens) cell is a verdict (`win | marginal | fail`) plus a primary numeric metric.

**Division of labor:**

- This document — formulas, inputs, outputs, pass conditions, verdict states,
  and worked examples. Do not duplicate threshold values here; cross-reference
  `corpus/program/SCALES.md` for every numeric threshold.
- `corpus/program/SCALES.md` — all per-scale threshold values (median wages,
  civic cost ceilings, feasible member-pool sizes).
- Plan D simulation code — the formal implementation of these formulas. The math
  here defines the rules; Plan D encodes them in executable form.

---

## 1. Three Lenses — Overview

The same catalog entry is evaluated three times, each time asking a different
viability question:

| Lens | Ownership model | Viability question |
|---|---|---|
| **MARKET** | Private operator, profit motive | Can a single operator recover capital and earn a living wage? |
| **COOPERATIVE** | Worker/member co-op | Can the economics close with a membership pool the community can realistically sustain? |
| **CIVIC** | Municipal / public | Can the annual per-household cost be justified relative to other civic services? |

Scale is a first-class variable. Each lens runs at all three scales (village,
town, small_city), producing nine cells per catalog entry. Threshold values
at each scale are defined in `corpus/program/SCALES.md §2`.

---

## 2. MARKET Lens

### 2.1 Inputs

| Input | Source in catalog entry | Notes |
|---|---|---|
| `capital_cost` | `economics.capital_cost.mid` (or override) | USD; use mid unless scenario specifies otherwise |
| `install_cost` | `economics.install_cost` | USD; added to capital |
| `annual_operating_cost` | `economics.annual_maintenance` + `economics.annual_consumables` + `economics.floor_space_rent_per_year` | Sum of recurring fixed costs |
| `throughput_units_per_year` | `sim_params.throughput_units_equiv_per_year` | Adjusted for `sim_params.downtime_fraction` |
| `variable_cost_per_unit` | `sim_params.variable_cost_per_unit` | USD/unit |
| `market_price_per_unit` | `economics.market_price_per_unit.mid` (or scenario) | USD/unit; required for any MARKET evaluation |
| `labor_hours_per_unit` | `sim_params.labor_hours_per_unit` | Pre-burden wage rate applied separately |
| `cost_of_capital` | Scenario default: **8 %/yr** | Simple interest; may be overridden with justification |
| `scale` | Evaluation cell | Determines median-wage threshold from `SCALES.md §3` |

**Effective throughput:**

```
effective_units_per_year = throughput_units_per_year × (1 − downtime_fraction)
```

### 2.2 Outputs

| Output | Definition |
|---|---|
| **Annual revenue** | `effective_units_per_year × market_price_per_unit` |
| **Annual variable cost** | `effective_units_per_year × variable_cost_per_unit` |
| **Annual gross margin** | `annual_revenue − annual_variable_cost − annual_operating_cost` |
| **Capital service cost** | `(capital_cost + install_cost) × cost_of_capital` |
| **Operator take-home** | `annual_gross_margin − capital_service_cost` |
| **Payback years** *(primary metric)* | `(capital_cost + install_cost) ÷ annual_gross_margin` |
| **ROI** | `annual_gross_margin ÷ (capital_cost + install_cost)` |

### 2.3 Pass Condition

```
MARKET passes if:
  payback_years ≤ 8
  AND operator_take_home ≥ scale_appropriate_median_wage
```

`scale_appropriate_median_wage` — see `corpus/program/SCALES.md §3` for values by scale.

Both sub-conditions must hold. A design that pays back in 5 years but leaves the
operator below the median wage is not a viable market business; a design that pays
the operator well but never recovers capital is not financially sustainable.

### 2.4 Worked Example — forge-003 at Town Scale

Using spec §5 frontmatter numbers (`economics.capital_cost.mid = 28000`,
`install_cost = 6000`, `annual_maintenance = 1500`, `annual_consumables = 4200`,
`floor_space_rent_per_year = 4800`, `sim_params.throughput_units_equiv_per_year =
2400`, `sim_params.downtime_fraction = 0.12`, `sim_params.variable_cost_per_unit =
3.1`, `economics.market_price_per_unit.mid = 45`):

```
effective_units   = 2400 × (1 − 0.12) = 2,112 units/yr
annual_revenue    = 2,112 × $45       = $95,040
annual_var_cost   = 2,112 × $3.10     = $6,547
annual_op_cost    = $1,500 + $4,200 + $4,800 = $10,500
annual_gross_margin = $95,040 − $6,547 − $10,500 = $77,993
capital_service   = ($28,000 + $6,000) × 0.08    = $2,720
operator_take_home = $77,993 − $2,720             = $75,273
payback_years     = $34,000 ÷ $77,993             ≈ 0.44 years
```

At town scale, median wage threshold = $56,000.

- Payback ≤ 8? **Yes** (0.44 yr)
- Take-home ≥ $56,000? **Yes** ($75,273)

Pass condition: **PASS** — the math clears both sub-conditions with significant
margin. Verdict: **win** (>20% margin on both tests — see Section 5).

> Note: These numbers assume full market-rate pricing at mid throughput. The
> `lens_fit.market = marginal` rating in forge-003 reflects qualitative factors
> (local demand uncertainty, operator pipeline) not captured in the base-case math.
> Authors document those factors in `lens_context`; the lens formula evaluates the
> quantitative case only.

---

## 3. COOPERATIVE Lens

### 3.1 Inputs

| Input | Source in catalog entry | Notes |
|---|---|---|
| `capital_cost` | `economics.capital_cost.mid` | USD |
| `install_cost` | `economics.install_cost` | USD |
| `annual_operating_cost` | `economics.annual_maintenance` + `economics.annual_consumables` + `economics.floor_space_rent_per_year` | Shared across members |
| `lifespan_years` | `sim_params.lifespan_years` | Capital amortized over this window |
| `per_member_labor_offset` | Scenario input | Annual value of member labor contributed per member (reduces cash requirement); default $0 if no data |
| `scale` | Evaluation cell | Determines feasible member pool from `SCALES.md §5` |

### 3.2 Outputs

| Output | Definition |
|---|---|
| **Annual capital charge** | `(capital_cost + install_cost) ÷ lifespan_years` |
| **Total annual cost to close** | `annual_capital_charge + annual_operating_cost` |
| **Adjusted annual cost** | `total_annual_cost − (N × per_member_labor_offset)` (iterated for break-even N) |
| **Break-even member count** *(primary metric)* | Minimum N such that `N × per_member_dues ≥ adjusted_annual_cost` |
| **Per-member annual contribution** | `total_annual_cost ÷ break_even_member_count` |
| **Utilization** | `effective_units_per_year ÷ (max_active_hours_per_week × 52 × units_per_hour)` — contextual only |

**Break-even member count formula:**

```
break_even_members = ceil(total_annual_cost ÷ per_member_annual_dues)
```

Where `per_member_annual_dues` is a scenario input (default: $200/yr for a
tool-sharing cooperative — authors override with documented rationale).

### 3.3 Pass Condition

```
COOPERATIVE passes if:
  break_even_members ≤ feasible_member_pool
```

`feasible_member_pool` — see `corpus/program/SCALES.md §5` for participation rates and
pool sizes by scale. The feasible pool for a specific evaluation uses the actual population if known;
otherwise the scale midpoint. Floor constraint: pool is never less than 10 members
(per `SCALES.md §5.5`).

### 3.4 Worked Example — forge-003 at Town Scale

```
annual_capital_charge = ($28,000 + $6,000) ÷ 25 = $1,360/yr
annual_op_cost        = $1,500 + $4,200 + $4,800 = $10,500/yr
total_annual_cost     = $1,360 + $10,500          = $11,860/yr
per_member_dues       = $200/yr (default scenario)
break_even_members    = ceil($11,860 ÷ $200)       = 60 members
feasible_pool (town)  = 7,500 × 0.025              = 188 members
```

- Break-even (60) ≤ feasible pool (188)? **Yes** — margin = 128 members.

Pass condition: **PASS**. Verdict: **win** (60 ÷ 188 = 32% of pool consumed;
≥20% headroom — see Section 5).

---

## 4. CIVIC Lens

### 4.1 Inputs

| Input | Source in catalog entry | Notes |
|---|---|---|
| `capital_cost` | `economics.capital_cost.mid` | USD |
| `install_cost` | `economics.install_cost` | USD |
| `amortization_years` | Scenario input; default **30 years** | Range 25–40; authors may override with justification |
| `annual_operating_cost` | `economics.annual_maintenance` + `economics.annual_consumables` | Floor-space rent excluded (civic facility owns building) |
| `household_count` | Scale-derived (population × 0.40) | From `SCALES.md §2`; actual count if known |
| `annual_public_use_hours` | Scenario input | Total open-access hours per year; required for usage-rate test |
| `scale` | Evaluation cell | Determines cost and usage thresholds from `SCALES.md §4` |

### 4.2 Outputs

| Output | Definition |
|---|---|
| **Annual capital charge** | `(capital_cost + install_cost) ÷ amortization_years` |
| **Total annual civic cost** | `annual_capital_charge + annual_operating_cost` |
| **Per-household annual cost** *(primary metric)* | `total_annual_civic_cost ÷ household_count` |
| **Hours-of-use per capita** | `annual_public_use_hours ÷ population` |

### 4.3 Pass Condition

```
CIVIC passes if:
  per_household_annual_cost ≤ civic_cost_threshold
  AND hours_of_use_per_capita ≥ usage_rate_threshold
```

Per-household cost thresholds — see `corpus/program/SCALES.md §4` for values by scale.

Usage-rate thresholds are defined per-entry in the simulation scenario (the spec
does not prescribe a universal number; minimum viable usage is context-dependent).
The default baseline is **2 hours/capita/year**; entries with specialized equipment
may apply a lower threshold with documented rationale.

Both sub-conditions must hold: a cheap facility no one uses does not pass; a
heavily used facility that consumes an unreasonable share of the household budget
does not pass.

### 4.4 Worked Example — forge-003 at Town Scale

```
annual_capital_charge    = ($28,000 + $6,000) ÷ 30 = $1,133/yr
annual_op_cost (civic)   = $1,500 + $4,200          = $5,700/yr
  (floor-space rent excluded — civic building)
total_annual_civic_cost  = $1,133 + $5,700           = $6,833/yr
household_count (town)   = 7,500 × 0.40              = 3,000 households
per_household_cost       = $6,833 ÷ 3,000            = $2.28/hh/yr
threshold (town)         = $100/hh/yr
```

Usage rate: assume 1,560 open-access hours/yr (30 hr/wk × 52 wk) and town
population 7,500:

```
hours_per_capita = 1,560 ÷ 7,500 = 0.21 hr/capita/yr
```

- Per-household cost ($2.28) ≤ $100? **Yes** — well below threshold.
- Usage rate (0.21 hr/capita) ≥ 2.0 hr/capita? **No** — fails usage-rate test.

Pass condition: **FAIL** (usage-rate sub-condition not met at default threshold).
The forge serves a specialized subset of residents; the civic model requires
either a lower usage-rate threshold (justified by the specialized-equipment
exception) or a program structure that broadens access. Authors document this
reasoning in `lens_context.civic`.

---

## 5. Verdict States

Each (entry × scale × lens) cell receives one verdict.

### 5.1 Definitions

| Verdict | Meaning | Numeric definition |
|---|---|---|
| `win` | Passes with meaningful margin | All pass-condition sub-conditions met AND margin ≥ 20% on the primary metric |
| `marginal` | Passes narrowly OR relies on optimistic assumptions | All sub-conditions met but primary-metric margin < 20%; OR: passes only with an optimistic-scenario input (e.g., `market_price_per_unit.high` instead of `.mid`) |
| `fail` | Does not pass | One or more pass-condition sub-conditions not met under any reasonable scenario |

### 5.2 Margin Definitions by Lens

**MARKET lens — margin on payback years:**

```
payback_margin = (8 − payback_years) ÷ 8
win     : payback_margin ≥ 0.20  (payback ≤ 6.4 years)
marginal: payback_margin  < 0.20  (payback between 6.4 and 8.0 years)
          OR operator_take_home within 20% below median-wage threshold
fail    : payback > 8 years OR operator_take_home < median_wage threshold
```

**COOPERATIVE lens — margin on member headroom:**

```
member_headroom_ratio = (feasible_pool − break_even_members) ÷ feasible_pool
win     : member_headroom_ratio ≥ 0.20  (break-even uses ≤ 80% of feasible pool)
marginal: member_headroom_ratio  < 0.20  (break-even uses > 80% of feasible pool)
fail    : break_even_members > feasible_pool
```

**CIVIC lens — margin on per-household cost:**

```
cost_margin = (threshold − per_household_cost) ÷ threshold
win     : cost_margin ≥ 0.20  (cost ≤ 80% of threshold) AND usage-rate met
marginal: cost_margin  < 0.20 AND cost ≤ threshold AND usage-rate met
          OR: usage-rate met only with optimistic assumptions
fail    : per_household_cost > threshold OR usage-rate not met
```

### 5.3 Multi-sub-condition cases

When a lens has two sub-conditions (MARKET: payback + wage; CIVIC: cost +
usage-rate), the verdict uses the **worse** of the two sub-condition results:

- If one sub-condition gives `win` and the other gives `marginal` → verdict is `marginal`.
- If either sub-condition gives `fail` → verdict is `fail`.

### 5.4 Optimistic-scenario flag

An entry may be evaluated with optimistic inputs (e.g., high market price,
high throughput, low downtime). If a pass is achieved only under optimistic inputs
that are not the `.mid` scenario defaults, the verdict is capped at `marginal`
regardless of margin. The simulation run must document which inputs were optimistic.

---

## 6. Primary Numeric Metric by Lens

The `results:` block in each catalog entry stores one primary metric per cell
alongside the verdict.

| Lens | Primary metric | Unit | Direction |
|---|---|---|---|
| MARKET | `payback_years` | years | lower is better (ceiling: 8) |
| COOPERATIVE | `break_even_members` | count | lower is better (ceiling: feasible pool) |
| CIVIC | `per_household_cost` | USD/hh/yr | lower is better (ceiling: scale threshold) |

These are the metrics compared against thresholds to determine pass/fail and margin.
Secondary metrics (ROI, per-member contribution, hours-per-capita) are computed and
stored but do not determine the verdict.

---

## 7. Deferrals

The following are intentionally deferred to Plan D (simulation code):

- Formal implementation of the above formulas as executable functions.
- Sensitivity analysis and Monte Carlo around `cost_sd` and throughput variance.
- Automated population of the `results:` block in catalog entries.
- Multi-currency normalization (handled at evaluation time via
  `corpus/program/CURRENCIES.md`; not part of lens math).
- Any lens extension for trades outside smithing (the formulas here are
  trade-agnostic; trade-specific throughput units are resolved before lens
  evaluation via `sim_params.throughput_units_equiv_per_year`).

---

## Appendix A: Threshold Cross-Reference

**`corpus/program/SCALES.md` is the authoritative source for all numeric threshold
values. The values below are a convenience reference only; if they diverge from
`SCALES.md`, `SCALES.md` governs.**

| Lens | Parameter | Defined in |
|---|---|---|
| MARKET | Scale-appropriate median wage | `SCALES.md §3` |
| CIVIC | Per-household cost ceiling | `SCALES.md §4` |
| COOPERATIVE | Participation rate | `SCALES.md §5` |
| COOPERATIVE | Feasible pool (at midpoint pop) | `SCALES.md §5` |
| COOPERATIVE | Floor constraint (min pool) | `SCALES.md §5.5` |

For the actual numeric values, read `corpus/program/SCALES.md` directly. Values
there are **illustrative anchors** that must be refined before any simulation run
is promoted from `draft` to `validated`.
