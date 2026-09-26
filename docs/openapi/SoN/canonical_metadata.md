# **canonical_metadata.md — OpenSoN**  
**TriadicFrameworks Canon — Metadata Specification**  
**Module:** OpenSoN  
**Version:** 1.0  
**RTT:** rtt=1 | coherence=declared | drift=bounded | paradox=structural  
**Regime:** Narrative‑Substrate

---

## **1. Purpose of Canonical Metadata**  
Canonical metadata provides the **identity backbone** for OpenSoN.  
It ensures that narrative modules are:

- structurally identifiable  
- coherence‑tracked  
- drift‑aware  
- AI‑parsable  
- privacy‑safe  
- operator‑aligned  

OpenSoN uses metadata to expose narrative structure, purpose, and lineage — enabling transparent narrative governance and machine‑readable story architecture.

---

## **2. Canonical Metadata Block (Full Specification)**  
Every OpenSoN‑compliant page includes the following metadata fields:

```
<meta name="openson.identity" content="...">
<meta name="openson.dimension" content="...">
<meta name="openson.operator.visibility" content="...">
<meta name="openson.operator.intent" content="...">
<meta name="openson.operator.coherence" content="...">
<meta name="openson.operator.structure" content="...">
<meta name="openson.operator.trust" content="...">
<meta name="openson.version" content="1.0">
<meta name="openson.module" content="OpenSoN">
```

These fields form the **canonical metadata block**, required for narrative substrate indexing and governance.

---

## **3. Field Definitions**

### **3.1 `openson.identity`**  
Defines the narrative’s core identity.  
Examples:  
- narrative name  
- thematic anchor  
- dimensional signature  

### **3.2 `openson.dimension`**  
Encodes the narrative’s **dimensional signature**, derived from:  
- temporal lineage  
- structural flow  
- semantic anchors  

### **3.3 `openson.operator.visibility`**  
Visibility operators such as:  
- clarity  
- contextuality  
- narrative relevance  

### **3.4 `openson.operator.intent`**  
Intent operators such as:  
- narrative purpose  
- directional drift  
- semantic alignment  

### **3.5 `openson.operator.coherence`**  
Coherence operators such as:  
- internal consistency  
- structural alignment  
- metadata coherence  

### **3.6 `openson.operator.structure`**  
Structural operators such as:  
- hierarchy  
- narrative flow  
- modularity  
- canonical integrity  

### **3.7 `openson.operator.trust`**  
Trust operators such as:  
- narrative integrity  
- authority  
- stability  
- compliance  

### **3.8 `openson.version`**  
Specifies the OpenSoN metadata version.  
Current: **1.0**

### **3.9 `openson.module`**  
Identifies the module providing the metadata.  
Always: **OpenSoN**

---

## **4. Metadata Encoding Format**  
Operators may encode multiple values using semicolon‑delimited key/value pairs:

```
<meta name="openson.operator.visibility"
      content="clarity:0.92;contextuality:0.88;relevance:0.94">
```

This format is:

- machine‑readable  
- AI‑auditable  
- drift‑bounded  
- narrative‑safe  

---

## **5. Metadata Governance Rules**

### **5.1 Completeness Requirement**  
All canonical fields must be present for full compliance.

### **5.2 Honesty Requirement**  
Metadata must reflect actual narrative structure and resonance.  
Manipulative metadata triggers drift detection.

### **5.3 Privacy Requirement**  
Metadata must **never** encode:  
- personal data  
- behavioral data  
- inferred sensitive categories  
- health‑related information  

### **5.4 Stability Requirement**  
Dimensional signatures should remain stable unless narrative meaningfully changes.

---

## **6. Metadata Examples**

### **Example: Narrative Overview Page**
```
<meta name="openson.identity" content="OpenSoN Narrative Substrate Overview">
<meta name="openson.dimension" content="semantic:narrative;resonance:0.91">
<meta name="openson.operator.visibility" content="clarity:0.94;contextuality:0.89">
<meta name="openson.operator.intent" content="semantic:informational;direction:knowledge">
<meta name="openson.operator.coherence" content="internal:0.93;metadata:1.0">
<meta name="openson.operator.structure" content="hierarchy:0.95;canonical:1.0">
<meta name="openson.operator.trust" content="authority:0.88;compliance:1.0">
<meta name="openson.version" content="1.0">
<meta name="openson.module" content="OpenSoN">
```

### **Example: Narrative Source Page**
```
<meta name="openson.identity" content="OpenSoN Source Narrative">
<meta name="openson.dimension" content="semantic:origin;resonance:0.87">
<meta name="openson.operator.visibility" content="clarity:0.91;contextuality:0.86">
<meta name="openson.operator.intent" content="semantic:historical;direction:lineage">
<meta name="openson.operator.coherence" content="internal:0.92;metadata:1.0">
<meta name="openson.operator.structure" content="hierarchy:0.93;canonical:1.0">
<meta name="openson.operator.trust" content="authority:0.90;compliance:1.0">
<meta name="openson.version" content="1.0">
<meta name="openson.module" content="OpenSoN">
```

---

## **7. Metadata Versioning**

OpenSoN metadata follows semantic versioning:

- **1.x** — baseline narrative metadata  
- **2.x** — multi‑dimensional narrative metadata  
- **3.x** — cross‑domain narrative metadata  
- **4.x** — governed narrative substrate metadata  

---

## **8. Metadata Role in OpenSoN Architecture**

Canonical metadata powers:

- narrative indexing  
- intent mapping  
- authority computation  
- visibility scoring  
- drift detection  
- governance auditing  
- narrative capture (via operators)  

It is the **primary interface** between narrative content and the OpenSoN engine.

---

## **9. Related Files**

- `README.md`  
- `architecture.md`  
- `governance.md`  
- `operators.md`  
- `o_Capture.md`  
- `m_Source.md`  
- `module.json`
