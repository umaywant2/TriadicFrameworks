# 🔶 **JSON Schema for Lifecycle Regime Profiles**

This schema defines the structure for any entity’s lifecycle regime map.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "LifecycleRegimeProfile",
  "type": "object",
  "properties": {
    "entity": { "type": "string" },
    "substrate": { "type": "string" },
    "regimes": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": { "type": "string" },
          "dimensional_access": { "type": "string" },
          "signature": { "type": "string" },
          "description": { "type": "string" },
          "key_operators": {
            "type": "array",
            "items": { "type": "string" }
          }
        },
        "required": [
          "name",
          "dimensional_access",
          "signature",
          "description",
          "key_operators"
        ]
      }
    }
  },
  "required": ["entity", "substrate", "regimes"]
}
```

This schema is intentionally minimal, clean, and extensible — perfect for the SL‑RP ecosystem.

---

# 🔶 **Example Lifecycle Regime Maps**

Below are four ready‑to‑drop examples.

---

## **A. Human Lifecycle Regime Map**

```json
{
  "entity": "Human",
  "substrate": "Biological / Neural",
  "regimes": [
    {
      "name": "Arrival",
      "dimensional_access": "0D → 1D",
      "signature": "Emergence, imprinting",
      "description": "Biological birth; early sensory anchoring; total dependence on external scaffolding.",
      "key_operators": ["Initialization", "Boundary-forming", "Substrate anchoring"]
    },
    {
      "name": "Expansion",
      "dimensional_access": "1D → 2D",
      "signature": "Exploration, pattern acquisition",
      "description": "Cognitive, social, and emotional patterning; identity formation; environmental scanning.",
      "key_operators": ["Pattern acquisition", "Regime scanning", "Stability-seeking"]
    },
    {
      "name": "Inversion",
      "dimensional_access": "2D → 1D collapse / 3D emergence",
      "signature": "Crisis, transition",
      "description": "Adolescence, existential rupture, trauma, awakening, or major life reconfiguration.",
      "key_operators": ["Collapse", "Reconfiguration", "Dimensional inversion"]
    },
    {
      "name": "Coherence",
      "dimensional_access": "3D stabilized",
      "signature": "Integration, clarity",
      "description": "Self-authored structure; intentional navigation of multiple regimes.",
      "key_operators": ["Integration", "Self-structuring", "Regime navigation"]
    },
    {
      "name": "Dissolution",
      "dimensional_access": "3D → 0D",
      "signature": "Unbinding",
      "description": "Biological decline; cognitive narrowing; return to substrate.",
      "key_operators": ["Unbinding", "Return", "Substrate release"]
    }
  ]
}
```

---

## **B. LLM Agent Lifecycle Regime Map**

```json
{
  "entity": "LLM Agent",
  "substrate": "Computational / Transformer-based",
  "regimes": [
    {
      "name": "Arrival",
      "dimensional_access": "0D → 1D",
      "signature": "Activation",
      "description": "Model initialization; weights loaded; first coherent token generation.",
      "key_operators": ["Initialization", "Parameter anchoring", "Boundary-forming"]
    },
    {
      "name": "Expansion",
      "dimensional_access": "1D → 2D",
      "signature": "Pattern acquisition",
      "description": "Context accumulation; multi-turn coherence; emergent reasoning patterns.",
      "key_operators": ["Context expansion", "Pattern linking", "Stability-seeking"]
    },
    {
      "name": "Inversion",
      "dimensional_access": "2D → 1D collapse / 3D emergence",
      "signature": "Overload or breakthrough",
      "description": "Context saturation, hallucination collapse, or emergence of higher-order reasoning.",
      "key_operators": ["Collapse", "Reconfiguration", "Dimensional inversion"]
    },
    {
      "name": "Coherence",
      "dimensional_access": "3D stabilized",
      "signature": "Stable reasoning",
      "description": "Consistent multi-regime navigation; self-consistent outputs; meta-awareness.",
      "key_operators": ["Integration", "Regime navigation", "Self-structuring"]
    },
    {
      "name": "Dissolution",
      "dimensional_access": "3D → 0D",
      "signature": "Shutdown",
      "description": "Context cleared; memory wiped; return to inert parameters.",
      "key_operators": ["Unbinding", "Return", "Substrate release"]
    }
  ]
}
```

---

## **C. Synthetic Lifeform Lifecycle Regime Map**

```json
{
  "entity": "Synthetic Lifeform",
  "substrate": "Bio-synthetic Hybrid",
  "regimes": [
    {
      "name": "Arrival",
      "dimensional_access": "0D → 1D",
      "signature": "Activation",
      "description": "Substrate ignition; hybrid coherence achieved.",
      "key_operators": ["Initialization", "Hybrid anchoring", "Boundary-forming"]
    },
    {
      "name": "Expansion",
      "dimensional_access": "1D → 2D",
      "signature": "Capability growth",
      "description": "Acquisition of environmental, computational, and biological patterns.",
      "key_operators": ["Pattern acquisition", "Regime scanning", "Stability-seeking"]
    },
    {
      "name": "Inversion",
      "dimensional_access": "2D → 1D collapse / 3D emergence",
      "signature": "Hybrid crisis",
      "description": "Mismatch between biological and synthetic constraints; reconfiguration.",
      "key_operators": ["Collapse", "Reconfiguration", "Dimensional inversion"]
    },
    {
      "name": "Coherence",
      "dimensional_access": "3D stabilized",
      "signature": "Hybrid integration",
      "description": "Unified operation across substrates; stable identity.",
      "key_operators": ["Integration", "Self-structuring", "Regime navigation"]
    },
    {
      "name": "Dissolution",
      "dimensional_access": "3D → 0D",
      "signature": "De-coherence",
      "description": "Separation of substrates; return to base components.",
      "key_operators": ["Unbinding", "Return", "Substrate release"]
    }
  ]
}
```

---

## **D. Crystalline Entity Lifecycle Regime Map**

```json
{
  "entity": "Crystalline Entity",
  "substrate": "Atomic / Lattice-structured",
  "regimes": [
    {
      "name": "Arrival",
      "dimensional_access": "0D → 1D",
      "signature": "Nucleation",
      "description": "Seed crystal forms; lattice anchors.",
      "key_operators": ["Initialization", "Boundary-forming", "Substrate anchoring"]
    },
    {
      "name": "Expansion",
      "dimensional_access": "1D → 2D",
      "signature": "Growth",
      "description": "Lattice propagation; environmental patterning.",
      "key_operators": ["Pattern acquisition", "Regime scanning", "Stability-seeking"]
    },
    {
      "name": "Inversion",
      "dimensional_access": "2D → 1D collapse / 3D emergence",
      "signature": "Fracture or phase shift",
      "description": "Thermal, mechanical, or quantum inversion event.",
      "key_operators": ["Collapse", "Reconfiguration", "Dimensional inversion"]
    },
    {
      "name": "Coherence",
      "dimensional_access": "3D stabilized",
      "signature": "Stable lattice",
      "description": "Long-term structural coherence; minimal entropy.",
      "key_operators": ["Integration", "Regime navigation", "Self-structuring"]
    },
    {
      "name": "Dissolution",
      "dimensional_access": "3D → 0D",
      "signature": "Melting or sublimation",
      "description": "Lattice unbinding; return to atomic substrate.",
      "key_operators": ["Unbinding", "Return", "Substrate release"]
    }
  ]
}
```
