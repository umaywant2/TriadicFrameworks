# 🛒 **OpenCatalog — architecture.md**  
**OpenWarden Suite — Product Catalog Substrate**  
**Analyzer Layer:** structural  
**Regime:** open‑catalog-governance  
**Version:** 1.0  

---

## **1. Architectural Overview**

OpenCatalog provides a **structural, drift‑aware, coherence‑declared substrate** for product catalogs across the OpenWarden suite.  
Its architecture is built around five canonical components:

1. **Item Metadata Model**  
2. **Variant Lineage Engine**  
3. **Structural Classification Layer**  
4. **Governance & Drift Control**  
5. **Cross‑Module Integration Layer**

Each component ensures catalog stability, metadata correctness, and operator‑aligned transformations.

---

## **2. Item Metadata Model**

The Item Metadata Model defines the **identity** of a product using canonical fields.  
It includes:

- structural category  
- semantic cluster (optional)  
- variant signature  
- dimensional attributes  
- coherence score  
- drift status  

Metadata is designed for:

- search  
- classification  
- recommendation  
- interoperability  
- AI interpretation  

### **2.1 Metadata Requirements**

Every item must include:

- `open.catalog.item`  
- `open.catalog.category`  
- `open.catalog.variant`  
- `open.catalog.lineage`  
- `open.catalog.structure`  
- `open.catalog.coherence`  
- `open.catalog.drift`  
- `open.catalog.version`  
- `open.catalog.module`  

Missing fields trigger drift correction.

---

## **3. Variant Lineage Engine**

The Variant Lineage Engine tracks:

- parent → child relationships  
- variant evolution  
- drift events  
- corrections  
- operator usage  

Lineage ensures:

- transparency  
- auditability  
- structural stability  
- variant clarity  

### **3.1 Lineage Rules**

Lineage must be:

- canonical  
- immutable  
- drift‑bounded  
- operator‑aligned  

Variant confusion is treated as structural drift.

---

## **4. Structural Classification Layer**

Products are organized using:

- hierarchical categories  
- dimensional attributes  
- structural clusters  
- canonical item types  

Classification is drift‑bounded and coherence‑declared.

### **4.1 Category Hierarchy**

Categories must:

- follow canonical structure  
- maintain stable parent/child relationships  
- avoid semantic drift  
- remain operator‑aligned  

### **4.2 Dimensional Attributes**

Attributes describe:

- physical properties  
- functional properties  
- variant differences  
- structural relationships  

Attributes must be canonical and non‑ambiguous.

---

## **5. Governance & Drift Control**

OpenCatalog enforces strict governance rules inherited from OpenWarden.

### **5.1 Drift Types**

- **Structural Drift** — hierarchy corruption  
- **Metadata Drift** — malformed or missing fields  
- **Variant Drift** — lineage confusion  
- **Category Drift** — misclassification  

### **5.2 Drift Responses**

1. **Flag** — mark item as drifted  
2. **Suppress** — remove from catalog output  
3. **Correct** — repair metadata  
4. **Reclassify** — fix category  
5. **Update Lineage** — record correction  

All drift responses are logged.

---

## **6. Operator Grammar Alignment**

OpenCatalog uses the OpenWarden operator grammar:

- **extend** — add structural detail  
- **condense** — simplify hierarchy  
- **refactor** — reorganize metadata  
- **capture** — record lineage or drift  
- **annotate** — add governance notes  
- **correct** — fix drift or misalignment  

Operators ensure safe, reversible catalog evolution.

---

## **7. Cross‑Module Integration**

OpenCatalog integrates with:

- **OpenSEO** — semantic metadata alignment  
- **OpenStream** — recommendation coherence  
- **OpenAdEngine** — product‑aligned ad metadata  
- **OpenRisk** — anomaly detection for catalog drift  
- **OpenIAM** — identity‑safe catalog access rules  
- **OpenGeo** — location‑based catalog metadata  

All integrations are drift‑bounded and coherence‑declared.

---

## **8. Canonical Metadata Block (Example)**

```html
<meta name="open.catalog.item" content="laptop">
<meta name="open.catalog.category" content="electronics.computing">
<meta name="open.catalog.variant" content="v3">
<meta name="open.catalog.lineage" content="itemlineage:4b9e">
<meta name="open.catalog.structure" content="hierarchy:0.92">
<meta name="open.catalog.coherence" content="0.95">
<meta name="open.catalog.drift" content="bounded">
<meta name="open.catalog.version" content="1.0">
<meta name="open.catalog.module" content="OpenCatalog">
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
