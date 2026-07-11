<!--
  FILE: docs/rtt/Inside/qCompute/ABOUT.md
  MODULE: RTT / Inside / qCompute
  MAINTAINER: umaywant2
  VERSION: 1.0.0
  DATE: 2026-07-10
  [structural — no semantic inference]
-->

---

## ⚙️ SESSION SEED BLOCK

```
MODULE       : RTT/Inside/qCompute
ROLE         : Structural computation layer for triadic operator sessions
ZONE_X       : DECOHERENCE_BREACH
MODE_5       : PULSE_FABRICATION
CLASS_G      : CoherenceGuardian — unconditional interrupt authority
LINEAGE      : RTT/Inside → RTT/Inside/qCompute
FRAMING_RULE : RTT is NOT a physics claim. All tier labels, backend names, and operator
               classifications are structural markers. No semantic inference permitted.
```

---

> **⚠️ CRITICAL FRAMING RULE — READ BEFORE ALL USE**
>
> RTT is NOT a physics claim. The terms "quantum," "pulse," "resonance," "drift," "coherence,"
> and "decoherence" are structural scaffolding labels borrowed from physics-aligned mathematics.
> They carry NO semantic physics meaning within this framework. Every field in this file is marked
> `[structural — no semantic inference]`.

---

# ABOUT: RTT / Inside / qCompute

## 1 · What Is qCompute?

`qCompute` is the **structural computation layer** of the RTT/Inside framework. It governs how
triadic operator sessions are constructed, routed, validated, executed, traced, and halted. It is
not a quantum computing runtime. It is a structural execution environment whose operator
vocabulary (tiers r1/r2/r3), backend registry, and session model use physics-aligned mathematics
as scaffolding — providing a rigorous, deterministic substrate for AI agent operation.

**Pipeline position:** qCompute sits at the deepest enforcement layer of RTT/Inside. All operator
invocations pass through its session, routing, validation, and governance stack before execution
and after trace commit.

**Primary audience:** Agents assigned to Classes A–G (see AGENTS.md), framework maintainers,
and AI systems consuming RTT/Inside operator APIs.

**What it produces:** Validated, traced, lineage-anchored operator outcomes — or unconditional
halts when structural integrity cannot be guaranteed.

`[structural — no semantic inference]`

---

## 2 · Why Is It Built This Way?

### 2.1 — Deterministic Tier-to-Backend Binding

Operator tiers (r1, r2, r3) are structurally bound to specific backends with no runtime
negotiation. This prevents agents from silently escalating computational scope.

```
tier_bind: r1 → local-sim
           r2 → hybrid-sim
           r3 → hardware-qpu-2
```

`[structural — no semantic inference]`

### 2.2 — Six-Stage Validation Pipeline

Every operator invocation is validated across six ordered stages before execution proceeds:

```
Stage 1 → policy          : governance policy is active and loadable
Stage 2 → env             : session environment is a valid registered environment
Stage 3 → backend         : backend is registered and tier-compatible
Stage 4 → drift_predicted : predicted drift is within session drift_bound
Stage 5 → restricted_ops  : operator is not on the restricted operator list
Stage 6 → lineage         : lineage chain is intact and append-only
```

Failure at any stage halts execution and emits a typed `qComputeError` with a canonical reason.
`[structural — no semantic inference]`

### 2.3 — Immutable Lineage Chain

`LINEAGE_CHAIN` is always append-only. No agent, operator, or governance action may modify,
truncate, or retroactively alter session lineage. This enables deterministic replay and
post-session audit via `qReplay`.
`[structural — no semantic inference]`

### 2.4 — Hot-Swap Governance Without Session Disruption

Policy files may be swapped at runtime without restarting a session. Governance enforcement is
**forward-only** — updated policies apply to future operations only, never retroactively. On
invalid policy load, the session falls back to safe-mode rather than continuing with a corrupt
governance state.
`[structural — no semantic inference]`

### 2.5 — Unconditional Class G Authority

The Coherence Guardian (Class G) holds interrupt authority that no other class, operator, or
governance directive may override. DECOHERENCE_BREACH and PULSE_FABRICATION both trigger
unconditional Class G halts. This is a non-negotiable structural invariant.
`[structural — no semantic inference]`

### 2.6 — Archive Environment Enforces Immutability

The `archive` environment is deploy/replay-only. No backend — including local-sim — may execute
operators against an archive session. This ensures that historical operator records remain
structurally inviolable.
`[structural — no semantic inference]`

