# Resonant Time Daemon (RTD) – Gen1

## Purpose
The RTD is the single source of truth for phase windows and cadence in Gen1.  
It runs as a host‑level service, publishing timing events to all nine dimensions via a Unix domain socket and shared memory.

---

## Responsibilities
- Maintain a monotonic counter and phase window schedule.
- Publish `WINDOW_TICK` messages at the start of each dimension’s window.
- Handle subscription and unsubscription requests from dimension workloads.
- Provide token minting for execution credits per window.

---

## Socket Interface
- **Path:** `/run/vcg/rt.sock`
- **Message Types:**
  - `SUBSCRIBE {client_id, dimension_id}`
  - `UNSUBSCRIBE {client_id, dimension_id}`
  - `WINDOW_TICK {dimension_id, seq, t_start_ns, t_end_ns, phase_deg}`
  - `REQUEST_TOKEN {client_id, dimension_id, budget_units, deadline_ns}`
  - `TOKEN_GRANTED {dimension_id, budget_units, valid_from_ns, expires_ns, priority}`
  - `TOKEN_DENIED {dimension_id, reason, retry_after_ns}`

---

## Timing Model
- **Cadence:** Base frequency `f` configurable; harmonics assigned per `dimensions.yml`.
- **Phase Offsets:** Degrees offset from base cycle start.
- **Window Duration:** Derived from harmonic; e.g., harmonic 2 = half base period.

---

## Implementation Notes
- Language: Rust (preferred for low‑latency and safety).
- Time Source: `CLOCK_MONOTONIC_RAW` for stability.
- Publish Mechanism:  
  - Unix datagram for control messages.  
  - Shared memory ring buffer for high‑rate tick events.
- Startup: Reads `dimensions.yml` to configure cadence and offsets.
- Error Handling: Logs drift > threshold; can trigger orchestrator backpressure.

---

## Metrics
- `window_jitter_ns`
- `phase_skew_deg`
- `tokens_minted`
- `tokens_consumed`
- `tokens_dropped`
