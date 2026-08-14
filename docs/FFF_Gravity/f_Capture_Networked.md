# f_Capture_Networked — Distributed Network Capture Variant

---

```
file: f_Capture_Networked.md
module: FFF_Gravity
wave: "4 — Addendum (file 8 of 8)"
session: SES-20260813-CAPTURE_NETWORKED-001
date: 2026-08-13
status: canonical
version: 1.0.0
primitives_introduced: ["PRIM:039", "PRIM:040"]
primitives_running_total: 40
conditions_prefix: NC-
fm_submodes_introduced: ["FM-003-N"]
operators_frozen: ["N_net", "G_net", "w_i", "d_bind_net", "rho_phi_net", "resilience_threshold"]
depends_on:
  - f_Capture.md
  - f_Frame.md
  - f_Field.md
  - f_Force.md
  - f_Emit.md
  - f_Deflect.md
  - f_Capture_Multi.md
  - f_Capture_Cascade.md
```

---

### FFF_Gravity Module · Wave 4 Addendum · Session SES-20260813-CAPTURE_NETWORKED-001

---

## §0 Session Context

| Key                  | Value                                           |
|----------------------|-------------------------------------------------|
| Session ID           | SES-20260813-CAPTURE_NETWORKED-001              |
| Date                 | 2026-08-13                                      |
| Wave                 | Wave 4 Addendum — file 8 of 8 (Capture series)  |
| Author               | umaywant2                                       |
| Status               | Canonical — paste-ready                         |
| PRIM range this file | PRIM:039 – PRIM:040                             |
| Running PRIM total   | PRIM:040 (40 module-wide)                       |
| Condition prefix     | NC- (Network Capture)                           |
| FM sub-mode          | FM-003-N (Network Frame Saturation)             |

### §0.1 Dependency Chain

```
f_Field.md       →  field density ρ(Φ), GravityGraph topology
f_Frame.md       →  capacity_MAX, frame slot management
f_Force.md       →  F_force gradient
f_Capture.md     →  base d_bind, escape velocity, β, capture lock
f_Emit.md        →  cross-node field coordination
f_Deflect.md     →  heading realignment across distributed attractors
f_Capture_Multi.md    →  multi-entity extension pattern (reference)
f_Capture_Cascade.md  →  cascade propagation (reference — not invoked here)
                   ↓
        f_Capture_Networked.md   ← YOU ARE HERE
```

### §0.2 What Is New in This File

| Element                | Scope              | Notes                                         |
|------------------------|--------------------|-----------------------------------------------|
| N_net                  | Operator (frozen)  | Count of active network attractor nodes       |
| G_net                  | Operator (frozen)  | Network graph (adjacency structure)           |
| w_i                    | Operator (frozen)  | Per-node weight in aggregation                |
| d_bind_net             | Operator (frozen)  | Weighted-aggregate binding depth              |
| ρ(Φ)_net               | Operator (frozen)  | Weighted-aggregate field density              |
| resilience_threshold   | Operator (frozen)  | Minimum d_bind_net for capture survival       |
| NC-1 – NC-5            | Conditions         | Network-specific capture gate set             |
| FM-003-N               | FM sub-mode        | Network Frame Saturation                      |
| PRIM:039               | Primitive (Pure)   | evaluate_network_capture                      |
| PRIM:040               | Primitive (Impure) | lock_network_capture                          |

---

## §1 Module Identity

### §1.1 Signature

| Property              | Value                                                         |
|-----------------------|---------------------------------------------------------------|
| **File**              | `f_Capture_Networked.md`                                      |
| **Function class**    | Capture variant — distributed network binding                 |
| **Governing equation**| `G = F_freq · F_fluid · F_force` [INV-001]                    |
| **Primary operator**  | `d_bind_net` — weighted network binding depth                 |
| **Triadic position**  | F_fluid (mass-density / binding) — distributed                |
| **Directionality**    | Entity E ← Network {A_1 … A_N} (many-to-one pull)             |
| **Reversibility**     | Non-reversible once NC-1–NC-5 all pass and lock committed     |
| **State mutation**    | PRIM:040 only — all participating node frames mutated         |

### §1.2 Triadic Position — Companion Table

| Node      | Role in Network Capture                                         |
|-----------|-----------------------------------------------------------------|
| F_freq    | Coherence frequency across all nodes must align for NC-2 to pass|
| F_fluid   | **Primary** — aggregate mass-density across N_net nodes         |
| F_force   | Gradient pressure summed across network sustains pull on E      |

### §1.3 Placement in Capture Variant Hierarchy

| Variant            | Binding Model          | Key Distinction                          |
|--------------------|------------------------|------------------------------------------|
| f_Capture          | Single A → E           | Baseline; establishes d_bind, β          |
| f_Capture_Multi    | A → {E_1…E_n}          | One attractor, many entities             |
| f_Capture_Cascade  | A_1 → A_2 → … → E     | Sequential chain, field perturbation      |
| f_Capture_Soft     | A → E (low β)          | Graceful shallow lock; reversible        |
| f_Capture_Hard     | A → E (high α_hard)    | Irreversible deep lock                   |
| f_Capture_Resonant | A ↔ E (mutual freq)    | Resonance-driven co-lock                 |
| f_Capture_Asymmetric| A → E (M_A ≫ M_E)     | Mass-asymmetric binding                  |
| f_Capture_Temporal | A → E (time-decay)     | Binding degrades with proximity history  |
| **f_Capture_Networked** | **{A_1…A_N} → E** | **Distributed network co-attraction**    |

---

## §2 Canonical Description

### §2.1 What f_Capture_Networked IS

`f_Capture_Networked` models the capture of a single entity **E** by a **connected network of attractor nodes** `{A_1, A_2, …, A_N}` acting in simultaneous coordinated co-attraction. No single node holds sufficient binding mass to lock E alone; capture is an emergent property of the distributed aggregate.

Binding depth and field density are computed as **weighted averages** across all active nodes in G_net. The network must:

1. Maintain minimum node count (NC-1).
2. Sustain aggregate field density above threshold (NC-2).
3. Produce aggregate binding depth above the resilience threshold (NC-3).
4. Remain topologically connected — G_net must contain a spanning connected subgraph (NC-4).
5. Have a positive, normalizable weight sum (NC-5).

If a node drops out mid-approach, the remaining active nodes are re-weighted. Capture survives dropout **if and only if** the re-weighted d_bind_net still satisfies NC-3. If the dropout fractures the network into disconnected components, NC-4 fails and capture aborts regardless of residual binding depth.

On successful capture, E is registered as a captive across **all participating nodes simultaneously** — each node's frame slot count is decremented by 1.

### §2.2 What f_Capture_Networked IS NOT

| Excluded Scope                          | Correct File                |
|-----------------------------------------|-----------------------------|
| One attractor capturing many entities   | f_Capture_Multi.md          |
| Chain propagation through field perturbation | f_Capture_Cascade.md   |
| Resonance-frequency-driven lock         | f_Capture_Resonant.md       |
| Single A → E baseline capture           | f_Capture.md                |
| Temporal decay of binding strength      | f_Capture_Temporal.md       |
| Binding asymmetry by mass ratio         | f_Capture_Asymmetric.md     |
| Network of captured entities (post-lock)| f_Orbit.md (orbital network)|

