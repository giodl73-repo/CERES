"""Tier A CLI entry point.

Usage:
    python -m tier_a.cli --catalog ../../catalog/smithing/ --results-dir ./results

See README.md for full usage documentation.
"""
import argparse
import datetime
import sys
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="tier_a",
        description="CERES Tier A scenario comparator — evaluates catalog entries across 9 cells.",
    )
    parser.add_argument(
        "--catalog",
        type=Path,
        required=True,
        help="Path to catalog trade directory (e.g. ../../catalog/smithing/)",
    )
    parser.add_argument(
        "--results-dir",
        type=Path,
        default=Path("./results"),
        help="Directory for output files (default: ./results)",
    )
    parser.add_argument(
        "--scales",
        type=Path,
        default=None,
        help="Optional path to a YAML file overriding default scale parameters",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Parse and validate entries without writing results",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print per-cell results to stdout",
    )
    return parser


def _render_summary(path: Path, summary: dict) -> None:
    """Render summary to markdown: matrix overview + per-entry verdicts + aggregate counts."""
    today = datetime.date.today().isoformat()
    entries = summary["entries"]
    skipped = summary.get("skipped", [])

    lines = ["# Tier A Simulation — Summary\n\n"]
    lines.append(f"**Run date:** {today}\n\n")
    lines.append(f"**Entries evaluated:** {len(entries)}\n\n")
    lines.append(f"**Entries skipped:** {len(skipped)}\n\n")

    # The 9 cells in order
    cells = [
        "village_market", "village_coop", "village_civic",
        "town_market", "town_coop", "town_civic",
        "small_city_market", "small_city_coop", "small_city_civic",
    ]

    # Aggregate verdict counts per cell
    lines.append("## Matrix Aggregate (verdict counts per cell)\n\n")
    lines.append("| Cell | Win | Marginal | Fail |\n|---|---|---|---|\n")
    for cell in cells:
        scale, lens_name = cell.rsplit("_", 1) if "_" in cell else (cell, "")
        # Handle small_city_* which has two underscores
        # Re-split using known scales
        counts = {"win": 0, "marginal": 0, "fail": 0}
        for eid, cell_results in entries.items():
            # cell_results is {(scale, lens): LensResult}
            # Determine (scale, lens) from the cell name
            scale_key, lens_key = _cell_name_to_tuple(cell)
            lr = cell_results.get((scale_key, lens_key))
            if lr is not None:
                v = lr.verdict
                if v in counts:
                    counts[v] += 1
        lines.append(f"| {cell} | {counts['win']} | {counts['marginal']} | {counts['fail']} |\n")

    lines.append("\n## Per-Entry Verdicts\n\n")
    lines.append(
        "| Entry | village_m | village_c | village_civ | town_m | town_c | town_civ | sc_m | sc_c | sc_civ |\n"
    )
    lines.append("|---|---|---|---|---|---|---|---|---|---|\n")
    for eid in sorted(entries.keys()):
        cell_results = entries[eid]
        verdicts = []
        for cell in cells:
            scale_key, lens_key = _cell_name_to_tuple(cell)
            lr = cell_results.get((scale_key, lens_key))
            v = lr.verdict[:4] if lr else "—"
            verdicts.append(v)
        lines.append(f"| {eid} | " + " | ".join(verdicts) + " |\n")

    if skipped:
        lines.append("\n## Skipped Entries\n\n")
        for s in skipped:
            lines.append(f"- `{s['path']}` — {s['reason']}\n")

    path.write_text("".join(lines), encoding="utf-8")


def _cell_name_to_tuple(cell: str) -> tuple[str, str]:
    """Convert cell name like 'small_city_market' to ('small_city', 'market')."""
    known_scales = ["small_city", "village", "town"]
    for scale in known_scales:
        if cell.startswith(scale + "_"):
            lens = cell[len(scale) + 1:]
            return (scale, lens)
    raise ValueError(f"Cannot parse cell name: {cell!r}")


def main(argv: list[str] | None = None) -> int:
    """CLI entry point. Returns exit code."""
    parser = build_parser()
    args = parser.parse_args(argv)

    # Import here so CLI arg errors surface before heavy imports
    from .runner import run_catalog  # noqa: PLC0415

    # Pass results_dir=None for dry-run (no writeback), otherwise pass results_dir
    results_dir_for_runner = None if args.dry_run else args.results_dir

    all_results = run_catalog(
        catalog_dir=args.catalog,
        results_dir=results_dir_for_runner,
    )

    # Build summary dict for SUMMARY.md rendering
    # We need to also collect skipped from runner; re-run accounting here
    # Since run_catalog only returns the successful entries dict, count skipped separately
    entries_dir = args.catalog / "entries"
    total_md = len(list(entries_dir.glob("*.md"))) if entries_dir.exists() else 0
    skipped_count = total_md - len(all_results)

    summary = {
        "entries": all_results,
        "skipped": [{"path": "unknown", "reason": "see logs"}] * skipped_count if skipped_count > 0 else [],
    }

    if args.verbose:
        for entry_id, cells in all_results.items():
            print(f"\n=== {entry_id} ===")
            for (scale, lens), result in cells.items():
                print(f"  {scale:12s} / {lens:8s}  {result.verdict:8s}  "
                      f"{result.metric_name}={result.primary_metric:.2f}")

    # Write SUMMARY.md
    args.results_dir.mkdir(parents=True, exist_ok=True)
    summary_path = args.results_dir / "SUMMARY.md"
    _render_summary(summary_path, summary)

    print(f"Evaluated {len(all_results)} entries; skipped {skipped_count}")
    print(f"Summary written to {summary_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
