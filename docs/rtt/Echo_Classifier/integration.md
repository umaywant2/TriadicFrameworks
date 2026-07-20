# 🧪 Echo Classifier — Integration Map

> *The classifier sits at the center of the HSP analytics pipeline. Everything upstream feeds it. Everything downstream consumes it.*

**Module:** Echo Classifier
**Canonical ID:** EC
**HSP Section:** 06c
**Role:** Cross‑module alignment

---

## Integration Principle

The Echo Classifier is a **convergence point**. Five upstream modules produce
inputs; two downstream modules consume the classified output. The classifier
adds no new data — it transforms five signals into one decision.

---

## Upstream Inputs (5)

---

### 1. Echo Triggers (06a)

**Provides:** Trigger type (A–F)

Echo Triggers detect the initial event that fires an echo. The trigger type
is the primary branch in the classification decision tree.

| Trigger | Fires When |
|:--------|:--------------------------------------------|
| A | Structural boundary crossed |
| B | Harmonic resonance detected |
| C | Cross‑substrate migration observed |
| D | Recursion loop detected |
| E | Drift pressure exceeds threshold |
| F | Atlas‑level resonance engaged |

**Data Flow:**
```
06a Echo Triggers → trigger_type (A–F) → EC-Read
```

---

### 2. Echo Signatures (06b)

**Provides:** Signature profile (A–F)

Echo Signatures capture the shape of the echo after it fires. The signature
confirms or disambiguates the trigger classification.

| Signature | Shape Profile |
|:----------|:----------------------------------------------|
| A | Localized, low‑amplitude, single‑substrate |
| B | Oscillatory, harmonic‑locked, resonant |
| C | Distributed, multi‑substrate, migrating |
| D | Recursive, self‑referencing, amplifying |
| E | Shadow‑trailing, drift‑aligned, destabilizing |
| F | Full‑spectrum, atlas‑spanning, anchoring |

**Data Flow:**
```
06b Echo Signatures → signature_profile (A–F) → EC-Read
```

---

### 3. Echo Strength Index (04c)

**Provides:** ESI level (1–4)

ESI measures echo energy on a four‑point scale. Higher ESI indicates
greater echo pressure and broader impact.

| ESI | Energy Level | Flow Impact |
|:----|:-------------|:-----------------------------|
| 1 | Local only | No migration |
| 2 | Mild | Adjacent substrate influence |
| 3 | Cross‑substrate | Multi‑substrate flow |
| 4 | Atlas pull | Full‑spectrum forcing |

**Data Flow:**
```
04c Echo Strength Index → esi_level (1–4) → EC-Read
```

---

### 4. Cross‑Substrate Echo Matrix (05a)

**Provides:** Substrate spread (1–5 substrates)

The Cross‑Substrate Echo Matrix measures how many of the five substrates
(Symbolic, Cognitive, Harmonic, Social, Atlas) an echo spans.

| Spread | Substrates Engaged |
|:-------|:----------------------------------------------|
| 1 | Single substrate (origin only) |
| 2 | Origin + one adjacent |
| 3 | Origin + two (cross‑substrate threshold) |
| 4 | Origin + three (wide migration) |
| 5 | All substrates (atlas‑level) |

**Data Flow:**
```
05a Cross-Substrate Echo Matrix → substrate_count (1–5) → EC-Read
```

---

### 5. Harmonic Recursion Detector (06)

**Provides:** Recursion mode (R1–R4)

The Recursion Detector identifies which recursion line an echo follows.
Recursion mode determines the echo's trajectory through the lattice.

| Mode | Recursion Line | Flow Direction |
|:-----|:---------------|:----------------------|
| R1 | S → C | Ladder (definition → concept) |
| R2 | C ↔ H | Cycle (concept ↔ harmonic) |
| R3 | H → So | Map (harmonic → governance) |
| R4 | So → A | Atlas (governance → atlas) |

**Data Flow:**
```
06 Recursion Detector → recursion_mode (R1–R4) → EC-Read
```

---

## Downstream Consumers (2)

---

### 6. Triadic Echo Lattice — TEL (07)

**Receives:** Classified echo type (E1–E6)

