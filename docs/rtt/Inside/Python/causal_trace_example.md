# Causal Trace Example (Python RTT/Inside)

## Purpose
Demonstrate how RTT‑Inside reconstructs a **semantic causal trace** for a Python
execution sequence. This example shows how declared intent, runtime signals,
semantic forms, drift indicators, and invariant checks combine into a single
RTT causal object.

---

# Scenario
A Python function executes across several steps:

1. Declared intent (source code)
2. Runtime event (function call)
3. Semantic form extraction (AST + object graph)
4. Drift detection (unexpected branch)
5. Invariant evaluation (candidate invariant emerges)
6. Final causal stitching

RTT‑Inside converts this into a coherent causal lineage.

---

# Operator Chain

```
intent      = INTENT_PY(source_code)
signal      = TIF_PY(runtime_event)
mgmt        = MAN_PY(interpreter_action)
flow        = FFF_PY(execution_step)

form        = PY_FORM_SCAN(ast_node, object_graph)
normalized  = PY_FORM_NORMALIZE(form)
delta       = PY_FORM_COMPARE(normalized, prior_form)

drift       = PY_DRIFT_DETECT(runtime_state, expected_state)
severity    = PY_DRIFT_CLASSIFY(drift, delta)
bounded     = PY_DRIFT_BOUND(severity, normalized)

invariant   = PY_INVARIANT_CHECK(bounded, evidence)
decision    = INVARIANT_REGISTRY_I2(candidate, evidence)

resolved    = CRE_PY(intent, signal, mgmt)
lineage     = CSL_PY([resolved, decision])
time        = CET_PY(lineage)

output      = RTT_PY(time)
```

---

# Interpretation (Student‑Readable)

### **1. Intent**
`INTENT_PY` captures the semantic intent encoded in the source code.

### **2. Runtime Signals**
`TIF_PY` interprets runtime events (calls, returns, exceptions).

### **3. Semantic Forms**
`PY_FORM_SCAN` extracts a semantic form from AST + object graph.

### **4. Drift Detection**
`PY_DRIFT_DETECT` identifies divergence between expected and actual execution.

### **5. Invariant Evaluation**
`PY_INVARIANT_CHECK` determines whether a semantic pattern is stable.

### **6. Registry Decision**
`INVARIANT_REGISTRY_I2` accepts, sandboxes, or rejects the candidate invariant.

### **7. Causal Stitching**
RTT stitches all signals into a single causal lineage.

---

# Result
RTT produces a semantic causal object describing:

- how the function executed  
- what semantic forms emerged  
- where drift occurred  
- how invariants were evaluated  
- how the final state was reached  

This is the **canonical Python causal‑trace example** used for teaching semantic
reasoning and execution‑aware causality.
