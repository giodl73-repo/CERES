"""Catalog entry I/O: YAML frontmatter read/write for Tier A simulation.

See catalog/SCHEMA.md v1.1 and catalog/smithing/SCHEMA.md for field definitions.
"""
from pathlib import Path
import yaml


def read_entry(entry_path: str | Path) -> dict:
    """Parse YAML frontmatter from a catalog entry Markdown file.

    Returns a dict containing at minimum: id, trade, economics, sim_params.
    Raises ValueError if required fields are missing.
    """
    raise NotImplementedError


def write_results(entry_path: str | Path, results: dict) -> None:
    """Write the results block back into the catalog entry frontmatter.

    Preserves all existing frontmatter fields; only the `results` key is
    updated or created. The prose body of the Markdown file is unchanged.
    """
    raise NotImplementedError


def iter_entries(catalog_dir: str | Path) -> list[dict]:
    """Yield parsed entry dicts for all .md files under catalog_dir/entries/."""
    raise NotImplementedError
