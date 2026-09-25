# 🛒 **OpenCatalog — canonical_metadata.md**  
**OpenWarden Suite — Product Catalog Substrate**  
**Analyzer Layer:** structural  
**Regime:** open‑catalog-governance  
**Version:** 1.0  

---

## **1. Canonical Metadata Overview**

OpenCatalog defines the **canonical metadata schema** for all catalog items across the OpenWarden suite.  
This metadata ensures:

- structural integrity  
- variant clarity  
- lineage transparency  
- drift‑bounded updates  
- operator grammar compliance  
- AI‑ready catalog fields  

Every item must include the fields defined in this document.

---

## **2. Canonical Metadata Fields**

### **2.1 Structural Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.catalog.item` | Item identity | `laptop` |
| `open.catalog.category` | Hierarchical category | `electronics.computing` |
| `open.catalog.structure` | Structural coherence score | `hierarchy:0.92` |
| `open.catalog.attributes` | Dimensional attributes | `ram:32gb;cpu:ryzen7` |

Structural fields define the item’s place in the catalog hierarchy.

---

### **2.2 Variant Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.catalog.variant` | Variant identifier | `v3` |
| `open.catalog.lineage` | Lineage ID | `itemlineage:4b9e` |
| `open.catalog.parent` | Parent variant (optional) | `v2` |

Variant fields ensure clarity across product evolutions.

---

### **2.3 Governance Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.catalog.coherence` | Coherence score (0–1) | `0.95` |
| `open.catalog.drift` | Drift status | `bounded` |
| `open.catalog.policy` | Governance policy tag | `openwarden-suite` |

Governance fields allow drift detection, correction, and lineage tracking.

---

### **2.4 Operator Grammar Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.catalog.operator.extend` | Operator availability | `true` |
| `open.catalog.operator.condense` | Operator availability | `true` |
| `open.catalog.operator.refactor` | Operator availability | `true` |
| `open.catalog.operator.capture` | Operator availability | `true` |
| `open.catalog.operator.annotate` | Operator availability | `true` |
| `open.catalog.operator.correct` | Operator availability | `true` |

Operators ensure safe, reversible catalog transformations.

---

### **2.5 Module Identity Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.catalog.version` | Module version | `1.0` |
| `open.catalog.module` | Module name | `OpenCatalog` |
| `open.catalog.signature` | Structural signature | `opencatalog-substrate` |

These fields anchor the item to the OpenCatalog substrate.

---

## **3. Canonical Metadata Block (Full Example)**

```html
<meta name="open.catalog.item" content="laptop">
<meta name="open.catalog.category" content="electronics.computing">
<meta name="open.catalog.structure" content="hierarchy:0.92">
<meta name="open.catalog.attributes" content="ram:32gb;cpu:ryzen7">

<meta name="open.catalog.variant" content="v3">
<meta name="open.catalog.lineage" content="itemlineage:4b9e">
<meta name="open.catalog.parent" content="v2">

<meta name="open.catalog.coherence" content="0.95">
<meta name="open.catalog.drift" content="bounded">
<meta name="open.catalog.policy" content="openwarden-suite">

<meta name="open.catalog.operator.extend" content="true">
<meta name="open.catalog.operator.condense" content="true">
<meta name="open.catalog.operator.refactor" content="true">
<meta name="open.catalog.operator.capture" content="true">
<meta name="open.catalog.operator.annotate" content="true">
<meta name="open.catalog.operator.correct" content="true">

<meta name="open.catalog.version" content="1.0">
<meta name="open.catalog.module" content="OpenCatalog">
<meta name="open.catalog.signature" content="opencatalog-substrate">
```

---

## **4. Metadata Validation Rules**

OpenCatalog enforces:

- **canonical structure**  
- **complete metadata**  
- **variant lineage integrity**  
- **operator grammar compliance**  
- **drift‑bounded updates**  

Metadata violations trigger:

- drift flag  
- suppression  
- correction  
- lineage update  

---

## **5. Cross‑Module Metadata Alignment**

OpenCatalog metadata aligns with:

- **OpenSEO** — semantic metadata  
- **OpenStream** — recommendation coherence  
- **OpenAdEngine** — product‑aligned ad metadata  
- **OpenRisk** — anomaly detection  
- **OpenIAM** — identity‑safe access rules  
- **OpenGeo** — location‑based metadata  

All alignment is drift‑bounded and coherence‑declared.

---

## **6. Required Metadata Presence**

Every item must include:

- structural fields  
- variant fields  
- governance fields  
- operator grammar fields  
- module identity fields  

Missing fields are treated as structural drift.
