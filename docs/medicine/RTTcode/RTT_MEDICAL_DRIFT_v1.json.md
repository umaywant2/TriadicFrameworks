# ✅ **RTT_MEDICAL_DRIFT_v1.json**  
### *RTTcode Signature — Medical Drift Operator*

---

This RTTcode packet defines the **machine‑readable drift‑detection contract** for the entire medical module.

This JSON must:

- match the structure of your other RTTcode signatures  
- be operator‑first  
- be minimal, canonical, and zero‑drift  
- reflect the tri‑regime medical environment (US, China, UK)  
- encode template drift, semantic drift, translation drift, AI drift, and commercial drift  
- be safe, patient‑appropriate, and structurally aligned with RTT/1  

Below is the **drop‑in ready** RTTcode signature for:

```
RTT_MEDICAL_DRIFT_v1.json
```

---

```json
{
  "rttcode_version": "1.0",
  "operator": "MEDICAL_DRIFT_OPERATOR",
  "module": "medicine",
  "purpose": "Detect structural drift across medical regimes (US clinical, China AI-augmented, UK public-health) including template, semantic, translation, AI, and commercial drift.",

  "inputs": {
    "metadata_packet": "RTT_MEDICAL_METADATA_v1",
    "substrate_packet": "RTT_MEDICAL_SUBSTRATE_v1",
    "regime_packet": "RTT_MEDICAL_REGIME_v1",
    "raw_content": "multi-snapshot, multi-regime medical pages"
  },

  "outputs": {
    "drift_map": {
      "template_drift": "low|medium|high",
      "semantic_drift": "low|medium|high",
      "translation_drift": "none|low|medium|high",
      "ai_drift": "none|low|medium|high",
      "commercial_drift": "none|low|medium|high",
      "regime_drift": "low|medium|high"
    },
    "drift_score": "float_0_to_1",
    "drift_flags": [
      "template_drift_detected",
      "semantic_drift_detected",
      "translation_drift_detected",
      "ai_drift_detected",
      "commercial_drift_detected",
      "regime_drift_detected"
    ]
  },

  "drift_logic": {
    "normalize_substrate": true,
    "compare_snapshots": true,
    "detect_template_changes": true,
    "detect_semantic_variation": true,
    "detect_translation_variance": true,
    "detect_ai_generated_instability": true,
    "detect_commercial_overlays": true,
    "cross_regime_alignment": [
      "clinical_regime",
      "ai_augmented_regime",
      "public_health_regime"
    ],
    "scoring_method": "weighted_drift_across_dimensions"
  },

  "regime_profiles": {
    "clinical_regime": {
      "expected_drift": "low",
      "notes": "Cleveland Clinic stable templates, conservative updates."
    },
    "ai_augmented_regime": {
      "expected_drift": "high",
      "notes": "Ping An mobile-first, translation drift, AI overlays, commercial layers."
    },
    "public_health_regime": {
      "expected_drift": "very_low",
      "notes": "NHS standardized templates, minimal redesign."
    }
  },

  "flags": {
    "template_drift_detected": "boolean",
    "semantic_drift_detected": "boolean",
    "translation_drift_detected": "boolean",
    "ai_drift_detected": "boolean",
    "commercial_drift_detected": "boolean",
    "regime_drift_detected": "boolean"
  },

  "safety": {
    "patient_safe_output": true,
    "no_medical_advice": true,
    "uncertainty_disclosure_required": true,
    "drift_risk_disclosure_required": true
  }
}
```

---

# ✔️ What This RTTcode Signature Achieves

This JSON defines the **entire drift‑detection contract** for the medical module:

- **Template drift** (Ping An high, NHS very low)  
- **Semantic drift** (translation + AI phrasing)  
- **Translation drift** (China‑specific)  
- **AI drift** (Ping An triage overlays)  
- **Commercial drift** (upsells, telemedicine prompts)  
- **Regime drift** (shifts in framing over time)  

It also encodes:

- cross‑regime alignment  
- drift scoring  
- safety constraints  
- machine‑readable flags  
- expected drift profiles per regime  

This is the backbone that allows the synthesis operator to say:

> “This element is unstable — here’s why.”
