# Craft Practitioner — reproducible reader delivery

> AI-simulated composite role review by the implementing agent. Not an independent
> human review, catalog validation or funding approval.

Artifact: [implementation plan](../plans/2026-11-05-wasm-self-service.md), round1.
Rubric focus: D3; secondary D6. No numeric grade.

## Overall

I support a reproducible tool that admits what breaks and how to recover; I do not treat an executable model as a shop-floor test.

## What works

Sections4–6 require full dependencies/notices, installed-tool prerequisites, outside-Git rebuild, genuine worker termination and usable fallback downloads. Section8 preserves original evidence and rollback.

## What does not yet hold

The initial owner-cache miss already illustrates why a lockfile is not an offline source kit. Consumables, maintenance, realistic interruptions and apprenticeship remain original catalog questions, not solved by packaging.

## The question I would push on

Can a second computer rebuild and recover the reader from the downloaded bytes, or does it still silently depend on this laptop's Cargo cache?
