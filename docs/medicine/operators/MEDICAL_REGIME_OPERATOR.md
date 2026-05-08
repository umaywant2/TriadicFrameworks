# **MEDICAL_REGIME_OPERATOR**  
### *RTT Operator — Medicine Module*  
### *Classifying Medical Information by Regime Logic*

---

## **Purpose**

The **MEDICAL_REGIME_OPERATOR** identifies the *medical regime* governing a piece of medical information.  
A regime is not a country — it is a **structural logic**:

- how symptoms are framed  
- how risk is communicated  
- how treatment is prioritized  
- how uncertainty is handled  
- how escalation is defined  
- how the patient is positioned  

This operator determines whether the content follows:

- **clinical regime** (US / Cleveland Clinic)  
- **AI‑augmented commercial regime** (China / Ping An)  
- **public‑health regime** (UK / NHS)  

This classification is essential for continuity, drift, and synthesis.

---

## **What This Operator Detects**

### **1. Regime Logic**

Each regime has a distinct structural fingerprint:

#### **Clinical Regime (US — Cleveland Clinic)**  
- conservative framing  
- physician‑centric  
- symptom → cause → treatment  
- low drift  
- high continuity  
- risk escalation is explicit  

#### **AI‑Augmented Commercial Regime (China — Ping An)**  
- AI triage overlays  
- dynamic symptom mapping  
- commercial prompts  
- mobile‑first structure  
- translation drift  
- high template volatility  

#### **Public‑Health Regime (UK — NHS)**  
- clarity‑first  
- population‑level framing  
- escalation thresholds are standardized  
- extremely low drift  
- minimal commercial influence  

---

### **2. Regime Signals**

The operator identifies regime signals such as:

- **clinical anchors** (US)  
- **AI‑generated suggestions** (China)  
- **public‑health escalation rules** (UK)  
- **commercial overlays** (China)  
- **risk‑first framing** (US)  
- **symptom‑first framing** (China)  
- **action‑first framing** (UK)  

---

### **3. Regime Drift**

Some content shifts regime over time:

- Ping An pages may shift from human‑written → AI‑augmented  
- Cleveland Clinic may update clinical guidelines  
- NHS may update public‑health recommendations  

The operator flags:

- `regime_shift_detected`  
- `regime_stable`  

---

### **4. Regime Coherence**

Coherence measures how consistently the regime logic is applied:

- section ordering  
- risk framing  
- escalation logic  
- treatment hierarchy  
- uncertainty handling  

Coherence levels:

- `high`  
- `medium`  
- `low`  

---

## **Inputs**

The operator accepts:

- raw medical pages  
- multi‑snapshot versions  
- multilingual content  
- AI‑generated triage outputs  
- metadata packets  
- substrate packets  
- drift maps  

---

## **Outputs**

### **1. Regime Classification Packet**

```
{
  "regime": "ai_augmented_regime",
  "regime_coherence": "medium",
  "regime_shift": "regime_shift_detected",
  "regime_signals": [
    "ai_generated_content_present",
    "commercial_overlay_present",
    "mobile_first_structure"
  ]
}
```

### **2. Regime Score (0–1)**

| Score | Meaning |
|-------|---------|
| **0.9–1.0** | Strong, stable regime identity |
| **0.7–0.89** | Mostly stable |
| **0.4–0.69** | Mixed regime signals |
| **0.0–0.39** | Regime instability or shift |

### **3. Regime Flags**

- `clinical_regime_detected`  
- `ai_augmented_regime_detected`  
- `public_health_regime_detected`  
- `regime_shift_detected`  
- `regime_incoherent`  

---

## **Regime Classification Algorithm**

1. **Ingest metadata packet**  
   Substrate, drift, translation stability.

2. **Identify regime signals**  
   Clinical anchors, AI overlays, public‑health framing.

3. **Evaluate framing logic**  
   Symptom‑first, risk‑first, action‑first.

4. **Detect commercial influence**  
   Upsells, telemedicine prompts.

5. **Detect AI augmentation**  
   Dynamic triage, probabilistic scoring.

6. **Assess regime coherence**  
   Consistency across sections.

7. **Detect regime drift**  
   Compare across snapshots.

8. **Produce regime packet**  
   Structured, RTT‑aligned output.

---

## **Examples (Generic)**

### **Cleveland Clinic**
```
regime: clinical_regime
regime_coherence: high
regime_shift: none
regime_signals: ["clinical_anchors_present"]
regime_score: 0.91
```

### **Ping An**
```
regime: ai_augmented_regime
regime_coherence: medium
regime_shift: regime_shift_detected
regime_signals: [
  "ai_generated_content_present",
  "commercial_overlay_present",
  "mobile_first_structure"
]
regime_score: 0.47
```

### **NHS.uk**
```
regime: public_health_regime
regime_coherence: very_high
regime_shift: none
regime_signals: ["public_health_escalation_rules"]
regime_score: 0.96
```

---

## **Why This Operator Matters**

Medical information is not neutral — it is **regime‑shaped**.

This operator reveals:

- why Cleveland Clinic feels conservative  
- why Ping An feels dynamic and commercial  
- why NHS feels clear and standardized  
- why advice differs across countries  
- why drift behaves differently across regimes  

It gives the module the ability to say:

> “This isn’t contradictory — it’s regime‑specific.”

This is the operator that makes the module *intelligent*.
