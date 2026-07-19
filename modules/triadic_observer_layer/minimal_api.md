# Minimal Observer API

The Triadic Observer Layer is intentionally lightweight. Its API is designed to be **easy to emit**, **hard to misuse**, and **domain‑agnostic by default**. Existing systems should be able to participate without architectural change or political risk.

The observer consumes observations. It does not request them.

---

## Design Goals

- Minimal surface area.
- Explicit phase declaration.
- First‑class time and source.
- No implied authority.
- Safe under partial adoption.

The API favors **clarity over completeness**.

---

## Core Observation Schema

Every observation submitted to the observer must conform to the following structure:

```json
{
  "domain": "string",
  "entity_id": "string",
  "phase": "string",
  "metric": "string",
  "value": "number|string",
  "unit": "string",
  "source": "string",
  "timestamp": "ISO-8601",
  "confidence": "string",
  "notes": "string (optional)"
}
```

---

## Field Semantics

- **domain** — The operational context (e.g., elections, supply_chain, science).
- **entity_id** — The smallest independently observable unit.
- **phase** — Declared lifecycle stage of the observation.
- **metric** — What is being measured.
- **value** — The reported measurement.
- **unit** — Measurement unit or classification.
- **source** — System or process emitting the observation.
- **timestamp** — When this observation existed in its reported form.
- **confidence** — Declarative certainty level (e.g., provisional, final).
- **notes** — Optional human context; never required.

No field implies correctness. All fields imply context.

---

## Phase Declaration Rules

- Phase must be explicit.
- Phase must not be inferred by the observer.
- Multiple phases may exist simultaneously for the same entity and metric.
- Phase transitions are observed, not enforced.

Phase disagreement is preserved as signal.

---

## Time Semantics

The timestamp represents **existence**, not ingestion.

- Late submissions are valid.
- Out‑of‑order events are valid.
- Corrections are new observations, not overwrites.

Temporal inconsistency is informational.

---

## Source Semantics

Sources are identifiers, not authorities.

- Multiple sources may emit the same metric.
- Conflicting sources are expected.
- Source trust is external to the observer.

The observer never ranks sources.

---

## Confidence Field

Confidence is declarative, not probabilistic.

Examples:
- provisional
- estimated
- audited
- certified
- archived

Confidence does not override phase or source.

---

## Domain Specialization

Domains may extend the schema with additional fields, but must not:
- Remove core fields.
- Collapse axes.
- Imply authority.

Extensions must remain observational.

---

## Example: Elections

```json
{
  "domain": "elections",
  "entity_id": "MI-Wayne-P042",
  "phase": "counted",
  "metric": "ballots_cast",
  "value": 1832,
  "unit": "count",
  "source": "county_tabulator_v3",
  "timestamp": "2026-11-03T21:14:00Z",
  "confidence": "provisional",
  "notes": "late upload due to network outage"
}
```

---

## Example: Supply Chain

```json
{
  "domain": "supply_chain",
  "entity_id": "DC-ATL-07",
  "phase": "in_transit",
  "metric": "units_shipped",
  "value": 4200,
  "unit": "items",
  "source": "logistics_system_A",
  "timestamp": "2026-04-12T09:30:00Z",
  "confidence": "reported"
}
```

---

## Observer Guarantees

The observer guarantees that:
- All observations are preserved.
- No observation is modified.
- No synthesis implies correctness.
- All outputs remain replayable.

The observer makes **structure visible**, not truth final.

---

This minimal API is sufficient to support triadic coherence analysis across domains without introducing control, prediction, or enforcement.

The simplicity is intentional. Complexity belongs in interpretation, not emission.
