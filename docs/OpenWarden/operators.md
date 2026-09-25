# 🛡️ **OpenWarden — operators.md**  
**OpenWarden Suite Root — Governance, Drift, Metadata & Structural Stewardship**  
**Analyzer Layer:** suite‑governance  
**Regime:** open‑warden‑substrate  
**Version:** 1.0  

---

## **1. Operator Grammar Overview**

OpenWarden defines the **root operator grammar** used across the entire suite.  
Operators govern how modules may:

- transform metadata  
- reorganize structure  
- correct drift  
- annotate governance state  
- extend canonical fields  
- condense verbosity  

Every operator is **suite‑safe**, **drift‑bounded**, **coherence‑declared**, and **structurally reversible**.

OpenWarden is the origin point — all other modules inherit these rules.

---

## **2. Operator Categories**

OpenWarden supports six canonical operator classes:

1. **Extend**  
2. **Condense**  
3. **Refactor**  
4. **Capture**  
5. **Annotate**  
6. **Correct**

These operators define the allowed transformations across the entire suite.

---

## **3. Extend Operator**

### **Purpose**  
Adds **canonical detail** to module metadata without altering declared module identity.

### **Allowed Extensions**  
- refining suite identity descriptors  
- expanding governance context  
- adding structural clarifications  

### **Forbidden Extensions**  
- adding non‑canonical fields  
- introducing ambiguous governance modes  
- altering declared module identity  

### **Example**  
Extending `suite:openwarden-root` → `suite:openwarden-root.triadic`

---

## **4. Condense Operator**

### **Purpose**  
Simplifies metadata while preserving suite meaning and coherence.

### **Allowed Condensation**  
- collapsing overly granular governance descriptors  
- simplifying structural metadata  
- reducing verbosity  

### **Forbidden Condensation**  
- removing lineage fields  
- removing governance fields  
- removing operator grammar fields  

### **Example**  
Condensing `governance:open-warden-substrate.extended` → `governance:open-warden-substrate`

---

## **5. Refactor Operator**

### **Purpose**  
Reorganizes module metadata for clarity, stability, or suite coherence.

### **Allowed Refactoring**  
- reorganizing governance blocks  
- restructuring identity hierarchy  
- normalizing structural signatures  

### **Forbidden Refactoring**  
- altering declared module identity  
- manipulating coherence scores  
- removing lineage identifiers  

### **Example**  
Refactoring suite fields from:  
`signature:suite;governance:open;coherence:1.0`  
to grouped structure:  
`suite.signature:suite;suite.governance:open;suite.coherence:1.0`

---

## **6. Capture Operator**

### **Purpose**  
Records governance signals, drift behavior, or lineage events.

### **Capture Targets**  
- drift events  
- boundary changes  
- operator usage  
- lineage updates  

### **Capture Rules**  
Captured data must be:

- canonical  
- non‑ambiguous  
- suite‑relevant  
- governance‑safe  

### **Example**  
Capturing a drift correction:  
`drift:unbounded → drift:bounded`

---

## **7. Annotate Operator**

### **Purpose**  
Adds governance‑safe annotations to module metadata.

### **Allowed Annotations**  
- coherence notes  
- drift warnings  
- structural clarifications  
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
Fixes suite drift, metadata misalignment, or operator misuse.

### **Correction Types**  
- governance correction  
- structural normalization  
- identity repair  
- canonical field restoration  

### **Forbidden Corrections**  
- altering declared module identity  
- inflating coherence scores  
- removing lineage  

### **Example**  
Correcting malformed metadata:  
`coherence:1.7` → `coherence:1.0`

---

## **9. Operator Safety Rules**

Operators must obey:

- **suite integrity constraints**  
- **drift boundaries**  
- **coherence declarations**  
- **canonical metadata rules**  
- **governance policies**  

Operators may never introduce:

- ambiguous governance states  
- malformed structural signatures  
- non‑canonical fields  
- adversarial suite drift  

---

## **10. Cross‑Module Operator Alignment**

OpenWarden operators govern:

- **OpenIAM** — identity operators  
- **OpenGeo** — geospatial operators  
- **OpenLLM** — model operators  
- **OpenRisk** — risk operators  
- **OpenStream** — streaming operators  
- **OpenVitals** — physiological operators  
- **OpenFeed** — feed operators  
- **OpenCatalog** — metadata operators  
- **OpenSEO** — semantic operators  
- **OpenAdEngine** — advertising operators  
- **OpenSoN** — social operators  

All alignment is drift‑bounded and coherence‑declared.

---

## **11. Operator Metadata Fields**

Modules must declare operator availability:

```html
<meta name="open.warden.operator.extend" content="true">
<meta name="open.warden.operator.condense" content="true">
<meta name="open.warden.operator.refactor" content="true">
<meta name="open.warden.operator.capture" content="true">
<meta name="open.warden.operator.annotate" content="true">
<meta name="open.warden.operator.correct" content="true">
```

These fields ensure operator grammar compliance.
