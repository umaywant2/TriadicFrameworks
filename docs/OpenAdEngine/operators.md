# 📢 **OpenAdEngine — operators.md**  
**OpenWarden Suite — Contextual Advertising Substrate**  
**Version:** 1.0  
**Analyzer Layer:** semantic  
**Regime:** open‑ad‑governance  

---

## **1. Operator Grammar Overview**

OpenAdEngine uses the **OpenWarden operator grammar**, ensuring ads behave predictably, ethically, and coherently across all substrates.  
Operators define how ads may be:

- transformed  
- interpreted  
- corrected  
- aligned  
- condensed  
- extended  

Every operator is **drift‑bounded**, **coherence‑declared**, and **metadata‑safe**.

---

## **2. Operator Categories**

OpenAdEngine supports six canonical operator classes:

1. **Extend**  
2. **Condense**  
3. **Refactor**  
4. **Capture**  
5. **Annotate**  
6. **Correct**

Each operator is described below with ad‑specific semantics.

---

## **3. Extend Operator**

### **Purpose**  
Adds **contextual or semantic detail** to an ad’s metadata without altering its declared intent.

### **Allowed Extensions**  
- semantic cluster refinement  
- contextual category expansion  
- dimensional signature elaboration  

### **Forbidden Extensions**  
- personal data  
- behavioral inference  
- sensitive category inference  

### **Example**  
Extending `semantic:software` → `semantic:software.devtools`

---

## **4. Condense Operator**

### **Purpose**  
Reduces metadata complexity while preserving meaning and coherence.

### **Allowed Condensation**  
- collapsing multi‑term semantic clusters  
- simplifying dimensional signatures  
- reducing variant tags  

### **Forbidden Condensation**  
- removing governance fields  
- removing drift fields  
- removing operator grammar fields  

### **Example**  
Condensing `semantic:software.devtools.build` → `semantic:software.devtools`

---

## **5. Refactor Operator**

### **Purpose**  
Reorganizes metadata for clarity, stability, or coherence.

### **Allowed Refactoring**  
- reorganizing dimensional fields  
- restructuring semantic hierarchy  
- normalizing resonance values  

### **Forbidden Refactoring**  
- altering declared intent  
- manipulating resonance to inflate alignment  
- removing lineage identifiers  

### **Example**  
Refactoring metadata to group semantic + contextual fields together.

---

## **6. Capture Operator**

### **Purpose**  
Records contextual signals, resonance behavior, or lineage events.

### **Capture Targets**  
- resonance fluctuations  
- drift events  
- operator usage  
- contextual alignment changes  

### **Capture Rules**  
Captured data must be:

- non‑personal  
- non‑behavioral  
- non‑sensitive  
- canonical  

### **Example**  
Capturing a resonance drop from `0.91 → 0.84`.

---

## **7. Annotate Operator**

### **Purpose**  
Adds governance‑safe annotations to metadata.

### **Allowed Annotations**  
- coherence notes  
- drift warnings  
- semantic clarifications  
- operator usage markers  

### **Forbidden Annotations**  
- personal identifiers  
- behavioral predictions  
- sensitive category labels  

### **Example**  
Annotating: `coherence:stable` or `drift:corrected`.

---

## **8. Correct Operator**

### **Purpose**  
Fixes metadata drift, semantic misalignment, or operator misuse.

### **Correction Types**  
- semantic correction  
- resonance recalibration  
- dimensional normalization  
- governance field restoration  

### **Forbidden Corrections**  
- altering declared intent  
- inflating resonance  
- removing lineage  

### **Example**  
Correcting a malformed field:  
`resonance:1.4` → `resonance:0.94`

---

## **9. Operator Safety Rules**

All operators must obey:

- **privacy‑first constraints**  
- **drift boundaries**  
- **coherence declarations**  
- **canonical metadata rules**  
- **suite governance policies**  

Operators may never introduce:

- personal data  
- behavioral inference  
- sensitive categories  
- adversarial resonance injection  

---

## **10. Cross‑Module Operator Alignment**

OpenAdEngine operators align with:

- **OpenSEO** — semantic operators  
- **OpenSoN** — social context operators  
- **OpenStream** — recommendation operators  
- **OpenCatalog** — product metadata operators  
- **OpenRisk** — anomaly detection operators  
- **OpenIAM** — identity‑safe operators  

All alignment is drift‑bounded and coherence‑declared.

---

## **11. Operator Metadata Fields**

Ads must declare operator availability:

```html
<meta name="open.ad.operator.extend" content="true">
<meta name="open.ad.operator.condense" content="true">
<meta name="open.ad.operator.refactor" content="true">
<meta name="open.ad.operator.capture" content="true">
<meta name="open.ad.operator.annotate" content="true">
<meta name="open.ad.operator.correct" content="true">
```

These fields ensure operator grammar compliance.
