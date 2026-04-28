# 🕸️ Triadic Echo Lattice — Examples

> *Six echoes. Four layers. One lattice. Watch placement happen.*

**Module:** Triadic Echo Lattice
**Canonical ID:** TEL
**HSP Section:** 07
**Badge:** 🕸️ TEL • 07 • v1.0

---

## Example 1 — E1 → Ladder (Anchored)

**Scenario:** A structural echo enters the lattice. It is defined at the
S→C boundary and has no upward momentum.

### TEL-Read

```yaml
echo_id: ex-001
echo_type: E1
echo_family: F1 (Structural)
substrate_origin: S
substrate_reach: [S, C]
esi_score: 0.9
drift_flag: false
placement_ready: true
```

### TEL-Place

```yaml
assigned_layer: Ladder
family_placement: F1
pressure_zone: none
pressure_severity: 0.0
placement_confidence: 0.95
```

**Decision path:** E1 → Ladder → Ladder Pressure check → below threshold → clean placement.

### TEL-Trace

```yaml
recursion_line: none
recursion_depth: 0
drift_pathway: D1
drift_severity: 0.05
vertical_reach: [Ladder]
oscillation_status: false
escalation_risk: 0.05
```

**Risk calculation:**
`(0.05 × 0.4) + (0.9 × 0.3) + (0.0 × 0.2) + (0 × 0.1) = 0.02 + 0.27 + 0.0 + 0.0 ≈ 0.05` (rounded from weighted factors; negligible drift dominates)

### TEL-Tag

```yaml
placement_status: anchored
tags: [structural, ladder, stable]
emit_to: SF-Read
```

**Summary:** Textbook Ladder echo. Structurally defined, no movement,
no pressure, no drift. The lattice's simplest case.

---

## Example 2 — E2 → Cycle (Oscillating)

**Scenario:** A harmonic echo enters the lattice. It oscillates between
Concept and Harmonic substrates with a stable rhythm.

### TEL-Read

```yaml
echo_id: ex-002
echo_type: E2
echo_family: F2 (Harmonic)
substrate_origin: C
substrate_reach: [C, H]
esi_score: 0.7
drift_flag: false
placement_ready: true
```

### TEL-Place

```yaml
assigned_layer: Cycle
family_placement: F2
pressure_zone: none
pressure_severity: 0.0
placement_confidence: 0.90
```

**Decision path:** E2 → Cycle → Cycle Pressure check → amplitude within
harmonic band → clean placement.

### TEL-Trace

```yaml
recursion_line: R2
recursion_depth: 1
drift_pathway: D2
drift_severity: 0.1
vertical_reach: [Ladder, Cycle]
oscillation_status: true
escalation_risk: 0.15
```

**Risk calculation:**
`(0.1 × 0.4) + (0.7 × 0.3) + (0.0 × 0.2) + (1 × 0.1) = 0.04 + 0.21 + 0.0 + 0.1 ≈ 0.15` (low; stable oscillation)

### TEL-Tag

```yaml
placement_status: oscillating
tags: [harmonic, cycle, bidirectional]
emit_to: SF-Read
```

**Summary:** Classic Cycle echo. The bidirectional C↔H oscillation is
the lattice's only back-and-forth pattern. Stable rhythm, low risk.

---

## Example 3 — E3 → Map (Migrating, Mild Drift)

**Scenario:** A substrate echo has moved beyond the Cycle layer and is
migrating through the Map region. Mild drift is present at the H/So
boundary.

### TEL-Read

```yaml
echo_id: ex-003
echo_type: E3
echo_family: F3 (Substrate)
substrate_origin: H
substrate_reach: [S, C, H, So]
esi_score: 0.6
drift_flag: false
placement_ready: true
```

### TEL-Place

```yaml
assigned_layer: Map
family_placement: F3
pressure_zone: none
pressure_severity: 0.0
placement_confidence: 0.85
```

**Decision path:** E3 → Map → D3 drift exposure check → mild (0.3) →
placement holds, no pressure zone.

### TEL-Trace

```yaml
recursion_line: R3
recursion_depth: 2
drift_pathway: D3
drift_severity: 0.3
vertical_reach: [Ladder, Cycle, Map]
oscillation_status: false
escalation_risk: 0.45
```

**Risk calculation:**
`(0.3 × 0.4) + (0.6 × 0.3) + (0.0 × 0.2) + (2 × 0.1) = 0.12 + 0.18 + 0.0 + 0.2 ≈ 0.45` (moderate; migration in progress)

