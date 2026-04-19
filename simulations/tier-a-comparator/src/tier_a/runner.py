"""Tier A matrix runner.

Evaluates every entry in a catalog directory against all 9 cells
(3 scales × 3 lenses) and returns a results dict.

See corpus/program/ECONOMIC-LENSES.md for lens definitions.
See corpus/program/SCALES.md for scale parameters.
"""
from pathlib import Path

from .lenses import market_lens, coop_lens, civic_lens, LensResult
from .scales import load_scales
from .io_catalog import iter_entries


SCALES = ["village", "town", "small_city"]
LENSES = {
    "market": market_lens,
    "coop": coop_lens,
    "civic": civic_lens,
}


def run_entry(entry: dict, scales: dict) -> dict:
    """Evaluate a single entry against all 9 cells.

    Returns a dict keyed by (scale, lens) tuples, each value a LensResult.
    """
    raise NotImplementedError


def run_catalog(
    catalog_dir: str | Path,
    results_dir: str | Path | None = None,
    scales: dict | None = None,
) -> dict:
    """Run the full Tier A matrix for every entry in catalog_dir.

    Returns a dict keyed by entry id, each value the 9-cell result dict
    from run_entry().

    If results_dir is provided, writes updated results blocks back to
    catalog entry files via io_catalog.write_results().
    """
    raise NotImplementedError
