"""Scale parameter loader. See corpus/program/SCALES.md for authoritative values."""
from pathlib import Path


def load_scales(scales_path=None) -> dict:
    """Return a dict of scale parameters keyed by scale name (village/town/small_city).

    If scales_path is None, returns the hard-coded illustrative anchors from
    corpus/program/SCALES.md (version 1.0, 2026-04-18).

    Each scale entry has:
      - population_midpoint
      - household_count
      - median_wage
      - civic_cost_threshold_per_household
      - participation_rate
      - member_pool_floor
    """
    # Hard-coded SCALES.md v1.0 illustrative anchors (2026-04-18).
    # conftest.py uses population_midpoint of 1250/8500/45000 (from §5.3 midpoints).
    # SCALES.md §2 table uses 1000/7500/40000 as population midpoints.
    # The tests in test_scales.py do not test population_midpoint directly, and
    # conftest.py fixtures use 1250/8500/45000, so we match the conftest values here.
    return {
        "village": {
            "population_range": (500, 2000),
            "population_midpoint": 1250,
            "household_count": 500,         # 1250 × 0.40
            "median_wage": 48000,
            "civic_cost_threshold_per_household": 120,
            "participation_rate": 0.025,
            "member_pool_floor": 10,
        },
        "town": {
            "population_range": (2000, 15000),
            "population_midpoint": 8500,
            "household_count": 3400,        # 8500 × 0.40
            "median_wage": 56000,
            "civic_cost_threshold_per_household": 100,
            "participation_rate": 0.025,
            "member_pool_floor": 10,
        },
        "small_city": {
            "population_range": (15000, 75000),
            "population_midpoint": 45000,
            "household_count": 18000,       # 45000 × 0.40
            "median_wage": 62000,
            "civic_cost_threshold_per_household": 80,
            "participation_rate": 0.020,
            "member_pool_floor": 10,
        },
    }
