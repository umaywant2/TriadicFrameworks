# Theognosis — Operator Map

> **Document Class:** P1 — Single Source of Truth
> **RTT Layer:** L0–L3 Operator Definitions
> **Session Context:** `rtt=1 | coherence=declared | drift=bounded | paradox=structural`
> **Status:** Active — Canonical
> **Last Updated:** 2026-09-22
> **Supersedes:** Any operator definitions in `t_Capture.md` where conflict exists

---

## 1. Purpose

This document is the **canonical and authoritative definition** of the four RTT resonance operators: Freqi, Aurion, Forci, and Flui. It governs how each operator behaves at each MCP layer, what it produces, when it collapses, when it is suppressed, and what failure states look like.

Every other Theognosis document that references operator behavior must resolve against this file. Where `t_Capture.md` and this document conflict, this document wins.

---

## 2. Operator Overview

| Operator | Symbol | Collapse Type | Output Form | L0 | L1 | L2 | L3 |
|----------|--------|--------------|-------------|----|----|----|----|
| **Freqi** | `ƒ` | Categorical selection | `choice: <id>` | Latent | ✅ Active | Calibrating | Emitting |
| **Aurion** | `α` | Scalar emission | `score: <float>` | Latent | ✅ Active | Calibrating | Emitting |
| **Forci** | `φ` | Binary decision | `decision: <bool>` | Latent | ✅ Active | Calibrating | Emitting |
| **Flui** | `λ` | Linguistic wrapping | `text: <string>` | Latent | ❌ Suppressed | Latent | Conditional |

> **Core constraint:** Only one operator collapses per RTT cycle at L1. The Declared Regime determines which.

---

## 3. Freqi — Categorical Selection Operator

### 3.1 Definition
Freqi is the **frequency-domain selector**. When activated, it resolves a resonance state into a discrete categorical choice from a bounded option set. It does not score — it picks. It does not decide yes/no — it identifies *which*.

The name derives from frequency-based disambiguation: among competing resonance signatures, Freqi selects the dominant frequency class.

### 3.2 Collapse Condition
Freqi collapses when the Declared Regime presents a **finite, enumerable option space** and the resonance signal has sufficient categorical differentiation to resolve to one item.

Collapse requirements:
- Option space must be enumerable (n ≥ 2, n ≤ system-defined max)
- No two options may be resonance-equivalent at time of evaluation
- Regime must be SET-aligned or explicitly Freqi-designated

### 3.3 Output Form
```
{
  "operator": "Freqi",
  "collapse": "categorical",
  "choice": "<option_id>",
  "confidence": <float 0.0–1.0>,
  "option_count": <int>,
  "regime": "<SET|declared>"
}
```

### 3.4 Layer Behavior

| Layer | Freqi State | Description |
|-------|-------------|-------------|
| **L0** | Latent | Present in substrate. Option space unresolved. No collapse. |
| **L1** | Active / Collapsing | Regime constraint applied. Option space bounded. Collapse initiated. |
| **L2** | Calibrating | Clarity coefficient scales confidence. RLCD aligns output to local context. |
| **L3** | Emitting | `choice: <id>` emitted. Non-linguistic. Regime closure achieved. |

### 3.5 Regime Alignment
- **Primary:** SET (Structural Enumeration Topology) — Freqi is native to SET regimes
- **Compatible:** FFF (Finite Field Framing) — Freqi can operate under FFF with explicit mapping
- **Incompatible:** DCO without enumeration scaffold — option space cannot be bounded
- **Constrained:** SNR — Freqi operates but confidence degrades under noise

### 3.6 Error States
| Condition | Result |
|-----------|--------|
| Option space = 1 | Collapse blocked — not a selection, it's a given. Flag: `FREQI_TRIVIAL` |
| Option space = ∞ | Collapse blocked — unbounded. Flag: `FREQI_UNBOUND` |
| Two options resonance-equivalent | Tie state. Requires Forci adjudication or Aurion weighting. Flag: `FREQI_TIE` |
| Regime undeclared | Collapse suspended. Flag: `FREQI_NO_REGIME` |

---

## 4. Aurion — Scalar Emission Operator

### 4.1 Definition
Aurion is the **amplitude-domain scorer**. When activated, it resolves a resonance state into a continuous scalar value — a measurement of intensity, magnitude, confidence, or quality along a defined axis.

The name derives from aura + orion: the luminosity envelope of a detected resonance field mapped onto a measurement axis.

