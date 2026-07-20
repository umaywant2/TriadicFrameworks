# **2. JSON Trace Emitter (Python)**

Add this to our `ResonanceCorridor` or as a standalone utility.

```python
import json
import time

def emit_json_trace(state):
    trace = {
        "task_id": state.task_id,
        "status": state.corridor_status,
        "steps": [],
        "q_history": []
    }

    for i, step in enumerate(state.steps):
        trace["steps"].append({
            "step_id": step.step_id,
            "parent_step_id": step.parent_step_id,
            "action": step.action,
            "observation": step.observation,
            "q_metrics": step.q_metrics,
            "timestamp": getattr(step, "timestamp", None)
        })

    for i, q in enumerate(state.q_history):
        trace["q_history"].append({
            "step": i,
            **q
        })

    return json.dumps(trace, indent=2)
```

---

# **3. Add timestamps to each step**

Modify the agent step node:

```python
import time

def agent_step(self, state):
    step_id = len(state.steps)
    parent = step_id - 1 if step_id > 0 else None

    last_obs = state.steps[-1].observation if state.steps else "START"
    action = self.llm(f"Task: {state.task_id}\nLast: {last_obs}\nNext action.")
    observation = f"Executed: {action}"

    state.steps.append(
        CorridorStep(
            step_id=step_id,
            parent_step_id=parent,
            action=action,
            observation=observation,
            q_metrics={},
            timestamp=time.time()
        )
    )
    return state
```

Now every step is time‑aligned for UI playback.

---

# **4. Emit trace at the end of a LangGraph run**

```python
final_state = app.invoke(initial_state, config={...})
json_trace = emit_json_trace(final_state)

with open("corridor_trace.json", "w") as f:
    f.write(json_trace)
```

Or return it directly to a web client.

---

# **5. What a Web UI can do with this**

A front‑end can now render:

### **Corridor Timeline**
- Each step as a node  
- Parent → child arrows (lineage)  
- Color by semantic drift or entropy  

### **Q‑Metric Waveforms**
- Semantic drift over time  
- Tool entropy over time  
- Latency drift  
- Retry ratio  
- Branching pressure  

### **Stability Envelope Visualization**
- Highlight steps where Q‑metrics exceed thresholds  
- Show “rewind” points  

### **Replay Mode**
- Step through the corridor like a debugger  
- Inspect actions, observations, Q‑metrics  

### **Heatmaps**
- Semantic drift heatmap  
- Tool‑use distribution  

This is the agent equivalent of a **logic analyzer** + **oscilloscope**.
