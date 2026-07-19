# **1. Real Q‑Metric Set**

These are structural, not aesthetic — they measure *stability of reasoning over time*.

### **Q1 — Semantic Drift**
How far the agent’s internal representation drifts from the original task.

```python
from sentence_transformers import SentenceTransformer, util
embedder = SentenceTransformer("all-MiniLM-L6-v2")

def q_semantic_drift(task_embedding, last_obs):
    obs_emb = embedder.encode(last_obs, convert_to_tensor=True)
    sim = util.cos_sim(task_embedding, obs_emb).item()
    return 1.0 - sim  # drift = 1 - similarity
```

---

### **Q2 — Tool‑Use Entropy**
Measures whether the agent is thrashing between tools.

```python
import math
from collections import Counter

def q_tool_entropy(tool_history):
    counts = Counter(tool_history)
    total = sum(counts.values())
    entropy = -sum((c/total) * math.log2(c/total) for c in counts.values())
    return entropy
```

---

### **Q3 — Latency Drift**
If each step takes longer than the previous, the corridor is destabilizing.

```python
def q_latency_drift(latencies):
    if len(latencies) < 2:
        return 0.0
    return latencies[-1] - latencies[-2]
```

---

### **Q4 — Branching Pressure**
How many “parallel hypotheses” the agent is implicitly maintaining.

```python
def q_branching_pressure(steps):
    parents = [s.parent_step_id for s in steps if s.parent_step_id is not None]
    return len(set(parents))
```

---

### **Q5 — Retry Ratio**
A classic instability signature.

```python
def q_retry_ratio(steps):
    retries = sum(1 for s in steps if "retry" in s.action.lower())
    return retries / max(1, len(steps))
```

---

# **2. CorridorSpec (Safety Envelope)**

This is our VCG‑style envelope — declarative, inspectable, enforceable.

```python
from pydantic import BaseModel

class CorridorSpec(BaseModel):
    max_steps: int = 64
    max_semantic_drift: float = 0.35
    max_tool_entropy: float = 2.0
    max_latency_drift: float = 1.0
    max_branching_pressure: int = 8
    max_retry_ratio: float = 0.25

    # actions the runtime may take
    on_warning: str = "continue"   # continue | reroute | human
    on_violation: str = "halt"     # halt | rewind | human
```

This is the **policy contract** between the graph and the corridor physics.

---

# **3. ResonanceCorridor Helper (Reusable LangGraph Module)**

This is the part that makes LangGraph “RTT‑Inside aware”.

```python
class ResonanceCorridor:
    def __init__(self, llm, spec: CorridorSpec):
        self.llm = llm
        self.spec = spec
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")

    def init(self, state, task_description):
        state.task_id = f"task-{hash(task_description) & 0xFFFF:x}"
        state.task_embedding = self.embedder.encode(task_description, convert_to_tensor=True)
        state.corridor_status = "stable"
        return state

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
                q_metrics={}
            )
        )
        return state

    def compute_q(self, state):
        steps = state.steps
        last_obs = steps[-1].observation

        q = {
            "semantic_drift": q_semantic_drift(state.task_embedding, last_obs),
            "tool_entropy": q_tool_entropy([s.action for s in steps]),
            "latency_drift": q_latency_drift(state.latencies),
            "branching_pressure": q_branching_pressure(steps),
            "retry_ratio": q_retry_ratio(steps),
            "step_count": len(steps),
        }

        state.q_history.append(q)
        steps[-1].q_metrics = q
        return state

    def enforce(self, state):
        q = state.q_history[-1]
        s = self.spec

        violations = []

        if q["step_count"] > s.max_steps:
            violations.append("max_steps")
        if q["semantic_drift"] > s.max_semantic_drift:
            violations.append("semantic_drift")
        if q["tool_entropy"] > s.max_tool_entropy:
            violations.append("tool_entropy")
        if q["latency_drift"] > s.max_latency_drift:
            violations.append("latency_drift")
        if q["branching_pressure"] > s.max_branching_pressure:
            violations.append("branching_pressure")
        if q["retry_ratio"] > s.max_retry_ratio:
            violations.append("retry_ratio")

        if not violations:
            state.corridor_status = "stable"
            return state

        # classify severity
        if any(v in ["semantic_drift", "latency_drift"] for v in violations):
            state.corridor_status = "warning"
            if self.spec.on_warning == "reroute":
                state.route = "human_review"
        else:
            state.corridor_status = "halted"
            if self.spec.on_violation == "halt":
                state.route = "halt"
            elif self.spec.on_violation == "rewind":
                state.route = "rewind"

        return state
```

---

# **4. Wiring it into LangGraph**

```python
corridor = ResonanceCorridor(llm=your_llm, spec=CorridorSpec())

graph = StateGraph(CorridorState)

graph.add_node("init", lambda s: corridor.init(s, task_description))
graph.add_node("step", corridor.agent_step)
graph.add_node("q", corridor.compute_q)
graph.add_node("vcg", corridor.enforce)

graph.set_entry_point("init")
graph.add_edge("init", "step")
graph.add_edge("step", "q")
graph.add_edge("q", "vcg")

def route(state):
    if state.corridor_status == "halted":
        return END
    if state.corridor_status == "warning":
        return "step"  # or "human_review"
    return "step"

graph.add_conditional_edges("vcg", route, {"step": "step", END: END})

app = graph.compile()
```

---

# **What we now have**

We’ve just built:

- **A physics layer for agent graphs**  
- **A safety envelope (CorridorSpec)**  
- **A reusable module (ResonanceCorridor)**  
- **Real Q‑metrics that measure structural stability**  
- **Lineage, drift, entropy, branching pressure**  
- **A VCG‑style enforcement loop**  
- **A LangGraph integration that halts, reroutes, or continues based on stability**

This is the first real RTT‑Inside runtime for agent frameworks.
