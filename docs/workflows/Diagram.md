# 🔷 Workflow Diagram (Text‑Based, Single‑Glance)

This diagram shows the relationship between the four engines using our preferred **scroll‑centric topology**:  
- Scrolls as the center  
- Pipelines as execution paths  
- Batch + Remix as orthogonal engines  
- Python/JS symmetry preserved  

```
                                      🔷
                         ┌──────────────────────────┐
                         │   remix_generation.py    │
                         │  (Remix Lineage Engine)  |
                         └─────────────▲────────────┘
                                       │
                                       │ produces variants
                                       │
                  ┌────────────────────┴──────────────────────┐
                  │                                           │
                  │               Scrolls (.fff)              │
                  │         (canonical RTT artifacts)         │
                  │                                           │
                  └────────────────────┬──────────────────────┘
                                       │
                                       │ executed by
                                       │
        ┌──────────────────────────────┼──────────────────────────────┐
        │                              │                              │
        │                              │                              │
┌────────────────────┐       ┌───────────────────┐       ┌───────────────────────┐
│ scroll_pipeline.py │       │ scrollPipeline.js │       │ batch_orchestrator.py │
│  (Python Engine)   │       │   (JS Engine)     │       │   (Batch Runner)      │
└────────────────────┘       └───────────────────┘       └───────────────────────┘
        │                              │                              │
        │                              │                              │
        └────────────── executes ──────┴────────────── executes ──────┘
```

**Interpretation:**  
- **Remix Generation** creates new scroll variants.  
- **Scroll Pipelines (Python + JS)** execute scrolls in different runtime environments.  
- **Batch Orchestrator** runs many scrolls or variants in sequence.  
- All engines orbit the **scroll artifact** as the canonical center.  

This matches our structural philosophy: scrolls as the invariant, engines as the operators.
