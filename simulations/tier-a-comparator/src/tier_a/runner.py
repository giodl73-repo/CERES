"""Tier A matrix runner.

Evaluates every entry in a catalog directory against all 9 cells
(3 scales × 3 lenses) and returns a results dict.

See corpus/program/ECONOMIC-LENSES.md for lens definitions.
See corpus/program/SCALES.md for scale parameters.
"""
from pathlib import Path
from typing import Optional

from .lenses import market_lens, coop_lens, civic_lens, LensResult
from .scales import load_scales
from .io_catalog import read_entry, write_results, iter_entries


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
    results = {}
    for scale in SCALES:
        for lens_name, lens_fn in LENSES.items():
            result = lens_fn(entry, scale, scales)
            results[(scale, lens_name)] = result
    return results


def run_catalog(
    catalog_dir: str | Path,
    results_dir: str | Path | None = None,
    scales: dict | None = None,
) -> dict:
    """Run the full Tier A matrix for every entry in catalog_dir.

    Returns a dict keyed by entry id, each value the 9-cell result dict
    from run_entry() — i.e. {(scale, lens): LensResult}.

    If results_dir is provided, writes updated results blocks back to
    catalog entry files via io_catalog.write_results().
    Also writes results back to each entry file (in-place in catalog_dir/entries/)
    regardless of results_dir when results_dir is not None.
    """
    catalog_dir = Path(catalog_dir)
    scales = scales or load_scales()
    entries_dir = catalog_dir / "entries"

    all_results = {}
    skipped = []

    for entry_path in sorted(entries_dir.glob("*.md")):
        try:
            entry = read_entry(entry_path)

            # Validate minimal required fields
            if "sim_params" not in entry or "economics" not in entry:
                skipped.append({"path": str(entry_path), "reason": "missing sim_params or economics"})
                continue

            entry_id = entry.get("id")
            if not entry_id:
                skipped.append({"path": str(entry_path), "reason": "missing id field"})
                continue

            cell_results = run_entry(entry, scales)
            all_results[entry_id] = cell_results

            # Write results back to the catalog entry file (unless dry-run, indicated by results_dir=None)
            if results_dir is not None:
                # Convert tuple-keyed results to string-keyed for YAML serialization
                serializable = {}
                for (scale, lens_name), lr in cell_results.items():
                    cell_key = f"{scale}_{lens_name}"
                    serializable[cell_key] = {
                        "verdict": lr.verdict,
                        "primary_metric": lr.primary_metric,
                        "metric_name": lr.metric_name,
                        "notes": lr.notes,
                    }
                write_results(entry_path, serializable)

        except Exception as e:
            skipped.append({"path": str(entry_path), "reason": str(e)})

    return all_results
