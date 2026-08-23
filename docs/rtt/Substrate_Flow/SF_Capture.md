## 📁 File Manifest

| File | Role | Key Content |
| --- | --- | --- |
| **SF_Capture.md** | Design capture | Origin, 5 substrates, 4 channels, 4 driver types, drift currents, recursion lines, composite flow map, 4 design decisions |
| **README.md** | Module entry point | Badges, file tree, nav, session context, 4 quick-ref tables |
| **operators.md** | Flow engine | 4 operators (SF-Read/SF-Route/SF-Drift/SF-Tag), channel logic, driver matrix |
| **integration.md** | Pipeline map | Upstream (EC, TEL, ESI, 05a), downstream (HSP stability, Opacity), sibling diagram |
| **examples.md** | Applied walkthroughs | 5 flow scenarios (one per channel + atlas pull), cross-example comparison |
| **index.html** | Landing page | Blue/ocean theme, flow-channel glyph, DOC_MAP routing, HSP Suite nav |

## 📄 SF_Capture.md

```
# 🌊 Substrate Flow — Design Capture

> *Echoes don't sit still. This module maps how they move.*

**Module:** Substrate Flow
**Canonical ID:** SF
**HSP Section:** 08
**Capture Status:** Finalized

---

## Origin

Substrate Flow emerged during HSP development as the missing movement
layer. HSP had formalized what echoes *are* (Echo Classifier, 06c) and
where they *sit* (Triadic Echo Lattice, 07) — but no module existed to
map how echoes *move* between substrates, what drives that movement,
and what happens when movement becomes unstable.

Without a flow map, echo migration was invisible — echoes appeared in new
substrates without explanation, drift seemed random, and recursion had no
visible channel. Substrate Flow replaces guesswork with a canonical flow
architecture.

---

## Conceptual Lineage

```
HSP formalizes echo families (F1–F6)
    ↓
Echo Classifier (06c) assigns echo type (E1–E6)
    ↓
Triadic Echo Lattice (07) places echo in lattice
    ↓
╔═══════════════════════════════════════════╗
║  Substrate Flow (08) — THIS MODULE        ║
║  Maps how classified echoes move through  ║
║  substrates via channels, drivers, and    ║
║  currents                                 ║
╚═══════════════════════════════════════════╝
```

---

## What This Module Does

Substrate Flow defines:
1. **Five substrates** — the territories echoes move between
2. **Four flow channels** — the canonical pathways between substrates
3. **Four flow driver types** — the forces that cause movement
4. **Drift‑shadow currents** — destabilizing flows created by drift
5. **Recursion‑driven flow lines** — flow paths bent by recursion

---

## The Five Substrates

| ID | Substrate | Role |
|:---|:----------|:-----|
| S | Symbolic | Definitions, terms, formal notation |
| C | Cognitive | Concepts, meaning, understanding |
| H | Harmonic | Resonance, intervals, oscillation |
| So | Social | Governance, norms, collective structure |
| A | Atlas | Full‑spectrum anchoring, canonical permanence |

---

## The Four Flow Channels

| Channel | Path | Character |
|:--------|:-----|:----------|
| S → C | Symbolic → Cognitive | Definition refinement, meaning consolidation, early echo formation |
| C ↔ H | Cognitive ↔ Harmonic | Harmonic alignment, interval oscillation, cycle recursion |
| H → So | Harmonic → Social | Governance torsion, operator inversion, map recursion |
| So → A | Social → Atlas | High‑altitude resonance, atlas forcing, projection drift |

**Key Structural Note:**
- S → C is the most common flow (definition → concept).
- C ↔ H is the oscillation zone (cycle recursion).
- H → So is the governance torsion zone (map recursion).
- All flows eventually point upward toward Atlas.

---

## Flow Drivers

### ESI (Echo Strength Index)
| ESI | Flow Effect |
|:----|:------------|
| 1 | Local flow only — echo stays in origin substrate |
| 2 | Mild migration — adjacent substrate influence |
| 3 | Cross‑substrate flow — multi‑substrate movement |
| 4 | Atlas pull — full‑spectrum forcing toward A |

### Recursion Mode (R1–R4)
| Mode | Flow Line |
|:-----|:----------|
| R1 | S → C (ladder recursion) |
| R2 | C ↔ H (cycle recursion) |
| R3 | H → So (map recursion) |
| R4 | So → A (atlas recursion) |

### Drift Type (D1–D4)
| Drift | Instability Zone |
|:------|:-----------------|
| D1 | S/C instability |
| D2 | C/H instability |
| D3 | H/So instability |
| D4 | A instability |

### Echo Family (F1–F6)
| Family | Flow Behavior |
|:-------|:--------------|
| F1 | Stays low (structural) |
| F2 | Stays harmonic (oscillation) |
| F3 | Migrates (cross‑substrate) |
| F4 | Forces upward (escalation) |
| F5 | Destabilizes (drift‑shadow) |
| F6 | Anchors atlas (permanence) |

---

## Drift‑Shadow Flow Currents

Drift creates currents that pull echoes upward:

```
D1: S → C   (symbolic/cognitive instability)
D2: C → H   (cognitive/harmonic instability)
D3: H → So  (harmonic/social instability)
D4: So → A  (social/atlas instability)
```

F5 drift‑shadow echoes ride these currents. They are symptoms of
underlying structural instability, not independent events.

---

## Recursion‑Driven Flow Lines

Recursion bends substrate flow:

```
R1: S → C   (ladder — definition enters concept space)
R2: C ↔ H   (cycle — concept oscillates with harmonic)
R3: H → So  (map — harmonic enters governance space)
R4: So → A  (atlas — governance enters atlas space)
```

Echoes follow recursion lines unless stabilized by external anchoring.

---

## Composite Substrate Echo Flow Map

```
S  --(R1/D1)-->  C  --(R2/D2)-->  H  --(R3/D3)-->  So  --(R4/D4)-->  A
 \                ^       ^         \                ^               ^
  \               |       |          \               |               |
   \              |       |           \              |               |
    \             |       |            \             |               |
     \            |       |             \            |               |
      \           |       |              \           |               |
       \          |       |               \          |               |
        \         |       |                \         |               |
         \        |       |                 \        |               |
          \       |       |                  \       |               |
           +-----------------------------------------------------------+
           |                    Atlas Pull (F6)                        |
           +-----------------------------------------------------------+
