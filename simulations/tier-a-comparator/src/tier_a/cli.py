"""Tier A CLI entry point.

Usage:
    python -m tier_a.cli --catalog ../../catalog/smithing/ --results-dir ./results

See README.md for full usage documentation.
"""
import argparse
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


def main(argv: list[str] | None = None) -> int:
    """CLI entry point. Returns exit code."""
    parser = build_parser()
    args = parser.parse_args(argv)

    # Import here so CLI arg errors surface before heavy imports
    from .runner import run_catalog  # noqa: PLC0415

    results = run_catalog(
        catalog_dir=args.catalog,
        results_dir=None if args.dry_run else args.results_dir,
    )

    if args.verbose:
        for entry_id, cells in results.items():
            print(f"\n=== {entry_id} ===")
            for (scale, lens), result in cells.items():
                print(f"  {scale:12s} / {lens:8s}  {result.verdict:8s}  "
                      f"{result.metric_name}={result.primary_metric:.2f}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
