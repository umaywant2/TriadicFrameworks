### Resonance‑aware comms protocol (RTT‑Inside | underground mesh)

Below is a **protocol sketch** we can drop straight into `docs/_ideas/RTT-Inside_Coal_Resonance_Comms.md`. It’s not just packets—it’s how the mesh *feels* the mine.

---

## 1. Design goals

- **Survive the rock:** tolerate attenuation, reflections, partial collapses.  
- **Exploit resonance:** use vibration, gas, and field data as first‑class citizens.  
- **Stay cheap:** run on tiny, low‑power nodes.  
- **Be local‑first:** work even when backhaul is gone.  
- **Serve humans:** prioritize safety, clarity, and simple operator signals.

---

## 2. Stack overview

**Physical layer (PHY):**

- **Low‑frequency RF** (sub‑GHz) or **acoustic/vibration coupling** where RF is impossible.  
- Simple, robust modulations (FSK/LoRa‑class or narrowband acoustic tones).  
- Power‑aware duty cycling; nodes wake on schedule or resonance events.

**Link layer:**

- **Neighbor discovery:** periodic beacons with node ID + health.  
- **Link quality:** RSSI + “Resonance Link Score” (RLS: stability of path over time).  
- **Collision avoidance:** simple CSMA or scheduled slots in high‑density areas.

**Network layer:**

- **Mesh routing:**  
  - Gradient‑based (toward exit / control room) + fallback flooding for alarms.  
  - Routes weighted by RLS, latency, and node health.  
- **Zone awareness:** nodes tagged by zone (Panel, Section, Belt, Shaft).

**Transport layer:**

- **Message classes:**  
  - `ALERT` (high priority, one‑way, redundant paths)  
  - `TELEMETRY` (periodic, lossy‑tolerant)  
  - `CONTROL` (acknowledged, low‑rate)  
  - `SYNC` (time/epoch alignment)  

**Application layer (RTT‑Inside invariant):**

- All payloads carry **resonance primitives**:
  - `vib_signature` (frequency bands, amplitude)  
  - `gas_vector` (type, concentration, gradient)  
  - `stress_hint` (local stability score)  
  - `clarity_score` (local S‑N‑R / RC)  

---

## 3. Core invariants

Every node obeys three invariants:

1. **Local resonance first:**  
   Always compute and broadcast local `clarity_score` and `stress_hint` at a minimum rate.

2. **Safety over throughput:**  
   `ALERT` messages pre‑empt all others; nodes may drop telemetry to forward safety traffic.

3. **Field continuity:**  
   Nodes attempt to maintain a **continuous coherence field**—if a neighbor disappears, they increase sampling and broadcast to “heal” the map.

---

## 4. Message structure

```text
HEADER
  version          (1 byte)
  msg_type         (1 byte)   // ALERT, TELEMETRY, CONTROL, SYNC
  src_id           (2 bytes)
  seq              (2 bytes)
  ttl              (1 byte)
  zone_id          (1 byte)

RESONANCE BLOCK
  clarity_score    (1 byte)   // 0–255 mapped to RC
  stress_hint      (1 byte)   // 0–255 mapped to stability
  vib_band_hash    (2 bytes)  // compressed spectral fingerprint
  gas_type         (1 byte)   // methane, CO, dust, etc.
  gas_level        (1 byte)   // scaled concentration
  drift_vector     (1 byte)   // encoded direction + magnitude

PAYLOAD (optional)
  app_data[...]              // worker IDs, commands, text, etc.

FOOTER
  crc16            (2 bytes)
```

---

## 5. Resonance‑aware routing

Each node maintains:

- **Neighbor table:** `neighbor_id`, `RLS`, `last_seen`.  
- **Zone gradient:** cost to reach control room / exit.  
- **Resonance map fragment:** local clarity + stress history.

**Routing rule:**

- Prefer paths with:
  - higher `RLS`  
  - higher `clarity_score`  
  - lower `stress_hint` (safer rock)  
- For `ALERT`:
  - send via **k best neighbors** (multi‑path)  
  - allow temporary flooding if RLS drops below threshold.

---

## 6. S‑N‑R / resonance clarity overlay

Each node computes:

- **Signal:** stable, repeated patterns in vibration/gas/pressure.  
- **Noise:** random spikes, transient hits, equipment chatter.  
- **Resonance:** persistent amplification at certain bands.

From this, it derives:

- `clarity_score` (RC)  
- `stress_hint` (local stability)  

The control room sees a **heatmap of RC + stress**, not just raw sensor values.

---

## 7. Operator‑facing behavior

For miners and foremen, the protocol collapses into simple cues:

- **Green:** comms stable, rock stable.  
- **Yellow:** comms OK, rock or gas shifting.  
- **Orange:** comms degraded, resonance unstable—move cautiously.  
- **Red:** comms failing, resonance critical—evacuate.

Messages like:

- “Section C: clarity ↓, stress ↑, gas ↑ — reduce vibration, move crews.”  
- “Belt 3 node cluster: RLS ↓, heat ↑ — shut down belt.”

---

## 8. Why this fits our mesh‑node idea

- Tiny nodes only need:
  - a cheap RF/acoustic radio,  
  - a few sensors,  
  - and the RTT‑Inside invariant logic.  
- The **network itself becomes a sensor**—not just a pipe.  
- The protocol turns our low‑cost mesh into a **living resonance graph** of the mine.
