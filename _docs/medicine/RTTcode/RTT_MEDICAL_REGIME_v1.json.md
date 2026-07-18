# ✅ **RTT_MEDICAL_REGIME_v1.json**  
### *RTTcode Signature — Medical Regime Operator*

---

This RTTcode packet is the **regime‑classification contract** for the entire medical module — the JSON signature that defines how the MEDICAL_REGIME_OPERATOR identifies:

- clinical regime (US / Cleveland Clinic)  
- AI‑augmented commercial regime (China / Ping An)  
- public‑health regime (UK / NHS)  

This signature must be:

- operator‑first  
- minimal  
- canonical  
- zero‑drift  
- machine‑readable  
- aligned with the tri‑regime structure  
- consistent with your other RTTcode files  

Below is the **drop‑in ready** RTTcode signature for:

```
RTT_MEDICAL_REGIME_v1.json
```

---

```json
{
  "rttcode_version": "1.0",
  "operator": "MEDICAL_REGIME_OPERATOR",
  "module": "medicine",
  "purpose": "Classify medical information into structural regimes (clinical, AI-augmented commercial, public-health) and detect regime coherence, signals, and shifts.",

  "inputs": {
    "metadata_packet": "RTT_MEDICAL_METADATA_v1",
    "substrate_packet": "RTT_MEDICAL_SUBSTRATE_v1",
    "drift_packet": "RTT_MEDICAL_DRIFT_v1",
    "raw_content": "medical page content across regimes and snapshots"
  },

  "outputs": {
    "regime_packet": {
      "regime": "clinical_regime|ai_augmented_regime|public_health_regime",
      "regime_coherence": "high|medium|low",
      "regime_shift": "regime_shift_detected|none",
      "regime_signals": "list"
    },
    "regime_score": "float_0_to_1",
    "regime_flags": [
      "clinical_regime_detected",
      "ai_augmented_regime_detected",
      "public_health_regime_detected",
      "regime_shift_detected",
      "regime_incoherent"
    ]
  },

  "regime_logic": {
    "detect_regime_signals": true,
    "evaluate_framing_logic": true,
    "detect_commercial_overlays": true,
    "detect_ai_augmentation": true,
    "detect_public_health_structure": true,
    "assess_regime_coherence": true,
    "detect_regime_shift": true,
    "scoring_method": "weighted_regime_signal_strength"
  },

  "regime_profiles": {
    "clinical_regime": {
      "signals": [
        "clinical_anchors_present",
        "risk_escalation_explicit",
        "symptom_cause_treatment_structure"
      ],
      "expected_coherence": "high",
      "notes": "Cleveland Clinic baseline."
    },
    "ai_augmented_regime": {
      "signals": [
        "ai_generated_content_present",
        "commercial_overlay_present",
        "mobile_first_structure",
        "translation_layer_detected"
      ],
      "expected_coherence": "medium",
      "notes": "Ping An high drift, AI overlays, commercial layers."
    },
    "public_health_regime": {
      "signals": [
        "public_health_escalation_rules",
        "clarity_first_structure",
        "population_level_risk_framing",
        "standardized_action_paths"
      ],
      "expected_coherence": "very_high",
      "notes": "NHS standardized templates, clarity-first."
    }
  },

  "flags": {
    "clinical_regime_detected": "boolean",
    "ai_augmented_regime_detected": "boolean",
    "public_health_regime_detected": "boolean",
    "regime_shift_detected": "boolean",
    "regime_incoherent": "boolean"
  },

  "safety": {
    "patient_safe_output": true,
    "no_medical_advice": true,
    "uncertainty_disclosure_required": true,
    "regime_difference_disclosure_required": true
  }
}
```

---

# ✔️ What This RTTcode Signature Establishes

This JSON defines the **structural logic** of medical regimes:

### **Clinical Regime (US / Cleveland Clinic)**
- conservative  
- physician‑centric  
- stable templates  
- explicit escalation logic  

### **AI‑Augmented Commercial Regime (China / Ping An)**
- AI triage overlays  
- translation drift  
- commercial prompts  
- mobile‑first volatility  

### **Public‑Health Regime (UK / NHS)**
- clarity‑first  
- standardized escalation rules  
- extremely low drift  
- population‑level framing  

It also encodes:

- regime signals  
- regime coherence  
- regime shifts  
- safety constraints  
- machine‑readable flags  

This is the contract that allows the synthesis operator to say:

> “This difference is not a contradiction — it is regime‑specific.”
