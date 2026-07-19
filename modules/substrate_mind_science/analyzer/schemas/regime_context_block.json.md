# 🧭 SMS Analyzer — Regime Context Block

The **Regime Context Block** stabilizes interpretation across sessions by making structural conditions explicit. It exists to prevent regime blindness, over‑interpretation, and false attribution—especially when data is sparse or load is chronic.

This block is **structural‑first**. Only a small, descriptive subset ever surfaces to students or clinicians.

---

## Purpose

The Regime Context Block answers a single question:

**“Under what structural conditions should this session be interpreted?”**

It does not explain behavior, assign cause, or imply diagnosis.

---

## Design Principles

- Context precedes meaning
- Regimes change interpretation rules
- Stability can exist under compression
- Divergence is informative, not failure
- Observer assumptions are part of the system

---

## Canonical Regime Context Block (Annotated)

```json
{
  "consciousnessRegime": {
    "primary": "Reflective",
    "secondary": ["Immersive"],
    "confidence": 0.78
  },

  "lifeRegimeProfile": {
    "current": "Sustained High Load",
    "baseline": "Adaptive Stability",
    "confidence": 0.64
  },

  "structuralPosture": {
    "orientation": "Stabilizing",
    "flexibility": 0.52,
    "compression": 0.31
  },

  "environmentalContext": {
    "auditoryExposure": {
      "reported": false,
      "duration": null,
      "perceptualRange": null
    }
  },

  "measurementIntegrity": "Green",

  "regimeMismatchFlags": []
}
```

---

## Field Descriptions

### Consciousness Regime
Describes the **state‑dependent rules of experience**.

- Primary regime anchors interpretation
- Secondary regimes allow mixed or transitional states
- Confidence reflects interpretive stability, not certainty

---

### Life Regime Profile
Anchors the session within **long‑running structural conditions**.

- Prevents population‑norm miscomparison
- Distinguishes chronic adaptation from acute change
- Enables meaningful drift analysis across sessions

---

### Structural Posture
Describes how the system is **holding itself together**.

- Orientation — stabilizing, exploratory, defensive
- Flexibility — capacity to absorb change
- Compression — degree of constraint under load

Compression is not pathology.

---

### Environmental Context (Optional)
Activated only when relevant to the scenario.

- Used to rule out overlooked physical contributors
- Never treated as causal explanation
- Artifacts are contextual references only

---

### Measurement Integrity
Indicates how fragile interpretation may be.

- **Green** — stable, low inference
- **Yellow** — assumption‑dependent
- **Red** — inference‑heavy, regime‑sensitive

This field never surfaces in summaries.

---

### Regime Mismatch Flags
Guardrails against observer error.

Flags appear when:
- Triadic models diverge sharply
- Invariants strain under one grammar but resolve under another
- Observer expectations conflict with regime context

Flags are **interpretive cautions**, not findings.

---

## What Surfaces vs What Stays Structural

### Student / Clinician‑Visible
- Primary consciousness posture (plain language)
- High‑level life‑regime orientation
- Overall structural orientation

### Structural‑Only
- Confidence values
- Secondary regimes
- Flexibility and compression metrics
- Measurement integrity
- Regime mismatch flags

This separation preserves clarity without false certainty.

---

## Learning Outcome

Students learn that:
- Context changes meaning
- Stability can coexist with strain
- Interpretation requires humility
- Structure protects against overreach

The Regime Context Block is not an answer.
It is the **frame that makes answers possible**.
