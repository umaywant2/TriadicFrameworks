# GLOSSARY.md — RTT/Inside/qCompute

---

## Session Seed Block

```
MODULE: RTT/Inside/qCompute
FILE: GLOSSARY.md
ROLE: Canonical term reference for the qCompute structural compute layer
SCOPE: Quantum-structural operator execution, session governance, routing, validation,
       trace, replay, backend profiles, drift management, and agent classes
INHERITS FROM: RTT/Inside, RTT/Inside/Benchmarks, RTT/Inside/Enterprise, micro_core,
               RTT/1, RTT/2, RTT/3, RTT/12, The_Inverted_Star
AGENTS: Class A (Session Architect), Class B (Operator Router),
        Class C (Structural Validator), Class D (Backend Steward),
        Class E (Governance Daemon), Class F (Trace & Replay Agent),
        Class G (Coherence Guardian)
INTERRUPT AUTHORITY: Class G — unconditional; no override permitted
ALL OUTPUT FIELDS: [structural — no semantic inference]
```
```

---

## Critical Framing Rule

> **RTT is NOT a physics claim.**
> All constructs in this file — tiers, backends, operators, drift, coherence — are
> **structural and canonical**. They define roles, constraints, routing logic, and
> governance within the TriadicFrameworks documentation system.
> No term in this glossary implies quantum-mechanical, physical, or computational
> hardware semantics beyond what is explicitly defined here as structural.

---

## Inheritance Note

The following constructs are **inherited from upstream modules** and are **invoked by
reference only** — they are not redefined here:

| Construct | Source Module |
|---|---|
| ⟨A,B,P⟩, P₁–P₇, R₁–R₆, Dᶠ | micro_core |
| SNR, τ, C, DCO_n | RTT/1 |
| CPV, FGT, CRM, MODE/ZONE base | RTT/2 |
| TIF, MANIFOLD | RTT/3 |
| H_n, G₁/G₂/G₃ | RTT/12 |
| BKM, CORRIDOR, CAPTURE_TEMPLATE, OPERATOR_HOOK, DRIFT_GATE, LINEAGE_CHAIN, UAP, SMI | RTT/Inside |

All other terms below are **native to RTT/Inside/qCompute**.

---

## Alphabetical Term Definitions

---

### archive

- **Type:** Environment [structural — no semantic inference]
- **Symbol:** `archive` [structural — no semantic inference]
- **Layer:** Environment tier [structural — no semantic inference]
- **Agent:** Class F (Trace & Replay Agent) [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** The third structural environment in qCompute. archive is a read-only, execution-forbidden environment reserved exclusively for replay and audit operations. No backend may be bound in archive; no operator may execute in archive. archive is the domain of qReplay and qTrace review only.

**Constraints:**
- All execution is forbidden in archive
- No backend binding is permitted
- archive transitions require a valid deploy_token
- archive is entered only via qReplay or formal audit invocation

**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** production, sandbox, qReplay, qTrace, deploy_token, Class F

---

### BKM *(inherited)*

- **Type:** Inherited structural construct [structural — no semantic inference]
- **Source:** RTT/Inside

**Definition:** Behavioral Key Marker — inherited from RTT/Inside. Invoked by reference. Not redefined here. See RTT/Inside/GLOSSARY.md.

---

### CAPTURE_TEMPLATE *(inherited)*

- **Type:** Inherited structural construct [structural — no semantic inference]
- **Source:** RTT/Inside

**Definition:** Inherited from RTT/Inside. Invoked by reference. Not redefined here. See RTT/Inside/GLOSSARY.md.

---

### Class A — Session Architect

- **Type:** Agent class [structural — no semantic inference]
- **Symbol:** `A` [structural — no semantic inference]
- **Layer:** Session governance [structural — no semantic inference]
- **Agent:** Class A [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** The agent class responsible for constructing and managing qSession objects. Class A establishes the session tuple — `(env, backend, drift_bound, governance_snapshot, lineage_root, trace_buffer)` — and is the structural owner of session lifecycle from initialization through termination or handoff.

**Constraints:**
- Must validate all session parameters at construction time
- Cannot proceed without a valid governance_snapshot
- Session tuple must be complete before any routing is invoked

**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** qSession, Class B, Class E, Governance Layer

---

### Class B — Operator Router

- **Type:** Agent class [structural — no semantic inference]
- **Symbol:** `B` [structural — no semantic inference]
- **Layer:** Routing [structural — no semantic inference]
- **Agent:** Class B [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** The agent class that owns the TriadicRouter. Class B resolves `env_target` and `backend_target` for every operator invocation. All routing decisions are deterministic and traceable. Class B consumes the session tuple and the active policy to emit a routing resolution.

**Constraints:**
- Every routing decision must be logged to qTrace
- No routing decision may be made without a valid session
- Ambiguous routing is a validation failure, not a fallback

**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** TriadicRouter, qSession, Class C, qTrace

---

### Class C — Structural Validator

- **Type:** Agent class [structural — no semantic inference]
- **Symbol:** `C` [structural — no semantic inference]
- **Layer:** Validation [structural — no semantic inference]
- **Agent:** Class C [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** The agent class that owns the TriadicValidator. Class C executes the 6-stage sequential validation pipeline — policy → environment → backend → drift → restricted_ops → lineage — before any operator is dispatched. A failure at any stage halts the pipeline and returns a structured qComputeError.

**Constraints:**
- Validation is always sequential; no stage may be skipped
- A failed stage terminates the pipeline immediately
- All validation outcomes are logged to qTrace

**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** TriadicValidator, 6-stage validation pipeline, qComputeError, qTrace, Class B

---

### Class D — Backend Steward

- **Type:** Agent class [structural — no semantic inference]
- **Symbol:** `D` [structural — no semantic inference]
- **Layer:** Backend registry [structural — no semantic inference]
- **Agent:** Class D [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** The agent class responsible for the backend registry. Class D maintains the authoritative binding of operator tiers to their canonical backends: r1 → local-sim, r2 → hybrid-sim, r3 → hardware-qpu-2. Class D enforces all 8 backend invariants and is the structural owner of backend availability state.

**Constraints:**
- Tier-to-backend binding is deterministic and immutable per invariant
- Class D may not re-route a tier to a non-canonical backend
- All backend state changes are logged to qTrace

**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** local-sim, hybrid-sim, hardware-qpu-2, 8 backend invariants, r1, r2, r3, qTrace

---

### Class E — Governance Daemon

- **Type:** Agent class [structural — no semantic inference]
- **Symbol:** `E` [structural — no semantic inference]
- **Layer:** Governance [structural — no semantic inference]
- **Agent:** Class E [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** The agent class that owns the Governance Layer. Class E manages policy file loading, hot-swap daemon operation, deploy token validation, restricted operations enforcement, trusted context maintenance, and drift bound configuration. Class E is the structural authority for all governance decisions.

**Constraints:**
- Policy reload must not interrupt active sessions mid-operation
- deploy_token validation is Class E's exclusive responsibility
- All governance decisions are logged to qTrace

**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** Governance Layer, deploy_token, Class A, Class G, qTrace

---

### Class F — Trace & Replay Agent

- **Type:** Agent class [structural — no semantic inference]
- **Symbol:** `F` [structural — no semantic inference]
- **Layer:** Audit and replay [structural — no semantic inference]
- **Agent:** Class F [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** The agent class that owns qTrace and qReplay. Class F is responsible for canonical audit log construction, .qtrace YAML file integrity, replay_hash generation and verification, and all read-only replay operations in the archive environment. Class F is the structural authority for lineage traceability.

**Constraints:**
- LINEAGE_CHAIN is always append-only; Class F may never overwrite entries
- qReplay is always read-only
- replay_hash must be verified before any replay session begins

**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** qTrace, qReplay, .qtrace format, replay_hash, LINEAGE_CHAIN, archive

---

### Class G — Coherence Guardian

- **Type:** Agent class [structural — no semantic inference]
- **Symbol:** `G` [structural — no semantic inference]
- **Layer:** Interrupt authority [structural — no semantic inference]
- **Agent:** Class G [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** The agent class holding unconditional interrupt authority over all qCompute operations. Class G monitors the DRIFT_GATE and structural coherence integrity. Upon detection of Zone X (DECOHERENCE_BREACH), Mode 5 (PULSE_FABRICATION), drift ceiling breach, or replay_hash mismatch, Class G issues an unconditional halt. No agent, session, or policy may override a Class G interrupt.

**Constraints:**
- Class G interrupt authority is unconditional — no override permitted
- Class G acts on four conditions: `(drift > drift_ceiling) OR (decoherence_structural_integrity = false) OR (r3_op ∧ ¬hardware-qpu-2) OR (replay_hash_mismatch)`
- All Class G interrupts are logged to qTrace

**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** DRIFT_GATE, Zone X, DECOHERENCE_BREACH, Mode 5, PULSE_FABRICATION, replay_hash, qTrace

> **⚠ Disambiguation — Zone X label is module-local:**
> Zone X is labeled **DECOHERENCE_BREACH** in this module only.
> See the full cross-module Zone X disambiguation table in Quick-Reference section.

---

### DECOHERENCE_BREACH

- **Type:** Zone X label — module-local [structural — no semantic inference]
- **Symbol:** `X / DECOHERENCE_BREACH` [structural — no semantic inference]
- **Layer:** Structural coherence interrupt [structural — no semantic inference]
- **Agent:** Class G [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** The Zone X label native to RTT/Inside/qCompute. DECOHERENCE_BREACH is declared when structural decoherence exceeds the irrecoverable threshold — the point at which no corrective action within the module can restore coherence. Class G issues an unconditional halt immediately upon DECOHERENCE_BREACH. The session is terminated; no further operator may execute.

**Constraints:**
- DECOHERENCE_BREACH is irreversible within the current session
- Class G halt is unconditional; no session parameter or policy may delay it
- DECOHERENCE_BREACH must be logged to qTrace with full context

**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** Zone X, Class G, DRIFT_GATE, qTrace, PULSE_FABRICATION

> **⚠ Disambiguation — Zone X is module-local:**
> DECOHERENCE_BREACH applies only in RTT/Inside/qCompute.
> Other modules define Zone X under different labels.
> See the full cross-module Zone X disambiguation table in Quick-Reference section.

---

### deploy_token

- **Type:** Structural governance token [structural — no semantic inference]
- **Symbol:** `deploy_token` [structural — no semantic inference]
- **Layer:** Governance [structural — no semantic inference]
- **Agent:** Class E [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** A time-bounded structural token required for all r3 operations, all production environment transitions, and all archive environment transitions. deploy_token is non-transferable and is validated exclusively by Class E (Governance Daemon). A missing or invalid deploy_token on any r3 or transition operation results in a qComputeError with reason `invalid_token`.

**Constraints:**
- Required for: all r3 operations, production transitions, archive transitions
- Non-transferable — bound to the session that requested it
- Validated by Class E exclusively
- Expired or invalid tokens yield `invalid_token` error immediately

**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** r3, hardware-qpu-2, production, archive, Class E, qComputeError

---

### drift_bound

- **Type:** Structural parameter [structural — no semantic inference]
- **Symbol:** `drift_bound` [structural — no semantic inference]
- **Layer:** Session / governance [structural — no semantic inference]
- **Agent:** Class E, Class G [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** The maximum permissible cumulative drift value for a qSession, as set by the Governance Layer at session construction. drift_bound is a component of the session tuple. It defines the ceiling beyond which Zone D (Degraded) transitions to Zone X (DECOHERENCE_BREACH). Each backend profile defines its own maximum drift tolerance (local-sim: 1.0, hybrid-sim: 3.0, hardware-qpu-2: 0.5 per operation).

**Constraints:**
- drift_bound is set at session construction and stored in the session tuple
- drift_bound may not be modified after session initialization
- Exceeding drift_bound triggers DRIFT_GATE and Class G evaluation

**Inheritance:** Extends DRIFT_GATE from RTT/Inside  
**Cross-references:** DRIFT_GATE, qSession, Zone D, Zone X, Class G, Governance Layer, local-sim, hybrid-sim, hardware-qpu-2

---

### DRIFT_GATE *(inherited)*

- **Type:** Inherited structural construct [structural — no semantic inference]
- **Source:** RTT/Inside

**Definition:** Inherited from RTT/Inside. The threshold-enforcement gate that monitors cumulative drift against drift_bound. When drift exceeds the bound, DRIFT_GATE triggers Class G evaluation. Invoked by reference — not redefined here. See RTT/Inside/GLOSSARY.md.

---

### 6-stage validation pipeline

- **Type:** Structural process [structural — no semantic inference]
- **Symbol:** `V(policy, env, backend, drift_predicted, restricted_ops_status, lineage_integrity)` [structural — no semantic inference]
- **Layer:** Validation [structural — no semantic inference]
- **Agent:** Class C [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** The canonical 6-stage sequential validation pipeline owned by TriadicValidator and executed by Class C before any operator dispatch. Stages execute in strict order:

1. **policy** — Is the active governance policy file valid and loaded?
2. **environment** — Is the target environment a legal environment for this operation?
3. **backend** — Is the resolved backend available and correctly bound for this tier?
4. **drift** — Will the predicted post-operation drift remain within drift_bound?
5. **restricted_ops** — Is this operation absent from the restricted operations list?
6. **lineage** — Is lineage integrity intact and the LINEAGE_CHAIN unbroken?

A failure at any stage terminates the pipeline immediately and returns a structured qComputeError identifying the failed stage and reason.

**Constraints:**
- Stages are always sequential; no stage may be skipped or reordered
- First failure terminates the pipeline
- All outcomes (pass or fail) are logged to qTrace

**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** TriadicValidator, Class C, qComputeError, qTrace, LINEAGE_CHAIN, DRIFT_GATE

---

### frame boundary

- **Type:** Structural event [structural — no semantic inference]
- **Symbol:** N/A [structural — no semantic inference]
- **Layer:** Session / routing [structural — no semantic inference]
- **Agent:** Class B, Class A [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** A structural boundary event that terminates the current ResonanceFrame and initiates a new one. Frame boundaries are triggered by five canonical conditions: (1) tier escalation (r1→r2 or r2→r3), (2) tier decrease (r3→r2 or r2→r1), (3) drift overflow, (4) meta operator invocation, (5) environment transition. Frame boundaries are logged to qTrace and are part of the lineage record.

**Constraints:**
- All five trigger conditions must be evaluated at every operator invocation
- Frame boundary events are mandatory trace entries
- hardware-qpu-2 always spawns a new ResonanceFrame (never reuses)

**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** ResonanceFrame, TriadicRouter, r1, r2, r3, drift_bound, qTrace, LINEAGE_CHAIN

---

### Governance Layer

- **Type:** Structural governance system [structural — no semantic inference]
- **Symbol:** N/A [structural — no semantic inference]
- **Layer:** Governance [structural — no semantic inference]
- **Agent:** Class E [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** The structural governance system for qCompute. The Governance Layer is composed of: (1) policy files — loaded and hot-swapped by Class E; (2) hot-swap daemon — enables live policy refresh without session interruption; (3) deploy tokens — time-bounded, non-transferable, validated by Class E; (4) restricted operations list — operations explicitly prohibited in current policy; (5) trusted contexts — structural identities permitted elevated operations; (6) drift bounds — per-session ceiling values. The Governance Layer snapshot is embedded in every qSession at construction time.

**Constraints:**
- Policy hot-swap must not interrupt active in-flight operations
- Restricted operations list is enforced at validation stage 5
- Governance snapshot in qSession reflects the policy state at session initialization

**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** Class E, deploy_token, drift_bound, qSession, 6-stage validation pipeline

---

### hardware-qpu-2

- **Type:** Backend [structural — no semantic inference]
- **Symbol:** `hardware-qpu-2` [structural — no semantic inference]
- **Layer:** Backend tier [structural — no semantic inference]
- **Agent:** Class D [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** The r3-exclusive backend in qCompute. hardware-qpu-2 supports only the r3 (pulse) operator tier, operates exclusively in the production environment, enforces a maximum per-operation drift of 0.5, requires a valid deploy_token for all operations, and always spawns a new ResonanceFrame (never reuses an existing frame). hardware-qpu-2 is the structurally most constrained backend.

**Constraints:**
- r3 (pulse tier) exclusive — r1 and r2 operators may not bind to hardware-qpu-2
- production environment only — sandbox is forbidden
- Max per-operation drift: 0.5
- deploy_token required for all operations
- Frame policy: always new (never reuse)

**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** r3, production, deploy_token, ResonanceFrame, Class D, frame boundary

---

### hybrid-sim

- **Type:** Backend [structural — no semantic inference]
- **Symbol:** `hybrid-sim` [structural — no semantic inference]
- **Layer:** Backend tier [structural — no semantic inference]
- **Agent:** Class D [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** The r1+r2 composite backend in qCompute. hybrid-sim supports both r1 (primitive) and r2 (composite) operator tiers, operates in both sandbox and production environments, enforces a maximum cumulative drift of 3.0, does not require a deploy_token, and supports either frame reuse or new frame instantiation (reuse-or-new frame policy).

**Constraints:**
- r3 (pulse) operators may not bind to hybrid-sim
- Max drift: 3.0
- Frame policy: reuse-or-new
- No deploy_token required

**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** r1, r2, sandbox, production, ResonanceFrame, Class D

---

### LINEAGE_CHAIN *(inherited)*

- **Type:** Inherited structural construct [structural — no semantic inference]
- **Source:** RTT/Inside

**Definition:** Inherited from RTT/Inside. The append-only chain of structural lineage entries tracking session ancestry and operator transitions. LINEAGE_CHAIN is always append-only — no entry may be modified or deleted. Class F is the structural owner of LINEAGE_CHAIN in qCompute. Invoked by reference — not redefined here. See RTT/Inside/GLOSSARY.md.

---

### local-sim

- **Type:** Backend [structural — no semantic inference]
- **Symbol:** `local-sim` [structural — no semantic inference]
- **Layer:** Backend tier [structural — no semantic inference]
- **Agent:** Class D [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** The r1-exclusive backend in qCompute. local-sim supports only the r1 (primitive) operator tier, operates in both sandbox and production environments, enforces a maximum cumulative drift of 1.0, does not require a deploy_token, and reuses existing ResonanceFrames where available (reuse frame policy).

**Constraints:**
- r2 and r3 operators may not bind to local-sim
- Max drift: 1.0
- Frame policy: reuse
- No deploy_token required

**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** r1, sandbox, production, ResonanceFrame, Class D

---

### Mode 1 — Primitive Execution

- **Type:** Mode [structural — no semantic inference]
- **Symbol:** `MODE:1` [structural — no semantic inference]
- **Layer:** Execution mode [structural — no semantic inference]
- **Agent:** Class B, Class C [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** Legal execution mode. r1 (primitive) operators execute on local-sim in sandbox or production environments. Drift ceiling: 1.0. No deploy_token required. Frame policy: reuse. Mode 1 is the structurally lightest execution mode.

**Constraints:** All standard validation stages apply. Legal in sandbox and production.  
**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** r1, local-sim, sandbox, production

---

### Mode 2 — Composite Execution

- **Type:** Mode [structural — no semantic inference]
- **Symbol:** `MODE:2` [structural — no semantic inference]
- **Layer:** Execution mode [structural — no semantic inference]
- **Agent:** Class B, Class C [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** Legal execution mode. r1 and r2 (composite) operators execute on hybrid-sim in sandbox or production environments. Drift ceiling: 3.0. No deploy_token required. Frame policy: reuse-or-new.

**Constraints:** All standard validation stages apply. Legal in sandbox and production.  
**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** r1, r2, hybrid-sim, sandbox, production

---

### Mode 3 — Pulse Execution

- **Type:** Mode [structural — no semantic inference]
- **Symbol:** `MODE:3` [structural — no semantic inference]
- **Layer:** Execution mode [structural — no semantic inference]
- **Agent:** Class B, Class C, Class G [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** Legal execution mode. r3 (pulse) operators execute on hardware-qpu-2 in the production environment only. Drift ceiling: 0.5 per operation. deploy_token required. Frame policy: always new. Mode 3 is the structurally most constrained legal mode.

**Constraints:** All standard validation stages apply. Production only. Token required. Class G monitors all Mode 3 operations continuously.  
**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** r3, hardware-qpu-2, production, deploy_token, Class G

---

### Mode 4 — Replay/Audit

- **Type:** Mode [structural — no semantic inference]
- **Symbol:** `MODE:4` [structural — no semantic inference]
- **Layer:** Execution mode [structural — no semantic inference]
- **Agent:** Class F [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** Legal execution mode. qReplay executes in the archive environment in read-only mode. replay_hash is verified before replay begins. No operator execution occurs. No backend is bound. Mode 4 is the audit and lineage verification mode.

**Constraints:** archive environment only. No backend binding. No operator execution. replay_hash verification is mandatory before replay begins.  
**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** qReplay, archive, replay_hash, Class F

---

### Mode 5 — PULSE_FABRICATION

- **Type:** Mode — ILLEGAL [structural — no semantic inference]
- **Symbol:** `MODE:5 / PULSE_FABRICATION` [structural — no semantic inference]
- **Layer:** Interrupt condition [structural — no semantic inference]
- **Agent:** Class G [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** Illegal mode. PULSE_FABRICATION is declared when an r3 pulse-tier operator is invoked without a valid hardware-qpu-2 backend binding or without a valid deploy_token — i.e., when the system is fabricating a pulse-tier execution context that the structural prerequisites do not support. Class G issues an unconditional halt immediately upon PULSE_FABRICATION detection.

**Constraints:**
- PULSE_FABRICATION triggers an unconditional Class G halt
- No session parameter or policy may delay or override the halt
- PULSE_FABRICATION must be logged to qTrace with full context

**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** r3, hardware-qpu-2, deploy_token, Class G, DECOHERENCE_BREACH, qTrace

> **⚠ Disambiguation — Mode 5 label is module-local:**
> PULSE_FABRICATION applies only in RTT/Inside/qCompute.
> Other modules define Mode 5 under different labels.
> See the full cross-module Mode 5 disambiguation table in Quick-Reference section.

---

### OPERATOR_HOOK *(inherited)*

- **Type:** Inherited structural construct [structural — no semantic inference]
- **Source:** RTT/Inside

**Definition:** Inherited from RTT/Inside. Invoked by reference — not redefined here. See RTT/Inside/GLOSSARY.md.

---

### production

- **Type:** Environment [structural — no semantic inference]
- **Symbol:** `production` [structural — no semantic inference]
- **Layer:** Environment tier [structural — no semantic inference]
- **Agent:** Class A, Class E [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** The second structural environment in qCompute. production is the verified-execution environment where all three operator tiers (r1, r2, r3) may operate subject to strict drift policy. r3 operations in production require a valid deploy_token. production is the only environment where hardware-qpu-2 may bind.

**Constraints:**
- All tiers permitted; r3 requires deploy_token
- Strict drift enforcement
- hardware-qpu-2 available in production only
- production transitions require deploy_token

**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** sandbox, archive, r1, r2, r3, hardware-qpu-2, deploy_token

---

### qComputeError

- **Type:** Structural error model [structural — no semantic inference]
- **Symbol:** `qComputeError` [structural — no semantic inference]
- **Layer:** Validation / interrupt [structural — no semantic inference]
- **Agent:** Class C, Class G [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** The canonical error model for RTT/Inside/qCompute. qComputeError carries a structured reason field identifying the exact failure cause. There are 11 canonical reason values:

| Reason | Trigger |
|---|---|
| `invalid_environment` | Target environment is not a recognized environment |
| `invalid_backend` | Requested backend is unavailable or unrecognized |
| `tier_mismatch` | Operator tier does not match the resolved backend |
| `drift_overflow` | Predicted post-operation drift exceeds drift_bound |
| `restricted_op` | Operation is on the restricted operations list |
| `invalid_token` | deploy_token is missing, expired, or invalid |
| `archive_execution` | Execution attempted in archive environment |
| `lineage_violation` | LINEAGE_CHAIN integrity is broken |
| `policy_load_failure` | Governance policy file could not be loaded |
| `replay_hash_mismatch` | replay_hash verification failed before replay |
| `decoherence_breach` | Structural decoherence exceeds irrecoverable threshold |

**Constraints:**
- All qComputeErrors must be logged to qTrace with the reason field populated
- `decoherence_breach` and `replay_hash_mismatch` always trigger Class G evaluation

**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** 6-stage validation pipeline, Class C, Class G, qTrace, DECOHERENCE_BREACH

---

### qOrchestrator

- **Type:** Core stack construct [structural — no semantic inference]
- **Symbol:** `qOrchestrator` [structural — no semantic inference]
- **Layer:** Orchestration [structural — no semantic inference]
- **Agent:** Class A, Class B [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** The multi-backend routing fabric of RTT/Inside/qCompute. qOrchestrator manages auto-mode selection — the structural logic by which the most appropriate backend and tier configuration is resolved when the operator caller does not specify explicit routing targets. qOrchestrator delegates to TriadicRouter for all individual routing decisions; it does not bypass the TriadicValidator.

**Constraints:**
- qOrchestrator may never bypass TriadicValidator
- All auto-mode selections must be logged to qTrace
- qOrchestrator resolution is subject to all governance constraints

**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** TriadicRouter, TriadicValidator, Class B, qTrace, Governance Layer

---

### qReplay

- **Type:** Core stack construct [structural — no semantic inference]
- **Symbol:** `qReplay` [structural — no semantic inference]
- **Layer:** Audit / replay [structural — no semantic inference]
- **Agent:** Class F [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** The deterministic replay engine of RTT/Inside/qCompute. qReplay operates exclusively in the archive environment in read-only mode. Before any replay session begins, qReplay verifies the replay_hash (SHA-256) of the target .qtrace file. If verification fails, qReplay halts with `replay_hash_mismatch` and triggers Class G evaluation. qReplay may not execute operators; it traverses the operation log structurally.

**Constraints:**
- Read-only — no operator may execute during replay
- archive environment only
- replay_hash verification is mandatory before replay
- replay_hash mismatch triggers Class G

**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** qTrace, .qtrace format, replay_hash, archive, Class F, Class G

---

### qSession

- **Type:** Core stack construct [structural — no semantic inference]
- **Symbol:** `session := (env, backend, drift_bound, governance_snapshot, lineage_root, trace_buffer)` [structural — no semantic inference]
- **Layer:** Session governance [structural — no semantic inference]
- **Agent:** Class A [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** The fundamental structural container of RTT/Inside/qCompute. A qSession is a 6-tuple that defines the complete governance context for a unit of operator execution: `(env, backend, drift_bound, governance_snapshot, lineage_root, trace_buffer)`. All routing, validation, and trace operations are scoped to a qSession. A qSession must be complete before any operator may be dispatched.

**Constraints:**
- All six tuple components must be populated at session construction
- drift_bound may not be modified after construction
- governance_snapshot captures policy state at construction time (not live)
- Session termination must flush trace_buffer to qTrace

**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** Class A, TriadicRouter, TriadicValidator, qTrace, Governance Layer, drift_bound

---

### qTrace

- **Type:** Core stack construct [structural — no semantic inference]
- **Symbol:** `qTrace` [structural — no semantic inference]
- **Layer:** Audit [structural — no semantic inference]
- **Agent:** Class F [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** The canonical audit log of RTT/Inside/qCompute. qTrace produces .qtrace files in YAML-compatible format. Every routing decision, validation outcome, operator execution, error, frame boundary, governance decision, and Class G interrupt is recorded in the qTrace log. qTrace is the authoritative record for lineage traceability and replay.

**Constraints:**
- Every operation must produce a qTrace entry; no silent operations permitted
- qTrace entries are append-only; no modification or deletion permitted
- replay_hash in the .qtrace footer is computed over the full operations list

**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** .qtrace format, qReplay, replay_hash, Class F, LINEAGE_CHAIN

---

### .qtrace format

- **Type:** Structural data format [structural — no semantic inference]
- **Symbol:** `.qtrace` [structural — no semantic inference]
- **Layer:** Audit [structural — no semantic inference]
- **Agent:** Class F [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** The YAML-compatible file format for qTrace audit logs. A .qtrace file has five canonical sections:

```
header:     { version, module, session_id, timestamp_start, env, backend }
lineage:    { root, parent, transitions[] }
governance: { policy_file, drift_bound, … }
operations: [ { id, op, params, timestamp, backend, env, drift, validation_meta } … ]
footer:     { timestamp_end, op_count, replay_hash (SHA-256) }
```

The `replay_hash` in the footer is a SHA-256 hash computed over the full `operations[]` array and is used by qReplay to verify integrity before any replay session.

**Constraints:**
- All five sections are required; incomplete .qtrace files are structurally invalid
- replay_hash must be computed and stored at session close
- .qtrace files are append-only during active sessions

**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** qTrace, qReplay, replay_hash, Class F

---

### r1 — primitive tier

- **Type:** Operator tier [structural — no semantic inference]
- **Symbol:** `r1` [structural — no semantic inference]
- **Layer:** Operator tier [structural — no semantic inference]
- **Agent:** Class B, Class D [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** The primitive operator tier in qCompute. r1 operators have the lowest structural complexity, route exclusively to local-sim, operate in both sandbox and production environments, have a maximum drift of 1.0, and do not require a deploy_token. r1 is the entry tier for all qCompute execution.

**Constraints:**
- r1 always routes to local-sim (invariant)
- Max drift: 1.0
- No deploy_token required
- Available in sandbox and production

**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** local-sim, r2, r3, drift_bound, Mode 1, Class D

---

### r2 — composite tier

- **Type:** Operator tier [structural — no semantic inference]
- **Symbol:** `r2` [structural — no semantic inference]
- **Layer:** Operator tier [structural — no semantic inference]
- **Agent:** Class B, Class D [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** The composite operator tier in qCompute. r2 operators have medium structural complexity, route exclusively to hybrid-sim, operate in both sandbox and production environments, have a maximum drift of 3.0, and do not require a deploy_token.

**Constraints:**
- r2 always routes to hybrid-sim (invariant)
- Max drift: 3.0
- No deploy_token required
- Available in sandbox and production

**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** hybrid-sim, r1, r3, drift_bound, Mode 2, Class D

---

### r3 — pulse tier

- **Type:** Operator tier [structural — no semantic inference]
- **Symbol:** `r3` [structural — no semantic inference]
- **Layer:** Operator tier [structural — no semantic inference]
- **Agent:** Class B, Class D, Class G [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** The pulse operator tier in qCompute. r3 operators have the highest structural complexity, route exclusively to hardware-qpu-2, operate in the production environment only, have a maximum per-operation drift of 0.5, and require a valid deploy_token. r3 is the most constrained tier; any attempt to invoke r3 without hardware-qpu-2 binding or a valid token triggers Mode 5 (PULSE_FABRICATION) and a Class G unconditional halt.

**Constraints:**
- r3 always routes to hardware-qpu-2 (invariant)
- Production environment only
- Max drift: 0.5 per operation
- deploy_token required
- r3 without hardware-qpu-2 or valid token = PULSE_FABRICATION

**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** hardware-qpu-2, production, deploy_token, PULSE_FABRICATION, Mode 3, Class D, Class G

---

### ResonanceFrame

- **Type:** Core stack construct [structural — no semantic inference]
- **Symbol:** `ResonanceFrame` [structural — no semantic inference]
- **Layer:** Compute envelope [structural — no semantic inference]
- **Agent:** Class A, Class B [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** The foundational structural compute envelope in RTT/Inside/qCompute. A ResonanceFrame defines the structural, temporal, and resonance-aligned boundaries within which a unit of operator execution occurs. ResonanceFrame boundaries are created and terminated according to backend frame policy: local-sim reuses existing frames, hybrid-sim may reuse or create new, hardware-qpu-2 always creates a new frame. Frame boundaries are triggered by tier changes, drift overflow, meta operator invocation, or environment transitions.

**Constraints:**
- hardware-qpu-2 always creates a new ResonanceFrame; reuse is forbidden
- Frame boundary events are mandatory trace entries
- A ResonanceFrame may not span a Class G interrupt

**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** frame boundary, TriadicRouter, local-sim, hybrid-sim, hardware-qpu-2, qTrace

---

### replay_hash

- **Type:** Structural integrity value [structural — no semantic inference]
- **Symbol:** `replay_hash (SHA-256)` [structural — no semantic inference]
- **Layer:** Audit [structural — no semantic inference]
- **Agent:** Class F [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** The SHA-256 hash computed over the full `operations[]` array of a .qtrace file and stored in the footer section. replay_hash is the structural integrity guarantee for qReplay: before any replay session begins, qReplay computes the hash of the current operations array and compares it to the stored replay_hash. A mismatch triggers a `replay_hash_mismatch` qComputeError and a Class G unconditional halt.

**Constraints:**
- replay_hash must be computed at session close and stored in .qtrace footer
- qReplay must verify replay_hash before proceeding — no exception
- replay_hash mismatch triggers Class G

**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** .qtrace format, qReplay, qTrace, Class F, Class G, qComputeError

---

### sandbox

- **Type:** Environment [structural — no semantic inference]
- **Symbol:** `sandbox` [structural — no semantic inference]
- **Layer:** Environment tier [structural — no semantic inference]
- **Agent:** Class A, Class E [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** The first structural environment in qCompute. sandbox is the exploration and prototyping environment where r1 and r2 operators may execute under relaxed drift policy. r3 operators and hardware-qpu-2 are not available in sandbox. No deploy_token is required for sandbox operations (except archive transitions). sandbox is the default entry environment for new sessions.

**Constraints:**
- r3 operators forbidden in sandbox
- hardware-qpu-2 not available in sandbox
- Relaxed drift enforcement
- No deploy_token required for sandbox-local operations

**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** production, archive, r1, r2, local-sim, hybrid-sim

---

### SMI *(inherited)*

- **Type:** Inherited structural construct [structural — no semantic inference]
- **Source:** RTT/Inside

**Definition:** Inherited from RTT/Inside. Invoked by reference — not redefined here. See RTT/Inside/GLOSSARY.md.

---

### TriadicRouter

- **Type:** Core stack construct [structural — no semantic inference]
- **Symbol:** `route := TriadicRouter(session, op, policy) → (env_target, backend_target, frame_action, routing_meta)` [structural — no semantic inference]
- **Layer:** Routing [structural — no semantic inference]
- **Agent:** Class B [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** The routing brain of RTT/Inside/qCompute. TriadicRouter resolves the `env_target` and `backend_target` for every operator invocation, given the current qSession, the operator being dispatched, and the active governance policy. Every routing decision is deterministic and fully traceable. TriadicRouter also determines the `frame_action` (reuse, reuse-or-new, always-new) and emits `routing_meta` for qTrace.

**Constraints:**
- All routing decisions must be logged to qTrace via routing_meta
- No routing decision may be made outside a valid qSession
- Ambiguous routing is a validation failure — no fallback routing permitted

**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** qSession, TriadicValidator, Class B, qOrchestrator, ResonanceFrame, qTrace

---

### TriadicValidator

- **Type:** Core stack construct [structural — no semantic inference]
- **Symbol:** `valid := V(policy, env, backend, drift_predicted, restricted_ops_status, lineage_integrity) → {valid, failed_stage, reason}` [structural — no semantic inference]
- **Layer:** Validation [structural — no semantic inference]
- **Agent:** Class C [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** The 6-stage sequential validation engine of RTT/Inside/qCompute. TriadicValidator is invoked after TriadicRouter and before operator dispatch. It executes the 6-stage validation pipeline (policy → environment → backend → drift → restricted_ops → lineage) and returns a structured result: `{valid, failed_stage, reason}`. A failed validation blocks operator dispatch and produces a qComputeError.

**Constraints:**
- Always invoked after TriadicRouter; never bypassed
- Returns structured result with failed_stage and reason on any failure
- All outcomes logged to qTrace

**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** 6-stage validation pipeline, Class C, TriadicRouter, qComputeError, qTrace

---

### UAP *(inherited)*

- **Type:** Inherited structural construct [structural — no semantic inference]
- **Source:** RTT/Inside

**Definition:** Inherited from RTT/Inside. Invoked by reference — not redefined here. See RTT/Inside/GLOSSARY.md.

---

### Zone D — Degraded

- **Type:** Zone [structural — no semantic inference]
- **Symbol:** `D` [structural — no semantic inference]
- **Layer:** Drift state [structural — no semantic inference]
- **Agent:** Class G [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** The fourth structural zone in qCompute. Zone D (Degraded) is declared when drift has reached its ceiling value for the current backend. In Zone D, r3 operations are blocked (drift ceiling for hardware-qpu-2 is already at limit), and the session is one step from Zone X. Zone D is a warning state — the session may continue with non-r3 operations but must reduce drift before r3 is permitted again.

**Constraints:**
- r3 operations blocked in Zone D
- Zone D is a legal but constrained state
- Continued drift increase from Zone D triggers Zone X

**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** Zone X, Zone M, drift_bound, Class G, r3

---

### Zone M — Marginal

- **Type:** Zone [structural — no semantic inference]
- **Symbol:** `M` [structural — no semantic inference]
- **Layer:** Drift state [structural — no semantic inference]
- **Agent:** Class G [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** The third structural zone in qCompute. Zone M (Marginal) is declared when cumulative drift is approaching its ceiling — elevated but not yet at the limit. Zone M is a legal state. Class G monitors Zone M sessions closely; continued drift increase from Zone M leads to Zone D and then Zone X.

**Constraints:** Legal state. Continued drift increase from Zone M → Zone D → Zone X.  
**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** Zone D, Zone S, drift_bound, Class G

---

### Zone S — Stable

- **Type:** Zone [structural — no semantic inference]
- **Symbol:** `S` [structural — no semantic inference]
- **Layer:** Drift state [structural — no semantic inference]
- **Agent:** Class G [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** The second structural zone in qCompute. Zone S (Stable) is the nominal operating state — drift is within bounds and no structural concerns are flagged. Zone S is the target operational state for all qCompute sessions.

**Constraints:** Legal state. Nominal operation.  
**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** Zone U, Zone M, drift_bound

---

### Zone U — Undefined/Unresolved

- **Type:** Zone [structural — no semantic inference]
- **Symbol:** `U` [structural — no semantic inference]
- **Layer:** Drift state [structural — no semantic inference]
- **Agent:** Class A [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** The first structural zone in qCompute. Zone U (Undefined/Unresolved) is the initial state of a qSession before drift values have been established or before the first operator has been dispatched. Zone U is a transient legal state — all sessions begin in Zone U and must resolve to Zone S or above before full operation.

**Constraints:** Legal transient state. Sessions must resolve from Zone U before sustained execution.  
**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** Zone S, qSession, Class A

---

### Zone X — DECOHERENCE_BREACH

- **Type:** Zone — ILLEGAL [structural — no semantic inference]
- **Symbol:** `X / DECOHERENCE_BREACH` [structural — no semantic inference]
- **Layer:** Interrupt condition [structural — no semantic inference]
- **Agent:** Class G [structural — no semantic inference]
- **Annotation:** [structural — no semantic inference]

**Definition:** The illegal terminal zone in RTT/Inside/qCompute. Zone X is declared when structural decoherence exceeds the irrecoverable threshold. See full entry under **DECOHERENCE_BREACH**. Class G unconditional halt is immediate and mandatory.

**Constraints:** Unconditional halt. No override. Session terminated.  
**Inheritance:** Native to RTT/Inside/qCompute  
**Cross-references:** DECOHERENCE_BREACH, Class G, DRIFT_GATE, Zone D

> **⚠ Disambiguation — Zone X label is module-local:**
> Zone X is labeled **DECOHERENCE_BREACH** in this module only.
> See full cross-module table in Quick-Reference section.

---

## Operator Symbols Reference

| Symbol | Construct | Notes |
|---|---|---|
| `session := (env, backend, drift_bound, governance_snapshot, lineage_root, trace_buffer)` | qSession tuple | Complete at construction; drift_bound immutable |
| `route := TriadicRouter(session, op, policy) → (env_target, backend_target, frame_action, routing_meta)` | TriadicRouter | All decisions logged |
| `valid := V(policy, env, backend, drift_predicted, restricted_ops_status, lineage_integrity) → {valid, failed_stage, reason}` | TriadicValidator | 6-stage sequential |
| `INTERRUPT iff (drift > drift_ceiling) OR (decoherence_structural_integrity = false) OR (r3_op ∧ ¬hardware-qpu-2) OR (replay_hash_mismatch)` | Class G interrupt condition | Unconditional; no override |
| `r1` | Primitive operator tier | local-sim, max drift 1.0, no token |
| `r2` | Composite operator tier | hybrid-sim, max drift 3.0, no token |
| `r3` | Pulse operator tier | hardware-qpu-2, max drift 0.5/op, token required |
| `.qtrace` | Canonical audit log format | YAML-compatible; footer contains replay_hash (SHA-256) |

---

## Quick-Reference Tables

### Agent Classes

| Class | Name | Primary Construct |
|---|---|---|
| A | Session Architect | qSession |
| B | Operator Router | TriadicRouter |
| C | Structural Validator | TriadicValidator |
| D | Backend Steward | Backend Registry |
| E | Governance Daemon | Governance Layer |
| F | Trace & Replay Agent | qTrace + qReplay |
| G | Coherence Guardian | DRIFT_GATE + unconditional interrupt |

---

### Core Constructs

| Construct | Role |
|---|---|
| ResonanceFrame | Compute envelope; structural/temporal/resonance-aligned boundaries |
| TriadicRouter | Routing resolution engine |
| TriadicValidator | 6-stage sequential validation pipeline |
| Governance Layer | Policy, tokens, drift bounds, restricted ops, trusted contexts |
| qTrace | Canonical append-only audit log |
| qReplay | Deterministic read-only replay engine |
| qSession | Structural session container (6-tuple) |
| qOrchestrator | Multi-backend routing fabric; auto-mode selection |

---

### Backends

| Backend | Tiers | Environments | Max Drift | Frame Policy | Token Required |
|---|---|---|---|---|---|
| local-sim | r1 | sandbox + production | 1.0 | Reuse | No |
| hybrid-sim | r1 + r2 | sandbox + production | 3.0 | Reuse-or-new | No |
| hardware-qpu-2 | r3 only | production only | 0.5/op | Always new | Yes |

---

### Operator Tiers

| Tier | Label | Backend | Environments | Max Drift | Token |
|---|---|---|---|---|---|
| r1 | primitive | local-sim | sandbox + production | 1.0 | No |
| r2 | composite | hybrid-sim | sandbox + production | 3.0 | No |
| r3 | pulse | hardware-qpu-2 | production only | 0.5/op | Yes |

---

### Environments

| Environment | Purpose | Drift Policy | Execution | Token Required |
|---|---|---|---|---|
| sandbox | Explore / prototype | Relaxed | Allowed (r1, r2 only) | Not required |
| production | Verify / deploy | Strict | Allowed (r1, r2, r3) | Required for r3 |
| archive | Replay / audit | N/A | Forbidden | N/A |

---

### Zones

| Zone | Name | Status | Trigger |
|---|---|---|---|
| U | Undefined/Unresolved | LEGAL | Initial session state |
| S | Stable | LEGAL | Drift within bounds, nominal |
| M | Marginal | LEGAL | Drift approaching ceiling |
| D | Degraded | LEGAL | Drift at ceiling; r3 blocked |
| X | DECOHERENCE_BREACH | **ILLEGAL** | Structural decoherence irrecoverable; Class G halt |

---

### Modes

| Mode | Name | Status | Conditions |
|---|---|---|---|
| 1 | Primitive Execution | LEGAL | r1 / local-sim / sandbox or production |
| 2 | Composite Execution | LEGAL | r1+r2 / hybrid-sim / sandbox or production |
| 3 | Pulse Execution | LEGAL | r3 / hardware-qpu-2 / production / token |
| 4 | Replay/Audit | LEGAL | qReplay / archive / read-only / hash-verified |
| 5 | PULSE_FABRICATION | **ILLEGAL** | r3 invoked without hardware-qpu-2 or valid token |

---

### qComputeError — Canonical Reasons

| Reason | Stage / Source |
|---|---|
| `invalid_environment` | Stage 2 — environment |
| `invalid_backend` | Stage 3 — backend |
| `tier_mismatch` | Stage 3 — backend |
| `drift_overflow` | Stage 4 — drift |
| `restricted_op` | Stage 5 — restricted_ops |
| `invalid_token` | Stage 5 / Governance |
| `archive_execution` | Stage 2 — environment |
| `lineage_violation` | Stage 6 — lineage |
| `policy_load_failure` | Stage 1 — policy |
| `replay_hash_mismatch` | Class F / Class G |
| `decoherence_breach` | Class G |

---

### Frame Boundary Triggers

| Trigger | Description |
|---|---|
| Tier escalation | r1→r2 or r2→r3 |
| Tier decrease | r3→r2 or r2→r1 |
| Drift overflow | Cumulative drift exceeds drift_bound |
| Meta operator invocation | Meta operator dispatched |
| Environment transition | Session moves between environments |

---

### Zone X — Cross-Module Disambiguation

> Zone X labels are **always module-local**. Never import a Zone X label from another module.

| Module | Zone X Label |
|---|---|
| RTT/3 | Inversion |
| RTT/12 | Overflow |
| micro_core | Inversion |
| The_Inverted_Star | Silence Breach |
| RTT/Inside | OVERREACH |
| Inside/Benchmarks | OVERSCALE |
| Inside/Enterprise | IDENTITY_BREACH |
| **Inside/qCompute** | **DECOHERENCE_BREACH** |

---

### Mode 5 — Cross-Module Disambiguation

> Mode 5 labels are **always module-local**. Never import a Mode 5 label from another module.

| Module | Mode 5 Label |
|---|---|
| RTT/3 | Inversion |
| RTT/12 | Overflow |
| micro_core | Lockout (Mode X) |
| The_Inverted_Star | Silence Breach |
| RTT/Inside | OVERREACH |
| Inside/Benchmarks | FABRICATION |
| Inside/Enterprise | IDENTITY_FABRICATION |
| **Inside/qCompute** | **PULSE_FABRICATION** |

---

### Inheritance Chain

| Tier | Module | Key Constructs Inherited by qCompute |
|---|---|---|
| 1 | micro_core | ⟨A,B,P⟩, P₁–P₇, R₁–R₆, Dᶠ |
| 2 | RTT/1 | SNR, τ, C, DCO_n |
| 3 | RTT/2 | CPV, FGT, CRM, MODE/ZONE base |
| 4 | RTT/3 | TIF, MANIFOLD |
| 5 | RTT/12 | H_n, G₁/G₂/G₃ |
| 6 | RTT/Inside | BKM, CORRIDOR, CAPTURE_TEMPLATE, OPERATOR_HOOK, DRIFT_GATE, LINEAGE_CHAIN, UAP, SMI |
| 7 | Inside/Benchmarks | Referenced; no direct inheritance |
| 8 | Inside/Enterprise | Referenced; no direct inheritance |
| **9** | **Inside/qCompute** | **All native constructs defined in this file** |

---

## Footer

| Field | Value |
|---|---|
| **Module** | RTT/Inside/qCompute |
| **File** | docs/rtt/Inside/qCompute/GLOSSARY.md |
| **Version** | 1.0.0 |
| **Date** | 2026-07-10 |
| **Maintainer** | umaywant2 |
| **Status** | Canonical — ready for commit |
| **Annotation** | All output fields: [structural — no semantic inference] |