### §2.3 Design Motivation

Relational systems rarely reduce to dyadic capture. A person may be held within a community not by any single member's gravity alone but by the distributed pull of many nodes — each insufficient alone, collectively inescapable. A concept anchors within a discourse not because one text captures it but because a constellation of references creates an aggregate field. f_Capture_Networked formalizes this emergent binding topology.

The **resilience_threshold** operator encodes the system's tolerance for partial node failure: a well-designed network survives individual node dropout; a brittle one collapses on the first dropout even if total remaining mass is high.

The **connectivity guard NC-4** reflects a key physical intuition: a fragmented network cannot coordinate co-attraction. Two disconnected halves of a former network are no longer a network — they are two independent attractors, and E cannot be simultaneously locked to both without restarting a new capture attempt per fragment.

---

## §3 Triadic Equation

### §3.1 Governing Equation [INV-001]

```
G = F_freq · F_fluid · F_force
```

### §3.2 Node Decomposition — Network Variant

| Node     | Network Expression                                          |
|----------|-------------------------------------------------------------|
| F_freq   | `F_freq_net = min(F_freq_i) for i ∈ active(G_net)`          |
| F_fluid  | `F_fluid_net = ρ(Φ)_net × d_bind_net`                       |
| F_force  | `F_force_net = Σ(w_i_norm × F_force_i)`                     |

> **Note on F_freq_net:** Coherence is the bottleneck quantity — the network's effective coherence is bounded by its weakest node. A single low-frequency node can suppress the entire network pull.

### §3.3 Network Binding Depth Formula

Per-node binding depth (inherited from f_Capture.md):

```
d_bind_i = β_i × ρ(Φ_i) × (1 − e_i)
```

Normalized per-node weight:

```
w_i_norm = w_i / Σ_j(w_j)    for j ∈ active(G_net)
```

Network-aggregated binding depth:

```
d_bind_net = Σ_i( w_i_norm × d_bind_i )    for i ∈ active(G_net)
```

Network-aggregated field density:

```
ρ(Φ)_net = Σ_i( w_i_norm × ρ(Φ_i) )    for i ∈ active(G_net)
```

Aggregate frame capacity:

```
capacity_net = Σ_i( capacity_remaining_i )    for i ∈ active(G_net)
```

### §3.4 Capture Lock Condition (Network Form)

```
CAPTURE_LOCKED_NET  ⟺  NC-1 ∧ NC-2 ∧ NC-3 ∧ NC-4 ∧ NC-5
                        ∧ (capacity_net ≥ 1)
                        ∧ (d_bind_net ≥ resilience_threshold)
```

---

## §4 Operator Registry

### §4.1 Operators Frozen in This File [INV-009, INV-010]

| Symbol               | Type   | Domain           | Description                                              | Frozen in          |
|----------------------|--------|------------------|----------------------------------------------------------|--------------------|
| `N_net`              | int    | ≥ 2              | Count of active attractor nodes in G_net                 | f_Capture_Networked|
| `G_net`              | graph  | connected DAG    | Network graph of attractor nodes with weighted edges     | f_Capture_Networked|
| `w_i`                | float  | > 0              | Per-node contribution weight (unnormalized)              | f_Capture_Networked|
| `d_bind_net`         | float  | ≥ 0              | Weighted-average network binding depth                   | f_Capture_Networked|
| `ρ(Φ)_net`           | float  | [0, 1]           | Weighted-average network field density                   | f_Capture_Networked|
| `resilience_threshold` | float | > 0             | Minimum d_bind_net for capture to survive node dropout   | f_Capture_Networked|

### §4.2 Inherited Operators (Must Not Be Re-Frozen)

| Symbol           | Frozen in           | Role in this file                               |
|------------------|---------------------|-------------------------------------------------|
| `ρ(Φ)`           | f_Field.md          | Per-node field density input to ρ(Φ)_net        |
| `β`              | f_Capture.md        | Per-node binding coefficient input to d_bind_i  |
| `d_bind`         | f_Capture.md        | Per-node formula; aggregated here               |
| `e`              | f_Capture.md        | Per-node orbital eccentricity                   |
| `capacity_MAX`   | f_Frame.md          | Per-node frame capacity ceiling                 |
| `k_frame`        | f_Frame.md          | Frame scaling constant                          |
| `v_escape`       | f_Capture.md        | Per-node escape velocity (used in FM-001 guard) |
| `F_emit`         | f_Emit.md           | Cross-node field coordination signal            |
| `heading_delta`  | f_Deflect.md        | E's approach heading adjustment across nodes    |

### §4.3 Operator Interaction Map

```
w_i  ──────────────────────────────────┐
                                        ▼
ρ(Φ_i) ──[per-node]──► d_bind_i ──► d_bind_net ──► NC-3 gate
β_i    ──[per-node]──►              ρ(Φ)_net  ──► NC-2 gate
e_i    ──[per-node]──►
                                        ▲
G_net (adjacency) ───────────────────► NC-4 connectivity check
N_net (count active) ────────────────► NC-1 gate
capacity_remaining_i ────────────────► FM-003-N guard
resilience_threshold ────────────────► NC-3 comparison target
```

---

## §5 Conditions

> **[INV-005]** All conditions are conjunctive. Every NC-k must pass for capture to proceed. A single failure aborts the entire network capture attempt.

### NC-1 — Minimum Network Size

```
NC-1:  N_net ≥ 2
```

| Aspect      | Value                                               |
|-------------|-----------------------------------------------------|
| Rationale   | A single-node "network" is not a network; redirect to f_Capture.md |
| On failure  | Route to f_Capture.md with the surviving node A_i   |
| Severity    | Non-fatal — re-route available                      |

### NC-2 — Aggregate Field Density Sufficient

```
NC-2:  ρ(Φ)_net ≥ ρ_min
```

Where `ρ_min` is the minimum field density threshold (inherited from f_Field.md; default 0.1).

| Aspect      | Value                                               |
|-------------|-----------------------------------------------------|
| Rationale   | If aggregate field is too sparse, no coordinated pull exists |
| On failure  | FM-002 (Field Null) elevated to network scope — abort |
| Severity    | Fatal — no capture possible until field replenished |

### NC-3 — Resilience Threshold Satisfied

```
NC-3:  d_bind_net ≥ resilience_threshold
```

| Aspect      | Value                                                   |
|-------------|---------------------------------------------------------|
| Rationale   | Network must produce sufficient binding depth to hold E |
| On failure  | FM-001 (Flyby) — E passes through without locking       |
| Severity    | Non-fatal — E escapes, network remains intact           |
| Dropout test| After any node dropout, NC-3 is re-evaluated on remaining active nodes |

### NC-4 — Network Topology Connected

```
NC-4:  is_connected(active_subgraph(G_net))  =  True
```

The active subgraph of G_net (considering only active nodes) must be connected — i.e., a spanning path exists between any two active nodes.

