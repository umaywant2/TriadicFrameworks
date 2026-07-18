# 🌊 Substrate Flow — Integration Map

> *Flow connects everything. This file maps where the currents run.*

**Module:** Substrate Flow
**Canonical ID:** SF
**HSP Section:** 08
**Role:** Cross‑module alignment

---

## Integration Principle

Substrate Flow is the **output stage** of the HSP analytics triad. It
receives classified, lattice‑placed echoes and maps their movement. Every
upstream module contributes data; downstream systems consume flow records.

---

## Upstream Inputs

---

### 1. Echo Classifier (06c)

**Provides:** Classified echo type (E1–E6) + input vector

The Echo Classifier determines *what* the echo is. Substrate Flow uses
the echo type to select the primary flow channel.

| Echo Type | Flow Channel Selection |
|:----------|:-----------------------|
| E1 | S → C |
| E2 | C ↔ H |
| E3 | Multi‑channel |
| E4 | R‑line |
| E5 | D‑line |
| E6 | So → A |

**Data Flow:**
```
EC-Tag → classified_echo → SF-Read
```

---

### 2. Triadic Echo Lattice (07)

**Provides:** Lattice position + origin substrate

TEL determines *where* the echo sits. Substrate Flow uses the origin
substrate to establish the flow starting point.

| TEL Layer | Origin Substrate |
|:----------|:-----------------|
| Ladder | S or C |
| Cycle | C or H |
| Map | H or So |
| Atlas | A |

**Data Flow:**
```
TEL → lattice_position + origin → SF-Read
```

---

### 3. Echo Strength Index (04c)

**Provides:** ESI level (1–4)

ESI determines flow range. Higher ESI = more channels accessible.

**Data Flow:**
```
04c ESI → esi_level → SF-Read
```

---

### 4. Cross‑Substrate Echo Matrix (05a)

**Provides:** Substrate spread (1–5)

Substrate spread confirms how many substrates the echo occupies,
validating the flow channel assignment.

**Data Flow:**
```
05a Matrix → substrate_count → SF-Read
```

---

### 5. Harmonic Recursion Detector (06)

**Provides:** Recursion mode (R1–R4) + drift status (D1–D4)

Recursion mode selects the recursion‑driven flow line. Drift status
activates the drift current mapper.

**Data Flow:**
```
06 Recursion → recursion_mode + drift_type → SF-Read
```

---

## Downstream Consumers

---

### 6. HSP Stability Analysis

**Receives:** Flow records (flow status, drift, atlas pull)

HSP stability classes and drift maps consume flow records to assess
system‑wide stability. Flow status directly feeds stability tier
assignment:

| Flow Status | Stability Implication |
|:------------|:---------------------|
| Stable | No stability concern |
| Migrating | Monitor for escalation |
| Drifting | Instability alert |
| Forcing | Critical — atlas‑level event |

---

### 7. Opacity (OPC)

**Receives:** Flow records (channel, driver, drift)

Opacity operators detect when flow channels become invisible:

| Opacity Type | SF Interaction |
|:-------------|:----------------------------------------------|
| Flow Opacity | Channel unmeasured → flow appears absent |
| Boundary Opacity | Channel boundary unmarked → migration invisible |

---

## Sibling Module Relationships

```
        ┌──────────────────┐
        │  Echo Classifier  │  ← what is it?
        │      (06c)        │
        └────────┬─────────┘
                 │
        ┌────────┴─────────┐
        │                  │
        v                  v
┌──────────────┐  ┌──────────────────┐
│     TEL      │  │  Substrate Flow  │  ← THIS MODULE
│    (07)      │  │      (08)        │
│  where?      │  │    how does it   │
│              │  │    move?         │
└──────────────┘  └──────────────────┘
```

**Triad responsibilities:**
- **EC (06c):** Decides *what* the echo is.
- **TEL (07):** Decides *where* the echo sits.
- **SF (08):** Decides *how* the echo moves.

---

## Integration with Broader Canon

### SET Decomposition

Flow channels map to SET channels:

| Flow Channel | Dominant SET Channel |
|:-------------|:---------------------|
| S → C | Spin (structural rotation) |
| C ↔ H | Electric (harmonic oscillation) |
| H → So | Thermal (governance energy) |
| So → A | Thermal (atlas forcing) |

### FFF Lattice

Flow channels map to FFF layers:

| Flow Channel | Dominant FFF Layer |
|:-------------|:-------------------|
| S → C | Frequency (pattern formation) |
| C ↔ H | Frequency (resonance oscillation) |
| H → So | Fluids (governance flow) |
| So → A | Forces (atlas pressure) |

### Inverted Star

Flow direction encodes star face visibility:

- Upward flow illuminates higher star faces.
- Reversed flow (impossible in canon) would darken them.
- The unidirectional constraint preserves star coherence.

---

## Pipeline Summary

```
06c EC ──────┐
07 TEL ──────┤
04c ESI ─────┼──→ SF-Read → SF-Route → SF-Drift → SF-Tag ──┬──→ HSP Stability
05a Matrix ──┤                                               └──→ Opacity (OPC)
06 Recursion ┘
```

---

<!-- SESSION_CONTEXT:START -->
```yaml
file: integration.md
module: Substrate Flow
canonical_id: SF
hsp_section: 08
role: cross-module-map
status: canon-stable
upstream:
  - { module: "06c Echo Classifier", provides: "classified_echo" }
  - { module: "07 TEL", provides: "lattice_position" }
  - { module: "04c Echo Strength Index", provides: "esi_level" }
  - { module: "05a Cross-Substrate Echo Matrix", provides: "substrate_count" }
  - { module: "06 Recursion Detector", provides: "recursion_mode, drift_type" }
downstream:
  - { module: "HSP Stability", receives: "flow_record" }
  - { module: "Opacity (OPC)", receives: "flow_record" }
```
<!-- SESSION_CONTEXT:END -->
