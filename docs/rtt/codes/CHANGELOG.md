# Changelog — `/docs/rtt/codes/`

> RTT/codes module — QR-compatible metadata layer: schema, validators, generators, style system, and domain examples.

All notable changes to files in `/docs/rtt/codes/` are documented in this file.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [1.1] — 2026-05-06

### Context

Full 14-file module audit triggered by directory migration from `/docs/rttcodes/` to `/docs/rtt/codes/`.
Audit confirmed **zero path breaks** — no file in the module references the old path.
Two infrastructure files received metadata refresh; twelve content files passed clean.

### Migration

- **Previous location:** `/docs/rttcodes/`
- **Current location:** `/docs/rtt/codes/`
- **Impact:** All internal relative paths preserved. No `$ref`, `$id`, or cross-file reference required updating. The canonical schema directory (`/docs/schemas/`) was not relocated.

### Changed — `RTT_codes_module.json` (Module Manifest)

- **`_meta`** — Added full module registry block:
  - `module`, `canonical_id`, `module_type`, `role`, `version`, `status`, `author`, `license`
  - `canonical_path`, `module_home` (now `/docs/rtt/codes/`), `module_url`
  - `repository`, `last_updated`, `migration_note`
- **`_session_context`** — Replaced old non-standard `session_context` with standardized `_session_context` block matching TriadicFrameworks conventions (9 fields).
- **`_version_history`** — Added array with v1.0 and v1.1 entries.
- **`cross_module_propagation`** — Added imports (RTT/1 operators, SARG structural grammar) and exports (schema, validators, generators, style system, examples).
- **`structural_grammar`** — Added dimensional, regime, coherence, drift, and regime sensitivity envelopes.
- **Version** — Bumped from 1.0 → 1.1.

### Changed — `schema/rttcode.schema.json` (Local QR Payload Schema)

- **`$id`** — Added: `https://www.triadicframeworks.org/rtt/codes/schema/rttcode.schema.json`.
- **`$comment`** — Added refresh stamp with migration note.
- **`_meta`** — Added full module registry block with `relationship_note` documenting the distinction between this schema (QR payload) and the canonical packet schema (`/docs/schemas/rttcode.v1.json`).
- **`_session_context`** — Added 9-field session context block.
- **`_version_history`** — Added array with v1.0 and v1.1 entries. Documents intentional inclusion of `"simulation"` in domain enum.
- **Version** — Bumped from 1.0 → 1.1.

### Not Changed — Example Payloads (8 files)

All eight domain example payloads passed the audit with no changes required:

| File | Domain | Artifact | Version | Status |
|------|--------|----------|---------|--------|
| `examples/docs.json` | docs | diagram | v1.0 | ✅ Pass |
| `examples/governance.json` | governance | docs | v1.3.1 | ✅ Pass |
| `examples/observer.json` | observer | module | v0.4.2 | ✅ Pass |
| `examples/other.json` | other | other | v0.0.1 | ✅ Pass |
| `examples/rtt.json` | rtt | paper | v2.1.0 | ✅ Pass |
| `examples/set.json` | set | simulation | v0.9.3 | ✅ Pass |
| `examples/simulation.json` | simulation | config | v0.2.0 | ✅ Pass |
| `examples/substrate.json` | substrate | README | v1.0.0 | ✅ Pass |

**Rationale for no metadata addition:** Example payloads are pure sample data — they validate against the schema but do not define infrastructure. Adding `_meta`/`_session_context` would conflate sample content with module metadata.

### Not Changed — Schema Examples (4 files)

All four schema-level example files passed the audit with no changes required:

| File | Purpose | Status |
|------|---------|--------|
| `schema/rttcode-payload-example.json` | Inline validation example (≡ `examples/substrate.json`) | ✅ Pass |
| `schema/examples/diagram.schema.json` | Minimal payload sample (required fields only) | ✅ Pass |
| `schema/examples/paper.schema.json` | Full payload sample (≡ `examples/rtt.json`) | ✅ Pass |
| `schema/examples/simulation.schema.json` | Full payload sample (≡ `examples/set.json`) | ✅ Pass |

### Noted — Content Duplicate Pairs

Three example files exist in both `examples/` and `schema/examples/`. This is **by design** — `examples/` holds domain-organized samples; `schema/examples/` holds validation-organized samples:

1. `examples/substrate.json` ≡ `schema/rttcode-payload-example.json`
2. `examples/rtt.json` ≡ `schema/examples/paper.schema.json`
3. `examples/set.json` ≡ `schema/examples/simulation.schema.json`

### Noted — Schema Relationship

The module contains **two distinct schemas** serving different levels of abstraction:

| Schema | Location | Purpose | Properties |
|--------|----------|---------|------------|
| QR Payload Schema | `schema/rttcode.schema.json` | QR-compatible metadata payload | domain, artifact_type, version, triad, url, checksum |
| RTTcode Packet Schema | `/docs/schemas/rttcode.v1.json` | Full RTTcode packet structure | rtt_version, tick, entities, environment, intent |

Both schemas now document this relationship in their `_meta` blocks.

### Noted — Domain Enum Discrepancy

The local QR payload schema includes `"simulation"` in its `domain` enum. The canonical packet schema's `_domains` list does not. This is **intentional** — `"simulation"` is a payload-level classification used by `examples/simulation.json` and does not map to a canonical RTTcode packet domain. Documented in `_version_history` of `schema/rttcode.schema.json`.

---

## [1.0] — 2025-01-01

### Added

- `RTT_codes_module.json` — Module manifest.
- `schema/rttcode.schema.json` — QR-compatible metadata payload schema.
- `schema/rttcode-payload-example.json` — Inline validation example.
- `schema/examples/diagram.schema.json` — Minimal payload example.
- `schema/examples/paper.schema.json` — Full payload example (paper).
- `schema/examples/simulation.schema.json` — Full payload example (simulation).
- `examples/docs.json` — Domain example: docs.
- `examples/governance.json` — Domain example: governance.
- `examples/observer.json` — Domain example: observer.
- `examples/other.json` — Domain example: other.
- `examples/rtt.json` — Domain example: rtt.
- `examples/set.json` — Domain example: set.
- `examples/simulation.json` — Domain example: simulation.
- `examples/substrate.json` — Domain example: substrate.

---

## File Inventory

| File | Current Version | Status |
|------|-----------------|--------|
| `RTT_codes_module.json` | 1.1 | refreshed |
| `schema/rttcode.schema.json` | 1.1 | refreshed |
| `schema/rttcode-payload-example.json` | 1.0 | pass |
| `schema/examples/diagram.schema.json` | 1.0 | pass |
| `schema/examples/paper.schema.json` | 1.0 | pass |
| `schema/examples/simulation.schema.json` | 1.0 | pass |
| `examples/docs.json` | 1.0 | pass |
| `examples/governance.json` | 1.0 | pass |
| `examples/observer.json` | 1.0 | pass |
| `examples/other.json` | 1.0 | pass |
| `examples/rtt.json` | 1.0 | pass |
| `examples/set.json` | 1.0 | pass |
| `examples/simulation.json` | 1.0 | pass |
| `examples/substrate.json` | 1.0 | pass |
| `CHANGELOG.md` | — | this file |

---

### Related Changelog

The canonical schema directory has its own changelog at `/docs/schemas/CHANGELOG.md`, covering the master packet schema (`rttcode.v1.json`) and its four sub-schemas (`tick.v1.json`, `entity.v1.json`, `environment.v1.json`, `intent.v1.json`).

---

*Maintained by: Nawder Loswin · TriadicFrameworks · MIT*

