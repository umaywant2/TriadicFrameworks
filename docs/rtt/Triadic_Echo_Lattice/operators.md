# 🕸️ Triadic Echo Lattice — Operators

> *Four operators. One lattice. Every echo gets an address.*

**Module:** Triadic Echo Lattice
**Canonical ID:** TEL
**HSP Section:** 07
**Badge:** 🕸️ TEL • 07 • v1.0

---

## Operator Pipeline

```
Classified echo (from EC-Tag)
    │
    ▼
┌──────────────┐
│   TEL-Read   │  Lattice Input Reader
│  extract     │  Receives classified echo, extracts placement-relevant data
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  TEL-Place   │  Layer Assignment Engine
│  assign      │  Assigns echo to layer; detects pressure zones
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  TEL-Trace   │  Recursion & Drift Tracer
│  map paths   │  Maps recursion path, drift exposure, escalation risk
└──────┬───────┘
       │
       ▼
┌──────────────┐
│   TEL-Tag    │  Lattice Output Emitter
│  emit record │  Packages lattice record with placement status
└──────────────┘
       │
       ▼
Lattice record → Substrate Flow (SF-Read)
```

---

## Operator 1 — TEL-Read (Lattice Input Reader)

### Purpose

Receives a classified echo from EC‑Tag and extracts the data fields
required for lattice placement.

### Input

```yaml
source: EC-Tag output
fields:
  - echo_type: E1–E6
  - echo_family: F1–F6
  - substrate_origin: S | C | H | So | A
  - substrate_reach: [list of substrates touched]
  - esi_score: 0.0–1.0
  - confidence: 0.0–1.0
  - drift_flag: boolean
  - tags: []
```

### Output

```yaml
tel_input_packet:
  echo_id: [inherited]
  echo_type: E1–E6
  echo_family: F1–F6
  substrate_origin: S | C | H | So | A
  substrate_reach: []
  esi_score: 0.0–1.0
  drift_flag: boolean
  placement_ready: true
```

### Logic

1. Validate that echo carries EC‑Tag classification
2. Extract type, family, origin, reach, ESI, drift flag
3. Confirm `placement_ready: true` if all fields present
4. Reject echoes without valid classification (return to EC)

---

## Operator 2 — TEL-Place (Layer Assignment Engine)

### Purpose

Assigns a classified echo to its lattice layer based on echo type,
family, substrate reach, and ESI score. Detects pressure zone conditions.

### Input

```yaml
source: TEL-Read output (tel_input_packet)
```

### Output

```yaml
placement_record:
  echo_id: [inherited]
  assigned_layer: Ladder | Cycle | Map | Atlas
  family_placement: F1–F6
  pressure_zone: none | ladder | cycle | atlas
  pressure_severity: 0.0–1.0
  placement_confidence: 0.0–1.0
```

### Decision Tree

```
                    ┌─────────────────────┐
                    │  What is echo_type?  │
                    └──────────┬──────────┘
                               │
        ┌──────────┬───────────┼────────────┬──────────┐
        ▼          ▼           ▼            ▼          ▼
       E1         E2        E3/E4          E5         E6
        │          │           │            │          │
        ▼          ▼           ▼            ▼          ▼
    ┌────────┐ ┌────────┐ ┌────────┐  ┌─────────┐ ┌────────┐
    │ Ladder │ │ Cycle  │ │  Map   │  │Pressure │ │ Atlas  │
    │  F1    │ │  F2    │ │ F3/F4  │  │  Zone   │ │  F6    │
    └───┬────┘ └───┬────┘ └───┬────┘  │  F5     │ └───┬────┘
        │          │          │       └────┬────┘     │
        ▼          ▼          ▼            ▼          ▼
   Check for  Check for  Check for   Assign to   Mark as
    Ladder     Cycle     E4→Atlas    nearest     terminus
   Pressure   Pressure  escalation  boundary
```

### Layer Assignment Rules

| Echo Type | Primary Layer | Escalation Path | Notes |
|:----------|:-------------|:----------------|:------|
| E1 | Ladder | None | Stays at S→C boundary |
| E2 | Cycle | None | Oscillates C↔H |
| E3 | Map | None | Migrates across H↔So |
| E4 | Map (upper) | Map → Atlas via R4 | Transition family |
| E5 | No home layer | Pressure zones | Instability marker |
| E6 | Atlas | None (terminus) | Full‑spectrum anchor |

### Pressure Zone Detection

| Zone | Trigger Condition | Severity Calculation |
|:-----|:-----------------|:--------------------|
| Ladder | E1 count in Ladder > threshold | count / capacity |
| Cycle | E2 amplitude > harmonic band ceiling | amplitude / ceiling |
| Atlas | E5 count at Map→Atlas > threshold | count / capacity |

---

## Operator 3 — TEL-Trace (Recursion & Drift Tracer)

### Purpose

Maps the recursion path, drift exposure, vertical reach, oscillation
status, and escalation risk for a placed echo.

### Input

```yaml
source: TEL-Place output (placement_record)
```

