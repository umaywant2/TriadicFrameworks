# **v2.0.0 Release Notes — vST Micro‑Agent: Spacetime Structural Query Wrapper**

## **Overview**

Version **2.0.0** expands the vST Micro‑Agent with a new structural‑detection example and updated documentation.  
This release strengthens the artifact’s role as a **substrate‑agnostic query wrapper** for unknown or heterogeneous signals, including those originating from distributed sensor networks, communication channels, or archival datasets.

The core logic of the micro‑agent remains unchanged.  
This update adds clarity, examples, and improved onboarding for researchers evaluating structural patterns in unfamiliar data streams.

---

## **What’s New in v2.0.0**

### **1. New Example: Minimal vST Structural Query Language Detection**
A new example demonstrates how the micro‑agent can detect **structural regularities** in arbitrary input streams using the vST Structural Query Language (vST‑SQL).

This example shows:

- how to wrap an unknown signal into a structural query envelope  
- how the interpreter identifies repeatable, traceable, and transfer‑addressable patterns  
- how structural detection differs from raw signal analysis  
- how to apply the micro‑agent to **any** high‑dimensional or unfamiliar data source  

This example is intentionally minimal and substrate‑agnostic.  
It does **not** make claims about any specific dataset or domain.  
It simply demonstrates the method.

---

### **2. Updated Documentation**
The following files have been added or expanded:

- **README.md** — clearer overview of the micro‑agent’s purpose and usage  
- **New example folder** for structural detection  
- **Interpreter notes** updated to reflect the new example  
- **Schema documentation** clarified for v2.0.0  

These updates improve onboarding for researchers exploring structural analysis across domains.

---

### **3. Metadata Improvements**
The Zenodo metadata (`zenodo.json`) has been updated to:

- reflect the new version  
- include keywords related to structural detection, substrate‑agnostic analysis, and signal‑agnostic query wrappers  
- clarify the scientific scope of the artifact  

---

## **Why This Matters**

The vST Micro‑Agent is designed for **unknown‑signal environments**:

- distributed sensor networks  
- communication channels with unfamiliar structure  
- archival datasets lacking semantic annotation  
- exploratory analysis of complex or noisy streams  

This release provides a **clear, minimal demonstration** of how structural queries can reveal patterns that are not visible at the raw signal level.

It does not assert the presence of structure in any specific dataset.  
It simply provides the tools and examples needed for researchers to explore structure where appropriate.

---

## **Folder Structure for v2.0.0**

Here is the recommended structure including the new example:

```
📐

README.md

examples/
  sample_interpretation_walkthrough.md
  sample_query_envelope.json
  structural_detection_minimal/
    example_signal_input.json
    example_query_envelope.json
    example_interpretation_output.md

interpreter/
  interpreter_logic.md
  interpreter_pseudocode.txt

schema/
  vST_micro_agent.schema.json

metadata/
  zenodo.json
```

This keeps the new structural‑detection example cleanly separated and easy to reference.
