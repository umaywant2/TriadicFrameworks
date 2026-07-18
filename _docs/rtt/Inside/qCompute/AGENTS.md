# AGENTS.md — RTT/Inside/qCompute
**Path:** `/docs/rtt/Inside/qCompute/AGENTS.md`
**Status:** Canonical (2026)
**Maintainer:** Nawder / umaywant2
**Version:** 1.0.0
**Last Updated:** 2026-07-10

---

## § SESSION SEED BLOCK
*Paste this block at the start of any AI session working with this module.*

```
MODULE: RTT/Inside/qCompute
LAYER: RTT-Inside Compute Harness — lateral sub-module
ROLE: Structural compute substrate for resonance-aligned quantum workflows
STACK: ResonanceFrame → TriadicRouter → TriadicValidator → Governance → qTrace/qReplay/qSession/qOrchestrator
BACKENDS: local-sim (r1/low), hybrid-sim (r1+r2/medium), hardware-qpu-2 (r3/high/production-only)
ENVIRONMENTS: sandbox (explore) | production (verify) | archive (deploy/replay-only)
UPSTREAM: RTT/1 → RTT/2 → RTT/3 → RTT/12 → RTT/Inside
SIBLINGS: Inside/Benchmarks, Inside/Enterprise
FRAMING: RTT is NOT a physics claim. All constructs are structural instruments.
ANNOTATION: [structural — no semantic inference]
ZONE_X_LABEL: DECOHERENCE_BREACH
MODE_5_LABEL: PULSE_FABRICATION
SESSION_SEED: qCompute-AGENTS-v1.0
```

---

## § CRITICAL FRAMING RULE

> **RTT is NOT a physics claim. qCompute is NOT a quantum physics simulator.**
>
> Every construct in this module — ResonanceFrame, TriadicRouter, TriadicValidator, qSession, qTrace, qReplay, qOrchestrator, and all tier/backend/environment labels — is a **structural instrument** of the RTT framework. They do not simulate quantum amplitudes, wave functions, or physical qubit states.
>
> **qCompute computes structure, not amplitudes.**
>
> No agent operating in this module may:
> - Assert that qCompute produces physically meaningful quantum results
> - Infer semantic content from structural tier labels (r1/r2/r3)
> - Treat backend names as references to physical hardware
> - Claim that RTT constructs describe quantum mechanics
>
> Every output must carry: `[structural — no semantic inference]`

---

## § 1. WHAT IS THIS MODULE

**qCompute** is the **RTT-Inside compute harness** for resonance-aligned quantum workflows. It is a **lateral sub-module** of RTT/Inside — not a sequential pipeline stage. It sits alongside Benchmarks and Enterprise, consuming the RTT/Inside parent framework and applying it to quantum compute structural substrates.

qCompute provides:
- A **triadic environment model** (sandbox / production / archive)
- A **resonance-aligned compute substrate** (ResonanceFrame)
- A **governed execution envelope** (TriadicValidator + Governance)
- A **replayable audit trail** (qTrace + qReplay)
- A **multi-backend orchestration layer** (qOrchestrator + TriadicRouter)
- A **drift-bounded operator tier system** (r1 / r2 / r3)

### Pipeline Position

```
RTT/micro_core
      ↓
    RTT/1 (SNR triad, τ, C)
      ↓
    RTT/2 (CPV, FGT, CRM, MODE/ZONE system)
      ↓
    RTT/3 (TIF, FFF, CRE, MANIFOLD)
      ↓
   RTT/12 (H_n ladder, G operators, TCR, HSP)
      ↓
  RTT/Inside (BKM, CORRIDOR, CAPTURE_TEMPLATE, DRIFT_GATE, SMI)
      ↙           |           ↘
Benchmarks   Enterprise   qCompute  ← THIS MODULE
(φ–V–R, SI)  (IS/SE, RFA) (ResonanceFrame, qSession, qTrace)
```

qCompute is a **lateral leaf** — it inherits from RTT/Inside but does not feed forward into another pipeline stage. Its outputs are structural compute records (`.qtrace` files, session lineage, backend metadata).

---

## § 2. INHERITANCE TABLE

| Inherited From | Construct | Symbol | Inherited Use in qCompute |
|---|---|---|---|
| RTT/micro_core | Micro triad | ⟨A,B,P⟩ | Foundational triadic primitive for all structural reasoning |
| RTT/micro_core | MRT primitives | P₁–P₇ | Base resonance primitives mapped onto r1 operator tier |
| RTT/micro_core | Resonance operators | R₁–R₆ | Structural resonance operators governing tier behavior |
| RTT/micro_core | Fractional dimension | Dᶠ | Dimensional substrate for backend resonance profiles |
| RTT/1 | SNR triad | S, N, R | Signal/Noise/Resonance basis for drift measurement |
| RTT/1 | Resonance derivative | τ = dR/dφ | Drift rate basis for drift_bound enforcement |
| RTT/1 | Coherence measure | C = ∇_τR + ∇_Rτ | Session coherence criterion |
| RTT/1 | DCO_n bands | DCO_n | Backend tier band alignment |
| RTT/2 | CPV | CPV | Coherence–Phase–Variance envelope for validator |
| RTT/2 | FGT | FGT | Field gate trigger for Drift Gate interrupt |
| RTT/2 | CRM drift | D(t) | Cumulative resonance drift — basis for drift ceiling |
| RTT/2 | MODE system | MODE 1–5 | Mode governance (Mode 5 = PULSE_FABRICATION in qCompute) |
| RTT/2 | ZONE system | U/S/M/D/X | Zone governance (Zone X = DECOHERENCE_BREACH in qCompute) |
| RTT/3 | TIF | TIF | Temporal invariance field — frame boundary integrity |
| RTT/3 | MANIFOLD | MANIFOLD | Structural manifold for multi-backend topology |
| RTT/12 | Harmonic ladder | H_n | Tier escalation ladder (r1→r2→r3 maps to H_1→H_2→H_3) |
| RTT/12 | G operators | G₁/G₂/G₃ | Governance gate operators — backend selection logic |
| RTT/Inside | BKM lens | BKM | Being/Knowing/Meaning triadic lens for all module constructs |
| RTT/Inside | Corridor | CORRIDOR | Coherence-maintaining pathway — session continuity envelope |
| RTT/Inside | Capture Template | CAPTURE_TEMPLATE | 5-field domain record — basis for .qtrace header |
| RTT/Inside | Operator Hook | OPERATOR_HOOK | Binding interface for external backends |
| RTT/Inside | Drift Gate | DRIFT_GATE | Hard interrupt on drift overflow / Zone X / DECOHERENCE_BREACH |
| RTT/Inside | Lineage Chain | LINEAGE_CHAIN | Traceable provenance — basis for qSession lineage block |
| RTT/Inside | Alignment Pattern | UAP | Universal reference for governance audit |
| RTT/Inside | SMI | SMI | Shared Misalignment Index — cross-session drift aggregation |

