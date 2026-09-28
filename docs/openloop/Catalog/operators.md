# 🛒 **OpenCatalog — operators.md**  
**OpenWarden Suite — Product Catalog Substrate**  
**Analyzer Layer:** structural  
**Regime:** open‑catalog-governance  
**Version:** 1.0  

---

## **1. Operator Grammar Overview**

OpenCatalog uses the **OpenWarden operator grammar**, ensuring catalog items evolve predictably, safely, and coherently across all TriadicFrameworks modules.  
Operators define how catalog metadata may be:

- transformed  
- reorganized  
- corrected  
- annotated  
- extended  
- condensed  

Every operator is **drift‑bounded**, **coherence‑declared**, and **structurally safe**.

---

## **2. Operator Categories**

OpenCatalog supports six canonical operator classes:

1. **Extend**  
2. **Condense**  
3. **Refactor**  
4. **Capture**  
5. **Annotate**  
6. **Correct**

Each operator is described below with catalog‑specific semantics.

---

## **3. Extend Operator**

### **Purpose**  
Adds **structural or dimensional detail** to an item’s metadata without altering its identity or category.

### **Allowed Extensions**  
- adding dimensional attributes  
- refining structural hierarchy  
- expanding variant descriptors  

### **Forbidden Extensions**  
- adding non‑canonical fields  
- introducing ambiguous attributes  
- altering declared item identity  

### **Example**  
Extending `electronics.computing` → `electronics.computing.laptops`

---

## **4. Condense Operator**

### **Purpose**  
Simplifies metadata while preserving structural meaning and coherence.

### **Allowed Condensation**  
- collapsing overly granular categories  
- simplifying variant descriptors  
- reducing attribute verbosity  

### **Forbidden Condensation**  
- removing lineage fields  
- removing governance fields  
- removing operator grammar fields  

### **Example**  
Condensing `electronics.computing.laptops.ultrabooks` → `electronics.computing.laptops`

---

## **5. Refactor Operator**

### **Purpose**  
Reorganizes metadata for clarity, stability, or structural coherence.

### **Allowed Refactoring**  
- reorganizing dimensional attributes  
- restructuring category hierarchy  
- normalizing variant signatures  

### **Forbidden Refactoring**  
- altering declared item identity  
- manipulating coherence scores  
- removing lineage identifiers  

### **Example**  
Refactoring attributes from:  
`ram:32gb;cpu:ryzen7;screen:15in`  
to a grouped structure:  
`hardware:ram:32gb;hardware:cpu:ryzen7;display:15in`

---

## **6. Capture Operator**

### **Purpose**  
Records structural signals, lineage events, or drift occurrences.

### **Capture Targets**  
- variant evolution  
- category changes  
- drift events  
- operator usage  

### **Capture Rules**  
Captured data must be:

- canonical  
- non‑ambiguous  
- structurally relevant  
- governance‑safe  

### **Example**  
Capturing a variant evolution:  
`v3 → v4 (battery upgrade)`

---

## **7. Annotate Operator**

### **Purpose**  
Adds governance‑safe annotations to metadata.

### **Allowed Annotations**  
- coherence notes  
- drift warnings  
- structural clarifications  
- lineage markers  

### **Forbidden Annotations**  
- non‑canonical fields  
- ambiguous category labels  
- semantic tags unrelated to structure  

### **Example**  
Annotating: `coherence:stable` or `drift:corrected`.

---

## **8. Correct Operator**

### **Purpose**  
Fixes structural drift, metadata corruption, or operator misuse.

### **Correction Types**  
- category correction  
- attribute normalization  
- variant lineage repair  
- governance field restoration  

### **Forbidden Corrections**  
- altering declared item identity  
- inflating coherence scores  
- removing lineage  

### **Example**  
Correcting malformed metadata:  
`category:electronics.computing.laptp` → `electronics.computing.laptops`

---

## **9. Operator Safety Rules**

Operators must obey:

- **structural integrity constraints**  
- **drift boundaries**  
- **coherence declarations**  
- **canonical metadata rules**  
- **suite governance policies**  

Operators may never introduce:

- ambiguous categories  
- malformed attributes  
- non‑canonical fields  
- adversarial structural drift  

---

## **10. Cross‑Module Operator Alignment**

OpenCatalog operators align with:

- **OpenSEO** — semantic metadata operators  
- **OpenStream** — recommendation operators  
- **OpenAdEngine** — product‑aligned ad operators  
- **OpenRisk** — anomaly detection operators  
- **OpenIAM** — identity‑safe operators  
- **OpenGeo** — location metadata operators  

All alignment is drift‑bounded and coherence‑declared.

---

## **11. Operator Metadata Fields**

Catalog items must declare operator availability:

```html
<meta name="open.catalog.operator.extend" content="true">
<meta name="open.catalog.operator.condense" content="true">
<meta name="open.catalog.operator.refactor" content="true">
<meta name="open.catalog.operator.capture" content="true">
<meta name="open.catalog.operator.annotate" content="true">
<meta name="open.catalog.operator.correct" content="true">
```

These fields ensure operator grammar compliance.