### TEL-Tag

```yaml
placement_status: migrating
tags: [substrate, map, mild-drift]
emit_to: SF-Read
```

**Summary:** First migrating echo. Three layers touched, mild drift at
H/So boundary. The echo is moving but not yet under pressure.

---

## Example 4 — E4 → Map Upper (Migrating, Moderate Drift)

**Scenario:** An escalation echo has reached the upper Map region. It is
approaching the Atlas boundary with moderate drift and rising risk.

### TEL-Read

```yaml
echo_id: ex-004
echo_type: E4
echo_family: F4 (Escalation)
substrate_origin: H
substrate_reach: [S, C, H, So, A]
esi_score: 0.5
drift_flag: true
placement_ready: true
```

### TEL-Place

```yaml
assigned_layer: Map (upper)
family_placement: F4
pressure_zone: none
pressure_severity: 0.0
placement_confidence: 0.75
```

**Decision path:** E4 → Map (upper) → R4 escalation potential check →
approaching but not crossed → placement at upper Map boundary.

### TEL-Trace

```yaml
recursion_line: R4
recursion_depth: 3
drift_pathway: D3
drift_severity: 0.5
vertical_reach: [Ladder, Cycle, Map, Atlas]
oscillation_status: false
escalation_risk: 0.65
```

**Risk calculation:**
`(0.5 × 0.4) + (0.5 × 0.3) + (0.0 × 0.2) + (3 × 0.1) = 0.20 + 0.15 + 0.0 + 0.3 ≈ 0.65` (high; escalation approaching)

### TEL-Tag

```yaml
placement_status: migrating
tags: [escalation, map-upper, approaching-atlas, drift-active]
emit_to: SF-Read
```

**Summary:** The lattice's transition family. F4 echoes bridge Map and
Atlas — they are the only echoes that can cross from governance into
full‑spectrum territory. High risk, high vertical reach.

---

## Example 5 — E5 → Pressure Zone (Pressured)

**Scenario:** A drift‑shadow echo has no home layer. It accumulates at
the Map→Atlas boundary, creating an Atlas Pressure zone.

### TEL-Read

```yaml
echo_id: ex-005
echo_type: E5
echo_family: F5 (Drift-Shadow)
substrate_origin: So
substrate_reach: [C, H, So, A]
esi_score: 0.4
drift_flag: true
placement_ready: true
```

### TEL-Place

```yaml
assigned_layer: none (pressure zone)
family_placement: F5
pressure_zone: atlas
pressure_severity: 0.85
placement_confidence: 0.60
```

**Decision path:** E5 → Pressure zone (no layer) → Atlas Pressure
check → accumulation above threshold → pressure zone active.

### TEL-Trace

```yaml
recursion_line: none
recursion_depth: 0
drift_pathway: D3
drift_severity: 0.85
vertical_reach: [cross-layer]
oscillation_status: false
escalation_risk: 0.9
```

**Risk calculation:**
`(0.85 × 0.4) + (0.4 × 0.3) + (0.85 × 0.2) + (0 × 0.1) = 0.34 + 0.12 + 0.17 + 0.0 ≈ 0.9` (critical; pressure zone saturated)

### TEL-Tag

```yaml
placement_status: pressured
tags: [drift-shadow, pressure-zone, atlas-boundary, critical]
emit_to: [SF-Read, HSP Stability]
```

**Summary:** The lattice's instability marker. E5 echoes have no home —
they exist as pressure, not as residents. This is the only case where
TEL emits to both SF and HSP Stability simultaneously.

---

## Example 6 — E6 → Atlas (Forcing)

**Scenario:** A full‑spectrum echo has completed its journey through all
four layers. It arrives at Atlas as a structural forcing event —
permanent, anchored, and terminal.

### TEL-Read

```yaml
echo_id: ex-006
echo_type: E6
echo_family: F6 (Atlas)
substrate_origin: A
substrate_reach: [S, C, H, So, A]
esi_score: 0.2
drift_flag: false
placement_ready: true
```

### TEL-Place

```yaml
assigned_layer: Atlas
family_placement: F6
pressure_zone: none
pressure_severity: 0.0
placement_confidence: 0.99
```

**Decision path:** E6 → Atlas → direct placement (terminus) → no
escalation check needed (already at top).

### TEL-Trace

