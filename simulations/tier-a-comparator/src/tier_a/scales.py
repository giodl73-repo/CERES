"""Scale parameter loader. See corpus/program/SCALES.md for authoritative values."""
from pathlib import Path
import yaml


def load_scales(scales_path: str | Path | None = None) -> dict:
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
    raise NotImplementedError
