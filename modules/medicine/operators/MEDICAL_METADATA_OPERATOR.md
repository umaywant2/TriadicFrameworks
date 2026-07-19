# **MEDICAL_METADATA_OPERATOR**  
### *RTT Operator — Medicine Module*  
### *Substrate • Regime • Drift Sensitivity • Coherence*

---

## **Purpose**

The **MEDICAL_METADATA_OPERATOR** extracts the *structural metadata* of medical information across different regimes (US, China, UK).  
It identifies:

- substrate type  
- medical regime  
- drift sensitivity  
- coherence level  
- translation stability  
- AI‑augmentation flags  
- commercial influence markers  

This operator provides the **metadata backbone** used by all other medical operators.

---

## **What This Operator Detects**

### **1. Substrate Type**
Medical pages vary widely in substrate:

- **HTML** (Cleveland Clinic, NHS)  
- **Mobile‑first app substrate** (Ping An)  
- **AI‑generated triage overlays**  
- **PDFs** (clinical guidelines)  
- **Image‑embedded text** (common in Chinese medical sites)  

The operator classifies substrate as:

- `html`  
- `mobile_html`  
- `pdf`  
- `image`  
- `ocr`  
- `mixed`  

---

### **2. Medical Regime Classification**

Each source belongs to a distinct medical regime:

| Source | Regime | Notes |
|--------|--------|-------|
| **Cleveland Clinic (US)** | Clinical | Conservative, low drift |
| **Ping An (China)** | AI‑Augmented Commercial | High drift, multilingual |
| **NHS.uk (UK)** | Public Health | Extremely stable, clarity‑first |

The operator assigns:

- `clinical_regime`  
- `ai_augmented_regime`  
- `public_health_regime`  

---

### **3. Drift Sensitivity**

Drift sensitivity is determined by:

- template volatility  
- translation variability  
- AI‑generated content  
- commercial overlays  
- mobile‑first redesign frequency  

Expected patterns:

- **Cleveland Clinic:** low drift  
- **NHS.uk:** very low drift  
- **Ping An:** high drift  

Drift levels:

- `low`  
- `medium`  
- `high`  

---

### **4. Coherence Level**

Coherence measures how internally consistent the medical information is across:

- time  
- templates  
- languages  
- regimes  

Coherence levels:

- `high`  
- `medium`  
- `low`  

---

### **5. Translation Stability (China‑specific)**

Ping An introduces translation drift:

- Chinese → English  
- medical terminology variance  
- AI‑generated phrasing  

The operator flags:

- `translation_stable`  
- `translation_unstable`  
- `translation_high_drift`  

---

### **6. Commercial Influence Markers**

Ping An includes:

- upsells  
- telemedicine prompts  
- product suggestions  

The operator flags:

- `commercial_overlay_present`  
- `commercial_overlay_absent`  

---

### **7. AI‑Augmentation Flags**

Ping An’s triage system introduces:

- AI‑generated suggestions  
- probabilistic symptom mapping  
- dynamic risk scoring  

The operator flags:

- `ai_generated_content_present`  
- `ai_generated_content_absent`  

---

## **Inputs**

The operator accepts:

- raw medical pages  
- multi‑snapshot versions  
- multilingual content  
- AI‑augmented triage outputs  
- public‑health guidance pages  

---

## **Outputs**

### **1. Metadata Packet**

A structured JSON‑like output:

```
{
  "substrate": "html",
  "regime": "clinical_regime",
  "drift_sensitivity": "low",
  "coherence": "high",
  "translation_stability": "translation_stable",
  "commercial_overlay": "commercial_overlay_absent",
  "ai_augmentation": "ai_generated_content_absent"
}
```

### **2. Metadata Score**

A 0–1 score indicating metadata stability.

### **3. Metadata Flags**

Flags for:

- drift risk  
- translation instability  
- commercial influence  
- AI augmentation  

---

## **Metadata Extraction Algorithm**

1. **Identify substrate**  
   Detect HTML, mobile HTML, PDF, image, OCR, or mixed.

2. **Classify regime**  
   US → clinical  
   China → AI‑augmented commercial  
   UK → public health  

3. **Assess drift sensitivity**  
   Based on template volatility and language stability.

4. **Evaluate coherence**  
   Check internal consistency across sections.

5. **Detect translation drift**  
   Chinese → English variance.

6. **Detect commercial overlays**  
   Ads, upsells, telemedicine prompts.

7. **Detect AI augmentation**  
   Triage suggestions, dynamic scoring.

8. **Produce metadata packet**  
   Structured, stable, RTT‑aligned.

---

## **Example (Generic)**

For a Cleveland Clinic page:

```
substrate: html
regime: clinical_regime
drift_sensitivity: low
coherence: high
translation_stability: translation_stable
commercial_overlay: commercial_overlay_absent
ai_augmentation: ai_generated_content_absent
```

For a Ping An page:

```
substrate: mobile_html
regime: ai_augmented_regime
drift_sensitivity: high
coherence: medium
translation_stability: translation_high_drift
commercial_overlay: commercial_overlay_present
ai_augmentation: ai_generated_content_present
```

For an NHS page:

```
substrate: html
regime: public_health_regime
drift_sensitivity: low
coherence: high
translation_stability: translation_stable
commercial_overlay: commercial_overlay_absent
ai_augmentation: ai_generated_content_absent
```

---

## **Why This Operator Matters**

Medical information is only as reliable as its metadata.

This operator:

- anchors the entire medical module  
- enables drift‑bounded interpretation  
- supports cross‑regime comparison  
- filters substrate noise  
- stabilizes multilingual content  
- identifies commercial or AI‑generated distortions  

It is the **foundation** for all downstream medical reasoning.