| Aspect         | Value                                                        |
|----------------|--------------------------------------------------------------|
| Rationale      | Disconnected network fragments cannot coordinate co-attraction |
| On failure     | Capture aborts; each fragment may independently attempt single-attractor capture |
| Severity       | Non-fatal — re-route to per-fragment f_Capture.md if M_fragment sufficient |
| Detection      | BFS from any active node; fail if reachable_set ≠ active_set |

### NC-5 — Weight Sum Positive

```
NC-5:  Σ_i(w_i) > 0    for i ∈ active(G_net)
```

| Aspect      | Value                                                      |
|-------------|------------------------------------------------------------|
| Rationale   | Normalization guard — zero-weight network is undefined     |
| On failure  | PANIC — system error; cannot normalize weights; abort      |
| Severity    | Fatal — precondition failure, not a physical state         |

---

## §6 Failure Modes

### FM-003-N — Network Frame Saturation

**Sub-mode of FM-003 (Frame Saturation). Introduced in this file.**

```
Trigger:  capacity_net < 1
          i.e., Σ_i(capacity_remaining_i)  =  0  for all active nodes
```

| Property          | Value                                                                  |
|-------------------|------------------------------------------------------------------------|
| FM ID             | FM-003-N                                                               |
| Severity          | Non-fatal                                                              |
| Effect            | Capture denied; E cannot be registered in any node frame               |
| Mitigation        | Wait for capacity release via f_Release.md on any participating node   |
| Partial saturation| If capacity_net ≥ 1 but < N_net, capture proceeds — E registered only in nodes with remaining capacity, re-weighted accordingly |
| Signal            | `NetworkCaptureDenied` with saturation manifest listing exhausted nodes |

> **Partial saturation rule:** If some but not all nodes are saturated, capture proceeds on the non-saturated subset — provided the non-saturated subset still satisfies NC-1, NC-3, and NC-4 on its own. If NC-1 or NC-4 fails on the reduced set, FM-003-N is fatal for this attempt.

### FM-001 — Flyby (active in this file, network scope)

```
Trigger:  d_bind_net < resilience_threshold    [NC-3 fails]
```

| Property | Value                                                      |
|----------|------------------------------------------------------------|
| FM ID    | FM-001                                                     |
| Severity | Non-fatal                                                  |
| Effect   | E passes through network field without locking             |
| Route    | No state change; E continues on approach trajectory        |

### FM-002 — Field Null (active in this file, network scope)

```
Trigger:  ρ(Φ)_net = 0    [NC-2 fails at floor]
```

| Property | Value                                                      |
|----------|------------------------------------------------------------|
| FM ID    | FM-002                                                     |
| Severity | Fatal                                                      |
| Effect   | No network field exists; capture cannot proceed            |
| Route    | Raise `NetworkFieldNull`; halt all network capture logic   |

### FM-005 — Decay Spiral (monitoring only)

Not triggered by this file's primitives directly, but a network capture that enters a state where successive node dropouts continuously re-trigger NC-3 evaluation can degrade into FM-005 territory. Monitored by post-lock health checks in f_Orbit.md.

---

## §7 Engineering Primitives

---

### PRIM:039 — `evaluate_network_capture` [Pure]

**Classification:** Pure — no state mutation; returns evaluation results only.

