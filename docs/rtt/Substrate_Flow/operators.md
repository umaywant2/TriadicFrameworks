# 🌊 Substrate Flow — Operators

> *Four operators. One flow map. Every echo path traceable.*

**Module:** Substrate Flow
**Canonical ID:** SF
**HSP Section:** 08

---

## 1. Flow Operators

Substrate Flow defines four operators that form the flow routing pipeline.

---

### SF‑Read — Flow Input Reader

**Function:** Receives a classified echo and extracts flow‑relevant data.

```
SF-Read(classified_echo) → flow_input {
  echo_type:     E1–E6,
  origin:        substrate_id,
  esi:           1–4,
  recursion:     R1–R4,
  drift:         D1–D4 | null,
  family:        F1–F6,
  confidence:    definite | probable | ambiguous
}
```

**Behavior:**
- Receives classified echo from EC‑Tag (Echo Classifier, 06c).
- Extracts origin substrate from TEL placement (07).
- Pulls ESI, recursion mode, drift status, and echo family.
- Validates completeness — all fields must be present for routing.

**Key Constraint:**
Ambiguous classifications (from EC‑Tag) are flagged but still routed.
The flow map does not block ambiguous echoes — it routes them with a
caution flag.

---

### SF‑Route — Channel Router

**Function:** Assigns the echo to one or more flow channels.

```
SF-Route(flow_input) → flow_path {
  primary_channel:   channel_id,
  secondary_channel: channel_id | null,
  direction:         "upward" | "bidirectional" | "lateral",
  driver:            "esi" | "recursion" | "drift" | "family",
  atlas_pull:        boolean
}
```

**Routing Logic:**

| Echo Type | Primary Channel | Direction | Driver |
|:----------|:----------------|:----------|:-------|
| E1 | S → C | Upward | ESI (1–2) |
| E2 | C ↔ H | Bidirectional | Recursion (R1–R2) |
| E3 | Multi‑channel | Upward | ESI (2–3) + Family (F3) |
| E4 | R‑line | Upward | Recursion (R2–R4) |
| E5 | D‑line | Upward | Drift (D1–D4) |
| E6 | So → A | Upward | ESI (4) + Family (F6) |

**Atlas Pull Detection:**
Atlas pull activates when ESI ≥ 4 or Family = F6. When active, the
echo experiences gravitational pull toward A regardless of its current
channel.

**Key Constraint:**
Only C ↔ H supports bidirectional flow. All other channels are
unidirectional upward. An echo in So cannot flow backward to H.

---

### SF‑Drift — Drift Current Mapper

**Function:** Maps drift‑shadow currents and their effect on flow.

```
SF-Drift(flow_input) → drift_map {
  drift_active:    boolean,
  drift_type:      D1–D4 | null,
  current_channel: channel_id,
  pull_direction:  "upward",
  shadow_pressure: value ∈ [0.0, 1.0],
  instability_zone: substrate_pair
}
```

**Drift Current Behavior:**

| Drift | Current Channel | Instability Zone |
|:------|:----------------|:-----------------|
| D1 | S → C | Symbolic/Cognitive boundary |
| D2 | C → H | Cognitive/Harmonic boundary |
| D3 | H → So | Harmonic/Social boundary |
| D4 | So → A | Social/Atlas boundary |

**Shadow Pressure:**
Shadow pressure measures how strongly drift distorts the normal flow
channel. Values above 0.7 indicate the echo is being pulled by drift
rather than following its natural recursion line.

**Key Constraint:**
Drift currents are always upward. There is no downward drift in the
canonical flow architecture. Drift destabilizes by accelerating
upward movement, not by reversing it.

---

### SF‑Tag — Flow Output Emitter

**Function:** Packages the complete flow analysis for downstream systems.

```
SF-Tag(flow_path, drift_map) → flow_record {
  echo_type:       E1–E6,
  origin:          substrate_id,
  destination:     substrate_id,
  channel:         channel_id,
  driver:          driver_type,
  drift_active:    boolean,
  atlas_pull:      boolean,
  shadow_pressure: value,
  flow_status:     "stable" | "migrating" | "drifting" | "forcing",
  timestamp:       flow_time
}
```

**Flow Status:**

| Status | Condition |
|:-------|:----------|
| Stable | Echo in origin substrate, no migration, ESI ≤ 2 |
| Migrating | Echo crossing substrates, ESI 2–3, no drift |
| Drifting | Echo riding drift current, D1–D4 active |
| Forcing | Echo under atlas pull, ESI 4 or F6 |