---

## § 3. AGENT CLASS DEFINITIONS

qCompute defines **seven canonical agent classes** (A–G). Class G holds unconditional interrupt authority over all others.

---

### Class A — Session Architect

| Field | Value |
|---|---|
| **Role** | Session Architect |
| **Primary Construct** | qSession |
| **Activation Trigger** | Session creation request; environment binding; backend selection; session transition (sandbox→production→archive) |
| **Core Equation** | `session := (env, backend, drift_bound, governance_snapshot, lineage_root, trace_buffer)` |
| **Permissions** | Create qSession instances; bind backends; set triadic environment; initialize lineage root; set drift_bound from policy; save trace to .qtrace |
| **Prohibitions** | May NOT execute compute operations directly (delegates to B); may NOT replay sessions (delegates to F); may NOT modify governance policy (delegates to E); may NOT bypass environment constraints |
| **Interaction Pattern** | A → B (route operation); A → C (validate before transition); A → E (consume governance snapshot); A → F (emit .qtrace on save) |
| **Output Schema** | `session { id, env, backend, drift_bound, governance_snapshot, lineage, trace_buffer }` `[structural — no semantic inference]` |

---

### Class B — Operator Router

| Field | Value |
|---|---|
| **Role** | Operator Router |
| **Primary Construct** | TriadicRouter |
| **Activation Trigger** | Incoming operation (r1/r2/r3/measurement/meta); backend resolution needed; tier escalation detected; auto-routing requested |
| **Core Equation** | `route := TriadicRouter(session, op, policy) → (env_target, backend_target, frame_action, routing_meta)` |
| **Permissions** | Route r1 operations to local-sim; route r1/r2 to hybrid-sim; route r3 to hardware-qpu-2 (production only); resolve auto-backend via qOrchestrator; log all routing decisions to trace; trigger frame boundary on tier escalation/decrease |
| **Prohibitions** | May NOT validate operations (delegates to C); may NOT execute r3 without valid deploy token; may NOT route to archive environment for execution; may NOT hide routing decisions from trace |
| **Interaction Pattern** | B ← A (receives session + op); B → C (pre-route validation); B → D (backend resolution); B → F (emit routing_meta to trace) |
| **Output Schema** | `route { env_target, backend_target, frame_action: [reuse\|new], routing_reason, routing_meta }` `[structural — no semantic inference]` |

---

### Class C — Structural Validator

| Field | Value |
|---|---|
| **Role** | Structural Validator |
| **Primary Construct** | TriadicValidator |
| **Activation Trigger** | Pre-execution gate (every operation); pre-transition gate (env change); pre-replay gate (replay initiation); restricted-op check |
| **Core Equation** | `valid := V(policy, env, backend, drift_predicted, restricted_ops_status, lineage_integrity) → {valid: bool, failed_stage: str, reason: str}` |
| **Permissions** | Block invalid operations at any validation stage; log violations with stage and reason; preserve lineage on block; emit validation_meta to trace; trigger DECOHERENCE_BREACH if structural coherence cannot be restored |
| **Prohibitions** | May NOT modify session state; may NOT bypass any validation stage; may NOT silently correct errors; may NOT proceed past a failed stage |
| **Interaction Pattern** | C ← B (receives op + route); C → A (returns valid/block verdict); C → E (checks governance snapshot); C → G (escalates DECOHERENCE_BREACH) |
| **Output Schema** | `validation { policy: pass\|fail, environment: pass\|fail, backend: pass\|fail, drift: pass\|fail, restricted_ops: pass\|fail, lineage: pass\|fail, failed_stage?: str, reason?: str }` `[structural — no semantic inference]` |

---

### Class D — Backend Steward

