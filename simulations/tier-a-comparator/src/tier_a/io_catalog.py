"""Catalog entry I/O: YAML frontmatter read/write for Tier A simulation.

See catalog/SCHEMA.md v1.1 and catalog/smithing/SCHEMA.md for field definitions.
"""
from pathlib import Path
import yaml


def _split_frontmatter(text: str):
    """Split a markdown file into (frontmatter_str, body_str).

    Expects the file to start with '---\n', end the frontmatter with a second
    '---' line, and have optional prose body after that.

    Returns (frontmatter_str, body_str) where frontmatter_str is the raw YAML
    between the delimiters (without the '---' lines themselves).
    Raises ValueError if the file does not start with '---'.
    """
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].rstrip("\r\n") != "---":
        raise ValueError("File does not begin with YAML frontmatter delimiter '---'")

    # Find closing '---'
    close_idx = None
    for i, line in enumerate(lines[1:], start=1):
        if line.rstrip("\r\n") == "---":
            close_idx = i
            break
    if close_idx is None:
        raise ValueError("Frontmatter closing '---' not found")

    frontmatter_lines = lines[1:close_idx]
    body_lines = lines[close_idx + 1 :]

    frontmatter_str = "".join(frontmatter_lines)
    body_str = "".join(body_lines)
    return frontmatter_str, body_str


def read_entry(entry_path) -> dict:
    """Parse YAML frontmatter from a catalog entry Markdown file.

    Returns a dict containing at minimum: id, trade, economics, sim_params.
    Raises ValueError if required fields are missing.
    """
    path = Path(entry_path)
    text = path.read_text(encoding="utf-8")
    frontmatter_str, _body = _split_frontmatter(text)
    data = yaml.safe_load(frontmatter_str)
    if data is None:
        data = {}
    return data


def write_results(entry_path, results: dict) -> None:
    """Write the results block back into the catalog entry frontmatter.

    Uses a targeted edit strategy: locate or create the `results:` key in the
    raw frontmatter text and replace its YAML block, leaving everything else
    completely unchanged.  The prose body of the Markdown file is untouched.
    """
    path = Path(entry_path)
    text = path.read_text(encoding="utf-8")
    frontmatter_str, body_str = _split_frontmatter(text)

    # Serialize the new results block
    results_yaml = yaml.safe_dump(
        {"results": results},
        sort_keys=False,
        default_flow_style=False,
        allow_unicode=True,
    )
    # results_yaml starts with "results:\n  ..." — strip the trailing newline
    results_block = results_yaml.rstrip("\n")

    # Check whether a results: key already exists in the frontmatter
    lines = frontmatter_str.splitlines(keepends=True)
    results_start = None
    results_end = None
    for i, line in enumerate(lines):
        if line.startswith("results:"):
            results_start = i
            # Find the end of this block: next top-level key or end of frontmatter
            j = i + 1
            while j < len(lines):
                stripped = lines[j]
                # Top-level key: line starts with a non-space/non-tab character
                # that is not a comment and not blank
                first_char = stripped[0] if stripped.strip() else " "
                if first_char not in (" ", "\t", "#", "\n", "\r") and stripped.strip():
                    break
                j += 1
            results_end = j
            break

    if results_start is not None:
        # Replace the existing results block
        new_lines = (
            lines[:results_start]
            + [results_block + "\n"]
            + lines[results_end:]
        )
    else:
        # Append results block at end of frontmatter
        new_lines = lines + [results_block + "\n"]

    new_frontmatter = "".join(new_lines)
    new_text = "---\n" + new_frontmatter + "---" + body_str
    path.write_text(new_text, encoding="utf-8")


def iter_entries(catalog_dir) -> list[dict]:
    """Yield parsed entry dicts for all .md files under catalog_dir/entries/."""
    entries_dir = Path(catalog_dir) / "entries"
    result = []
    for md_file in sorted(entries_dir.glob("*.md")):
        result.append(read_entry(md_file))
    return result
