"""Tier A lens functions. See corpus/program/ECONOMIC-LENSES.md."""
import math
from typing import Literal, NamedTuple

# MARKET lens: cost of capital rate (ECONOMIC-LENSES.md §2.1)
COST_OF_CAPITAL = 0.08  # 8%/yr

# MARKET lens: per-member annual dues default (ECONOMIC-LENSES.md §3.2)
DEFAULT_DUES_PER_MEMBER = 200  # USD/yr

# CIVIC lens: default amortization years (ECONOMIC-LENSES.md §4.1)
DEFAULT_AMORTIZATION_YEARS = 30

# CIVIC lens: default usage rate threshold (ECONOMIC-LENSES.md §4.3)
DEFAULT_USAGE_RATE_THRESHOLD = 2.0  # hr/capita/yr

# Verdict margin: 20% on primary metric (ECONOMIC-LENSES.md §5.2)
MARGIN_WIN = 0.20


class LensResult(NamedTuple):
    verdict: Literal["win", "marginal", "fail"]
    primary_metric: float
    metric_name: str
    notes: str = ""


def market_lens(entry: dict, scale: str, scales: dict) -> LensResult:
    """MARKET lens pass condition: payback ≤ 8 years AND operator_take_home ≥ scale_median_wage.

    Primary metric: payback_years (lower is better; ceiling 8).
    Verdict margins (ECONOMIC-LENSES.md §5.2):
      win     : payback_margin ≥ 0.20  (payback ≤ 6.4 yr) AND take-home ≥ median_wage × 1.20
      marginal: payback ≤ 8 AND (payback_margin < 0.20 OR take-home within [median×0.80, median×1.20))
      fail    : payback > 8 yr OR take-home < median_wage × 0.80
    """
    econ = entry["economics"]
    params = entry["sim_params"]
    scale_data = scales[scale]

    capital_cost = econ["capital_cost"]["mid"]
    install_cost = econ.get("install_cost", 0)
    total_invested = capital_cost + install_cost

    annual_maintenance = econ.get("annual_maintenance", 0)
    annual_consumables = econ.get("annual_consumables", 0)
    floor_space_rent = econ.get("floor_space_rent_per_year", 0)
    annual_fixed = annual_maintenance + annual_consumables + floor_space_rent

    throughput = params["throughput_units_equiv_per_year"]
    downtime = params.get("downtime_fraction", 0.0)
    effective_units = throughput * (1.0 - downtime)

    # Entries with lens_fit.market: poor legitimately omit market_price_per_unit
    mpu = econ.get("market_price_per_unit")
    if not mpu or mpu.get("mid", 0) == 0:
        return LensResult(
            verdict="fail",
            primary_metric=-1.0,
            metric_name="payback_years",
            notes="market_price_per_unit absent or zero; entry not designed for market lens",
        )
    market_price = mpu["mid"]
    variable_cost_per_unit = params.get("variable_cost_per_unit", 0.0)

    annual_revenue = effective_units * market_price
    annual_variable = effective_units * variable_cost_per_unit
    annual_gross_margin = annual_revenue - annual_variable - annual_fixed

    capital_service = total_invested * COST_OF_CAPITAL
    operator_take_home = annual_gross_margin - capital_service

    median_wage = scale_data["median_wage"]

    # Division-by-zero guard: if gross_margin <= 0, payback is never recoverable
    if annual_gross_margin <= 0:
        payback_years = -1.0
        verdict = "fail"
        notes = "annual_gross_margin <= 0; payback never recoverable"
        return LensResult(
            verdict=verdict,
            primary_metric=payback_years,
            metric_name="payback_years",
            notes=notes,
        )

    payback_years = total_invested / annual_gross_margin

    # Wage sub-condition
    # win on wage: take_home >= median_wage × 1.20
    # marginal on wage: take_home in [median_wage × 0.80, median_wage × 1.20)
    # fail on wage: take_home < median_wage × 0.80
    wage_win_threshold = median_wage * 1.20
    wage_fail_threshold = median_wage * 0.80

    if operator_take_home < wage_fail_threshold:
        wage_verdict = "fail"
    elif operator_take_home < wage_win_threshold:
        wage_verdict = "marginal"
    else:
        wage_verdict = "win"

    # Payback sub-condition
    # win on payback: payback <= 6.4 (i.e., margin >= 20% of ceiling 8)
    # marginal on payback: 6.4 < payback <= 8.0
    # fail on payback: payback > 8.0
    payback_ceiling = 8.0
    if payback_years > payback_ceiling:
        payback_verdict = "fail"
    elif payback_years > payback_ceiling * (1.0 - MARGIN_WIN):
        # payback > 6.4
        payback_verdict = "marginal"
    else:
        payback_verdict = "win"

    # Combine: use worst of the two sub-conditions (ECONOMIC-LENSES.md §5.3)
    verdict_rank = {"win": 0, "marginal": 1, "fail": 2}
    combined_rank = max(verdict_rank[wage_verdict], verdict_rank[payback_verdict])
    verdict_map = {0: "win", 1: "marginal", 2: "fail"}
    verdict = verdict_map[combined_rank]

    notes_parts = []
    if wage_verdict != "win":
        notes_parts.append(
            f"wage_verdict={wage_verdict} (take_home={operator_take_home:.0f} vs median={median_wage})"
        )
    if payback_verdict != "win":
        notes_parts.append(f"payback_verdict={payback_verdict} (payback={payback_years:.2f} yr)")

    return LensResult(
        verdict=verdict,
        primary_metric=float(payback_years),
        metric_name="payback_years",
        notes="; ".join(notes_parts),
    )