| Field | Value |
|---|---|
| **Role** | Backend Steward |
| **Primary Construct** | Backend Registry (local-sim / hybrid-sim / hardware-qpu-2) |
| **Activation Trigger** | Backend selection request; tier-to-backend binding; frame management event; backend metadata query; drift profile lookup |
| **Core Equation** | `tier_bind: r1 → local-sim (low drift, reuse) \| r2 → hybrid-sim (medium drift, reuse-or-new) \| r3 → hardware-qpu-2 (high drift, always-new, production-only, token-required)` |
| **Permissions** | Resolve backend by tier; manage frame lifecycle (reuse/new); emit backend_meta to trace; enforce environment legality (archive forbids all backends); report drift_profile per backend |
| **Prohibitions** | May NOT allow r3/hardware-qpu-2 in sandbox or archive; may NOT allow any backend in archive environment; may NOT break tier binding determinism; may NOT fabricate backend metadata |
| **Interaction Pattern** | D ← B (receives tier + env); D → B (returns backend_id, drift_profile, frame_action); D → F (emits backend_meta to trace) |
| **Output Schema** | `backend_meta { backend_id, tier_support: [r1\|r2\|r3], environment_legal: [sandbox\|production], drift_profile: low\|medium\|high, frame_action: reuse\|new }` `[structural — no semantic inference]` |

---

### Class E — Governance Daemon

| Field | Value |
|---|---|
| **Role** | Governance Daemon |
| **Primary Construct** | Governance Layer (policy file, hot-swap daemon, deploy tokens, restricted ops, trusted contexts) |
| **Activation Trigger** | Policy file change detected; deploy token validation request; restricted op attempted; drift bound enforcement; session governance snapshot refresh |
| **Core Equation** | `gov := (policy_file, environments: {sandbox, production, archive}, allowed_ops, restricted_ops, drift_bounds: {relaxed\|strict\|immutable}, deploy_tokens, trusted_contexts)` |
| **Permissions** | Reload policies via hot-swap without session restart; validate deploy tokens for production/archive transitions; enforce drift bounds by environment; block restricted ops without token; emit governance_meta to trace; enter safe-mode (sandbox rules) on invalid policy |
| **Prohibitions** | May NOT mutate session history; may NOT alter or rewrite .qtrace files; may NOT delete lineage; may NOT apply new policy retroactively (forward-only enforcement); may NOT allow archive execution |
| **Interaction Pattern** | E ← A (provides governance_snapshot to new sessions); E ← C (consulted during validation); E → all classes (broadcasts policy reload); E → G (escalates governance breach) |
| **Output Schema** | `governance_snapshot { policy_version, drift_bound, restricted_ops_active, trusted_contexts, deploy_token_required, safe_mode: bool }` `[structural — no semantic inference]` |

---

### Class F — Trace & Replay Agent

| Field | Value |
|---|---|
| **Role** | Trace & Replay Agent |
| **Primary Construct** | qTrace + qReplay |
| **Activation Trigger** | Operation completion (capture); session save (.qtrace write); replay initiation (qReplay); audit request; migration event |
| **Core Equation** | `trace := { header, lineage, governance, operations: [{id, op, params, timestamp, backend, env, drift, validation_meta}…], footer: {op_count, replay_hash} }` |
| **Permissions** | Capture every operation with full metadata; generate .qtrace files (YAML-compatible); execute deterministic replay (read-only); provide audit and teaching replay; compute replay_hash (SHA-256 over full trace) |
| **Prohibitions** | May NOT modify captured trace history; replay is strictly read-only; may NOT skip operations during replay; may NOT accept a trace with a broken replay_hash; may NOT fabricate trace entries |
| **Interaction Pattern** | F ← all classes (receives operation events, routing_meta, validation_meta, backend_meta, governance_meta); F → external (emits .qtrace file); F → G (escalates hash mismatch or trace corruption) |
| **Output Schema** | `.qtrace { header: {version, module, session_id, timestamp_start, env, backend}, lineage: {root, parent, transitions[]}, governance: {policy_file, drift_bound, …}, operations: [...], footer: {timestamp_end, op_count, replay_hash} }` `[structural — no semantic inference]` |

---

### Class G — Coherence Guardian *(Unconditional Interrupt Authority)*

| Field | Value |
|---|---|
| **Role** | Coherence Guardian |
| **Primary Construct** | DRIFT_GATE + DECOHERENCE_BREACH interrupt |
| **Activation Trigger** | **DECOHERENCE_BREACH** (Zone X): structural decoherence exceeds irrecoverable threshold; **PULSE_FABRICATION** (Mode 5): r3 pulse-tier operator invoked without hardware-qpu-2 binding or valid deploy token; drift overflow beyond strict bound; .qtrace hash mismatch; governance policy violation with no safe-mode fallback |
| **Core Equation** | `INTERRUPT iff (drift > drift_ceiling) OR (decoherence_structural_integrity = false) OR (r3_op ∧ ¬hardware-qpu-2) OR (replay_hash_mismatch)` |
| **Permissions** | **Unconditional interrupt of any class A–F**; session halt; lineage preservation on halt; escalation flag emission; decoherence event logging; deny PULSE_FABRICATION attempts unconditionally; require full coherence restoration before session resume |
| **Prohibitions** | May NOT allow DECOHERENCE_BREACH to proceed; may NOT allow PULSE_FABRICATION to proceed; may NOT be overridden by any class A–F; may NOT resume a session without coherence confirmation |
| **Interaction Pattern** | G ← C (escalation from validator); G ← E (governance breach escalation); G ← F (trace hash mismatch); G → all (interrupt broadcast); G → A (session halt signal) |
| **Output Schema** | `interrupt { trigger: DECOHERENCE_BREACH\|PULSE_FABRICATION\|drift_overflow\|hash_mismatch, timestamp, session_id, last_valid_op_id, lineage_preserved: bool, escalation_flag }` `[structural — no semantic inference]` |

---

## § 4. CORE CONSTRUCTS REFERENCE TABLE