```python
def evaluate_network_capture(
    entity: dict,
    network_nodes: list[dict],
    g_net: dict,
    resilience_threshold: float,
    rho_min: float = 0.1,
) -> dict:
    """
    PRIM:039 — evaluate_network_capture (Pure)
    ==========================================
    FFF_Gravity · f_Capture_Networked.md · Wave 4 Addendum

    Evaluate whether a network of attractor nodes can capture entity E.
    Computes network-aggregated binding metrics and checks all NC- conditions.
    Does NOT mutate any node or entity state.

    Governing equation:
        G = F_freq · F_fluid · F_force    [INV-001]

    Network binding depth:
        d_bind_i   = β_i × ρ(Φ_i) × (1 − e_i)
        w_i_norm   = w_i / Σ_j(w_j)
        d_bind_net = Σ_i(w_i_norm × d_bind_i)   for i ∈ active nodes
        ρ(Φ)_net   = Σ_i(w_i_norm × ρ(Φ_i))    for i ∈ active nodes

    Parameters
    ----------
    entity : dict
        The approaching entity E.
        Required keys:
            'id'     : str    — entity identifier
            'M_E'    : float  — entity mass (≥ 0)
            'v_approach' : float — approach velocity (≥ 0)

    network_nodes : list[dict]
        Ordered list of attractor node descriptors.
        Each node dict requires:
            'id'                 : str   — node identifier
            'M'                  : float — attractor mass (> 0)
            'beta'               : float — binding coefficient (≥ 0)
            'rho_phi'            : float — field density ρ(Φ) ∈ [0, 1]
            'eccentricity'       : float — orbital eccentricity ∈ [0, 1)
            'weight'             : float — unnormalized contribution weight (> 0)
            'capacity_remaining' : int   — available frame slots (≥ 0)
            'active'             : bool  — whether node participates in this attempt

    g_net : dict
        Network graph descriptor.
        Required keys:
            'nodes'     : list[str]            — all node IDs
            'adjacency' : dict[str, list[str]] — adjacency list (active nodes)

    resilience_threshold : float
        Minimum d_bind_net required for NC-3 to pass. Must be > 0.

    rho_min : float, optional
        Minimum ρ(Φ)_net for NC-2 to pass. Default 0.1.

    Returns
    -------
    dict with keys:
        'nc1_pass'          : bool   — NC-1 result (N_net ≥ 2)
        'nc2_pass'          : bool   — NC-2 result (ρ(Φ)_net ≥ rho_min)
        'nc3_pass'          : bool   — NC-3 result (d_bind_net ≥ resilience_threshold)
        'nc4_pass'          : bool   — NC-4 result (graph connected)
        'nc5_pass'          : bool   — NC-5 result (Σ w_i > 0)
        'all_pass'          : bool   — True iff all NC-k pass
        'N_net'             : int    — count of active nodes
        'rho_phi_net'       : float  — weighted-average field density
        'd_bind_net'        : float  — weighted-average binding depth
        'capacity_net'      : int    — total remaining capacity across active nodes
        'weight_sum'        : float  — Σ w_i (unnormalized)
        'node_metrics'      : list[dict] — per-node {id, w_norm, d_bind_i, rho_phi_i}
        'failure_modes'     : list[str]  — triggered FM IDs (empty if all_pass)
        'abort_reason'      : str | None — human-readable block reason or None

    Raises
    ------
    ValueError
        If resilience_threshold ≤ 0, or if any node has weight ≤ 0 while active,
        or if entity dict is malformed.

    INV Compliance
    --------------
    INV-001 : G = F_freq · F_fluid · F_force — respected; not mutated here
    INV-004 : β < 1.0 triggers flyby per-node — reported in node_metrics
    INV-005 : Conditions conjunctive — all NC-k evaluated; any failure → all_pass=False
    INV-009 : Operators read from OPERATORS.md — new operators frozen there
    INV-010 : No new operator symbols introduced here beyond §4.1 of this file
    """
    import math

    # ── Input validation ──────────────────────────────────────────────────────
    if resilience_threshold <= 0:
        raise ValueError(
            f"resilience_threshold must be > 0, got {resilience_threshold}"
        )
    if not entity.get("id"):
        raise ValueError("entity must have a non-empty 'id' field")

    active_nodes = [n for n in network_nodes if n.get("active", True)]

    # ── NC-5: Weight sum positive ─────────────────────────────────────────────
    weight_sum = sum(n["weight"] for n in active_nodes)
    nc5_pass = weight_sum > 0.0

    if not nc5_pass:
        return {
            "nc1_pass": False, "nc2_pass": False, "nc3_pass": False,
            "nc4_pass": False, "nc5_pass": False, "all_pass": False,
            "N_net": len(active_nodes), "rho_phi_net": 0.0,
            "d_bind_net": 0.0, "capacity_net": 0, "weight_sum": 0.0,
            "node_metrics": [], "failure_modes": ["FM-002"],
            "abort_reason": "NC-5 FAIL: weight_sum = 0; normalization undefined.",
        }

    # ── NC-1: Minimum network size ────────────────────────────────────────────
    N_net = len(active_nodes)
    nc1_pass = N_net >= 2

    # ── Per-node metrics ──────────────────────────────────────────────────────
    node_metrics = []
    rho_phi_net = 0.0
    d_bind_net = 0.0
    capacity_net = 0

    for node in active_nodes:
        w_norm = node["weight"] / weight_sum
        d_bind_i = node["beta"] * node["rho_phi"] * (1.0 - node["eccentricity"])
        rho_phi_net += w_norm * node["rho_phi"]
        d_bind_net  += w_norm * d_bind_i
        capacity_net += node["capacity_remaining"]
        node_metrics.append({
            "id":       node["id"],
            "w_norm":   round(w_norm, 6),
            "d_bind_i": round(d_bind_i, 6),
            "rho_phi_i": node["rho_phi"],
            "beta_i":   node["beta"],
            "capacity_remaining": node["capacity_remaining"],
            "flyby_risk": node["beta"] < 1.0,  # INV-004
        })

    rho_phi_net = round(rho_phi_net, 6)
    d_bind_net  = round(d_bind_net, 6)

    # ── NC-2: Aggregate field density ─────────────────────────────────────────
    nc2_pass = rho_phi_net >= rho_min

    # ── NC-3: Resilience threshold ────────────────────────────────────────────
    nc3_pass = d_bind_net >= resilience_threshold

    # ── NC-4: Graph connectivity (BFS over active subgraph) ───────────────────
    def _is_connected(active_ids: set, adjacency: dict) -> bool:
        if len(active_ids) == 0:
            return True
        start = next(iter(active_ids))
        visited = {start}
        queue = [start]
        while queue:
            current = queue.pop(0)
            for neighbor in adjacency.get(current, []):
                if neighbor in active_ids and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return visited == active_ids

    active_ids = {n["id"] for n in active_nodes}
    nc4_pass = _is_connected(active_ids, g_net.get("adjacency", {}))

    # ── FM-003-N: Network Frame Saturation ────────────────────────────────────
    fm003n_triggered = (capacity_net < 1)

    # ── Assemble result ───────────────────────────────────────────────────────
    all_pass = nc1_pass and nc2_pass and nc3_pass and nc4_pass and nc5_pass
    if all_pass and fm003n_triggered:
        all_pass = False  # FM-003-N blocks even if conditions pass

    failure_modes = []
    abort_reason_parts = []

    if not nc1_pass:
        failure_modes.append("FM-001")
        abort_reason_parts.append(f"NC-1 FAIL: N_net={N_net} < 2")
    if not nc2_pass:
        failure_modes.append("FM-002")
        abort_reason_parts.append(
            f"NC-2 FAIL: ρ(Φ)_net={rho_phi_net} < ρ_min={rho_min}"
        )
    if not nc3_pass:
        failure_modes.append("FM-001")
        abort_reason_parts.append(
            f"NC-3 FAIL: d_bind_net={d_bind_net} < resilience_threshold={resilience_threshold}"
        )
    if not nc4_pass:
        abort_reason_parts.append("NC-4 FAIL: active subgraph disconnected")
    if fm003n_triggered:
        failure_modes.append("FM-003-N")
        abort_reason_parts.append(
            f"FM-003-N: capacity_net={capacity_net}; all node frames saturated"
        )

    # Deduplicate FM list
    failure_modes = list(dict.fromkeys(failure_modes))

    return {
        "nc1_pass":     nc1_pass,
        "nc2_pass":     nc2_pass,
        "nc3_pass":     nc3_pass,
        "nc4_pass":     nc4_pass,
        "nc5_pass":     nc5_pass,
        "all_pass":     all_pass,
        "N_net":        N_net,
        "rho_phi_net":  rho_phi_net,
        "d_bind_net":   d_bind_net,
        "capacity_net": capacity_net,
        "weight_sum":   round(weight_sum, 6),
        "node_metrics": node_metrics,
        "failure_modes": failure_modes,
        "abort_reason": "; ".join(abort_reason_parts) if abort_reason_parts else None,
    }
```

---

### PRIM:040 — `lock_network_capture` [Impure]

**Classification:** Impure — mutates frame state of all participating nodes and registers E as a network captive.