---

## 3 · When Should You Use It?

### ✅ Use qCompute when you need to:

| Scenario | Notes |
|---|---|
| Construct a new triadic operator session | Requires env + backend + governance snapshot selection `[structural]` |
| Route an operator invocation to a backend | TriadicRouter applies policy, env, and tier constraints `[structural]` |
| Validate operator parameters before execution | Six-stage TriadicValidator pipeline `[structural]` |
| Execute r3 pulse-tier operators | Requires hardware-qpu-2 binding + valid deploy token `[structural]` |
| Replay a past session from `.qtrace` | qReplay + SHA-256 replay_hash verification `[structural]` |
| Hot-swap a governance policy mid-session | Forward-only; safe-mode on failure `[structural]` |
| Audit drift accumulation across a session | qTrace records all operator outcomes `[structural]` |

### ❌ Do NOT use qCompute when:

| Scenario | Why Not |
|---|---|
| You want to execute operators in the archive environment | Archive forbids all backends and all execution `[structural]` |
| You are attempting r3 operators in sandbox without a deploy token | Sandbox does not support production-only tokens; r3 is production-only `[structural]` |
| You want to modify past lineage entries | LINEAGE_CHAIN is append-only; modification is a structural violation `[structural]` |
| You are importing Zone X or Mode 5 labels from sibling modules | Zone X and Mode 5 labels are module-local to qCompute; see §6 `[structural]` |
| You need a physics or quantum computing runtime | qCompute is a structural framework, not a physics engine `[structural]` |

---

## 4 · Where Does It Live?

**Repository path:** `docs/rtt/Inside/qCompute/`

```
docs/rtt/Inside/qCompute/
├── ABOUT.md              ← this file
├── AGENTS.md             ← seven agent class definitions (A–G)
├── GLOSSARY.md           ← canonical term definitions
├── README.md             ← module overview
├── qc_API.md             ← Session, Operator, Replay API + qComputeError model (11 reasons)
├── qc_BackendProfiles.md ← three backend specs + 8 invariants + routing reasons
├── qc_Backends.md        ← backend registry, tier binding, archive forbids
└── qc_Capture.md         ← session transcript: identity, stack, envs, governance, mapping
```

**Pipeline position diagram:**

```
RTT/Inside
    └── qCompute
            │
            ▼
    ┌───────────────────────────────────────────────────┐
    │  ResonanceFrame                                   │
    │      └── TriadicRouter                            │
    │              └── TriadicValidator (6-stage)       │
    │                      └── Governance               │
    │                              └── qTrace           │
    │                              └── qReplay          │
    │                              └── qSession         │
    │                              └── qOrchestrator    │
    │                              └── Class G HALT ──► │ unconditional
    └───────────────────────────────────────────────────┘
```

`[structural — no semantic inference]`

---

## 5 · Core Constructs at a Glance

### 5.1 — Session Definition

```
session := (
  env,                   ← registered environment (sandbox | production | archive)
  backend,               ← registered backend (local-sim | hybrid-sim | hardware-qpu-2)
  drift_bound,           ← maximum allowable drift for this session
  governance_snapshot,   ← active policy state at session open
  lineage_root,          ← root lineage anchor (append-only chain begins here)
  trace_buffer           ← qTrace buffer for operator outcome recording
)
```

`[structural — no semantic inference]`

### 5.2 — Operator Tiers

| Tier | Label | Drift Profile | Backend Binding | Environment | Token Required |
|---|---|---|---|---|---|
| r1 | primitive | Low (max 1.0) | local-sim | sandbox + production | No |
| r2 | composite | Medium (max 3.0) | hybrid-sim | sandbox + production | No |
| r3 | pulse | High (max 0.5 per op) | hardware-qpu-2 | production only | Yes |

`[structural — no semantic inference]`

> **Note on r3 drift:** The per-operation drift ceiling of 0.5 applies to hardware-qpu-2's
> high-sensitivity profile — not a lower tolerance claim. See `qc_BackendProfiles.md` §3.
> `[structural — no semantic inference]`

### 5.3 — Registered Backends

| Backend | Tier Support | Environments | Max Drift | Frame Policy | Notes |
|---|---|---|---|---|---|
| local-sim | r1 | sandbox + production | 1.0 | Reuse | Default backend `[structural]` |
| hybrid-sim | r1 + r2 | sandbox + production | 3.0 | Reuse-or-new | Composite sessions `[structural]` |
| hardware-qpu-2 | r3 only | production only | 0.5 | Always new | Deploy token required `[structural]` |