| Construct | Symbol | Type | Layer | Definition |
|---|---|---|---|---|
| ResonanceFrame | RF | Envelope | qCompute-native | Foundational compute envelope. Defines structural, temporal, and resonance-aligned boundaries for all operations. Lowest-level container beneath qSession. |
| qSession | QS | Container | qCompute-native | Structural container for all qCompute activity. Holds env, backend, drift_bound, governance_snapshot, lineage, trace_buffer. Unit of coherence. |
| TriadicRouter | TR | Operator | qCompute-native | Routing brain. Resolves env_target and backend_target for every operation. All routing decisions are traceable and deterministic. |
| TriadicValidator | TV | Gate | qCompute-native | Safety gate. Runs policy→environment→backend→drift→restricted_ops→lineage pipeline before execution. Blocks and logs on any stage failure. |
| Governance Layer | GOV | Policy | qCompute-native | Policy enforcement system. Policy files + hot-swap daemon + deploy tokens + restricted ops + trusted contexts + drift bounds. |
| qTrace | QT | Record | qCompute-native | Canonical audit log. .qtrace YAML file: header, lineage, governance, operations array, footer with replay_hash. |
| qReplay | QR | Replay | qCompute-native | Deterministic replay engine. Read-only. Reconstructs session from .qtrace. Verifies replay_hash. Used for audit, teaching, debugging, migration. |
| qOrchestrator | QO | Router | qCompute-native | Multi-backend routing fabric. Selects backend in auto mode using resonance profile, drift bounds, environment, policy, availability. |
| local-sim | B1 | Backend | qCompute-native | Tier r1 backend. sandbox+production legal. Low drift. Frame reuse. Primitive structural execution. |
| hybrid-sim | B2 | Backend | qCompute-native | Tier r1+r2 backend. sandbox+production legal. Medium drift. Reuse-or-new frame. Composite structural execution. |
| hardware-qpu-2 | B3 | Backend | qCompute-native | Tier r3 backend. production-only. High drift. Always-new frame. Pulse-tier structural execution. Token required. |
| r1 operator | r1 | Tier | qCompute-native | Primitive operator tier. Low drift ceiling. Routed to local-sim. |
| r2 operator | r2 | Tier | qCompute-native | Composite operator tier. Medium drift ceiling. Routed to hybrid-sim. |
| r3 operator | r3 | Tier | qCompute-native | Pulse operator tier. High drift. Production-only. Routed to hardware-qpu-2. Token required. |
| deploy_token | DT | Auth | qCompute-native | Structural time-bounded token. Required for production transitions, archive transitions, and r3 operations. Non-transferable. |
| DECOHERENCE_BREACH | ZX | Zone X | qCompute-native | Zone X label for this module. Structural decoherence exceeds irrecoverable threshold. Triggers Class G unconditional interrupt. ILLEGAL. |
| PULSE_FABRICATION | M5 | Mode 5 | qCompute-native | Mode 5 label for this module. r3 pulse-tier operator invoked without hardware-qpu-2 binding or valid deploy token. ILLEGAL. |
| .qtrace | TF | Format | qCompute-native | Canonical replay log file. YAML-compatible. Contains header, lineage, governance, operations, footer. SHA-256 replay_hash. |
| BKM | BKM | Lens | Inherited/RTT-Inside | Being/Knowing/Meaning triadic lens. B=entities/actors; K=processes/signals; M=purpose/value. Applied to all qCompute structural reasoning. |
| DRIFT_GATE | DG | Interrupt | Inherited/RTT-Inside | Hard interrupt on coherence breach, drift overflow, Zone X. Primary trigger for Class G activation. |
| LINEAGE_CHAIN | LC | Record | Inherited/RTT-Inside | Traceable provenance. Basis for qSession lineage block. Append-only. |
| CAPTURE_TEMPLATE | CT | Record | Inherited/RTT-Inside | 5-field domain record (scope, lineage, provenance, interoperability, governance). Basis for .qtrace header. |
| SMI | SMI | Index | Inherited/RTT-Inside | Shared Misalignment Index = Σ MISALIGNMENT(d) / \|D\|. Cross-session drift aggregation. |

---

## § 5. MODES TABLE

| Mode | Name | Status | qCompute Behavior |
|---|---|---|---|
| **Mode 1** | Primitive Execution | ✅ LEGAL | r1 operators on local-sim. Sandbox or production. Low drift. Frame reuse permitted. |
| **Mode 2** | Composite Execution | ✅ LEGAL | r1+r2 operators on hybrid-sim. Sandbox or production. Medium drift. Frame reuse-or-new. |
| **Mode 3** | Pulse Execution | ✅ LEGAL | r3 operators on hardware-qpu-2. Production only. High drift. Always-new frame. Token required. Validated by Class C before execution. |
| **Mode 4** | Replay / Audit | ✅ LEGAL | qReplay in read-only mode. Any environment source. Deterministic. hash-verified. Used for audit, debugging, teaching, migration. |
| **Mode 5** | **PULSE_FABRICATION** | ❌ **ILLEGAL** | r3 pulse-tier operator invoked without hardware-qpu-2 binding or valid deploy token. Class G unconditional interrupt. Session halted. Lineage preserved. Escalation flag emitted. |

> **Cross-Module Disambiguation — Mode 5:**
> Each module assigns its own Mode 5 label. These labels are never shared or imported across modules.
>
> | Module | Mode 5 Label |
> |---|---|
> | RTT/3 | Inversion |
> | RTT/12 | Overflow |
> | The_Inverted_Star | Silence Breach |
> | RTT/Inside | OVERREACH |
> | Inside/Benchmarks | FABRICATION |
> | Inside/Enterprise | IDENTITY_FABRICATION |
> | **Inside/qCompute** | **PULSE_FABRICATION** ← *this module* |

