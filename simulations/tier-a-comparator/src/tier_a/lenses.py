"""Tier A lens functions. See corpus/program/ECONOMIC-LENSES.md."""
import math
from typing import Literal, NamedTuple


class LensResult(NamedTuple):
    verdict: Literal["win", "marginal", "fail"]
    primary_metric: float
    metric_name: str
    notes: str = ""


def market_lens(entry: dict, scale: str, scales: dict) -> LensResult:
    """MARKET lens pass condition: payback ≤ 8 years AND operator_take_home ≥ scale_median_wage.

    Primary metric: payback_years (lower is better; ceiling 8).
    Verdict margins (ECONOMIC-LENSES.md §5.2):
      win     : payback_margin ≥ 0.20  (payback ≤ 6.4 yr) AND take-home ≥ median_wage
      marginal: payback_margin  < 0.20 (payback 6.4–8.0 yr) OR take-home within 20% below threshold
      fail    : payback > 8 yr OR take-home < median_wage
    """
    raise NotImplementedError


def coop_lens(entry: dict, scale: str, scales: dict) -> LensResult:
    """COOPERATIVE lens pass condition: break_even_member_count ≤ feasible_member_pool.

    Primary metric: break_even_members (lower is better; ceiling = feasible_pool).
    Verdict margins (ECONOMIC-LENSES.md §5.2):
      win     : member_headroom_ratio ≥ 0.20  (break-even ≤ 80% of feasible pool)
      marginal: member_headroom_ratio  < 0.20  (break-even > 80% of feasible pool)
      fail    : break_even_members > feasible_pool
    per_member_annual_dues default: $200/yr (ECONOMIC-LENSES.md §3.2).
    """
    raise NotImplementedError


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
    raise NotImplementedError
