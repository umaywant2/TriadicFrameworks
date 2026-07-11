## 1. Capture as the first engine layer

In IPD‑12, **capture** is not “just description”—it is a formal structural act:

- **Define identity** of each process  
- **Expose boundaries** and constraints  
- **Lay out layers** (what the process is made of)  
- **Trace operational flow** (how it runs)  
- **Declare coherence baseline** (what “makes sense” for this process)

Only once capture is complete can drift, coherence, and paradox be evaluated.

---

## 2. Capture fields (canonical set)

Every IPD‑12 process must be captured with the following fields:

- **Name:** canonical identifier of the process  
- **Purpose:** what the process is for  
- **Boundaries:** limits, constraints, scope  
- **Structural layers:** main components or strata  
- **Operational flow:** sequence or topology of operations  
- **Coherence baseline:** what counts as “working” or “aligned” for this process  
- **Domain:** the domain(s) the process belongs to (music, physics, workflow, etc.)  
- **Regime level (RTT):** surface/mid/deep (IPD‑12 stays ≤ deep)  

This is the **capture schema** that `map_process()` is expected to fill.

---

## 3. Capture operators and their roles

### **map_process()**

- **Role:** primary capture operator  
- **Input:** raw description of a process  
- **Output:** structured capture object with all fields above  
- **Guarantee:** process is now “visible” to IPD‑12

### **compare_process()**

- **Role:** capture‑adjacent operator  
- **Input:** two or more captured processes  
- **Output:** shared structure, shared constraints, shared anchors  
- **Guarantee:** coherence anchors can be declared across processes

Capture grammar is therefore:

```text
map_process()  →  compare_process()
```

before any drift is allowed.

---

## 4. Capture layers and drift‑tensor alignment

Capture grammar is explicitly aligned with the drift‑tensor:

- **Geometric layer:** captured via structural layers and form  
- **Operational layer:** captured via operational flow  
- **Temporal layer:** captured via time, pacing, evolution notes  
- **Conceptual layer:** captured via purpose and coherence baseline  
- **Domain layer:** captured via domain field and regime level  

If capture is incomplete in any of these, the corresponding drift‑tensor layer is **locked**.

---

## 5. Capture modes (RTT‑1 vs research)

### **RTT‑1 teaching mode**

- Simple language  
- Minimal fields (purpose, boundaries, layers, flow, coherence)  
- Used in classroom examples and student exercises  

### **Research mode (RTT‑2/3/12)**

- Full schema  
- Domain‑rich capture  
- Regime‑aware notes  
- Used in multi‑domain drift analyzers and bridge documents  

IPD‑12’s capture grammar supports both, but `p_Capture.md` is RTT‑1‑biased.

---

## 6. Capture → Drift contract

The expansion clarifies a strict contract:

- **No drift without capture.**  
- **No tensor without layered capture.**  
- **No paradox without coherence baseline.**

Formally:

```text
map_process()  is a hard prerequisite for:
    drift(), drift_tensor(), detect_divergence(), align_coherence(), cross_system()
```

Capture is the **root operator** of IPD‑12.

---

If you want, next step could be a **capture schema snippet** (JSON/YAML) you can embed directly into `p_Capture.md` for AI tooling and validation.

---

Here is your **IPD‑12 Capture Schema Snippet**, formatted in both **JSON** and **YAML**, and fully aligned with the capture grammar visible in your active tab   [github.com](https://github.com/umaywant2/TriadicFrameworks/edit/main/docs/prompts/p_Capture.md).

This schema is designed to drop directly into:

```
docs/prompts/p_Capture.md
```

or into:

```
frameworks/ipd_12/capture.schema.json
```

It matches the composite grammar you’re editing (Capture → Drift → Tensor → Divergence → Coherence → Cross‑System → Paradox).

---

# **IPD‑12 Capture Schema (JSON)**

```json
{
  "process": {
    "name": "string",
    "purpose": "string",
    "boundaries": ["string"],
    "structural_layers": ["string"],
    "operational_flow": ["string"],
    "coherence_baseline": "string",
    "domain": "string",
    "regime_level": "surface | mid | deep"
  },
  "capture_metadata": {
    "version": "1.0",
    "engine": "RTT-IPD-12",
    "required_fields": [
      "name",
      "purpose",
      "boundaries",
      "structural_layers",
      "operational_flow",
      "coherence_baseline"
    ]
  }
}
```

---

# **IPD‑12 Capture Schema (YAML)**

```yaml
process:
  name: string
  purpose: string
  boundaries:
    - string
  structural_layers:
    - string
  operational_flow:
    - string
  coherence_baseline: string
  domain: string
  regime_level: surface | mid | deep

capture_metadata:
  version: "1.0"
  engine: RTT-IPD-12
  required_fields:
    - name
    - purpose
    - boundaries
    - structural_layers
    - operational_flow
    - coherence_baseline
```

---

# **Schema Notes (aligned with your active tab)**

These fields map directly to the composite grammar you’re editing in `p_Capture.md`:

- **structural_layers** → required for `drift_tensor()` unlock  
- **operational_flow** → required for operational drift layer  
- **coherence_baseline** → required for `align_coherence()`  
- **domain** → required for domain drift layer  
- **regime_level** → ensures IPD‑12 stays ≤ deep regime  

This schema ensures **map_process()** always produces a complete capture object, enabling all downstream operators:

```
map_process()
compare_process()
drift()
detect_divergence()
drift_tensor()
align_coherence()
cross_system()
```

  [github.com](https://github.com/umaywant2/TriadicFrameworks/edit/main/docs/prompts/p_Capture.md)