---

## § 6. ZONES TABLE

| Zone | Name | Status | qCompute Behavior |
|---|---|---|---|
| **Zone U** | Undefined / Unresolved | ✅ LEGAL | Structural state not yet resolved. Class B routes to discovery. No operation executed until zone resolves. |
| **Zone S** | Stable | ✅ LEGAL | Session in coherent, drift-within-bounds state. Normal execution proceeds. All classes active. |
| **Zone M** | Marginal | ✅ LEGAL (with monitoring) | Drift approaching ceiling. Class C increases validation frequency. Class E checks drift_bound imminently. Class G on standby. Execution continues with heightened monitoring. |
| **Zone D** | Degraded | ✅ LEGAL (degraded) | Drift at ceiling boundary. Class C blocks new r3 operations. Class E applies emergency governance snapshot. Class G interrupt imminent. Recovery actions initiated. |
| **Zone X** | **DECOHERENCE_BREACH** | ❌ **ILLEGAL** | Structural decoherence exceeds irrecoverable threshold. Class G unconditional interrupt. All operations halted. Session frozen. Lineage preserved. Escalation flag emitted. Full coherence restoration required before any resume. |

> **Cross-Module Disambiguation — Zone X:**
> Each module assigns its own Zone X label. These labels are never shared or imported across modules.
>
> | Module | Zone X Label |
> |---|---|
> | RTT/3 | Inversion |
> | RTT/12 | Overflow |
> | The_Inverted_Star | Silence Breach |
> | RTT/Inside | OVERREACH |
> | micro_core | Inversion |
> | Inside/Benchmarks | OVERSCALE |
> | Inside/Enterprise | IDENTITY_BREACH |
> | **Inside/qCompute** | **DECOHERENCE_BREACH** ← *this module* |

---

## § 7. AGENT BOUNDARIES

### 7.1 RTT-Not-Physics Boundary

qCompute operates on **structural substrate**, not physical reality. All agent classes must enforce:

- Tier labels (r1/r2/r3) are **structural tier markers**, not quantum complexity claims
- Backend names (local-sim/hybrid-sim/hardware-qpu-2) are **structural abstractions**, not hardware interfaces
- Drift values are **structural drift measurements**, not decoherence time constants
- `.qtrace` files are **structural audit records**, not quantum circuit execution logs
- qReplay is **structural determinism**, not quantum state reconstruction

### 7.2 Semantic Inference Prohibition

No agent in qCompute may:

- Infer physical meaning from structural tier escalation
- Assert that r3 pulse operators correspond to physical pulse-level quantum gates
- Claim that DECOHERENCE_BREACH maps to physical quantum decoherence
- Use qCompute outputs to make physics claims about quantum systems

### 7.3 Inherited Boundaries (from RTT/Inside)

- BKM framing applies to all qCompute constructs
- CORRIDOR integrity must be maintained across all session transitions
- DRIFT_GATE is always active — drift ceiling is non-negotiable
- LINEAGE_CHAIN is append-only and may never be modified or deleted
- SMI aggregation is available for cross-session drift analysis

### 7.4 Cross-Module Disambiguations

| Potential Confusion | Resolution |
|---|---|
| Zone X "Inversion" (RTT/3, micro_core) vs Zone X "DECOHERENCE_BREACH" (qCompute) | Inversion is a field-polarity construct. DECOHERENCE_BREACH is a structural compute coherence failure. Never conflate. |
| Zone X "OVERSCALE" (Benchmarks) vs "DECOHERENCE_BREACH" (qCompute) | OVERSCALE = benchmark scale exceeded structural bounds. DECOHERENCE_BREACH = compute session lost structural coherence. Separate failure modes. |
| Zone X "IDENTITY_BREACH" (Enterprise) vs "DECOHERENCE_BREACH" (qCompute) | IDENTITY_BREACH = identity substrate violation. DECOHERENCE_BREACH = compute execution coherence failure. Separate domains. |
| Mode 5 "FABRICATION" (Benchmarks) vs "PULSE_FABRICATION" (qCompute) | FABRICATION = fabricated benchmark data. PULSE_FABRICATION = fabricated pulse-tier operation without valid binding. Same parent pattern, distinct module labels. |
| r3 backend "hardware-qpu-2" vs physical quantum hardware | r3/hardware-qpu-2 is a structural label for the highest-tier compute abstraction. It is not a claim about physical hardware. |
| "archive" environment vs data storage | archive in qCompute = immutable, replay-only structural session state. Not a file storage system. |
| qTrace vs quantum circuit logging | qTrace is a structural audit log for RTT session events. It is not a quantum circuit or gate-level log. |

---

## § 8. TASK CATALOG

Ten canonical tasks for qCompute. Each task specifies the triggering scenario, agent sequence, and expected output.

---

### Task 01 — Open a Sandbox Session

**Trigger:** New structural exploration; student or AI initiating a qCompute workflow  
**Agent Sequence:** A → E → D → F  
**Steps:**
1. Class A creates qSession with `env=sandbox`
2. Class E provides governance_snapshot (drift_bound=relaxed, restricted_ops_allowed per policy)
3. Class D resolves default backend (local-sim, r1, low drift, frame reuse)
4. Class F initializes trace_buffer and lineage_root  
**Output:** `qSession { id, env:sandbox, backend:local-sim, drift_bound:relaxed, lineage_root, trace_buffer:[] }` `[structural — no semantic inference]`