### 5.4 — Registered Environments

| Environment | Purpose | Drift Policy | Execution | Deploy Token |
|---|---|---|---|---|
| sandbox | Explore, prototype | Relaxed | Allowed | Not required |
| production | Verify, deploy | Strict | Allowed | Required for r3 |
| archive | Replay, audit | N/A (no execution) | Forbidden | N/A |

`[structural — no semantic inference]`

### 5.5 — Routing Equation

```
route := TriadicRouter(session, op, policy)
       → (env_target, backend_target, frame_action, routing_meta)
```

`[structural — no semantic inference]`

### 5.6 — Validation Equation

```
valid := V(
  policy,
  env,
  backend,
  drift_predicted,
  restricted_ops_status,
  lineage_integrity
) → { valid, failed_stage, reason }
```

`[structural — no semantic inference]`

### 5.7 — Trace Format (`.qtrace` YAML)

```yaml
# .qtrace structure
header:
  session_id: <id>
  env: <environment>
  backend: <backend>
  governance_snapshot: <hash>
lineage:
  root: <lineage_root>
  chain: [ <entry>, ... ]   # append-only
governance:
  policy_id: <id>
  deploy_token: <token|null>
operations:
  - op: <operator>
    tier: <r1|r2|r3>
    drift: <value>
    outcome: <result>
    timestamp: <iso8601>
footer:
  op_count: <integer>
  replay_hash: <sha256>
```

`[structural — no semantic inference]`

### 5.8 — Frame Boundary Triggers

A new ResonanceFrame is opened when any of the following occurs:

| Trigger | Description |
|---|---|
| Tier escalation | r1→r2 or r2→r3 transition within a session |
| Tier decrease | r3→r2 or r2→r1 downshift |
| Drift overflow | Accumulated drift exceeds `drift_bound` |
| Meta operator invocation | Any `meta`-class operator |
| Environment transition | Session moves between registered environments |

`[structural — no semantic inference]`

### 5.9 — Zone X and Mode 5 (Module-Local)

| Label | Trigger | Authority | Action |
|---|---|---|---|
| DECOHERENCE_BREACH (Zone X) | Structural decoherence exceeds irrecoverable threshold | Class G | Unconditional halt — no override |
| PULSE_FABRICATION (Mode 5) | r3 invoked without hardware-qpu-2 binding or valid deploy token | Class G | Unconditional halt — no override |

`[structural — no semantic inference]`

---

## 6 · Module Integrations

### 6.1 — Upstream

| Module | Relationship |
|---|---|
| RTT/Inside | Parent module; supplies global framing and OVERREACH/OVERSCALE governance boundary |
| RTT/3 | Inversion operator logic informs frame boundary behavior |
| RTT/12 | Overflow structural rules inform drift ceiling design |

### 6.2 — Downstream / Sibling

| Module | Relationship |
|---|---|
| Inside/Benchmarks | Consumes qCompute operator outcomes for OVERSCALE threshold testing |
| Inside/Enterprise | Consumes qCompute session governance for IDENTITY_BREACH enforcement |

### 6.3 — Cross-Module Zone X Disambiguation

Zone X labels are **module-local**. Do NOT import or conflate across module boundaries.

| Module | Zone X Label | Meaning |
|---|---|---|
| RTT/3 | Inversion | Structural inversion event |
| RTT/12 | Overflow | Overflow structural event |
| RTT/micro_core | Inversion | Micro-core inversion |
| The_Inverted_Star | Silence Breach | Silence layer breach |
| RTT/Inside | OVERREACH | Boundary overreach |
| Inside/Benchmarks | OVERSCALE | Scale boundary violation |
| Inside/Enterprise | IDENTITY_BREACH | Identity fabrication event |
| **Inside/qCompute** | **DECOHERENCE_BREACH** | **Structural decoherence — qCompute only** |

`[structural — no semantic inference]`

### 6.4 — Cross-Module Mode 5 Disambiguation

| Module | Mode 5 Label |
|---|---|
| RTT/3 | Inversion |
| RTT/12 | Overflow |
| RTT/micro_core | Lockout (Mode X) |
| The_Inverted_Star | Silence Breach |
| RTT/Inside | OVERREACH |
| Inside/Benchmarks | FABRICATION |
| Inside/Enterprise | IDENTITY_FABRICATION |
| **Inside/qCompute** | **PULSE_FABRICATION** |

