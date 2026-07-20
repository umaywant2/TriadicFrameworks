# **1. JSON Trace Format (Web‑UI Friendly)**

A single corridor run produces a JSON object like:

```json
{
  "task_id": "task-9af3",
  "status": "stable",
  "steps": [
    {
      "step_id": 0,
      "parent_step_id": null,
      "action": "search('quantum turbulence')",
      "observation": "Executed search",
      "q_metrics": {
        "semantic_drift": 0.12,
        "tool_entropy": 0.0,
        "latency_drift": 0.0,
        "branching_pressure": 0,
        "retry_ratio": 0.0
      },
      "timestamp": 1736280000.123
    },
    {
      "step_id": 1,
      "parent_step_id": 0,
      "action": "summarize(results)",
      "observation": "Executed summarize",
      "q_metrics": {
        "semantic_drift": 0.18,
        "tool_entropy": 0.69,
        "latency_drift": 0.12,
        "branching_pressure": 1,
        "retry_ratio": 0.0
      },
      "timestamp": 1736280001.004
    }
  ],
  "q_history": [
    {
      "step": 0,
      "semantic_drift": 0.12,
      "tool_entropy": 0.0,
      "latency_drift": 0.0,
      "branching_pressure": 0,
      "retry_ratio": 0.0
    },
    {
      "step": 1,
      "semantic_drift": 0.18,
      "tool_entropy": 0.69,
      "latency_drift": 0.12,
      "branching_pressure": 1,
      "retry_ratio": 0.0
    }
  ]
}
```

This is intentionally:

- **Flat** (easy for JS to consume)  
- **Time‑indexed**  
- **Lineage‑aware**  
- **Q‑metric rich**  
- **Web‑UI ready**  

A front‑end can now render:

- step timeline  
- Q‑metric waveforms  
- branching graph  
- semantic drift heatmap  
- rewind points  
