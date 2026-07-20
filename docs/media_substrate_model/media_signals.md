# 📡 Media Signals

Media signals are the raw inputs that adapters convert into the Media Substrate Vector:

```
[S, D, A, N, T]
```

These signals come from diverse sources—text streams, platform metrics, distribution graphs, narrative structures, and temporal patterns. The MSM treats all of them as structural data, not content or ideology. This file defines the categories of signals the MSM can ingest and how they map to the five substrate axes.

---

## 🛰 Signal Integrity Signals (S)

Signal Integrity reflects the fidelity and reliability of information as it moves through the ecosystem. Relevant raw signals include:

- Noise levels (linguistic noise, platform noise, compression artifacts)  
- Verification density (fact‑checks, citations, cross‑references)  
- Redundancy (multiple independent confirmations)  
- Distortion patterns (algorithmic reshaping, editorial filtering)  
- Compression ratios (summaries, truncation, clipping)  
- Error rates (misquotes, mislinks, broken chains of reference)

These signals allow adapters to estimate how well meaning can be preserved across propagation.

---

## 🌐 Distribution Topology Signals (D)

Distribution Topology describes the structural shape of information flow. Relevant raw signals include:

- Graph connectivity (degree, clustering, modularity)  
- Centralization metrics (hub dominance, bottlenecks)  
- Silo boundaries (community partitions, echo chambers)  
- Cross‑talk frequency (inter‑cluster edges)  
- Flow velocity (how quickly information moves across the graph)  
- Redirection patterns (retweets, shares, reposts, link chains)

These signals allow adapters to map the topology of the media environment.

---

## ⚡ Attention Dynamics Signals (A)

Attention Dynamics represent the energy of the system. Relevant raw signals include:

- Engagement spikes (likes, shares, comments, watch time)  
- Volatility (variance in attention over time)  
- Concentration (how tightly attention pools around topics)  
- Decay curves (how quickly attention dissipates)  
- Cascade signatures (rapid amplification events)  
- Saturation (attention overload or burnout)

These signals allow adapters to quantify attention as a structural force.

---

## 🧩 Narrative Coherence Signals (N)

Narrative Coherence measures the stability and interpretability of meaning. Relevant raw signals include:

- Semantic alignment (topic similarity, shared frames)  
- Conflict markers (contradictions, incompatible claims)  
- Drift indicators (shifts in framing or terminology)  
- Fragmentation (divergence across communities)  
- Narrative half‑life (persistence of storylines)  
- Interpretability (clarity, consistency, legibility)

These signals allow adapters to detect whether narratives are stable, plural, conflicting, or collapsing.

---

## ⏱ Temporal Cadence Signals (T)

Temporal Cadence captures the speed and decay pressure of the media environment. Relevant raw signals include:

- Update frequency (posts per minute/hour/day)  
- Acceleration (increasing posting or engagement rates)  
- Refresh pressure (demand for constant novelty)  
- Persistence (how long items remain visible or relevant)  
- Compression (shrinking half‑life of information)  
- Burstiness (irregular temporal clustering)

These signals allow adapters to measure how fast the system is moving and how much strain cadence is placing on signal and narrative.

---

## 🧬 Cross‑Axis Composite Signals

Some raw signals map to multiple axes simultaneously. These composites are especially important for invariant evaluation.

- **Virality signatures** → A + D + T  
- **Misinformation patterns** → S + N  
- **Outrage cycles** → A + N + T  
- **Silo hardening** → D + N  
- **Epistemic decay** → S + T  
- **Narrative churn** → N + T + A  

Adapters may use composite signals to improve vector accuracy without interpreting content.

---

## 🧱 Signal Normalization

All raw signals must be normalized to the range **0.0–1.0** before being mapped to the substrate. Normalization strategies include:

- Min‑max scaling  
- Log scaling for heavy‑tailed distributions  
- Z‑score normalization for volatility metrics  
- Temporal smoothing for cadence and attention  
- Graph‑based normalization for topology metrics  

Normalization ensures that all adapters produce comparable vectors regardless of input type.

---

## 📚 Signal Summary

Media signals fall into five structural categories:

- **Signal Integrity** — fidelity and noise  
- **Distribution Topology** — flow and structure  
- **Attention Dynamics** — energy and volatility  
- **Narrative Coherence** — meaning and stability  
- **Temporal Cadence** — speed and decay pressure  

These signals form the raw material that adapters convert into the MSM’s structural primitives.