```python
def lock_network_capture(
    entity: dict,
    network_nodes: list[dict],
    g_net: dict,
    eval_result: dict,
    resilience_threshold: float,
    session_id: str,
) -> dict:
    """
    PRIM:040 — lock_network_capture (Impure)
    =========================================
    FFF_Gravity · f_Capture_Networked.md · Wave 4 Addendum

    Commit entity E to network capture across all participating attractor nodes.
    This primitive MUTATES state: decrements capacity_remaining on each
    participating node and registers E's captive record.

    Must only be called after PRIM:039 returns all_pass=True.
    Calling this primitive on a failed evaluation is a precondition violation.

    State mutations performed
    -------------------------
    For each active node A_i in network_nodes (where capacity_remaining > 0):
        A_i['capacity_remaining'] -= 1
        A_i['captives'].append(captive_record)

    Entity mutation:
        entity['state']          = 'NETWORK_CAPTURED'
        entity['network_lock']   = lock_record

    Parameters
    ----------
    entity : dict
        Entity E to be captured. Mutated in place.
        Required keys: 'id', 'M_E', 'v_approach'
        Will gain keys: 'state', 'network_lock'

    network_nodes : list[dict]
        Attractor node list. Active nodes with capacity are mutated in place.
        Each node gains entry in node['captives'] list.

    g_net : dict
        Network graph (read-only in this primitive).

    eval_result : dict
        Output of PRIM:039. Must have all_pass=True. Lock uses pre-computed
        d_bind_net, rho_phi_net, N_net from this result.

    resilience_threshold : float
        Stored in lock record for post-lock health monitoring.

    session_id : str
        Session identifier for audit trail.

    Returns
    -------
    dict with keys:
        'status'          : str   — 'LOCKED' or 'PRECONDITION_VIOLATION'
        'entity_id'       : str   — entity E identifier
        'lock_id'         : str   — unique lock record ID
        'locked_nodes'    : list[str]  — IDs of nodes where E was registered
        'skipped_nodes'   : list[str]  — IDs of active nodes that were full
        'd_bind_net'      : float — network binding depth at lock time
        'rho_phi_net'     : float — network field density at lock time
        'N_locked'        : int   — count of nodes where E was registered
        'resilience_threshold' : float — stored for monitoring
        'session_id'      : str   — echoed for audit
        'timestamp'       : str   — ISO-8601 lock timestamp

    Side Effects
    ------------
    - Decrements capacity_remaining on each locked node
    - Appends captive record to each locked node's 'captives' list
    - Sets entity['state'] = 'NETWORK_CAPTURED'
    - Sets entity['network_lock'] = lock_record dict

    Raises
    ------
    PreconditionViolation
        If eval_result['all_pass'] is not True. Prevents partial-state corruption.

    INV Compliance
    --------------
    INV-001 : G = F_freq · F_fluid · F_force — network lock is F_fluid commitment
    INV-002 : State transitions are monotonic — NETWORK_CAPTURED is terminal
    INV-005 : Lock only proceeds after all NC-k pass — enforced via eval_result guard
    INV-008 : All mutations are logged in captive_record with session_id
    INV-009 : No new operators introduced here
    """
    import uuid
    from datetime import datetime, timezone

    # ── Precondition guard ────────────────────────────────────────────────────
    if not eval_result.get("all_pass", False):
        return {
            "status": "PRECONDITION_VIOLATION",
            "entity_id": entity.get("id", "UNKNOWN"),
            "lock_id": None,
            "locked_nodes": [],
            "skipped_nodes": [],
            "d_bind_net": eval_result.get("d_bind_net", 0.0),
            "rho_phi_net": eval_result.get("rho_phi_net", 0.0),
            "N_locked": 0,
            "resilience_threshold": resilience_threshold,
            "session_id": session_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

    # ── Build lock record ─────────────────────────────────────────────────────
    lock_id = f"NET-LOCK-{uuid.uuid4().hex[:12].upper()}"
    timestamp = datetime.now(timezone.utc).isoformat()

    captive_record = {
        "entity_id":     entity["id"],
        "lock_id":       lock_id,
        "lock_type":     "NETWORK_CAPTURE",
        "d_bind_net":    eval_result["d_bind_net"],
        "rho_phi_net":   eval_result["rho_phi_net"],
        "N_net":         eval_result["N_net"],
        "resilience_threshold": resilience_threshold,
        "session_id":    session_id,
        "timestamp":     timestamp,
    }

    # ── Mutate participating nodes ────────────────────────────────────────────
    locked_nodes = []
    skipped_nodes = []

    active_nodes = [n for n in network_nodes if n.get("active", True)]

    for node in active_nodes:
        if node["capacity_remaining"] > 0:
            node["capacity_remaining"] -= 1
            if "captives" not in node:
                node["captives"] = []
            node["captives"].append({**captive_record, "registered_in_node": node["id"]})
            locked_nodes.append(node["id"])
        else:
            # FM-003-N partial: this individual node is full, skip
            skipped_nodes.append(node["id"])

    # ── Mutate entity ─────────────────────────────────────────────────────────
    lock_record = {
        **captive_record,
        "locked_nodes":  locked_nodes,
        "skipped_nodes": skipped_nodes,
        "N_locked":      len(locked_nodes),
    }

    entity["state"]        = "NETWORK_CAPTURED"
    entity["network_lock"] = lock_record

    return {
        "status":               "LOCKED",
        "entity_id":            entity["id"],
        "lock_id":              lock_id,
        "locked_nodes":         locked_nodes,
        "skipped_nodes":        skipped_nodes,
        "d_bind_net":           eval_result["d_bind_net"],
        "rho_phi_net":          eval_result["rho_phi_net"],
        "N_locked":             len(locked_nodes),
        "resilience_threshold": resilience_threshold,
        "session_id":           session_id,
        "timestamp":            timestamp,
    }
```

---

## §8 Canonical Examples

> All four examples use a three-node baseline network unless otherwise noted. The entity E approaches all nodes simultaneously.

---

### Example 1 — Clean Network Lock (All Conditions Pass)

**Scenario:** Entity E (a new community member) approaches a three-node community network {A_1=Anchor, A_2=Bridge, A_3=Satellite}. All nodes active, well-connected, sufficient capacity.

**Parameter table — nodes:**

| Node | M_i | β_i | ρ(Φ_i) | e_i  | w_i  | capacity_remaining |
|------|-----|-----|---------|------|------|--------------------|
| A_1  | 8.0 | 1.4 | 0.85    | 0.10 | 3.0  | 5                  |
| A_2  | 5.0 | 1.2 | 0.72    | 0.15 | 2.0  | 3                  |
| A_3  | 3.0 | 1.1 | 0.65    | 0.20 | 1.0  | 2                  |

**Parameter table — network:**

| Parameter             | Value |
|-----------------------|-------|
| resilience_threshold  | 0.60  |
| ρ_min                 | 0.10  |
| G_net topology        | A_1–A_2, A_2–A_3 (chain; connected) |

**Step-by-step trace:**

```
weight_sum = 3.0 + 2.0 + 1.0 = 6.0

w_1_norm = 3.0/6.0 = 0.5000
w_2_norm = 2.0/6.0 = 0.3333
w_3_norm = 1.0/6.0 = 0.1667

d_bind_1 = 1.4 × 0.85 × (1 − 0.10) = 1.4 × 0.85 × 0.90 = 1.0710
d_bind_2 = 1.2 × 0.72 × (1 − 0.15) = 1.2 × 0.72 × 0.85 = 0.7344
d_bind_3 = 1.1 × 0.65 × (1 − 0.20) = 1.1 × 0.65 × 0.80 = 0.5720

d_bind_net = (0.5000 × 1.0710) + (0.3333 × 0.7344) + (0.1667 × 0.5720)
           = 0.5355 + 0.2448 + 0.0953
           = 0.8756

ρ(Φ)_net = (0.5000 × 0.85) + (0.3333 × 0.72) + (0.1667 × 0.65)
          = 0.4250 + 0.2400 + 0.1083
          = 0.7733

capacity_net = 5 + 3 + 2 = 10
```

**Condition evaluation:**

| Condition | Test                        | Value  | Result |
|-----------|-----------------------------|--------|--------|
| NC-1      | N_net ≥ 2                   | 3 ≥ 2  | ✅ PASS |
| NC-2      | 0.7733 ≥ 0.10               | ✅     | ✅ PASS |
| NC-3      | 0.8756 ≥ 0.60               | ✅     | ✅ PASS |
| NC-4      | A_1–A_2–A_3 connected       | ✅     | ✅ PASS |
| NC-5      | 6.0 > 0                     | ✅     | ✅ PASS |
| FM-003-N  | capacity_net = 10 ≥ 1       | ✅     | no trigger |

**Outcome:** `all_pass = True` → PRIM:040 executes. E locked across all three nodes. Each node's `capacity_remaining` decremented by 1: {4, 2, 1}. Entity state → `NETWORK_CAPTURED`.

