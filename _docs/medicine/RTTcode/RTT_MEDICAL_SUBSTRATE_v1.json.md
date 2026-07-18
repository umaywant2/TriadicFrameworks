# ✅ **RTT_MEDICAL_SUBSTRATE_v1.json**  
### *RTTcode Signature — Medical Substrate Operator*

---

This is the **substrate RTTcode signature**, which defines the machine‑readable contract for the MEDICAL_SUBSTRATE_OPERATOR — the operator that determines:

- what the medical content *is made of*  
- how stable it is  
- how much noise it carries  
- how much interference it introduces  
- how safe it is for downstream reasoning  

This signature must be:

- **operator‑first**  
- **minimal**  
- **canonical**  
- **zero‑drift**  
- **aligned with the tri‑regime medical module**  
- **consistent with your other RTTcode files**  

Below is the **drop‑in ready** JSON for:

```
RTT_MEDICAL_SUBSTRATE_v1.json
```

---

```json
{
  "rttcode_version": "1.0",
  "operator": "MEDICAL_SUBSTRATE_OPERATOR",
  "module": "medicine",
  "purpose": "Classify and evaluate the substrate of medical information across regimes (US clinical, China AI-augmented, UK public-health).",

  "inputs": {
    "raw_content": "medical page (html, mobile_html, pdf, image, ocr, mixed)",
    "snapshot_set": "multi-snapshot versions of the same page",
    "language_variants": "multilingual content when present"
  },

  "outputs": {
    "substrate_packet": {
      "substrate_type": "html|mobile_html|pdf|image|ocr|mixed",
      "substrate_stability": "very_high|high|medium|low",
      "substrate_noise": "low|medium|high",
      "layer_interference": "layer_interference_present|layer_interference_absent",
      "accessibility_stability": "very_high|high|medium|low",

      "translation_layer": "present|absent",
      "commercial_layer": "present|absent",
      "ai_overlay_layer": "present|absent"
    },
    "substrate_score": "float_0_to_1",
    "substrate_flags": [
      "substrate_unstable",
      "noise_high",
      "translation_layer_detected",
      "commercial_layer_detected",
      "ai_overlay_detected",
      "ocr_risk"
    ]
  },

  "substrate_logic": {
    "detect_substrate_type": true,
    "detect_noise_layers": true,
    "detect_translation_layers": true,
    "detect_ai_overlays": true,
    "detect_commercial_overlays": true,
    "evaluate_accessibility": true,
    "scoring_method": "weighted_stability_minus_noise"
  },

  "regime_profiles": {
    "clinical_regime": {
      "expected_substrate": "html",
      "expected_noise": "low",
      "expected_interference": "absent",
      "notes": "Cleveland Clinic stable HTML substrate."
    },
    "ai_augmented_regime": {
      "expected_substrate": "mobile_html",
      "expected_noise": "high",
      "expected_interference": "present",
      "notes": "Ping An mobile-first, AI overlays, translation layers, commercial prompts."
    },
    "public_health_regime": {
      "expected_substrate": "html",
      "expected_noise": "low",
      "expected_interference": "absent",
      "notes": "NHS standardized, clarity-first HTML substrate."
    }
  },

  "flags": {
    "substrate_unstable": "boolean",
    "noise_high": "boolean",
    "translation_layer_detected": "boolean",
    "commercial_layer_detected": "boolean",
    "ai_overlay_detected": "boolean",
    "ocr_risk": "boolean"
  },

  "safety": {
    "patient_safe_output": true,
    "no_medical_advice": true,
    "substrate_risk_disclosure_required": true,
    "uncertainty_disclosure_required": true
  }
}
```

---

# ✔️ What This RTTcode Signature Establishes

This JSON defines the **substrate backbone** for the medical module:

### It classifies:
- HTML (Cleveland Clinic, NHS)  
- mobile HTML (Ping An)  
- PDF  
- image  
- OCR  
- mixed substrates  

### It evaluates:
- substrate stability  
- noise levels  
- interference layers  
- accessibility stability  

### It detects:
- translation layers  
- commercial overlays  
- AI overlays  
- OCR risk  

### It encodes regime expectations:
- **US clinical** → stable HTML, low noise  
- **China AI‑augmented** → mobile, high noise, AI overlays  
- **UK public‑health** → very stable HTML, clarity‑first  

This is the contract that allows the drift, continuity, and synthesis operators to trust the input.
