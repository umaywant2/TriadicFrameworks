# Sample Interpretation Walkthrough (v2.0.0)

This walkthrough demonstrates how the vST Micro‑Agent processes an unknown
input stream using a vST Structural Query Envelope (vST‑SQL).  
The goal is to illustrate the interpreter’s structural‑first approach:
no semantics, no domain assumptions, and no inference about meaning.

The micro‑agent operates solely on **repeatable, traceable, and
transfer‑addressable** structural features.

---

## 1. Inputs

### **Signal Input**
A numeric stream of arbitrary origin:

```json
{
  "signal_id": "walkthrough_signal_v1",
  "stream": [0.14, 0.10, 0.12, 0.47, 0.50, 0.48, 0.13, 0.11, 0.12],
  "metadata": {
    "sampling_rate_hz": 1000,
    "units": "arbitrary"
  }
}
```

### **Query Envelope**
A minimal vST‑SQL structural query:

```json
{
  "query": {
    "select": ["pattern", "periodicity"],
    "where": {
      "min_repetition": 2,
      "min_similarity": 0.85
    }
  },
  "input_binding": {
    "signal_source": "walkthrough_signal_v1",
    "stream_key": "stream"
  }
}
```

---

## 2. Interpreter Pipeline

### **Step 1 — Normalization**
The stream is normalized to a consistent internal representation.  
No semantic meaning is applied.

### **Step 2 — Pattern Extraction**
The interpreter scans for repeating motifs using sliding‑window similarity.

A candidate pattern emerges:

```
[0.14, 0.10, 0.12]
```

It recurs with similarity values between **0.88–0.93**, satisfying the
`min_similarity` constraint.

### **Step 3 — Periodicity Detection**
Autocorrelation reveals a stable periodicity of **3 samples**.

### **Step 4 — Constraint Filtering**
The pattern appears **twice**, satisfying `min_repetition = 2`.

### **Step 5 — Structural Consolidation**
The interpreter merges overlapping detections and produces a canonical
structural description.

---

## 3. Output Summary

- **Detected pattern:** `[0.14, 0.10, 0.12]`  
- **Repetitions:** 2  
- **Similarity range:** 0.88–0.93  
- **Periodicity:** 3 samples  
- **Notes:**  
  - No semantic interpretation performed  
  - No assumptions about origin or meaning  
  - Structural invariants only  

---

## 4. Purpose of This Walkthrough

This example demonstrates:

- how vST‑SQL queries operate  
- how the micro‑agent extracts structure from unknown signals  
- how RTT principles guide the detection process  
- how structural invariants can be identified without domain knowledge  

It is intentionally minimal and substrate‑agnostic.