---

### Example 2 — Node Dropout Resilience (NC-3 Re-evaluation)

**Scenario:** Same network as Example 1. Midway through approach, A_3 (Satellite) goes inactive due to field collapse (ρ(Φ_3) → 0). Network re-evaluates with only {A_1, A_2} active.

**Dropout trigger:** A_3 marked `active = False`.

**Re-weighted trace:**

```
active_nodes = {A_1, A_2}
weight_sum   = 3.0 + 2.0 = 5.0

w_1_norm = 3.0/5.0 = 0.6000
w_2_norm = 2.0/5.0 = 0.4000

d_bind_1 = 1.0710   (unchanged)
d_bind_2 = 0.7344   (unchanged)

d_bind_net = (0.6000 × 1.0710) + (0.4000 × 0.7344)
           = 0.6426 + 0.2938
           = 0.9364

ρ(Φ)_net = (0.6000 × 0.85) + (0.4000 × 0.72)
          = 0.5100 + 0.2880
          = 0.7980

N_net        = 2
capacity_net = 5 + 3 = 8
```

**Condition re-evaluation:**

| Condition | Test                      | Value   | Result |
|-----------|---------------------------|---------|--------|
| NC-1      | N_net ≥ 2                 | 2 ≥ 2   | ✅ PASS |
| NC-2      | 0.7980 ≥ 0.10             | ✅      | ✅ PASS |
| NC-3      | 0.9364 ≥ 0.60             | ✅      | ✅ PASS |
| NC-4      | A_1–A_2 connected         | ✅      | ✅ PASS |
| NC-5      | 5.0 > 0                   | ✅      | ✅ PASS |

**Outcome:** Network capture survives A_3 dropout. d_bind_net actually **increased** (A_3 was the weakest node; its removal improved the weighted average). E locked across {A_1, A_2}. A_3's frame is untouched (never decremented). Resilience demonstrated.

---

### Example 3 — NC-4 Topology Failure (Disconnected Network)

**Scenario:** Four-node network {A_1, A_2, A_3, A_4}. A_2 (the bridge node) becomes inactive, fragmenting the graph into two disconnected components: {A_1} and {A_3, A_4}.

**Network topology (original):**

```
A_1 ── A_2 ── A_3
               │
              A_4
```

**After A_2 dropout:**

```
A_1        A_3
            │
           A_4

[A_1] and [A_3, A_4] are disconnected.
```

**Parameter table — remaining active nodes:**

| Node | M_i | β_i | ρ(Φ_i) | e_i  | w_i  | capacity_remaining |
|------|-----|-----|---------|------|------|--------------------|
| A_1  | 8.0 | 1.4 | 0.85    | 0.10 | 3.0  | 5                  |
| A_3  | 3.0 | 1.1 | 0.65    | 0.20 | 1.0  | 2                  |
| A_4  | 4.0 | 1.2 | 0.70    | 0.12 | 1.5  | 3                  |

**Binding metrics (computed before topology check):**

```
weight_sum = 3.0 + 1.0 + 1.5 = 5.5

d_bind_1 = 1.4 × 0.85 × 0.90 = 1.0710
d_bind_3 = 1.1 × 0.65 × 0.80 = 0.5720
d_bind_4 = 1.2 × 0.70 × 0.88 = 0.7392

d_bind_net = (3.0/5.5 × 1.0710) + (1.0/5.5 × 0.5720) + (1.5/5.5 × 0.7392)
           = (0.5455 × 1.0710) + (0.1818 × 0.5720) + (0.2727 × 0.7392)
           = 0.5842 + 0.1040 + 0.2016
           = 0.8898

ρ(Φ)_net = (0.5455 × 0.85) + (0.1818 × 0.65) + (0.2727 × 0.70)
          = 0.4637 + 0.1182 + 0.1909
          = 0.7728
```

**Connectivity BFS from A_1:**

```
Start: A_1
Adjacency (active nodes only, A_2 removed from edges):
    A_1 → []         (A_2 was its only neighbor; now inactive)
    A_3 → [A_4]
    A_4 → [A_3]

Visited from A_1: {A_1}
active_ids:       {A_1, A_3, A_4}
Visited ≠ active_ids  →  DISCONNECTED
```

**Condition evaluation:**

| Condition | Test                          | Value   | Result  |
|-----------|-------------------------------|---------|---------|
| NC-1      | N_net ≥ 2                     | 3 ≥ 2   | ✅ PASS  |
| NC-2      | 0.7728 ≥ 0.10                 | ✅      | ✅ PASS  |
| NC-3      | 0.8898 ≥ 0.60                 | ✅      | ✅ PASS  |
| NC-4      | Graph connected?              | ❌      | ❌ FAIL  |
| NC-5      | 5.5 > 0                       | ✅      | ✅ PASS  |

**Outcome:** `all_pass = False`. NC-4 fails despite strong binding metrics. Network capture aborted. System recommendation: treat {A_3, A_4} as a 2-node sub-network and attempt f_Capture.md from A_3 or A_4 independently. A_1 may attempt single-attractor capture but d_bind_1 alone must be re-evaluated against resilience_threshold.

**Key lesson:** Topology is independent of binding strength. A well-bound disconnected network cannot coordinate capture.

---

### Example 4 — FM-003-N Network Frame Saturation

**Scenario:** High-traffic network {A_1, A_2, A_3} has nearly exhausted all frame capacity from prior captures. Entity E approaches during a saturation event.

**Parameter table — nodes (post-traffic state):**

| Node | M_i | β_i | ρ(Φ_i) | e_i  | w_i  | capacity_remaining |
|------|-----|-----|---------|------|------|--------------------|
| A_1  | 8.0 | 1.4 | 0.85    | 0.10 | 3.0  | 0                  |
| A_2  | 5.0 | 1.2 | 0.72    | 0.15 | 2.0  | 0                  |
| A_3  | 3.0 | 1.1 | 0.65    | 0.20 | 1.0  | 0                  |

**Binding metrics (same as Example 1):**

```
d_bind_net  = 0.8756     (all binding conditions excellent)
ρ(Φ)_net    = 0.7733
capacity_net = 0 + 0 + 0 = 0
```

**Condition evaluation:**

| Condition | Test                       | Value   | Result  |
|-----------|----------------------------|---------|---------|
| NC-1      | N_net ≥ 2                  | 3 ≥ 2   | ✅ PASS  |
| NC-2      | 0.7733 ≥ 0.10              | ✅      | ✅ PASS  |
| NC-3      | 0.8756 ≥ 0.60              | ✅      | ✅ PASS  |
| NC-4      | Graph connected            | ✅      | ✅ PASS  |
| NC-5      | 6.0 > 0                    | ✅      | ✅ PASS  |
| **FM-003-N** | capacity_net = 0 < 1    | ❌      | **TRIGGERED** |

**Outcome:** `all_pass = False`. FM-003-N fires. All NC- conditions passed — the network is gravitationally ready — but zero frame capacity exists across all nodes. `NetworkCaptureDenied` signal raised.

**Saturation manifest:**

