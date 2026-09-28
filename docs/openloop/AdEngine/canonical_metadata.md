# 📢 **OpenAdEngine — canonical_metadata.md**  
**OpenWarden Suite — Contextual Advertising Substrate**  
**Version:** 1.0  
**Regime:** open‑ad‑governance  
**Analyzer Layer:** semantic  

---

## **1. Canonical Metadata Overview**

OpenAdEngine requires a **strict, drift‑bounded, coherence‑declared metadata block** for all ads delivered within the OpenWarden suite.  
This metadata ensures:

- transparency  
- operator alignment  
- resonance stability  
- contextual correctness  
- AI‑readiness  
- drift detection  

All fields are **mandatory** unless explicitly marked optional.

---

## **2. Canonical Metadata Fields**

### **2.1 Dimensional Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.ad.dimension.semantic` | Semantic topic cluster | `semantic:software` |
| `open.ad.dimension.contextual` | Page/module context | `contextual:developer-tools` |
| `open.ad.dimension.resonance` | Resonance score (0–1) | `0.91` |
| `open.ad.dimension.intent` | Intent category | `transactional` |

These fields define the **identity** of the ad.

---

### **2.2 Structural Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.ad.structure.hierarchy` | Structural alignment score | `0.93` |
| `open.ad.structure.category` | Non‑personal audience category | `semantic:developers` |
| `open.ad.structure.variant` | Optional variant tag | `v2` |

Structural fields ensure predictable behavior across modules.

---

### **2.3 Governance Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.ad.coherence` | Coherence score (0–1) | `0.94` |
| `open.ad.drift` | Drift status | `bounded` |
| `open.ad.lineage` | Lineage identifier | `adlineage:7f2c` |
| `open.ad.policy` | Governance policy tag | `openwarden-suite` |

These fields allow drift detection, correction, and lineage tracking.

---

### **2.4 Operator Grammar Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.ad.operator.extend` | Operator availability | `true` |
| `open.ad.operator.condense` | Operator availability | `true` |
| `open.ad.operator.refactor` | Operator availability | `true` |
| `open.ad.operator.capture` | Operator availability | `true` |
| `open.ad.operator.annotate` | Operator availability | `true` |
| `open.ad.operator.correct` | Operator availability | `true` |

These fields ensure ads follow the same operator grammar as other OpenWarden modules.

---

### **2.5 Module Identity Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.ad.version` | Module version | `1.0` |
| `open.ad.module` | Module name | `OpenAdEngine` |
| `open.ad.signature` | Dimensional signature | `openadengine-substrate` |

These fields anchor the ad to the OpenAdEngine substrate.

---

## **3. Canonical Metadata Block (Full Example)**

```html
<meta name="open.ad.dimension.semantic" content="semantic:software">
<meta name="open.ad.dimension.contextual" content="contextual:developer-tools">
<meta name="open.ad.dimension.resonance" content="0.91">
<meta name="open.ad.dimension.intent" content="transactional">

<meta name="open.ad.structure.hierarchy" content="0.93">
<meta name="open.ad.structure.category" content="semantic:developers">
<meta name="open.ad.structure.variant" content="v2">

<meta name="open.ad.coherence" content="0.94">
<meta name="open.ad.drift" content="bounded">
<meta name="open.ad.lineage" content="adlineage:7f2c">
<meta name="open.ad.policy" content="openwarden-suite">

<meta name="open.ad.operator.extend" content="true">
<meta name="open.ad.operator.condense" content="true">
<meta name="open.ad.operator.refactor" content="true">
<meta name="open.ad.operator.capture" content="true">
<meta name="open.ad.operator.annotate" content="true">
<meta name="open.ad.operator.correct" content="true">

<meta name="open.ad.version" content="1.0">
<meta name="open.ad.module" content="OpenAdEngine">
<meta name="open.ad.signature" content="openadengine-substrate">
```

---

## **4. Metadata Validation Rules**

OpenAdEngine enforces:

- **no personal data**  
- **no behavioral inference**  
- **no sensitive categories**  
- **no cross‑site tracking**  
- **no non‑canonical fields**  
- **no adversarial resonance injection**  

Metadata must be:

- drift‑bounded  
- coherence‑declared  
- operator‑aligned  
- suite‑governed  

---

## **5. Cross‑Module Metadata Alignment**

OpenAdEngine metadata aligns with:

- **OpenSEO** (semantic operators)  
- **OpenSoN** (social context)  
- **OpenStream** (recommendation coherence)  
- **OpenCatalog** (product metadata)  
- **OpenRisk** (anomaly detection)  
- **OpenIAM** (identity‑safe delivery rules)  

All alignment is drift‑bounded and lineage‑tracked.

---

## **6. Required Metadata Presence**

Every ad must include:

- dimensional fields  
- structural fields  
- governance fields  
- operator grammar fields  
- module identity fields  

Missing fields trigger:

- drift flag  
- suppression  
- correction  
- lineage update  
