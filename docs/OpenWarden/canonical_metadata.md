# 🛡️ **OpenWarden — canonical_metadata.md**  
**OpenWarden Suite Root — Governance, Drift, Metadata & Structural Stewardship**  
**Analyzer Layer:** suite‑governance  
**Regime:** open‑warden‑substrate  
**Version:** 1.0  

---

## **1. Canonical Metadata Overview**

OpenWarden defines the **canonical metadata schema** for the entire OpenWarden suite.  
This metadata ensures:

- suite identity clarity  
- governance correctness  
- drift taxonomy stability  
- coherence declaration  
- lineage transparency  
- operator grammar compliance  
- cross‑module interoperability  

Every module must include the fields defined in this document.

---

## **2. Canonical Metadata Fields**

### **2.1 Suite Identity Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.warden.signature` | Suite signature | `suite:openwarden-root` |
| `open.warden.governance` | Governance regime | `governance:open-warden-substrate` |
| `open.warden.context` | Optional suite context | `context:triadicframeworks` |

These fields define the suite’s identity and governance substrate.

---

### **2.2 Coherence & Drift Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.warden.coherence` | Coherence score (0–1) | `1.0` |
| `open.warden.drift` | Drift status | `bounded` |

These fields determine suite stability and drift behavior.

---

### **2.3 Lineage Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.warden.lineage` | Suite lineage ID | `wardenlineage:root` |
| `open.warden.parent` | Parent lineage (optional) | `none` |

Lineage ensures transparency and prevents suite confusion.

---

### **2.4 Operator Grammar Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.warden.operator.extend` | Operator availability | `true` |
| `open.warden.operator.condense` | Operator availability | `true` |
| `open.warden.operator.refactor` | Operator availability | `true` |
| `open.warden.operator.capture` | Operator availability | `true` |
| `open.warden.operator.annotate` | Operator availability | `true` |
| `open.warden.operator.correct` | Operator availability | `true` |

Operators ensure safe, reversible suite evolution.

---

### **2.5 Module Identity Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.warden.version` | Suite version | `1.0` |
| `open.warden.module` | Module name | `OpenWarden` |
| `open.warden.signature.structural` | Structural signature | `openwarden-substrate` |

These fields anchor all modules to the OpenWarden substrate.

---

## **3. Canonical Metadata Block (Full Example)**

```html
<meta name="open.warden.signature" content="suite:openwarden-root">
<meta name="open.warden.governance" content="governance:open-warden-substrate">
<meta name="open.warden.context" content="context:triadicframeworks">

<meta name="open.warden.coherence" content="1.0">
<meta name="open.warden.drift" content="bounded">

<meta name="open.warden.lineage" content="wardenlineage:root">
<meta name="open.warden.parent" content="none">

<meta name="open.warden.operator.extend" content="true">
<meta name="open.warden.operator.condense" content="true">
<meta name="open.warden.operator.refactor" content="true">
<meta name="open.warden.operator.capture" content="true">
<meta name="open.warden.operator.annotate" content="true">
<meta name="open.warden.operator.correct" content="true">

<meta name="open.warden.version" content="1.0">
<meta name="open.warden.module" content="OpenWarden">
<meta name="open.warden.signature.structural" content="openwarden-substrate">
```

---

## **4. Metadata Validation Rules**

OpenWarden enforces:

- **suite identity correctness**  
- **governance stability**  
- **drift taxonomy coherence**  
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

OpenWarden metadata governs and aligns:

- **OpenIAM** — identity substrate  
- **OpenGeo** — geospatial substrate  
- **OpenLLM** — model substrate  
- **OpenRisk** — risk substrate  
- **OpenStream** — streaming substrate  
- **OpenVitals** — physiological substrate  
- **OpenFeed** — feed substrate  
- **OpenCatalog** — metadata substrate  
- **OpenSEO** — semantic substrate  
- **OpenAdEngine** — advertising substrate  
- **OpenSoN** — social substrate  

All alignment is drift‑bounded and coherence‑declared.

---

## **6. Required Metadata Presence**

Every module must include:

- suite identity fields  
- coherence & drift fields  
- lineage fields  
- operator grammar fields  
- module identity fields  

Missing fields are treated as suite drift.
