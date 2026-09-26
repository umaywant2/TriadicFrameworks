# ⚠️ **OpenRisk — canonical_metadata.md**  
**OpenWarden Suite — Risk Analysis Substrate**  
**Analyzer Layer:** dimensional  
**Regime:** open‑risk‑governance  
**Version:** 1.0  

---

## **1. Canonical Metadata Overview**

OpenRisk defines the **canonical metadata schema** for all risk objects across the OpenWarden suite.  
This metadata ensures:

- dimensional clarity  
- risk score correctness  
- severity stability  
- coherence declaration  
- drift‑bounded risk behavior  
- lineage transparency  
- operator grammar compliance  

Every risk object must include the fields defined in this document.

---

## **2. Canonical Metadata Fields**

### **2.1 Dimensional & Risk Identity Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.risk.dimension` | Dimensional category | `risk:fraud-detection` |
| `open.risk.type` | Risk type descriptor (optional) | `type:transactional` |
| `open.risk.context` | Context descriptor | `context:ecommerce` |

These fields define the risk object’s dimensional identity.

---

### **2.2 Risk Score & Severity Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.risk.score` | Canonical risk score | `score:0.72` |
| `open.risk.severity` | Severity descriptor | `severity:medium` |
| `open.risk.boundary` | Severity boundary | `boundary:moderate` |

Risk scores must remain canonical, bounded, and reversible.

---

### **2.3 Coherence & Drift Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.risk.coherence` | Coherence score (0–1) | `0.91` |
| `open.risk.drift` | Drift status | `bounded` |

These fields determine stability and drift behavior.

---

### **2.4 Lineage Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.risk.lineage` | Lineage ID | `risklineage:7c3f` |
| `open.risk.parent` | Parent lineage (optional) | `risklineage:7c3e` |

Lineage ensures transparency and prevents risk confusion.

---

### **2.5 Operator Grammar Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.risk.operator.extend` | Operator availability | `true` |
| `open.risk.operator.condense` | Operator availability | `true` |
| `open.risk.operator.refactor` | Operator availability | `true` |
| `open.risk.operator.capture` | Operator availability | `true` |
| `open.risk.operator.annotate` | Operator availability | `true` |
| `open.risk.operator.correct` | Operator availability | `true` |

Operators ensure safe, reversible risk evolution.

---

### **2.6 Module Identity Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.risk.version` | Module version | `1.0` |
| `open.risk.module` | Module name | `OpenRisk` |
| `open.risk.signature` | Dimensional signature | `openrisk-substrate` |

These fields anchor the object to the OpenRisk substrate.

---

## **3. Canonical Metadata Block (Full Example)**

```html
<meta name="open.risk.dimension" content="risk:fraud-detection">
<meta name="open.risk.type" content="type:transactional">
<meta name="open.risk.context" content="context:ecommerce">

<meta name="open.risk.score" content="score:0.72">
<meta name="open.risk.severity" content="severity:medium">
<meta name="open.risk.boundary" content="boundary:moderate">

<meta name="open.risk.coherence" content="0.91">
<meta name="open.risk.drift" content="bounded">

<meta name="open.risk.lineage" content="risklineage:7c3f">
<meta name="open.risk.parent" content="risklineage:7c3e">

<meta name="open.risk.operator.extend" content="true">
<meta name="open.risk.operator.condense" content="true">
<meta name="open.risk.operator.refactor" content="true">
<meta name="open.risk.operator.capture" content="true">
<meta name="open.risk.operator.annotate" content="true">
<meta name="open.risk.operator.correct" content="true">

<meta name="open.risk.version" content="1.0">
<meta name="open.risk.module" content="OpenRisk">
<meta name="open.risk.signature" content="openrisk-substrate">
```

---

## **4. Metadata Validation Rules**

OpenRisk enforces:

- **dimensional correctness**  
- **risk score stability**  
- **severity coherence**  
- **lineage integrity**  
- **operator grammar compliance**  
- **drift‑bounded updates**  

Metadata violations trigger:

- drift flag  
- suppression  
- correction  
- lineage update  

---

## **5. Cross‑Module Metadata Alignment**

OpenRisk metadata aligns with:

- **OpenIAM** — identity‑safe risk rules  
- **OpenGeo** — location‑aware risk boundaries  
- **OpenFeed** — risk‑aware feed filtering  
- **OpenCatalog** — risk metadata alignment  
- **OpenSEO** — semantic risk metadata  
- **OpenLLM** — model‑aware anomaly detection  
- **OpenWarden** — suite‑governed risk policies  

All alignment is drift‑bounded and coherence‑declared.

---

## **6. Required Metadata Presence**

Every risk object must include:

- dimensional fields  
- risk score & severity fields  
- coherence & drift fields  
- lineage fields  
- operator grammar fields  
- module identity fields  

Missing fields are treated as dimensional drift.
