## 1. Rewind mechanics (lineage‑based rollback)

We treat `steps` as a lineage chain and allow rollback to any prior `step_id`.

### 1.1. Add rewind API to `CorridorState`

```python
from typing import List, Dict, Any, Optional
from pydantic import BaseModel

class CorridorStep(BaseModel):
    step_id: int
    parent_step_id: Optional[int]
    action: str
    observation: str
    q_metrics: Dict[str, float]

class CorridorState(BaseModel):
    task_id: str
    steps: List[CorridorStep] = []
    q_history: List[Dict[str, float]] = []
    latencies: List[float] = []
    corridor_status: str = "stable"
    route: Optional[str] = None

    def rewind_to(self, target_step_id: int):
        """Drop all steps and Q-history after target_step_id."""
        self.steps = [s for s in self.steps if s.step_id <= target_step_id]
        self.q_history = self.q_history[: len(self.steps)]
        self.latencies = self.latencies[: len(self.steps)]
        self.corridor_status = "stable"
        self.route = None
        return self
```

### 1.2. Let the VCG enforcement choose rewind

Extend `ResonanceCorridor.enforce`:

```python
    def enforce(self, state: CorridorState) -> CorridorState:
        q = state.q_history[-1]
        s = self.spec
        violations = []

        # ... same checks as before ...

        if not violations:
            state.corridor_status = "stable"
            return state

        # classify severity
        if any(v in ["semantic_drift", "latency_drift"] for v in violations):
            state.corridor_status = "warning"
            if s.on_warning == "reroute":
                state.route = "human_review"
        else:
            state.corridor_status = "halted"
            if s.on_violation == "halt":
                state.route = "halt"
            elif s.on_violation == "rewind":
                # simple policy: rewind to last stable step
                last_stable_idx = max(0, len(state.steps) - 2)
                state.rewind_to(last_stable_idx)
                state.route = "rewind"

        return state
```

### 1.3. Wire rewind into LangGraph routing

```python
def route(state: CorridorState):
    if state.route == "halt":
        return END
    if state.route == "rewind":
        # after rewind, just continue stepping
        return "step"
    if state.route == "human_review":
        return "human_review"
    return "step"
```

Now the corridor can **snap back** to a prior stable point instead of just dying.

---

## 2. Corridor‑level visualization

Let’s give a quick “oscilloscope” for Q‑metrics over steps.

### 2.1. Text‑based sparkline view (no plotting libs required)

```python
def sparkline(values, width=40, chars="▁▂▃▄▅▆▇█"):
    if not values:
        return ""
    vmin, vmax = min(values), max(values)
    if vmax == vmin:
        return chars[0] * min(len(values), width)
    scaled = [
        int((v - vmin) / (vmax - vmin) * (len(chars) - 1))
        for v in values
    ]
    return "".join(chars[i] for i in scaled[:width])

def visualize_corridor(state: CorridorState):
    steps = list(range(len(state.q_history)))
    if not steps:
        print("No Q-history yet.")
        return

    def series(key):
        return [q[key] for q in state.q_history]

    print(f"Task: {state.task_id}")
    print(f"Steps: {len(steps)}  Status: {state.corridor_status}")
    print()

    for key in ["semantic_drift", "tool_entropy", "latency_drift",
                "branching_pressure", "retry_ratio"]:
        vals = series(key)
        print(f"{key:18}: {sparkline(vals)}  [{min(vals):.3f} .. {max(vals):.3f}]")
```

Call `visualize_corridor(final_state)` and we get a **console waveform** of Q‑metrics over time.

---

## 3. Corridor Debug Console

A tiny REPL‑style console to inspect lineage, Q‑metrics, and rewind interactively.

### 3.1. Simple CLI debug console

```python
def corridor_debug_console(state: CorridorState):
    print(f"\n=== Corridor Debug Console ===")
    print(f"Task: {state.task_id}")
    print(f"Steps: {len(state.steps)}  Status: {state.corridor_status}")
    print("Commands: q, steps, step <id>, qplot, rewind <id>, exit\n")

    while True:
        cmd = input("corridor> ").strip()
        if cmd in ("exit", "quit", "q"):
            break
        elif cmd == "steps":
            for s in state.steps:
                print(f"[{s.step_id}] parent={s.parent_step_id} action={s.action}")
        elif cmd.startswith("step "):
            try:
                sid = int(cmd.split()[1])
            except ValueError:
                print("Invalid step id")
                continue
            matches = [s for s in state.steps if s.step_id == sid]
            if not matches:
                print("No such step")
                continue
            s = matches[0]
            print(f"\nStep {s.step_id}")
            print(f"Parent: {s.parent_step_id}")
            print(f"Action: {s.action}")
            print(f"Observation: {s.observation}")
            print(f"Q-metrics: {s.q_metrics}\n")
        elif cmd == "qplot":
            visualize_corridor(state)
        elif cmd.startswith("rewind "):
            try:
                sid = int(cmd.split()[1])
            except ValueError:
                print("Invalid step id")
                continue
            state.rewind_to(sid)
            print(f"Rewound to step {sid}. Steps now: {len(state.steps)}")
        else:
            print("Unknown command")
```

We can drop this into a notebook or a dev shell:

```python
final_state = app.invoke(initial_state, config={...})
corridor_debug_console(final_state)
```

We now have:

- **Rewind mechanics** wired into the runtime and the console  
- **Corridor‑level visualization** (Q‑metric “waveforms”)  
- **A debug console** that feels like a scope + trace viewer for agents
