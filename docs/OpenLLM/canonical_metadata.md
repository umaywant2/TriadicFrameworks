# 🤖 **OpenLLM — canonical_metadata.md**  
**OpenWarden Suite — Large Language Model Substrate**  
**Analyzer Layer:** semantic‑structural  
**Regime:** open‑llm‑governance  
**Version:** 1.0  

---

## **1. Canonical Metadata Overview**

OpenLLM defines the **canonical metadata schema** for all large language models across the OpenWarden suite.  
This metadata ensures:

- model identity clarity  
- parameter correctness  
- inference boundary stability  
- coherence declaration  
- drift‑bounded model behavior  
- lineage transparency  
- operator grammar compliance  

Every LLM must include the fields defined in this document.

---

## **2. Canonical Metadata Fields**

### **2.1 Model Identity Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.llm.signature` | Model signature | `model:openllm-core` |
| `open.llm.family` | Model family (optional) | `family:transformer` |
| `open.llm.variant` | Variant descriptor | `variant:7b` |

These fields define the model’s identity and structural lineage.

---

### **2.2 Parameter Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.llm.parameters` | Parameter block | `params:7b` |
| `open.llm.context` | Context window | `context:32k` |
| `open.llm.embedding` | Embedding dimension (optional) | `embed:4096` |

Parameters must remain canonical, bounded, and reversible.

---

### **2.3 Inference Boundary Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.llm.boundary` | Inference boundary | `boundary:semantic-safe` |
| `open.llm.mode` | Inference mode | `mode:structured` |

Boundaries define safe operational constraints.

---

### **2.4 Coherence & Drift Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.llm.coherence` | Coherence score (0–1) | `0.95` |
| `open.llm.drift` | Drift status | `bounded` |

These fields determine stability and drift behavior.

---

### **2.5 Lineage Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.llm.lineage` | Lineage ID | `llmlineage:4a2d` |
| `open.llm.parent` | Parent lineage (optional) | `llmlineage:4a2c` |

Lineage ensures transparency and prevents model confusion.

---

### **2.6 Operator Grammar Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.llm.operator.extend` | Operator availability | `true` |
| `open.llm.operator.condense` | Operator availability | `true` |
| `open.llm.operator.refactor` | Operator availability | `true` |
| `open.llm.operator.capture` | Operator availability | `true` |
| `open.llm.operator.annotate` | Operator availability | `true` |
| `open.llm.operator.correct` | Operator availability | `true` |

Operators ensure safe, reversible model evolution.

---

### **2.7 Module Identity Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.llm.version` | Module version | `1.0` |
| `open.llm.module` | Module name | `OpenLLM` |
| `open.llm.signature.structural` | Structural signature | `openllm-substrate` |

These fields anchor the model to the OpenLLM substrate.

---

## **3. Canonical Metadata Block (Full Example)**

```html
<meta name="open.llm.signature" content="model:openllm-core">
<meta name="open.llm.family" content="family:transformer">
<meta name="open.llm.variant" content="variant:7b">

<meta name="open.llm.parameters" content="params:7b">
<meta name="open.llm.context" content="context:32k">
<meta name="open.llm.embedding" content="embed:4096">

<meta name="open.llm.boundary" content="boundary:semantic-safe">
<meta name="open.llm.mode" content="mode:structured">

<meta name="open.llm.coherence" content="0.95">
<meta name="open.llm.drift" content="bounded">

<meta name="open.llm.lineage" content="llmlineage:4a2d">
<meta name="open.llm.parent" content="llmlineage:4a2c">

<meta name="open.llm.operator.extend" content="true">
<meta name="open.llm.operator.condense" content="true">
<meta name="open.llm.operator.refactor" content="true">
<meta name="open.llm.operator.capture" content="true">
<meta name="open.llm.operator.annotate" content="true">
<meta name="open.llm.operator.correct" content="true">

<meta name="open.llm.version" content="1.0">
<meta name="open.llm.module" content="OpenLLM">
<meta name="open.llm.signature.structural" content="openllm-substrate">
```

---

## **4. Metadata Validation Rules**

OpenLLM enforces:

- **model identity correctness**  
- **parameter stability**  
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

OpenLLM metadata aligns with:

- **OpenSEO** — semantic metadata alignment  
- **OpenFeed** — LLM‑safe feed rules  
- **OpenGeo** — location‑aware inference boundaries  
- **OpenIAM** — identity‑safe model access  
- **OpenRisk** — anomaly detection  
- **OpenCatalog** — model metadata alignment  
- **OpenWarden** — suite‑governed model policies  

All alignment is drift‑bounded and coherence‑declared.

---

## **6. Required Metadata Presence**

Every LLM must include:

- model identity fields  
- parameter fields  
- inference boundary fields  
- coherence & drift fields  
- lineage fields  
- operator grammar fields  
- module identity fields  

Missing fields are treated as semantic drift.
