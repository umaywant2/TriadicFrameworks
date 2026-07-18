# **6. Optional: Stream JSON traces live**

If we want real‑time UI updates:

```python
def stream_trace_update(state, websocket):
    update = {
        "step": len(state.steps) - 1,
        "q": state.q_history[-1],
        "status": state.corridor_status
    }
    websocket.send(json.dumps(update))
```

This gives us a **live corridor monitor**.

---

Here we go, Nawder — this is the moment where our agent‑corridor runtime gets its **own file format**, just like hardware engineers have **VCD**, **FSDB**, or **ETW**.  
Except this one is for *reasoning corridors*, not voltage transitions.

Below is a clean, extensible, future‑proof **Corridor Trace File (CTF)** specification — something we can log, replay, diff, visualize, and even stream.

We’ll give:

- the **file format**  
- the **schema**  
- the **event model**  
- the **encoding rules**  
- and a **minimal writer**  

This is the first real “waveform dump” for agent cognition.

---

# **Corridor Trace File (CTF) — Specification v0.1**

A **CTF** file is a structured, append‑only log of a corridor execution.  
It is designed to be:

- **streamable** (line‑delimited JSON events)  
- **indexable** (step‑indexed)  
- **lineage‑aware**  
- **Q‑metric rich**  
- **tool‑agnostic**  
- **visualization‑friendly**  

Think of it as:  
**VCD + Chrome DevTools trace + LangGraph state + Q‑metric physics**.

---

# **1. File Structure**

A `.ctf` file is a sequence of **newline‑delimited JSON objects**, each representing an event.

```
{ "type": "header", ... }
{ "type": "step", ... }
{ "type": "q", ... }
{ "type": "rewind", ... }
{ "type": "status", ... }
{ "type": "footer", ... }
```

This makes it:

- easy to stream  
- easy to parse incrementally  
- easy to visualize live  

---

# **2. Event Types**

### **2.1. header**
Metadata about the corridor run.

```json
{
  "type": "header",
  "task_id": "task-9af3",
  "timestamp": 1736280000.123,
  "corridor_spec": {
    "max_steps": 64,
    "max_semantic_drift": 0.35,
    "max_tool_entropy": 2.0,
    "max_latency_drift": 1.0,
    "max_branching_pressure": 8,
    "max_retry_ratio": 0.25
  }
}
```

---

### **2.2. step**
Represents a single agent action + observation.

```json
{
  "type": "step",
  "step_id": 12,
  "parent_step_id": 11,
  "timestamp": 1736280002.551,
  "action": "search('quantum turbulence')",
  "observation": "Executed search",
  "tool": "search",
  "latency_ms": 412
}
```

---

### **2.3. q**
Q‑metrics computed after each step.

```json
{
  "type": "q",
  "step_id": 12,
  "semantic_drift": 0.22,
  "tool_entropy": 1.58,
  "latency_drift": 0.14,
  "branching_pressure": 3,
  "retry_ratio": 0.08
}
```

---

### **2.4. status**
Corridor‑level status update.

```json
{
  "type": "status",
  "step_id": 12,
  "corridor_status": "warning",
  "violations": ["semantic_drift"]
}
```

---

### **2.5. rewind**
Lineage‑based rollback event.

```json
{
  "type": "rewind",
  "from_step": 12,
  "to_step": 10,
  "timestamp": 1736280002.900
}
```

---

### **2.6. footer**
Marks the end of the trace.

```json
{
  "type": "footer",
  "timestamp": 1736280003.200,
  "final_status": "stable"
}
```

---

# **3. Schema Summary**

| Event Type | Purpose |
|------------|---------|
| `header` | Corridor metadata + spec |
| `step` | Action + observation + lineage |
| `q` | Q‑metrics for that step |
| `status` | Stability envelope state |
| `rewind` | Lineage rollback |
| `footer` | End of trace |

---

# **4. Encoding Rules**

### **4.1. Line‑delimited JSON (LDJSON)**  
Each event is a single JSON object on its own line.

### **4.2. Append‑only**  
Events are written in chronological order.

### **4.3. Step‑indexed**  
`step_id` is monotonically increasing unless a rewind occurs.

### **4.4. Rewind semantics**  
After a rewind event:

- future steps are considered invalid  
- the viewer should visually “snap back”  
- Q‑metrics after the rewind are recomputed  

### **4.5. Deterministic replay**  
A viewer can reconstruct the entire corridor by replaying events in order.

---

# **5. Minimal CTF Writer**

Add this to our corridor runtime:

```python
import json

class CTFWriter:
    def __init__(self, file_path):
        self.f = open(file_path, "w")

    def write(self, event: dict):
        self.f.write(json.dumps(event) + "\n")
        self.f.flush()

    def close(self):
        self.f.close()
```

---

# **6. Integrating with the corridor runtime**

### **6.1. Emit header**

```python
writer.write({
    "type": "header",
    "task_id": state.task_id,
    "timestamp": time.time(),
    "corridor_spec": self.spec.dict()
})
```

---

### **6.2. Emit step**

```python
writer.write({
    "type": "step",
    "step_id": step.step_id,
    "parent_step_id": step.parent_step_id,
    "timestamp": step.timestamp,
    "action": step.action,
    "observation": step.observation,
    "tool": extract_tool(step.action),
    "latency_ms": step.latency_ms
})
```

---

### **6.3. Emit Q‑metrics**

```python
writer.write({
    "type": "q",
    "step_id": step.step_id,
    **step.q_metrics
})
```

---

### **6.4. Emit status**

```python
writer.write({
    "type": "status",
    "step_id": step.step_id,
    "corridor_status": state.corridor_status,
    "violations": violations
})
```

---

### **6.5. Emit rewind**

```python
writer.write({
    "type": "rewind",
    "from_step": old_step,
    "to_step": new_step,
    "timestamp": time.time()
})
```

---

### **6.6. Emit footer**

```python
writer.write({
    "type": "footer",
    "timestamp": time.time(),
    "final_status": state.corridor_status
})
```

---

# **7. What this unlocks**

With `.ctf` files, we can now build:

### **A Corridor Waveform Viewer**
- Q‑metric waveforms  
- branching graph  
- semantic drift heatmap  
- rewind markers  
- tool‑use entropy timeline  

### **A Live Corridor Monitor**
- stream events over WebSockets  
- visualize stability envelopes in real time  

### **A Debugger**
- step through lineage  
- inspect Q‑metrics  
- replay corridor evolution  

### **A Diff Tool**
- compare two corridor runs  
- highlight divergence points  
- compute drift deltas  

This is the agent equivalent of **VCD**, **Chrome trace**, and **OpenTelemetry** rolled into one.

---

We’re literally building the VCD viewer for cognition—love this.

We’ll give **just enough** to be real and droppable into `triadicframeworks.org` later:

- A **React/Next.js Corridor Viewer** page that loads a `.ctf` JSON (or API) and renders:
  - step timeline
  - status badges
  - Q‑metric panel shell
- A **D3.js Q‑metric waveform panel** component that we can plug into that viewer

I’ll assume **Next.js 13+ / App Router**, TypeScript, and a simple `/api/corridor/:id` that returns parsed CTF as JSON.
