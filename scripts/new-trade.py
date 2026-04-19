#!/usr/bin/env python3
"""
scripts/new-trade.py — CERES trade scaffolding generator

Usage:
    python scripts/new-trade.py baking --letter F
    python scripts/new-trade.py weaving --letter H
    python scripts/new-trade.py baking --dry-run

Generates stub files for a new CERES trade and adds rows to plans/README.md.
"""

import argparse
import re
import sys
from datetime import date
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent
TODAY = date.today().isoformat()
SPEC_PATH = "specs/2026-04-18-ceres-design.md"

DEFAULT_CULTURES = [
    "medieval-northern-europe",
    "song-china",
    "tokugawa-japan",
    "american-frontier",
]

# Map from trade slug to a human-readable equipment noun used in per-chapter
# outline headings (falls back to "{Trade} Equipment" if not listed).
TRADE_EQUIPMENT_NOUNS: dict[str, str] = {
    "baking": "Oven/Hearth",
    "weaving": "Loom",
    "smithing": "Forge",
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def title_case(slug: str) -> str:
    """Convert a kebab-case slug to Title Case."""
    return " ".join(w.capitalize() for w in slug.replace("-", " ").split())


def next_letter(letter: str) -> str:
    """Return the next uppercase letter (F -> G, H -> I, etc.)."""
    return chr(ord(letter.upper()) + 1)


def equipment_noun(trade: str) -> str:
    return TRADE_EQUIPMENT_NOUNS.get(trade.lower(), f"{title_case(trade)} Equipment")


# ---------------------------------------------------------------------------
# Stub content builders
# ---------------------------------------------------------------------------


def research_trade_stub(trade: str, doc_type: str, extra_fm: str = "") -> str:
    """Generic research/trades/{trade}/*.md stub."""
    lines = [
        "---",
        f"trade: {trade}",
        f"doc_type: {doc_type}",
    ]
    if extra_fm:
        lines.append(extra_fm.rstrip())
    lines += [
        'status: stub',
        'version: "1.0"',
        "---",
        "",
        f"## Stub",
        "",
        f"This file is a scaffold placeholder for `research/trades/{trade}/{doc_type.upper().replace('-', '-')}.md`.",
        "Replace with researched content when Plan work begins.",
        "",
    ]
    return "\n".join(lines)


def requirements_stub(trade: str) -> str:
    return (
        "---\n"
        f"trade: {trade}\n"
        "doc_type: functional-requirements\n"
        "status: stub\n"
        'version: "1.0"\n'
        "---\n\n"
        "## Stub\n\n"
        f"Cross-cultural functional requirements for `{trade}`. "
        "Replace with researched content.\n"
    )


def historical_forms_stub(trade: str) -> str:
    return (
        "---\n"
        f"trade: {trade}\n"
        "doc_type: historical-forms\n"
        "status: stub\n"
        'version: "1.0"\n'
        "---\n\n"
        "## Stub\n\n"
        f"Comparative historical forms for `{trade}`. "
        "Replace with researched content.\n"
    )


def decline_verdict_stub(trade: str) -> str:
    return (
        "---\n"
        f"trade: {trade}\n"
        "doc_type: decline-verdict\n"
        "verdict: TBD\n"
        "status: stub\n"
        'version: "1.0"\n'
        "---\n\n"
        "## Stub\n\n"
        f"Decline-or-restructuring verdict for `{trade}`. "
        "Replace with researched content.\n"
    )


def sources_stub(trade: str) -> str:
    return (
        "---\n"
        f"trade: {trade}\n"
        "doc_type: bibliography\n"
        "status: stub\n"
        'version: "1.0"\n'
        "---\n\n"
        "## Stub\n\n"
        f"Consolidated bibliography for `{trade}`. "
        "Replace with researched content.\n"
    )


def culture_stub(trade: str, culture: str) -> str:
    return (
        "---\n"
        f"culture: {culture}\n"
        f"trade: {trade}\n"
        "status: stub\n"
        'version: "1.0"\n'
        "review_status: {panel: pending, editorial: pending}\n"
        "---\n\n"
        "## Stub\n\n"
        f"Cultural chapter: `{trade}` in `{culture}`. "
        "Replace with researched content.\n"
    )


def catalog_readme_stub(trade: str) -> str:
    return (
        "---\n"
        f"trade: {trade}\n"
        "doc_type: catalog-overview\n"
        'version: "1.0"\n'
        "status: stub\n"
        "---\n\n"
        f"# {title_case(trade)} Catalog — Overview\n\n"
        "## Stub\n\n"
        f"Catalog README for `{trade}`. Replace with authored content.\n"
    )


def catalog_schema_stub(trade: str) -> str:
    return (
        "---\n"
        f"trade: {trade}\n"
        "doc_type: schema-extension\n"
        "extends: catalog/SCHEMA.md\n"
        'version: "1.0"\n'
        "status: stub\n"
        "---\n\n"
        f"Base schema: catalog/SCHEMA.md\n\n"
        f"# {title_case(trade)} Schema Extension\n\n"
        "## Stub\n\n"
        f"Trade-specific schema extension for `{trade}`. Replace with authored content.\n"
    )


def playbook_stub(trade: str, scale: str) -> str:
    return (
        "---\n"
        f"trade: {trade}\n"
        f"scale: {scale}\n"
        "doc_type: playbook\n"
        'version: "1.0"\n'
        "status: stub\n"
        "---\n\n"
        f"# {title_case(trade)} Playbook — {title_case(scale)} Scale\n\n"
        "## Stub\n\n"
        f"Playbook for `{trade}` at `{scale}` scale. Replace with authored content.\n"
    )


# ---------------------------------------------------------------------------
# Plan file content builders
# ---------------------------------------------------------------------------


def research_plan(trade: str, letter: str) -> str:
    """Build content for the research (Phase 1) plan."""
    upper = letter.upper()
    cat_letter = next_letter(letter)
    trade_title = title_case(trade)
    equip = equipment_noun(trade)

    return (
        "---\n"
        f"id: plan-{letter.lower()}-research-{trade}\n"
        f"name: Research Corpus — {trade_title}\n"
        f"description: Historical functional-requirements research for {trade} across 4 anchor cultures\n"
        "status: draft\n"
        'version: "1.0"\n'
        f"created: {TODAY}\n"
        "phase: 1\n"
        "subsystem: research-corpus\n"
        f"trade: {trade}\n"
        "depends_on: [plan-a-scaffolding]\n"
        f"blocks: [plan-{cat_letter.lower()}-catalog-{trade}]\n"
        "estimated_effort: 2-3 weeks focused\n"
        "primary_artifact_type: research\n"
        "success_signal: >\n"
        f"  4 cultural chapters for {trade} (medieval N. Europe, Song China, Tokugawa\n"
        "  Japan, American frontier) plus REQUIREMENTS, HISTORICAL-FORMS,\n"
        "  DECLINE-VERDICT, SOURCES — anti-romantic, P-5-Historian-grade citations.\n"
        f"spec: {SPEC_PATH}\n"
        "---\n\n"
        f"# Plan {upper}: Research Corpus — {trade_title}\n\n"
        f"> **Pattern inherited from Plan B (smithing).** Same structure: 4 cultural chapters + synthesis docs.\n"
        f"> Follow Plan B (`plans/2026-04-19-plan-b-research-smithing.md`) as the template.\n"
        f"> Trade-specific guidance: see the per-task notes below.\n\n"
        f"**Goal:** Produce the historical research foundation for {trade}.\n"
        "**Citation policy:** `[CITATION-NEEDED: <claim>]` over fabrication.\n"
        "**Anchor cultures (4 of 6):** medieval-northern-europe, song-china, tokugawa-japan, american-frontier\n\n"
        "## Task Index\n\n"
        "| # | Task | Creates |\n"
        "|---|---|---|\n"
        f"| 1 | Medieval Northern Europe {trade} | `research/cultures/medieval-northern-europe/{trade}.md` |\n"
        f"| 2 | Song-era China {trade} | `research/cultures/song-china/{trade}.md` |\n"
        f"| 3 | Tokugawa Japan {trade} | `research/cultures/tokugawa-japan/{trade}.md` |\n"
        f"| 4 | American frontier {trade} | `research/cultures/american-frontier/{trade}.md` |\n"
        f"| 5 | Cross-cultural functional requirements | `research/trades/{trade}/REQUIREMENTS.md` |\n"
        f"| 6 | Comparative historical forms | `research/trades/{trade}/HISTORICAL-FORMS.md` |\n"
        f"| 7 | Decline-or-restructuring verdict | `research/trades/{trade}/DECLINE-VERDICT.md` |\n"
        f"| 8 | Consolidated bibliography | `research/trades/{trade}/SOURCES.md` |\n"
        "| 9 | Closeout | TRACKER + plans/README + frontmatter |\n\n"
        "## Per-Chapter Outline\n\n"
        "Same 10-section outline as Plan B. Required sections:\n"
        f"Frontmatter / Period and Geography / The {trade_title}-Practitioner's Place /\n"
        f"The {equip} / Products / Labor Regime / Supply Chain /\n"
        "Decline or Restructuring / Functional Requirements Learned / Sources\n\n"
        "Anti-romanticism rules: `docs/STYLE-GUIDE.md §4`.\n"
        "Citation policy: `[CITATION-NEEDED: <claim>]` over fabrication.\n"
    )


def catalog_plan(trade: str, letter: str) -> str:
    """Build content for the catalog (Phase 2) plan."""
    upper = letter.upper()
    res_letter = chr(ord(letter.upper()) - 1)
    trade_title = title_case(trade)

    return (
        "---\n"
        f"id: plan-{letter.lower()}-catalog-{trade}\n"
        f"name: Catalog — {trade_title}\n"
        f"description: 15 {trade} catalog entries per DECLINE-VERDICT guidance\n"
        "status: draft\n"
        'version: "1.0"\n'
        f"created: {TODAY}\n"
        "phase: 2\n"
        "subsystem: catalog\n"
        f"trade: {trade}\n"
        f"depends_on: [plan-a-scaffolding, plan-{res_letter.lower()}-research-{trade}]\n"
        "blocks: []\n"
        "estimated_effort: 3-5 weeks focused\n"
        "primary_artifact_type: catalog\n"
        "success_signal: >\n"
        f"  15 {trade} catalog entries at `catalog/{trade}/entries/*.md`, each\n"
        "  schema-compliant; every entry cites sources or carries bracketed\n"
        "  placeholders. Cross-entry audit confirms 9-cell matrix coverage.\n"
        f"spec: {SPEC_PATH}\n"
        "---\n\n"
        f"# Plan {upper}: Catalog — {trade_title}\n\n"
        f"> **Pattern inherited from Plan C (smithing).** Same structure: manifest + schema extension + 15 entries.\n"
        f"> Follow Plan C (`plans/2026-04-19-plan-c-catalog-smithing.md`) as the template.\n"
        f"> **Simulation already scripted:** after entries are authored, run:\n"
        f"> `python -m simulations.tier_a.cli --catalog catalog/{trade}/` (or equivalent) to produce 135 cells.\n\n"
        f"**Goal:** 15 {trade} catalog entries per DECLINE-VERDICT guidance for this trade.\n\n"
        "## Task Index\n"
        "| # | Task | Creates |\n"
        "|---|---|---|\n"
        f"| 1 | Catalog manifest / README | `catalog/{trade}/README.md` |\n"
        f"| 2 | {trade_title}-specific schema extension | `catalog/{trade}/SCHEMA.md` |\n"
        f"| 3-17 | Entries 001-015 | `catalog/{trade}/entries/*.md` |\n"
        f"| 18 | Cross-entry audit | `reviews/CATALOG-AUDIT-plan-{letter.lower()}.md` |\n"
        "| 19 | Closeout | TRACKER + plans/README + frontmatter |\n"
    )


# ---------------------------------------------------------------------------
# plans/README.md update
# ---------------------------------------------------------------------------

# Regex to find the last row in the plan index table so we can append after it.
# The table rows start with "| plan-" and the section ends with a blank line then "---"
_TABLE_ROW_RE = re.compile(r"^(\| plan-[^\n]+\|)\s*$", re.MULTILINE)


def _build_readme_rows(trade: str, res_letter: str, cat_letter: str) -> str:
    """Return two markdown table rows (research + catalog) to append."""
    trade_title = title_case(trade)
    res_id = f"plan-{res_letter.lower()}-research-{trade}"
    cat_id = f"plan-{cat_letter.lower()}-catalog-{trade}"
    res_signal = (
        f"4 cultural chapters for {trade} + REQUIREMENTS, HISTORICAL-FORMS, "
        "DECLINE-VERDICT, SOURCES — anti-romantic, P-5-Historian-grade citations."
    )
    cat_signal = (
        f"15 {trade} catalog entries schema-compliant; 9-cell matrix coverage confirmed."
    )
    row_res = (
        f"| {res_id} | Research Corpus — {trade_title} | draft | 1 | {trade} "
        f"| plan-a-scaffolding | {res_signal} |"
    )
    row_cat = (
        f"| {cat_id} | Catalog — {trade_title} | draft | 2 | {trade} "
        f"| plan-a-scaffolding, {res_id} | {cat_signal} |"
    )
    return row_res + "\n" + row_cat


def update_plans_readme(trade: str, res_letter: str, cat_letter: str, dry_run: bool) -> bool:
    """
    Append two rows to the plan index table in plans/README.md.
    Returns True if changed (or would change), False if rows already present.
    """
    readme_path = REPO_ROOT / "plans" / "README.md"
    if not readme_path.exists():
        print(f"  WARNING: {readme_path} not found; skipping README update.", file=sys.stderr)
        return False

    content = readme_path.read_text(encoding="utf-8")
    res_id = f"plan-{res_letter.lower()}-research-{trade}"
    cat_id = f"plan-{cat_letter.lower()}-catalog-{trade}"

    if res_id in content and cat_id in content:
        print(f"  SKIP plans/README.md — rows for {res_id} and {cat_id} already present.")
        return False

    new_rows = _build_readme_rows(trade, res_letter, cat_letter)

    # Find the last table row in the index table (the "## 3." section) and append after it.
    # Strategy: find all matches, replace text after the last match.
    matches = list(_TABLE_ROW_RE.finditer(content))
    if not matches:
        print("  WARNING: Could not find plan index table rows in plans/README.md; skipping.", file=sys.stderr)
        return False

    last_match = matches[-1]
    insert_pos = last_match.end()
    new_content = content[:insert_pos] + "\n" + new_rows + content[insert_pos:]

    if dry_run:
        print(f"  DRY-RUN: would append to plans/README.md:\n    {new_rows.replace(chr(10), chr(10) + '    ')}")
        return True

    readme_path.write_text(new_content, encoding="utf-8")
    print(f"  UPDATED plans/README.md (+2 rows for {trade})")
    return True


# ---------------------------------------------------------------------------
# File registry: (repo-relative path, content)
# ---------------------------------------------------------------------------


def build_file_list(
    trade: str,
    res_letter: str,
    cultures: list[str],
) -> list[tuple[str, str]]:
    """Return list of (repo-relative-path, content) tuples."""
    cat_letter = next_letter(res_letter)
    files: list[tuple[str, str]] = []

    # 1. research/trades/{trade}/
    files.append((f"research/trades/{trade}/REQUIREMENTS.md", requirements_stub(trade)))
    files.append((f"research/trades/{trade}/HISTORICAL-FORMS.md", historical_forms_stub(trade)))
    files.append((f"research/trades/{trade}/DECLINE-VERDICT.md", decline_verdict_stub(trade)))
    files.append((f"research/trades/{trade}/SOURCES.md", sources_stub(trade)))

    # 2. research/cultures/{culture}/{trade}.md × N
    for culture in cultures:
        files.append((f"research/cultures/{culture}/{trade}.md", culture_stub(trade, culture)))

    # 3. catalog/{trade}/
    files.append((f"catalog/{trade}/README.md", catalog_readme_stub(trade)))
    files.append((f"catalog/{trade}/SCHEMA.md", catalog_schema_stub(trade)))
    files.append((f"catalog/{trade}/entries/.gitkeep", ""))

    # 4. playbook/{trade}/
    for scale in ("village", "town", "small-city"):
        files.append((f"playbook/{trade}/{scale}.md", playbook_stub(trade, scale)))

    # 5. Plan files
    res_plan_filename = f"plans/{TODAY}-plan-{res_letter.lower()}-research-{trade}.md"
    cat_plan_filename = f"plans/{TODAY}-plan-{cat_letter.lower()}-catalog-{trade}.md"
    files.append((res_plan_filename, research_plan(trade, res_letter)))
    files.append((cat_plan_filename, catalog_plan(trade, cat_letter)))

    return files


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="CERES trade scaffolding generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("trade", help="Trade slug (e.g. baking, weaving)")
    parser.add_argument(
        "--letter",
        default=None,
        help="Letter for the research plan (catalog = letter+1). E.g. F for baking, H for weaving.",
    )
    parser.add_argument(
        "--cultures",
        default=",".join(DEFAULT_CULTURES),
        help="Comma-separated culture slugs (default: 4 anchor cultures)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be created without writing any files",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    trade = args.trade.lower().strip()
    dry_run: bool = args.dry_run
    cultures = [c.strip() for c in args.cultures.split(",") if c.strip()]

    # Determine letter
    if args.letter:
        res_letter = args.letter.upper()
    else:
        # Default: ask user explicitly — but allow dry-run without letter
        if dry_run:
            res_letter = "X"  # placeholder for dry-run
            print(f"  NOTE: --letter not provided; using '{res_letter}' as placeholder for dry-run.")
        else:
            print("ERROR: --letter is required when not using --dry-run.", file=sys.stderr)
            sys.exit(1)

    cat_letter = next_letter(res_letter)

    print(f"\n{'DRY RUN — ' if dry_run else ''}Scaffolding trade: {trade!r}")
    print(f"  Research plan letter : {res_letter}")
    print(f"  Catalog plan letter  : {cat_letter}")
    print(f"  Cultures             : {cultures}")
    print(f"  Repo root            : {REPO_ROOT}")
    print()

    file_list = build_file_list(trade, res_letter, cultures)

    created: list[str] = []
    skipped: list[str] = []

    for rel_path, content in file_list:
        abs_path = REPO_ROOT / rel_path
        if dry_run:
            print(f"  WOULD CREATE: {rel_path}")
            created.append(rel_path)
            continue

        if abs_path.exists():
            print(f"  SKIP (exists): {rel_path}")
            skipped.append(rel_path)
            continue

        abs_path.parent.mkdir(parents=True, exist_ok=True)
        abs_path.write_text(content, encoding="utf-8")
        print(f"  CREATED: {rel_path}")
        created.append(rel_path)

    # Update plans/README.md
    print()
    update_plans_readme(trade, res_letter, cat_letter, dry_run)

    # Summary
    print()
    print("=" * 60)
    print(f"{'DRY RUN ' if dry_run else ''}Summary for trade={trade!r}")
    print(f"  Files {'that would be ' if dry_run else ''}created : {len(created)}")
    if skipped:
        print(f"  Files skipped (exist) : {len(skipped)}")
    print("=" * 60)


if __name__ == "__main__":
    main()
