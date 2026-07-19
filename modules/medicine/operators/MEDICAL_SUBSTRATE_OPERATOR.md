# **MEDICAL_SUBSTRATE_OPERATOR**  
### *RTT Operator — Medicine Module*  
### *Substrate Classification • Stability • Layer Interference*

---

## **Purpose**

The **MEDICAL_SUBSTRATE_OPERATOR** identifies and evaluates the *substrate* of medical information across different regimes.  
Medical content is unusually sensitive to substrate because:

- ads distort meaning  
- mobile templates reorder clinical logic  
- AI overlays introduce dynamic content  
- translation layers create semantic drift  
- PDF vs HTML changes continuity  
- image‑embedded text breaks accessibility  

This operator ensures that downstream reasoning (continuity, drift, synthesis) is based on **clean, substrate‑aware input**.

---

## **What This Operator Detects**

### **1. Substrate Type**

The operator classifies medical content into one of the following:

- `html` — standard web pages (Cleveland Clinic, NHS)  
- `mobile_html` — mobile‑first, dynamic templates (Ping An)  
- `pdf` — clinical guidelines, static documents  
- `image` — screenshots, infographics, embedded text  
- `ocr` — extracted text from images  
- `mixed` — combinations of the above  

This classification is foundational for drift and continuity analysis.

---

### **2. Substrate Stability**

Substrate stability measures how likely the substrate is to:

- preserve structure  
- preserve meaning  
- resist drift  
- resist commercial interference  
- resist translation distortion  

Expected patterns:

| Source | Stability |
|--------|-----------|
| **Cleveland Clinic** | high |
| **NHS.uk** | very high |
| **Ping An** | low–medium |

---

### **3. Substrate Noise**

Noise includes:

- ads  
- trackers  
- telemedicine prompts  
- product suggestions  
- AI triage overlays  
- SEO‑driven blocks  
- mobile‑only reorderings  

The operator flags:

- `noise_low`  
- `noise_medium`  
- `noise_high`  

Ping An often triggers `noise_high`.

---

### **4. Substrate Layer Interference**

This detects when substrate layers interfere with medical meaning:

- mobile templates reorder symptom → cause → treatment  
- AI overlays inject dynamic suggestions  
- translation layers alter phrasing  
- ads interrupt clinical flow  
- image‑embedded text breaks continuity  

The operator flags:

- `layer_interference_present`  
- `layer_interference_absent`  

---

### **5. Accessibility Stability**

Accessibility affects structural clarity:

- alt‑text presence  
- heading hierarchy  
- semantic HTML  
- screen‑reader compatibility  

NHS is strongest here.  
Ping An is weakest.

---

## **Inputs**

The operator accepts:

- raw medical pages  
- mobile and desktop variants  
- PDFs  
- images  
- OCR text  
- AI‑augmented triage overlays  

---

## **Outputs**

### **1. Substrate Packet**

A structured metadata output:

```
{
  "substrate_type": "mobile_html",
  "substrate_stability": "medium",
  "substrate_noise": "high",
  "layer_interference": "layer_interference_present",
  "accessibility_stability": "low"
}
```

### **2. Substrate Score (0–1)**

| Score | Meaning |
|-------|---------|
| **0.9–1.0** | Very stable (NHS) |
| **0.7–0.89** | Stable (Cleveland Clinic) |
| **0.4–0.69** | Moderate stability |
| **0.0–0.39** | Unstable (Ping An mobile) |

### **3. Substrate Flags**

- `substrate_unstable`  
- `noise_high`  
- `translation_layer_detected`  
- `ai_overlay_detected`  
- `commercial_layer_detected`  
- `ocr_risk`  

---

## **Substrate Evaluation Algorithm**

1. **Identify substrate type**  
   HTML, mobile HTML, PDF, image, OCR, mixed.

2. **Detect noise layers**  
   Ads, AI overlays, commercial prompts.

3. **Assess stability**  
   Based on structure, consistency, and template volatility.

4. **Detect layer interference**  
   Reordering, injected content, translation drift.

5. **Evaluate accessibility**  
   Semantic HTML, alt‑text, heading structure.

6. **Compute substrate score**  
   Weighted by stability and noise.

7. **Produce substrate packet**  
   Structured, RTT‑aligned output.

---

## **Examples (Generic)**

### **Cleveland Clinic**
```
substrate_type: html
substrate_stability: high
substrate_noise: low
layer_interference: absent
accessibility_stability: high
substrate_score: 0.88
```

### **Ping An**
```
substrate_type: mobile_html
substrate_stability: medium
substrate_noise: high
layer_interference: present
accessibility_stability: low
substrate_score: 0.41
```

### **NHS.uk**
```
substrate_type: html
substrate_stability: very_high
substrate_noise: low
layer_interference: absent
accessibility_stability: very_high
substrate_score: 0.95
```

---

## **Why This Operator Matters**

Medical information is **not substrate‑neutral**.

Substrate determines:

- how meaning is preserved  
- how drift propagates  
- how continuity kernels survive  
- how AI overlays distort content  
- how translation layers alter semantics  
- how patients interpret risk  

The **MEDICAL_SUBSTRATE_OPERATOR** ensures that all downstream reasoning is based on **clean, stable, substrate‑aware input**.

This is the operator that makes the module *structurally safe*.
