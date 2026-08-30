fn assert_contains(source_name: &str, source: &str, needle: &str) {
    assert!(
        source.contains(needle),
        "{source_name} should contain policy text: {needle}"
    );
}

#[test]
fn pitfall_policy_keeps_catalog_numbers_out_of_procurement_use() {
    // CERES-PF-02: CERES numbers are research-paper estimates, not supplier
    // quotes, procurement plans, or due-diligence-grade financial models.
    let readme = include_str!("../README.md");
    let methodology = include_str!("../docs/METHODOLOGY.md");
    let style_guide = include_str!("../docs/STYLE-GUIDE.md");
    let scope_keeper = include_str!("../.roles/editorial/E-2-scope-keeper.md");
    let numeracy_checker = include_str!("../.roles/editorial/E-3-numeracy-checker.md");

    assert_contains(
        "README.md",
        readme,
        "Conceptual designs, not procurement plans",
    );
    assert_contains(
        "docs/METHODOLOGY.md",
        methodology,
        "CERES is **not** a due-diligence exercise",
    );
    assert_contains(
        "docs/METHODOLOGY.md",
        methodology,
        "not good numbers for booking",
    );
    assert_contains(
        "docs/STYLE-GUIDE.md",
        style_guide,
        "research-paper estimates, not supplier BOMs",
    );
    assert_contains(
        ".roles/editorial/E-2-scope-keeper.md",
        scope_keeper,
        "Non-goal violation",
    );
    assert_contains(
        ".roles/editorial/E-3-numeracy-checker.md",
        numeracy_checker,
        "Order-of-magnitude wrong",
    );
}

#[test]
fn pitfall_policy_keeps_citation_placeholders_out_of_validated_evidence() {
    // CERES-PF-03: schema completeness and simulation runs do not validate
    // claims while citation placeholders or source-quality gaps remain.
    let tracker = include_str!("../TRACKER.md");
    let methodology = include_str!("../docs/METHODOLOGY.md");
    let style_guide = include_str!("../docs/STYLE-GUIDE.md");
    let principles = include_str!("../corpus/canon/PRINCIPLES.md");
    let citation_auditor = include_str!("../.roles/editorial/E-1-citation-auditor.md");
    let catalog_audit = include_str!("../reviews/CATALOG-AUDIT-plan-c.md");

    assert_contains(
        "TRACKER.md",
        tracker,
        "450 `[CITATION-NEEDED]` placeholders",
    );
    assert_contains(
        "docs/METHODOLOGY.md",
        methodology,
        "Uncited estimate = P1 editorial finding",
    );
    assert_contains(
        "docs/STYLE-GUIDE.md",
        style_guide,
        "Every economic number has a source",
    );
    assert_contains(
        "corpus/canon/PRINCIPLES.md",
        principles,
        "A confident number with no source is a confident guess",
    );
    assert_contains(
        ".roles/editorial/E-1-citation-auditor.md",
        citation_auditor,
        "No promotion to `validated`",
    );
    assert_contains(
        "reviews/CATALOG-AUDIT-plan-c.md",
        catalog_audit,
        "CITATION-NEEDED",
    );
}

#[test]
fn pitfall_policy_keeps_downstream_reuse_from_importing_ceres_policy() {
    // CERES-PF-04: downstream products can consume bounded evidence or neutral
    // foundations, but not CERES thresholds as a generic economy/crafting API.
    let readme = include_str!("../README.md");
    let scenarium_adoption = include_str!("../docs/scenarium-adoption.md");
    let capability_expansion = include_str!("../docs/capability-expansion.md");
    let principles = include_str!("../corpus/canon/PRINCIPLES.md");

    assert_contains(
        "README.md",
        readme,
        "CERES is not a game engine, crafting engine, or faction engine",
    );
    assert_contains(
        "README.md",
        readme,
        "no downstream manifest or consumer-owned",
    );
    assert_contains(
        "docs/scenarium-adoption.md",
        scenarium_adoption,
        "catalog and economic policy remain CERES-owned",
    );
    assert_contains(
        "docs/capability-expansion.md",
        capability_expansion,
        "route geography in PORTO",
    );
    assert_contains(
        "corpus/canon/PRINCIPLES.md",
        principles,
        "schema is the contract between the catalog author and the simulation layer",
    );
}