```

This is the **canonical flow map**.

---

## Key Design Decisions

### 1. Four channels, not five

Despite five substrates, there are only four channels. Atlas does not
originate flow — it receives it. A is always a destination, never a source.
This is a structural invariant: the atlas collects; it does not emit.

### 2. Bidirectional C ↔ H only

Only the Cognitive ↔ Harmonic channel is bidirectional. All other channels
are unidirectional (upward). This encodes the empirical observation that
concepts and harmonics oscillate freely, but once something enters
governance (So) or atlas (A), it does not flow backward.

### 3. Drift and recursion share channels

Drift currents (D1–D4) and recursion lines (R1–R4) use the same four
channels but with different dynamics. Recursion is structural (the echo
follows a line). Drift is entropic (the echo is pulled by instability).
Same path, different physics.

### 4. Atlas Pull as gravitational metaphor

F6 echo families and ESI‑4 readings create "atlas pull" — a gravitational
force that draws echoes toward the atlas substrate. This is not a flow
channel; it is a force field that operates across all channels simultaneously.

---

## What This Module Is Not

- **Not a classifier.** Classification happens upstream (Echo Classifier, 06c).
  Substrate Flow receives pre‑classified echoes.
- **Not a lattice.** Lattice placement happens in TEL (07). Substrate Flow
  maps movement, not position.
- **Not a stability measure.** HSP stability classes and drift maps handle
  stability. Substrate Flow maps the movement patterns that stability
  analysis depends on.

---

## Referenced By

- 07 — Triadic Echo Lattice
- 05a — Cross‑Substrate Echo Matrix
- 06b — Echo Signatures
- 06c — Echo Classifier

---

## Session Origin

- **Conceptual source:** HSP analytics session (section 08)
- **First formalization:** HSP v1.0
- **Module extraction:** 2026-04-27
- **Capture finalization:** 2026-04-27

---

<!-- SESSION_CONTEXT:START -->
```yaml
file: SF_Capture.md
module: Substrate Flow
canonical_id: SF
hsp_section: 08
role: session-capture
status: finalized
origin_date: 2026-04-27
capture_type: module-extraction
parent: HSP (RTT-Analytics-Core)
siblings:
  - Echo Classifier (06c)
  - TEL (07)
lineage_note: >
  Substrate Flow was extracted from HSP section 08 as a standalone
  module to complete the HSP analytics suite alongside Echo Classifier
  and TEL.
```
<!-- SESSION_CONTEXT:END -->

```