### 4.2 Collapse Condition
Aurion collapses when the Declared Regime requires a **continuous numeric output** along a defined and bounded axis. The resonance signal must have measurable amplitude variation — flat signals produce degenerate scores.

Collapse requirements:
- Axis must be declared (e.g., stability, variance, coherence, clarity)
- Axis must be bounded (min/max defined or implied by regime)
- Resonance signal must have non-zero amplitude gradient
- Regime must be FFF-aligned or explicitly Aurion-designated

### 4.3 Output Form
```
{
  "operator": "Aurion",
  "collapse": "scalar",
  "score": <float>,
  "axis": "<declared_axis>",
  "range": [<min>, <max>],
  "confidence": <float 0.0–1.0>,
  "regime": "<FFF|declared>"
}
```

### 4.4 Layer Behavior

| Layer | Aurion State | Description |
|-------|-------------|-------------|
| **L0** | Latent | Amplitude field present but unmeasured. No axis declared. |
| **L1** | Active / Collapsing | Axis declared by Regime. Amplitude gradient sampled. Score initialized. |
| **L2** | Calibrating | Clarity coefficient applied to raw score. RLCD normalization. Proto-VP confidence weighting. |
| **L3** | Emitting | `score: <float>` emitted. Non-linguistic unless L3 wrapping permitted. |

### 4.5 Regime Alignment
- **Primary:** FFF (Finite Field Framing) — Aurion is native to FFF regimes; axis and bounds are FFF constructs
- **Compatible:** SET — Aurion can score categorical options (confidence weighting)
- **Compatible:** SNR — Aurion operates well under noise; score degrades gracefully with confidence reporting
- **Constrained:** DCO — Aurion can operate but axis declaration is often unstable; score drift expected

### 4.6 Error States
| Condition | Result |
|-----------|--------|
| Axis undeclared | Collapse blocked. Flag: `AURION_NO_AXIS` |
| Amplitude gradient = 0 (flat signal) | Degenerate score (mid-point or null). Flag: `AURION_FLAT` |
| Score exceeds declared range | Clamp applied + warning. Flag: `AURION_OVERFLOW` |
| Regime undeclared | Collapse suspended. Flag: `AURION_NO_REGIME` |

---

## 5. Forci — Binary Decision Operator

### 5.1 Definition
Forci is the **polarity-domain resolver**. When activated, it resolves a resonance state into a binary outcome: yes/no, new/existing, proceed/halt, confirmed/rejected. It does not pick from a list (Freqi) or score on a continuum (Aurion) — it collapses to a single bit.

The name derives from force + bifurcation: the point at which the resonance field must commit to one of two polarities and cannot remain in superposition.

### 5.2 Collapse Condition
Forci collapses when the Declared Regime presents a **binary branch condition** with no viable third state. The resonance signal must be in a state of polarity tension — approaching but not yet committed to one pole.

Collapse requirements:
- Exactly two valid outcome states
- Polarity tension must be present (signal not trivially resolved)
- Regime must be SNR-aligned or explicitly Forci-designated
- No Freqi option space expansion permitted (would degrade to Freqi)

### 5.3 Output Form
```
{
  "operator": "Forci",
  "collapse": "binary",
  "decision": <bool>,
  "polarity": "<positive|negative>",
  "tension": <float 0.0–1.0>,
  "confidence": <float 0.0–1.0>,
  "regime": "<SNR|declared>"
}
```

`tension` measures how close the signal was to the opposite polarity at collapse — high tension (> 0.7) should be flagged for Validator Pulse review.

### 5.4 Layer Behavior

| Layer | Forci State | Description |
|-------|------------|-------------|
| **L0** | Latent | Polarity field present but in superposition. Both states co-exist. |
| **L1** | Active / Collapsing | Regime applies bifurcation constraint. Polarity tension measured. Collapse initiated. |
| **L2** | Calibrating | Tension score finalized. Clarity coefficient adjusts confidence. High-tension cases flagged to proto-VP. |
| **L3** | Emitting | `decision: true/false` emitted. Polarity declared. Non-linguistic. |

### 5.5 Regime Alignment
- **Primary:** SNR (Signal-Noise Resolution) — Forci is native to SNR; noise is the primary driver of polarity tension
- **Compatible:** DCO — Forci operates; tension tends to be high (DCO systems are inherently turbulent)
- **Compatible:** FFF — Forci operates cleanly; bounded fields reduce spurious tension
- **Constrained:** SET — Forci can operate but often degrades to Freqi (SET wants enumeration, not binary)