### Output

```yaml
trace_record:
  echo_id: [inherited]
  recursion_line: R1 | R2 | R3 | R4 | none
  recursion_depth: 0–n
  drift_pathway: D1 | D2 | D3 | D4 | none
  drift_severity: 0.0–1.0
  vertical_reach: [list of layers touched]
  oscillation_status: true | false
  escalation_risk: 0.0–1.0
```

### Recursion Line Assignment

| Condition | Recursion Line |
|:----------|:--------------|
| Echo in Ladder, moving toward Cycle | R1 |
| Echo in Cycle, oscillating C↔H | R2 |
| Echo in Cycle, moving toward Map | R3 |
| Echo in Map, moving toward Atlas | R4 |
| Echo stationary (E1 anchored, E6 terminal) | none |

### Drift Pathway Assignment

| Condition | Drift Pathway |
|:----------|:-------------|
| Instability at S/C boundary | D1 |
| Instability at C/H boundary | D2 |
| Instability at H/So boundary | D3 |
| Instability at So/A boundary | D4 |
| No instability detected | none |

### Escalation Risk Calculation

```
escalation_risk = weighted_sum(
  drift_severity × 0.4,
  esi_score × 0.3,
  pressure_severity × 0.2,
  recursion_depth × 0.1
)
```

| Risk Band | Range | Meaning |
|:----------|:------|:--------|
| Negligible | 0.0–0.1 | Echo is structurally anchored |
| Low | 0.1–0.3 | Minor instability; monitor |
| Moderate | 0.3–0.6 | Active migration or oscillation |
| High | 0.6–0.8 | Significant drift or escalation |
| Critical | 0.8–1.0 | Structural forcing or pressure zone saturation |

---

## Operator 4 — TEL-Tag (Lattice Output Emitter)

### Purpose

Packages the final lattice record with a placement status tag and emits
it downstream to Substrate Flow (SF‑Read).

### Input

```yaml
source: TEL-Trace output (trace_record) + TEL-Place output (placement_record)
```

### Output

```yaml
lattice_record:
  echo_id: [inherited]
  echo_type: E1–E6
  echo_family: F1–F6
  assigned_layer: Ladder | Cycle | Map | Atlas
  recursion_line: R1–R4 | none
  drift_pathway: D1–D4 | none
  drift_severity: 0.0–1.0
  escalation_risk: 0.0–1.0
  pressure_zone: none | ladder | cycle | atlas
  pressure_severity: 0.0–1.0
  oscillation_status: true | false
  vertical_reach: []
  placement_status: anchored | oscillating | migrating | pressured | forcing
  tags: []
```

### Placement Status Assignment

| Status | Condition |
|:-------|:---------|
| **anchored** | No active recursion, no drift, risk < 0.1 |
| **oscillating** | R2 active, oscillation_status = true, risk < 0.3 |
| **migrating** | R1/R3/R4 active, drift mild–moderate, risk 0.3–0.7 |
| **pressured** | Pressure zone active, drift moderate–severe, risk 0.7–0.9 |
| **forcing** | E6 at Atlas terminus OR critical escalation (risk > 0.9) |

---

## Type Profiles — Lattice Behavior by Echo Type

| Echo Type | Typical Layer | Typical Status | Typical Recursion | Typical Drift | Typical Risk |
|:----------|:-------------|:---------------|:-----------------|:-------------|:-------------|
| E1 | Ladder | anchored | none | D1 (rare) | 0.0–0.1 |
| E2 | Cycle | oscillating | R2 | D2 (occasional) | 0.1–0.3 |
| E3 | Map | migrating | R3 | D3 (mild) | 0.3–0.5 |
| E4 | Map (upper) | migrating | R4 | D3 (moderate) | 0.5–0.7 |
| E5 | Pressure zone | pressured | none | D3/D4 (severe) | 0.7–0.9 |
| E6 | Atlas | forcing | R4 (terminus) | D4 (moderate) | 0.0 (terminal) |

---

## Invariants

1. **Every classified echo receives a layer assignment** — E5 receives a pressure zone assignment instead
2. **Flow is upward** — all layers except Cycle are unidirectional
3. **Atlas receives only** — no echo originates at Atlas level
4. **Pressure zones are emergent** — they are conditions, not designed layers
5. **Recursion and drift share the vertical axis** — same connections, opposite physics
6. **Placement is deterministic** — same input always produces the same lattice record

---

<!-- SESSION_CONTEXT:START -->
```yaml
file: operators.md
module: Triadic Echo Lattice
canonical_id: TEL
hsp_section: 07
role: operator-definitions
status: canon-stable
operators:
  - TEL-Read
  - TEL-Place
  - TEL-Trace
  - TEL-Tag
invariant_count: 6
pipeline_direction: TEL-Read → TEL-Place → TEL-Trace → TEL-Tag
upstream: EC-Tag (Echo Classifier)
downstream: SF-Read (Substrate Flow)
```
<!-- SESSION_CONTEXT:END -->