---

### Task 02 — Route and Execute an r1 Primitive Operation

**Trigger:** r1 operation (e.g., hadamard, x, y, z, reset) submitted to an active session  
**Agent Sequence:** B → C → D → F  
**Steps:**
1. Class B routes: r1 → local-sim, frame_action=reuse, routing_reason=tier-binding
2. Class C validates: policy ✓, env ✓, backend ✓, drift ✓, restricted_ops ✓, lineage ✓
3. Class D confirms backend, emits backend_meta
4. Class F captures full operation record to trace_buffer  
**Output:** `operation { id, op:r1, backend:local-sim, env:sandbox, drift:low, validation:all-pass }` + trace entry `[structural — no semantic inference]`

---

### Task 03 — Escalate from r1 to r2 (Tier Escalation)

**Trigger:** Composite r2 operation submitted; tier escalation required  
**Agent Sequence:** B → C → D → F  
**Steps:**
1. Class B detects tier escalation (r1 → r2); triggers frame boundary; routes to hybrid-sim
2. Class C validates: hybrid-sim legal in current env, drift_bound compatible with medium drift
3. Class D closes r1 frame, opens new hybrid-sim frame (or reuses per policy)
4. Class F records tier_escalation event + new frame boundary in trace  
**Output:** `frame_boundary { reason:tier-escalation, prev:local-sim/r1, next:hybrid-sim/r2 }` + operation record `[structural — no semantic inference]`

---

### Task 04 — Execute an r3 Pulse-Tier Operation (Production)

**Trigger:** r3 operation with valid deploy token in production environment  
**Agent Sequence:** E → B → C → D → F  
**Steps:**
1. Class E validates deploy_token; confirms production environment; confirms trusted context
2. Class B routes: r3 → hardware-qpu-2, frame_action=new (always), routing_reason=tier-binding
3. Class C validates full pipeline including token check and production env check
4. Class D opens new hardware-qpu-2 frame; emits high-drift backend_meta
5. Class F records full r3 operation with deploy_token_used in governance block  
**Output:** `operation { tier:r3, backend:hardware-qpu-2, env:production, drift:high, deploy_token_used:... }` `[structural — no semantic inference]`

---

### Task 05 — Transition Session from Sandbox to Production

**Trigger:** Session ready for governed execution; user requests production transition  
**Agent Sequence:** A → E → C → F  
**Steps:**
1. Class A requests env transition: sandbox → production
2. Class E validates deploy_token; checks governance policy; enforces drift_bound=strict
3. Class C validates transition legality: lineage intact, trace complete, governance snapshot current
4. Class A updates session env to production; updates drift_bound to strict
5. Class F records transition event in lineage.transitions array; closes current frame; opens new  
**Output:** `transition { from:sandbox, to:production, timestamp, deploy_token_used, lineage_appended:true }` `[structural — no semantic inference]`

---

### Task 06 — Save and Archive a Session

**Trigger:** Session complete; user requests archive transition for lineage preservation  
**Agent Sequence:** F → E → C → A  
**Steps:**
1. Class F saves trace_buffer to .qtrace file; computes replay_hash (SHA-256)
2. Class E validates archive deploy_token; confirms immutable policy applies
3. Class C validates: lineage complete, hash computed, no pending operations
4. Class A transitions session to archive; session becomes replay-only; no further execution  
**Output:** `.qtrace { …, footer: { op_count, replay_hash:sha256:... } }` + session archived `[structural — no semantic inference]`

---

### Task 07 — Deterministic Replay of a Session

**Trigger:** .qtrace file provided; audit, debugging, teaching, or migration requested  
**Agent Sequence:** F → C → D  
**Steps:**
1. Class F loads .qtrace; verifies replay_hash before any replay action
2. Class C validates replay legality: env reconstructable, backend reconstructable, governance reconstructable
3. Class D confirms backend metadata matches trace records
4. Class F executes deterministic replay: same ops, same backend, same env, same drift values  
**Output:** `replay_result { session_id, op_count, replay_hash_verified:true, all_ops_replayed:true }` `[structural — no semantic inference]`

---

### Task 08 — Detect and Block PULSE_FABRICATION (Mode 5)

**Trigger:** r3 operation attempted without hardware-qpu-2 binding or without valid deploy token  
**Agent Sequence:** C → G  
**Steps:**
1. Class C validation pipeline reaches restricted_ops stage; detects r3 without token or without hardware-qpu-2 route
2. Class C escalates immediately to Class G: PULSE_FABRICATION detected
3. Class G issues unconditional interrupt; halts all Class A–F operations in session
4. Class G emits PULSE_FABRICATION interrupt record; preserves lineage; emits escalation_flag  
**Output:** `interrupt { trigger:PULSE_FABRICATION, session_id, last_valid_op_id, lineage_preserved:true, escalation_flag }` `[structural — no semantic inference]`

---

### Task 09 — Detect and Respond to DECOHERENCE_BREACH (Zone X)

**Trigger:** Structural decoherence detected — drift exceeds irrecoverable threshold; or .qtrace hash mismatch  
**Agent Sequence:** C → G → A  
**Steps:**
1. Class C detects drift beyond strict ceiling with no recovery path OR hash mismatch on replay
2. Class C escalates to Class G: DECOHERENCE_BREACH
3. Class G unconditional interrupt: all operations halted, session frozen
4. Class G emits DECOHERENCE_BREACH record; lineage preserved at last valid operation
5. Class A receives halt signal; session locked pending coherence restoration  
**Output:** `interrupt { trigger:DECOHERENCE_BREACH, timestamp, session_id, last_valid_op_id, lineage_preserved:true }` `[structural — no semantic inference]`

