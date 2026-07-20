# Changelog — `/docs/schemas/`

> Canonical RTTcode schema directory — master packet schema and sub-schemas.

All notable changes to files in `/docs/schemas/` are documented in this file.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [1.1] — 2026-05-06

### Context

Metadata and session context refresh across all five canonical schemas.
Triggered by the RTT/codes module migration from `/docs/rttcodes/` to `/docs/rtt/codes/`.
Schema directory (`/docs/schemas/`) was **not** relocated — all `$id` and `$ref` paths remain unchanged.

### Changed — `rttcode.v1.json` (Master Packet Schema)

- **`$comment`** — Added refresh stamp with migration note.
- **`description`** — Expanded to include "QR-compatible metadata identifiers" and domain scope.
- **`_meta`** — Added full module registry block:
  - `module`, `canonical_id`, `role`, `version`, `status`, `author`, `license`
  - `canonical_path`, `module_home` (now `/docs/rtt/codes/`), `module_url`, `module_json`
  - `repository`, `last_updated`, `migration_note`
- **`_session_context`** — Added 9-field session context block matching TriadicFrameworks conventions.
- **`_version_history`** — Added array with v1.0 and v1.1 entries.
- **`_domains`** — Added recognized domain values registry (rtt, set, substrate, observer, governance, docs, other).
- **`_related_schemas`** — Added registry of all four `$ref` targets with human-readable roles.
- **Property descriptions** — Added `description` fields alongside `$ref` for tick, entities, environment, intent.
- **Version** — Bumped from 1.0 → 1.1.

### Changed — `tick.v1.json`

- **`$comment`** — Added refresh stamp.
- **`description`** — Enriched with D369 R4.1 (monotonic time marker) parallel.
- **`_meta`** — Added full module registry block with `parent_schema: rttcode.v1.json`.
- **`_session_context`** — Added 4-field session context block.
- **`_version_history`** — Added array with v1.0 and v1.1 entries.
- **Property descriptions** — Enriched `index`, `timestamp`, `coherence` with structural context.
- **Version** — Bumped from 1.0 → 1.1.

### Changed — `entity.v1.json`

- **`$comment`** — Added refresh stamp.
- **`description`** — Enriched with D369 R5.1 (source identity) parallel.
- **`_meta`** — Added full module registry block with `parent_schema: rttcode.v1.json`.
- **`_session_context`** — Added 4-field session context block.
- **`_version_history`** — Added array with v1.0 and v1.1 entries.
- **Property descriptions** — Enriched `id`, `state.value`, `resonance.amplitude`, `resonance.phase`.
- **Version** — Bumped from 1.0 → 1.1.

### Changed — `environment.v1.json`

- **`$comment`** — Added refresh stamp.
- **`description`** — Enriched with structural boundary context parallel.
- **`_meta`** — Added full module registry block with `parent_schema: rttcode.v1.json`.
- **`_session_context`** — Added 4-field session context block.
- **`_version_history`** — Added array with v1.0 and v1.1 entries.
- **Property descriptions** — Enriched `boundary.min/max`, `ambient.temperature/noise`, `drift.max_drift/accumulation_rate`.
- **Version** — Bumped from 1.0 → 1.1.

### Changed — `intent.v1.json`

- **`$comment`** — Added refresh stamp.
- **`description`** — Enriched with D369 NC-5 (does not define control logic) parallel.
- **`_meta`** — Added full module registry block with `parent_schema: rttcode.v1.json`.
- **`_session_context`** — Added 4-field session context block.
- **`_version_history`** — Added array with v1.0 and v1.1 entries.
- **Property descriptions** — Enriched `target`, `direction`, `magnitude`.
- **Version** — Bumped from 1.0 → 1.1.

### Not Changed

- **All `$id` URLs** — Preserved exactly (no path migration affected this directory).
- **All `$ref` paths** — Preserved exactly (relative to `/docs/schemas/`).
- **All property schemas** — Zero changes to types, enums, required fields, or validation logic.
- **Full backward compatibility** — Any payload valid under v1.0 is valid under v1.1.

---

## [1.0] — 2025-01-01

### Added

- `rttcode.v1.json` — Master RTTcode packet schema (tick + entities + environment + intent).
- `tick.v1.json` — Monotonic tick sub-schema.
- `entity.v1.json` — Entity participation sub-schema.
- `environment.v1.json` — Environment context sub-schema.
- `intent.v1.json` — Intent classification sub-schema.

---

## File Inventory

| File                 | Current Version | Status       |
|----------------------|-----------------|--------------|
| `rttcode.v1.json`    | 1.1             | canon-stable |
| `tick.v1.json`       | 1.1             | canon-stable |
| `entity.v1.json`     | 1.1             | canon-stable |
| `environment.v1.json`| 1.1             | canon-stable |
| `intent.v1.json`     | 1.1             | canon-stable |
| `CHANGELOG.md`       | —               | this file    |

---

*Maintained by: Nawder Loswin · TriadicFrameworks · Apache 2.0 / MIT*