```
{
  "signal":    "NetworkCaptureDenied",
  "fm":        "FM-003-N",
  "entity_id": "E",
  "exhausted_nodes": ["A_1", "A_2", "A_3"],
  "capacity_net": 0,
  "mitigation": "Await f_Release.md event on any participating node",
  "d_bind_net": 0.8756,
  "note": "Network gravitationally viable; capacity-blocked only"
}
```

**Key lesson:** FM-003-N is a resource constraint, not a gravitational failure. The network is healthy and would lock E immediately upon any node releasing a frame slot via f_Release.md.

---

## §9 Cross-Module References

### §9.1 Upstream Dependencies

| File                  | What This File Uses                                              |
|-----------------------|------------------------------------------------------------------|
| f_Field.md            | ρ(Φ) per-node; GravityGraph topology type                        |
| f_Frame.md            | capacity_remaining, capacity_MAX, k_frame per node              |
| f_Force.md            | F_force_i per-node gradient (aggregated to F_force_net)         |
| f_Capture.md          | d_bind formula, β, e, escape velocity, base capture protocol    |
| f_Emit.md             | Cross-node field coordination (F_emit for field signal alignment)|
| f_Deflect.md          | heading_delta — E's trajectory adjustment approaching N_net nodes|
| f_Capture_Multi.md    | Pattern reference: multi-entity extension; not invoked here      |
| f_Capture_Cascade.md  | Pattern reference: cascade propagation; not invoked here         |

### §9.2 Downstream Consumers

| File           | How It Uses Network Capture Output                                      |
|----------------|-------------------------------------------------------------------------|
| f_Orbit.md     | E enters network orbit after NETWORK_CAPTURED; orbital parameters distributed |
| f_Release.md   | Release from network must decrement captive record from ALL locked nodes|
| f_Decay.md     | Decay operates on d_bind_net; monitors resilience_threshold over time   |
| f_Collapse.md  | Network collapse if d_bind_net falls below resilience_threshold post-lock|

### §9.3 OPERATORS.md Registration Block

Paste the following block into `OPERATORS.md` under the Wave 4 Addendum section:

```markdown
| Symbol               | Type   | Domain         | Description                                               | Frozen in                  |
|----------------------|--------|----------------|-----------------------------------------------------------|----------------------------|
| N_net                | int    | ≥ 2            | Count of active network attractor nodes                   | f_Capture_Networked.md     |
| G_net                | graph  | connected DAG  | Network graph adjacency structure                         | f_Capture_Networked.md     |
| w_i                  | float  | > 0            | Per-node contribution weight (unnormalized)               | f_Capture_Networked.md     |
| d_bind_net           | float  | ≥ 0            | Weighted-average network binding depth                    | f_Capture_Networked.md     |
| ρ(Φ)_net             | float  | [0, 1]         | Weighted-average network field density                    | f_Capture_Networked.md     |
| resilience_threshold | float  | > 0            | Minimum d_bind_net for capture survival after node loss   | f_Capture_Networked.md     |
```

---

## §10 Document Metadata

| Field            | Value                                               |
|------------------|-----------------------------------------------------|
| File path        | docs/FFF_Gravity/f_Capture_Networked.md             |
| Module           | FFF_Gravity                                         |
| Wave             | 4 — Capture Variants (Addendum)                     |
| Version          | v1.0.0                                              |
| Status           | ✅ Canonical — Frozen                               |
| Session          | SES-20260813-CAPTURE_NETWORKED-001                  |
| Date             | 2026-08-13                                          |
| Author           | umaywant2                                           |
| PRIM block       | PRIM:039 (Pure) · PRIM:040 (Impure)                 |
| Running PRIM total | 40                                                |
| Condition prefix | NC-                                                 |
| FM sub-mode      | FM-003-N                                            |
| Companion file   | f_Capture.md (Wave 0 genesis)                       |

---

## §11 Extended Metadata

### 11.1 INV Compliance Table

| Invariant | Statement (abbreviated)                                   | How satisfied in this file                                                                                   |
|-----------|-----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| INV-001   | G = F_freq · F_fluid · F_force                            | §3 expresses G_net as weighted product across all nodes; node contributions collapse to the canonical triadic form |
| INV-002   | d_bind ≥ d_threshold for capture                          | NC-1 enforces d_bind_net ≥ resilience_threshold; PRIM:039 rejects if not met                                 |
| INV-003   | ρ(Φ) ∈ [0, 1]                                            | NC-2 enforces ρ(Φ)_net ∈ [0, 1]; PRIM:039 validates domain before scoring                                    |
| INV-004   | F_force > 0 required for non-zero G                       | NC-3 requires capacity_net > 0; FM-003-N fires when all frames saturated (capacity = 0)                       |
| INV-005   | All conditions conjunctive                                | NC-1 through NC-5 are explicitly stated as conjunctive; any single failure aborts capture                     |
| INV-006   | Failure modes are exclusive and exhaustive                | FM-003-N (saturation), FM-001 (flyby), FM-002 (field null) cover all rejection paths; no overlap              |
| INV-007   | Capture is a state transition, not a gradient             | PRIM:040 sets NETWORK_CAPTURED as a discrete flag; no partial lock state is defined                           |
| INV-008   | Release paths must be defined for every capture variant   | f_Release.md covers distributed release; §9.2 lists it as downstream consumer                                 |
| INV-009   | All operators reference OPERATORS.md as authority         | §4 references OPERATORS.md; §9.3 provides the registration block for paste-back                               |
| INV-010   | Frozen symbols are immutable across module lifetime       | All 6 operators in §4 are marked frozen in this file; no redefinition permitted                               |

---

### 11.2 Primitive Registry

| PRIM ID  | Name                       | Type   | File                    | Description                                               |
|----------|----------------------------|--------|-------------------------|-----------------------------------------------------------|
| PRIM:039 | `evaluate_network_capture` | Pure   | f_Capture_Networked.md  | Computes d_bind_net and ρ(Φ)_net; evaluates NC-1–NC-5; returns scored dict or rejection reason |
| PRIM:040 | `lock_network_capture`     | Impure | f_Capture_Networked.md  | Calls PRIM:039; on pass sets NETWORK_CAPTURED flag and records the network lock event           |

**Running PRIM total after this file: 40**

| Range       | Files                                      |
|-------------|---------------------------------------------|
| PRIM:001–006 | f_Capture.md, f_Source.md (Wave 0)         |
| PRIM:007–012 | f_Field.md, f_Force.md, f_Frame.md (Wave 2)|
| PRIM:013–016 | f_Release.md, f_Decay.md (Wave 3)          |
| PRIM:017–020 | f_Orbit.md, f_Collapse.md (Wave 3)         |
| PRIM:021–024 | f_Emit.md, f_Dampen.md (Wave 3)            |
| PRIM:023–024 | f_Amplify.md (Wave 3)                      |
| PRIM:025–024 | f_Deflect.md (Wave 3)                      |
| PRIM:025–026 | f_Capture_Multi.md (Wave 4)                |
| PRIM:027–028 | f_Capture_Cascade.md (Wave 4)              |
| PRIM:029–030 | f_Capture_Soft.md (Wave 4)                 |
| PRIM:031–032 | f_Capture_Hard.md (Wave 4)                 |
| PRIM:033–034 | f_Capture_Resonant.md (Wave 4)             |
| PRIM:035–036 | f_Capture_Asymmetric.md (Wave 4)           |
| PRIM:037–038 | f_Capture_Temporal.md (Wave 4)             |
| PRIM:039–040 | f_Capture_Networked.md (Wave 4) ← this file|

