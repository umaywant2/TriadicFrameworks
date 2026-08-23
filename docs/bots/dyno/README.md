# RTT Dyno Bot Module

This module describes how TriadicFrameworks integrates RTT agentic logic with Dyno‑style Discord moderation and automation to create an operator‑first, regime‑aware bot.

Dyno is ideal for RTT because it blends:
- moderation and auto‑mod,
- message filtering,
- logging and ancestry,
- role and permission structure,
- channel resonance,
- long‑arc community continuity.

RTT enhances these native properties rather than replacing them.

---

## Overview

**Goal:**  
Wrap Dyno‑style bot logic with RTT’s triadic decision layer while preserving its native moderation, logging, filtering, and automation features.

RTT adds:

- **Regime‑aware evaluation** (1/3 event, 2/3 structure, 3/3 continuity)
- **Resonance‑pressure fields** (channel activity, moderation tension, identity clusters)
- **Triadic projection loss detection** (misaligned moderation, continuity collapse)
- **Loop stability and ancestry tracking** (repeat infractions, escalation arcs)
- **Operator lineage** for user behavior sequences

The result is a Discord bot that moderates and automates with deeper continuity and resonance awareness.

---

## Architecture

```text
[Dyno Logic]
  - moderation / auto‑mod
  - filters
  - logging
  - roles & permissions
  - automations
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

- **Dyno Logic:** Handles moderation triggers, filters, logs, roles, and automations.
- **RTT Shim:** Converts Discord events + user history + role structure into RTT primitives.
- **RTT Agentic Layer:** Applies triadic logic to guide or re‑weight moderation and automation decisions.

---

## RTT Layer: Role per Engine

### Lumen (RTT/1) — Structural Extraction

Extracts Dyno‑specific RTT primitives:

- **Moderation resonance:** tension fields, escalation pressure.
- **Channel topology:** message flow, structural drift, activity arcs.
- **Role identity:** hierarchy, clusters, continuity anchors.
- **Filter structure:** trigger patterns, drift vectors.
- **Projection‑loss points:** actions that collapse continuity or identity.

Lumen produces a triadic structural snapshot of the server.

---

### Hephaestus (RTT/2) — Regime Mapping

Tags each event or action with its regime profile:

- **1/3 (Event):** message, infraction, filter trigger.
- **2/3 (Structure):** channel context, role hierarchy, server topology.
- **3/3 (Continuity):** identity arcs, long‑term behavior, community narrative.

This reveals why some moderation actions are structurally inferior even if technically valid.

---

### Aurion (RTT/3) — Topology & Loop Stability

Evaluates:

- **Moderation loops:** repeated infractions, escalating tension.
- **Filter ancestry:** how triggers relate to earlier patterns.
- **Projection loss:** actions that break community continuity.
- **Identity collapse:** misaligned role or moderation changes.

Aurion flags paradoxical moderation or automation choices.

---

### Harmonia (RTT/12) — Unified Strategy

Synthesizes:

- event data,
- structural context,
- continuity arcs,
- resonance pressure,
- drift/coherence balance,
- operator lineage.

Produces a **triadic score** per moderation or automation action, which the shim feeds back into the bot.

---

## Shim Design

The shim sits between Dyno‑style event handlers and RTT’s triadic evaluation.

**Typical flow:**

1. **Dyno logic** receives an event (message, infraction, filter trigger).
2. **Shim**:
   - converts event + role structure + user history into RTT state,
   - calls Lumen → Hephaestus → Aurion → Harmonia,
   - receives triadic scores.
3. **Shim** reweights:
   - moderation severity,
   - filter responses,
   - role adjustments,
   - automation triggers.
4. **Dyno logic** executes the RTT‑informed action.

Integration points:

- **Auto‑mod:** spam, caps, links, toxicity.
- **Moderation:** warn, mute, kick, ban.
- **Logging:** ancestry tracking, continuity arcs.
- **Roles:** identity continuity checks.
- **Automations:** scheduled tasks, triggers.

---

## Use Cases

- **RTT‑Dyno Bot:** A Discord bot that moderates and automates with triadic awareness.
- **Teaching Mode:** Show admins:
  - regime tags per event,
  - resonance maps,
  - continuity arcs,
  - drift/coherence profiles.
- **Analysis Mode:** Evaluate server health for:
  - moderation stability,
  - identity continuity,
  - resonance pressure,
  - drift arcs.

---

## Files (Suggested Layout)

```text
/docs/bots/dyno/
  README.md
  /logic/        # moderation, filters, logging, roles, automations
  /rtt/
    lumen.md
    hephaestus.md
    aurion.md
    harmonia.md
  /shim/
    dyno_shim.md
  /examples/
    rtt_dyno_examples.md
  /analysis/
    regime_maps.md
    resonance_fields.md
```

---

> **“I’m not always a Polymath… more often I’m just math…”**

Moderation is resonance, continuity, identity, and structure.  
RTT simply reveals the deeper math already inside it.