def coop_lens(entry: dict, scale: str, scales: dict) -> LensResult:
    """COOPERATIVE lens pass condition: break_even_member_count ≤ feasible_member_pool.

    Primary metric: break_even_members (lower is better; ceiling = feasible_pool).
    Verdict margins (ECONOMIC-LENSES.md §5.2):
      win     : member_headroom_ratio ≥ 0.20  (break-even ≤ 80% of feasible pool)
      marginal: member_headroom_ratio  < 0.20  (break-even > 80% of feasible pool)
      fail    : break_even_members > feasible_pool
    per_member_annual_dues default: $200/yr (ECONOMIC-LENSES.md §3.2).
    """
    econ = entry["economics"]
    params = entry["sim_params"]
    scale_data = scales[scale]

    capital_cost = econ["capital_cost"]["mid"]
    install_cost = econ.get("install_cost", 0)
    total_invested = capital_cost + install_cost

    annual_maintenance = econ.get("annual_maintenance", 0)
    annual_consumables = econ.get("annual_consumables", 0)
    floor_space_rent = econ.get("floor_space_rent_per_year", 0)
    annual_op_cost = annual_maintenance + annual_consumables + floor_space_rent

    lifespan_years = params.get("lifespan_years", 25)
    annual_capital_charge = total_invested / lifespan_years

    total_annual_cost = annual_capital_charge + annual_op_cost

    dues = params.get("per_member_annual_dues", DEFAULT_DUES_PER_MEMBER)

    break_even = math.ceil(total_annual_cost / dues)

    # Feasible member pool
    population_midpoint = scale_data["population_midpoint"]
    participation_rate = scale_data["participation_rate"]
    member_pool_floor = scale_data.get("member_pool_floor", 10)
    feasible_pool = max(population_midpoint * participation_rate, member_pool_floor)

    if break_even > feasible_pool:
        verdict = "fail"
    else:
        headroom_ratio = (feasible_pool - break_even) / feasible_pool
        if headroom_ratio >= MARGIN_WIN:
            verdict = "win"
        else:
            verdict = "marginal"

    return LensResult(
        verdict=verdict,
        primary_metric=float(break_even),
        metric_name="break_even_members",
        notes=(
            f"feasible_pool={feasible_pool:.1f}, break_even={break_even}, "
            f"total_annual_cost={total_annual_cost:.0f}"
        ),
    )


def civic_lens(entry: dict, scale: str, scales: dict) -> LensResult:
    """CIVIC lens pass condition: per_household_cost ≤ scale_threshold AND utilization ≥ threshold.

    Primary metric: per_household_cost (lower is better; ceiling = scale threshold).
    Amortization default: 30 years (ECONOMIC-LENSES.md §4.1).
    Floor-space rent excluded from civic operating costs (civic facility owns building).
    Verdict margins (ECONOMIC-LENSES.md §5.2):
      win     : cost_margin ≥ 0.20 AND usage-rate met
      marginal: cost_margin  < 0.20 AND cost ≤ threshold AND usage-rate met
      fail    : per_household_cost > threshold OR usage-rate not met
    """
    econ = entry["economics"]
    params = entry["sim_params"]
    scale_data = scales[scale]

    capital_cost = econ["capital_cost"]["mid"]
    install_cost = econ.get("install_cost", 0)
    total_invested = capital_cost + install_cost

    # Civic operating costs exclude floor-space rent (civic facility owns building)
    annual_maintenance = econ.get("annual_maintenance", 0)
    annual_consumables = econ.get("annual_consumables", 0)
    annual_op_cost_civic = annual_maintenance + annual_consumables

    amortization_years = params.get("amortization_years", DEFAULT_AMORTIZATION_YEARS)
    annual_capital_charge = total_invested / amortization_years

    total_civic_cost = annual_capital_charge + annual_op_cost_civic

    household_count = scale_data["household_count"]
    per_household_cost = total_civic_cost / household_count

    threshold = scale_data["civic_cost_threshold_per_household"]

    # Usage rate sub-condition
    population_midpoint = scale_data["population_midpoint"]
    annual_public_use_hours = params.get("annual_public_use_hours", 0)
    usage_rate_threshold = params.get("usage_rate_threshold", DEFAULT_USAGE_RATE_THRESHOLD)

    hours_per_capita = annual_public_use_hours / population_midpoint if population_midpoint > 0 else 0.0
    usage_passes = hours_per_capita >= usage_rate_threshold

    # Cost sub-condition
    if per_household_cost > threshold:
        cost_verdict = "fail"
    else:
        cost_margin = (threshold - per_household_cost) / threshold
        if cost_margin >= MARGIN_WIN:
            cost_verdict = "win"
        else:
            cost_verdict = "marginal"

    # Usage verdict
    usage_verdict = "win" if usage_passes else "fail"

    # Combine: worst of the two sub-conditions (ECONOMIC-LENSES.md §5.3)
    verdict_rank = {"win": 0, "marginal": 1, "fail": 2}
    combined_rank = max(verdict_rank[cost_verdict], verdict_rank[usage_verdict])
    verdict_map = {0: "win", 1: "marginal", 2: "fail"}
    verdict = verdict_map[combined_rank]

    notes_parts = [
        f"per_hh={per_household_cost:.2f}, threshold={threshold}, "
        f"hrs/capita={hours_per_capita:.3f} vs threshold={usage_rate_threshold}"
    ]

    return LensResult(
        verdict=verdict,
        primary_metric=float(per_household_cost),
        metric_name="per_household_cost",
        notes="; ".join(notes_parts),
    )
