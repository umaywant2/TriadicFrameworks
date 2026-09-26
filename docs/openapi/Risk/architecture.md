# ⚠️ **OpenRisk — architecture.md**  
**OpenWarden Suite — Risk Analysis Substrate**  
**Analyzer Layer:** dimensional  
**Regime:** open‑risk‑governance  
**Version:** 1.0  

---

## **1. Architectural Overview**

OpenRisk provides a **dimensional, drift‑aware, coherence‑declared risk substrate** for the OpenWarden suite.  
Its architecture is built around five canonical components:

1. **Dimensional Signature Model**  
2. **Risk Score & Anomaly Engine**  
3. **Boundary & Severity Layer**  
4. **Governance & Drift Control**  
5. **Cross‑Module Integration Layer**

Each component ensures risk stability, metadata correctness, and operator‑aligned transformations.

---

## **2. Dimensional Signature Model**

The Dimensional Signature Model defines the **identity** of a risk object using canonical fields.  
It includes:

- dimensional category  
- risk score block  
- anomaly lineage  
- coherence score  
- drift status  

Risk metadata is designed for:

- fraud detection  
- anomaly interpretation  
- lineage tracking  
- interoperability  
- AI‑safe risk scoring  

### **2.1 Metadata Requirements**

Every risk object must include:

- `open.risk.dimension`  
- `open.risk.score`  
- `open.risk.severity`  
- `open.risk.coherence`  
- `open.risk.drift`  
- `open.risk.lineage`  
- `open.risk.version`  
- `open.risk.module`  

Missing fields trigger drift correction.

---

## **3. Risk Score & Anomaly Engine**

The Risk Score & Anomaly Engine ensures:

- risk score correctness  
- anomaly lineage stability  
- fraud metadata integrity  
- drift detection  
- operator‑aligned transformations  

### **3.1 Risk Score Rules**

Risk scores must be:

- canonical  
- bounded  
- reversible  
- dimensionally coherent  

Risk score corruption is treated as dimensional drift.

### **3.2 Anomaly Rules**

Anomalies must maintain:

- correct lineage  
- non‑ambiguous descriptors  
- stable severity mapping  

Anomaly drift triggers correction and lineage update.

---

## **4. Boundary & Severity Layer**

Risk interpretation is governed by:

- severity boundaries  
- anomaly magnitude  
- contextual overlays  
- canonical metadata  

### **4.1 Boundary Inputs**

- dimensional category  
- risk score block  
- severity descriptor  
- operator grammar fields  

### **4.2 Boundary Outputs**

- severity classification  
- boundary correction  
- anomaly recalibration  
- lineage update  

Boundary violations trigger suppression.

---

## **5. Governance & Drift Control**

OpenRisk enforces strict governance rules inherited from OpenWarden.

### **5.1 Drift Types**

- **Risk Drift** — malformed or unstable risk scores  
- **Anomaly Drift** — corrupted or ambiguous anomalies  
- **Boundary Drift** — incorrect or mismatched severity boundaries  
- **Metadata Drift** — missing or manipulated fields  
- **Lineage Drift** — corrupted or ambiguous lineage  

### **5.2 Drift Responses**

1. **Flag** — mark risk object as drifted  
2. **Suppress** — remove from risk output  
3. **Correct** — repair metadata  
4. **Recalibrate** — adjust severity or score  
5. **Update Lineage** — record correction  

All drift responses are logged.

---

## **6. Operator Grammar Alignment**

OpenRisk uses the OpenWarden operator grammar:

- **extend** — add dimensional detail  
- **condense** — simplify metadata  
- **refactor** — reorganize risk fields  
- **capture** — record drift or lineage  
- **annotate** — add governance notes  
- **correct** — fix drift or misalignment  

Operators ensure safe, reversible risk evolution.

---

## **7. Cross‑Module Integration**

OpenRisk integrates with:

- **OpenIAM** — identity‑safe risk rules  
- **OpenGeo** — location‑aware risk boundaries  
- **OpenFeed** — risk‑aware feed filtering  
- **OpenCatalog** — risk metadata alignment  
- **OpenSEO** — semantic risk metadata  
- **OpenLLM** — model‑aware anomaly detection  
- **OpenWarden** — suite‑governed risk policies  

All integrations are drift‑bounded and coherence‑declared.

---

## **8. Canonical Metadata Block (Example)**

```html
<meta name="open.risk.dimension" content="risk:fraud-detection">
<meta name="open.risk.score" content="score:0.72">
<meta name="open.risk.severity" content="severity:medium">
<meta name="open.risk.coherence" content="0.91">
<meta name="open.risk.drift" content="bounded">
<meta name="open.risk.lineage" content="risklineage:7c3f">
<meta name="open.risk.version" content="1.0">
<meta name="open.risk.module" content="OpenRisk">
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
