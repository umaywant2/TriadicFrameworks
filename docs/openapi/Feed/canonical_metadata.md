# 📡 **OpenFeed — canonical_metadata.md**  
**OpenWarden Suite — Social Feed Substrate**  
**Analyzer Layer:** semantic  
**Regime:** open‑feed-governance  
**Version:** 1.0  

---

## **1. Canonical Metadata Overview**

OpenFeed defines the **canonical metadata schema** for all feed items across the OpenWarden suite.  
This metadata ensures:

- semantic clarity  
- contextual alignment  
- resonance stability  
- coherence declaration  
- lineage transparency  
- drift‑bounded ranking  
- operator grammar compliance  

Every feed item must include the fields defined in this document.

---

## **2. Canonical Metadata Fields**

### **2.1 Semantic & Contextual Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.feed.semantic` | Semantic topic cluster | `topic:ai` |
| `open.feed.contextual` | Contextual category | `context:research` |
| `open.feed.intent` | Declared intent | `informational` |

These fields define the meaning and context of the feed item.

---

### **2.2 Resonance & Coherence Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.feed.resonance` | Resonance score (0–1) | `0.89` |
| `open.feed.coherence` | Coherence score (0–1) | `0.93` |

These fields determine ranking stability and semantic alignment.

---

### **2.3 Lineage Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.feed.lineage` | Lineage ID | `feedlineage:7c2f` |
| `open.feed.parent` | Parent lineage (optional) | `feedlineage:7c2e` |

Lineage ensures transparency and prevents feed manipulation.

---

### **2.4 Governance Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.feed.drift` | Drift status | `bounded` |
| `open.feed.policy` | Governance policy tag | `openwarden-suite` |

Governance fields allow drift detection, correction, and auditability.

---

### **2.5 Operator Grammar Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.feed.operator.extend` | Operator availability | `true` |
| `open.feed.operator.condense` | Operator availability | `true` |
| `open.feed.operator.refactor` | Operator availability | `true` |
| `open.feed.operator.capture` | Operator availability | `true` |
| `open.feed.operator.annotate` | Operator availability | `true` |
| `open.feed.operator.correct` | Operator availability | `true` |

Operators ensure safe, reversible feed evolution.

---

### **2.6 Module Identity Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.feed.version` | Module version | `1.0` |
| `open.feed.module` | Module name | `OpenFeed` |
| `open.feed.signature` | Semantic signature | `openfeed-substrate` |

These fields anchor the item to the OpenFeed substrate.

---

## **3. Canonical Metadata Block (Full Example)**

```html
<meta name="open.feed.semantic" content="topic:ai">
<meta name="open.feed.contextual" content="context:research">
<meta name="open.feed.intent" content="informational">

<meta name="open.feed.resonance" content="0.89">
<meta name="open.feed.coherence" content="0.93">

<meta name="open.feed.lineage" content="feedlineage:7c2f">
<meta name="open.feed.parent" content="feedlineage:7c2e">

<meta name="open.feed.drift" content="bounded">
<meta name="open.feed.policy" content="openwarden-suite">

<meta name="open.feed.operator.extend" content="true">
<meta name="open.feed.operator.condense" content="true">
<meta name="open.feed.operator.refactor" content="true">
<meta name="open.feed.operator.capture" content="true">
<meta name="open.feed.operator.annotate" content="true">
<meta name="open.feed.operator.correct" content="true">

<meta name="open.feed.version" content="1.0">
<meta name="open.feed.module" content="OpenFeed">
<meta name="open.feed.signature" content="openfeed-substrate">
```

---

## **4. Metadata Validation Rules**

OpenFeed enforces:

- **semantic correctness**  
- **contextual alignment**  
- **resonance stability**  
- **coherence declaration**  
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

OpenFeed metadata aligns with:

- **OpenSEO** — semantic operators  
- **OpenSoN** — social context metadata  
- **OpenStream** — recommendation coherence  
- **OpenCatalog** — product metadata alignment  
- **OpenRisk** — anomaly detection  
- **OpenIAM** — identity‑safe feed rules  

All alignment is drift‑bounded and coherence‑declared.

---

## **6. Required Metadata Presence**

Every feed item must include:

- semantic fields  
- contextual fields  
- resonance & coherence fields  
- lineage fields  
- governance fields  
- operator grammar fields  
- module identity fields  

Missing fields are treated as semantic drift.