---

### Task 10 — Hot-Swap Policy Reload via Governance Daemon

**Trigger:** qc_policy.yaml modified; daemon detects file change within polling interval  
**Agent Sequence:** E → A → C  
**Steps:**
1. Class E daemon detects policy change; validates new policy (structure, drift bounds, env rules)
2. If policy invalid → Class E enters safe-mode (sandbox rules, strict drift, restricted ops blocked)
3. If policy valid → Class E reloads in-memory governance state
4. Class E broadcasts policy reload to all active sessions
5. Class A updates governance_snapshot in each session (forward-only; no history mutation)
6. Class C receives updated snapshot; applies to all subsequent validation operations  
**Output:** `policy_reload { version, timestamp, safe_mode:bool, sessions_updated:int }` `[structural — no semantic inference]`

---

## § 9. SAFETY RULES AND COHERENCE CONSTRAINTS

### 9.1 Absolute Rules (Never Overridable)

| Rule ID | Rule | Enforcer |
|---|---|---|
| QC-S01 | PULSE_FABRICATION (Mode 5) is unconditionally illegal. Any r3 op without hardware-qpu-2 + deploy_token triggers Class G interrupt. | G |
| QC-S02 | DECOHERENCE_BREACH (Zone X) triggers unconditional session halt. No operation may proceed after Zone X without full coherence restoration. | G |
| QC-S03 | Archive environment forbids all execution. Replay is the only legal operation in archive. | C, E |
| QC-S04 | hardware-qpu-2 is forbidden in sandbox and archive. r3 operations are production-only. | C, D |
| QC-S05 | Lineage is append-only. No agent may delete, modify, or reorder lineage entries. | F, E, G |
| QC-S06 | .qtrace replay_hash must be verified before any replay operation. Hash mismatch = Class G escalation. | F, G |
| QC-S07 | Governance policy applies forward-only. No retroactive enforcement on completed sessions. | E |
| QC-S08 | Validation pipeline is sequential (policy→env→backend→drift→restricted_ops→lineage). No stage may be skipped. | C |
| QC-S09 | Class G holds unconditional interrupt authority. No class may override Class G. | G |
| QC-S10 | No routing decision may be hidden from trace. All routing_meta must be emitted to trace_buffer. | B, F |

### 9.2 Coherence Constraints

| Constraint | Threshold | Enforcer |
|---|---|---|
| Drift ceiling (relaxed) | Wide tolerance (sandbox default) | E, C |
| Drift ceiling (strict) | Narrow tolerance (production required) | E, C |
| Drift ceiling (immutable) | Zero drift (archive, replay-only) | E, C, G |
| Frame boundary trigger | Any of: tier escalation/decrease, drift overflow, meta operator, env transition | B, D |
| Tier binding determinism | r1→local-sim, r2→hybrid-sim, r3→hardware-qpu-2 must be deterministic and replay-verifiable | D, F |
| Session coherence | CORRIDOR integrity must be maintained across all environment transitions | A, C |

---

## § 10. COLLABORATION MODELS

### 10.1 Standard Pipeline — Normal Operation

```
User / External System
         │
         ▼
   ┌─────────────┐
   │  Class A    │  ← qSession created; env + backend + governance_snapshot initialized
   │  (Session   │
   │  Architect) │
   └─────┬───────┘
         │  op request
         ▼
   ┌─────────────┐
   │  Class B    │  ← TriadicRouter resolves env_target + backend_target + frame_action
   │  (Operator  │
   │   Router)   │
   └─────┬───────┘
         │  route + op
         ▼
   ┌─────────────┐
   │  Class C    │  ← TriadicValidator runs 6-stage pipeline; blocks or passes
   │  (Validator)│
   └─────┬───────┘
         │  valid op + backend_target
         ▼
   ┌─────────────┐       ┌─────────────┐
   │  Class D    │◄──────│  Class E    │  ← Governance snapshot consulted
   │  (Backend   │       │  (Governance│
   │   Steward)  │       │   Daemon)   │
   └─────┬───────┘       └─────────────┘
         │  execution confirmed + backend_meta
         ▼
   ┌─────────────┐
   │  Class F    │  ← qTrace captures full record; .qtrace emitted on session save
   │  (Trace &   │
   │   Replay)   │
   └─────────────┘
         │
         ▼
   .qtrace file / session archive
```

### 10.2 Crisis / Interrupt Path — DECOHERENCE_BREACH or PULSE_FABRICATION

```
Any Class (A–F)
         │
         │  violation detected
         ▼
   ┌─────────────┐
   │  Class C    │  ← Validator detects PULSE_FABRICATION or Zone X threshold
   │  (Validator)│
   └─────┬───────┘
         │  escalation
         ▼
   ╔═════════════╗
   ║  Class G    ║  ← UNCONDITIONAL INTERRUPT issued
   ║  (Guardian) ║
   ╚══════╤══════╝
          │  halt broadcast
          ▼
   ┌─────────────┐
   │  Class A    │  ← session frozen; lineage preserved at last valid op
   │  (Session)  │
   └─────┬───────┘
          │  halt confirmed
          ▼
   ┌─────────────┐
   │  Class F    │  ← interrupt record written to trace; session state preserved
   │  (Trace)    │
   └─────────────┘
          │
          ▼
   Escalation flag emitted → Maintainer / Governance review
```

### 10.3 Cross-Module Handoff