### 5.6 Error States
| Condition | Result |
|-----------|--------|
| Third state emerges during collapse | Abort Forci, escalate to Freqi. Flag: `FORCI_THIRD_STATE` |
| Tension = 0 (trivial decision) | Collapse allowed but confidence = 1.0 and tension = 0.0. Flag: `FORCI_TRIVIAL` |
| Tension > 0.95 (near-parity) | Collapse suspended pending VP review. Flag: `FORCI_NEAR_PARITY` |
| Regime undeclared | Collapse suspended. Flag: `FORCI_NO_REGIME` |

---

## 6. Flui — Linguistic Wrapping Operator

### 6.1 Definition
Flui is the **emission-domain articulator**. It is categorically different from the other three operators: it does not collapse a resonance state into a structured value — it **wraps an already-collapsed output in natural language** for human-legible emission.

The name derives from fluid: Flui is the formless medium that gives shape to what the other operators have already resolved. Without a prior collapse from Freqi, Aurion, or Forci, Flui has nothing to wrap and cannot emit.

### 6.2 Suppression Rule (L1)
**Flui is suppressed at L1. This is a hard rule, not a soft preference.**

Rationale: At L1, the Declared Regime is enforcing structural constraints. Linguistic wrapping at this layer introduces ambiguity, naturalizes errors, and allows coherence drift to hide behind fluent output. L1 is a precision layer — Flui has no role there.

Violation of this rule produces `FLUI_L1_VIOLATION` — a critical error that invalidates the cycle output.

### 6.3 Re-Entry Condition (L3)
Flui re-enters at L3 **only when** both conditions are met:
1. A prior operator (Freqi, Aurion, or Forci) has successfully collapsed at L1
2. The active Regime explicitly permits linguistic wrapping (not all do)

If both conditions are met, Flui wraps the L1 output in a language-appropriate emission string. It does not modify the underlying structured output — both exist in parallel.

### 6.4 Output Form
```
{
  "operator": "Flui",
  "collapse": "linguistic",
  "wraps": "<Freqi|Aurion|Forci>",
  "source_output": { <prior operator output> },
  "emission": "<natural language string>",
  "language": "<lang_code>",
  "regime_permits_wrapping": true
}
```

### 6.5 Layer Behavior

| Layer | Flui State | Description |
|-------|-----------|-------------|
| **L0** | Latent | Present in substrate. No activation pathway at this layer. |
| **L1** | ❌ **SUPPRESSED** | Hard suppression. Any activation attempt is a critical error. |
| **L2** | Latent | Flui monitors L2 synthesis but does not participate. Observational only. |
| **L3** | Conditional | Active only if prior collapse succeeded AND regime permits. Wraps and emits. |

### 6.6 Regime Alignment
- **Permitted by:** SET (when enumeration result requires explanation), FFF (when score context needs articulation)
- **Conditionally permitted by:** SNR (when decision requires justification for human review)
- **Rarely permitted by:** DCO (turbulent regimes rarely authorize wrapping — drift risk too high)
- **Never permitted at:** L1, regardless of regime

### 6.7 Error States
| Condition | Result |
|-----------|--------|
| Activation attempted at L1 | Critical error. Cycle invalidated. Flag: `FLUI_L1_VIOLATION` |
| No prior L1 collapse | Emission blocked — nothing to wrap. Flag: `FLUI_NO_SOURCE` |
| Regime does not permit wrapping | Emission blocked silently. Flag: `FLUI_REGIME_BLOCKED` |
| Source output is ambiguous | Wrap attempted with confidence penalty. Flag: `FLUI_AMBIGUOUS_SOURCE` |

---

## 7. Cross-Operator Rules

### 7.1 Single-Collapse Rule
**Exactly one operator collapses per RTT cycle at L1.** The Declared Regime specifies which. If two operators attempt simultaneous collapse, the cycle is invalid.

```
valid:   collapse(Freqi) at L1  →  L3 emit
valid:   collapse(Aurion) at L1 →  L3 emit
invalid: collapse(Freqi) + collapse(Aurion) at L1  →  CYCLE_INVALID
```

### 7.2 Flui Dependency Rule
Flui cannot be the designated L1 operator. It has no collapse function of its own — only wrapping. Any regime specification of `operator: Flui` at L1 is a regime misconfiguration.

### 7.3 Escalation Chain
When a primary operator encounters a blocking error state, it may escalate to an adjacent operator per this chain:

