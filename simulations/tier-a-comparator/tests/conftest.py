"""pytest configuration and shared fixtures for Tier A tests."""
import sys
from pathlib import Path

# Add src/ to sys.path so `import tier_a` works without an editable install
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import pytest


@pytest.fixture
def scales_fixture():
    """Hard-coded scale parameters from corpus/program/SCALES.md v1.0 (2026-04-18)."""
    return {
        "village": {
            "population_midpoint": 1250,
            "household_count": 500,
            "median_wage": 48000,
            "civic_cost_threshold_per_household": 120,
            "participation_rate": 0.025,
            "member_pool_floor": 10,
        },
        "town": {
            "population_midpoint": 8500,
            "household_count": 3400,
            "median_wage": 56000,
            "civic_cost_threshold_per_household": 100,
            "participation_rate": 0.025,
            "member_pool_floor": 10,
        },
        "small_city": {
            "population_midpoint": 45000,
            "household_count": 18000,
            "median_wage": 62000,
            "civic_cost_threshold_per_household": 80,
            "participation_rate": 0.020,
            "member_pool_floor": 10,
        },
    }


@pytest.fixture
def entry_fixture():
    """Canonical mini-entry for lens testing.

    Matches ECONOMIC-LENSES.md §2.4 worked example (forge-003 at Town Scale).
    Adjust per-test as needed by copying and mutating in the test body.
    """
    return {
        "id": "test-forge-001",
        "trade": "smithing",
        "economics": {
            "currency": "USD",
            "capital_cost": {"low": 18000, "mid": 28000, "high": 45000},
            "install_cost": 6000,
            "annual_maintenance": 1500,
            "annual_consumables": 4200,
            "floor_space_rent_per_year": 4800,
            "market_price_per_unit": {"low": 32, "mid": 45, "high": 70},
            "industrial_baseline_price": 12,
        },
        "sim_params": {
            "cost_mean": 28000,
            "cost_sd": 8000,
            "throughput_units_equiv_per_year": 2400,
            "variable_cost_per_unit": 3.1,
            "labor_hours_per_unit": 0.6,
            "downtime_fraction": 0.12,
            "lifespan_years": 25,
            # Civic lens params
            "annual_public_use_hours": 3120,  # 60 hr/wk × 52 wk — well above 2 hr/capita threshold
            "usage_rate_threshold": 2.0,      # hr/capita/yr (ECONOMIC-LENSES.md §4.3 default)
            "amortization_years": 30,         # ECONOMIC-LENSES.md §4.1 default
            # Coop lens params
            "per_member_annual_dues": 200,    # ECONOMIC-LENSES.md §3.2 default
            "per_member_labor_offset": 0,     # default $0
        },
    }
