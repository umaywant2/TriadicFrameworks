# 🌍 **OpenGeo — operators.md**  
**OpenWarden Suite — Geospatial Metadata Substrate**  
**Analyzer Layer:** dimensional  
**Regime:** open‑geo‑governance  
**Version:** 1.0  

---

## **1. Operator Grammar Overview**

OpenGeo uses the **OpenWarden operator grammar**, ensuring geospatial metadata evolves predictably, safely, and coherently across all TriadicFrameworks modules.  
Operators define how geospatial metadata may be:

- transformed  
- reorganized  
- corrected  
- annotated  
- extended  
- condensed  

Every operator is **drift‑bounded**, **coherence‑declared**, and **dimensionally safe**.

---

## **2. Operator Categories**

OpenGeo supports six canonical operator classes:

1. **Extend**  
2. **Condense**  
3. **Refactor**  
4. **Capture**  
5. **Annotate**  
6. **Correct**

Each operator is described below with geospatial‑specific semantics.

---

## **3. Extend Operator**

### **Purpose**  
Adds **dimensional or locality detail** to a geospatial object’s metadata without altering its declared region or coordinate identity.

### **Allowed Extensions**  
- refining dimensional categories  
- expanding locality descriptors  
- adding contextual overlays  

### **Forbidden Extensions**  
- adding non‑canonical fields  
- introducing ambiguous locality  
- altering declared region identity  

### **Example**  
Extending `region:north-america` → `region:north-america.great-lakes`

---

## **4. Condense Operator**

### **Purpose**  
Simplifies metadata while preserving dimensional meaning and coherence.

### **Allowed Condensation**  
- collapsing overly granular locality descriptors  
- simplifying boundary metadata  
- reducing dimensional verbosity  

### **Forbidden Condensation**  
- removing lineage fields  
- removing governance fields  
- removing operator grammar fields  

### **Example**  
Condensing `locality:midwest.great-lakes.detroit-metro` → `locality:midwest.great-lakes`

---

## **5. Refactor Operator**

### **Purpose**  
Reorganizes metadata for clarity, stability, or dimensional coherence.

### **Allowed Refactoring**  
- reorganizing coordinate blocks  
- restructuring locality hierarchy  
- normalizing dimensional signatures  

### **Forbidden Refactoring**  
- altering declared region identity  
- manipulating coherence scores  
- removing lineage identifiers  

### **Example**  
Refactoring coordinates from:  
`lat:42.204;lon:-83.485;alt:200m`  
to grouped structure:  
`coords:lat:42.204;coords:lon:-83.485;coords:alt:200m`

---

## **6. Capture Operator**

### **Purpose**  
Records dimensional signals, coordinate behavior, or lineage events.

### **Capture Targets**  
- coordinate fluctuations  
- boundary changes  
- drift events  
- operator usage  

### **Capture Rules**  
Captured data must be:

- canonical  
- non‑ambiguous  
- dimensionally relevant  
- governance‑safe  

### **Example**  
Capturing a coordinate correction:  
`lat:42.204 → lat:42.205`

---

## **7. Annotate Operator**

### **Purpose**  
Adds governance‑safe annotations to metadata.

### **Allowed Annotations**  
- coherence notes  
- drift warnings  
- locality clarifications  
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
- coordinate correction  
- locality normalization  
- boundary recalibration  
- governance field restoration  

### **Forbidden Corrections**  
- altering declared region identity  
- inflating coherence scores  
- removing lineage  

### **Example**  
Correcting malformed metadata:  
`coordinates:lat:91.000` → `coordinates:lat:42.204`

---

## **9. Operator Safety Rules**

Operators must obey:

- **dimensional integrity constraints**  
- **drift boundaries**  
- **coherence declarations**  
- **canonical metadata rules**  
- **suite governance policies**  

Operators may never introduce:

- ambiguous locality  
- malformed coordinates  
- non‑canonical fields  
- adversarial dimensional drift  

---

## **10. Cross‑Module Operator Alignment**

OpenGeo operators align with:

- **OpenSEO** — semantic region operators  
- **OpenSoN** — social locality operators  
- **OpenStream** — geospatial recommendation operators  
- **OpenCatalog** — location‑based product operators  
- **OpenAdEngine** — contextual geospatial ad operators  
- **OpenRisk** — anomaly detection operators  
- **OpenIAM** — identity‑safe operators  

All alignment is drift‑bounded and coherence‑declared.

---

## **11. Operator Metadata Fields**

Geospatial objects must declare operator availability:

```html
<meta name="open.geo.operator.extend" content="true">
<meta name="open.geo.operator.condense" content="true">
<meta name="open.geo.operator.refactor" content="true">
<meta name="open.geo.operator.capture" content="true">
<meta name="open.geo.operator.annotate" content="true">
<meta name="open.geo.operator.correct" content="true">
```

These fields ensure operator grammar compliance.
