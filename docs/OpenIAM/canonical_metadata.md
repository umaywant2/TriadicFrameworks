# 🛡️ **OpenIAM — canonical_metadata.md**  
**OpenWarden Suite — Identity & Access Substrate**  
**Analyzer Layer:** structural  
**Regime:** open‑identity‑governance  
**Version:** 1.0  

---

## **1. Canonical Metadata Overview**

OpenIAM defines the **canonical metadata schema** for all identity and access objects across the OpenWarden suite.  
This metadata ensures:

- identity clarity  
- permission integrity  
- boundary stability  
- coherence declaration  
- drift‑bounded identity evolution  
- lineage transparency  
- operator grammar compliance  

Every identity object must include the fields defined in this document.

---

## **2. Canonical Metadata Fields**

### **2.1 Identity & Role Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.iam.role` | Role signature | `role:admin` |
| `open.iam.identity` | Identity descriptor (optional) | `identity:system-user` |
| `open.iam.scope` | Access scope | `scope:global` |

These fields define the identity and its operational role.

---

### **2.2 Permission Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.iam.permissions` | Permission block | `read:all;write:restricted` |
| `open.iam.boundary` | Access boundary | `boundary:global` |

Permissions must remain canonical, bounded, and reversible.

---

### **2.3 Coherence & Drift Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.iam.coherence` | Coherence score (0–1) | `0.96` |
| `open.iam.drift` | Drift status | `bounded` |

These fields determine stability and drift behavior.

---

### **2.4 Lineage Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.iam.lineage` | Lineage ID | `iamlineage:9d4c` |
| `open.iam.parent` | Parent lineage (optional) | `iamlineage:9d4b` |

Lineage ensures transparency and prevents privilege confusion.

---

### **2.5 Operator Grammar Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.iam.operator.extend` | Operator availability | `true` |
| `open.iam.operator.condense` | Operator availability | `true` |
| `open.iam.operator.refactor` | Operator availability | `true` |
| `open.iam.operator.capture` | Operator availability | `true` |
| `open.iam.operator.annotate` | Operator availability | `true` |
| `open.iam.operator.correct` | Operator availability | `true` |

Operators ensure safe, reversible identity evolution.

---

### **2.6 Module Identity Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.iam.version` | Module version | `1.0` |
| `open.iam.module` | Module name | `OpenIAM` |
| `open.iam.signature` | Structural signature | `openiam-substrate` |

These fields anchor the object to the OpenIAM substrate.

---

## **3. Canonical Metadata Block (Full Example)**

```html
<meta name="open.iam.role" content="role:admin">
<meta name="open.iam.identity" content="identity:system-user">
<meta name="open.iam.scope" content="scope:global">

<meta name="open.iam.permissions" content="read:all;write:restricted">
<meta name="open.iam.boundary" content="boundary:global">

<meta name="open.iam.coherence" content="0.96">
<meta name="open.iam.drift" content="bounded">

<meta name="open.iam.lineage" content="iamlineage:9d4c">
<meta name="open.iam.parent" content="iamlineage:9d4b">

<meta name="open.iam.operator.extend" content="true">
<meta name="open.iam.operator.condense" content="true">
<meta name="open.iam.operator.refactor" content="true">
<meta name="open.iam.operator.capture" content="true">
<meta name="open.iam.operator.annotate" content="true">
<meta name="open.iam.operator.correct" content="true">

<meta name="open.iam.version" content="1.0">
<meta name="open.iam.module" content="OpenIAM">
<meta name="open.iam.signature" content="openiam-substrate">
```

---

## **4. Metadata Validation Rules**

OpenIAM enforces:

- **identity correctness**  
- **permission stability**  
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

OpenIAM metadata aligns with:

- **OpenCatalog** — identity‑safe product access  
- **OpenFeed** — identity‑safe feed rules  
- **OpenGeo** — location‑aware identity boundaries  
- **OpenRisk** — anomaly detection  
- **OpenSEO** — semantic identity metadata  
- **OpenWarden** — suite‑governed identity policies  

All alignment is drift‑bounded and coherence‑declared.

---

## **6. Required Metadata Presence**

Every identity object must include:

- identity & role fields  
- permission fields  
- coherence & drift fields  
- lineage fields  
- operator grammar fields  
- module identity fields  

Missing fields are treated as identity drift.