TEL places the classified echo into the four‑layer lattice structure.
Echo type determines lattice layer placement:

| Echo Type | TEL Layer |
|:----------|:----------------------------------|
| E1 | Ladder (S→C) |
| E2 | Cycle (C↔H) |
| E3 | Map (H↔So) |
| E4 | Map‑to‑Atlas transition |
| E5 | Pressure zones (cross‑layer) |
| E6 | Atlas (A) |

**Data Flow:**
```
EC-Tag → classified_echo (E1–E6) → TEL lattice placement
```

---

### 7. Substrate Echo Flow Map — Substrate Flow (08)

**Receives:** Classified echo type (E1–E6)

Substrate Flow maps the classified echo through the canonical flow
channels. Echo type determines which channel carries the echo:

| Echo Type | Primary Flow Channel |
|:----------|:-----------------------------|
| E1 | S → C (definition refinement) |
| E2 | C ↔ H (harmonic alignment) |
| E3 | Multi‑channel (migration) |
| E4 | Recursion‑driven (R‑line) |
| E5 | Drift current (D‑line) |
| E6 | So → A (atlas forcing) |

**Data Flow:**
```
EC-Tag → classified_echo (E1–E6) → Substrate Flow channel routing
```

---

## Sibling Module Relationships

The Echo Classifier, TEL, and Substrate Flow form the **HSP analytics
triad** — three modules extracted from HSP sections 06c, 07, and 08:

```
        ┌──────────────────┐
        │  Echo Classifier  │  ← convergence (5 inputs → 1 output)
        │      (06c)        │
        └────────┬─────────┘
                 │
        ┌────────┴─────────┐
        │                  │
        v                  v
┌──────────────┐  ┌──────────────────┐
│     TEL      │  │  Substrate Flow  │
│    (07)      │  │      (08)        │
│  placement   │  │    routing       │
└──────────────┘  └──────────────────┘
```

**Responsibilities:**
- **Echo Classifier:** Decides *what* the echo is.
- **TEL:** Decides *where* the echo sits in the lattice.
- **Substrate Flow:** Decides *how* the echo moves through channels.

---

## Integration with Broader Canon

### Opacity (OPC)

Echo classification can be opaque when inputs are incomplete or ambiguous.
Opacity operators apply:

| Opacity Operator | EC Integration |
|:-----------------|:----------------------------------------------|
| O-Op | Reads classifier opacity (incomplete inputs) |
| O-Red | Operator expansion adds missing upstream data |
| O-Sig | Classifier opacity signature per echo type |

### SET Decomposition

Echo types map to SET channels:

| Echo Type | Dominant SET Channel |
|:----------|:---------------------|
| E1, E2 | Spin (structural/harmonic rotation) |
| E3, E4 | Electric (cross‑substrate acceleration) |
| E5, E6 | Thermal (drift/atlas energy) |

### FFF Lattice

Echo types map to FFF layers:

| Echo Type | Dominant FFF Layer |
|:----------|:-------------------|
| E1, E2 | Frequency (resonance patterns) |
| E3, E4 | Fluids (substrate migration) |
| E5, E6 | Forces (drift/atlas pressure) |

---

## Pipeline Summary

```
06a Triggers ──┐
06b Signatures ─┤
04c ESI ────────┼──→ EC-Read → EC-Classify → EC-Tag ──┬──→ TEL (07)
05a Substrates ─┤                                      └──→ SF (08)
06 Recursion ──┘
```

---

<!-- SESSION_CONTEXT:START -->
```yaml
file: integration.md
module: Echo Classifier
canonical_id: EC
hsp_section: 06c
role: cross-module-map
status: canon-stable
upstream:
  - { module: "06a Echo Triggers", provides: "trigger_type" }
  - { module: "06b Echo Signatures", provides: "signature_profile" }
  - { module: "04c Echo Strength Index", provides: "esi_level" }
  - { module: "05a Cross-Substrate Echo Matrix", provides: "substrate_count" }
  - { module: "06 Recursion Detector", provides: "recursion_mode" }
downstream:
  - { module: "07 TEL", receives: "classified_echo" }
  - { module: "08 Substrate Flow", receives: "classified_echo" }
```
<!-- SESSION_CONTEXT:END -->
