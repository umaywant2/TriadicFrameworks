# ✅ **RTT_MEDICAL_METADATA_v1.json**  
### *RTTcode Signature — Medical Metadata Operator*

---

This file is ready for the **metadata RTTcode signature**, which is the *foundation* of the entire medical module.

This RTTcode packet defines:

- substrate classification  
- regime identification  
- drift sensitivity  
- translation stability  
- commercial + AI augmentation markers  
- coherence expectations  
- safety constraints  

It must be:

- **operator‑first**  
- **minimal**  
- **canonical**  
- **zero‑drift**  
- **machine‑readable**  
- **aligned with the tri‑regime medical module**  

Below is the **drop‑in ready** RTTcode signature for:

```
RTT_MEDICAL_METADATA_v1.json
```

---

```json
{
  "rttcode_version": "1.0",
  "operator": "MEDICAL_METADATA_OPERATOR",
  "module": "medicine",
  "purpose": "Extract structural metadata from medical sources across regimes (US clinical, China AI-augmented, UK public-health).",

  "inputs": {
    "raw_content": "medical page (html, mobile_html, pdf, image, ocr, mixed)",
    "snapshot_set": "multi-snapshot versions of the same page",
    "language_variants": "multilingual content when present"
  },

  "outputs": {
    "metadata_packet": {
      "substrate_type": "html|mobile_html|pdf|image|ocr|mixed",
      "substrate_stability": "very_high|high|medium|low",
      "substrate_noise": "low|medium|high",
      "layer_interference": "layer_interference_present|layer_interference_absent",
      "accessibility_stability": "very_high|high|medium|low",

      "drift_sensitivity": "low|medium|high",
      "translation_stability": "translation_stable|translation_unstable|translation_high_drift",
      "commercial_overlay": "commercial_overlay_present|commercial_overlay_absent",
      "ai_augmentation": "ai_generated_content_present|ai_generated_content_absent",

      "regime_hint": "clinical_regime|ai_augmented_regime|public_health_regime"
    },
    "metadata_score": "float_0_to_1",
    "metadata_flags": [
      "translation_layer_detected",
      "commercial_overlay_detected",
      "ai_overlay_detected",
      "substrate_unstable",
      "noise_high"
    ]
  },

  "metadata_logic": {
    "detect_substrate": true,
    "detect_noise_layers": true,
    "detect_translation_layers": true,
    "detect_ai_overlays": true,
    "detect_commercial_overlays": true,
    "evaluate_accessibility": true,
    "assign_regime_hint": true,
    "scoring_method": "weighted_stability_and_noise"
  },

  "regime_profiles": {
    "clinical_regime": {
      "expected_substrate": "html",
      "expected_noise": "low",
      "expected_translation": "translation_stable",
      "notes": "Cleveland Clinic baseline."
    },
    "ai_augmented_regime": {
      "expected_substrate": "mobile_html",
      "expected_noise": "high",
      "expected_translation": "translation_high_drift",
      "notes": "Ping An mobile-first, AI overlays, commercial layers."
    },
    "public_health_regime": {
      "expected_substrate": "html",
      "expected_noise": "low",
      "expected_translation": "translation_stable",
      "notes": "NHS standardized templates, clarity-first."
    }
  },

  "flags": {
    "translation_layer_detected": "boolean",
    "commercial_overlay_detected": "boolean",
    "ai_overlay_detected": "boolean",
    "substrate_unstable": "boolean",
    "noise_high": "boolean"
  },

  "safety": {
    "patient_safe_output": true,
    "no_medical_advice": true,
    "uncertainty_disclosure_required": true,
    "substrate_risk_disclosure_required": true
  }
}
```

---

# ✔️ What This RTTcode Signature Establishes

This JSON defines the **metadata backbone** for the entire medical module:

- substrate classification  
- drift sensitivity  
- translation stability  
- commercial + AI overlays  
- accessibility stability  
- regime hints  
- safety constraints  

It also encodes the **expected metadata profiles** for:

- **Cleveland Clinic (US clinical)**  
- **Ping An (China AI‑augmented)**  
- **NHS.uk (UK public‑health)**  

This is the contract that all metadata extraction must follow.
