# 🫀 **OpenVitals — operators.md**  
**OpenWarden Suite — Health & Physiological Signal Substrate**  
**Analyzer Layer:** dimensional  
**Regime:** open‑vitals‑governance  
**Version:** 1.0  

---

## **1. Operator Grammar Overview**

OpenVitals uses the **OpenWarden operator grammar**, ensuring physiological metadata evolves predictably, safely, and coherently across all TriadicFrameworks modules.  
Operators define how vital‑signal metadata may be:

- transformed  
- reorganized  
- corrected  
- annotated  
- extended  
- condensed  

Every operator is **drift‑bounded**, **coherence‑declared**, and **physio‑safe**.

---

## **2. Operator Categories**

OpenVitals supports six canonical operator classes:

1. **Extend**  
2. **Condense**  
3. **Refactor**  
4. **Capture**  
5. **Annotate**  
6. **Correct**

Each operator is described below with physiological‑specific semantics.

---

## **3. Extend Operator**

### **Purpose**  
Adds **dimensional or physiological detail** to a vital signal’s metadata without altering its declared identity.

### **Allowed Extensions**  
- refining vital metric descriptors  
- expanding physiological context  
- adding interpretation boundary clarifications  

### **Forbidden Extensions**  
- adding non‑canonical fields  
- introducing ambiguous physiological modes  
- altering declared vital identity  

### **Example**  
Extending `metric:heart-rate` → `metric:heart-rate.resting`

---

## **4. Condense Operator**

### **Purpose**  
Simplifies metadata while preserving physiological meaning and coherence.

### **Allowed Condensation**  
- collapsing overly granular variability descriptors  
- simplifying boundary metadata  
- reducing dimensional verbosity  

### **Forbidden Condensation**  
- removing lineage fields  
- removing governance fields  
- removing operator grammar fields  

### **Example**  
Condensing `boundary:physio-safe.moderate` → `boundary:physio-safe`

---

## **5. Refactor Operator**

### **Purpose**  
Reorganizes physiological metadata for clarity, stability, or dimensional coherence.

### **Allowed Refactoring**  
- reorganizing vital metric blocks  
- restructuring boundary hierarchy  
- normalizing dimensional signatures  

### **Forbidden Refactoring**  
- altering declared vital identity  
- manipulating coherence scores  
- removing lineage identifiers  

### **Example**  
Refactoring vital fields from:  
`metric:heart-rate;boundary:physio-safe;stability:high`  
to grouped structure:  
`vitals.metric:heart-rate;vitals.boundary:physio-safe;vitals.stability:high`

---

## **6. Capture Operator**

### **Purpose**  
Records physiological signals, variability behavior, or lineage events.

### **Capture Targets**  
- variability changes  
- boundary adjustments  
- drift events  
- operator usage  

### **Capture Rules**  
Captured data must be:

- canonical  
- non‑ambiguous  
- physiologically relevant  
- governance‑safe  

### **Example**  
Capturing a variability update:  
`stability:high → stability:medium`

---

## **7. Annotate Operator**

### **Purpose**  
Adds governance‑safe annotations to vital metadata.

### **Allowed Annotations**  
- coherence notes  
- drift warnings  
- boundary clarifications  
- lineage markers  

### **Forbidden Annotations**  
- personal identifiers  
- behavioral predictions  
- sensitive category labels  

### **Example**  
Annotating: `coherence:stable` or `drift:corrected`.

---

## **8. Correct Operator**

### **Purpose**  
Fixes physiological drift, metadata misalignment, or operator misuse.

### **Correction Types**  
- vital metric correction  
- variability normalization  
- boundary recalibration  
- governance field restoration  

### **Forbidden Corrections**  
- altering declared vital identity  
- inflating coherence scores  
- removing lineage  

### **Example**  
Correcting malformed metadata:  
`range:10-400` → `range:60-100`

---

## **9. Operator Safety Rules**

Operators must obey:

- **dimensional integrity constraints**  
- **drift boundaries**  
- **coherence declarations**  
- **canonical metadata rules**  
- **suite governance policies**  

Operators may never introduce:

- ambiguous boundaries  
- malformed vital metrics  
- non‑canonical fields  
- adversarial physiological drift  

---

## **10. Cross‑Module Operator Alignment**

OpenVitals operators align with:

- **OpenRisk** — anomaly‑aware physiological operators  
- **OpenStream** — continuity‑aware signal operators  
- **OpenIAM** — identity‑safe health operators  
- **OpenGeo** — location‑aware physiological operators  
- **OpenCatalog** — vital metadata operators  
- **OpenLLM** — model‑aware physiological operators  
- **OpenWarden** — suite‑governed structural operators  

All alignment is drift‑bounded and coherence‑declared.

---

## **11. Operator Metadata Fields**

Vital signals must declare operator availability:

```html
<meta name="open.vitals.operator.extend" content="true">
<meta name="open.vitals.operator.condense" content="true">
<meta name="open.vitals.operator.refactor" content="true">
<meta name="open.vitals.operator.capture" content="true">
<meta name="open.vitals.operator.annotate" content="true">
<meta name="open.vitals.operator.correct" content="true">
```

These fields ensure operator grammar compliance.
