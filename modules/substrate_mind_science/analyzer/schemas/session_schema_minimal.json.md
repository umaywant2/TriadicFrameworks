# 📐 SMS Analyzer — Minimal Session Schema

This document defines the **minimal, canonical session schema** used by the SMS Analyzer for student learning in the RTT NoS sandbox. It is intentionally compact, readable, and extensible.

The schema is designed to:
- support cross‑session comparison,
- preserve regime context,
- enable triadic integration,
- and remain legible to both humans and higher‑order reasoning systems.

This is **not** a data capture specification. Values are illustrative and relative.

---

## Design Intent

- One session = one structural snapshot
- No single field is decisive
- Context stabilizes interpretation
- Extensions attach cleanly without mutation

This schema is the **backbone** from which per‑sense, per‑operator, and per‑integration views are derived.

---

## Minimal Session Schema (Annotated)

```json
{
  "sessionId": "YYYY-MM-DD-XX",
  "scenario": "Chronic Load Adaptation",

  "sensoryVectors": {
    "smell":   { "R": 0.2, "E": 0.6, "M": 0.5, "C": 0.2, "G": 0.8, "P": 0.9 },
    "sight":   { "R": 0.5, "E": 0.6, "M": 0.5, "C": 0.8, "G": 0.5, "P": 0.6 },
    "hearing": { "R": 0.5, "E": 0.6, "M": 0.5, "C": 0.8, "G": 0.5, "P": 0.6 },
    "touch":   { "R": 0.3, "E": 0.6, "M": 0.5, "C": 0.4, "G": 0.8, "P": 0.9 },
    "taste":   { "R": 0.2, "E": 0.6, "M": 0.5, "C": 0.2, "G": 0.8, "P": 0.9 }
  },

  "triadicIntegration": {
    "dominantSense": {
      "sense": "sight",
      "wholeMindState": "Stable under load"
    },
    "weightedModel": {
      "wholeMindState": "Sustained tension, adaptive"
    },
    "invariantDriven": {
      "primaryInvariant": "Load–Coherence Stability",
      "wholeMindState": "Compressed but coherent"
    }
  },

  "regimeContext": {
    "consciousnessRegime": {
      "primary": "Reflective",
      "confidence": 0.74
    },
    "lifeRegimeProfile": {
      "current": "Sustained High Load",
      "baseline": "Adaptive Stability"
    },
    "structuralPosture": {
      "orientation": "Stabilizing",
      "flexibility": 0.48,
      "compression": 0.42
    },
    "measurementIntegrity": "Green",
    "regimeMismatchFlags": []
  },

  "studentSummary": {
    "wholeMindState": "Stable under sustained load",
    "primaryPosture": "Reflective",
    "trajectory": "Stable",
    "keyContributors": ["Sight", "Hearing"]
  }
}
```

---

## Field Notes

- **sensoryVectors**  
  Relative operator values per sense. Precision is not required; comparison is.

- **triadicIntegration**  
  All three models are always present. Divergence is informative.

- **regimeContext**  
  Structural layer that stabilizes interpretation. Most fields do not surface.

- **studentSummary**  
  The only layer intended for immediate orientation.

---

## Extension Points

The minimal schema supports clean attachment of optional modules:

- `environmentalContext`
- `aiAugmentationContext`
- `longitudinalDrift`
- `observerNotes`

Extensions must **not** alter existing fields.

---

## Learning Reminder

This schema teaches students:
- how structure is assembled,
- why context matters,
- and how restraint improves reasoning.

It is a scaffold, not a verdict.
