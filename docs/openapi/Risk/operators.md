# ⚠️ **OpenRisk — operators.md**  
**OpenWarden Suite — Risk Analysis Substrate**  
**Analyzer Layer:** dimensional  
**Regime:** open‑risk‑governance  
**Version:** 1.0  

---

## **1. Operator Grammar Overview**

OpenRisk uses the **OpenWarden operator grammar**, ensuring risk metadata evolves predictably, safely, and coherently across all TriadicFrameworks modules.  
Operators define how risk metadata may be:

- transformed  
- reorganized  
- corrected  
- annotated  
- extended  
- condensed  

Every operator is **drift‑bounded**, **coherence‑declared**, and **dimensionally safe**.

---

## **2. Operator Categories**

OpenRisk supports six canonical operator classes:

1. **Extend**  
2. **Condense**  
3. **Refactor**  
4. **Capture**  
5. **Annotate**  
6. **Correct**

Each operator is described below with risk‑specific semantics.

---

## **3. Extend Operator**

### **Purpose**  
Adds **dimensional or severity detail** to a risk object’s metadata without altering its declared risk category.

### **Allowed Extensions**  
- refining dimensional categories  
- expanding severity descriptors  
- adding contextual overlays  

### **Forbidden Extensions**  
- adding non‑canonical fields  
- introducing ambiguous severity  
- altering declared risk identity  

### **Example**  
Extending `risk:fraud-detection` → `risk:fraud-detection.transactional`

---

## **4. Condense Operator**

### **Purpose**  
Simplifies metadata while preserving dimensional meaning and coherence.

### **Allowed Condensation**  
- collapsing overly granular severity descriptors  
- simplifying boundary metadata  
- reducing dimensional verbosity  

### **Forbidden Condensation**  
- removing lineage fields  
- removing governance fields  
- removing operator grammar fields  

### **Example**  
Condensing `severity:high.critical` → `severity:high`

---

## **5. Refactor Operator**

### **Purpose**  
Reorganizes risk metadata for clarity, stability, or dimensional coherence.

### **Allowed Refactoring**  
- reorganizing risk score blocks  
- restructuring severity hierarchy  
- normalizing dimensional signatures  

### **Forbidden Refactoring**  
- altering declared risk identity  
- manipulating coherence scores  
- removing lineage identifiers  

### **Example**  
Refactoring risk score fields from:  
`score:0.72;severity:medium;boundary:moderate`  
to grouped structure:  
`risk.score:0.72;risk.severity:medium;risk.boundary:moderate`

---

## **6. Capture Operator**

### **Purpose**  
Records dimensional signals, anomaly behavior, or lineage events.

### **Capture Targets**  
- risk score fluctuations  
- severity changes  
- drift events  
- operator usage  

### **Capture Rules**  
Captured data must be:

- canonical  
- non‑ambiguous  
- dimensionally relevant  
- governance‑safe  

### **Example**  
Capturing a severity correction:  
`severity:medium → severity:high`

---

## **7. Annotate Operator**

### **Purpose**  
Adds governance‑safe annotations to risk metadata.

### **Allowed Annotations**  
- coherence notes  
- drift warnings  
- severity clarifications  
- boundary markers  

### **Forbidden Annotations**  
- personal identifiers  
- behavioral predictions  
- sensitive category labels  

### **Example**  
Annotating: `coherence:stable` or `drift:corrected`.

---

## **8. Correct Operator**

### **Purpose**  
Fixes dimensional drift, metadata misalignment, or operator misuse.

### **Correction Types**  
- risk score correction  
- severity normalization  
- boundary recalibration  
- governance field restoration  

### **Forbidden Corrections**  
- altering declared risk identity  
- inflating coherence scores  
- removing lineage  

### **Example**  
Correcting malformed metadata:  
`score:1.42` → `score:0.42`

---

## **9. Operator Safety Rules**

Operators must obey:

- **dimensional integrity constraints**  
- **drift boundaries**  
- **coherence declarations**  
- **canonical metadata rules**  
- **suite governance policies**  

Operators may never introduce:

- ambiguous severity  
- malformed risk scores  
- non‑canonical fields  
- adversarial dimensional drift  

---

## **10. Cross‑Module Operator Alignment**

OpenRisk operators align with:

- **OpenIAM** — identity‑safe risk operators  
- **OpenGeo** — location‑aware risk operators  
- **OpenFeed** — risk‑aware feed operators  
- **OpenCatalog** — risk metadata operators  
- **OpenSEO** — semantic risk operators  
- **OpenLLM** — model‑aware anomaly operators  
- **OpenWarden** — suite‑governed structural operators  

All alignment is drift‑bounded and coherence‑declared.

---

## **11. Operator Metadata Fields**

Risk objects must declare operator availability:

```html
<meta name="open.risk.operator.extend" content="true">
<meta name="open.risk.operator.condense" content="true">
<meta name="open.risk.operator.refactor" content="true">
<meta name="open.risk.operator.capture" content="true">
<meta name="open.risk.operator.annotate" content="true">
<meta name="open.risk.operator.correct" content="true">
```

These fields ensure operator grammar compliance.
