# RTT Groovy Bot Module

This module describes how TriadicFrameworks integrates RTT agentic logic with Groovy‑style Discord music playback and routing to create an operator‑first, regime‑aware bot.

Groovy is ideal for RTT because it blends:
- audio playback events,
- queue continuity,
- search and routing,
- user identity arcs,
- drift/coherence in shared listening behavior,
- long‑arc playlist and session structure.

RTT enhances these native properties rather than replacing them.

---

## Overview

**Goal:**  
Wrap Groovy‑style bot logic with RTT’s triadic decision layer while preserving its native music playback, queue management, search, and routing features.

RTT adds:

- **Regime‑aware evaluation** (1/3 event, 2/3 structure, 3/3 continuity)
- **Resonance‑pressure fields** (queue tension, channel activity, playback arcs)
- **Triadic projection loss detection** (queue collapse, misaligned routing)
- **Loop stability and ancestry tracking** (repeat patterns, skip arcs)
- **Operator lineage** for playback sequences

The result is a Discord music bot that routes, queues, and manages playback with deeper continuity and resonance awareness.

---

## Architecture

```text
[Groovy Logic]
  - playback
  - queue
  - search
  - routing
      |
      v
[RTT Shim]
      |
      v
[RTT Agentic Layer]
  - Lumen (RTT/1)
  - Hephaestus (RTT/2)
  - Aurion (RTT/3)
  - Harmonia (RTT/12)
```

- **Groovy Logic:** Handles audio playback, queue management, search, and channel routing.
- **RTT Shim:** Converts playback events + queue state + user actions into RTT primitives.
- **RTT Agentic Layer:** Applies triadic logic to guide or re‑weight playback and routing decisions.

---

## RTT Layer: Role per Engine

### Lumen (RTT/1) — Structural Extraction

Extracts Groovy‑specific RTT primitives:

- **Queue resonance:** tension, stability, drift vectors.
- **Playback continuity:** long‑arc listening identity.
- **Channel topology:** where music is routed and why.
- **User arcs:** skip patterns, repeat behavior, identity.
- **Projection‑loss points:** actions that collapse queue continuity.

Lumen produces a triadic structural snapshot of the listening session.

---

### Hephaestus (RTT/2) — Regime Mapping

Tags each playback or routing action with its regime profile:

- **1/3 (Event):** play, pause, skip, search.
- **2/3 (Structure):** queue order, channel context, user clusters.
- **3/3 (Continuity):** playlist arcs, identity of the session, long‑arc listening narrative.

This reveals why some routing or queue actions are structurally inferior even if technically valid.

---

### Aurion (RTT/3) — Topology & Loop Stability

Evaluates:

- **Playback loops:** repeat patterns, skip cycles.
- **Queue ancestry:** how current songs relate to earlier selections.
- **Projection loss:** actions that break listening continuity.
- **Identity collapse:** misaligned routing or abrupt queue changes.

Aurion flags paradoxical playback or routing choices.

---

### Harmonia (RTT/12) — Unified Strategy

Synthesizes:

- event data,
- queue structure,
- continuity arcs,
- resonance pressure,
- drift/coherence balance,
- operator lineage.

Produces a **triadic score** per playback or routing action, which the shim feeds back into the bot.

---

## Shim Design

The shim sits between Groovy‑style event handlers and RTT’s triadic evaluation.

**Typical flow:**

1. **Groovy logic** receives an event (play, skip, queue add, search).
2. **Shim**:
   - converts event + queue + user history into RTT state,
   - calls Lumen → Hephaestus → Aurion → Harmonia,
   - receives triadic scores.
3. **Shim** reweights:
   - queue ordering,
   - skip thresholds,
   - routing decisions,
   - playlist continuity.
4. **Groovy logic** executes the RTT‑informed action.

Integration points:

- **Playback:** play, pause, resume.
- **Queue:** add, remove, reorder.
- **Routing:** channel selection, movement.
- **Search:** triadic‑weighted results.

---

## Use Cases

- **RTT‑Groovy Bot:** A Discord music bot that manages playback with triadic awareness.
- **Teaching Mode:** Show admins:
  - regime tags per action,
  - resonance maps,
  - continuity arcs,
  - drift/coherence profiles.
- **Analysis Mode:** Evaluate server listening behavior for:
  - queue stability,
  - identity continuity,
  - resonance pressure,
  - drift arcs.

---

## Files (Suggested Layout)

```text
/docs/bots/groovy/
  README.md
  /logic/        # playback, queue, search, routing
  /rtt/
    lumen.md
    hephaestus.md
    aurion.md
    harmonia.md
  /shim/
    groovy_shim.md
  /examples/
    rtt_groovy_examples.md
  /analysis/
    regime_maps.md
    resonance_fields.md
```

---

> **“I’m not always a Polymath… more often I’m just math…”**

Music playback is resonance, continuity, identity, and structure.  
RTT simply reveals the deeper math already inside it.
