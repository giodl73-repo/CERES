# Round2 P6: source layout amendment

> AI-simulated composite review by the implementing agent; no independent human
> panel, equipment/economic validation, funding approval or catalog promotion.

Artifact: `plans/2026-11-05-wasm-self-service.md`, especially section9.
Role: `.roles/panel/P-6-skeptical-funder.md`. Rubric focus: D6; secondaryD5; no score assigned.

## Overall

The amendment survives the immediate size objection only if the whole kit is optional, bounded, independently verifiable and actually rebuilt. Delivery remains open.

## What works

Section9 names the6,853,502-byte measured source ZIP and a concrete limit instead of silently raising the original runtime ceiling. Sections6–8 separate local, hosted, artifact and default/live gates.

## What doesn't

The strongest remaining objection is circular evidence: a manifest could certify its own omissions. Require complete Git-tree reconstruction against the exact commit object, a separately trusted manifest SHA, corruption controls and actual receiver rebuilds. No author authentication or byte-identical-module promise follows.

## The question I'd push on

What independent artifact identity and full-tree evidence prevent a green build from distributing a missing, altered or unbuildable source kit?
