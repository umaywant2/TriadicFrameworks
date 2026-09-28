# 🛡️ **OpenIAM — architecture.md**  
**OpenWarden Suite — Identity & Access Substrate**  
**Analyzer Layer:** structural  
**Regime:** open‑identity‑governance  
**Version:** 1.0  

---

## **1. Architectural Overview**

OpenIAM provides a **structural, drift‑aware, coherence‑declared identity substrate** for the OpenWarden suite.  
Its architecture is built around five canonical components:

1. **Identity Metadata Model**  
2. **Role & Permission Engine**  
3. **Boundary & Access Layer**  
4. **Governance & Drift Control**  
5. **Cross‑Module Integration Layer**

Each component ensures identity stability, metadata correctness, and operator‑aligned transformations.

---

## **2. Identity Metadata Model**

The Identity Metadata Model defines the **identity** of a subject using canonical fields.  
It includes:

- role signature  
- permission block  
- boundary descriptor  
- coherence score  
- drift status  
- lineage ID  

Identity metadata is designed for:

- access control  
- lineage tracking  
- interoperability  
- AI interpretation  

### **2.1 Metadata Requirements**

Every identity must include:

- `open.iam.role`  
- `open.iam.permissions`  
- `open.iam.boundary`  
- `open.iam.coherence`  
- `open.iam.drift`  
- `open.iam.lineage`  
- `open.iam.version`  
- `open.iam.module`  

Missing fields trigger drift correction.

---

## **3. Role & Permission Engine**

The Role & Permission Engine ensures:

- role correctness  
- permission stability  
- boundary integrity  
- drift detection  
- operator‑aligned transformations  

### **3.1 Role Rules**

Roles must be:

- canonical  
- bounded  
- reversible  
- structurally coherent  

Role corruption is treated as identity drift.

### **3.2 Permission Rules**

Permissions must maintain:

- correct access boundaries  
- non‑ambiguous descriptors  
- stable inheritance patterns  

Permission drift triggers correction and lineage update.

---

## **4. Boundary & Access Layer**

Access is determined by:

- role signature  
- permission block  
- boundary descriptor  
- coherence score  
- canonical metadata  

### **4.1 Boundary Inputs**

- role category  
- permission block  
- boundary descriptor  
- operator grammar fields  

### **4.2 Boundary Outputs**

- access classification  
- boundary correction  
- permission recalibration  
- lineage update  

Boundary violations trigger suppression.

---

## **5. Governance & Drift Control**

OpenIAM enforces strict governance rules inherited from OpenWarden.

### **5.1 Drift Types**

- **Identity Drift** — malformed or unstable identity metadata  
- **Permission Drift** — corrupted or ambiguous permissions  
- **Boundary Drift** — incorrect or mismatched access boundaries  
- **Metadata Drift** — missing or manipulated fields  
- **Lineage Drift** — corrupted or ambiguous lineage  

### **5.2 Drift Responses**

1. **Flag** — mark identity as drifted  
2. **Suppress** — remove from access output  
3. **Correct** — repair metadata  
4. **Recalibrate** — adjust permissions or boundaries  
5. **Update Lineage** — record correction  

All drift responses are logged.

---

## **6. Operator Grammar Alignment**

OpenIAM uses the OpenWarden operator grammar:

- **extend** — add structural detail  
- **condense** — simplify metadata  
- **refactor** — reorganize identity fields  
- **capture** — record drift or lineage  
- **annotate** — add governance notes  
- **correct** — fix drift or misalignment  

Operators ensure safe, reversible identity evolution.

---

## **7. Cross‑Module Integration**

OpenIAM integrates with:

- **OpenCatalog** — identity‑safe product access  
- **OpenFeed** — identity‑safe feed rules  
- **OpenGeo** — location‑aware identity boundaries  
- **OpenRisk** — anomaly detection for identity drift  
- **OpenSEO** — semantic identity metadata  
- **OpenWarden** — suite‑governed identity policies  

All integrations are drift‑bounded and coherence‑declared.

---

## **8. Canonical Metadata Block (Example)**

```html
<meta name="open.iam.role" content="role:admin">
<meta name="open.iam.permissions" content="read:all;write:restricted">
<meta name="open.iam.boundary" content="boundary:global">
<meta name="open.iam.coherence" content="0.96">
<meta name="open.iam.drift" content="bounded">
<meta name="open.iam.lineage" content="iamlineage:9d4c">
<meta name="open.iam.version" content="1.0">
<meta name="open.iam.module" content="OpenIAM">
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
