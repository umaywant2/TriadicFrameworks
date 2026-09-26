# 🫀 **OpenVitals — architecture.md**  
**OpenWarden Suite — Health & Physiological Signal Substrate**  
**Analyzer Layer:** dimensional  
**Regime:** open‑vitals‑governance  
**Version:** 1.0  

---

## **1. Architectural Overview**

OpenVitals provides a **dimensional, drift‑aware, coherence‑declared physiological signal substrate** for the OpenWarden suite.  
Its architecture is built around five canonical components:

1. **Vital Signature Engine**  
2. **Physiological Metric Layer**  
3. **Interpretation Boundary System**  
4. **Governance & Drift Control**  
5. **Cross‑Module Integration Layer**

Each component ensures physiological stability, metadata correctness, and operator‑aligned transformations.

---

## **2. Vital Signature Engine**

The Vital Signature Engine defines the **identity** of a physiological signal using canonical fields.  
It includes:

- dimensional signature  
- vital metric block  
- interpretation boundary  
- coherence score  
- drift status  
- lineage ID  

Vital signatures allow consistent interpretation across modules.

### **2.1 Metadata Requirements**

Every vital signal must include:

- `open.vitals.signature`  
- `open.vitals.metric`  
- `open.vitals.boundary`  
- `open.vitals.coherence`  
- `open.vitals.drift`  
- `open.vitals.lineage`  
- `open.vitals.version`  
- `open.vitals.module`  

Missing fields trigger drift correction.

---

## **3. Physiological Metric Layer**

The Physiological Metric Layer ensures:

- vital metric correctness  
- variability stability  
- interpretation integrity  
- drift detection  
- operator‑aligned transformations  

### **3.1 Vital Metric Rules**

Vital metrics must be:

- canonical  
- bounded  
- reversible  
- dimensionally coherent  

Metric corruption is treated as physiological drift.

### **3.2 Variability Rules**

Variability descriptors must maintain:

- correct physiological mapping  
- non‑ambiguous descriptors  
- stable interpretation boundaries  

Variability drift triggers correction and lineage update.

---

## **4. Interpretation Boundary System**

Physiological interpretation is governed by:

- declared boundaries  
- dimensional constraints  
- contextual overlays  
- canonical metadata  

### **4.1 Boundary Inputs**

- dimensional signature  
- vital metric block  
- variability descriptor  
- operator grammar fields  

### **4.2 Boundary Outputs**

- interpretation classification  
- boundary correction  
- variability recalibration  
- lineage update  

Boundary violations trigger suppression.

---

## **5. Governance & Drift Control**

OpenVitals enforces strict governance rules inherited from OpenWarden.

### **5.1 Drift Types**

- **Signal Drift** — malformed or unstable physiological signals  
- **Variability Drift** — corrupted or ambiguous variability descriptors  
- **Boundary Drift** — incorrect or mismatched interpretation boundaries  
- **Metadata Drift** — missing or manipulated fields  
- **Lineage Drift** — corrupted or ambiguous lineage  

### **5.2 Drift Responses**

1. **Flag** — mark signal as drifted  
2. **Suppress** — remove from interpretation output  
3. **Correct** — repair metadata  
4. **Recalibrate** — adjust variability or boundaries  
5. **Update Lineage** — record correction  

All drift responses are logged.

---

## **6. Operator Grammar Alignment**

OpenVitals uses the OpenWarden operator grammar:

- **extend** — add dimensional or physiological detail  
- **condense** — simplify metadata  
- **refactor** — reorganize vital fields  
- **capture** — record drift or lineage  
- **annotate** — add governance notes  
- **correct** — fix drift or misalignment  

Operators ensure safe, reversible physiological evolution.

---

## **7. Cross‑Module Integration**

OpenVitals integrates with:

- **OpenRisk** — anomaly detection for physiological drift  
- **OpenIAM** — identity‑safe health‑signal access  
- **OpenGeo** — location‑aware physiological interpretation  
- **OpenFeed** — health‑signal‑aware feed rules  
- **OpenCatalog** — vital metadata alignment  
- **OpenLLM** — model‑aware physiological interpretation  
- **OpenWarden** — suite‑governed health‑signal policies  

All integrations are drift‑bounded and coherence‑declared.

---

## **8. Canonical Metadata Block (Example)**

```html
<meta name="open.vitals.signature" content="vital:openvitals-core">
<meta name="open.vitals.metric" content="metric:heart-rate">
<meta name="open.vitals.boundary" content="boundary:physio-safe">
<meta name="open.vitals.coherence" content="0.92">
<meta name="open.vitals.drift" content="bounded">
<meta name="open.vitals.lineage" content="vitalslineage:3f9a">
<meta name="open.vitals.version" content="1.0">
<meta name="open.vitals.module" content="OpenVitals">
```

---

## **9. File Structure**

- `README.md` — front door  
- `architecture.md` — this file  
- `canonical_metadata.md` — metadata schema  
- `governance.md` — drift & policy rules  
- `operators.md` — operator grammar  
- `index.html` — module front page  
- `module.json` — manifest  