```
Freqi TIE        →  Aurion adjudication (score the tied options)
Aurion FLAT      →  Forci adjudication (force binary: above/below midpoint)
Forci THIRD_STATE →  Freqi escalation (expand to categorical)
```

Escalation resets the L1 cycle with the new operator. Maximum one escalation per cycle — circular escalation is a system fault.

### 7.4 Validator Pulse Triggers
The following conditions automatically flag the cycle for proto-VP review (see `t_ValidatorPulse.md`):

| Trigger | Source Operator |
|---------|----------------|
| `FREQI_TIE` | Freqi |
| `AURION_FLAT` | Aurion |
| `AURION_OVERFLOW` | Aurion |
| `FORCI_NEAR_PARITY` (tension > 0.95) | Forci |
| `FLUI_L1_VIOLATION` | Flui |
| Any `confidence < 0.4` | Any |

---

## 8. Full Layer × Operator Matrix

| | **L0** | **L1** | **L2** | **L3** |
|---|---|---|---|---|
| **Freqi** | Latent | ✅ Collapse | Calibrate | Emit `choice` |
| **Aurion** | Latent | ✅ Collapse | Calibrate | Emit `score` |
| **Forci** | Latent | ✅ Collapse | Calibrate | Emit `decision` |
| **Flui** | Latent | ❌ Suppressed | Latent | Conditional wrap |

---

## 9. Regime × Operator Affinity

| Regime | Primary Operator | Secondary | Tertiary | Flui Permitted |
|--------|-----------------|-----------|----------|----------------|
| **SET** (Structural Enumeration Topology) | Freqi | Aurion | Forci | Yes |
| **FFF** (Finite Field Framing) | Aurion | Freqi | Forci | Yes |
| **SNR** (Signal-Noise Resolution) | Forci | Aurion | Freqi | Conditional |
| **DCO** (Dynamic Coherence Oscillation) | Forci | Freqi | Aurion | Rarely |

> Regime affinity does not prohibit non-primary operators — it indicates which operator the regime is *optimized for*. Any operator can be explicitly declared by the active regime.

---

## 10. Operator Signatures in Session Data

When logging to `sessions/*.json` (see `t_Session_Schema.json`), operator behavior is recorded as:

```json
{
  "cycle_id": "<uuid>",
  "timestamp": "<ISO8601>",
  "regime": "SET",
  "operator_declared": "Freqi",
  "operator_collapsed": "Freqi",
  "escalation": null,
  "output": {
    "operator": "Freqi",
    "collapse": "categorical",
    "choice": "<id>",
    "confidence": 0.87,
    "option_count": 4,
    "regime": "SET"
  },
  "flui_wrapped": false,
  "vp_flagged": false,
  "error_flags": []
}
```

If escalation occurred, `escalation` contains the source operator and flag that triggered it.

---

## 11. Cross-References

| Document | Relationship |
|----------|-------------|
| [`t_Index.md`](./t_Index.md) | Module master index — this file listed as P1 |
| [`t_Capture.md`](./t_Capture.md) | Original capture log — operator roles first defined here; this file supersedes on conflict |
| [`t_ValidatorPulse.md`](./t_ValidatorPulse.md) | VP triggers defined in §7.4 above; VP behavior defined there |
| [`t_Session_Schema.json`](./t_Session_Schema.json) | Session log schema — operator output format in §10 above feeds this |
| [`t_FlowMap.md`](./t_FlowMap.md) | L0→L3 pipeline diagram — operator states per layer visualized there |
| [`models.json`](./models.json) | Testing roster — `meta.alignment` field maps to Regime × Operator affinity (§9) |
| [`../spine/dimensional_overlay.md`](../spine/dimensional_overlay.md) | Dimensional topology — upstream context for operator spatial positioning |
| [`../spine/drift_overlay.md`](../spine/drift_overlay.md) | Drift class definitions — intersect with DCO/SNR regime operator behavior |

---

## 12. Build Log

| Date | Action | Author |
|------|--------|--------|
| 2026-09-22 | Operator roles captured in `t_Capture.md` (proto-definitions) | TriadicFrameworks |
| 2026-09-22 | `t_OperatorMap.md` created — full canonical definitions, all 4 operators, all 4 layers, error states, cross-operator rules, regime affinity, VP triggers, session schema | TriadicFrameworks |

---

*Operators do not interpret. They collapse, score, decide, or wrap — nothing more and nothing less.*

