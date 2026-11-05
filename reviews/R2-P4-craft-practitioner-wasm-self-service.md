# Round2 P4: source layout amendment

> AI-simulated composite review by the implementing agent; no independent human
> panel, equipment/economic validation, funding approval or catalog promotion.

Artifact: `plans/2026-11-05-wasm-self-service.md`, especially section9.
Role: `.roles/panel/P-4-craft-practitioner.md`. Rubric focus: D3; secondaryD6; no score assigned.

## Overall

I support the plan only with an actual restored-source rebuild and deliberate breakage tests. A checksum list alone cannot repair a failed installation.

## What works

Section9 requires complete tree/mode verification before writes, protected destinations and a valid outside-Git restoration. Sections4/8 retain installed tool/linker prerequisites and the reused compiled target.

## What doesn't

Windows export conversion and the first CRLF lock identity already broke this path; the new exporter must use raw Git objects. The receiver must preserve original executable modes and reject the whole unsafe archive before making files.

## The question I'd push on

Can a reader follow the shipped instructions with a new input tree/Cargo home and get the original native and WASM behavior without this laptop’s dependency cache?
