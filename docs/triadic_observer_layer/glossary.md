# Glossary

This glossary defines shared terminology used across the Triadic Observer Layer documentation. Terms are intentionally framed to emphasize **observability, restraint, and structural clarity**, rather than authority or interpretation.

---

- **Triadic Observer Layer (TOL)** — A read‑only observability substrate that preserves phase, source, and time across complex systems without asserting authority or control.

- **Observation** — A structured emission describing a metric at a specific phase, from a specific source, at a specific time. Observations assert context, not correctness.

- **Phase** — The declared lifecycle stage of an observation within a process. Phases are explicit, non‑exclusive, and never inferred.

- **Source** — The system, process, or actor that emitted an observation. Sources are named but not ranked or trusted by the observer.

- **Time Axis** — The temporal context of an observation, capturing when it existed in its reported form. Time is first‑class and immutable once recorded.

- **Triadic Axes** — The three orthogonal dimensions (phase, source, time) through which all observations are interpreted.

- **Entity** — The smallest independently observable unit within a domain (e.g., precinct, facility, model version).

- **Metric** — A named quantity or state being observed. Metrics describe measurements, not guarantees or outcomes.

- **Confidence** — A declarative label describing the emitter’s certainty or status (e.g., provisional, audited). Confidence does not override phase or source.

- **Artifact Lineage** — The preserved history of observations, including superseded or corrected values, maintaining traceability across time.

- **Phase Collapse** — The loss of distinction between lifecycle stages, often leading to premature certainty or narrative compression.

- **Source Divergence** — The presence of conflicting observations from different sources. Treated as informational, not adversarial.

- **Temporal Incoherence** — Discontinuities or irregularities in timing, such as delays, jumps, or out‑of‑order events.

- **Anomaly** — A pattern of incoherence across one or more triadic axes. Anomalies are classified diagnostically, not judged.

- **Read‑Only Posture** — The observer’s strict non‑intervention stance. It observes and reports without modifying upstream systems.

- **Regime Awareness** — Recognition that assumptions, conditions, and behaviors change over time, requiring uncertainty to remain visible.

- **Coherence** — Structural alignment across phase, source, and time. Coherence emerges from preserved structure, not enforced agreement.

- **Legibility** — The ability for humans and institutions to understand system behavior through preserved structure rather than narrative simplification.

---

This glossary is shared across all domains.  
Terms are invariant unless explicitly extended by a domain‑specific schema.
