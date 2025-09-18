# Virtual Compute Gateway Orchestrator – Gen1

## Purpose
Coordinates execution across nine virtual dimensions, enforcing resonant time windows, token budgets, and triadic harmonic loops.

---

## Responsibilities
- Read `dimensions.yml` and initialize per‑dimension state.
- Subscribe to RTD for window ticks.
- Mint execution tokens per dimension per window.
- Route cross‑dimension messages, applying soft/hard barriers.
- Adjust QoS amplitude dynamically based on load and borrowing rules.
- Export metrics for observability.

---

## Control Flow
1. **Startup:** Load config, connect to RTD, initialize IPC endpoints for each dimension.
2. **On WINDOW_TICK:**  
   - Mint tokens for that dimension.  
   - Notify waiting workloads via `/run/vcg/dX.sock`.
3. **On REQUEST_TOKEN:**  
   - Check budget and QoS weight.  
   - Grant or deny with retry hint.
4. **Cross‑dimension routing:**  
   - Enforce phase alignment.  
   - Apply barriers if dependencies require.

---

## IPC
- **Per‑dimension socket:** `/run/vcg/dX.sock`
- **Message Types:**  
  - `TOKEN_GRANTED`  
  - `TOKEN_DENIED`  
  - `VCG_ROUTE {from_d, to_d, corr_id, payload_ref}`

---

## Metrics
- `tokens_minted/consumed/dropped`
- `borrow_events`
- `barrier_wait_ns`
- `queue_depth`
- `latency_p50/p95/p99`

---

## Implementation Notes
- Language: Rust or Go.
- Concurrency: Async runtime (Tokio or equivalent).
- Config Reload: SIGHUP triggers reload of `dimensions.yml`.
- Failure Handling: If RTD is unreachable, pause all token minting and log critical.
