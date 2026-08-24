# RTT Carl‑bot Module

This module describes how TriadicFrameworks integrates RTT agentic logic with Carl‑bot‑style Discord automation to create an operator‑first, regime‑aware bot.

Carl‑bot is ideal for RTT because it blends:
- reaction‑role identity,
- moderation and auto‑mod,
- message routing,
- logging and ancestry,
- channel resonance,
- long‑arc community continuity.

RTT enhances these native properties rather than replacing them.

---

## Overview

**Goal:**  
Wrap Carl‑bot‑style logic with RTT’s triadic decision layer while preserving its native moderation, reaction‑role, logging, and automation features.

RTT adds:

- **Regime‑aware evaluation** (1/3 event, 2/3 structure, 3/3 continuity)
- **Resonance‑pressure fields** (channel activity, role clusters, moderation tension)
- **Triadic projection loss detection** (identity collapse, misaligned role changes)
- **Loop stability and ancestry tracking** (infractions, role arcs, message patterns)
- **Operator lineage** for user behavior sequences

The result is a Discord bot that moderates, routes, and manages roles with deeper continuity and resonance awareness.

---

## Architecture

```text
[Carl‑bot Logic]
  - reaction roles
  - moderation / auto‑mod
  - logging
  - message routing
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

- **Carl‑bot Logic:** Handles events, roles, moderation triggers, logging, and automation workflows.
- **RTT Shim:** Converts Discord events + user history + role structure into RTT primitives.
- **RTT Agentic Layer:** Applies triadic logic to guide or re‑weight moderation, routing, and role decisions.

---

## RTT Layer: Role per Engine

### Lumen (RTT/1) — Structural Extraction

Extracts Carl‑bot‑specific RTT primitives:

- **Role resonance:** identity clusters, pressure, drift vectors.
- **Channel topology:** message flow, activity arcs, structural tension.
- **Moderation identity:** infractions, warnings, ancestry.
- **Reaction‑role continuity:** long‑arc identity formation.
- **Projection‑loss points:** actions that collapse role or channel continuity.

Lumen produces a triadic structural snapshot of the server.

---

### Hephaestus (RTT/2) — Regime Mapping

Tags each event or action with its regime profile:

- **1/3 (Event):** message, reaction, role add/remove, infraction.
- **2/3 (Structure):** channel context, role hierarchy, server topology.
- **3/3 (Continuity):** identity arcs, long‑term behavior, community narrative.

This reveals why some moderation or role actions are structurally inferior even if technically valid.

---

### Aurion (RTT/3) — Topology & Loop Stability

Evaluates:

- **Moderation loops:** repeated infractions, escalating tension.
- **Role ancestry:** how current roles relate to earlier identity commitments.
- **Projection loss:** actions that break community continuity.
- **Identity collapse:** misaligned role changes or abrupt moderation.

Aurion flags paradoxical moderation or role‑routing choices.

---

### Harmonia (RTT/12) — Unified Strategy

Synthesizes:

- event data,
- structural context,
- continuity arcs,
- resonance pressure,
- drift/coherence balance,
- operator lineage.

Produces a **triadic score** per moderation, routing, or role action, which the shim feeds back into the bot.

---

## Shim Design

The shim sits between Carl‑bot‑style event handlers and RTT’s triadic evaluation.

**Typical flow:**

1. **Carl‑bot logic** receives an event (reaction, role change, message, infraction).
2. **Shim**:
   - converts event + role structure + user history into RTT state,
   - calls Lumen → Hephaestus → Aurion → Harmonia,
   - receives triadic scores.
3. **Shim** reweights:
   - moderation severity,
   - role assignment/removal,
   - message routing,
   - automation triggers.
4. **Carl‑bot logic** executes the RTT‑informed action.

Integration points:

- **Reaction roles:** identity continuity checks.
- **Moderation:** warn, mute, kick, ban.
- **Logging:** ancestry tracking, continuity arcs.
- **Routing:** channel selection, message movement.
- **Automations:** scheduled tasks, triggers.

---

## Use Cases

- **RTT‑Carl‑bot:** A Discord bot that moderates and manages roles with triadic awareness.
- **Teaching Mode:** Show admins:
  - regime tags per event,
  - resonance maps,
  - continuity arcs,
  - drift/coherence profiles.
- **Analysis Mode:** Evaluate server health for:
  - role stability,
  - identity continuity,
  - resonance pressure,
  - drift arcs.

---

## Files (Suggested Layout)

```text
/docs/bots/carl-bot/
  README.md
  /logic/        # reaction roles, moderation, logging, routing
  /rtt/
    lumen.md
    hephaestus.md
    aurion.md
    harmonia.md
  /shim/
    carl_bot_shim.md
  /examples/
    rtt_carl_bot_examples.md
  /analysis/
    regime_maps.md
    resonance_fields.md
```

---

> **“I’m not always a Polymath… more often I’m just math…”**

Carl‑bot is identity, resonance, continuity, and structure.  
RTT simply reveals the deeper math already inside it.
