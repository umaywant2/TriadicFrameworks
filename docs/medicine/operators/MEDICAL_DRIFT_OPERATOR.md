# **MEDICAL_DRIFT_OPERATOR**  
### *RTT Operator — Medicine Module*  
### *Detecting Structural Drift in Medical Information Across Regimes*

---

## **Purpose**

The **MEDICAL_DRIFT_OPERATOR** identifies, classifies, and maps **structural drift** in medical information across:

- time  
- templates  
- languages  
- medical regimes  
- AI‑generated overlays  
- commercial layers  
- mobile vs desktop substrates  

This operator reveals *where* and *how* medical information becomes unstable — and why continuity kernels matter.

---

## **What This Operator Detects**

### **1. Template Drift**
Changes in:

- layout  
- navigation  
- section ordering  
- symptom → cause → treatment flow  
- mobile vs desktop structure  

**Ping An** shows the highest template drift.  
**Cleveland Clinic** and **NHS** show very low drift.

---

### **2. Semantic Drift**
Changes in meaning caused by:

- translation variance (Chinese → English)  
- AI‑generated phrasing  
- SEO‑driven rewriting  
- culturally specific framing  

This is especially important for Ping An’s multilingual substrate.

---

### **3. Regime Drift**
Differences in medical framing across:

| Regime | Drift Pattern |
|--------|---------------|
| **Clinical (US)** | conservative, low drift |
| **AI‑Augmented (China)** | high drift, dynamic content |
| **Public Health (UK)** | extremely low drift |

The operator isolates regime‑specific drift from universal drift.

---

### **4. Commercial Drift**
Changes introduced by:

- upsells  
- telemedicine prompts  
- product suggestions  
- insurance‑linked recommendations  

This is primarily a Ping An phenomenon.

---

### **5. AI‑Generated Drift**
Ping An’s triage system introduces:

- probabilistic symptom mapping  
- dynamic risk scoring  
- non‑deterministic phrasing  

The operator flags AI‑driven instability.

---

### **6. Time‑Series Drift**
Changes across snapshots:

- year‑to‑year  
- pre‑ vs post‑template redesign  
- pre‑ vs post‑AI integration  
- pre‑ vs post‑translation updates  

This is the same logic used in archive_org, but tuned for medical content.

---

## **Inputs**

The operator accepts:

- multi‑snapshot medical pages  
- multi‑regime sources  
- multilingual content  
- AI‑generated triage outputs  
- mobile and desktop variants  

---

## **Outputs**

### **1. Drift Map**
A structural map showing:

- template drift  
- semantic drift  
- regime drift  
- translation drift  
- AI drift  
- commercial drift  

### **2. Drift Score (0–1)**

| Score | Meaning |
|-------|---------|
| **0.9–1.0** | Very low drift (NHS) |
| **0.7–0.89** | Low drift (Cleveland Clinic) |
| **0.4–0.69** | Moderate drift |
| **0.0–0.39** | High drift (Ping An) |

### **3. Drift Flags**

- `template_drift_detected`  
- `semantic_drift_detected`  
- `translation_drift_detected`  
- `ai_drift_detected`  
- `commercial_drift_detected`  
- `regime_drift_detected`  

### **4. Drift Vector**
A directional vector showing *where* drift originates:

```
clinical → ai_augmented
public_health → ai_augmented
ai_augmented → clinical
```

This is used by the synthesis operator.

---

## **Drift Detection Algorithm**

1. **Normalize substrate**  
   Remove ads, AI overlays, translation artifacts.

2. **Compare snapshots**  
   Identify structural changes across time.

3. **Compare regimes**  
   Align US → China → UK medical structures.

4. **Detect template drift**  
   Layout, navigation, section ordering.

5. **Detect semantic drift**  
   Meaning changes across languages or AI phrasing.

6. **Detect commercial drift**  
   Identify upsells and telemedicine prompts.

7. **Detect AI drift**  
   Flag dynamic triage suggestions.

8. **Compute drift score**  
   Weighted by severity and frequency.

9. **Produce drift map + flags**  
   Structured, RTT‑aligned output.

---

## **Example (Generic)**

### **Cleveland Clinic**
```
template_drift: low
semantic_drift: low
translation_drift: none
ai_drift: none
commercial_drift: none
regime_drift: low
drift_score: 0.85
```

### **Ping An**
```
template_drift: high
semantic_drift: medium
translation_drift: high
ai_drift: high
commercial_drift: medium
regime_drift: high
drift_score: 0.32
```

### **NHS.uk**
```
template_drift: very_low
semantic_drift: low
translation_drift: none
ai_drift: none
commercial_drift: none
regime_drift: low
drift_score: 0.92
```

---

## **Why This Operator Matters**

Medical information is **not stable** across:

- countries  
- languages  
- templates  
- commercial incentives  
- AI‑generated overlays  

Patients experience this as:

- conflicting advice  
- inconsistent terminology  
- unclear escalation thresholds  
- contradictory risk framing  

The **MEDICAL_DRIFT_OPERATOR** exposes these instabilities so the **continuity operator** can extract what is *actually stable*.

This is the operator that makes the module *trustworthy*.
