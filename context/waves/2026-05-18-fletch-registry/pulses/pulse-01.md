# Pulse 01: Smithing and baking registry seed

## Goal

Publish the first CERES-owned FLETCH registry so downstream knowledge and game
repos can discover stable local-production theory, catalog schema, and example
trade entries.

## Change

- Added `.fletch\registries\ceres-smithing-baking-assets.json`.
- Registered the CERES theory document, catalog schema, and one baking and one
  smithing catalog entry as repo-owned local file assets.

## Validation

```powershell
cargo test
fletch registry validate --file .fletch\registries\ceres-smithing-baking-assets.json
```
