# **IPD‑12 Capture Auto‑Formatter**  
### *Canonical Ordering Rules for All Capture Objects*

The formatter enforces **one universal rule**:

> **Every capture object must appear in canonical IPD‑12 order before any drift‑layer operator is allowed to run.**

This prevents malformed captures from breaking drift‑tensor chains or paradox detection.

---

## **1. Canonical Field Order**

Every capture object MUST follow this exact order:

```
1. name
2. purpose
3. boundaries
4. structural_layers
5. operational_flow
6. coherence_baseline
7. domain
8. regime_level
```

This ordering mirrors the composite grammar in your active tab (  [github.com](https://github.com/umaywant2/TriadicFrameworks/edit/main/docs/prompts/p_Capture.md)).

---

## **2. Canonical Formatting Rules**

### **Rule A — All fields must be present**
No optional fields.  
No empty fields.  
No nulls.

### **Rule B — Arrays must be non‑empty**
- `boundaries`
- `structural_layers`
- `operational_flow`

### **Rule C — Values must be atomic**
No nested objects inside capture fields.  
No multi‑layer structures inside a single field.

### **Rule D — Domain must be singular**
One domain per process.  
Multi‑domain drift is handled at the bundle level.

### **Rule E — Regime level must be ≤ deep**
IPD‑12 cannot accept composite, substrate, dimensional, or infinite regimes.

---

## **3. Canonical Sorting Rules**

The formatter applies sorting rules to ensure consistency:

### **A. boundaries**
Sort alphabetically.

### **B. structural_layers**
Sort by structural depth:
```
form → function → behavior → interpretation
```

### **C. operational_flow**
Sort by execution order:
```
start → middle → end
```

### **D. domain**
No sorting — domain is atomic.

### **E. regime_level**
No sorting — must be one of:
```
surface | mid | deep
```

---

## **4. Canonical Normalization Rules**

### **Normalize naming**
- lowercase with underscores  
- no spaces  
- no hyphens  
- no camelCase  

Example:
```
"Human Notes" → "human_notes"
```

### **Normalize purpose**
Purpose must be a **single sentence**, no conjunctions.

### **Normalize boundaries**
Convert constraints into nouns:
```
"limited time" → "time"
"must be accurate" → "accuracy"
```

### **Normalize structural layers**
Convert layers into canonical nouns:
```
"listening" → "input"
"thinking" → "interpretation"
"writing" → "output"
```

### **Normalize operational flow**
Convert steps into canonical verbs:
```
"listen" → "input"
"interpret" → "process"
"write" → "output"
```

---

## **5. Canonical Output Template**

After formatting, every capture object must look like:

```json
{
  "name": "canonical_name",
  "purpose": "single-sentence purpose",
  "boundaries": ["sorted", "constraints"],
  "structural_layers": ["form", "function", "behavior"],
  "operational_flow": ["input", "process", "output"],
  "coherence_baseline": "declared baseline",
  "domain": "workflow",
  "regime_level": "surface"
}
```

---

## **6. Auto‑Formatter Pseudocode**

```text
function autoformat(capture):
    enforce_field_order()
    enforce_required_fields()
    normalize_name()
    normalize_purpose()
    normalize_boundaries()
    normalize_structural_layers()
    normalize_operational_flow()
    validate_domain()
    validate_regime_level()
    sort_arrays()
    return formatted_capture
```

---

## **7. Why this matters**

The formatter guarantees:

- **drift()** always has boundaries  
- **drift_tensor()** always has layers  
- **align_coherence()** always has a baseline  
- **cross_system()** always has domain alignment  
- **paradox()** always has dependency + drift + coherence  

It ensures every capture object is **operator‑ready**.