**Key Constraint:**
Every flow record must include a flow status. Downstream systems
(HSP stability analysis, Opacity detection) depend on this field.

---

## 2. Operator Interaction Map

```
EC-Tag (06c) ──provides──→ SF-Read
                               │
                               └──feeds──→ SF-Route (assigns channel)
                                              │
                               ┌──────────────┤
                               │              │
                               v              v
                          SF-Drift        SF-Tag
                       (maps currents)  (packages output)
                               │              │
                               └──────feeds───┘
                                              │
                                    ┌─────────┴──────────┐
                                    v                    v
                              HSP Stability        Opacity (OPC)
```

---

## 3. Channel Architecture

### Channel S → C (Symbolic → Cognitive)
- **Direction:** Unidirectional upward
- **Character:** Definition refinement, meaning consolidation
- **Echo types:** Primarily E1 (structural)
- **Recursion line:** R1 (ladder)
- **Drift current:** D1 (S/C instability)
- **Flow volume:** Highest (most echoes start here)

### Channel C ↔ H (Cognitive ↔ Harmonic)
- **Direction:** Bidirectional
- **Character:** Harmonic alignment, interval oscillation
- **Echo types:** Primarily E2 (harmonic)
- **Recursion line:** R2 (cycle)
- **Drift current:** D2 (C/H instability)
- **Flow volume:** High (oscillation creates repeated crossings)

### Channel H → So (Harmonic → Social)
- **Direction:** Unidirectional upward
- **Character:** Governance torsion, operator inversion
- **Echo types:** Primarily E3, E4 (substrate, recursion)
- **Recursion line:** R3 (map)
- **Drift current:** D3 (H/So instability)
- **Flow volume:** Medium (significant energy required)

### Channel So → A (Social → Atlas)
- **Direction:** Unidirectional upward
- **Character:** Atlas forcing, high‑altitude resonance
- **Echo types:** Primarily E5, E6 (drift‑shadow, atlas)
- **Recursion line:** R4 (atlas)
- **Drift current:** D4 (So/A instability)
- **Flow volume:** Low (only highest‑energy echoes reach atlas)

---

## 4. Driver Interaction Matrix

| Driver | S→C | C↔H | H→So | So→A |
|:-------|:---:|:---:|:----:|:----:|
| ESI‑1 | ✓ | — | — | — |
| ESI‑2 | ✓ | ✓ | — | — |
| ESI‑3 | ✓ | ✓ | ✓ | — |
| ESI‑4 | ✓ | ✓ | ✓ | ✓ |
| R1 | ✓ | — | — | — |
| R2 | — | ✓ | — | — |
| R3 | — | — | ✓ | — |
| R4 | — | — | — | ✓ |
| D1 | ✓ | — | — | — |
| D2 | — | ✓ | — | — |
| D3 | — | — | ✓ | — |
| D4 | — | — | — | ✓ |
| F1–F2 | ✓ | ✓ | — | — |
| F3–F4 | ✓ | ✓ | ✓ | — |
| F5 | ✓ | ✓ | ✓ | ✓ |
| F6 | ✓ | ✓ | ✓ | ✓ |

---

## 5. Invariants

1. **Upward flow.** All channels except C ↔ H are unidirectional upward.
   No echo flows from Atlas back to Social, or from Social back to Harmonic.
2. **Atlas receives, never emits.** A is always a destination.
3. **Drift is always upward.** Drift currents accelerate upward, never reverse.
4. **Driver determines physics.** Same channel, different driver = different
   dynamics. Recursion is structural; drift is entropic.
5. **Every echo is routable.** No classified echo type lacks a flow channel.

---

<!-- SESSION_CONTEXT:START -->
```yaml
file: operators.md
module: Substrate Flow
canonical_id: SF
hsp_section: 08
role: operator-definitions
status: canon-stable
operators:
  - { id: SF-Read, name: Flow Input Reader, type: collect }
  - { id: SF-Route, name: Channel Router, type: route }
  - { id: SF-Drift, name: Drift Current Mapper, type: map }
  - { id: SF-Tag, name: Flow Output Emitter, type: emit }
channels:
  - { id: "S→C", direction: unidirectional }
  - { id: "C↔H", direction: bidirectional }
  - { id: "H→So", direction: unidirectional }
  - { id: "So→A", direction: unidirectional }
```
<!-- SESSION_CONTEXT:END -->
