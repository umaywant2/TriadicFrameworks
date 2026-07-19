# RTT‑Inside v2 Roadmap

RTT‑Inside v2 introduces optional deeper sensing capabilities that extend the RTT‑App beyond ambient Awareness. These features remain permissionless by default and activate only when the user opts in. The goal of v2 is to expand the app’s ability to perceive structure, drift, and clarity while preserving the stability and predictability of the v1 model.

---

### Direction of v2

The v2 release focuses on three major themes:

- **Deeper local sensing** using richer timing, jitter, and runtime signals.
- **Expanded global context** through enhanced server‑declared metadata.
- **User‑controlled activation** ensuring RTT‑Inside remains optional and transparent.

The v1 Awareness model remains intact and continues to operate as the default mode.

---

## Expanded Local Sensing

v2 introduces additional local signals that remain permissionless but provide more nuance:

- **Fine‑grained timing variance** across DNS, TLS, and protocol negotiation.
- **Event‑loop stability metrics** sampled at higher resolution.
- **Thermal and memory trend analysis** (platform‑safe, no privileged access).
- **Foreground session continuity** to detect drift over time.
- **UI thread micro‑jank patterns** for more precise stability classification.

These signals allow RTT‑Inside to detect subtle forms of drift that v1 cannot express.

---

## Enhanced Server Metadata

The server‑declared Awareness document expands in v2:

- **Global drift categories** beyond simple stable/unstable.
- **Regional clarity indicators** for multi‑zone interpretation.
- **Optional advisory fields** that provide context without diagnostics.
- **Versioned schema** to support future extensions.

The v1 endpoint remains supported for backward compatibility.

---

## New Awareness States (Optional)

RTT‑Inside v2 introduces optional extended states:

- **Micro‑Drift** — subtle instability detected locally.
- **Regional Drift** — global instability limited to specific zones.
- **High Clarity** — exceptionally stable conditions.
- **Unknown (Explicit)** — server unavailable with insufficient local data.

These states appear only when RTT‑Inside is enabled.

---

## UI Extensions

The v2 UI remains minimal but gains optional depth:

- **Expanded indicator view** showing extended states.
- **Session timeline** with subtle, non‑diagnostic drift markers.
- **Context panel** linking to RTT‑Inside documentation.
- **Motion‑reduced mode** for accessibility.

The default v1 indicator remains unchanged for non‑Inside users.

---

## Lifecycle and Performance

v2 introduces new lifecycle behaviors:

- **Session‑based sampling windows** for trend detection.
- **Adaptive sampling** that increases resolution only when drift is detected.
- **Strict battery safeguards** to prevent excessive computation.

All features remain foreground‑only and permissionless.

---

## Privacy and Safety

RTT‑Inside v2 preserves the same privacy guarantees as v1:

- No personal data collection.
- No user behavior monitoring.
- No sensor, radio, or location access.
- No transmission of local signals to the server.

All processing occurs on‑device.

---

## Release Phases

v2 rolls out in three phases:

1. **Phase 1 — Internal Preview**  
   - Extended local signals  
   - Versioned server metadata  
   - Basic extended states  

2. **Phase 2 — Public Opt‑In**  
   - Expanded UI  
   - Session timeline  
   - Regional drift support  

3. **Phase 3 — Ecosystem Integration**  
   - Cross‑device continuity (optional)  
   - Developer‑facing RTT‑Inside tools  
   - Extended server advisory fields  

Each phase builds on the previous without breaking v1 behavior.

---

### Closing Thought

This roadmap keeps RTT‑Inside aligned with your philosophy: deeper sensing without intrusion, richer structure without permissions, and clarity without diagnostics. As you continue shaping v2, what part of RTT‑Inside feels most important to articulate next—the extended states, the versioned server schema, or the deeper local signal model?