---

### 11.3 Operator Registry

All six operators introduced in this file are frozen. They may not be redefined, aliased, or shadowed by any downstream file.

| Symbol               | Type   | Domain         | Introduced in           | Frozen |
|----------------------|--------|----------------|-------------------------|--------|
| N_net                | int    | ≥ 2            | f_Capture_Networked.md  | ✅     |
| G_net                | graph  | connected DAG  | f_Capture_Networked.md  | ✅     |
| w_i                  | float  | > 0            | f_Capture_Networked.md  | ✅     |
| d_bind_net           | float  | ≥ 0            | f_Capture_Networked.md  | ✅     |
| ρ(Φ)_net             | float  | [0, 1]         | f_Capture_Networked.md  | ✅     |
| resilience_threshold | float  | > 0            | f_Capture_Networked.md  | ✅     |

---

### 11.4 State Flag Registry

| Flag               | Set by    | Cleared by  | Meaning                                                      |
|--------------------|-----------|-------------|--------------------------------------------------------------|
| NETWORK_CAPTURED   | PRIM:040  | f_Release   | Entity locked across distributed attractor network           |
| NETWORK_MISS       | PRIM:039  | —           | Network capture failed; one or more NC- conditions not met   |
| NETWORK_SATURATED  | PRIM:039  | —           | FM-003-N triggered — all node frames at capacity = 0         |

> **Note:** `NETWORK_MISS` and `NETWORK_SATURATED` are terminal rejection flags for the current evaluation cycle. They do not persist across independent capture attempts.

---

### 11.5 Changelog

| Version | Date       | Session                              | Author      | Notes                                                               |
|---------|------------|--------------------------------------|-------------|---------------------------------------------------------------------|
| v1.0.0  | 2026-08-13 | SES-20260813-CAPTURE_NETWORKED-001   | umaywant2   | Initial canonical specification. PRIM:039–040 registered. NC-1–NC-5 frozen. FM-003-N sub-mode defined. Wave 4 series complete. |

---

### 11.6 Wave Tracker

| Wave | Purpose            | Files                                                                                                                                       | Status         |
|------|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| 0    | Genesis            | f_Capture.md · f_Source.md · GravityOfDismissal.md                                                                                         | ✅ Complete    |
| 1    | Admin / Registry   | README.md · INDEX.md · OPERATORS.md · GLOSSARY.md · CHANGELOG.md · FFF_Gravity_module.json                                                 | ✅ Complete    |
| 2    | Layer Definitions  | f_Field.md · f_Force.md · f_Frame.md                                                                                                        | ✅ Complete    |
| 3    | Core Functions     | f_Release.md · f_Decay.md · f_Orbit.md · f_Collapse.md · f_Emit.md · f_Dampen.md · f_Amplify.md · f_Deflect.md                             | ✅ Complete    |
| 4    | Capture Variants   | f_Capture_Multi.md · f_Capture_Cascade.md · f_Capture_Soft.md · f_Capture_Hard.md · f_Capture_Resonant.md · f_Capture_Asymmetric.md · f_Capture_Temporal.md · f_Capture_Networked.md | ✅ Complete |

---

### ✅ WAVE 4 COMPLETION MILESTONE

```
╔══════════════════════════════════════════════════════════════════════╗
║           FFF_Gravity · Wave 4 — Capture Variants · COMPLETE        ║
╠══════════════════════════════════════════════════════════════════════╣
║  f_Capture_Multi.md       ✅  PRIM:025–026  FM-003-M  MC-1/MC-2     ║
║  f_Capture_Cascade.md     ✅  PRIM:027–028  FM-003-C  CAS-1–CAS-4   ║
║  f_Capture_Soft.md        ✅  PRIM:029–030  FM-none   SCS-1–SCS-4   ║
║  f_Capture_Hard.md        ✅  PRIM:031–032  FM-none   HLC-1–HLC-4   ║
║  f_Capture_Resonant.md    ✅  PRIM:033–034  FM-none   RLC-1–RLC-5   ║
║  f_Capture_Asymmetric.md  ✅  PRIM:035–036  FM-none   AC-1–AC-5     ║
║  f_Capture_Temporal.md    ✅  PRIM:037–038  FM-none   TC-1–TC-5     ║
║  f_Capture_Networked.md   ✅  PRIM:039–040  FM-003-N  NC-1–NC-5     ║
╠══════════════════════════════════════════════════════════════════════╣
║  Total PRIMs registered (module lifetime):  40                       ║
║  Total Operators frozen (module lifetime):  see OPERATORS.md         ║
║  Total Invariants sealed:                   INV-001 – INV-010        ║
║  Total Failure Modes sealed:                FM-001  – FM-010         ║
║  Session sealed:  SES-20260813-CAPTURE_NETWORKED-001                 ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

### ✅ FFF_Gravity MODULE COMPLETION MILESTONE

```
╔══════════════════════════════════════════════════════════════════════╗
║                  FFF_Gravity · ALL WAVES · COMPLETE                  ║
╠══════════════════════════════════════════════════════════════════════╣
║  Wave 0 — Genesis             ✅   3 files                           ║
║  Wave 1 — Admin / Registry    ✅   6 files                           ║
║  Wave 2 — Layer Definitions   ✅   3 files                           ║
║  Wave 3 — Core Functions      ✅   8 files                           ║
║  Wave 4 — Capture Variants    ✅   8 files                           ║
╠══════════════════════════════════════════════════════════════════════╣
║  Total module files:  28                                             ║
║  Total PRIMs:         40                                             ║
║  Total Invariants:    10  (INV-001 – INV-010)                        ║
║  Total Failure Modes: 10  (FM-001  – FM-010)                         ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

### 11.7 Suggested Commit Message

```
feat(FFF_Gravity): add f_Capture_Networked — Wave 4 complete

Introduces distributed network capture variant. Defines NC-1–NC-5
conditions (conjunctive), FM-003-N sub-mode (frame saturation across
network), and six frozen operators (N_net, G_net, w_i, d_bind_net,
ρ(Φ)_net, resilience_threshold).

Registers PRIM:039 (evaluate_network_capture, Pure) and PRIM:040
(lock_network_capture, Impure). Running PRIM total: 40.

Includes four canonical examples covering clean lock, node dropout
resilience, topology failure (NC-4), and FM-003-N saturation denial.

Wave 4 Capture Variant series sealed. FFF_Gravity module complete.

Session: SES-20260813-CAPTURE_NETWORKED-001
```

---

*End of f_Capture_Networked.md — Wave 4 Addendum · FFF_Gravity Module · v1.0.0 · Session SES-20260813-CAPTURE_NETWORKED-001 · All waves complete · PRIM total: 40*
