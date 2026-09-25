# 🫀 **OpenVitals — canonical_metadata.md**  
**OpenWarden Suite — Health & Physiological Signal Substrate**  
**Analyzer Layer:** dimensional  
**Regime:** open‑vitals‑governance  
**Version:** 1.0  

---

## **1. Canonical Metadata Overview**

OpenVitals defines the **canonical metadata schema** for all physiological signals across the OpenWarden suite.  
This metadata ensures:

- dimensional identity clarity  
- vital metric correctness  
- boundary stability  
- coherence declaration  
- drift‑bounded physiological behavior  
- lineage transparency  
- operator grammar compliance  

Every vital signal must include the fields defined in this document.

---

## **2. Canonical Metadata Fields**

### **2.1 Vital Identity Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.vitals.signature` | Vital signature | `vital:openvitals-core` |
| `open.vitals.metric` | Vital metric descriptor | `metric:heart-rate` |
| `open.vitals.context` | Context descriptor (optional) | `context:resting` |

These fields define the physiological signal’s identity.

---

### **2.2 Boundary & Interpretation Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.vitals.boundary` | Interpretation boundary | `boundary:physio-safe` |
| `open.vitals.stability` | Stability descriptor | `stability:high` |
| `open.vitals.range` | Expected physiological range | `range:60-100` |

Boundaries must remain canonical, bounded, and reversible.

---

### **2.3 Coherence & Drift Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.vitals.coherence` | Coherence score (0–1) | `0.92` |
| `open.vitals.drift` | Drift status | `bounded` |

These fields determine stability and drift behavior.

---

### **2.4 Lineage Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.vitals.lineage` | Lineage ID | `vitalslineage:3f9a` |
| `open.vitals.parent` | Parent lineage (optional) | `vitalslineage:3f99` |

Lineage ensures transparency and prevents signal confusion.

---

### **2.5 Operator Grammar Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.vitals.operator.extend` | Operator availability | `true` |
| `open.vitals.operator.condense` | Operator availability | `true` |
| `open.vitals.operator.refactor` | Operator availability | `true` |
| `open.vitals.operator.capture` | Operator availability | `true` |
| `open.vitals.operator.annotate` | Operator availability | `true` |
| `open.vitals.operator.correct` | Operator availability | `true` |

Operators ensure safe, reversible physiological evolution.

---

### **2.6 Module Identity Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.vitals.version` | Module version | `1.0` |
| `open.vitals.module` | Module name | `OpenVitals` |
| `open.vitals.signature.structural` | Structural signature | `openvitals-substrate` |

These fields anchor the object to the OpenVitals substrate.

---

## **3. Canonical Metadata Block (Full Example)**

```html
<meta name="open.vitals.signature" content="vital:openvitals-core">
<meta name="open.vitals.metric" content="metric:heart-rate">
<meta name="open.vitals.context" content="context:resting">

<meta name="open.vitals.boundary" content="boundary:physio-safe">
<meta name="open.vitals.stability" content="stability:high">
<meta name="open.vitals.range" content="range:60-100">

<meta name="open.vitals.coherence" content="0.92">
<meta name="open.vitals.drift" content="bounded">

<meta name="open.vitals.lineage" content="vitalslineage:3f9a">
<meta name="open.vitals.parent" content="vitalslineage:3f99">

<meta name="open.vitals.operator.extend" content="true">
<meta name="open.vitals.operator.condense" content="true">
<meta name="open.vitals.operator.refactor" content="true">
<meta name="open.vitals.operator.capture" content="true">
<meta name="open.vitals.operator.annotate" content="true">
<meta name="open.vitals.operator.correct" content="true">

<meta name="open.vitals.version" content="1.0">
<meta name="open.vitals.module" content="OpenVitals">
<meta name="open.vitals.signature.structural" content="openvitals-substrate">
```

---

## **4. Metadata Validation Rules**

OpenVitals enforces:

- **dimensional correctness**  
- **vital metric stability**  
- **boundary coherence**  
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

OpenVitals metadata aligns with:

- **OpenRisk** — anomaly detection for physiological drift  
- **OpenIAM** — identity‑safe health‑signal access  
- **OpenGeo** — location‑aware physiological interpretation  
- **OpenFeed** — health‑signal‑aware feed rules  
- **OpenCatalog** — vital metadata alignment  
- **OpenLLM** — model‑aware physiological interpretation  
- **OpenWarden** — suite‑governed health‑signal policies  

All alignment is drift‑bounded and coherence‑declared.

---

## **6. Required Metadata Presence**

Every vital signal must include:

- identity fields  
- boundary & interpretation fields  
- coherence & drift fields  
- lineage fields  
- operator grammar fields  
- module identity fields  

Missing fields are treated as physiological drift.
