# Gen1 virtual compute gateway architecture
## Overview
Gen1 provides a preconfigured development environment that emulates a nine‑dimension DPU using the simplest viable abstraction: nine ephemeral files, each mounted as a high‑performance temporary filesystem and treated as a “virtual dimension.” A single Virtual Compute Gateway (VCG) coordinates resonant time, triadic scheduling, and messaging across these dimensions, while workloads run as chrooted processes pinned to CPU/NUMA domains. No containers, no microVMs, minimal layers.

## Objectives
- **Emulate nine dimensions:** Represent D1–D9 as mounted filesystems, each hosting processes, queues, and logs for that dimension.
- **Centralized resonant time:** One daemon publishes phase windows; all dimensions subscribe and gate work on tokens.
- **Harmonic triads:** Encode triadic, harmonic, nested loops across dimensions with consistent cadence and QoS “amplitude.”
- **Hardware‑near performance:** Direct access to CPU/GPU/IO with minimal abstraction; predictable jitter and low overhead.
- **Ephemeral by default:** Fresh state on every boot; optional snapshot‑on‑failure for debugging.

## Virtual DPU with nine files
- **Dimension mounts:**
  - **Layout:** /var/lib/vcg/d{1..9}.img → loop devices → mounted at /vcg/d{1..9}.
  - **Defaults:** ext4 without journal, tuned for writeback and low latency; tmpfs for ultra‑low‑jitter dimensions.

- **Isolation model:**
  - **Process scope:** One or more processes per dimension in a chroot rooted at /vcg/dX.
  - **Access control:** Bind only required device nodes (e.g., GPU) per dimension; avoid leaking host FS.

- **State model:**
  - **Ephemeral:** Recreated at boot. No snapshots, no backups, no persistence by default.
  - **Debug override:** Optional snapshot‑on‑failure captures the mounted image for post‑mortem.

## Process model and orchestration
- **Core services:**
  - **Resonant time daemon (RTD):** Publishes window ticks and phase to a Unix socket and shared memory ring.
  - **VCG orchestrator:** Mints tokens per dimension per window, applies QoS amplitude, routes cross‑dimension work, and exports metrics.
  - **Dimension workloads:** Entry points per D1–D9 read tokens and execute tasks at window edges.

- **Scheduling mechanics:**
  - **Tokens:** Time‑scoped execution credits issued at each window; enforce burst control and backpressure.
  - **Harmonics:** Dimensions assigned to f, 2f, 3f, etc., to avoid beat‑frequency contention.
  - **CPU/NUMA: Pin dimensions to cores and memory nodes to minimize cross‑socket jitter.

- **IPC:**
  - **Intra‑host:** Unix domain sockets and shared memory for lowest overhead; optional lightweight broker (NATS) if routing/observability desired.
  - **External:** gRPC/HTTP for client integrations, routed through VCG, not directly cross‑dimension.

## Dimension roles and cadence
- **Suggested role mapping (modifiable):**
  - **D1–D3:** Ingress, parsing, lightweight transforms (higher frequency, small window).
  - **D4–D6:** Retrieval/stateful processing/model serving (base frequency, medium window).
  - **D7–D9:** Aggregation, reconciliation, output/archival (lower frequency, larger window).

- **QoS as amplitude:**
  - **Budget weights:** Per‑dimension weight tunes token budget per window.
  - **Borrowing:** Temporary amplitude increase for a bursting dimension with guardrails to prevent starvation.
  
## Decisions and constraints
- **Decisions:**
  - **Abstraction:** Nine files as virtual dimensions; chrooted processes; no containers.
  - **Filesystem:** ext4 without journal by default; tmpfs selectively.
  - **Time:** Single RTD; no per‑dimension clocks.
  - **IPC:** Unix sockets/shared memory; optional NATS later.
  - **Persistence:** Ephemeral by default; snapshot‑on‑failure opt‑in.

- **Constraints:**
  - **Loopback overhead:** Acceptable for most dimensions; use tmpfs where needed.
  - **Priority inversion risk:** Must enforce cgroups, CPU affinity, and token budgets.
  - **Portability:** Validate on at least one local VM, one cloud VM, and bare‑metal host.