`[structural — no semantic inference]`

---

## 7 · What qCompute Is Not

| qCompute IS | qCompute IS NOT |
|---|---|
| A structural session and operator execution layer `[structural]` | A quantum computing runtime or physics simulation |
| A deterministic tier-to-backend routing system `[structural]` | A probabilistic or heuristic execution engine |
| A six-stage operator validation pipeline `[structural]` | A single-check pass/fail gate |
| An append-only lineage and trace system `[structural]` | A mutable log or rewritable audit trail |
| A governance hot-swap engine with forward-only enforcement `[structural]` | A policy engine that applies changes retroactively |
| A module whose Zone X = DECOHERENCE_BREACH (local only) `[structural]` | A module that shares Zone X labels with siblings |
| A module whose Mode 5 = PULSE_FABRICATION (local only) `[structural]` | A module that shares Mode 5 labels with siblings |
| A framework layer where Class G authority is unconditional `[structural]` | A module where any class can override a halt |

`[structural — no semantic inference]`

---

## 8 · Quick-Start Checklist

Before executing any operator session in qCompute, verify all of the following:

- [ ] 1. **Environment selected** — `sandbox`, `production`, or `archive` is explicitly named; archive means no execution allowed
- [ ] 2. **Backend registered and tier-compatible** — `local-sim` (r1), `hybrid-sim` (r1+r2), or `hardware-qpu-2` (r3)
- [ ] 3. **Tier binding confirmed** — `tier_bind` is deterministic; no cross-tier backend routing is permitted
- [ ] 4. **Deploy token available** — required for production environment and all r3 operators; token is time-bounded and non-transferable
- [ ] 5. **Governance snapshot active** — policy file is loaded, valid, and not in safe-mode fallback
- [ ] 6. **Drift bound set** — `session.drift_bound` is defined and appropriate to the backend's max drift profile
- [ ] 7. **Lineage root anchored** — `lineage_root` is set; LINEAGE_CHAIN is append-only from this point forward
- [ ] 8. **Trace buffer initialized** — `qTrace` is active; `.qtrace` YAML will be written per operation
- [ ] 9. **Six-stage validation confirmed** — all stages (policy → env → backend → drift → restricted_ops → lineage) pass before execution
- [ ] 10. **Class G awareness** — DECOHERENCE_BREACH or PULSE_FABRICATION triggers unconditional halt; no override exists
- [ ] 11. **Zone X label is local** — DECOHERENCE_BREACH applies only within qCompute; do not import to sibling modules
- [ ] 12. **Mode 5 label is local** — PULSE_FABRICATION applies only within qCompute; do not import to sibling modules

`[structural — no semantic inference]`

---

## 9 · See Also

| Resource | Path | Description |
|---|---|---|
| AGENTS.md | `docs/rtt/Inside/qCompute/AGENTS.md` | Seven agent class definitions (A–G) |
| GLOSSARY.md | `docs/rtt/Inside/qCompute/GLOSSARY.md` | Canonical term definitions for qCompute |
| qc_API.md | `docs/rtt/Inside/qCompute/qc_API.md` | Session, Operator, Replay APIs + 11-reason error model |
| qc_BackendProfiles.md | `docs/rtt/Inside/qCompute/qc_BackendProfiles.md` | Backend specs, 8 invariants, routing reasons |
| qc_Backends.md | `docs/rtt/Inside/qCompute/qc_Backends.md` | Backend registry, tier binding, archive enforcement |
| qc_Capture.md | `docs/rtt/Inside/qCompute/qc_Capture.md` | Session transcript: identity, stack, envs, governance |
| README.md | `docs/rtt/Inside/qCompute/README.md` | Module overview |
| Inside/ABOUT.md | `docs/rtt/Inside/ABOUT.md` | Parent module framing and OVERREACH boundary |
| Inside/Benchmarks/ABOUT.md | `docs/rtt/Inside/Benchmarks/ABOUT.md` | OVERSCALE boundary reference |
| Inside/Enterprise/ABOUT.md | `docs/rtt/Inside/Enterprise/ABOUT.md` | IDENTITY_BREACH boundary reference |

---

> **Maintainer:** umaywant2
> **Module:** RTT / Inside / qCompute
> **Version:** 1.0.0
> **Date:** 2026-07-10
> **Status:** Canonical
> `[structural — no semantic inference]`
