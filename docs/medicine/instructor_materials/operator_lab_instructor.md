# **RTT Medical Operator Lab — Instructor Version**  
### *Instructor Materials for the Tri‑Regime Medical Module*  
### *RTT/1‑Aligned • Zero Drift • Structural • Student‑Safe*

---

## **Instructor Overview**

This lab teaches students how to run the five medical operators:

1. **MEDICAL_METADATA_OPERATOR**  
2. **MEDICAL_DRIFT_OPERATOR**  
3. **MEDICAL_SUBSTRATE_OPERATOR**  
4. **MEDICAL_REGIME_OPERATOR**  
5. **MEDICAL_CONTINUITY_OPERATOR**  
6. **MEDICAL_SYNTHESIS_OPERATOR** (capstone)

Students work with **three medical regimes**:

- **Cleveland Clinic (US clinical)**  
- **Ping An Good Doctor (China AI‑augmented)**  
- **NHS.uk (UK public‑health)**  

The goal is to teach:

- drift awareness  
- substrate literacy  
- regime differences  
- continuity kernel extraction  
- patient‑safe synthesis  

Students **never** produce medical advice.  
They produce **structural clarity**.

---

## **Instructor Notes (Global)**

- Students must work with **structural elements only** (symptoms, risk factors, red flags, escalation logic).  
- Students must **never** copy text from real medical pages.  
- Students must use the **example JSON packets** provided in `/docs/medicine/examples/`.  
- Students must treat Ping An as **high‑drift**, **translation‑unstable**, **AI‑augmented**, and **commercially influenced**.  
- Students must treat NHS as **very low drift**, **clarity‑first**, and **public‑health oriented**.  
- Students must treat Cleveland Clinic as **clinical baseline**.  
- Students must always disclose uncertainty and escalation indicators.  
- Students must never collapse regime differences into a single narrative.  
- Students must always identify drift sources before synthesizing.

---

# **Lab Structure (Instructor Version)**

Each step below includes:

- **Student Task**  
- **Instructor Expectations**  
- **Common Pitfalls**  
- **Grading Notes**

---

# **STEP 1 — MEDICAL_METADATA_OPERATOR**  
### *Identify substrate, noise, translation layers, AI overlays, commercial layers.*

---

### **Student Task**

Students ingest the three example JSON files and extract:

- substrate type  
- substrate stability  
- noise level  
- translation stability  
- commercial overlays  
- AI augmentation  
- accessibility stability  
- drift sensitivity  
- regime hint  

### **Instructor Expectations**

Students should correctly identify:

| Regime | Expected Metadata |
|--------|------------------|
| **Cleveland Clinic** | html, low noise, stable, no overlays |
| **Ping An** | mobile_html, high noise, translation drift, AI overlays, commercial layers |
| **NHS** | html, very low noise, stable, clarity‑first |

### **Common Pitfalls**

- Treating Ping An as stable  
- Missing translation drift  
- Missing commercial overlays  
- Assuming all HTML is equal  
- Forgetting accessibility stability  

### **Grading Notes**

Full credit requires:

- correct substrate classification  
- correct noise identification  
- correct overlay detection  
- correct regime hint  

---

# **STEP 2 — MEDICAL_DRIFT_OPERATOR**  
### *Detect template, semantic, translation, AI, commercial, and regime drift.*

---

### **Student Task**

Students compute drift maps for each regime using the example packets.

### **Instructor Expectations**

- Cleveland Clinic → **low drift**  
- Ping An → **high drift**  
- NHS → **very low drift**  

Students must identify:

- template drift  
- semantic drift  
- translation drift  
- AI drift  
- commercial drift  
- regime drift  

### **Common Pitfalls**

- Underestimating Ping An drift  
- Missing AI‑generated instability  
- Missing commercial drift  
- Treating NHS as “no drift” instead of “very low drift”  

### **Grading Notes**

Full credit requires:

- correct drift classification  
- correct drift flags  
- correct drift score reasoning  

---

# **STEP 3 — MEDICAL_SUBSTRATE_OPERATOR**  
### *Evaluate substrate stability, interference, and risk.*

---

### **Student Task**

Students evaluate:

- substrate stability  
- substrate noise  
- layer interference  
- accessibility stability  
- translation/commercial/AI layers  

### **Instructor Expectations**

- Cleveland Clinic → stable, low noise  
- Ping An → unstable, high interference  
- NHS → very stable, minimal interference  

### **Common Pitfalls**

- Ignoring accessibility  
- Treating mobile_html as equivalent to html  
- Missing interference layers  

### **Grading Notes**

Full credit requires:

- correct substrate packet  
- correct interference identification  
- correct substrate score  

---

# **STEP 4 — MEDICAL_REGIME_OPERATOR**  
### *Classify regime logic and detect regime coherence or shifts.*

---

### **Student Task**

Students classify each example into:

- clinical regime  
- AI‑augmented commercial regime  
- public‑health regime  

### **Instructor Expectations**

- Cleveland Clinic → clinical  
- Ping An → AI‑augmented commercial  
- NHS → public‑health  

Students must identify:

- regime signals  
- regime coherence  
- regime shifts  

### **Common Pitfalls**

- Treating Ping An as clinical  
- Missing regime shifts  
- Overlooking public‑health framing  

### **Grading Notes**

Full credit requires:

- correct regime classification  
- correct regime signals  
- correct coherence assessment  

---

# **STEP 5 — MEDICAL_CONTINUITY_OPERATOR**  
### *Extract the continuity kernel across regimes.*

---

### **Student Task**

Students compute:

- stable symptoms  
- stable risk factors  
- stable red flags  
- stable actions  
- stable differentials  

### **Instructor Expectations**

Students must produce a **regime‑invariant continuity kernel**.

Expected stable elements:

- symptoms: discomfort, pressure, shortness of breath  
- risks: age, chronic illness, hypertension  
- red flags: severe pain, difficulty breathing, fainting  
- actions: emergency escalation for red flags  
- differentials: cardiac, pulmonary, musculoskeletal  

### **Common Pitfalls**

- Including regime‑specific elements  
- Including AI‑generated suggestions  
- Including commercial prompts  
- Including translation artifacts  

### **Grading Notes**

Full credit requires:

- correct continuity kernel  
- correct exclusion of drift‑sensitive elements  

---

# **STEP 6 — MEDICAL_SYNTHESIS_OPERATOR**  
### *Produce a drift‑bounded, regime‑aware, patient‑safe synthesis.*

---

### **Student Task**

Students integrate all upstream packets to produce:

- stable elements  
- unstable elements  
- regime‑specific elements  
- drift‑sensitive elements  
- substrate risks  
- uncertainty flags  
- escalation indicators  
- patient‑safe summary  

### **Instructor Expectations**

Students must:

- preserve continuity kernel  
- separate regime‑specific differences  
- disclose uncertainty  
- identify escalation indicators  
- avoid medical advice  
- avoid collapsing regimes  

### **Common Pitfalls**

- Writing medical advice  
- Collapsing regimes into one narrative  
- Ignoring drift  
- Ignoring substrate risks  
- Missing uncertainty disclosure  

### **Grading Notes**

Full credit requires:

- correct synthesis packet  
- correct regime separation  
- correct uncertainty disclosure  
- correct escalation indicators  
- patient‑safe summary  

---

# **Instructor Rubric (10‑Point Scale)**

| Category | Points | Criteria |
|----------|--------|----------|
| Metadata | 2 | Correct substrate/noise/overlays |
| Drift | 2 | Correct drift map + flags |
| Substrate | 1 | Correct stability + interference |
| Regime | 1 | Correct regime classification |
| Continuity | 2 | Correct continuity kernel |
| Synthesis | 2 | Patient‑safe, drift‑bounded, regime‑aware |

A score of **9–10** indicates full operator literacy.

---

# **Instructor Closing Notes**

This lab trains students to:

- see medical information structurally  
- identify drift and instability  
- understand regime differences  
- extract continuity kernels  
- produce safe, stable, cross‑regime synthesis  

It is the **medical equivalent** of the archive_org operator lab — but tuned for:

- multilingual drift  
- AI‑generated instability  
- commercial overlays  
- public‑health framing  
- clinical conservatism  
