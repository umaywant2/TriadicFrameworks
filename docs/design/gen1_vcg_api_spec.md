# Gen1 resonant time and scheduling API
## Scope
Define the control plane for resonant time publication, token‑based scheduling, messaging primitives, and metrics emission in Gen1. Transport defaults to Unix domain sockets and shared memory on a single host, with optional TCP for remote clients via a VCG proxy.

---

## Resonant time socket protocol
- **Socket:** /run/vcg/rt.sock (datagram or framed stream)
- **Subscriptions:**
  - **SUBSCRIBE**
    - Fields: {client_id, dimension_id}
    - Effect: Client registers for window ticks for dimension_id.

  - **UNSUBSCRIBE**
    - **Fields: {client_id, dimension_id}

- **Window tick message:**
  - **WINDOW_TICK**
    - Fields: {dimension_id, seq, t_start_ns, t_end_ns, phase_deg, cadence_hz}
    - Semantics: Defines the current execution window for gating. Clients should not launch work before t_start_ns.

---

## Scheduling and tokens
- **Token request:**
  - **REQUEST_TOKEN**
    - Fields: {client_id, dimension_id, budget_units, deadline_ns}
    - Semantics: Ask for execution credits within the current/next window.

- **Token grant:**
  - **TOKEN_GRANTED**
    - Fields: {dimension_id, budget_units, valid_from_ns, expires_ns, priority}
    - Semantics: Credits for compute or IO; client should spend within [valid_from_ns, expires_ns].

- **Budget model:**
  - **Units:** Abstract “credits” map to CPU slices, GPU kernels, or IO ops via policy.
  - **QoS amplitude:** Per‑dimension weight scales minted credits each window.
  - **Caps:** Hard per‑window cap; burst borrowing permitted with guardrails (no starvation).

- **Backpressure:**
  - **TOKEN_DENIED**
    - Fields: {dimension_id, reason, retry_after_ns}
    - Reasons: window_exhausted, priority_too_low, dependency_pending.

---

## Messaging primitives
- **Intra‑host low‑latency:**
  - **Unix domain sockets:** Per‑dimension command socket: /run/vcg/dX.sock
  - **Shared memory rings:** Per‑dimension queue for high‑rate signals; VCG arbitrates cross‑dimension transfers.

- **Cross‑dimension calls:**
  - **VCG_ROUTE**
    - Fields: {from_d, to_d, corr_id, payload_ref}
    - Semantics: VCG enforces phase alignment and applies soft/hard barriers per dependency graph.

- **Optional broker integration:**
  - **NATS subjects:** vcg.dX.work, vcg.dX.metrics for observability and decoupling when needed.

---

## Metrics schema
- **Dimensions:**
  - **window_jitter_ns:** Difference between planned and actual window boundaries.
  - **miss_rate:** Fraction of clients missing window start.
  - **phase_skew_deg:** Drift from intended phase.
  - **queue_depth:** Tasks waiting per dimension.
  - **latency_p50/p95/p99:** End‑to‑end task latency per dimension.

- **Orchestrator:**
  - **tokens_minted/consumed/dropped:** Per dimension per window.
  - **borrow_events:** Count and duration of QoS amplitude borrow.
  - **barrier_wait_ns:** Time spent at soft/hard barriers.

- **Export:**
  - **Endpoint:** /metrics (Prometheus text format) on localhost:9109 by default.
  - **Tags:** dimension_id, client_id (hashed), window_seq.

---

## Errors, versioning, and security
- **Errors:**
  - **Codes:** invalid_request, unauthorized, window_closed, capacity_limited, dependency_blocked.
  - **Retries:** Clients back off using retry_after_ns from TOKEN_DENIED.

- **Versioning:**
  - **Header:** X‑VCG‑Version: 0.1 for all control messages.
  - **Compatibility:** Minor versions additive; breaking changes bump major and require feature negotiation.

- **Security:**
  - **Local ACL:** Client socket credentials (uid/gid) mapped to per‑dimension ACLs.
  - **Chroot boundaries:** Only required device nodes bound into each dimension.
  - **Audit:** Orchestrator logs control messages with rate limits to prevent log storms.