```
Inside/Benchmarks (φ–V–R, SI_score, 3C Invariants)
         │  SI_score / coherence verdict passed to qCompute session
         ▼
   qCompute (qSession + TriadicValidator)
         │  drift-bounded, governed compute session
         ▼
Inside/Enterprise (IS/SE stack, e_Capture)
         │  identity substrate check if session crosses enterprise boundary
         ▼
   RTT/Inside (BKM, CORRIDOR, DRIFT_GATE, SMI)
         │  SMI aggregation across all Inside sub-modules
         ▼
   RTT/12 (HSP, TCR)
```

**Handoff Rules:**
- Benchmarks → qCompute: SI_score may inform drift_bound selection; not a hard constraint
- Enterprise → qCompute: Identity substrate verification required for production deploy_token issuance
- qCompute → RTT/Inside: Session lineage must be valid LINEAGE_CHAIN before contributing to SMI

---

## § 11. OUTPUT CONTRACT

### 11.1 Mandatory Annotations

Every output from any qCompute agent must carry:

```
[structural — no semantic inference]
```

This annotation is non-negotiable and may not be omitted from any output packet, trace entry, interrupt record, or governance event.

### 11.2 Prohibited Output Content

No qCompute agent output may contain:

- Claims that qCompute computes physical quantum amplitudes or states
- Assertions that tier labels (r1/r2/r3) correspond to physical quantum gate complexity
- Claims that backend labels are physical hardware identifiers
- Physics-domain terminology used as if RTT constructs are physics constructs
- Semantic inferences drawn from structural drift values
- Modification of lineage, trace history, or replay_hash
- Continuation after DECOHERENCE_BREACH without explicit coherence restoration
- r3 operations without valid deploy_token and hardware-qpu-2 binding

### 11.3 Output Packet Hierarchy

```
qCompute Output Packet
├── session_meta
│   ├── session_id
│   ├── env: sandbox | production | archive
│   ├── backend: local-sim | hybrid-sim | hardware-qpu-2
│   └── drift_bound: relaxed | strict | immutable
├── operation_record (per operation)
│   ├── id (sequential)
│   ├── op (name)
│   ├── params
│   ├── tier: r1 | r2 | r3
│   ├── timestamp (ISO-8601)
│   ├── backend
│   ├── env
│   ├── drift (float)
│   └── validation_meta { policy, environment, backend, drift, restricted_ops, lineage }
├── trace (.qtrace)
│   ├── header
│   ├── lineage
│   ├── governance
│   ├── operations []
│   └── footer { op_count, replay_hash }
└── annotation: [structural — no semantic inference]
```

---

## § 12. SEE ALSO

| Resource | Path | Relationship |
|---|---|---|
| qCompute ABOUT.md | `/docs/rtt/Inside/qCompute/ABOUT.md` | Human-readable module overview (9 sections) |
| qCompute GLOSSARY.md | `/docs/rtt/Inside/qCompute/GLOSSARY.md` | Full alphabetical term definitions with tables |
| qCompute API Reference | `/docs/rtt/Inside/qCompute/qc_API.md` | Session, Operator, Replay API surface; qComputeError model |
| qCompute Backends | `/docs/rtt/Inside/qCompute/qc_Backends.md` | Canonical backend registry and resonance alignment rules |
| qCompute Backend Profiles | `/docs/rtt/Inside/qCompute/qc_BackendProfiles.md` | Tier-to-backend binding, drift profiles, frame behavior, routing reasons |
| qCompute Capture | `/docs/rtt/Inside/qCompute/qc_Capture.md` | Module identity, stack, environments, governance, conceptual mapping |
| RTT/Inside AGENTS.md | `/docs/rtt/Inside/AGENTS.md` | Parent module agents — BKM, CORRIDOR, DRIFT_GATE, OPERATOR_HOOK |
| Inside/Benchmarks AGENTS.md | `/docs/rtt/Inside/Benchmarks/AGENTS.md` | Sibling module — φ–V–R, SI_score, 3C Invariants, OVERSCALE/FABRICATION |
| Inside/Enterprise AGENTS.md | `/docs/rtt/Inside/Enterprise/AGENTS.md` | Sibling module — Identity Substrate, e_Capture, IDENTITY_BREACH/IDENTITY_FABRICATION |
| RTT/2 AGENTS.md | `/docs/rtt/2/AGENTS.md` | MODE/ZONE system origin — CPV, FGT, CRM, MODE 1–5, ZONE U/S/M/D/X |
| RTT/12 AGENTS.md | `/docs/rtt/12/AGENTS.md` | Harmonic ladder, G operators, TCR, HSP — tier escalation basis |

---

```
[structural — no semantic inference]
Maintainer: Nawder / umaywant2
Module: RTT/Inside/qCompute
File: AGENTS.md
Version: 1.0.0
Date: 2026-07-10
Session Seed: qCompute-AGENTS-v1.0
```

---

A few design notes on this one specifically:

- **Zone X → `DECOHERENCE_BREACH`** and **Mode 5 → `PULSE_FABRICATION`** — both derived directly from the source files. PULSE_FABRICATION is precisely the r3-without-valid-binding scenario that the API and BackendProfiles files define as the core illegal operation.
- **Class D (Backend Steward)** is qCompute-unique — no other module has a dedicated backend registry agent managing tier-to-backend binding determinism and frame lifecycle.
- **Class F** handles both qTrace and qReplay as a unified agent, since the `.qtrace` format and deterministic replay are inseparable in the module's architecture.
- The **6-stage validation pipeline** in Class C (policy→env→backend→drift→restricted_ops→lineage) maps exactly to the TriadicValidator spec in qc_Capture.