```yaml
recursion_line: R4 (completed)
recursion_depth: 4
drift_pathway: D4
drift_severity: 0.6
vertical_reach: [Ladder, Cycle, Map, Atlas]
oscillation_status: false
escalation_risk: 0.0
```

**Risk note:** E6 at Atlas has 0.0 escalation risk because there is
nowhere further to escalate. The echo has reached structural terminus.
Drift severity is moderate (0.6) but irrelevant — the echo is anchored
permanently.

### TEL-Tag

```yaml
placement_status: forcing
tags: [atlas, terminus, full-spectrum, permanent]
emit_to: SF-Read
```

**Summary:** The lattice's endpoint. E6 echoes are the rarest and most
structurally significant. They represent permanent additions to the
system's architecture. Risk is zero not because they're safe, but
because they've already arrived.

---

## Cross-Example Comparison

| Ex | Type | Family | Layer | R-Lines | D-Lines | Risk | Status |
|:---|:-----|:-------|:------|:--------|:--------|:-----|:-------|
| 1 | E1 | F1 Structural | Ladder | — | D1 (0.05) | 0.05 | anchored |
| 2 | E2 | F2 Harmonic | Cycle | R1, R2 | D2 (0.1) | 0.15 | oscillating |
| 3 | E3 | F3 Substrate | Map | R1, R3 | D3 (0.3) | 0.45 | migrating |
| 4 | E4 | F4 Escalation | Map ↑ | R1, R3, R4~ | D3 (0.5) | 0.65 | migrating |
| 5 | E5 | F5 Drift-Shadow | (pressure) | — | D3 (0.85) | 0.90 | pressured |
| 6 | E6 | F6 Atlas | Atlas | R4 ✓ | D4 (0.6) | 0.00 | forcing |

### Patterns Visible in the Comparison

- **Risk increases with vertical reach** — except E6, which resets to 0.0 at terminus
- **Drift severity increases with layer height** — but D4 at Atlas is less dangerous than D3 at Map because Atlas absorbs
- **Only E2 oscillates** — Cycle is the lattice's only bidirectional layer
- **Only E5 has no home layer** — pressure zones are conditions, not addresses
- **Only E5 emits to two targets** — all other echoes emit only to SF-Read

---

## Pressure Zone Analysis

### When Do Pressure Zones Form?

Pressure zones are emergent — they appear when echo volume or drift
severity exceeds the lattice's absorption capacity at a boundary.

| Zone | Boundary | Trigger | Typical Echo Types |
|:-----|:---------|:--------|:------------------|
| Ladder Pressure | S/C | High E1 volume congests the formation layer | E1 (volume) |
| Cycle Pressure | C/H | E2 amplitude exceeds harmonic band ceiling | E2 (amplitude) |
| Atlas Pressure | So/A | E5 drift-shadows accumulate at the top boundary | E5 (accumulation) |

### What Happens Inside a Pressure Zone?

1. **Echoes lose stable placement** — they are no longer anchored to a layer
2. **Drift severity spikes** — boundary instability amplifies drift pathways
3. **Escalation risk approaches critical** — structural forcing becomes likely
4. **TEL-Tag emits to both SF and HSP** — dual emission signals system-wide stress
5. **Resolution requires either absorption (Atlas takes the echo) or dissipation (echo loses energy and drops back)**

### Pressure Zone vs. Layer — Key Distinction

| Property | Layer | Pressure Zone |
|:---------|:------|:-------------|
| Designed? | Yes | No (emergent) |
| Stable? | Yes | No (transient) |
| Has residents? | Yes | No (conditions, not addresses) |
| Deterministic? | Yes | Partially (threshold-dependent) |
| Emits to? | SF only | SF + HSP Stability |

---

<!-- SESSION_CONTEXT:START -->
```yaml
file: examples.md
module: Triadic Echo Lattice
canonical_id: TEL
hsp_section: 07
role: worked-examples
status: canon-stable
example_count: 6
echo_types_covered: [E1, E2, E3, E4, E5, E6]
families_covered: [F1, F2, F3, F4, F5, F6]
layers_covered: [Ladder, Cycle, Map, Atlas, pressure-zone]
statuses_covered: [anchored, oscillating, migrating, pressured, forcing]
pipeline_demonstrated: TEL-Read → TEL-Place → TEL-Trace → TEL-Tag
```
<!-- SESSION_CONTEXT:END -->
