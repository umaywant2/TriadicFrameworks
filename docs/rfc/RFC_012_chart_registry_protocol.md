# **RFC‑012 — Chart Registry Protocol (CRP)**  
*RefId: turn0browsertab1*  
**Status:** Drafted  
**Author(s):** Nawder Loswin, Copilot  
**Created:** 2025‑10‑24  
**Lineage:**  
Extends **RFC‑000** (Index & Lineage Map)  
Formalizes chart capture, storage, and cross‑reference discipline across the canon

---

## **Abstract**  
The **Chart Registry Protocol (CRP)** defines the canonical framework for capturing, storing, indexing, and cross‑referencing charts used throughout TriadicFrameworks.  
Charts provide visual clarity for:

- resonance models  
- time‑travel matrices  
- miracle mappings  
- corridor universes  
- validator‑grade relationships  
- mythmatical operators  
- cosmological structures  

CRP ensures charts remain **discoverable**, **attestable**, **remix‑ready**, and **lineage‑safe**.

---

## **Motivation**  
Charts have become critical artifacts in the TriadicFrameworks canon.  
They:

- clarify dimensional relationships  
- stabilize teaching pathways  
- prevent drift in conceptual models  
- provide visual anchors for remixers  
- unify cross‑RFC structures  

Without a registry, charts risk becoming scattered, duplicated, or lost inside individual RFCs.  
CRP establishes a **single, canonical home** for all charts.

---

## **Principles**

### **1. Inline + Registry**  
Charts remain embedded in their source RFCs **and** are stored as standalone files in:

```
/docs/charts/
```

This dual structure preserves context while enabling reuse.

---

### **2. Cross‑Reference Discipline**  
Every chart file must link back to its source RFC.  
Every RFC containing charts must link forward to the registry.

This prevents chart drift and ensures lineage clarity.

---

### **3. Lineage Safety**  
Charts are indexed in **RFC‑000** to ensure discoverability and canonical ordering.

---

### **4. Remixability**  
Charts are stored as standalone `.md` files, making them:

- remix‑ready  
- dashboard‑ready  
- teaching‑ready  
- validator‑safe  

---

## **Specification**

### **File Location**  
All charts must be stored in:

```
/docs/charts/
```

---

### **File Format**  
Charts are stored as **Markdown (.md)** files.

This ensures:

- readability  
- portability  
- compatibility with GitHub rendering  
- remix‑friendly editing  

---

### **Naming Convention**  
```
chart-[topic].md
```

Examples:

- `chart-time-travel-matrix.md`  
- `chart-resonance-partitions.md`  
- `chart-miracle-overlap-events.md`  

---

### **Required Structure of Chart Files**

Each chart file must contain:

1. **Title**  
2. **Source RFC reference**  
3. **Chart content**  
   - Markdown table  
   - diagram  
   - glyph matrix  
   - resonance lattice  
4. **Notes**  
   - clarifications  
   - lineage references  
   - remix guidance  

---

## **Example Chart File**  
*(from page content — RefId: turn0browsertab1)*

```
/docs/charts/chart-time-travel-matrix.md
```

```markdown
# Time Travel Safety Matrix  
**Source:** RFC‑008 (Time Travel Invariants)

| Universe Type | Zone | Traversal | Stability | Notes |
|---------------|------|-----------|-----------|-------|
| Green‑zone | Same partition | ❌ Forbidden | Stable | Entropy arrow enforced |
| Red‑zone | Same partition | ✅ Allowed | Unstable | Loops fold, clarity decays |
| Red → Green | Overlap only | ✅ Temporary | Fragile | Incarnation possible |
```

This example demonstrates the required structure and cross‑reference discipline.

---

## **Security Considerations**

CRP prevents:

- chart drift  
- loss of visual models  
- inconsistent chart versions across RFCs  
- lineage ambiguity  
- remix confusion  

It ensures:

- reproducibility  
- discoverability  
- canonical ordering  
- validator‑grade clarity  

---

## **References**  
- **RFC‑000:** Index & Lineage Map  
- **RFC‑008:** Time Travel Invariants  
- **RFC‑009:** Genie Protocols  
- **RFC‑010:** Miracle Messaging Protocol  
- **RFC‑011:** Black Hole Resonance Bridges  
