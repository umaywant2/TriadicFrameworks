# 🛡️ **OpenIAM — operators.md**  
**OpenWarden Suite — Identity & Access Substrate**  
**Analyzer Layer:** structural  
**Regime:** open‑identity‑governance  
**Version:** 1.0  

---

## **1. Operator Grammar Overview**

OpenIAM uses the **OpenWarden operator grammar**, ensuring identity and access metadata evolves predictably, safely, and coherently across all TriadicFrameworks modules.  
Operators define how identity metadata may be:

- transformed  
- reorganized  
- corrected  
- annotated  
- extended  
- condensed  

Every operator is **drift‑bounded**, **coherence‑declared**, and **structurally safe**.

---

## **2. Operator Categories**

OpenIAM supports six canonical operator classes:

1. **Extend**  
2. **Condense**  
3. **Refactor**  
4. **Capture**  
5. **Annotate**  
6. **Correct**

Each operator is described below with identity‑specific semantics.

---

## **3. Extend Operator**

### **Purpose**  
Adds **structural or permission detail** to an identity’s metadata without altering its declared role.

### **Allowed Extensions**  
- refining role signatures  
- expanding permission descriptors  
- adding boundary clarifications  

### **Forbidden Extensions**  
- adding non‑canonical fields  
- introducing ambiguous permissions  
- altering declared role identity  

### **Example**  
Extending `role:admin` → `role:admin.system`

---

## **4. Condense Operator**

### **Purpose**  
Simplifies metadata while preserving structural meaning and coherence.

### **Allowed Condensation**  
- collapsing overly granular permission blocks  
- simplifying boundary descriptors  
- reducing metadata verbosity  

### **Forbidden Condensation**  
- removing lineage fields  
- removing governance fields  
- removing operator grammar fields  

### **Example**  
Condensing `read:all;write:restricted;execute:limited` → `read:all;write:restricted`

---

## **5. Refactor Operator**

### **Purpose**  
Reorganizes identity metadata for clarity, stability, or structural coherence.

### **Allowed Refactoring**  
- reorganizing permission blocks  
- restructuring boundary hierarchy  
- normalizing role signatures  

### **Forbidden Refactoring**  
- altering declared role identity  
- manipulating coherence scores  
- removing lineage identifiers  

### **Example**  
Refactoring permissions from:  
`read:all;write:restricted;admin:partial`  
to grouped structure:  
`permissions.read:all;permissions.write:restricted;permissions.admin:partial`

---

## **6. Capture Operator**

### **Purpose**  
Records structural signals, permission behavior, or lineage events.

### **Capture Targets**  
- permission changes  
- boundary adjustments  
- drift events  
- operator usage  

### **Capture Rules**  
Captured data must be:

- canonical  
- non‑ambiguous  
- structurally relevant  
- governance‑safe  

### **Example**  
Capturing a permission update:  
`write:restricted → write:limited`

---

## **7. Annotate Operator**

### **Purpose**  
Adds governance‑safe annotations to identity metadata.

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
Fixes identity drift, metadata misalignment, or operator misuse.

### **Correction Types**  
- permission correction  
- boundary normalization  
- role signature repair  
- governance field restoration  

### **Forbidden Corrections**  
- altering declared role identity  
- inflating coherence scores  
- removing lineage  

### **Example**  
Correcting malformed metadata:  
`permissions:read:none` → `permissions:read:restricted`

---

## **9. Operator Safety Rules**

Operators must obey:

- **structural integrity constraints**  
- **drift boundaries**  
- **coherence declarations**  
- **canonical metadata rules**  
- **suite governance policies**  

Operators may never introduce:

- ambiguous permissions  
- malformed boundaries  
- non‑canonical fields  
- adversarial structural drift  

---

## **10. Cross‑Module Operator Alignment**

OpenIAM operators align with:

- **OpenCatalog** — identity‑safe product operators  
- **OpenFeed** — identity‑safe feed operators  
- **OpenGeo** — location‑aware identity operators  
- **OpenRisk** — anomaly detection operators  
- **OpenSEO** — semantic identity operators  
- **OpenWarden** — suite‑governed structural operators  

All alignment is drift‑bounded and coherence‑declared.

---

## **11. Operator Metadata Fields**

Identity objects must declare operator availability:

```html
<meta name="open.iam.operator.extend" content="true">
<meta name="open.iam.operator.condense" content="true">
<meta name="open.iam.operator.refactor" content="true">
<meta name="open.iam.operator.capture" content="true">
<meta name="open.iam.operator.annotate" content="true">
<meta name="open.iam.operator.correct" content="true">
```

These fields ensure operator grammar compliance.
