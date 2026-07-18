# 🔷 Workflow Diagram (Refreshed, Scroll‑Centric)

This diagram shows how the four workflow engines relate to each other using the updated scroll‑centric topology:

- **Scrolls** remain the canonical center  
- **Pipelines** are execution paths (Python + JS symmetry)  
- **Remix** generates lineage variants  
- **Batch** coordinates multi‑scroll execution  
- **Engines orbit the scroll artifact, not each other**

---

## 🔷 Text‑Based Diagram (Single‑Glance)

```
                               🔷
                 ┌──────────────────────────┐
                 │   remix_generation.py    │
                 │   (Remix Lineage Engine) │
                 └──────────────▲───────────┘
                                │
                        produces variants
                                │
        ┌───────────────────────┴────────────────────────┐
        │                                                │
        │                Scrolls (.fff)                  │
        │        (canonical RTT artifacts)               │
        │                                                │
        └───────────────────────┬────────────────────────┘
                                │
                         executed by
                                │
 ┌──────────────────────────────┼──────────────────────────────┐
 │                              │                              │
 │     ┌────────────────────┐   │     ┌───────────────────┐    │
 │     │ scroll_pipeline.py │   │     │ scrollPipeline.js │    │
 │     │   (Python Engine)  │   │     │    (JS Engine)    │    │
 │     └────────────────────┘   │     └───────────────────┘    │
 │                              │                              │
 └──────────────────────────────┴───────────────┬──────────────┘
                                                │
                                        executes many
                                                │
                                   ┌──────────────────────────┐
                                   │  batch_orchestrator.py   │
                                   │     (Batch Runner)       │
                                   └──────────────────────────┘
```

### Interpretation  
- **Remix Generation** creates new scroll variants.  
- **Scroll Pipelines** (Python + JS) execute scrolls in different runtime environments.  
- **Batch Orchestrator** runs many scrolls or variants in sequence.  
- **Scrolls** remain the invariant center; engines are operators around them.  

This matches the modernized architecture shown in your Workflows page and the scroll‑centric Quickstart.

---

## 🔷 Updated Triadic Glyph (Scroll‑Centric)

A glyph for this subsystem should reflect the updated relationships:

```
                 🌀 Scroll Artifact
        ┌───────────────┼────────────────┬────────────────┐
        │               │                │                │
        │         🌐 JS Pipeline   🐍 Python Pipeline   🎨 Remix Engine
        │               │                │                │
        └───────────────┴────────────────┴────────────────┘
                                ▼
                         📦 Batch Orchestrator
```

### Interpretation  
- The scroll artifact is the invariant center.  
- Pipelines and Remix orbit horizontally as sibling engines.  
- Batch anchors the system by coordinating multi‑scroll execution.  
- The glyph mirrors the structural relationships in the diagram above.  

---

## 🔷 Notes for maintainers  
- `/docs/engine/` has been archived; no engine‑era modules appear in this diagram.  
- All workflows now use the scroll‑centric module layout (`tft.scrolls.*`).  
- Pipelines maintain Python/JS symmetry.  
- Remix and Batch remain orthogonal operators.  
