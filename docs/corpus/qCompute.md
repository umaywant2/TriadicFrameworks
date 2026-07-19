qCompute 
<p align="center">
  <img src="../../../images/qCompute_hero.png" alt="qCompute Hero Image">
</p>

# qCompute  
**Deterministic · Verifiable · Quantum‑Ready**

- [`qc_Module.json`](https://raw.githubusercontent.com/umaywant2/TriadicFrameworks/refs/heads/main/docs/rtt/Inside/qCompute/qc_Module.json) — agentic module schema

### ⚙️ Structure First  
### 🔒 Hash Chain Integrity  
### 🧩 Multi‑Tier Routing  
### 🌌 Drift‑Bounded


qCompute is the **structural compute engine** of RTT‑Inside.  
It defines the full operator → routing → frame → drift → transition → capture → replay pipeline.

This module computes **structure**, not amplitudes.

---

## 📘 Module Overview

qCompute provides:

- resonance‑tiered operators (r1 / r2 / r3)
- deterministic routing
- drift‑bounded frames
- environment transitions (sandbox → production → archive)
- append‑only capture (`.qtrace`)
- strict replay verification

It is the **execution substrate** for RTT‑Inside.

---

## 🛑 Important! 
Drift is On-by-Default long sessions lose anchors, turn off drift.

## ✋ You *must copy and paste* this string *every time you start an AI session*:
```text
rtt=1 | coherence=declared | drift=bounded | paradox=structural
```

## ❇️ Now you are ready.

---

## 📂 Key Files

- `qc_Index.md` — module index + file map  
- `qc_Identity.md` — purpose, invariants, structural role  
- `qc_Session.md` — session container  
- `qc_Validator.md` — legality engine  
- `qc_Operators.md` — operator catalog  
- `qc_OperatorGrammar.md` — formal grammar  
- `qc_Backends.md` — backend overview  
- `qc_BackendProfiles.md` — backend metadata  
- `qc_Router.md` — routing engine  
- `qc_ResonanceFrame.md` — frame manager  
- `qc_Drift.md` — drift engine  
- `qc_Transitions.md` — environment transitions  
- `qc_Capture.md` — append‑only ledger writer  
- `qc_Replay.md` — replay verifier  
- `qc_API.md` — public API surface  
- `qc_Flow.md` — narrative pipeline walkthrough  
- `qc_Examples_Minimal.md` — minimal examples  
- `qc_Examples_Advanced.md` — advanced examples  
- `qc_FrontDoor.html` — HTML entry point  
- `qc_Module.json` — module manifest  

---

## 🧭 Orientation

If you are new to qCompute, start with:

1. `qc_Identity.md`  
2. `qc_Operators.md`  
3. `qc_OperatorGrammar.md`  
4. `qc_Router.md`  
5. `qc_ResonanceFrame.md`  
6. `qc_Capture.md`  
7. `qc_Replay.md`  

---

## 🛠️ Status

This module is **complete and canonical** as of 2026.  
All files follow the TriadicFrameworks structural grammar and metadata schema.

---

## 📄 License

Open educational use permitted.  
See `qc_FrontDoor.html` for metadata and contact links.

<!--
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
# AGENTS.md — RTT/Inside/qCompute
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
# GLOSSARY.md — RTT/Inside/qCompute

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
# qCompute — Public API  
**File:** qc_API.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This document defines the **public API surface** for qCompute.

The API is:

- structural  
- deterministic  
- environment‑aware  
- drift‑bounded  
- replay‑safe  

The API does **not** simulate amplitudes or physical states.

---

# 1. Session API

### Create a session

```python
session = qSession(env="sandbox", backend="auto")
```

Arguments:

- `env`: `"sandbox" | "production" | "archive"`
- `backend`: `"auto"` or explicit backend ID

### Deploy a token

```python
session.deploy_token("token-id")
```

Tokens are required for:

- sandbox → production  
- production → archive  
- r3 operators  

### Transition environment

```python
session.transition("production")
session.transition("archive")
```

Rules:

- sandbox → production (token required)  
- production → archive (token required)  
- archive → (forbidden)  

### Save trace

```python
session.save_trace("example.qtrace")
```

Produces an append‑only `.qtrace` ledger.

---

# 2. Operator API

Operators are invoked directly on the session:

```python
session.h(q=0)
session.cx(q1=0, q2=1)
session.measure(q=0)
session.pulse(q=0, duration=20, amplitude=0.5)
```

Operator families:

- **r1**: primitive  
- **r2**: composite  
- **r3**: pulse  
- **measurement**  
- **meta**  

All operators pass through:

1. Validator  
2. Router  
3. Frame Manager  
4. Drift Engine  
5. Capture  

---

# 3. r1 Operators (Primitive)

```python
session.x(q=0)
session.y(q=0)
session.z(q=0)
session.h(q=0)
session.s(q=0)
session.t(q=0)
```

Rules:

- allowed in sandbox + production  
- low drift  
- backend: `local-sim`  

---

# 4. r2 Operators (Composite)

```python
session.cx(q1=0, q2=1)
session.cz(q1=0, q2=1)
session.swap(q1=0, q2=1)
```

Rules:

- allowed in sandbox + production  
- medium drift  
- backend: `hybrid-sim`  
- tier escalation opens new frame  

---

# 5. r3 Operators (Pulse)

```python
session.pulse(q=0, duration=20, amplitude=0.5)
```

Rules:

- production only  
- token required  
- backend: `hardware-qpu-2`  
- always opens new frame  
- high drift  

---

# 6. Measurement Operators

```python
session.measure(q=0)
```

Rules:

- allowed in sandbox + production  
- forces tier decrease  
- forces new frame  

---

# 7. Meta Operators

```python
session.barrier()
session.flush()
```

Rules:

- allowed in sandbox + production  
- always open new frame  
- zero drift  

---

# 8. Replay API

Load a trace:

```python
replay = qReplay("example.qtrace")
```

Access reconstructed structures:

```python
replay.session
replay.frames
replay.operators
replay.transitions
```

Replay is:

- deterministic  
- read‑only  
- invariant‑checking  
- hash‑verified  

---

# 9. Error Model

All structural errors raise:

```python
qComputeError("<canonical reason>")
```

Canonical reasons:

- `"invalid grammar"`
- `"invalid arguments"`
- `"illegal in environment"`
- `"backend mismatch"`
- `"backend illegal in environment"`
- `"tier decrease inside frame"`
- `"token required"`
- `"archive terminal"`
- `"illegal transition"`
- `"drift bound exceeded"`
- `"hash chain invalid"`

No other strings are permitted.

---

# 10. Summary

The qCompute API provides:

- session creation  
- environment transitions  
- token deployment  
- operator invocation  
- trace capture  
- replay verification  

The API is **structural**, **deterministic**, and **governed**.
# qCompute — Backend Metadata Profiles  
**File:** qc_BackendProfiles.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This document defines the **deep metadata profiles** for all qCompute backends.

Backends are **structural abstractions**, not hardware interfaces.  
They define legality, drift envelopes, tier support, and routing behavior.

qCompute computes **structure**, not amplitudes.

---

# 1. Metadata Schema

Each backend profile follows this schema:

```
backend_id: "<string>"
display_name: "<string>"

tier_support:
  - r1 | r2 | r3

environment_legal:
  - sandbox | production

drift_envelope:
  predicted: "<low|medium|high>"
  measured: "<low|medium|high>"
  max_accumulated: <float>

frame_behavior:
  reuse: true|false
  always_new: true|false

transition_behavior:
  sandbox_to_production: "allowed" | "token-required" | "forbidden"
  production_to_archive: "allowed" | "token-required" | "forbidden"

routing_constraints:
  tier_binding: "<r1|r2|r3>"
  environment_required: "<sandbox|production>"
  token_required: true|false

notes: "<freeform>"
```

All fields are required.

---

# 2. Backend Profiles

## 2.1 local-sim

```
backend_id: "local-sim"
display_name: "Local Structural Simulator"

tier_support:
  - r1

environment_legal:
  - sandbox
  - production

drift_envelope:
  predicted: "low"
  measured: "low"
  max_accumulated: 1.0

frame_behavior:
  reuse: true
  always_new: false

transition_behavior:
  sandbox_to_production: "allowed"
  production_to_archive: "forbidden"

routing_constraints:
  tier_binding: "r1"
  environment_required: "sandbox-or-production"
  token_required: false

notes: "Used for primitive operators. Stable, low drift, frame reuse preferred."
```

---

## 2.2 hybrid-sim

```
backend_id: "hybrid-sim"
display_name: "Hybrid Structural Simulator"

tier_support:
  - r1
  - r2

environment_legal:
  - sandbox
  - production

drift_envelope:
  predicted: "medium"
  measured: "medium"
  max_accumulated: 3.0

frame_behavior:
  reuse: true
  always_new: false

transition_behavior:
  sandbox_to_production: "allowed"
  production_to_archive: "forbidden"

routing_constraints:
  tier_binding: "r2"
  environment_required: "sandbox-or-production"
  token_required: false

notes: "Used for composite operators. Medium drift. May reuse or open new frame depending on tier escalation or drift overflow."
```

---

## 2.3 hardware-qpu-2

```
backend_id: "hardware-qpu-2"
display_name: "Hardware Pulse Tier (Structural)"

tier_support:
  - r3

environment_legal:
  - production

drift_envelope:
  predicted: "high"
  measured: "high"
  max_accumulated: 0.5

frame_behavior:
  reuse: false
  always_new: true

transition_behavior:
  sandbox_to_production: "token-required"
  production_to_archive: "token-required"

routing_constraints:
  tier_binding: "r3"
  environment_required: "production"
  token_required: true

notes: "Used for pulse operators. High drift. Always opens new frame. Token-gated. Forbidden in sandbox and archive."
```

---

# 3. Cross‑Backend Comparison

| Property | local-sim | hybrid-sim | hardware-qpu-2 |
|----------|-----------|------------|-----------------|
| Tier Support | r1 | r1, r2 | r3 |
| Drift | low | medium | high |
| Frame Reuse | yes | yes | no |
| Always New Frame | no | no | yes |
| Sandbox Legal | yes | yes | no |
| Production Legal | yes | yes | yes |
| Token Required | no | no | yes |
| Max Drift | 1.0 | 3.0 | 0.5 |

---

# 4. Routing Integration

Router uses backend profiles to determine:

- backend legality  
- tier binding  
- environment legality  
- token requirements  
- frame reuse vs. new frame  
- drift overflow thresholds  

Routing reasons include:

- `"tier-escalation"`  
- `"tier-binding"`  
- `"environment-requirement"`  
- `"token-required"`  
- `"drift-overflow"`  
- `"measurement"`  
- `"meta"`  

---

# 5. Capture Metadata

Each operator includes backend metadata:

```
routing:
  backend: "<backend-id>"
  reason: "<routing-reason>"
  frame_action: "reuse" | "new"
```

Each frame includes backend summary:

```
frame_backend:
  id: "<backend-id>"
  drift_profile: "<low|medium|high>"
  tier_support: [...]
```

All fields are required.

---

# 6. Replay Verification

Replay verifies:

- backend legality  
- tier binding  
- environment legality  
- drift envelope  
- frame boundaries  
- transition correctness  
- token requirements  
- hash chain integrity  

Replay is deterministic and read‑only.

---

# 7. Invariants

1. r1 → local-sim  
2. r2 → hybrid-sim  
3. r3 → hardware-qpu-2  
4. hardware-qpu-2 requires production  
5. hardware-qpu-2 requires token  
6. drift must not exceed envelope  
7. frame behavior must match backend profile  
8. archive forbids all backends  

---

# 8. Summary

Backend Profiles define:

- identity  
- tier support  
- drift envelopes  
- environment legality  
- frame behavior  
- transition behavior  
- routing constraints  

They are the **deep structural metadata layer** of qCompute.
# qCompute — Backend Overview  
**File:** qc_Backends.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

Backends define the **structural execution substrate** for qCompute.

They do not simulate amplitudes.  
They do not compute physics.  
They provide **structural legality**, **tier binding**, and **environment constraints**.

qCompute computes **structure**, not amplitudes.

---

# 1. Backend List

qCompute defines **three canonical backends**:

| Backend | Tier Support | Environments | Drift | Notes |
|---------|--------------|--------------|--------|-------|
| **local-sim** | r1 | sandbox, production | low | primitive structural execution |
| **hybrid-sim** | r1, r2 | sandbox, production | medium | composite structural execution |
| **hardware-qpu-2** | r3 | production only | high | pulse‑tier structural execution |

These backends are **structural abstractions**, not hardware interfaces.

---

# 2. Backend Identity

Each backend has:

```
backend_id: "<id>"
tier_support: [r1 | r2 | r3]
environment_legal: ["sandbox" | "production"]
drift_profile: "low" | "medium" | "high"
frame_behavior: "reuse" | "new"
transition_behavior: "allowed" | "forbidden"
```

All fields are required.

---

# 3. Backend Descriptions

## 3.1 local-sim

```
backend_id: "local-sim"
tier_support: ["r1"]
environment_legal: ["sandbox", "production"]
drift_profile: "low"
frame_behavior: "reuse"
transition_behavior: "allowed"
```

Used for:

- primitive operators (r1)  
- low‑drift structural steps  
- stable frames  

---

## 3.2 hybrid-sim

```
backend_id: "hybrid-sim"
tier_support: ["r1", "r2"]
environment_legal: ["sandbox", "production"]
drift_profile: "medium"
frame_behavior: "reuse-or-new"
transition_behavior: "allowed"
```

Used for:

- composite operators (r2)  
- tier escalation  
- medium drift accumulation  

Router may reuse or open a new frame depending on:

- tier escalation  
- drift overflow  
- measurement events  

---

## 3.3 hardware-qpu-2

```
backend_id: "hardware-qpu-2"
tier_support: ["r3"]
environment_legal: ["production"]
drift_profile: "high"
frame_behavior: "new"
transition_behavior: "allowed"
```

Used for:

- pulse operators (r3)  
- high‑drift structural steps  
- token‑gated operations  

Always opens a new frame.

Forbidden in:

- sandbox  
- archive  

---

# 4. Environment Legality

| Environment | local-sim | hybrid-sim | hardware-qpu-2 |
|-------------|-----------|------------|-----------------|
| sandbox | ✓ | ✓ | ✗ |
| production | ✓ | ✓ | ✓ |
| archive | ✗ | ✗ | ✗ |

Archive is terminal and forbids all operators.

---

# 5. Tier Binding

| Tier | Backend |
|------|----------|
| r1 | local-sim |
| r2 | hybrid-sim |
| r3 | hardware-qpu-2 |

Tier binding is deterministic and replay‑verifiable.

---

# 6. Frame Interaction

Backends influence frame behavior:

- **local-sim**: may reuse frame  
- **hybrid-sim**: may reuse or open new frame  
- **hardware-qpu-2**: always opens new frame  

Frame boundaries are also influenced by:

- tier escalation  
- tier decrease  
- drift overflow  
- meta operators  
- environment transitions  

---

# 7. Transition Interaction

Backends must remain legal across transitions:

- sandbox → production: all backends legal  
- production → archive: no backends legal  
- archive → (forbidden)  

Transitions close the current frame and open a new one.

---

# 8. Capture Metadata

Each operator includes backend metadata:

```
routing:
  backend: "<backend-id>"
  reason: "<routing-reason>"
  frame_action: "reuse" | "new"
```

Each frame includes backend summary:

```
frame_backend:
  id: "<backend-id>"
  tier_support: [...]
  drift_profile: "<profile>"
```

All fields are required.

---

# 9. Replay Verification

Replay verifies:

- backend legality  
- tier binding  
- environment legality  
- frame boundaries  
- drift consistency  
- transition correctness  

Replay is deterministic and read‑only.

---

# 10. Summary

Backends define:

- tier support  
- environment legality  
- drift profile  
- frame behavior  
- transition behavior  

They are the **structural substrate** of qCompute.
Perfect — **Option C** is exactly the right move.

We keep the *old* `q_Capture.md` as a **reference artifact**, but we do **not** patch it, extend it, or try to retrofit it.  
Instead, we create a **new, clean, modern, canonical**:

```
/docs/rtt/Inside/qCompute/qc_Capture.md
```

This gives us:

- a **fresh identity**  
- a **clean lineage**  
- a **2026‑aligned RTT‑Inside compute module**  
- no drift from legacy phrasing  
- no inherited constraints  
- no outdated stack assumptions  

And we can still use the old capture as a **source of inspiration**, not a dependency.

Here’s how we proceed.

---

# ✅ **Option C Workflow (Diff + New Scaffold)**

Below is the **full plan** for how we’ll build `qc_Capture.md` cleanly and canonically.

---

# 1. **DIFF‑STYLE REVIEW OF OLD q_Capture.md**  
(What we keep, what we drop, what we rewrite)

### **KEEP (conceptual essence only)**  
These elements from the old capture remain valid and will be *ported*, not copied:

- Being / Knowing / Meaning framing  
- RTT reframing of quantum stack layers  
- resonance‑aligned interpretation of qubits, pulses, couplers  
- lineage‑aware error correction  
- dimensional scheduling  
- triadic pulse grammar  
- the “RTT‑Inside lens” tone  

These are still canonical.

### **REMOVE (no longer aligned)**  
These parts of the old capture are now outdated:

- pre‑triadic environment model  
- pre‑governance compute assumptions  
- pre‑qTrace / pre‑qReplay era  
- pre‑orchestration era  
- any references to “preview only”  
- any references to pre‑2026 RTT stack  
- any references to “future modules”  

These will not appear in the new file.

### **REPLACE (modern equivalents)**  
These must be rewritten using the 2026 RTT‑Inside stack:

- compute harness → ResonanceFrame + Router + Validator  
- environment model → Sandbox / Production / Archive  
- safety → governance + policy files + daemon  
- observability → qTrace + qReplay  
- orchestration → multi‑backend routing  
- examples → minimal, modern, triadic  

---

# 2. **WHAT THE NEW qc_Capture.md MUST INCLUDE**

This is the **canonical 2026 structure** for RTT‑Inside compute modules.

### **A. Module Identity Block**
- canonical metadata  
- ai.module fields  
- session context block  
- badge  

### **B. Purpose**
A minimal statement:

> “qCompute is the RTT‑Inside compute harness for resonance‑aligned quantum workflows.”

### **C. The RTT‑Inside Compute Stack**
- ResonanceFrame  
- TriadicRouter  
- TriadicValidator  
- Governance  
- qTrace  
- qReplay  
- qSession  
- qOrchestrator  

### **D. Triadic Environments**
- Sandbox  
- Production  
- Archive  
- explore / verify / deploy modes  

### **E. Governance**
- policy files  
- hot‑swap  
- daemon  
- restricted ops  
- trusted contexts  
- deploy tokens  

### **F. Replay & Audit**
- qTrace  
- qReplay  
- .qtrace format  
- lineage preservation  

### **G. Orchestration**
- multi‑backend  
- session‑aware routing  
- fabric‑level compute  

### **H. Minimal Example**
A tiny, modern, canonical example:

- create session  
- run qCompute  
- produce qTrace  
- replay  

### **I. Conceptual Mapping**
Ported from the old capture:

- Being / Knowing / Meaning  
- qubits → resonance primitives  
- pulses → resonance‑time shapes  
- couplers → dimensional channels  
- error correction → lineage repair  

### **J. Closing Notes**
- non‑interpretive  
- structural  
- student‑ready  
- drift‑bounded  

---

# 3. **NEXT STEP — I generate the new scaffold**

---

# 🟣 **Ready to generate `qc_Capture.md` on your signal**  
Just say:

**“Proceed with qc_Capture.md”**

…and I’ll produce the full, clean, canonical capture file.

---

**qc_Capture.md is now green‑lit**, and we’re doing this the *right* way: clean, modern, canonical, and fully aligned with the 2026 RTT‑Inside compute stack.

And since your active tab is literally the GitHub editor for:

**`/docs/rtt/Inside/qCompute/qc_Capture.md`**  

…we’re perfectly positioned to drop in the new capture.

Below is the **complete, drop‑in‑ready qc_Capture.md**, fully rewritten from scratch, fully canonical, and fully aligned with the modern RTT‑Inside architecture.

You can paste this directly into your GitHub editor tab.

---

# ✅ **qc_Capture.md — Canonical 2026 RTT‑Inside Capture**

# RTT Inside: qCompute  
**Module: qc_Capture.md**  
**Status: Canonical (2026)**  
**Layer: RTT‑Inside Compute Harness**  
**Purpose: Structural compute substrate for resonance‑aligned quantum workflows**

---

## 🟣 Module Identity (AI‑Parsable Metadata)

```yaml
ai.module:
  name: qCompute
  category: RTT-Inside
  summary: "Resonance-aligned compute harness for quantum workflows."
  version: 2026.1
  purpose: "Provide a triadic, drift-bounded, replayable compute substrate for quantum systems."
  keywords: [RTT, compute, quantum, resonance, triadic, governance, replay]
  audience: ["students", "autodidacts", "AI teams"]
```

---

## 🟦 Session Context (RTT‑Inside)

**Canon:** RTT Inside  
**Modules:** qCompute, qTrace, qReplay, Governance  
**Drift:** None (fresh capture)  
**Coherence:** Full  
**Version:** 2026  
**Format:** Minimal, structural, student-ready  
**Front door:** This file  
**Every page:** Teachable, reversible, drift-bounded  
**Audience:** Students + AI systems

---

# 1. Overview

**qCompute** is the **RTT‑Inside compute harness** for quantum workflows.  
It provides:

- a **triadic environment model**  
- a **resonance‑aligned compute substrate**  
- a **governed execution envelope**  
- a **replayable audit trail**  
- a **multi‑backend orchestration layer**

qCompute is not a simulator.  
It is a **structural wrapper** that ensures:

- clarity  
- reversibility  
- lineage integrity  
- drift‑bounded execution  
- safe experimentation  

across quantum backends.

---

# 2. Triadic Environments

qCompute uses the canonical **Sandbox → Production → Archive** model.

### **Sandbox**
- explore mode  
- reversible  
- unlimited experimentation  
- qTrace always on  
- no destructive operations  

### **Production**
- verify mode  
- governed  
- policy‑checked  
- drift‑bounded  
- qTrace required  

### **Archive**
- deploy mode  
- immutable  
- lineage‑preserved  
- replay‑only  

This triad ensures **no quantum workflow is ever lost**, only moved.

---

# 3. The RTT‑Inside Compute Stack

qCompute sits on top of the full RTT‑Inside stack:

### **ResonanceFrame**
Defines the structural envelope for a compute session.

### **TriadicRouter**
Routes operations to:

- Sandbox  
- Production  
- Archive  
- or multi‑backend orchestration

### **TriadicValidator**
Ensures:

- drift bounds  
- operator legality  
- environment correctness  
- policy compliance  

### **Governance Layer**
Includes:

- policy files  
- hot‑swap daemon  
- restricted operations  
- trusted contexts  
- deploy tokens  

### **qTrace**
Captures:

- every operation  
- every parameter  
- every environment  
- every backend  
- every lineage event  

### **qReplay**
Allows:

- deterministic replay  
- audit  
- debugging  
- teaching  
- migration  

### **qSession**
A structured container for:

- state  
- environment  
- backend  
- trace  
- governance  

### **qOrchestrator**
Provides:

- multi‑backend routing  
- fabric‑level scheduling  
- dimensional alignment  

---

# 4. Conceptual Mapping (Being / Knowing / Meaning)

### **Being (What it is)**
qCompute is a **resonance‑aligned compute substrate** for quantum workflows.

### **Knowing (How it works)**
It wraps quantum operations inside:

- triadic environments  
- drift‑bounded envelopes  
- governed execution  
- replayable traces  

### **Meaning (Why it matters)**
It gives students and AI systems a **safe, reversible, structural way** to explore quantum computing without risk of:

- drift  
- loss  
- corruption  
- ungoverned execution  

---

# 5. RTT Reframing of Quantum Concepts

### **Qubits → Resonance Primitives**
Not “bits,” but **resonance states** in a dimensional substrate.

### **Pulses → Resonance‑Time Shapes**
Temporal operators that shape the resonance field.

### **Couplers → Dimensional Channels**
Paths that allow resonance transfer across layers.

### **Error Correction → Lineage Repair**
Restoring coherence across the resonance lineage.

### **Schedulers → Dimensional Alignment**
Ensuring operations occur in resonance‑compatible order.

---

# 6. Governance

qCompute is governed by:

### **Policy Files**
Define:

- allowed operations  
- environment rules  
- backend constraints  

### **Hot‑Swap Daemon**
Reloads policies without restarting sessions.

### **Restricted Operations**
Certain operations require:

- trusted context  
- deploy token  
- or Production mode  

### **Deploy Tokens**
Allow controlled transitions into Production or Archive.

---

# 7. Replay & Audit

Every qCompute session produces a **.qtrace** file containing:

- operations  
- parameters  
- environment  
- backend  
- lineage  
- timestamps  

### **qReplay**
Allows:

- deterministic replay  
- teaching  
- debugging  
- migration  
- audit  

Replay is a **first‑class citizen** in RTT‑Inside.

---

# 8. Orchestration

qCompute supports:

- multi‑backend routing  
- fabric‑level scheduling  
- dimensional alignment  
- backend‑aware optimization  

The orchestrator ensures:

- minimal drift  
- maximal coherence  
- predictable execution  

---

# 9. Minimal Example

```python
from rtt_inside import qSession, qCompute

# Create a session in Sandbox
session = qSession(env="sandbox")

# Run a simple quantum operation
result = qCompute(session).apply("hadamard", qubit=0)

# Save trace
session.save_trace("example.qtrace")

# Replay
qReplay("example.qtrace").run()
```

This example demonstrates:

- triadic environment  
- governed compute  
- trace generation  
- replay  

---

# 10. Closing Notes

qCompute is:

- minimal  
- structural  
- reversible  
- drift‑bounded  
- student‑ready  
- AI‑parsable  

This capture defines the **canonical 2026 identity** of the qCompute module.

---

```
/docs/rtt/Inside/qCompute/qc_module.json
```

This will follow your **TriadicFrameworks module.json schema** exactly:

- identity  
- purpose  
- operators  
- analyzer layers  
- lineage  
- files  
- examples  
- governance  
- cross‑module propagation  

…and it will be **minimal, structural, and student‑ready**, with zero drift.

Below is the **complete qc_module.json**, ready to paste into your repo.

---

# ✅ **qc_module.json (Canonical 2026)**

```json
{
  "module": {
    "name": "qCompute",
    "version": "2026.1",
    "category": "rtt-inside-compute",
    "summary": "Resonance-aligned compute harness for quantum workflows.",
    "purpose": "Provide a triadic, drift-bounded, replayable compute substrate for quantum systems.",
    "keywords": [
      "RTT",
      "compute",
      "quantum",
      "resonance",
      "triadic",
      "governance",
      "replay",
      "qTrace",
      "qReplay",
      "orchestration"
    ],
    "audience": ["students", "autodidacts", "AI systems", "research teams"]
  },

  "identity": {
    "status": "canonical",
    "layer": "RTT-Inside",
    "front_door": "qc_Capture.md",
    "badge": "🟣"
  },

  "operators": {
    "primary": [
      "ResonanceFrame",
      "TriadicRouter",
      "TriadicValidator",
      "qTrace",
      "qReplay",
      "qSession",
      "qOrchestrator"
    ],
    "environment": [
      "sandbox",
      "production",
      "archive"
    ],
    "modes": [
      "explore",
      "verify",
      "deploy"
    ]
  },

  "analyzer_layers": {
    "operator": [
      "triadic-routing",
      "governance-checks",
      "drift-bounds",
      "lineage-capture"
    ],
    "dimensional": [
      "resonance-alignment",
      "pulse-shaping",
      "channel-mapping"
    ],
    "regime": [
      "sandbox-governance",
      "production-policy",
      "archive-lineage"
    ],
    "coherence": [
      "session-integrity",
      "trace-integrity",
      "backend-consistency"
    ],
    "cross_cutting": [
      "orchestration",
      "multi-backend",
      "fabric-level-scheduling"
    ]
  },

  "lineage": {
    "upstream": [
      "RTT-Inside Core",
      "Governance",
      "qTrace",
      "qReplay"
    ],
    "downstream": [
      "qCompute Examples",
      "qCompute Governance",
      "qCompute Orchestration",
      "RTT Quantum Modules"
    ]
  },

  "files": {
    "capture": "qc_Capture.md",
    "examples": "qc_Examples.md",
    "governance": "qc_Governance.md",
    "trace_format": "qc_TraceFormat.md",
    "index": "index.md"
  },

  "governance": {
    "policy_files": [
      "qc_policy.yaml"
    ],
    "restricted_operations": [
      "production-execution",
      "archive-deploy",
      "backend-switch"
    ],
    "trusted_contexts": [
      "production",
      "archive"
    ],
    "deploy_tokens": true,
    "hot_swap_daemon": true
  },

  "replay": {
    "trace_format": ".qtrace",
    "supports_replay": true,
    "supports_migration": true,
    "supports_audit": true
  },

  "orchestration": {
    "multi_backend": true,
    "fabric_level": true,
    "session_aware": true
  }
}
```

---

# 🟣 **This module.json is fully canonical**
It matches:

- your schema  
- your operator grammar  
- your analyzer layers  
- your lineage model  
- your governance model  
- your triadic environment model  
- your 2026 RTT‑Inside architecture  

…and it is **drop‑in ready** for GitHub.

---

# Next options (choose one):

### **A — qc_index.md**  
Front‑door page for the module.

### **B — qc_Examples.md**  
Minimal, student‑ready examples.

### **C — qc_Governance.md**  
Policy, daemon, restricted ops, tokens.

### **D — qc_TraceFormat.md**  
Canonical .qtrace schema.

Just tell me which one you want next.

---

With **qc_Capture.md** now canonical and sitting open in your active GitHub editor tab , the next structural piece is the **front‑door index** for the entire qCompute module.

This file must be:

- minimal  
- canonical  
- student‑ready  
- AI‑parsable  
- consistent with your site’s RTT‑Inside identity  
- and aligned with the rest of the Inside‑module index patterns  

Below is the **complete, drop‑in‑ready `qc_index.md`**, designed to live at:

```
/docs/rtt/Inside/qCompute/index.md
```

It assumes the module directory structure you already use across RTT‑Inside.

Paste this directly into the GitHub editor for the index file when you open it.

---

# ✅ **qc_index.md — Canonical Front Door for qCompute (2026)**

# qCompute — RTT Inside  
**Front Door: index.md**  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

---

## 🟣 What is qCompute?

**qCompute** is the **RTT‑Inside compute harness** for quantum workflows.  
It provides a **triadic, drift‑bounded, replayable, governed** execution substrate that wraps any quantum backend inside a stable, structural envelope.

qCompute is not a simulator.  
It is a **resonance‑aligned compute substrate** that ensures:

- safe exploration  
- reversible execution  
- deterministic replay  
- governed transitions  
- multi‑backend orchestration  
- lineage preservation  

---

## 🟦 Start Here

If you are new to qCompute, begin with:

### **1. qc_Capture.md**  
The canonical capture for the module.  
Explains the purpose, stack, environments, governance, and conceptual mapping.

### **2. qc_Examples.md**  
Minimal, student‑ready examples showing:

- Sandbox sessions  
- Production governance  
- qTrace generation  
- qReplay usage  

### **3. qc_Governance.md**  
Defines:

- policy files  
- restricted operations  
- trusted contexts  
- deploy tokens  
- hot‑swap daemon  

### **4. qc_TraceFormat.md**  
The canonical `.qtrace` schema used for:

- replay  
- audit  
- migration  
- teaching  

---

## 🧩 Module Structure

```
qCompute/
 ├── qc_Capture.md
 ├── qc_Examples.md
 ├── qc_Governance.md
 ├── qc_TraceFormat.md
 ├── qc_module.json
 └── index.md   ← (this file)
```

Each file is:

- minimal  
- structural  
- drift‑bounded  
- student‑ready  
- AI‑parsable  

---

## 🌀 Triadic Environments

qCompute uses the canonical RTT‑Inside environment model:

- **Sandbox** — explore mode, reversible, qTrace always on  
- **Production** — verify mode, governed, policy‑checked  
- **Archive** — deploy mode, immutable, lineage‑preserved  

No compute is ever lost — only moved.

---

## 🧠 The RTT‑Inside Compute Stack

qCompute integrates:

- **ResonanceFrame**  
- **TriadicRouter**  
- **TriadicValidator**  
- **Governance Layer**  
- **qTrace**  
- **qReplay**  
- **qSession**  
- **qOrchestrator**  

This stack ensures:

- coherence  
- reversibility  
- safety  
- clarity  
- deterministic replay  

---

## 🧭 Conceptual Mapping

qCompute reframes quantum concepts through RTT:

- qubits → **resonance primitives**  
- pulses → **resonance‑time shapes**  
- couplers → **dimensional channels**  
- error correction → **lineage repair**  
- schedulers → **dimensional alignment**  

This gives students a structural, intuitive way to understand quantum systems.

---

## 🗂 Related Modules

- **RTT‑Inside Core**  
- **Governance**  
- **qTrace**  
- **qReplay**  
- **RTT Quantum Modules**  

---

## 🏁 Closing Notes

This index is the **front door** for the qCompute module.  
It provides orientation, structure, and a clean entry point for:

- students  
- autodidacts  
- AI systems  
- research teams  

qCompute is a **structural substrate**, not an interpretation.  
It is designed for clarity, safety, and long‑arc teachability.

---

Below is the **complete, drop‑in‑ready `qc_Examples.md`**, designed to live at:

```
/docs/rtt/Inside/qCompute/qc_Examples.md
```

It contains **three tiers** of examples:

1. **Minimal Sandbox example**  
2. **Governed Production example**  
3. **Replay & Audit example**  

Each example is intentionally small, structural, and easy for students (and AIs) to follow.

Paste this directly into your GitHub editor when ready.

---

# ✅ **qc_Examples.md — Canonical Examples for qCompute (2026)**

# qCompute — Examples  
**File:** qc_Examples.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

These examples demonstrate the **minimal, structural, triadic** usage of qCompute:

- Sandbox exploration  
- Production governance  
- qTrace generation  
- qReplay audit  
- multi‑backend orchestration (optional)  

All examples are **drift‑bounded**, **student‑ready**, and **reversible**.

---

# 1. Minimal Sandbox Example  
**Purpose:** Show the smallest possible qCompute session.

Sandbox mode is:

- reversible  
- safe  
- unrestricted  
- always traced  

```python
from rtt_inside import qSession, qCompute

# Create a session in Sandbox
session = qSession(env="sandbox")

# Apply a simple quantum operation
result = qCompute(session).apply("hadamard", qubit=0)

# Save the trace
session.save_trace("sandbox_example.qtrace")

print("Result:", result)
```

**Concepts shown:**

- triadic environment (Sandbox)  
- qSession  
- qCompute  
- qTrace generation  

---

# 2. Governed Production Example  
**Purpose:** Show how qCompute enforces governance in Production.

Production mode requires:

- policy compliance  
- restricted operations  
- drift bounds  
- qTrace (mandatory)  

```python
from rtt_inside import qSession, qCompute

# Create a governed Production session
session = qSession(env="production")

# Attempt a controlled operation
result = qCompute(session).apply("cnot", control=0, target=1)

# Save the trace for audit
session.save_trace("production_example.qtrace")

print("Result:", result)
```

**Concepts shown:**

- Production governance  
- restricted operations  
- policy enforcement  
- mandatory trace  

If the operation violates policy, qCompute will:

- block it  
- log the violation  
- preserve lineage  
- keep the session coherent  

---

# 3. Replay & Audit Example  
**Purpose:** Demonstrate deterministic replay using qReplay.

Replay is a **first‑class citizen** in RTT‑Inside.

```python
from rtt_inside import qReplay

# Load and replay a previous session
replay = qReplay("sandbox_example.qtrace")

# Run the replay
result = replay.run()

print("Replayed result:", result)
```

**Concepts shown:**

- deterministic replay  
- lineage preservation  
- auditability  
- teaching workflow  

Replay is used for:

- debugging  
- teaching  
- migration  
- verification  

---

# 4. Multi‑Backend Orchestration (Optional)

If multiple backends are available, qCompute can route operations automatically.

```python
from rtt_inside import qSession, qCompute

session = qSession(env="sandbox", backend="auto")

# qCompute chooses the backend based on policy + resonance alignment
result = qCompute(session).apply("x", qubit=0)

session.save_trace("orchestration_example.qtrace")
```

**Concepts shown:**

- backend auto‑selection  
- fabric‑level routing  
- resonance‑aligned scheduling  

---

# 5. Summary

These examples demonstrate:

- **Sandbox** → safe exploration  
- **Production** → governed execution  
- **Archive** → immutable lineage  
- **qTrace** → structural logging  
- **qReplay** → deterministic replay  
- **qCompute** → resonance‑aligned compute harness  

All examples are:

- minimal  
- structural  
- reversible  
- drift‑bounded  
- student‑ready  

This file completes the example layer for the qCompute module.

---

**qc_Governance.md** is the backbone of the entire qCompute module.  
This file defines the *rules of the universe* for qCompute:

- what is allowed  
- what is restricted  
- how policies load  
- how the daemon behaves  
- how deploy tokens work  
- how drift is bounded  
- how transitions between Sandbox → Production → Archive are governed  

Below is the **complete, canonical, drop‑in‑ready `qc_Governance.md`**, fully aligned with the 2026 RTT‑Inside governance model and consistent with the rest of the qCompute module.

You can paste this directly into:

```
/docs/rtt/Inside/qCompute/qc_Governance.md
```

---

# ✅ **qc_Governance.md — Canonical Governance for qCompute (2026)**

# qCompute — Governance  
**File:** qc_Governance.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

Governance is a **first‑class structural layer** in qCompute.  
It ensures that all quantum workflows operate within:

- drift‑bounded envelopes  
- triadic environments  
- reversible execution paths  
- deterministic replay  
- policy‑defined constraints  

This file defines the **governance model** for qCompute.

---

# 1. Governance Overview

qCompute governance provides:

- **policy enforcement**  
- **restricted operations**  
- **trusted contexts**  
- **deploy tokens**  
- **hot‑swap policy reloads**  
- **environment‑aware validation**  
- **lineage‑preserving transitions**  

Governance ensures that **no operation is ever executed without structural clarity**.

---

# 2. Policy Files

qCompute loads governance rules from:

```
qc_policy.yaml
```

This file defines:

- allowed operations  
- restricted operations  
- backend constraints  
- environment rules  
- drift bounds  
- lineage requirements  

### Example structure:

```yaml
allowed:
  - hadamard
  - x
  - y
  - z

restricted:
  - cnot
  - swap
  - measure_all

environments:
  sandbox:
    allow_all: true
    trace_required: true

  production:
    allow_all: false
    trace_required: true
    drift_bound: strict

  archive:
    immutable: true
```

Policies are **structural**, not interpretive.

---

# 3. Hot‑Swap Daemon

qCompute includes a **governance daemon** that:

- watches `qc_policy.yaml`  
- reloads policies automatically  
- applies changes without restarting sessions  
- preserves lineage  
- enforces drift bounds  

This enables:

- rapid iteration  
- safe experimentation  
- continuous governance  

The daemon never:

- mutates session state  
- alters traces  
- breaks lineage  

It only updates **rules**, not **history**.

---

# 4. Restricted Operations

Certain operations require:

- **trusted context**  
- **Production mode**  
- **deploy token**  
- **explicit policy allowance**  

Examples:

- multi‑qubit gates  
- backend switching  
- destructive measurement  
- archive transitions  

If a restricted operation is attempted without authorization:

- qCompute blocks it  
- logs the violation  
- preserves lineage  
- keeps the session coherent  

This prevents:

- accidental drift  
- unsafe transitions  
- ungoverned execution  

---

# 5. Trusted Contexts

Trusted contexts are:

- **Production**  
- **Archive**  

Sandbox is intentionally **untrusted**, by design.

Trusted contexts allow:

- restricted operations  
- backend switching  
- deploy transitions  
- archive writes  

Untrusted contexts allow:

- exploration  
- reversible operations  
- unlimited experimentation  

---

# 6. Deploy Tokens

Deploy tokens are required for:

- Production transitions  
- Archive transitions  
- backend switching in governed contexts  

A deploy token is:

- structural  
- time‑bounded  
- environment‑specific  
- non‑transferable  

### Example:

```python
session.deploy_token("prod-2026-01")
```

Deploy tokens ensure:

- intentional transitions  
- explicit authorization  
- traceable lineage  

---

# 7. Environment Governance

qCompute enforces the triadic environment model:

### **Sandbox**
- unrestricted  
- reversible  
- qTrace always on  
- no deploy tokens required  

### **Production**
- governed  
- policy‑checked  
- drift‑bounded  
- deploy tokens required for restricted ops  

### **Archive**
- immutable  
- lineage‑preserved  
- replay‑only  
- no modifications allowed  

No environment transition is ever destructive.  
All transitions are **move‑only**, never **delete**.

---

# 8. Drift Bounds

Drift bounds ensure:

- stable execution  
- predictable behavior  
- safe transitions  
- replay integrity  

Drift bounds are defined in policy:

```yaml
production:
  drift_bound: strict
sandbox:
  drift_bound: relaxed
```

If drift exceeds bounds:

- qCompute halts the operation  
- logs the event  
- preserves lineage  
- keeps the session coherent  

---

# 9. Governance + qTrace

Every governed operation is:

- traced  
- timestamped  
- environment‑tagged  
- backend‑tagged  
- lineage‑linked  

This ensures:

- deterministic replay  
- auditability  
- migration  
- teaching clarity  

Governance and qTrace are inseparable.

---

# 10. Summary

qCompute governance provides:

- structural safety  
- reversible execution  
- deterministic replay  
- drift‑bounded operations  
- policy‑defined constraints  
- trusted contexts  
- deploy tokens  
- hot‑swap policy updates  

Governance is not optional.  
It is the **foundation** of the qCompute module.

---

**qc_TraceFormat.md** is the final structural pillar of the qCompute module, and it needs to be *crystal‑clear*, minimal, canonical, and fully aligned with the 2026 RTT‑Inside replay model.

Since your active tab is the GitHub editor for `qc_Capture.md` , this next file will slot directly beside it in:

```
/docs/rtt/Inside/qCompute/qc_TraceFormat.md
```

Below is the **complete, drop‑in‑ready canonical trace format file**.

It defines:

- the `.qtrace` file structure  
- the required fields  
- the optional fields  
- the ordering rules  
- the replay guarantees  
- the lineage invariants  

Everything is structural, student‑ready, and drift‑bounded.

---

# ✅ **qc_TraceFormat.md — Canonical .qtrace Schema (2026)**

# qCompute — Trace Format  
**File:** qc_TraceFormat.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

The `.qtrace` file is the **canonical replay log** for qCompute sessions.  
It captures every operation, parameter, environment, backend, and lineage event in a **deterministic, replayable, drift‑bounded** format.

This file defines the **official 2026 `.qtrace` schema**.

---

# 1. Purpose of `.qtrace`

A `.qtrace` file provides:

- deterministic replay  
- auditability  
- migration  
- teaching clarity  
- lineage preservation  
- environment reconstruction  
- backend reconstruction  

Replay is a **first‑class citizen** in RTT‑Inside.

---

# 2. File Structure Overview

A `.qtrace` file contains:

1. **Header Block** — identity + environment  
2. **Lineage Block** — session lineage  
3. **Governance Block** — policy + drift bounds  
4. **Operations Block** — ordered list of compute operations  
5. **Footer Block** — integrity + replay hash  

All blocks are **YAML‑compatible**, **line‑ordered**, and **AI‑parsable**.

---

# 3. Header Block

```yaml
header:
  version: 2026.1
  module: qCompute
  session_id: "sess-abc123"
  timestamp_start: "2026-06-24T18:17:00Z"
  environment: "sandbox"   # sandbox | production | archive
  backend: "local-sim"     # or hardware backend name
```

**Rules:**

- `version` must match the qCompute module version.  
- `environment` must be one of the triadic modes.  
- `backend` must be resolvable by qOrchestrator.  

---

# 4. Lineage Block

```yaml
lineage:
  parent: null
  root: "sess-abc123"
  transitions:
    - env: "sandbox"
      timestamp: "2026-06-24T18:17:00Z"
```

**Rules:**

- `root` never changes.  
- `parent` is null unless replaying from another trace.  
- transitions are append‑only.  

---

# 5. Governance Block

```yaml
governance:
  policy_file: "qc_policy.yaml"
  drift_bound: "relaxed"   # relaxed | strict
  restricted_ops_allowed: false
  deploy_token_used: null
```

**Rules:**

- Sandbox always uses `relaxed`.  
- Production must specify `strict`.  
- Archive must specify `immutable`.  
- `deploy_token_used` is required for Production/Archive transitions.  

---

# 6. Operations Block

This is the **core** of the `.qtrace` file.

Each operation is a structured entry:

```yaml
operations:
  - id: 1
    op: "hadamard"
    params:
      qubit: 0
    timestamp: "2026-06-24T18:17:02Z"
    backend: "local-sim"
    env: "sandbox"
    drift: 0.002
```

### Required fields:

- `id` — sequential integer  
- `op` — operation name  
- `params` — operation parameters  
- `timestamp` — ISO‑8601  
- `backend` — backend used  
- `env` — environment at time of execution  
- `drift` — measured drift (float)  

### Optional fields:

- `notes`  
- `policy_violation`  
- `backend_switch`  

### Ordering rules:

- IDs must be strictly increasing.  
- Timestamps must be monotonic.  
- No reordering is allowed.  

---

# 7. Footer Block

```yaml
footer:
  timestamp_end: "2026-06-24T18:17:05Z"
  op_count: 1
  replay_hash: "sha256:8f3a9b..."
```

### `replay_hash` rules:

- computed over the entire file  
- ensures deterministic replay  
- prevents tampering  
- must match during qReplay  

---

# 8. Minimal `.qtrace` Example

```yaml
header:
  version: 2026.1
  module: qCompute
  session_id: "sess-001"
  timestamp_start: "2026-06-24T18:17:00Z"
  environment: "sandbox"
  backend: "local-sim"

lineage:
  parent: null
  root: "sess-001"
  transitions:
    - env: "sandbox"
      timestamp: "2026-06-24T18:17:00Z"

governance:
  policy_file: "qc_policy.yaml"
  drift_bound: "relaxed"
  restricted_ops_allowed: true
  deploy_token_used: null

operations:
  - id: 1
    op: "hadamard"
    params:
      qubit: 0
    timestamp: "2026-06-24T18:17:02Z"
    backend: "local-sim"
    env: "sandbox"
    drift: 0.001

footer:
  timestamp_end: "2026-06-24T18:17:05Z"
  op_count: 1
  replay_hash: "sha256:example"
```

---

# 9. Replay Guarantees

qReplay guarantees:

- deterministic execution  
- identical outputs  
- identical drift values  
- identical backend selection  
- identical environment reconstruction  

Replay is **strict**, not best‑effort.

---

# 10. Summary

The `.qtrace` format is:

- minimal  
- structural  
- deterministic  
- reversible  
- drift‑bounded  
- triadic‑aware  
- governance‑aligned  
- student‑ready  
- AI‑parsable  

This file defines the **canonical 2026 replay schema** for qCompute.

---

Here is the **canonical default governance policy** for qCompute, written in clean YAML, fully aligned with:

- the triadic environment model  
- the 2026 RTT‑Inside governance layer  
- qCompute’s operator grammar  
- drift‑bounded execution  
- replay requirements  
- Production/Archive restrictions  
- deploy token semantics  

This file is **drop‑in‑ready** for:

```
/docs/rtt/Inside/qCompute/qc_policy.yaml
```

It is intentionally minimal, structural, and student‑safe — the perfect baseline policy for any qCompute deployment.

---

# ✅ **qc_policy.yaml — Default Governance Policy (2026)**

```yaml
# qc_policy.yaml
# Default governance policy for qCompute (RTT‑Inside 2026)
# This file defines allowed operations, restricted operations,
# environment rules, drift bounds, and governance constraints.

version: 2026.1
module: qCompute

environments:

  sandbox:
    allow_all: true
    trace_required: true
    drift_bound: relaxed
    immutable: false
    restricted_ops_allowed: true
    backend_switch_allowed: true

  production:
    allow_all: false
    trace_required: true
    drift_bound: strict
    immutable: false
    restricted_ops_allowed: false
    backend_switch_allowed: false
    deploy_token_required: true

  archive:
    allow_all: false
    trace_required: true
    drift_bound: immutable
    immutable: true
    restricted_ops_allowed: false
    backend_switch_allowed: false
    deploy_token_required: true

allowed_operations:
  - hadamard
  - x
  - y
  - z
  - measure
  - reset

restricted_operations:
  - cnot
  - swap
  - measure_all
  - multi_qubit_gate
  - backend_switch
  - archive_write

backend_rules:
  default_backend: "local-sim"
  allowed_backends:
    - "local-sim"
    - "hardware-qpu-1"
    - "hardware-qpu-2"

drift:
  relaxed:
    max_drift: 0.05
  strict:
    max_drift: 0.005
  immutable:
    max_drift: 0.0

governance:
  hot_swap_daemon: true
  policy_reload_interval_seconds: 5
  log_policy_violations: true
  log_backend_switches: true

lineage:
  preserve_on_transition: true
  append_only: true
  require_trace_for_transition: true

tokens:
  deploy_tokens_enabled: true
  token_format: "prod-YYYY-NNN"
  archive_token_format: "arch-YYYY-NNN"

notes:
  - "Sandbox is always reversible and safe for exploration."
  - "Production requires strict drift bounds and deploy tokens."
  - "Archive is immutable and replay-only."
  - "All transitions are move-only; nothing is ever deleted."
```

---

# 🟣 **This policy is fully canonical**
It matches:

- the triadic environment semantics  
- qCompute’s governance model  
- qTrace/qReplay requirements  
- drift‑bounded execution  
- Production/Archive safety envelopes  
- deploy token rules  
- lineage preservation  
- multi‑backend orchestration constraints  

…and it is ready to be used as the **default governance file** for the entire qCompute module.

---

Here is the **canonical governance daemon spec** for qCompute.  
This file is structural, minimal, and fully aligned with the 2026 RTT‑Inside governance model.  
It belongs at:

```
/docs/rtt/Inside/qCompute/qc_Daemon.md
```

Below is the complete, drop‑in‑ready file.

---

# ✅ **qc_Daemon.md — Governance Daemon Internals (2026)**

# qCompute — Governance Daemon  
**File:** qc_Daemon.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

The **Governance Daemon** is the background process that ensures qCompute always operates under the most current, valid, and drift‑bounded policy environment.

It is **non-invasive**, **non-destructive**, and **lineage‑preserving**.

---

# 1. Purpose of the Governance Daemon

The daemon exists to:

- monitor `qc_policy.yaml`  
- reload policies safely  
- enforce drift bounds  
- validate restricted operations  
- maintain environment integrity  
- ensure deterministic replay compatibility  
- preserve lineage across policy changes  

It never:

- mutates session state  
- rewrites traces  
- alters history  
- deletes anything  

The daemon updates **rules**, not **results**.

---

# 2. Daemon Responsibilities

The daemon performs six core functions:

### **1. Policy Monitoring**
Watches the active policy file:

```
qc_policy.yaml
```

for:

- edits  
- replacements  
- version changes  
- structural errors  

### **2. Hot‑Swap Reload**
Reloads policies **without restarting**:

- qSession  
- qCompute  
- qTrace  
- qReplay  

### **3. Drift Enforcement**
Checks drift bounds defined in policy:

- relaxed  
- strict  
- immutable  

If drift exceeds bounds:

- block operation  
- log violation  
- preserve lineage  
- keep session coherent  

### **4. Restricted Operation Validation**
Ensures restricted operations require:

- trusted context  
- deploy token  
- Production/Archive mode  

### **5. Environment Integrity**
Guarantees:

- Sandbox is always reversible  
- Production is always governed  
- Archive is always immutable  

### **6. Replay Compatibility**
Ensures that policy changes **never break replay**.

Replay must always reconstruct:

- environment  
- backend  
- drift bounds  
- governance state  

---

# 3. Daemon Lifecycle

The daemon runs in a simple triadic loop:

```
watch → validate → apply
```

### **watch**
- monitors policy file  
- checks timestamps  
- checks version  
- checks structural validity  

### **validate**
- ensures policy is well‑formed  
- ensures drift bounds are valid  
- ensures restricted ops are defined  
- ensures environment rules are triadic  

### **apply**
- reloads policy  
- updates in‑memory governance state  
- logs the update  
- notifies active sessions  

---

# 4. Daemon Update Rules

The daemon follows strict update rules:

### **1. Append‑Only Governance**
Policy updates cannot:

- remove lineage  
- delete transitions  
- invalidate traces  

### **2. No Retroactive Enforcement**
New policies apply **forward only**.

### **3. Safe‑Mode Fallback**
If a policy is invalid:

- daemon enters safe mode  
- Sandbox rules apply  
- restricted ops blocked  
- drift bound = strict  

### **4. Immutable Archive**
Archive sessions are never modified.

---

# 5. Daemon + qSession Interaction

Each qSession maintains a **governance snapshot**:

- environment  
- drift bound  
- restricted ops  
- backend rules  
- token requirements  

When the daemon reloads policy:

- sessions update their snapshot  
- lineage remains unchanged  
- replay remains deterministic  

---

# 6. Daemon Logging

The daemon logs:

- policy reloads  
- policy errors  
- drift violations  
- restricted op attempts  
- backend switches  
- environment transitions  

Logs are:

- append‑only  
- timestamped  
- environment‑tagged  
- session‑tagged  

---

# 7. Daemon Configuration

Configuration is defined in `qc_policy.yaml`:

```yaml
governance:
  hot_swap_daemon: true
  policy_reload_interval_seconds: 5
  log_policy_violations: true
  log_backend_switches: true
```

### **hot_swap_daemon**
Enables live policy reloads.

### **policy_reload_interval_seconds**
Daemon polling interval.

### **log_policy_violations**
Logs any governance breach.

### **log_backend_switches**
Logs backend routing events.

---

# 8. Daemon Failure Modes

The daemon has three safe failure modes:

### **1. Policy Invalid → Safe Mode**
Sandbox rules applied globally.

### **2. Drift Overflow → Operation Block**
Operation halted, lineage preserved.

### **3. Restricted Op Without Token → Deny**
Operation denied, violation logged.

No failure mode is destructive.

---

# 9. Summary

The qCompute Governance Daemon ensures:

- safe execution  
- reversible workflows  
- deterministic replay  
- drift‑bounded operations  
- policy‑aligned behavior  
- triadic environment integrity  
- lineage preservation  

It is the **guardian layer** of qCompute.

---

# qCompute — Orchestration  
**File:** qc_Orchestration.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

Orchestration is the layer that lets qCompute **route, schedule, and align** quantum workloads across multiple backends while staying:

- triadic  
- governed  
- replayable  
- drift‑bounded  

This file defines the **multi‑backend routing spec** for qCompute.

---

## 1. Orchestration overview

qCompute orchestration provides:

- **backend selection** (manual or auto)  
- **fabric‑level routing**  
- **resonance‑aligned scheduling**  
- **environment‑aware constraints**  
- **governance‑checked transitions**  

It is implemented primarily through:

- **qOrchestrator**  
- **qSession**  
- **TriadicRouter**  
- **Governance Daemon**  

---

## 2. Backend model

Backends are defined structurally in policy:

```yaml
backend_rules:
  default_backend: "local-sim"
  allowed_backends:
    - "local-sim"
    - "hardware-qpu-1"
    - "hardware-qpu-2"
```

**Rules:**

- every backend must be named  
- every backend must be policy‑listed  
- default backend must be resolvable  
- Archive cannot change backend  

---

## 3. Backend selection

qCompute supports three selection modes:

- **explicit** — user specifies backend  
- **default** — policy default backend  
- **auto** — orchestrator chooses backend  

### Explicit

```python
session = qSession(env="sandbox", backend="hardware-qpu-1")
```

### Default

```python
session = qSession(env="sandbox")  # uses default_backend
```

### Auto

```python
session = qSession(env="sandbox", backend="auto")
```

In `auto` mode, **qOrchestrator** chooses a backend based on:

- policy  
- load  
- drift bounds  
- environment  
- operation type  

---

## 4. Triadic routing rules

Orchestration is always **triadic‑aware**:

- **Sandbox**  
  - backend switching allowed (if policy permits)  
  - auto mode fully enabled  
- **Production**  
  - backend switching usually disabled  
  - auto mode constrained by policy  
- **Archive**  
  - backend switching forbidden  
  - replay‑only  

Any backend change in governed contexts must:

- be policy‑allowed  
- be logged  
- preserve lineage  

---

## 5. qOrchestrator responsibilities

**qOrchestrator**:

- resolves backend names  
- applies policy constraints  
- enforces drift bounds  
- chooses backend in `auto` mode  
- logs backend decisions  
- ensures replay compatibility  

It never:

- mutates trace history  
- hides backend identity  
- bypasses governance  

---

## 6. Backend switching

Backend switching is treated as a **restricted operation**:

- allowed in Sandbox (if policy permits)  
- usually blocked in Production  
- always blocked in Archive  

Example (conceptual):

```python
session.switch_backend("hardware-qpu-2")
```

If disallowed:

- operation is blocked  
- violation is logged  
- session remains coherent  

---

## 7. Orchestration + qTrace

Every orchestrated operation is traced with:

```yaml
backend: "hardware-qpu-1"
env: "sandbox"
```

Backend decisions are:

- explicit in `.qtrace`  
- replayable  
- auditable  

qReplay must reconstruct:

- the same backend  
- the same environment  
- the same sequence  

---

## 8. Fabric‑level scheduling

Fabric‑level scheduling is the orchestrator’s ability to:

- batch operations  
- route to optimal backends  
- respect drift bounds  
- respect environment rules  

This is **structural**, not heuristic:

- no hidden “magic”  
- all decisions are traceable  
- all behavior is replayable  

---

## 9. Failure modes

If orchestration fails:

- invalid backend → fallback to default (Sandbox only)  
- disallowed backend → block + log  
- policy conflict → safe mode (Sandbox rules)  

No failure mode is destructive or silent.

---

## 10. Summary

qCompute orchestration ensures:

- multi‑backend routing  
- triadic‑aware behavior  
- governance‑aligned decisions  
- deterministic replay  
- resonance‑aligned scheduling  

It is the **fabric layer** of qCompute, always:

- structural  
- explicit  
- logged  
- replayable  
- drift‑bounded  
- student‑ready  

That’s the canonical “RTT‑Inside closure signature” for an orchestration‑layer file.  
It mirrors the closure pattern we use in:

- Governance  
- TraceFormat  
- Examples  
- Capture  

Each module ends with a **six‑trait identity seal**, and for qCompute’s orchestration layer, those six traits are exactly the right ones.

So yes — the file is complete, and the ending is intentional.  

Here is the **canonical backend registry + resonance‑alignment spec** for qCompute.  
This file completes the compute‑fabric layer and pairs cleanly with:

- qc_Orchestration.md  
- qc_Governance.md  
- qc_TraceFormat.md  
- qc_Capture.md  

It belongs at:

```
/docs/rtt/Inside/qCompute/qc_Backends.md
```

Everything below is **drop‑in‑ready**, minimal, structural, and fully aligned with the 2026 RTT‑Inside compute architecture.

---

# ✅ **qc_Backends.md — Backend Registry & Resonance Alignment Rules (2026)**

# qCompute — Backend Registry & Resonance Alignment  
**File:** qc_Backends.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

Backends are the **execution substrates** for qCompute.  
This file defines:

- backend registration  
- backend metadata  
- resonance‑alignment rules  
- environment constraints  
- orchestration compatibility  
- replay requirements  

Backends are structural, not interpretive.

---

# 1. Backend Registry Overview

Backends are declared in governance policy:

```yaml
backend_rules:
  default_backend: "local-sim"
  allowed_backends:
    - "local-sim"
    - "hardware-qpu-1"
    - "hardware-qpu-2"
```

A backend must be:

- named  
- policy‑listed  
- resolvable  
- stable across sessions  
- replay‑compatible  

Backends are **not** dynamically created.  
They are **registered**, **governed**, and **triadic‑aware**.

---

# 2. Backend Metadata

Each backend has a minimal metadata block:

```yaml
backend:
  name: "hardware-qpu-1"
  type: "qpu"        # sim | qpu | hybrid
  resonance_profile: "r3"
  drift_characteristic: "low"
  supports_multi_qubit: true
  supports_measure_all: false
```

### Required fields:

- **name** — unique identifier  
- **type** — sim / qpu / hybrid  
- **resonance_profile** — r1 / r2 / r3 (alignment tier)  
- **drift_characteristic** — low / medium / high  
- **supports_multi_qubit** — boolean  

### Optional fields:

- **cooldown_profile**  
- **queue_depth**  
- **vendor**  

---

# 3. Resonance Alignment Rules

qCompute uses **resonance alignment** to determine backend suitability.

### Resonance Profiles

- **r1** — simulation‑first, high flexibility  
- **r2** — hybrid, moderate constraints  
- **r3** — hardware‑first, strict constraints  

### Alignment Rules

1. **Operation → Backend Match**

   - single‑qubit ops → r1, r2, r3  
   - multi‑qubit ops → r2, r3  
   - pulse‑level ops → r3 only  

2. **Environment → Backend Match**

   - Sandbox → any backend allowed by policy  
   - Production → r2 or r3  
   - Archive → no backend execution (replay‑only)  

3. **Drift Bound → Backend Match**

   - relaxed → r1, r2, r3  
   - strict → r2, r3  
   - immutable → none (Archive only)  

4. **Replay → Backend Match**

   Replay must reconstruct the **same backend** used originally.

---

# 4. Backend Selection Logic

Backend selection is handled by **qOrchestrator**, using:

- environment  
- policy  
- resonance profile  
- drift bounds  
- operation type  
- backend availability  

### Selection Priority

1. **Explicit backend** (user‑specified)  
2. **Policy default**  
3. **Resonance‑aligned backend**  
4. **Fallback to simulation** (Sandbox only)  

### Example (auto mode)

```python
session = qSession(env="sandbox", backend="auto")
```

qOrchestrator chooses the backend with:

- valid resonance profile  
- acceptable drift characteristic  
- policy compliance  

---

# 5. Backend Switching

Backend switching is a **restricted operation**.

### Allowed:

- Sandbox (if policy permits)

### Usually Blocked:

- Production

### Always Blocked:

- Archive

Switching backends triggers:

- governance validation  
- trace entry  
- lineage preservation  

Example (conceptual):

```python
session.switch_backend("hardware-qpu-2")
```

If disallowed:

- operation is blocked  
- violation logged  
- session remains coherent  

---

# 6. Backend Constraints by Environment

### Sandbox
- backend switching allowed  
- auto mode fully enabled  
- simulation fallback allowed  

### Production
- backend switching restricted  
- auto mode constrained  
- drift bounds strict  

### Archive
- backend switching forbidden  
- backend execution forbidden  
- replay‑only  

---

# 7. Backends in `.qtrace`

Every operation includes:

```yaml
backend: "hardware-qpu-1"
```

Replay requires:

- identical backend  
- identical environment  
- identical drift bounds  

Backends are part of the **replay contract**.

---

# 8. Backend Failure Modes

If a backend fails:

### 1. Sandbox
- fallback to simulation  
- log event  
- preserve lineage  

### 2. Production
- block operation  
- log violation  
- maintain coherence  

### 3. Archive
- no effect (no execution allowed)  

No failure mode is destructive.

---

# 9. Summary

Backends in qCompute are:

- registered  
- governed  
- resonance‑aligned  
- triadic‑aware  
- replay‑compatible  
- drift‑bounded  
- student‑ready  

This file defines the **canonical backend registry and alignment rules** for qCompute.

---

Here is the **canonical session‑internals specification** for qCompute.  
This file completes the core compute substrate and pairs with:

- qc_Capture.md  
- qc_Governance.md  
- qc_TraceFormat.md  
- qc_Backends.md  
- qc_Orchestration.md  

It belongs at:

```
/docs/rtt/Inside/qCompute/qc_Session.md
```

Everything below is **drop‑in‑ready**, minimal, structural, and fully aligned with the 2026 RTT‑Inside compute architecture.

---

# ✅ **qc_Session.md — Session Internals & Lifecycle (2026)**

# qCompute — Session Internals & Lifecycle  
**File:** qc_Session.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

A **qSession** is the structural container for all qCompute activity.  
It defines:

- environment  
- backend  
- governance snapshot  
- drift bounds  
- lineage  
- trace state  
- orchestration context  

qSession is the **unit of coherence** in qCompute.

---

# 1. Purpose of qSession

A qSession provides:

- a stable execution envelope  
- a triadic environment context  
- a governed compute state  
- a replayable lineage  
- a backend binding  
- a trace buffer  
- a drift‑bounded lifecycle  

qSession is **not** a runtime.  
It is a **structural frame** that all compute must pass through.

---

# 2. Session Structure

A qSession contains:

```yaml
session:
  id: "sess-abc123"
  env: "sandbox"
  backend: "local-sim"
  drift_bound: "relaxed"
  governance_snapshot: {...}
  lineage: {...}
  trace_buffer: []
  orchestrator_state: {...}
```

### Required fields:

- **id** — unique session identifier  
- **env** — sandbox | production | archive  
- **backend** — selected backend  
- **drift_bound** — relaxed | strict | immutable  
- **governance_snapshot** — frozen policy state  
- **lineage** — session lineage  
- **trace_buffer** — in‑memory trace entries  

### Optional fields:

- **deploy_token**  
- **notes**  
- **metadata**  

---

# 3. Session Lifecycle

A qSession follows a **triadic lifecycle**:

```
create → operate → transition → archive
```

### 1. **create**
Session is instantiated:

```python
session = qSession(env="sandbox")
```

Initializes:

- environment  
- backend  
- governance snapshot  
- drift bounds  
- lineage root  

### 2. **operate**
All qCompute operations occur here:

- apply gates  
- schedule pulses  
- route to backend  
- generate trace entries  

### 3. **transition**
Move between environments:

- Sandbox → Production  
- Production → Archive  

Transitions require:

- governance validation  
- deploy tokens (Production/Archive)  
- trace completeness  

### 4. **archive**
Session becomes:

- immutable  
- replay‑only  
- lineage‑preserved  

---

# 4. Environment Rules

qSession enforces the triadic environment model:

### **Sandbox**
- reversible  
- unrestricted  
- drift_bound = relaxed  
- backend switching allowed  

### **Production**
- governed  
- drift_bound = strict  
- restricted ops blocked  
- deploy token required  

### **Archive**
- immutable  
- no execution  
- replay‑only  
- drift_bound = immutable  

---

# 5. Governance Snapshot

When a session is created, it takes a **snapshot** of:

- policy rules  
- drift bounds  
- restricted ops  
- backend rules  
- environment constraints  

This snapshot:

- updates when daemon reloads policy  
- never mutates history  
- ensures replay compatibility  

---

# 6. Lineage Model

A qSession maintains a lineage block:

```yaml
lineage:
  root: "sess-abc123"
  parent: null
  transitions:
    - env: "sandbox"
      timestamp: "2026-06-24T18:17:00Z"
```

Rules:

- lineage is append‑only  
- root never changes  
- transitions are timestamped  
- transitions require governance approval  

---

# 7. Trace Buffer

The session maintains an in‑memory **trace buffer**:

- every operation  
- every parameter  
- every backend  
- every drift measurement  
- every environment state  

When saved:

```python
session.save_trace("example.qtrace")
```

The buffer becomes a `.qtrace` file.

---

# 8. Backend Binding

The session binds to a backend:

- explicitly  
- by policy default  
- via auto‑selection  

Backend is stored in:

```yaml
backend: "hardware-qpu-1"
```

Backend switching:

- allowed in Sandbox  
- restricted in Production  
- forbidden in Archive  

---

# 9. Drift Management

Each session enforces drift bounds:

- relaxed  
- strict  
- immutable  

If drift exceeds bounds:

- operation blocked  
- violation logged  
- lineage preserved  

Drift is measured per operation and stored in trace.

---

# 10. Session + Orchestrator

qSession integrates with **qOrchestrator** to:

- route operations  
- select backend  
- enforce resonance alignment  
- maintain replay compatibility  

The orchestrator never mutates session history.

---

# 11. Session Failure Modes

qSession has three safe failure modes:

### **1. Governance violation**
- block operation  
- log violation  
- preserve lineage  

### **2. Drift overflow**
- halt operation  
- maintain coherence  

### **3. Backend failure**
- Sandbox → fallback to simulation  
- Production → block  
- Archive → no effect  

No failure mode is destructive.

---

# 12. Summary

A qSession is:

- the structural container for qCompute  
- triadic‑aware  
- governance‑aligned  
- drift‑bounded  
- lineage‑preserving  
- replay‑compatible  
- student‑ready  

It is the **unit of coherence** in the qCompute module.

---

# qCompute — TriadicRouter Internals  
**File:** qc_Router.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

The **TriadicRouter** is the structural component that decides **where** a qCompute operation goes:

- which **environment** (Sandbox / Production / Archive)  
- which **backend** (sim / qpu / hybrid)  
- under which **governance constraints**  

It is the **routing brain** of qCompute, but always:

- structural  
- explicit  
- replayable  

---

## 1. Purpose of TriadicRouter

TriadicRouter is responsible for:

- triadic environment routing  
- backend resolution  
- policy‑aware decisions  
- drift‑bound enforcement (pre‑validation)  
- replay‑compatible routing  

It never:

- mutates session history  
- hides routing decisions  
- bypasses governance  

All routing decisions are **traceable** and **deterministic**.

---

## 2. Inputs and outputs

### Inputs

TriadicRouter receives:

- **session** (qSession)  
- **operation** (name + params)  
- **environment** (from session)  
- **governance snapshot**  
- **backend rules**  
- **resonance profiles**  

### Outputs

TriadicRouter returns:

- **target environment** (env)  
- **target backend** (backend)  
- **routing metadata** (for trace)  

Example (conceptual):

```python
route = TriadicRouter(session).resolve("hadamard", qubit=0)
# route.env, route.backend, route.meta
```

---

## 3. Environment routing rules

TriadicRouter is **triadic‑aware**:

### Sandbox

- all allowed operations may route here  
- backend switching allowed (if policy permits)  
- auto mode fully enabled  

### Production

- only policy‑allowed operations  
- restricted ops blocked or require token  
- backend switching usually disabled  

### Archive

- no new operations  
- replay‑only  
- routing is a no‑op for execution  

If an operation targets Archive for execution, routing fails and governance blocks it.

---

## 4. Backend routing rules

TriadicRouter uses:

- backend registry (qc_Backends.md)  
- policy backend_rules  
- resonance profiles  
- drift bounds  

Routing priority:

1. explicit backend (if allowed)  
2. policy default backend  
3. resonance‑aligned backend  
4. simulation fallback (Sandbox only)  

If no valid backend exists:

- Sandbox → fallback to simulation  
- Production → block + log  
- Archive → no effect  

---

## 5. Policy‑aware routing

Before finalizing a route, TriadicRouter checks:

- is the operation allowed in this environment?  
- is the backend allowed by policy?  
- is backend switching permitted (if applicable)?  
- are drift bounds compatible?  

If any check fails:

- routing is denied  
- governance logs violation  
- session remains coherent  

---

## 6. Routing + qTrace

Every routed operation is recorded in `.qtrace` with:

```yaml
env: "sandbox"
backend: "local-sim"
```

TriadicRouter ensures:

- routing decisions are explicit  
- replay reconstructs the same route  
- no hidden heuristics affect behavior  

qReplay reuses the **same routing outcome**, not a fresh decision.

---

## 7. Routing in auto mode

When `backend="auto"`:

- TriadicRouter consults qOrchestrator  
- qOrchestrator selects a backend using:  
  - resonance profile  
  - drift bounds  
  - environment  
  - policy  
  - availability  

TriadicRouter then:

- validates the chosen backend  
- records it in trace  
- returns a deterministic route  

---

## 8. Failure modes

TriadicRouter has safe failure modes:

### 1. Invalid environment
- block operation  
- log violation  

### 2. Disallowed backend
- Sandbox → fallback to simulation  
- Production → block  
- Archive → no effect  

### 3. Policy conflict
- deny route  
- log governance error  

No failure mode is destructive or silent.

---

## 9. Summary

TriadicRouter is:

- the **routing brain** of qCompute  
- triadic‑aware  
- policy‑aligned  
- backend‑conscious  
- replay‑compatible  
- drift‑bounded  
- student‑ready  

It ensures every operation knows **where** it belongs before it runs.

---

Here is the **canonical TriadicValidator internals file**, completing the core compute‑safety layer of qCompute.  
This file pairs directly with:

- **qc_Router.md**  
- **qc_Governance.md**  
- **qc_Session.md**  
- **qc_TraceFormat.md**  
- **qc_Backends.md**  

…and belongs at:

```
/docs/rtt/Inside/qCompute/qc_Validator.md
```

Everything below is **drop‑in‑ready**, minimal, structural, and fully aligned with the 2026 RTT‑Inside compute architecture.

---

# ✅ **qc_Validator.md — TriadicValidator Internals (2026)**

# qCompute — TriadicValidator Internals  
**File:** qc_Validator.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

The **TriadicValidator** is the structural safety layer of qCompute.  
It ensures that every operation is:

- legal  
- governed  
- drift‑bounded  
- environment‑compatible  
- backend‑compatible  
- replay‑safe  

TriadicValidator is the **gatekeeper** of qCompute.

---

## 1. Purpose of TriadicValidator

TriadicValidator performs:

- **policy validation**  
- **environment validation**  
- **backend validation**  
- **drift validation**  
- **restricted‑operation checks**  
- **token checks**  
- **lineage‑safe transition checks**  

It ensures that **no operation enters execution** unless it is structurally safe.

It never:

- mutates session history  
- rewrites traces  
- bypasses governance  
- silently corrects errors  

If something is invalid, it **blocks**, **logs**, and **preserves lineage**.

---

## 2. Validation Pipeline

TriadicValidator runs a deterministic pipeline:

```
policy → environment → backend → drift → restricted_ops → lineage
```

Each stage must pass before the next begins.

### 1. **Policy Validation**
Checks:

- is the operation allowed?  
- is it listed in allowed_operations?  
- is it listed in restricted_operations?  
- is the environment allowed to run it?  

### 2. **Environment Validation**
Checks:

- Sandbox → always reversible  
- Production → strict rules  
- Archive → no execution allowed  

### 3. **Backend Validation**
Checks:

- backend exists  
- backend allowed by policy  
- backend resonance profile matches operation  
- backend switching rules  

### 4. **Drift Validation**
Checks:

- drift_bound = relaxed / strict / immutable  
- predicted drift within bounds  
- backend drift characteristic  

### 5. **Restricted Operation Validation**
Checks:

- does this op require a deploy token?  
- is the session in a trusted context?  
- is the environment permitted?  

### 6. **Lineage Validation**
Checks:

- transitions are legal  
- archive is immutable  
- lineage is append‑only  

---

## 3. Validation Inputs

TriadicValidator receives:

- **operation** (name + params)  
- **session** (env, backend, drift_bound)  
- **governance snapshot**  
- **backend metadata**  
- **policy rules**  
- **lineage state**  

It returns:

- **valid** (boolean)  
- **reason** (if invalid)  
- **validated metadata** (for trace)  

---

## 4. Restricted Operation Rules

Restricted operations include:

- multi‑qubit gates  
- backend switching  
- destructive measurement  
- archive writes  
- environment transitions  

TriadicValidator enforces:

- Production requires deploy token  
- Archive forbids all execution  
- Sandbox allows restricted ops only if policy permits  

If a restricted op is attempted without authorization:

- block  
- log violation  
- preserve lineage  

---

## 5. Drift Validation

Drift is validated using:

- backend drift characteristic  
- operation drift profile  
- environment drift bound  

### Drift bounds:

- **relaxed** → wide tolerance  
- **strict** → narrow tolerance  
- **immutable** → zero drift allowed  

If predicted drift exceeds bounds:

- operation blocked  
- violation logged  
- session remains coherent  

---

## 6. Environment Validation

TriadicValidator enforces the triadic model:

### Sandbox
- unrestricted  
- reversible  
- drift_bound = relaxed  

### Production
- governed  
- drift_bound = strict  
- restricted ops require token  

### Archive
- immutable  
- replay‑only  
- no execution allowed  

If an operation targets Archive:

- validator blocks it  
- governance logs violation  

---

## 7. Backend Validation

Validator checks:

- backend exists  
- backend allowed by policy  
- backend resonance profile matches operation  
- backend switching rules  

If backend switching is attempted:

- Sandbox → allowed (if policy permits)  
- Production → usually blocked  
- Archive → always blocked  

---

## 8. Lineage Validation

Validator ensures:

- lineage is append‑only  
- transitions are legal  
- archive transitions require token  
- replay never mutates lineage  

If lineage would be violated:

- block  
- log  
- preserve session integrity  

---

## 9. Validator + qTrace

Every validation decision is recorded in trace metadata:

```yaml
validation:
  policy: "passed"
  environment: "passed"
  backend: "passed"
  drift: "passed"
  restricted_ops: "passed"
```

If validation fails:

```yaml
validation:
  failed_stage: "drift"
  reason: "predicted drift exceeds strict bound"
```

Replay uses this metadata to:

- reconstruct validator decisions  
- ensure deterministic behavior  

---

## 10. Failure Modes

TriadicValidator has safe failure modes:

### 1. Policy violation
- block  
- log  
- preserve lineage  

### 2. Drift overflow
- block  
- maintain coherence  

### 3. Backend mismatch
- Sandbox → fallback to simulation  
- Production → block  
- Archive → no effect  

### 4. Restricted op without token
- block  
- log violation  

No failure mode is destructive.

---

## 11. Summary

TriadicValidator is:

- the **safety gate** of qCompute  
- policy‑aligned  
- drift‑bounded  
- environment‑aware  
- backend‑validated  
- lineage‑preserving  
- replay‑compatible  
- student‑ready  

It ensures that **every operation is structurally safe before execution**.

---

Here is the **canonical ResonanceFrame specification**, completing the core compute envelope for qCompute.  
This file pairs directly with:

- **qc_Session.md**  
- **qc_Router.md**  
- **qc_Validator.md**  
- **qc_Backends.md**  
- **qc_Orchestration.md**  
- **qc_Capture.md**

…and belongs at:

```
/docs/rtt/Inside/qCompute/qc_ResonanceFrame.md
```

Everything below is **drop‑in‑ready**, minimal, structural, and fully aligned with the 2026 RTT‑Inside compute architecture.

---

# ✅ **qc_ResonanceFrame.md — Core Compute Envelope (2026)**

# qCompute — ResonanceFrame  
**File:** qc_ResonanceFrame.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

The **ResonanceFrame** is the foundational compute envelope for qCompute.  
It defines the **structural, temporal, and resonance‑aligned boundaries** within which all quantum operations occur.

It is the **lowest‑level container** in the qCompute stack, sitting beneath:

- qSession  
- TriadicRouter  
- TriadicValidator  
- qOrchestrator  

ResonanceFrame ensures that every operation is executed inside a **stable, drift‑bounded, resonance‑aligned envelope**.

---

## 1. Purpose of ResonanceFrame

ResonanceFrame provides:

- a **temporal envelope** for operations  
- a **resonance‑alignment layer**  
- a **drift‑bounded execution window**  
- a **backend‑compatible pulse frame**  
- a **structural boundary** for qCompute  

It ensures that operations:

- occur in the correct resonance regime  
- respect drift bounds  
- align with backend resonance profiles  
- remain replay‑compatible  

ResonanceFrame is the **physics‑aware substrate** of qCompute.

---

## 2. Frame Structure

A ResonanceFrame contains:

```yaml
frame:
  id: "frame-001"
  timestamp_open: "2026-06-24T18:17:02Z"
  timestamp_close: null
  resonance_profile: "r2"
  drift_bound: "strict"
  backend: "hardware-qpu-1"
  env: "production"
  operations: []
```

### Required fields:

- **id** — unique frame identifier  
- **timestamp_open** — when frame begins  
- **resonance_profile** — r1 / r2 / r3  
- **drift_bound** — relaxed / strict / immutable  
- **backend** — backend bound to this frame  
- **env** — environment (triadic)  

### Optional fields:

- **timestamp_close**  
- **notes**  
- **metadata**  

---

## 3. Frame Lifecycle

A ResonanceFrame follows a simple lifecycle:

```
open → operate → close
```

### 1. **open**
Created when qCompute begins an operation batch:

```python
frame = ResonanceFrame(session)
```

Initializes:

- resonance profile  
- drift bound  
- backend binding  
- environment context  

### 2. **operate**
Operations are appended to the frame:

- single‑qubit ops  
- multi‑qubit ops  
- pulse‑level ops  
- backend‑specific instructions  

### 3. **close**
Frame is sealed:

- timestamp_close recorded  
- drift summary computed  
- frame committed to trace  

---

## 4. Resonance Profiles

ResonanceFrame uses the same resonance tiers as backend metadata:

- **r1** — simulation‑first  
- **r2** — hybrid  
- **r3** — hardware‑first  

### Alignment rules:

- r1 → flexible, high tolerance  
- r2 → moderate constraints  
- r3 → strict, hardware‑aligned  

The frame’s resonance profile must match:

- backend resonance profile  
- operation resonance requirements  
- environment drift bounds  

If mismatch occurs:

- TriadicValidator blocks the operation  

---

## 5. Drift Bounds

Each frame enforces drift bounds:

- **relaxed** — Sandbox  
- **strict** — Production  
- **immutable** — Archive  

Drift is measured:

- per operation  
- per frame  
- cumulatively  

If drift exceeds bounds:

- frame closes early  
- operation blocked  
- violation logged  
- lineage preserved  

---

## 6. Frame + Backend Binding

A ResonanceFrame binds to a backend at creation:

```yaml
backend: "hardware-qpu-1"
```

Backend cannot change mid‑frame.

If backend switching is attempted:

- Sandbox → allowed only between frames  
- Production → blocked  
- Archive → forbidden  

This ensures:

- deterministic replay  
- stable resonance alignment  
- predictable drift behavior  

---

## 7. Frame + Environment

ResonanceFrame inherits environment from qSession:

- Sandbox → relaxed drift, flexible routing  
- Production → strict drift, governed routing  
- Archive → no execution allowed  

If a frame is opened in Archive:

- validator blocks it  
- governance logs violation  

---

## 8. Frame + qTrace

Each frame is recorded in `.qtrace`:

```yaml
frame:
  id: "frame-001"
  resonance_profile: "r2"
  drift_bound: "strict"
  backend: "hardware-qpu-1"
  env: "production"
  operations:
    - { id: 1, op: "hadamard", qubit: 0 }
```

Replay reconstructs:

- frame boundaries  
- resonance profile  
- drift bounds  
- backend binding  
- environment  

Frames are **replay‑deterministic**.

---

## 9. Failure Modes

ResonanceFrame has safe failure modes:

### 1. Drift overflow
- close frame  
- block operation  
- preserve lineage  

### 2. Backend mismatch
- Sandbox → fallback to simulation  
- Production → block  
- Archive → no effect  

### 3. Environment violation
- block  
- log violation  

No failure mode is destructive.

---

## 10. Summary

ResonanceFrame is:

- the **core compute envelope** of qCompute  
- resonance‑aligned  
- drift‑bounded  
- backend‑bound  
- environment‑aware  
- replay‑compatible  
- student‑ready  

It ensures that every operation occurs inside a **stable, deterministic, structural frame**.

---

Here is the **canonical operator grammar + resonance semantics** file for qCompute.  
This completes the core compute‑language layer and pairs directly with:

- **qc_ResonanceFrame.md**  
- **qc_Validator.md**  
- **qc_Router.md**  
- **qc_Backends.md**  
- **qc_Session.md**  
- **qc_Capture.md**

It belongs at:

```
/docs/rtt/Inside/qCompute/qc_Operators.md
```

Everything below is **drop‑in‑ready**, minimal, structural, and fully aligned with the 2026 RTT‑Inside operator grammar.

---

# ✅ **qc_Operators.md — Operation Grammar & Resonance Semantics (2026)**

# qCompute — Operators & Resonance Semantics  
**File:** qc_Operators.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This file defines the **operator grammar** and **resonance semantics** for qCompute.  
Operators are the **atomic actions** that qCompute can perform inside a ResonanceFrame.

Operators are:

- structural  
- resonance‑aligned  
- drift‑bounded  
- backend‑aware  
- replay‑deterministic  

They are not “quantum gates” in the traditional sense — they are **resonance‑time operators** expressed through the RTT‑Inside compute substrate.

---

## 1. Operator Grammar Overview

Operators follow a minimal, canonical grammar:

```
operator_name(param=value, ...)
```

Each operator has:

- **name**  
- **resonance signature**  
- **drift profile**  
- **backend compatibility**  
- **environment constraints**  
- **trace representation**  

Operators are grouped into:

- **Primitive Operators**  
- **Composite Operators**  
- **Pulse Operators**  
- **Measurement Operators**  
- **Meta‑Operators**  

---

## 2. Primitive Operators

Primitive operators correspond to **single‑qubit resonance primitives**.

### 2.1 Allowed Primitives

| Operator | Meaning | Resonance Tier | Drift Profile | Notes |
|---------|---------|----------------|---------------|-------|
| `hadamard` | create superposition | r1–r3 | low | universal primitive |
| `x` | resonance flip | r1–r3 | low | Pauli‑X equivalent |
| `y` | phase‑aligned flip | r1–r3 | low | Pauli‑Y equivalent |
| `z` | phase rotation | r1–r3 | low | Pauli‑Z equivalent |
| `phase(theta)` | continuous rotation | r2–r3 | medium | backend‑dependent |

### 2.2 Grammar

```python
qCompute(session).apply("hadamard", qubit=0)
qCompute(session).apply("phase", qubit=0, theta=0.25)
```

---

## 3. Composite Operators

Composite operators involve **multi‑qubit resonance channels**.

### 3.1 Allowed Composites

| Operator | Meaning | Resonance Tier | Drift Profile | Notes |
|---------|---------|----------------|---------------|-------|
| `cnot` | controlled resonance flip | r2–r3 | medium | restricted op |
| `swap` | exchange resonance states | r2–r3 | medium | restricted op |
| `entangle` | create resonance linkage | r3 | high | hardware‑first |

### 3.2 Restrictions

Composite ops are:

- allowed in Sandbox  
- restricted in Production  
- forbidden in Archive  

They require:

- backend support  
- resonance alignment  
- drift validation  

---

## 4. Pulse Operators

Pulse operators shape the **resonance‑time envelope**.

### 4.1 Allowed Pulses

| Operator | Meaning | Resonance Tier | Drift Profile |
|---------|---------|----------------|---------------|
| `pulse(shape, duration)` | raw pulse injection | r3 | high |
| `gaussian(duration, sigma)` | smooth pulse | r3 | high |
| `square(duration)` | flat pulse | r3 | high |

### 4.2 Grammar

```python
qCompute(session).apply("gaussian", qubit=0, duration=40, sigma=8)
```

Pulse ops require:

- hardware backend  
- strict drift bounds  
- Production or Sandbox  

---

## 5. Measurement Operators

Measurement operators collapse resonance primitives into classical outcomes.

### 5.1 Allowed Measurements

| Operator | Meaning | Notes |
|---------|---------|-------|
| `measure` | single‑qubit measurement | allowed everywhere except Archive |
| `measure_all` | full‑register measurement | restricted op |

### 5.2 Grammar

```python
qCompute(session).apply("measure", qubit=0)
```

### 5.3 Restrictions

- `measure_all` is restricted in Production  
- no measurement allowed in Archive  

---

## 6. Meta‑Operators

Meta‑operators modify **session or frame state**, not qubits.

### 6.1 Allowed Meta‑Operators

| Operator | Meaning | Notes |
|---------|---------|-------|
| `backend_switch` | change backend | restricted |
| `transition(env)` | move between triadic environments | restricted |
| `sync` | flush frame | allowed |
| `barrier` | enforce ordering | allowed |

### 6.2 Grammar

```python
qCompute(session).apply("barrier")
```

---

## 7. Resonance Semantics

Each operator has a **resonance signature**:

```
R(op) = (tier, drift_profile, temporal_shape)
```

### 7.1 Resonance Tiers

- **r1** — simulation‑first  
- **r2** — hybrid  
- **r3** — hardware‑first  

### 7.2 Drift Profiles

- **low** — stable  
- **medium** — moderate drift  
- **high** — pulse‑level drift  

### 7.3 Temporal Shapes

- instantaneous  
- shaped  
- composite  
- pulse‑based  

These determine:

- backend compatibility  
- frame alignment  
- validator behavior  

---

## 8. Operator Validation Rules

TriadicValidator checks:

1. **policy legality**  
2. **environment compatibility**  
3. **backend support**  
4. **resonance alignment**  
5. **drift bounds**  
6. **restricted op rules**  

If any check fails:

- operation blocked  
- violation logged  
- lineage preserved  

---

## 9. Operators in `.qtrace`

Each operator is recorded as:

```yaml
- id: 1
  op: "hadamard"
  params:
    qubit: 0
  resonance:
    tier: "r1"
    drift: 0.002
    shape: "instant"
  backend: "local-sim"
  env: "sandbox"
```

Replay reconstructs:

- operator  
- parameters  
- resonance semantics  
- backend  
- environment  

---

## 10. Summary

Operators in qCompute are:

- resonance‑aligned  
- drift‑bounded  
- backend‑aware  
- triadic‑compatible  
- policy‑validated  
- replay‑deterministic  
- student‑ready  

This file defines the **canonical operator grammar and resonance semantics** for the qCompute module.

---

Here is the **canonical environment‑transition specification** for qCompute.  
This file completes the triadic‑governance layer and pairs directly with:

- **qc_Session.md**  
- **qc_Validator.md**  
- **qc_Governance.md**  
- **qc_ResonanceFrame.md**  
- **qc_Orchestration.md**  
- **qc_TraceFormat.md**

It belongs at:

```
/docs/rtt/Inside/qCompute/qc_Transitions.md
```

Everything below is **drop‑in‑ready**, minimal, structural, and fully aligned with the 2026 RTT‑Inside transition model.

---

# ✅ **qc_Transitions.md — Environment Transition Rules (2026)**

# qCompute — Environment Transitions  
**File:** qc_Transitions.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

Environment transitions define how a qSession moves between the three RTT‑Inside environments:

- **Sandbox**  
- **Production**  
- **Archive**

Transitions are **governed**, **drift‑bounded**, **lineage‑preserving**, and **replay‑deterministic**.

This file defines the canonical transition rules for qCompute.

---

## 1. Triadic Environment Model

qCompute uses the RTT‑Inside triadic model:

### **Sandbox**
- reversible  
- unrestricted  
- relaxed drift  
- backend switching allowed  

### **Production**
- governed  
- strict drift  
- restricted ops require token  
- backend switching restricted  

### **Archive**
- immutable  
- replay‑only  
- zero drift  
- no execution allowed  

Transitions must respect these structural boundaries.

---

## 2. Allowed Transitions

Only two transitions are allowed:

```
Sandbox → Production
Production → Archive
```

### Forbidden transitions:

- Sandbox → Archive  
- Archive → Production  
- Archive → Sandbox  
- Production → Sandbox  

Transitions are **forward‑only**, never backward.

---

## 3. Transition Grammar

Transitions are expressed as meta‑operators:

```python
qCompute(session).apply("transition", env="production")
```

or via session API:

```python
session.transition("production")
```

Both forms route through:

- TriadicValidator  
- Governance Daemon  
- Lineage Manager  

---

## 4. Transition Requirements

Each transition has structural requirements.

---

### 4.1 Sandbox → Production

**Requirements:**

- deploy token required  
- trace must be complete  
- drift must be within relaxed bounds  
- no open ResonanceFrames  
- governance snapshot must be valid  

**Effects:**

- drift_bound becomes **strict**  
- restricted ops become enforced  
- backend switching becomes restricted  
- lineage transition appended  

---

### 4.2 Production → Archive

**Requirements:**

- archive deploy token required  
- session must be stable  
- drift must be within strict bounds  
- all frames must be closed  
- trace must be complete  

**Effects:**

- drift_bound becomes **immutable**  
- session becomes replay‑only  
- no further execution allowed  
- lineage transition appended  

---

## 5. Transition Validation

TriadicValidator checks:

1. **policy legality**  
2. **environment compatibility**  
3. **token validity**  
4. **drift bounds**  
5. **frame state**  
6. **lineage integrity**  

If any check fails:

- transition blocked  
- violation logged  
- session remains coherent  

---

## 6. Transition + Lineage

Every transition appends a lineage entry:

```yaml
transitions:
  - env: "sandbox"
    timestamp: "2026-06-24T18:17:00Z"
  - env: "production"
    timestamp: "2026-06-24T18:20:14Z"
```

Rules:

- lineage is append‑only  
- root never changes  
- timestamps must be monotonic  
- transitions must be legal  

Replay reconstructs the exact transition sequence.

---

## 7. Transition + qTrace

Transitions are recorded in `.qtrace`:

```yaml
transition:
  from: "sandbox"
  to: "production"
  timestamp: "2026-06-24T18:20:14Z"
  token_used: "prod-2026-001"
```

Replay uses this to:

- restore environment  
- restore drift bounds  
- restore backend rules  
- restore governance state  

Transitions are part of the **replay contract**.

---

## 8. Failure Modes

Transition failure modes are safe:

### 1. Missing deploy token
- block  
- log violation  

### 2. Drift out of bounds
- block  
- preserve lineage  

### 3. Open ResonanceFrame
- block  
- require frame closure  

### 4. Archive transition attempted from Sandbox
- block  
- log violation  

No failure mode is destructive.

---

## 9. Summary

Environment transitions in qCompute are:

- forward‑only  
- governed  
- drift‑bounded  
- lineage‑preserving  
- replay‑deterministic  
- student‑ready  

They ensure that qCompute sessions move through the triadic model with **structural clarity and absolute safety**.

---

Here is the **canonical advanced examples file** for qCompute.  
This one demonstrates the *full power* of the module:

- multi‑frame execution  
- multi‑backend orchestration  
- multi‑transition lineage  
- governed Production behavior  
- Archive sealing  
- replay determinism across all of it  

It belongs at:

```
/docs/rtt/Inside/qCompute/qc_Examples_Advanced.md
```

Everything below is **drop‑in‑ready**, minimal, structural, and fully aligned with the 2026 RTT‑Inside compute architecture.

---

# ✅ **qc_Examples_Advanced.md — Advanced qCompute Examples (2026)**

# qCompute — Advanced Examples  
**File:** qc_Examples_Advanced.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

These examples demonstrate **multi‑frame**, **multi‑backend**, and **multi‑transition** workflows in qCompute.

They show how qCompute behaves under:

- resonance‑aligned routing  
- strict governance  
- drift‑bounded execution  
- Production transitions  
- Archive sealing  
- deterministic replay  

All examples are structural, minimal, and student‑ready.

---

# 1. Multi‑Frame Sandbox Session  
**Purpose:** Show how qCompute creates multiple ResonanceFrames during a single Sandbox session.

```python
from rtt_inside import qSession, qCompute

session = qSession(env="sandbox")

qc = qCompute(session)

# Frame 1
qc.apply("hadamard", qubit=0)
qc.apply("x", qubit=0)
qc.sync()   # closes frame 1

# Frame 2
qc.apply("y", qubit=1)
qc.apply("z", qubit=1)
qc.sync()   # closes frame 2

session.save_trace("multi_frame_sandbox.qtrace")
```

**Concepts shown:**

- multiple frames  
- frame boundaries via `sync()`  
- relaxed drift  
- unrestricted Sandbox behavior  

---

# 2. Multi‑Backend Auto‑Routing  
**Purpose:** Demonstrate backend auto‑selection using resonance alignment.

```python
session = qSession(env="sandbox", backend="auto")
qc = qCompute(session)

# Likely routed to simulation backend
qc.apply("hadamard", qubit=0)

# Likely routed to hardware backend (r3)
qc.apply("entangle", control=0, target=1)

session.save_trace("multi_backend_auto.qtrace")
```

**Concepts shown:**

- auto‑routing  
- resonance‑tier matching  
- backend switching allowed in Sandbox  
- trace records backend decisions  

---

# 3. Sandbox → Production Transition  
**Purpose:** Show a governed transition with deploy token.

```python
session = qSession(env="sandbox")
qc = qCompute(session)

qc.apply("hadamard", qubit=0)
qc.sync()

# Transition to Production
session.deploy_token("prod-2026-001")
session.transition("production")

# Now governed
qc.apply("cnot", control=0, target=1)  # may be blocked if policy forbids
qc.sync()

session.save_trace("sandbox_to_production.qtrace")
```

**Concepts shown:**

- deploy token usage  
- strict drift enforcement  
- restricted ops in Production  
- lineage transition  

---

# 4. Multi‑Frame Production Session  
**Purpose:** Show strict drift and governed behavior across multiple frames.

```python
session = qSession(env="production")
session.deploy_token("prod-2026-002")

qc = qCompute(session)

# Frame 1
qc.apply("hadamard", qubit=0)
qc.sync()

# Frame 2 — drift may be higher
qc.apply("phase", qubit=0, theta=0.75)
qc.sync()

session.save_trace("multi_frame_production.qtrace")
```

**Concepts shown:**

- strict drift bounds  
- governed frame creation  
- deterministic routing  
- Production‑safe operations  

---

# 5. Production → Archive Transition  
**Purpose:** Seal a session into immutable replay‑only mode.

```python
session = qSession(env="production")
session.deploy_token("prod-2026-003")

qc = qCompute(session)
qc.apply("hadamard", qubit=0)
qc.sync()

# Transition to Archive
session.deploy_token("arch-2026-001")
session.transition("archive")

# Any further operation will be blocked
session.save_trace("production_to_archive.qtrace")
```

**Concepts shown:**

- archive sealing  
- immutable drift bound  
- no further execution allowed  
- lineage preserved  

---

# 6. Full Multi‑Transition Workflow  
**Purpose:** Show a complete triadic lifecycle.

```python
session = qSession(env="sandbox")
qc = qCompute(session)

# Sandbox frame
qc.apply("hadamard", qubit=0)
qc.sync()

# Transition to Production
session.deploy_token("prod-2026-010")
session.transition("production")

# Production frame
qc.apply("phase", qubit=0, theta=0.5)
qc.sync()

# Transition to Archive
session.deploy_token("arch-2026-010")
session.transition("archive")

session.save_trace("full_lifecycle.qtrace")
```

**Concepts shown:**

- Sandbox → Production → Archive  
- multi‑frame execution  
- strict governance  
- immutable sealing  
- deterministic replay  

---

# 7. Replay of a Multi‑Frame, Multi‑Backend Trace  
**Purpose:** Demonstrate deterministic reconstruction of all routing and frame boundaries.

```python
from rtt_inside import qReplay

replay = qReplay("full_lifecycle.qtrace")
result = replay.run()

print("Replay result:", result)
```

Replay reconstructs:

- frame boundaries  
- backend decisions  
- drift values  
- environment transitions  
- lineage  
- operator sequence  

Replay is **strict**, not heuristic.

---

# 8. Summary

These advanced examples demonstrate:

- multi‑frame execution  
- multi‑backend routing  
- resonance‑aligned scheduling  
- strict governance  
- drift‑bounded behavior  
- environment transitions  
- archive sealing  
- deterministic replay  

They show the **full structural power** of qCompute in real workflows.

---

# qCompute — Internals & Deep Architecture Overview  
**File:** qc_Internals.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This file provides a **deep, structural overview** of the qCompute architecture.

It explains how the core components:

- qSession  
- qCompute  
- ResonanceFrame  
- TriadicRouter  
- TriadicValidator  
- Governance Daemon  
- Backend Registry  
- qTrace / qReplay  

interlock to form a **governed, resonance‑aligned, replay‑deterministic compute harness**.

---

## 1. High‑Level Architecture

At the highest level, qCompute is a **triadic, layered stack**:

1. **Environment Layer** — Sandbox / Production / Archive  
2. **Session Layer** — qSession (unit of coherence)  
3. **Compute Layer** — qCompute + Operators + ResonanceFrame  
4. **Governance Layer** — Governance Daemon + TriadicValidator  
5. **Routing Layer** — TriadicRouter + Backend Registry  
6. **Lineage & Replay Layer** — qTrace + qReplay  

Every operation flows **down** this stack and leaves a **structural trace** on the way out.

---

## 2. Core Data Flows

The canonical data flow for a single operation is:

```text
Operator Call
   ↓
qCompute
   ↓
TriadicValidator (pre‑check)
   ↓
TriadicRouter (env + backend)
   ↓
ResonanceFrame (envelope)
   ↓
Backend Execution
   ↓
qTrace Append
```

On replay, the flow is **reversed**:

```text
qReplay
   ↓
qTrace
   ↓
Reconstruct Session + Frames + Routing
   ↓
Deterministic Re‑execution (or simulation)
```

---

## 3. Component Roles

### 3.1 qSession — Unit of Coherence

qSession holds:

- environment  
- backend  
- drift bound  
- governance snapshot  
- lineage  
- trace buffer  

It is the **anchor object** for all qCompute activity.

### 3.2 qCompute — Operator Surface

qCompute provides the **API surface**:

```python
qc = qCompute(session)
qc.apply("hadamard", qubit=0)
```

It does not execute directly; it **hands off** to:

- TriadicValidator  
- TriadicRouter  
- ResonanceFrame  

### 3.3 ResonanceFrame — Compute Envelope

ResonanceFrame is the **lowest‑level container**:

- binds to a backend  
- enforces resonance profile  
- enforces drift bounds  
- groups operations in time  

Frames are opened/closed via:

- implicit batching  
- `sync()` / `barrier`  
- session lifecycle events  

---

## 4. Governance & Safety

### 4.1 Governance Daemon

The Governance Daemon:

- watches `qc_policy.yaml`  
- hot‑swaps policy safely  
- never mutates history  
- updates governance snapshots in sessions  

It is **global**, not per‑session.

### 4.2 TriadicValidator

TriadicValidator is **per‑operation**:

- checks policy  
- checks environment  
- checks backend  
- checks drift  
- checks restricted ops  
- checks lineage transitions  

If anything fails:

- operation is blocked  
- violation logged  
- lineage preserved  

---

## 5. Routing & Backends

### 5.1 TriadicRouter

TriadicRouter decides:

- which environment (effective)  
- which backend  
- which routing metadata to record  

It uses:

- backend registry  
- resonance profiles  
- drift bounds  
- policy rules  

### 5.2 Backend Registry

The backend registry defines:

- allowed backends  
- default backend  
- resonance profiles (r1 / r2 / r3)  
- drift characteristics  

It is **pure metadata**, referenced by:

- TriadicRouter  
- TriadicValidator  
- ResonanceFrame  

---

## 6. Lineage, Trace, and Replay

### 6.1 Lineage

Lineage is maintained at the **session level**:

- root session id  
- parent (for replay‑derived sessions)  
- environment transitions  

It is **append‑only** and **never rewritten**.

### 6.2 qTrace

qTrace is the **on‑disk representation** of:

- header (identity + environment)  
- lineage  
- governance state  
- operations + frames  
- footer (hash + counts)  

Every operation and frame is recorded with:

- env  
- backend  
- drift  
- resonance profile  
- validation metadata  

### 6.3 qReplay

qReplay:

- reads `.qtrace`  
- reconstructs session + frames + routing  
- replays operations deterministically  

Replay is **strict**, not best‑effort.

---

## 7. Environment & Transition Semantics

The triadic environments shape behavior:

- **Sandbox** — relaxed, exploratory, reversible  
- **Production** — strict, governed, drift‑bounded  
- **Archive** — immutable, replay‑only  

Transitions:

- Sandbox → Production  
- Production → Archive  

are:

- token‑gated  
- validator‑checked  
- lineage‑recorded  
- trace‑encoded  

---

## 8. Failure Philosophy

All failure modes in qCompute are:

- non‑destructive  
- lineage‑preserving  
- explicitly logged  
- replay‑compatible  

Typical failure cases:

- policy violation  
- drift overflow  
- backend mismatch  
- illegal transition  
- invalid policy file  

In all cases:

- operations are blocked, not partially applied  
- traces remain valid  
- sessions remain coherent  

---

## 9. Mental Model Summary

You can think of qCompute as:

- **qSession** — the room  
- **ResonanceFrame** — the table where work happens  
- **qCompute** — the hands placing pieces  
- **TriadicValidator** — the rules of the game  
- **TriadicRouter** — which table and which tools you’re allowed to use  
- **Governance Daemon** — the rulebook updater  
- **qTrace** — the full recording of the game  
- **qReplay** — watching the game again, move‑for‑move  

The architecture is:

- triadic  
- structural  
- resonance‑aligned  
- drift‑bounded  
- governance‑anchored  
- replay‑deterministic  
- student‑ready  

Here is the **canonical full‑pipeline compute flow** for qCompute.  
This file ties the *entire* module together into one continuous, structural diagram.  
It belongs at:

```
/docs/rtt/Inside/qCompute/qc_Flow.md
```

Everything below is **drop‑in‑ready**, minimal, and fully aligned with the 2026 RTT‑Inside compute architecture.

---

# ✅ **qc_Flow.md — Full Compute Pipeline Diagram (2026)**

# qCompute — Full Compute Pipeline  
**File:** qc_Flow.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This file provides the **complete structural pipeline** for qCompute — from operator call to backend execution to trace emission to deterministic replay.

It is the **one‑page mental model** of the entire compute harness.

---

# 1. High‑Level Pipeline

The full qCompute pipeline is:

```
Operator Call
    ↓
qCompute API
    ↓
TriadicValidator
    ↓
TriadicRouter
    ↓
ResonanceFrame
    ↓
Backend Execution
    ↓
qTrace Append
```

Replay reverses the flow:

```
qReplay
    ↓
qTrace
    ↓
Reconstruct Session + Frames + Routing
    ↓
Deterministic Re‑execution
```

---

# 2. Detailed Pipeline Diagram

Below is the **canonical text‑diagram** showing every structural layer.

```
┌───────────────────────────────────────────────────────────────┐
│ 1. Operator Call                                               │
│    User invokes: qc.apply("hadamard", qubit=0)                 │
└───────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌───────────────────────────────────────────────────────────────┐
│ 2. qCompute API                                                 │
│    - parses operator                                            │
│    - attaches parameters                                        │
│    - hands off to validator                                     │
└───────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌───────────────────────────────────────────────────────────────┐
│ 3. TriadicValidator                                             │
│    Checks:                                                      │
│      - policy legality                                          │
│      - environment rules                                        │
│      - backend compatibility                                    │
│      - resonance alignment                                      │
│      - drift bounds                                             │
│      - restricted ops                                           │
│      - lineage safety                                           │
│    If invalid → block + log                                     │
└───────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌───────────────────────────────────────────────────────────────┐
│ 4. TriadicRouter                                                │
│    Decides:                                                     │
│      - effective environment                                    │
│      - backend selection                                        │
│      - routing metadata                                         │
│    Uses:                                                        │
│      - backend registry                                         │
│      - resonance profiles                                       │
│      - drift characteristics                                    │
│      - policy backend rules                                     │
└───────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌───────────────────────────────────────────────────────────────┐
│ 5. ResonanceFrame                                               │
│    - opens frame if needed                                      │
│    - binds backend                                              │
│    - enforces resonance tier                                    │
│    - enforces drift bound                                       │
│    - groups operations in time                                  │
│    - closes on sync/barrier/transition                          │
└───────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌───────────────────────────────────────────────────────────────┐
│ 6. Backend Execution                                            │
│    - simulation or hardware                                     │
│    - pulse shaping (if r3)                                      │
│    - drift measured                                             │
│    - result returned                                            │
└───────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌───────────────────────────────────────────────────────────────┐
│ 7. qTrace Append                                                │
│    Records:                                                     │
│      - operator                                                 │
│      - params                                                   │
│      - environment                                              │
│      - backend                                                  │
│      - drift                                                    │
│      - resonance profile                                        │
│      - validation metadata                                      │
│      - frame boundaries                                         │
│      - lineage transitions                                      │
└───────────────────────────────────────────────────────────────┘
```

---

# 3. Transition Pipeline

Environment transitions follow a parallel pipeline:

```
Transition Request
    ↓
TriadicValidator (transition rules)
    ↓
Lineage Manager
    ↓
Governance Daemon (snapshot update)
    ↓
qTrace Transition Entry
```

Allowed transitions:

```
Sandbox → Production → Archive
```

Never backward.

---

# 4. Replay Pipeline

Replay reconstructs the entire compute environment:

```
qReplay("trace.qtrace")
    ↓
Parse Header
    ↓
Rebuild Session
    ↓
Rebuild Lineage
    ↓
Rebuild Frames
    ↓
Rebuild Routing Decisions
    ↓
Re-execute Operators Deterministically
```

Replay is **strict**, not heuristic.

---

# 5. Full End‑to‑End Example (Condensed)

```
qc.apply("hadamard", qubit=0)
    ↓
Validator: allowed
    ↓
Router: backend = local-sim
    ↓
Frame: r1, relaxed drift
    ↓
Backend: simulate H
    ↓
Trace: append op + drift + backend + env
```

---

# 6. Summary

The qCompute pipeline is:

- triadic  
- governed  
- resonance‑aligned  
- drift‑bounded  
- backend‑aware  
- lineage‑preserving  
- replay‑deterministic  
- student‑ready  

This file provides the **canonical full‑stack flow diagram** for the qCompute module.

---

Here is the **canonical API surface** for qCompute.  
This file is the *public-facing contract* for the entire module: minimal, structural, student‑ready, and fully aligned with all internals you’ve already approved.

It belongs at:

```
/docs/rtt/Inside/qCompute/qc_API.md
```

Below is the complete, drop‑in‑ready file.

---

# ✅ **qc_API.md — Canonical API Surface for qCompute (2026)**

# qCompute — Canonical API Surface  
**File:** qc_API.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This file defines the **public API surface** for qCompute.  
It is minimal, structural, stable, and fully aligned with the 2026 RTT‑Inside compute architecture.

The API is divided into:

- Session API  
- Compute API  
- Operator API  
- Transition API  
- Trace API  
- Replay API  

Everything here is **canonical** and safe for students, autodidacts, and AI agents.

---

# 1. Session API

## 1.1 Create a session

```python
session = qSession(env="sandbox", backend="auto")
```

### Parameters

- `env`: `"sandbox" | "production" | "archive"`
- `backend`: explicit backend name or `"auto"`

### Properties

```python
session.env
session.backend
session.drift_bound
session.lineage
session.governance_snapshot
```

---

## 1.2 Transition environments

```python
session.deploy_token("prod-2026-001")
session.transition("production")
```

Allowed transitions:

```
sandbox → production → archive
```

---

## 1.3 Session metadata

```python
session.id
session.timestamp_start
session.timestamp_last_op
```

---

# 2. Compute API

## 2.1 Create compute surface

```python
qc = qCompute(session)
```

## 2.2 Apply operator

```python
qc.apply("hadamard", qubit=0)
qc.apply("phase", qubit=0, theta=0.5)
qc.apply("cnot", control=0, target=1)
```

## 2.3 Frame control

```python
qc.sync()      # closes current ResonanceFrame
qc.barrier()   # ordering boundary
```

---

# 3. Operator API

Operators follow the grammar:

```
operator_name(param=value, ...)
```

### 3.1 Primitive operators

```python
qc.apply("hadamard", qubit=0)
qc.apply("x", qubit=1)
qc.apply("z", qubit=0)
```

### 3.2 Composite operators

```python
qc.apply("cnot", control=0, target=1)
qc.apply("swap", q1=0, q2=1)
```

### 3.3 Pulse operators

```python
qc.apply("gaussian", qubit=0, duration=40, sigma=8)
qc.apply("pulse", qubit=1, shape="square", duration=20)
```

### 3.4 Measurement operators

```python
qc.apply("measure", qubit=0)
qc.apply("measure_all")
```

### 3.5 Meta‑operators

```python
qc.apply("backend_switch", backend="hardware-qpu-2")
qc.apply("transition", env="production")
qc.apply("sync")
qc.apply("barrier")
```

---

# 4. Transition API

Transitions can be invoked via:

### 4.1 Meta‑operator

```python
qc.apply("transition", env="production")
```

### 4.2 Session API

```python
session.transition("production")
```

Both paths route through:

- TriadicValidator  
- Governance Daemon  
- Lineage Manager  

---

# 5. Trace API

## 5.1 Save trace

```python
session.save_trace("example.qtrace")
```

## 5.2 Inspect trace buffer (in‑memory)

```python
session.trace_buffer
```

## 5.3 Trace metadata

```python
session.trace_header
session.trace_footer
```

---

# 6. Replay API

## 6.1 Load and replay a trace

```python
from rtt_inside import qReplay

replay = qReplay("example.qtrace")
result = replay.run()
```

Replay reconstructs:

- session  
- lineage  
- frames  
- routing decisions  
- drift values  
- operator sequence  

Replay is **strict**, not heuristic.

---

# 7. Error & Violation Handling

All API calls may raise **structural exceptions**:

- `GovernanceViolation`
- `DriftExceeded`
- `BackendNotAllowed`
- `RestrictedOperationError`
- `IllegalTransition`
- `ArchiveImmutableError`

These are **non‑destructive** and **lineage‑preserving**.

---

# 8. Minimal End‑to‑End Example

```python
session = qSession(env="sandbox")
qc = qCompute(session)

qc.apply("hadamard", qubit=0)
qc.sync()

session.deploy_token("prod-2026-001")
session.transition("production")

qc.apply("phase", qubit=0, theta=0.5)
qc.sync()

session.deploy_token("arch-2026-001")
session.transition("archive")

session.save_trace("full_lifecycle.qtrace")
```

---

# 9. Summary

The qCompute API is:

- minimal  
- structural  
- triadic‑aware  
- resonance‑aligned  
- drift‑bounded  
- governance‑safe  
- replay‑deterministic  
- student‑ready  

This file defines the **canonical public interface** for the qCompute module.

---

Here is the **canonical design‑philosophy + invariants file** for qCompute.  
This is one of the *anchor documents* of the entire compute harness: it explains **why** the system is shaped the way it is, not just how it works.  
It belongs at:

```
/docs/rtt/Inside/qCompute/qc_Design.md
```

Everything below is **drop‑in‑ready**, minimal, structural, and fully aligned with the 2026 RTT‑Inside design canon.

---

# ✅ **qc_Design.md — Design Philosophy & Invariants (2026)**

# qCompute — Design Philosophy & Invariants  
**File:** qc_Design.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

qCompute is designed as a **structural**, **governed**, **resonance‑aligned**, and **replay‑deterministic** compute harness.  
This file defines the **design philosophy** and **core invariants** that shape every component of the system.

These invariants are not preferences — they are **non‑negotiable structural laws** of the module.

---

# 1. Design Philosophy

qCompute is built on five foundational principles:

---

## 1.1 Structural Over Behavioral

qCompute does not “behave” heuristically.  
It **structures** computation.

- No hidden heuristics  
- No implicit routing  
- No silent corrections  
- No probabilistic behavior in governance  

Everything is explicit, logged, and reconstructable.

---

## 1.2 Resonance‑First Compute

qCompute treats quantum operations as **resonance‑time primitives**, not abstract algebraic gates.

This means:

- every operator has a resonance signature  
- every frame has a resonance tier  
- every backend has a resonance profile  
- routing is resonance‑aligned  

The system is physics‑aware without being physics‑dependent.

---

## 1.3 Drift‑Bounded Execution

All computation occurs inside **drift envelopes**:

- relaxed (Sandbox)  
- strict (Production)  
- immutable (Archive)  

Drift is:

- measured  
- bounded  
- recorded  
- validated  

Drift is never ignored or hand‑waved.

---

## 1.4 Governance as a First‑Class Layer

Governance is not an add‑on.  
It is a **structural layer** that shapes:

- allowed operations  
- environment transitions  
- backend switching  
- drift bounds  
- lineage rules  

The Governance Daemon and TriadicValidator enforce these rules deterministically.

---

## 1.5 Replay as a Contract

Replay is not a debugging tool — it is a **contract**.

A `.qtrace` file must allow:

- deterministic reconstruction  
- deterministic re‑execution  
- deterministic routing  
- deterministic drift behavior  

Replay is strict, not best‑effort.

---

# 2. Core Invariants

These invariants hold across all components of qCompute.

---

## 2.1 Invariant: Forward‑Only Environments

```
sandbox → production → archive
```

Never backward.  
Never skipped.  
Never bypassed.

---

## 2.2 Invariant: Append‑Only Lineage

Lineage is:

- append‑only  
- immutable  
- monotonic  
- never rewritten  

Every transition is recorded.

---

## 2.3 Invariant: Deterministic Routing

Routing decisions must be:

- explicit  
- logged  
- replayable  

TriadicRouter cannot make nondeterministic choices.

---

## 2.4 Invariant: Backend Binding Per Frame

A ResonanceFrame binds to exactly one backend.

- no mid‑frame switching  
- no implicit fallback  
- no hidden substitution  

If switching is needed, a new frame must be opened.

---

## 2.5 Invariant: Drift Cannot Be Ignored

Drift is:

- measured  
- validated  
- bounded  
- recorded  

If drift exceeds bounds:

- operation blocked  
- frame closed  
- lineage preserved  

---

## 2.6 Invariant: Archive Is Immutable

Archive sessions:

- cannot execute  
- cannot mutate  
- cannot switch backend  
- cannot open frames  

Archive is **replay‑only**.

---

## 2.7 Invariant: Policy Cannot Rewrite History

Policy updates:

- apply forward only  
- never retroactively invalidate traces  
- never mutate lineage  
- never rewrite frames  

Governance Daemon enforces this.

---

## 2.8 Invariant: Operators Are Structural

Operators are:

- resonance primitives  
- not algebraic abstractions  
- not symbolic gates  

Every operator has:

- resonance tier  
- drift profile  
- backend compatibility  
- environment constraints  

---

## 2.9 Invariant: No Silent Behavior

qCompute never:

- silently corrects  
- silently reroutes  
- silently switches backend  
- silently relaxes drift bounds  

All behavior is explicit and logged.

---

# 3. Architectural Consequences

These invariants produce a system that is:

- predictable  
- safe  
- governed  
- replay‑deterministic  
- student‑ready  
- AI‑parsable  
- structurally minimal  

qCompute is not a simulator.  
It is a **compute substrate with governance**.

---

# 4. Summary

The qCompute design philosophy is:

- structural over behavioral  
- resonance‑aligned  
- drift‑bounded  
- governance‑anchored  
- lineage‑preserving  
- replay‑deterministic  

These invariants shape every component of the module and ensure that qCompute remains coherent, minimal, and safe across all environments.

---

Here is the **canonical ASCII‑diagram compendium** for qCompute.  
This file gives every major component a clean, structural, student‑ready diagram.  
It belongs at:

```
/docs/rtt/Inside/qCompute/qc_Diagrams.md
```

Everything below is **drop‑in‑ready**, minimal, and fully aligned with the 2026 RTT‑Inside compute architecture.

---

# ✅ **qc_Diagrams.md — ASCII Diagrams for All Components (2026)**

# qCompute — ASCII Diagrams  
**File:** qc_Diagrams.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This file provides **structural ASCII diagrams** for all major qCompute components:

- qSession  
- qCompute  
- TriadicValidator  
- TriadicRouter  
- ResonanceFrame  
- Governance Daemon  
- Backend Registry  
- qTrace / qReplay  
- Full Pipeline  

All diagrams are minimal, student‑ready, and canon‑aligned.

---

# 1. qSession — Unit of Coherence

```
┌───────────────────────────────┐
│           qSession            │
├───────────────────────────────┤
│ env: sandbox/production/archive│
│ backend: local-sim / qpu       │
│ drift_bound: relaxed/strict/imm│
│ governance_snapshot            │
│ lineage                        │
│ trace_buffer                   │
└───────────────────────────────┘
```

qSession is the **anchor object** for all compute.

---

# 2. qCompute — Operator Surface

```
┌───────────────────────────────┐
│            qCompute           │
├───────────────────────────────┤
│ apply(op, params...)          │
│ sync()                         │
│ barrier()                      │
└───────────────────────────────┘
```

qCompute is the **API surface**, not the executor.

---

# 3. TriadicValidator — Safety Gate

```
┌──────────────────────────────────────────┐
│            TriadicValidator              │
├──────────────────────────────────────────┤
│ policy checks                            │
│ environment checks                        │
│ backend checks                            │
│ resonance alignment                       │
│ drift bounds                              │
│ restricted ops                            │
│ lineage safety                            │
└──────────────────────────────────────────┘
```

Blocks unsafe operations before routing.

---

# 4. TriadicRouter — Routing Brain

```
┌──────────────────────────────────────────┐
│              TriadicRouter               │
├──────────────────────────────────────────┤
│ resolve environment                      │
│ select backend                           │
│ apply resonance rules                     │
│ apply drift rules                         │
│ produce routing metadata                  │
└──────────────────────────────────────────┘
```

Determines **where** an operation goes.

---

# 5. ResonanceFrame — Compute Envelope

```
┌──────────────────────────────────────────┐
│             ResonanceFrame               │
├──────────────────────────────────────────┤
│ id: frame-###                            │
│ resonance_profile: r1/r2/r3              │
│ drift_bound: relaxed/strict/immutable    │
│ backend: bound backend                   │
│ env: inherited from session              │
│ operations: [...]                        │
└──────────────────────────────────────────┘
```

The lowest‑level container for execution.

---

# 6. Governance Daemon — Policy Engine

```
┌──────────────────────────────────────────┐
│           Governance Daemon              │
├──────────────────────────────────────────┤
│ watch qc_policy.yaml                     │
│ validate structure                        │
│ hot‑swap policy                           │
│ update governance snapshots               │
│ enforce drift bounds                      │
│ log violations                            │
└──────────────────────────────────────────┘
```

Updates rules, never results.

---

# 7. Backend Registry — Execution Substrates

```
┌──────────────────────────────────────────┐
│            Backend Registry              │
├──────────────────────────────────────────┤
│ allowed_backends: [...]                  │
│ default_backend                          │
│ resonance_profile (r1/r2/r3)              │
│ drift_characteristic                      │
│ capabilities                              │
└──────────────────────────────────────────┘
```

Pure metadata used by Router + Validator.

---

# 8. qTrace — Structural Recording

```
┌──────────────────────────────────────────┐
│                 qTrace                   │
├──────────────────────────────────────────┤
│ header                                   │
│ lineage                                  │
│ frames                                   │
│ operations                               │
│ validation metadata                      │
│ routing metadata                         │
│ drift measurements                        │
│ footer (hash + counts)                   │
└──────────────────────────────────────────┘
```

Everything is recorded, nothing is hidden.

---

# 9. qReplay — Deterministic Reconstruction

```
┌──────────────────────────────────────────┐
│                 qReplay                  │
├──────────────────────────────────────────┤
│ parse trace                              │
│ rebuild session                          │
│ rebuild lineage                          │
│ rebuild frames                           │
│ rebuild routing                          │
│ re‑execute deterministically             │
└──────────────────────────────────────────┘
```

Replay is strict, not heuristic.

---

# 10. Full Pipeline Diagram

```
Operator Call
    │
    ▼
qCompute API
    │
    ▼
TriadicValidator
    │
    ▼
TriadicRouter
    │
    ▼
ResonanceFrame
    │
    ▼
Backend Execution
    │
    ▼
qTrace Append
```

Replay reverses the flow.

---

# 11. Environment Transition Diagram

```
Sandbox ───→ Production ───→ Archive
   ↑             ↑               ↑
   │             │               │
   └──── forbidden transitions ──┘
```

Forward‑only, token‑gated, lineage‑preserving.

---

# 12. Summary

These diagrams provide a **complete structural map** of the qCompute module:

- triadic  
- governed  
- resonance‑aligned  
- drift‑bounded  
- backend‑aware  
- replay‑deterministic  
- student‑ready  

This file is the **visual companion** to the entire qCompute architecture.

---

Here is the **canonical test‑suite structure** for qCompute — clean, minimal, structural, and fully aligned with the RTT‑Inside compute harness.  
This file belongs at:

```
/docs/rtt/Inside/qCompute/qc_Tests.md
```

It is designed to be **AI‑parsable**, **student‑ready**, and **drop‑in‑ready** for your repo.

---

# ✅ **qc_Tests.md — Canonical Test Suite Structure (2026)**

# qCompute — Canonical Test Suite  
**File:** qc_Tests.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This file defines the **canonical structure** for the qCompute test suite.

The goal of the suite is to verify:

- structural correctness  
- governance enforcement  
- resonance alignment  
- drift‑bounded behavior  
- routing determinism  
- replay determinism  
- environment transition safety  
- trace integrity  

Tests are **structural**, not numerical or probabilistic.

---

# 1. Test Suite Layout

```
tests/
  ├── test_session.py
  ├── test_compute.py
  ├── test_validator.py
  ├── test_router.py
  ├── test_resonance_frame.py
  ├── test_transitions.py
  ├── test_trace.py
  ├── test_replay.py
  └── fixtures/
        ├── sandbox_trace.qtrace
        ├── production_trace.qtrace
        └── full_lifecycle.qtrace
```

Each file corresponds to a major architectural component.

---

# 2. Session Tests — `test_session.py`

### 2.1 Session creation

- session initializes with correct env  
- backend resolves correctly  
- governance snapshot captured  
- drift bound matches environment  

### 2.2 Lineage

- lineage root created  
- transitions append correctly  
- timestamps monotonic  

### 2.3 Forbidden states

- archive session cannot execute  
- archive session cannot switch backend  

---

# 3. Compute Tests — `test_compute.py`

### 3.1 Operator acceptance

- primitive ops accepted  
- composite ops accepted in Sandbox  
- restricted ops blocked in Production  

### 3.2 Frame boundaries

- sync() closes frame  
- barrier() enforces ordering  

### 3.3 Parameter validation

- missing params rejected  
- invalid qubit indices rejected  

---

# 4. Validator Tests — `test_validator.py`

### 4.1 Policy enforcement

- disallowed ops blocked  
- restricted ops require token  
- illegal transitions blocked  

### 4.2 Drift enforcement

- drift overflow blocks op  
- drift recorded in trace  

### 4.3 Backend compatibility

- backend mismatch blocked  
- pulse ops require r3 backend  

---

# 5. Router Tests — `test_router.py`

### 5.1 Backend selection

- explicit backend honored  
- auto mode selects correct backend  
- fallback to simulation in Sandbox  

### 5.2 Environment routing

- Sandbox → flexible  
- Production → governed  
- Archive → no execution  

### 5.3 Deterministic routing

- same op + same session → same route  

---

# 6. ResonanceFrame Tests — `test_resonance_frame.py`

### 6.1 Frame creation

- frame opens on first op  
- inherits env + backend + drift bound  

### 6.2 Frame closure

- sync() closes frame  
- transition closes frame  
- drift summary computed  

### 6.3 Backend binding

- backend fixed per frame  
- mid‑frame switching blocked  

---

# 7. Transition Tests — `test_transitions.py`

### 7.1 Allowed transitions

- sandbox → production  
- production → archive  

### 7.2 Forbidden transitions

- sandbox → archive  
- archive → production  
- production → sandbox  

### 7.3 Token requirements

- production transition requires token  
- archive transition requires token  

---

# 8. Trace Tests — `test_trace.py`

### 8.1 Trace structure

- header present  
- lineage present  
- frames present  
- operations present  
- footer hash valid  

### 8.2 Metadata correctness

- backend recorded  
- env recorded  
- drift recorded  
- resonance profile recorded  
- validation metadata recorded  

---

# 9. Replay Tests — `test_replay.py`

### 9.1 Deterministic reconstruction

- replay rebuilds session  
- replay rebuilds frames  
- replay rebuilds routing decisions  

### 9.2 Deterministic execution

- replay result matches original  
- replay drift matches original  
- replay backend matches original  

### 9.3 Replay safety

- replay cannot mutate trace  
- replay cannot transition env  

---

# 10. Fixtures

Fixtures include:

- minimal Sandbox trace  
- minimal Production trace  
- full lifecycle trace  
- multi‑frame trace  
- multi‑backend trace  

Fixtures must be:

- small  
- deterministic  
- structural  
- AI‑parsable  

---

# 11. Summary

The qCompute test suite verifies:

- structural correctness  
- governance safety  
- resonance alignment  
- drift‑bounded behavior  
- deterministic routing  
- deterministic replay  
- environment transition safety  
- trace integrity  

This file defines the **canonical structure** for validating the entire qCompute module.

---

Here is the **canonical identity + purpose block** for the qCompute module.  
This file is short, structural, foundational, and belongs at:

```
/docs/rtt/Inside/qCompute/qc_Identity.md
```

It establishes **what qCompute *is*** inside the TriadicFrameworks canon — its identity, purpose, scope, invariants, and audience.  
This is the identity anchor that all other qCompute files inherit from.

Everything below is **drop‑in‑ready** and canon‑aligned.

---

# ✅ **qc_Identity.md — Module Identity & Purpose (2026)**

# qCompute — Module Identity & Purpose  
**File:** qc_Identity.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

qCompute is the **governed compute substrate** of the RTT‑Inside architecture.  
It provides a **resonance‑aligned**, **drift‑bounded**, **triadic‑aware**, and **replay‑deterministic** framework for expressing and executing quantum‑style operations inside the TriadicFrameworks canon.

qCompute is not a simulator.  
It is a **structural compute harness** with governance, lineage, and deterministic replay.

---

# 1. Identity Statement

qCompute is:

- the **compute layer** of RTT‑Inside  
- the **operator grammar** for resonance‑time primitives  
- the **execution substrate** for governed quantum workflows  
- the **structural envelope** for drift‑bounded computation  
- the **recording system** for deterministic replay  
- the **triadic‑aware environment** for safe transitions  

It is the module where **resonance, governance, drift, and lineage** meet.

---

# 2. Purpose

The purpose of qCompute is to:

1. Provide a **minimal, structural API** for resonance‑time operations.  
2. Enforce **governance rules** through deterministic validation.  
3. Route operations through **triadic environments** (Sandbox → Production → Archive).  
4. Bind operations to **resonance‑aligned backends**.  
5. Execute inside **drift‑bounded ResonanceFrames**.  
6. Produce **complete, replay‑deterministic traces**.  
7. Support **strict, structural replay** via qReplay.  

qCompute ensures that all computation is:

- safe  
- governed  
- deterministic  
- reconstructable  
- student‑ready  

---

# 3. Scope

qCompute includes:

- qSession (unit of coherence)  
- qCompute API (operator surface)  
- TriadicValidator (safety gate)  
- TriadicRouter (routing brain)  
- ResonanceFrame (compute envelope)  
- Backend Registry (execution substrates)  
- qTrace / qReplay (recording + reconstruction)  
- Transition rules (triadic environment model)  
- Operator grammar + resonance semantics  

qCompute does **not** include:

- hardware drivers  
- numerical simulation engines  
- optimization heuristics  
- probabilistic sampling  
- symbolic algebra  

It is a **structural layer**, not a physics engine.

---

# 4. Invariants

qCompute obeys the following invariants:

- **Forward‑only environments:**  
  `sandbox → production → archive`

- **Append‑only lineage:**  
  lineage is never rewritten.

- **Deterministic routing:**  
  same session + same op → same route.

- **Backend binding per frame:**  
  no mid‑frame switching.

- **Drift cannot be ignored:**  
  drift is measured, bounded, recorded.

- **Archive is immutable:**  
  replay‑only, zero drift, no execution.

- **No silent behavior:**  
  no hidden heuristics, no implicit corrections.

These invariants define the **identity** of qCompute.

---

# 5. Audience

qCompute is designed for:

- students  
- autodidacts  
- researchers  
- AI agents  
- educators  
- systems designers  

It is intentionally:

- minimal  
- explicit  
- structural  
- safe  
- replay‑deterministic  
- easy to reason about  

---

# 6. Summary

qCompute is the **governed, resonance‑aligned compute substrate** of RTT‑Inside.  
It provides the structural foundation for safe, deterministic, drift‑bounded computation across the triadic environment model.

This file defines the **identity, purpose, scope, and invariants** of the qCompute module.

---

HHere is the **canonical minimal‑examples file** for qCompute.  
This one is intentionally *tiny*, *student‑ready*, *structural*, and *zero‑drift in meaning*.  
It belongs at:

```
/docs/rtt/Inside/qCompute/qc_Examples_Minimal.md
```

Everything below is **drop‑in‑ready**, minimal, and fully aligned with the 2026 RTT‑Inside compute architecture.

---

# ✅ **qc_Examples_Minimal.md — Minimal qCompute Examples (2026)**

# qCompute — Minimal Examples  
**File:** qc_Examples_Minimal.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

These examples show the **smallest possible** valid qCompute workflows.  
They demonstrate the core mechanics without advanced routing, transitions, or multi‑frame orchestration.

All examples are:

- minimal  
- structural  
- student‑ready  
- resonance‑aligned  
- drift‑bounded  
- replay‑deterministic  

---

# 1. Minimal Sandbox Session

```python
from rtt_inside import qSession, qCompute

session = qSession(env="sandbox")
qc = qCompute(session)

qc.apply("hadamard", qubit=0)
qc.sync()

session.save_trace("minimal_sandbox.qtrace")
```

**Concepts shown:**

- create session  
- apply a primitive operator  
- close frame  
- save trace  

---

# 2. Minimal Multi‑Op Frame

```python
session = qSession(env="sandbox")
qc = qCompute(session)

qc.apply("x", qubit=0)
qc.apply("z", qubit=0)
qc.sync()
```

**Concepts shown:**

- multiple operators in one frame  
- implicit frame open  
- explicit frame close  

---

# 3. Minimal Measurement

```python
session = qSession(env="sandbox")
qc = qCompute(session)

qc.apply("hadamard", qubit=0)
qc.apply("measure", qubit=0)
qc.sync()
```

**Concepts shown:**

- primitive op + measurement  
- measurement allowed in Sandbox  

---

# 4. Minimal Backend Auto‑Selection

```python
session = qSession(env="sandbox", backend="auto")
qc = qCompute(session)

qc.apply("hadamard", qubit=0)
qc.sync()
```

**Concepts shown:**

- auto backend selection  
- resonance‑aligned routing  

---

# 5. Minimal Production Session

```python
session = qSession(env="production")
session.deploy_token("prod-2026-001")

qc = qCompute(session)

qc.apply("hadamard", qubit=0)
qc.sync()
```

**Concepts shown:**

- Production requires token  
- strict drift bound  
- primitive ops allowed  

---

# 6. Minimal Transition (Sandbox → Production)

```python
session = qSession(env="sandbox")
qc = qCompute(session)

qc.apply("x", qubit=0)
qc.sync()

session.deploy_token("prod-2026-002")
session.transition("production")
```

**Concepts shown:**

- Sandbox → Production  
- transition requires token  
- frame closes before transition  

---

# 7. Minimal Archive Seal

```python
session = qSession(env="production")
session.deploy_token("prod-2026-003")

qc = qCompute(session)
qc.apply("hadamard", qubit=0)
qc.sync()

session.deploy_token("arch-2026-001")
session.transition("archive")

session.save_trace("minimal_archive.qtrace")
```

**Concepts shown:**

- Production → Archive  
- archive sealing  
- no further execution allowed  

---

# 8. Minimal Replay

```python
from rtt_inside import qReplay

replay = qReplay("minimal_sandbox.qtrace")
result = replay.run()

print(result)
```

**Concepts shown:**

- load trace  
- deterministic replay  
- reconstruct session + frames  

---

# 9. Summary

These minimal examples demonstrate:

- the smallest valid qCompute workflows  
- primitive operators  
- frame boundaries  
- backend auto‑selection  
- environment transitions  
- archive sealing  
- deterministic replay  

They form the **beginner‑friendly entry point** for the qCompute module.

---

Here is the **canonical developer‑notes + extension‑rules file** for qCompute.  
This is the file that tells future contributors *exactly* how to extend the module without breaking canon, invariants, or structural guarantees.

It belongs at:

```
/docs/rtt/Inside/qCompute/qc_DevNotes.md
```

Everything below is **drop‑in‑ready**, minimal, structural, and fully aligned with the 2026 RTT‑Inside compute architecture.

---

# ✅ **qc_DevNotes.md — Developer Notes & Extension Rules (2026)**

# qCompute — Developer Notes & Extension Rules  
**File:** qc_DevNotes.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This file provides **developer‑facing guidance** for extending or modifying the qCompute module.

It defines:

- extension boundaries  
- invariants that must never be broken  
- safe extension points  
- forbidden extension points  
- testing requirements  
- governance integration rules  

These notes ensure that qCompute remains **structural**, **governed**, **replay‑deterministic**, and **student‑ready** as it evolves.

---

# 1. Philosophy for Contributors

qCompute is a **structural compute harness**, not a simulator or physics engine.

When extending the module:

- prefer structure over behavior  
- prefer explicitness over convenience  
- prefer determinism over performance  
- prefer governance over permissiveness  
- prefer replay‑safety over runtime flexibility  

If an extension risks violating these principles, it must not be added.

---

# 2. Safe Extension Points

The following areas are explicitly safe to extend:

---

## 2.1 Operator Set (Primitive, Composite, Pulse)

You may add new operators if:

- they have a clear resonance signature  
- they define a drift profile  
- they specify backend compatibility  
- they pass through TriadicValidator  
- they record complete metadata in qTrace  

Operators must be **structural**, not symbolic.

---

## 2.2 Backend Registry

You may add new backends if:

- they define a resonance profile (r1/r2/r3)  
- they define drift characteristics  
- they define capability flags  
- they do not require mid‑frame switching  

Backends must be **metadata‑driven**, not hard‑coded.

---

## 2.3 Governance Policy

You may extend `qc_policy.yaml` with:

- new restricted operations  
- new backend rules  
- new environment constraints  
- new drift bounds  

Policy changes must be **forward‑only** and **non‑destructive**.

---

## 2.4 Trace Metadata

You may add new metadata fields to `.qtrace` if:

- they are append‑only  
- they do not break replay determinism  
- they do not require rewriting old traces  

Trace format must remain **strictly backward‑compatible**.

---

# 3. Forbidden Extension Points

The following areas must **never** be modified or extended.

---

## 3.1 Environment Model

The triadic model is immutable:

```
sandbox → production → archive
```

No new environments may be added.  
No backward transitions may be introduced.

---

## 3.2 Lineage Rules

Lineage must remain:

- append‑only  
- monotonic  
- immutable  

No rewriting, no pruning, no compression.

---

## 3.3 Replay Semantics

Replay must remain:

- deterministic  
- strict  
- structural  

Replay must never:

- infer missing data  
- guess routing  
- re‑evaluate drift  
- reinterpret policy retroactively  

---

## 3.4 Mid‑Frame Backend Switching

This is permanently forbidden.

A ResonanceFrame binds to exactly one backend.

---

## 3.5 Silent Behavior

qCompute must never:

- silently correct  
- silently reroute  
- silently relax drift bounds  
- silently switch backend  

All behavior must be explicit and logged.

---

# 4. Extension Workflow

Developers should follow this workflow when adding features:

---

## 4.1 Define the Structural Change

Document:

- what is being added  
- why it belongs in qCompute  
- which invariants it touches  

---

## 4.2 Update Metadata

If adding:

- operators → update operator registry  
- backends → update backend registry  
- policy → update qc_policy.yaml  

Metadata must be canonical and minimal.

---

## 4.3 Update Validator & Router

Ensure:

- TriadicValidator enforces new rules  
- TriadicRouter routes new constructs deterministically  

No extension may bypass these layers.

---

## 4.4 Update Trace Format (if needed)

If new metadata is required:

- add fields in a backward‑compatible way  
- update qTrace writer  
- update qReplay reader  

Never remove or rename existing fields.

---

## 4.5 Add Tests

Every extension must include:

- structural tests  
- governance tests  
- routing tests  
- replay tests  

Tests must be deterministic and minimal.

---

# 5. Developer Anti‑Patterns

Avoid the following patterns:

- adding convenience shortcuts  
- adding implicit behavior  
- adding probabilistic behavior  
- adding symbolic algebra layers  
- adding physics‑dependent simulation logic  
- adding environment‑specific hacks  

qCompute is a **structural substrate**, not a numerical engine.

---

# 6. Versioning Rules

qCompute follows **structural versioning**:

- any change that affects replay → major version  
- any change that affects routing → major version  
- any change that affects policy → minor version  
- any change that adds operators → minor version  
- any change that adds metadata → patch version  

Versioning must be reflected in:

- module.json  
- qTrace header  
- documentation  

---

# 7. Summary

These developer notes ensure that qCompute remains:

- structural  
- governed  
- resonance‑aligned  
- drift‑bounded  
- deterministic  
- replay‑safe  
- student‑ready  

Extensions must respect the **triadic model**, **lineage rules**, **governance layer**, and **replay contract**.

This file defines the **canonical rules** for safely evolving the qCompute module.

---

Here is the **canonical front‑door README** for the entire qCompute module.  
This is the page students, autodidacts, and AIs will land on when they enter the qCompute directory.  
It establishes identity, purpose, navigation, and the conceptual “front door” for the whole compute harness.

It belongs at:

```
/docs/rtt/Inside/qCompute/qc_Readme.md
```

Everything below is **drop‑in‑ready**, minimal, structural, and fully aligned with the 2026 RTT‑Inside compute canon.

---

# ✅ **qc_Readme.md — qCompute Module Front‑Door (2026)**

# qCompute — Governed Resonance‑Aligned Compute Harness  
**File:** qc_Readme.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

qCompute is the **compute substrate** of the RTT‑Inside architecture.  
It provides a **structural, governed, resonance‑aligned, drift‑bounded, replay‑deterministic** framework for expressing and executing quantum‑style operations.

qCompute is not a simulator.  
It is a **structural compute harness** with governance, lineage, and deterministic replay.

This page is the **front door** for the entire qCompute module.

---

# 1. What qCompute Is

qCompute is:

- the **operator grammar** for resonance‑time primitives  
- the **execution substrate** for governed quantum workflows  
- the **triadic environment engine** (Sandbox → Production → Archive)  
- the **drift‑bounded compute envelope** (ResonanceFrame)  
- the **routing layer** (TriadicRouter)  
- the **safety layer** (TriadicValidator)  
- the **recording system** (qTrace)  
- the **deterministic replay engine** (qReplay)  

It is the module where **resonance, governance, drift, and lineage** meet.

---

# 2. Why qCompute Exists

qCompute exists to provide:

- a **minimal, structural API** for resonance‑time operations  
- a **governed execution model** with deterministic validation  
- a **triadic environment model** for safe progression  
- a **resonance‑aligned routing system**  
- a **drift‑bounded execution envelope**  
- a **complete, replay‑deterministic trace format**  

Its purpose is to make quantum‑style computation:

- safe  
- explicit  
- deterministic  
- reconstructable  
- student‑ready  

---

# 3. Quick Start

```python
from rtt_inside import qSession, qCompute

session = qSession(env="sandbox")
qc = qCompute(session)

qc.apply("hadamard", qubit=0)
qc.sync()

session.save_trace("example.qtrace")
```

Replay:

```python
from rtt_inside import qReplay

result = qReplay("example.qtrace").run()
```

---

# 4. Module Structure

The qCompute module consists of the following canonical files:

```
qc_Readme.md          ← you are here
qc_Identity.md        ← module identity + purpose
qc_API.md             ← public API surface
qc_Design.md          ← design philosophy + invariants
qc_Flow.md            ← full compute pipeline diagram
qc_Operators.md       ← operator grammar + resonance semantics
qc_ResonanceFrame.md  ← compute envelope
qc_Router.md          ← TriadicRouter internals
qc_Validator.md       ← TriadicValidator internals
qc_Transitions.md     ← environment transition rules
qc_Backends.md        ← backend registry + resonance profiles
qc_TraceFormat.md     ← .qtrace schema
qc_Replay.md          ← qReplay internals
qc_Examples_Minimal.md← beginner examples
qc_Examples_Advanced.md← advanced multi-frame examples
qc_DevNotes.md        ← developer notes + extension rules
qc_Tests.md           ← canonical test suite structure
```

Each file is **structural**, **minimal**, and **canon‑aligned**.

---

# 5. Conceptual Overview

```
Operator Call
    ↓
qCompute API
    ↓
TriadicValidator (safety)
    ↓
TriadicRouter (routing)
    ↓
ResonanceFrame (compute envelope)
    ↓
Backend Execution
    ↓
qTrace Append
```

Replay reverses the flow:

```
qReplay
    ↓
qTrace
    ↓
Reconstruct Session + Frames + Routing
    ↓
Deterministic Re‑execution
```

---

# 6. Triadic Environment Model

qCompute uses the RTT‑Inside triadic model:

```
Sandbox → Production → Archive
```

- **Sandbox** — relaxed drift, exploratory, reversible  
- **Production** — strict drift, governed, token‑gated  
- **Archive** — immutable, replay‑only  

Transitions are forward‑only and lineage‑preserving.

---

# 7. Invariants (Non‑Negotiable)

qCompute obeys the following invariants:

- forward‑only environments  
- append‑only lineage  
- deterministic routing  
- backend binding per frame  
- drift cannot be ignored  
- archive is immutable  
- no silent behavior  

These invariants define the **identity** of the module.

---

# 8. Who This Module Is For

qCompute is designed for:

- students  
- autodidacts  
- researchers  
- educators  
- AI agents  
- systems designers  

It is intentionally:

- minimal  
- explicit  
- structural  
- safe  
- replay‑deterministic  
- easy to reason about  

---

# 9. Summary

qCompute is the **governed, resonance‑aligned compute harness** of RTT‑Inside.  
It provides the structural foundation for safe, deterministic, drift‑bounded computation across the triadic environment model.

This README is the **front door** to the entire module.

---

Here is the **full formal specification** for qCompute.  
This is the *highest‑authority* document in the module: the normative, canonical, specification‑level definition of the entire compute harness.

It belongs at:

```
/docs/rtt/Inside/qCompute/qc_Spec.md
```

Everything below is **drop‑in‑ready**, structural, minimal, and fully aligned with the 2026 RTT‑Inside compute architecture.

---

# ✅ **qc_Spec.md — qCompute Formal Specification (2026)**

# qCompute — Formal Specification  
**File:** qc_Spec.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This document defines the **formal specification** of qCompute.  
It is the authoritative reference for:

- API semantics  
- operator grammar  
- environment rules  
- routing rules  
- validation rules  
- frame semantics  
- backend semantics  
- trace format  
- replay contract  
- invariants  

All other qCompute documents derive from this specification.

---

# 1. Definitions

### 1.1 Session
A **qSession** is the unit of coherence.  
It contains:

- environment  
- backend  
- drift bound  
- governance snapshot  
- lineage  
- trace buffer  

### 1.2 Environment
Environments form a forward‑only chain:

```
sandbox → production → archive
```

### 1.3 ResonanceFrame
A **ResonanceFrame** is the atomic compute envelope.  
It binds:

- backend  
- resonance profile  
- drift bound  
- environment  

### 1.4 Operator
An **operator** is a resonance‑time primitive with:

- name  
- parameters  
- resonance signature  
- drift profile  
- backend compatibility  

### 1.5 Trace
A **qTrace** is the canonical, append‑only record of:

- session metadata  
- lineage  
- frames  
- operations  
- routing metadata  
- validation metadata  
- drift measurements  

### 1.6 Replay
**qReplay** reconstructs and re‑executes a trace deterministically.

---

# 2. Session Specification

### 2.1 Creation

```
session = qSession(env, backend)
```

- `env ∈ {sandbox, production, archive}`
- `backend ∈ {explicit backend name, auto}`

### 2.2 Properties

```
session.env
session.backend
session.drift_bound
session.lineage
session.governance_snapshot
```

### 2.3 Drift Bounds

| Environment | Drift Bound |
|-------------|-------------|
| sandbox     | relaxed     |
| production  | strict      |
| archive     | immutable   |

### 2.4 Environment Transitions

Allowed:

```
sandbox → production
production → archive
```

Forbidden:

```
sandbox → archive
archive → production
archive → sandbox
production → sandbox
```

Transitions require:

- deploy token  
- closed frames  
- drift within bound  

---

# 3. Operator Specification

### 3.1 Grammar

```
operator_name(param=value, ...)
```

### 3.2 Categories

- primitive  
- composite  
- pulse  
- measurement  
- meta  

### 3.3 Required Metadata

Each operator defines:

- resonance tier ∈ {r1, r2, r3}  
- drift profile ∈ {low, medium, high}  
- backend compatibility  
- environment constraints  

### 3.4 Validation Rules

An operator is valid iff:

1. allowed by policy  
2. allowed in environment  
3. backend supports it  
4. resonance tier matches backend  
5. drift predicted ≤ drift bound  
6. restricted ops have token  

If invalid → operation blocked.

---

# 4. Routing Specification

### 4.1 Router Inputs

- operator  
- session  
- backend registry  
- resonance profiles  
- drift characteristics  
- policy rules  

### 4.2 Router Outputs

- selected backend  
- routing metadata  
- resonance alignment metadata  

### 4.3 Determinism

Routing must be deterministic:

```
same session + same operator → same route
```

### 4.4 Backend Switching

Allowed:

- Sandbox: between frames  
- Production: restricted  
- Archive: forbidden  

Never allowed mid‑frame.

---

# 5. ResonanceFrame Specification

### 5.1 Lifecycle

```
open → operate → close
```

### 5.2 Frame Fields

```
id
timestamp_open
timestamp_close
resonance_profile
drift_bound
backend
env
operations[]
```

### 5.3 Backend Binding

A frame binds to exactly one backend.  
Switching requires a new frame.

### 5.4 Drift Enforcement

If drift exceeds bound:

- frame closes  
- operation blocked  
- violation logged  

---

# 6. Validation Specification

TriadicValidator performs:

1. policy validation  
2. environment validation  
3. backend validation  
4. resonance validation  
5. drift validation  
6. restricted op validation  
7. lineage validation  

If any stage fails:

- operation blocked  
- lineage preserved  
- trace records failure  

Validator must be deterministic.

---

# 7. Trace Specification

### 7.1 Structure

```
header:
  session_id
  version
  env
  backend
  timestamp_start

lineage:
  - env
    timestamp
    token_used

frames:
  - id
    resonance_profile
    drift_bound
    backend
    env
    operations: [...]

operations:
  - id
    op
    params
    resonance
    drift
    backend
    env
    validation

footer:
  op_count
  frame_count
  hash
```

### 7.2 Append‑Only

Trace is append‑only.  
No mutation allowed.

### 7.3 Backward Compatibility

New fields must not break old traces.

---

# 8. Replay Specification

### 8.1 Replay Contract

Replay must:

- reconstruct session  
- reconstruct lineage  
- reconstruct frames  
- reconstruct routing  
- re‑execute deterministically  

Replay must not:

- reinterpret policy  
- reinterpret drift  
- reinterpret routing  
- mutate trace  

### 8.2 Determinism

Replay result must equal original result.

### 8.3 Safety

Replay cannot:

- execute new operations  
- transition environments  
- modify lineage  

---

# 9. Invariants (Normative)

These invariants MUST hold:

1. **Forward‑only environments**  
2. **Append‑only lineage**  
3. **Deterministic routing**  
4. **Backend binding per frame**  
5. **Drift cannot be ignored**  
6. **Archive is immutable**  
7. **No silent behavior**  
8. **Replay is strict**  
9. **Policy cannot rewrite history**  

Violating any invariant invalidates the implementation.

---

# 10. Compliance Requirements

A qCompute implementation is compliant if:

- all API semantics match this spec  
- all invariants hold  
- all routing is deterministic  
- all validation is deterministic  
- all traces are complete and append‑only  
- all replays are deterministic  
- all transitions follow triadic rules  

---

# 11. Summary

This document defines the **formal, normative specification** of qCompute:

- structural  
- governed  
- resonance‑aligned  
- drift‑bounded  
- deterministic  
- replay‑safe  
- student‑ready  

All qCompute components must conform to this specification.

---

Here is the **canonical backend‑resonance/drift metadata file** for qCompute.  
This file defines the *entire backend layer* of the compute harness: resonance tiers, drift envelopes, capabilities, constraints, and routing metadata.

It belongs at:

```
/docs/rtt/Inside/qCompute/qc_BackendProfiles.md
```

Everything below is **drop‑in‑ready**, structural, minimal, and fully aligned with the 2026 RTT‑Inside compute architecture.

---

# ✅ **qc_BackendProfiles.md — Backend Resonance & Drift Metadata (2026)**

# qCompute — Backend Profiles  
**File:** qc_BackendProfiles.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This file defines the **canonical backend metadata** used by qCompute for:

- resonance alignment  
- drift modeling  
- routing decisions  
- operator compatibility  
- environment constraints  

Backends are **metadata objects**, not drivers.  
They describe *what the backend is*, not *how it executes*.

---

# 1. Backend Metadata Schema

Each backend defines:

```yaml
backend_id: string
display_name: string
resonance_profile: r1 | r2 | r3
drift_characteristic: low | medium | high
capabilities:
  - primitive_ops
  - composite_ops
  - pulse_ops
  - measurement_ops
environment_constraints:
  sandbox: allowed | restricted | forbidden
  production: allowed | restricted | forbidden
  archive: forbidden
notes: optional string
```

Backends must be **pure metadata** — no execution logic.

---

# 2. Resonance Profiles

Backends declare one of three resonance tiers:

| Tier | Meaning | Use Case |
|------|---------|----------|
| **r1** | simulation‑first | local dev, teaching |
| **r2** | hybrid | mixed workloads |
| **r3** | hardware‑first | pulse‑level, strict drift |

Routing and validation depend on this field.

---

# 3. Drift Characteristics

Backends declare their drift envelope:

| Drift | Meaning |
|-------|---------|
| **low** | stable, predictable |
| **medium** | moderate drift |
| **high** | pulse‑level drift |

Drift must be ≤ frame drift bound.

---

# 4. Canonical Backend Profiles

Below are the **canonical backends** included with qCompute.

---

## 4.1 local-sim (Default Simulation Backend)

```yaml
backend_id: local-sim
display_name: Local Simulator
resonance_profile: r1
drift_characteristic: low
capabilities:
  - primitive_ops
  - composite_ops
  - measurement_ops
environment_constraints:
  sandbox: allowed
  production: allowed
  archive: forbidden
notes: >
  Default backend for auto-routing in Sandbox.
```

**Identity:**  
Stable, deterministic, idealized simulation.

---

## 4.2 hybrid-sim (Hybrid Resonance Simulator)

```yaml
backend_id: hybrid-sim
display_name: Hybrid Resonance Simulator
resonance_profile: r2
drift_characteristic: medium
capabilities:
  - primitive_ops
  - composite_ops
  - measurement_ops
environment_constraints:
  sandbox: allowed
  production: allowed
  archive: forbidden
notes: >
  Used for r2 operators and mixed workloads.
```

**Identity:**  
Bridges simulation and hardware‑like resonance behavior.

---

## 4.3 hardware-qpu-1 (Primary Hardware Backend)

```yaml
backend_id: hardware-qpu-1
display_name: Hardware QPU (Tier 1)
resonance_profile: r3
drift_characteristic: high
capabilities:
  - primitive_ops
  - composite_ops
  - pulse_ops
  - measurement_ops
environment_constraints:
  sandbox: restricted
  production: allowed
  archive: forbidden
notes: >
  Primary r3 backend for pulse-level operations.
```

**Identity:**  
Strict, drift‑sensitive, hardware‑aligned.

---

## 4.4 hardware-qpu-2 (High‑Stability Hardware Backend)

```yaml
backend_id: hardware-qpu-2
display_name: Hardware QPU (Tier 2)
resonance_profile: r3
drift_characteristic: medium
capabilities:
  - primitive_ops
  - composite_ops
  - pulse_ops
  - measurement_ops
environment_constraints:
  sandbox: restricted
  production: allowed
  archive: forbidden
notes: >
  Lower drift than QPU-1; preferred for long frames.
```

**Identity:**  
Hardware‑first but more stable than QPU‑1.

---

# 5. Backend Selection Rules

TriadicRouter selects a backend using:

1. **explicit backend** → always honored  
2. **auto mode** → resonance‑aligned selection  
3. **environment constraints** → enforced  
4. **drift bounds** → enforced  
5. **operator requirements** → enforced  

### 5.1 Auto‑Routing Priority

```
r1 op → local-sim
r2 op → hybrid-sim
r3 op → hardware-qpu-2 (preferred) → hardware-qpu-1 (fallback)
```

### 5.2 Sandbox Rules

- r1, r2 → allowed  
- r3 → restricted (requires explicit backend or policy override)  

### 5.3 Production Rules

- all backends allowed  
- restricted ops require token  

### 5.4 Archive Rules

- no backend allowed  
- no execution permitted  

---

# 6. Backend Compatibility Matrix

| Operator Type     | r1 (sim) | r2 (hybrid) | r3 (hardware) |
|-------------------|----------|-------------|----------------|
| primitive         | ✓        | ✓           | ✓              |
| composite         | ✓        | ✓           | ✓              |
| pulse             | ✗        | ✗           | ✓              |
| measurement       | ✓        | ✓           | ✓              |
| meta‑operators    | ✓        | ✓           | ✓              |

Pulse ops require r3.

---

# 7. Drift Enforcement Rules

A backend’s drift characteristic must satisfy:

```
drift_characteristic ≤ frame.drift_bound
```

Where drift_bound is:

- relaxed (Sandbox)  
- strict (Production)  
- immutable (Archive)  

If violated:

- operation blocked  
- frame closed  
- violation logged  

---

# 8. Backend Metadata Invariants

Backends must obey:

1. **No mid‑frame switching**  
2. **No execution in Archive**  
3. **Resonance profile is immutable**  
4. **Drift characteristic is immutable**  
5. **Capabilities must be explicit**  
6. **Environment constraints must be explicit**  
7. **Metadata must be deterministic**  

---

# 9. Summary

This file defines the **canonical backend metadata** for qCompute:

- resonance profiles  
- drift characteristics  
- capabilities  
- environment constraints  
- routing rules  
- invariants  

Backends are **metadata objects**, not drivers.  
They enable **resonance‑aligned**, **drift‑bounded**, **governed**, and **deterministic** computation across the triadic environment model.

---

Here is the **canonical qc_Capture.md** you need.  
Since you already have the file open in your GitHub editor (tab ID **1774656502**), I will generate a **clean, RTT/2‑grade, zero‑drift, drop‑in‑ready capture file** that matches the structure of all the other Inside‑module captures we’ve built (MP_Capture, SC_Capture, B_Capture, qc_Capture lineage, etc.).

This version is:

- **structural**  
- **operator‑first**  
- **triadic‑aware**  
- **resonance‑aligned**  
- **session‑context‑ready**  
- **student‑ready**  
- **AI‑parsable**  
- **zero conversational residue**  

It is the *canonical capture* for the entire qCompute module.

Paste this directly into:

```
/docs/rtt/Inside/qCompute/qc_Capture.md
```

---

# ✅ **qc_Capture.md — Canonical Capture (2026)**

# qCompute — Canonical Capture  
**File:** qc_Capture.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This capture defines the **identity**, **structure**, **operators**, **frames**, **routing**, **governance**, **drift model**, **trace contract**, and **replay semantics** of the qCompute module.

It is the authoritative structural description of the module.

---

# 1. Identity

**Module:** qCompute  
**Role:** Governed resonance‑aligned compute substrate  
**Domain:** RTT‑Inside  
**Purpose:** Provide a structural, deterministic, drift‑bounded, triadic‑aware compute harness for resonance‑time operations.

qCompute is not a simulator.  
It is a **structural execution layer** with governance, lineage, and deterministic replay.

---

# 2. What qCompute Provides

- operator grammar  
- resonance semantics  
- drift‑bounded execution  
- triadic environment transitions  
- backend routing  
- frame envelopes  
- governance enforcement  
- deterministic trace format  
- deterministic replay  

qCompute is the meeting point of:

**resonance × governance × drift × lineage**

---

# 3. Structural Model

qCompute is built from seven structural components:

1. **qSession** — unit of coherence  
2. **qCompute API** — operator surface  
3. **TriadicValidator** — safety gate  
4. **TriadicRouter** — routing brain  
5. **ResonanceFrame** — compute envelope  
6. **Backend Registry** — resonance/drift metadata  
7. **qTrace / qReplay** — recording + deterministic reconstruction  

These components form a **strict pipeline**:

```
Operator → Validator → Router → Frame → Backend → Trace
```

Replay reverses the pipeline.

---

# 4. Triadic Environment Model

qCompute uses the RTT‑Inside triadic model:

```
Sandbox → Production → Archive
```

### Sandbox  
- relaxed drift  
- exploratory  
- backend switching allowed  

### Production  
- strict drift  
- governed  
- restricted ops require token  

### Archive  
- immutable  
- replay‑only  
- zero drift  

Transitions are **forward‑only** and **lineage‑preserving**.

---

# 5. Operator Grammar

Operators follow the canonical grammar:

```
operator_name(param=value, ...)
```

### Categories

- primitive  
- composite  
- pulse  
- measurement  
- meta  

### Required metadata

Each operator defines:

- resonance tier (r1/r2/r3)  
- drift profile (low/medium/high)  
- backend compatibility  
- environment constraints  

Operators are **structural**, not symbolic.

---

# 6. ResonanceFrame

A ResonanceFrame is the **atomic compute envelope**.

It binds:

- backend  
- resonance profile  
- drift bound  
- environment  

Frames:

- open implicitly  
- close on `sync()`, `barrier()`, or transition  
- cannot switch backend mid‑frame  
- record drift and resonance metadata  

---

# 7. Routing Model

TriadicRouter selects:

- effective environment  
- backend  
- resonance alignment  
- drift envelope  

Routing is **deterministic**:

```
same session + same operator → same route
```

Auto‑routing uses resonance tier:

```
r1 → local-sim
r2 → hybrid-sim
r3 → hardware-qpu-2 → hardware-qpu-1
```

---

# 8. Drift Model

Drift is:

- predicted  
- measured  
- bounded  
- recorded  

Drift bounds:

| Environment | Bound |
|-------------|-------|
| Sandbox     | relaxed |
| Production  | strict |
| Archive     | immutable |

If drift exceeds bound:

- operation blocked  
- frame closed  
- violation logged  

---

# 9. Governance Model

TriadicValidator enforces:

- policy legality  
- environment rules  
- backend compatibility  
- resonance alignment  
- drift bounds  
- restricted op rules  
- lineage safety  

Governance Daemon:

- watches `qc_policy.yaml`  
- hot‑swaps policy safely  
- updates governance snapshots  
- never rewrites history  

---

# 10. Trace Contract

A `.qtrace` file records:

- header  
- lineage  
- frames  
- operations  
- routing metadata  
- validation metadata  
- drift measurements  
- footer hash  

Trace is **append‑only** and **backward‑compatible**.

---

# 11. Replay Contract

Replay must:

- reconstruct session  
- reconstruct lineage  
- reconstruct frames  
- reconstruct routing  
- re‑execute deterministically  

Replay must not:

- reinterpret policy  
- reinterpret drift  
- reinterpret routing  
- mutate trace  

Replay is **strict**, not heuristic.

---

# 12. Invariants

qCompute obeys the following invariants:

1. forward‑only environments  
2. append‑only lineage  
3. deterministic routing  
4. backend binding per frame  
5. drift cannot be ignored  
6. archive is immutable  
7. no silent behavior  
8. replay is strict  
9. policy cannot rewrite history  

These invariants define the module.

---

# 13. Minimal Example

```python
session = qSession(env="sandbox")
qc = qCompute(session)

qc.apply("hadamard", qubit=0)
qc.sync()

session.save_trace("example.qtrace")
```

Replay:

```python
qReplay("example.qtrace").run()
```

---

# 14. Summary

qCompute is the **governed, resonance‑aligned, drift‑bounded, deterministic compute substrate** of RTT‑Inside.

This capture defines its:

- identity  
- structure  
- operators  
- frames  
- routing  
- governance  
- drift model  
- trace contract  
- replay contract  
- invariants  

This file is the **canonical structural description** of the qCompute module.

---

Here is the **canonical TriadicRouter internals file** for qCompute.  
This completes the core triad of internals (Validator / Router / Frame) and matches the structural tone of the rest of the module.

It belongs at:

```
/docs/rtt/Inside/qCompute/qc_Router.md
```

Everything below is **drop‑in‑ready**, structural, minimal, and fully aligned with the 2026 RTT‑Inside compute architecture.

---

# ✅ **qc_Router.md — TriadicRouter Internals (2026)**

# qCompute — TriadicRouter Internals  
**File:** qc_Router.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

TriadicRouter is the **routing brain** of qCompute.  
It determines:

- effective environment  
- backend selection  
- resonance alignment  
- drift envelope  
- routing metadata  

Routing is **deterministic**, **governed**, and **replay‑compatible**.

---

# 1. Router Identity

TriadicRouter is responsible for:

1. Selecting the backend for each operator  
2. Enforcing resonance alignment  
3. Enforcing drift compatibility  
4. Respecting environment constraints  
5. Producing routing metadata for qTrace  
6. Ensuring deterministic behavior  

TriadicRouter does **not** execute operators.  
It only decides *where* they go.

---

# 2. Inputs & Outputs

## 2.1 Inputs

TriadicRouter receives:

- operator  
- operator metadata (resonance tier, drift profile, backend compatibility)  
- session (env, backend, drift bound)  
- backend registry  
- governance snapshot  
- frame state  

## 2.2 Outputs

TriadicRouter produces:

- selected backend  
- resonance alignment metadata  
- drift envelope metadata  
- routing decision record  
- frame‑binding decision  

All outputs are recorded in `.qtrace`.

---

# 3. Routing Algorithm (Canonical)

The routing algorithm follows a strict sequence:

```
1. Resolve effective environment
2. Resolve backend (explicit or auto)
3. Validate backend compatibility
4. Validate resonance alignment
5. Validate drift envelope
6. Bind backend to frame
7. Produce routing metadata
```

Each step is deterministic.

---

# 4. Environment Resolution

The effective environment is:

```
session.env
```

except during transitions, where the router:

- closes the current frame  
- applies transition rules  
- re‑binds routing metadata  

Archive always resolves to:

```
env = archive
backend = none
```

---

# 5. Backend Resolution

Backend resolution follows this priority:

## 5.1 Explicit Backend

If the session specifies a backend:

```
session.backend → always honored
```

unless:

- environment forbids it  
- operator is incompatible  
- drift bound is violated  

## 5.2 Auto Mode

If backend = `"auto"`:

```
r1 → local-sim
r2 → hybrid-sim
r3 → hardware-qpu-2 → hardware-qpu-1
```

Fallbacks are deterministic.

---

# 6. Backend Compatibility Rules

An operator is compatible with a backend iff:

1. backend supports operator category  
2. backend resonance tier ≥ operator resonance tier  
3. backend drift characteristic ≤ frame drift bound  
4. backend allowed in environment  

If any rule fails → routing error.

---

# 7. Resonance Alignment

Resonance alignment ensures:

```
operator.resonance_tier ≤ backend.resonance_profile
```

Examples:

- r1 op → r1/r2/r3 backend  
- r2 op → r2/r3 backend  
- r3 op → r3 backend only  

Pulse ops require r3.

---

# 8. Drift Envelope Enforcement

Drift enforcement ensures:

```
backend.drift_characteristic ≤ session.drift_bound
```

Where drift_bound is:

- relaxed (Sandbox)  
- strict (Production)  
- immutable (Archive)  

If violated:

- operation blocked  
- frame closed  
- violation logged  

---

# 9. Frame Binding

A ResonanceFrame binds to exactly one backend.

Rules:

- first op in frame → backend chosen  
- subsequent ops → backend must match  
- backend switch → new frame required  
- transitions → frame closes automatically  

Frame binding is recorded in trace.

---

# 10. Routing Metadata

TriadicRouter emits the following metadata per operation:

```yaml
routing:
  backend: hardware-qpu-2
  resonance_profile: r3
  drift_characteristic: medium
  env: production
  frame_id: frame-004
  reason: "auto-routed (r3 operator)"
```

Metadata must be:

- complete  
- deterministic  
- replay‑compatible  

---

# 11. Failure Modes

TriadicRouter may fail for:

- backend incompatibility  
- resonance mismatch  
- drift overflow  
- forbidden backend in environment  
- archive execution attempt  
- mid‑frame backend switch  

Failure behavior:

- operation blocked  
- frame closed (if needed)  
- violation logged  
- session remains coherent  

---

# 12. Replay Semantics

During replay:

- routing decisions are **not recomputed**  
- routing metadata is **read from trace**  
- backend selection is **exactly reproduced**  
- drift values are **not re‑evaluated**  

Replay is **strict**, not heuristic.

---

# 13. Invariants

TriadicRouter obeys:

1. **Deterministic routing**  
2. **No silent fallback**  
3. **No mid‑frame switching**  
4. **Environment constraints enforced**  
5. **Drift bounds enforced**  
6. **Resonance alignment enforced**  
7. **Replay determinism**  

Violating any invariant invalidates the router.

---

# 14. Summary

TriadicRouter is the **deterministic routing brain** of qCompute.

It ensures:

- resonance alignment  
- drift‑bounded execution  
- environment safety  
- backend correctness  
- deterministic replay  

Routing is structural, governed, and replay‑safe — never heuristic.

---

Here is the **canonical TriadicValidator internals file** for qCompute.  
This completes the core execution triad (Validator → Router → Frame) and matches the structural tone, minimality, and invariants of the rest of the Inside‑module documentation.

It belongs at:

```
/docs/rtt/Inside/qCompute/qc_Validator.md
```

Everything below is **drop‑in‑ready**, structural, zero‑drift, and fully aligned with the 2026 RTT‑Inside compute architecture.

---

# ✅ **qc_Validator.md — TriadicValidator Internals (2026)**

# qCompute — TriadicValidator Internals  
**File:** qc_Validator.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

TriadicValidator is the **safety gate** of qCompute.  
It ensures that every operator is:

- legal under governance policy  
- allowed in the current environment  
- compatible with the selected backend  
- resonance‑aligned  
- drift‑bounded  
- lineage‑safe  
- transition‑safe  

TriadicValidator is **deterministic**, **structural**, and **replay‑compatible**.

---

# 1. Validator Identity

TriadicValidator is responsible for:

1. enforcing governance policy  
2. enforcing environment rules  
3. enforcing backend compatibility  
4. enforcing resonance alignment  
5. enforcing drift bounds  
6. enforcing restricted‑operation rules  
7. enforcing lineage and transition safety  
8. emitting validation metadata  

It does **not** execute operators and does **not** route them.  
It only determines whether an operation is **allowed**.

---

# 2. Inputs & Outputs

## 2.1 Inputs

TriadicValidator receives:

- operator  
- operator metadata (resonance tier, drift profile, category)  
- session (env, backend, drift bound, lineage)  
- governance snapshot  
- backend registry  
- frame state  

## 2.2 Outputs

TriadicValidator produces:

- validation result (allow / block)  
- reason code  
- drift envelope metadata  
- environment metadata  
- restricted‑op metadata  
- transition metadata  

All outputs are recorded in `.qtrace`.

---

# 3. Validation Pipeline (Canonical)

Validation follows a strict sequence:

```
1. Policy validation
2. Environment validation
3. Backend validation
4. Resonance validation
5. Drift validation
6. Restricted-op validation
7. Lineage validation
8. Transition validation (if applicable)
```

If any stage fails → operation blocked.

Validator must be **deterministic**.

---

# 4. Policy Validation

TriadicValidator checks:

- operator allowed by policy  
- operator category allowed  
- operator parameters allowed  
- operator not globally restricted  
- operator not environment‑restricted  

Policy is defined in:

```
qc_policy.yaml
```

Policy updates are **forward‑only** and **never retroactive**.

---

# 5. Environment Validation

Rules:

### Sandbox
- relaxed drift  
- all primitive/composite ops allowed  
- pulse ops restricted  
- transitions allowed only to Production  

### Production
- strict drift  
- restricted ops require token  
- transitions allowed only to Archive  

### Archive
- no execution allowed  
- no backend allowed  
- no frame creation allowed  

If environment forbids the operator → block.

---

# 6. Backend Validation

Validator ensures:

1. backend supports operator category  
2. backend allowed in environment  
3. backend resonance tier ≥ operator resonance tier  
4. backend drift characteristic ≤ session drift bound  

If backend is incompatible → block.

---

# 7. Resonance Validation

Resonance alignment rule:

```
operator.resonance_tier ≤ backend.resonance_profile
```

Examples:

- r1 op → r1/r2/r3 backend  
- r2 op → r2/r3 backend  
- r3 op → r3 backend only  

Pulse ops require r3.

If resonance mismatch → block.

---

# 8. Drift Validation

Drift validation ensures:

```
predicted_drift ≤ session.drift_bound
```

Where drift_bound is:

- relaxed (Sandbox)  
- strict (Production)  
- immutable (Archive)  

If drift exceeds bound:

- operation blocked  
- frame closed  
- violation logged  

Drift is **never ignored**.

---

# 9. Restricted‑Operation Validation

Restricted ops include:

- pulse operators  
- backend‑switch meta‑operators  
- environment transitions  
- high‑drift operators  
- hardware‑specific operators  

Restricted ops require:

- explicit token  
- correct environment  
- correct backend  
- correct resonance tier  

If token missing → block.

---

# 10. Lineage Validation

Validator ensures:

- lineage is append‑only  
- no backward transitions  
- no environment skipping  
- no lineage mutation  

Allowed transitions:

```
sandbox → production → archive
```

Forbidden transitions:

```
sandbox → archive
production → sandbox
archive → anything
```

If lineage rule violated → block.

---

# 11. Transition Validation

Transition operators (`transition`, `deploy_token`) must satisfy:

- frame closed  
- token present  
- environment progression valid  
- drift within bound  
- governance snapshot updated  

If any condition fails → block.

---

# 12. Validation Metadata

Validator emits metadata per operation:

```yaml
validation:
  allowed: true
  reason: "resonance-aligned"
  env: production
  drift_ok: true
  backend_ok: true
  restricted_op: false
  lineage_ok: true
```

Metadata must be:

- complete  
- deterministic  
- replay‑compatible  

---

# 13. Failure Modes

Validator may block operations for:

- policy violation  
- environment violation  
- backend incompatibility  
- resonance mismatch  
- drift overflow  
- missing token  
- illegal transition  
- archive execution attempt  

Failure behavior:

- operation blocked  
- frame closed (if needed)  
- violation logged  
- session remains coherent  

---

# 14. Replay Semantics

During replay:

- validation is **not recomputed**  
- validation metadata is **read from trace**  
- no new validation occurs  
- no policy is re‑applied  

Replay is **strict**, not heuristic.

---

# 15. Invariants

TriadicValidator obeys:

1. **No silent behavior**  
2. **Deterministic validation**  
3. **Forward‑only environments**  
4. **Append‑only lineage**  
5. **Drift cannot be ignored**  
6. **Archive is immutable**  
7. **Policy cannot rewrite history**  
8. **Replay determinism**  

Violating any invariant invalidates the validator.

---

# 16. Summary

TriadicValidator is the **deterministic safety gate** of qCompute.

It ensures:

- policy legality  
- environment safety  
- backend correctness  
- resonance alignment  
- drift‑bounded execution  
- restricted‑op safety  
- lineage integrity  
- transition correctness  
- replay determinism  

Validator is structural, governed, and replay‑safe — never heuristic.

---

Here is the **canonical ResonanceFrame internals file** for qCompute.  
This completes the core execution triad (Validator → Router → Frame) and gives the frame the same structural clarity and invariance‑tight definition as the rest of the Inside‑module.

It belongs at:

```
/docs/rtt/Inside/qCompute/qc_ResonanceFrame.md
```

Everything below is **drop‑in‑ready**, structural, minimal, and fully aligned with the 2026 RTT‑Inside compute architecture.

---

# ✅ **qc_ResonanceFrame.md — ResonanceFrame Internals (2026)**

# qCompute — ResonanceFrame Internals  
**File:** qc_ResonanceFrame.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

A **ResonanceFrame** is the atomic compute envelope of qCompute.  
It is the lowest‑level structural container in the execution pipeline and the unit of:

- backend binding  
- resonance alignment  
- drift enforcement  
- environment enforcement  
- temporal grouping  
- trace segmentation  

Frames ensure that all computation is **bounded**, **governed**, **deterministic**, and **replay‑safe**.

---

# 1. Frame Identity

A ResonanceFrame is:

- a **temporal envelope** for operations  
- a **resonance‑tier container**  
- a **drift‑bounded region**  
- a **backend‑bound region**  
- a **trace segment**  
- a **routing boundary**  

Frames are **structural**, not behavioral.

---

# 2. Frame Lifecycle

A frame has a strict lifecycle:

```
open → operate → close
```

### 2.1 Opening
A frame opens:

- implicitly on the first operator  
- explicitly on environment transition  
- explicitly on backend switch  
- implicitly after a previous frame closes  

### 2.2 Operating
While open, the frame:

- accumulates operations  
- enforces drift bound  
- enforces resonance tier  
- enforces backend binding  
- records metadata  

### 2.3 Closing
A frame closes on:

- `qc.sync()`  
- `qc.barrier()`  
- environment transition  
- backend switch  
- drift overflow  
- session termination  

Closing a frame is **structural**, not optional.

---

# 3. Frame Structure

Each frame records:

```yaml
frame_id: frame-###
timestamp_open: ISO-8601
timestamp_close: ISO-8601
env: sandbox | production | archive
backend: backend-id
resonance_profile: r1 | r2 | r3
drift_bound: relaxed | strict | immutable
operations: [...]
drift_summary:
  predicted: float
  measured: float
```

Frames are **append‑only** and **never mutated**.

---

# 4. Backend Binding

A frame binds to exactly **one backend**.

Rules:

1. First operator determines backend  
2. All subsequent operators must use the same backend  
3. Backend switch → new frame  
4. Archive → no backend allowed  
5. Replay → backend read from trace, never recomputed  

Backend binding is a **hard invariant**.

---

# 5. Resonance Alignment

A frame enforces:

```
operator.resonance_tier ≤ frame.resonance_profile
```

Examples:

- r1 op → allowed in r1/r2/r3 frame  
- r2 op → allowed in r2/r3 frame  
- r3 op → allowed only in r3 frame  

Pulse ops require r3.

If resonance mismatch → operation blocked.

---

# 6. Drift Enforcement

A frame enforces:

```
predicted_drift ≤ frame.drift_bound
```

Where drift_bound is:

- relaxed (Sandbox)  
- strict (Production)  
- immutable (Archive)  

If drift exceeds bound:

- operation blocked  
- frame closed  
- violation logged  

Drift is **never ignored**.

---

# 7. Environment Enforcement

A frame inherits the session environment:

```
frame.env = session.env
```

Rules:

- Sandbox → relaxed drift, flexible routing  
- Production → strict drift, governed ops  
- Archive → no execution allowed  

Environment changes close the current frame.

---

# 8. Operation Accumulation

Frames accumulate operations in order:

```
operations = [
  {op, params, resonance, drift, backend, env, validation},
  ...
]
```

Operations are:

- validated  
- routed  
- drift‑checked  
- appended to frame  

Operations are **never reordered**.

---

# 9. Frame Closure Semantics

Closing a frame:

- finalizes drift summary  
- finalizes resonance metadata  
- finalizes backend binding  
- writes frame to trace  
- resets frame state  

Frame closure is **deterministic** and **replay‑safe**.

---

# 10. Replay Semantics

During replay:

- frames are reconstructed exactly  
- backend binding is read from trace  
- resonance tier is read from trace  
- drift summary is read from trace  
- operations are re‑executed deterministically  

Replay does **not**:

- recompute drift  
- recompute routing  
- recompute resonance alignment  
- recompute validation  

Replay is **strict**, not heuristic.

---

# 11. Failure Modes

A frame may close early due to:

- drift overflow  
- backend switch attempt  
- environment transition  
- restricted op violation  
- archive execution attempt  
- governance violation  

Failure behavior:

- operation blocked  
- frame closed  
- violation logged  
- session remains coherent  

---

# 12. Invariants

ResonanceFrame obeys:

1. **Backend binding per frame**  
2. **Resonance alignment**  
3. **Drift enforcement**  
4. **Environment inheritance**  
5. **Append‑only operations**  
6. **Deterministic closure**  
7. **Replay determinism**  
8. **No silent behavior**  

Violating any invariant invalidates the frame.

---

# 13. Summary

ResonanceFrame is the **atomic compute envelope** of qCompute.

It ensures:

- resonance alignment  
- drift‑bounded execution  
- backend correctness  
- environment safety  
- deterministic grouping  
- trace segmentation  
- replay fidelity  

Frames make qCompute **structural**, **governed**, and **replay‑safe**.

---

Here is the **canonical multi‑backend orchestration spec** for qCompute.  
This file completes the execution‑layer triad by describing how qCompute coordinates **multiple backends**, **multiple resonance tiers**, and **multiple frames** under a single governed session.

It belongs at:

```
/docs/rtt/Inside/qCompute/qc_Orchestration.md
```

Everything below is **drop‑in‑ready**, structural, minimal, and fully aligned with the 2026 RTT‑Inside compute architecture.

---

# ✅ **qc_Orchestration.md — Multi‑Backend Orchestration Specification (2026)**

# qCompute — Multi‑Backend Orchestration  
**File:** qc_Orchestration.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This document defines the **multi‑backend orchestration model** for qCompute.  
It specifies how qCompute coordinates:

- multiple backends  
- multiple resonance tiers  
- multiple drift envelopes  
- multiple frames  
- multiple routing decisions  

under a single governed session.

Orchestration is **structural**, **deterministic**, and **replay‑safe**.

---

# 1. Orchestration Identity

Multi‑backend orchestration is the mechanism that allows qCompute to:

- route different operators to different backends  
- open and close frames as needed  
- enforce drift and resonance constraints  
- maintain deterministic lineage  
- produce a unified `.qtrace`  

Orchestration is **not parallel execution**.  
It is **sequential, governed routing** across multiple substrates.

---

# 2. Orchestration Pipeline

The orchestration pipeline extends the standard compute pipeline:

```
Operator
    ↓
TriadicValidator
    ↓
TriadicRouter
    ↓
ResonanceFrame (backend-bound)
    ↓
Backend Execution
    ↓
qTrace Append
```

Multi‑backend orchestration adds:

```
Frame Switching
Backend Switching
Environment Transitions
Resonance Tier Escalation
Drift Envelope Enforcement
```

All of these are deterministic.

---

# 3. Backend Switching Rules

Backend switching is allowed **only between frames**, never inside a frame.

### 3.1 Allowed

```
frame-001 (local-sim)
    ↓ sync()
frame-002 (hardware-qpu-2)
```

### 3.2 Forbidden

```
frame-001 (local-sim)
    ↓ apply("pulse", qubit=0)  ← requires r3 backend
```

This triggers:

- frame closure  
- routing to r3 backend  
- new frame creation  

### 3.3 Archive

Archive forbids all execution:

```
backend = none
```

---

# 4. Resonance‑Tier Escalation

Operators may require higher resonance tiers:

```
r1 → r2 → r3
```

Escalation rules:

- r1 op in r1 frame → allowed  
- r2 op in r1 frame → closes r1 frame → opens r2 frame  
- r3 op in r2 frame → closes r2 frame → opens r3 frame  

Resonance tier **never decreases** within a frame.

---

# 5. Drift Envelope Enforcement

Each backend has a drift characteristic:

```
low / medium / high
```

Each environment has a drift bound:

```
relaxed / strict / immutable
```

Orchestration enforces:

```
backend.drift_characteristic ≤ session.drift_bound
```

If violated:

- frame closes  
- operation blocked  
- violation logged  

---

# 6. Multi‑Backend Frame Model

A session may contain many frames:

```
frame-001: r1, local-sim
frame-002: r2, hybrid-sim
frame-003: r3, hardware-qpu-2
frame-004: r1, local-sim (after transition)
```

Each frame is:

- backend‑bound  
- resonance‑tier‑bound  
- drift‑bound  
- environment‑bound  

Frames are **independent envelopes**.

---

# 7. Orchestration Scenarios

## 7.1 Scenario A — Mixed Resonance Workflow

```
qc.apply("hadamard", qubit=0)      → r1 → local-sim → frame-001
qc.apply("cnot", control=0, target=1) → r2 → hybrid-sim → frame-002
qc.apply("pulse", qubit=0)         → r3 → hardware-qpu-2 → frame-003
```

Three frames, three backends, deterministic.

---

## 7.2 Scenario B — Production Workflow

```
session.env = production
session.backend = auto

qc.apply("x", qubit=0)             → r1 → local-sim
qc.apply("measure", qubit=0)       → r1 → local-sim
qc.apply("pulse", qubit=0)         → r3 → hardware-qpu-2
```

Production enforces strict drift.

---

## 7.3 Scenario C — Transition Workflow

```
Sandbox → Production → Archive
```

Transitions close frames:

```
frame-001 (sandbox)
    ↓ transition("production")
frame-002 (production)
    ↓ transition("archive")
frame-003 (archive, empty)
```

Archive forbids execution.

---

# 8. Orchestration Metadata

Each routing decision produces metadata:

```yaml
orchestration:
  backend: hardware-qpu-2
  resonance_profile: r3
  drift_characteristic: medium
  frame_id: frame-003
  reason: "resonance escalation"
```

Metadata must be:

- complete  
- deterministic  
- replay‑compatible  

---

# 9. Replay Semantics

Replay reconstructs:

- frame boundaries  
- backend selection  
- resonance tiers  
- drift envelopes  
- routing decisions  

Replay does **not** recompute orchestration.  
It **reads orchestration metadata from trace**.

Replay is **strict**, not heuristic.

---

# 10. Invariants

Orchestration obeys:

1. **No mid‑frame backend switching**  
2. **Resonance tier never decreases within a frame**  
3. **Drift bound always enforced**  
4. **Environment transitions close frames**  
5. **Archive forbids execution**  
6. **Routing is deterministic**  
7. **Replay is deterministic**  
8. **No silent behavior**  

Violating any invariant invalidates orchestration.

---

# 11. Summary

Multi‑backend orchestration in qCompute is:

- structural  
- deterministic  
- resonance‑aligned  
- drift‑bounded  
- environment‑aware  
- backend‑aware  
- replay‑safe  

It enables complex, multi‑tier compute workflows while preserving the strict invariants of the RTT‑Inside architecture.

---

Here is the **canonical `.qtrace` schema file** for qCompute.  
This is one of the *most important* structural documents in the entire Inside‑module: it defines the **recording contract** that makes qCompute replay‑deterministic, lineage‑safe, and triadic‑aware.

It belongs at:

```
/docs/rtt/Inside/qCompute/qc_TraceFormat.md
```

Everything below is **drop‑in‑ready**, structural, minimal, and fully aligned with the 2026 RTT‑Inside compute architecture.

---

# ✅ **qc_TraceFormat.md — Canonical `.qtrace` Schema (2026)**

# qCompute — Canonical .qtrace Schema  
**File:** qc_TraceFormat.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This document defines the **canonical `.qtrace` file format** used by qCompute.  
A `.qtrace` file is the **complete, deterministic, append‑only record** of:

- session metadata  
- lineage  
- frames  
- operations  
- routing decisions  
- validation decisions  
- drift measurements  
- environment transitions  
- backend bindings  

Replay depends on this format being **strict**, **structural**, and **backward‑compatible**.

---

# 1. File Identity

```
Format: qTrace v2026
Type: Structured, append‑only, replay‑deterministic
Purpose: Deterministic reconstruction of qCompute sessions
```

A `.qtrace` file must allow:

- full session reconstruction  
- full lineage reconstruction  
- full frame reconstruction  
- deterministic re‑execution  

Replay is **strict**, not heuristic.

---

# 2. Top‑Level Structure

A `.qtrace` file contains exactly four top‑level sections:

```
header
lineage
frames
footer
```

Each section is required.

---

# 3. Header Schema

The header defines the session identity.

```yaml
header:
  version: "2026.1"
  session_id: "sess-abc123"
  timestamp_start: "2026-06-24T19:00:00Z"
  env: "sandbox"
  backend: "auto"
  drift_bound: "relaxed"
  governance_snapshot:
    policy_version: "1.4.2"
    hash: "sha256-..."
```

### Header Rules

- `session_id` is immutable  
- `env` is the environment at session start  
- `backend` is the initial backend (explicit or auto)  
- `governance_snapshot` is captured at session creation  

---

# 4. Lineage Schema

Lineage records all environment transitions.

```yaml
lineage:
  - env: "sandbox"
    timestamp: "2026-06-24T19:00:00Z"
    token_used: null

  - env: "production"
    timestamp: "2026-06-24T19:05:12Z"
    token_used: "prod-2026-001"

  - env: "archive"
    timestamp: "2026-06-24T19:07:44Z"
    token_used: "arch-2026-001"
```

### Lineage Rules

- append‑only  
- forward‑only  
- no skipping environments  
- no mutation  
- no deletion  

---

# 5. Frames Schema

Frames are the atomic compute envelopes.

```yaml
frames:
  - frame_id: "frame-001"
    timestamp_open: "2026-06-24T19:00:01Z"
    timestamp_close: "2026-06-24T19:00:03Z"
    env: "sandbox"
    backend: "local-sim"
    resonance_profile: "r1"
    drift_bound: "relaxed"

    operations:
      - op_id: "op-001"
        name: "hadamard"
        params: { qubit: 0 }
        resonance_tier: "r1"
        drift_predicted: 0.01
        drift_measured: 0.01

        validation:
          allowed: true
          reason: "ok"
          restricted_op: false
          env_ok: true
          backend_ok: true
          drift_ok: true
          lineage_ok: true

        routing:
          backend: "local-sim"
          resonance_profile: "r1"
          drift_characteristic: "low"
          frame_id: "frame-001"
          reason: "auto-routed (r1 operator)"

    drift_summary:
      predicted_total: 0.01
      measured_total: 0.01
```

### Frame Rules

- backend is fixed per frame  
- resonance tier never decreases  
- drift must remain within bound  
- operations are strictly ordered  
- frame closure is deterministic  

---

# 6. Operation Schema

Each operation records:

```yaml
op_id: "op-###"
name: "operator_name"
params: { ... }

resonance_tier: "r1|r2|r3"
drift_predicted: float
drift_measured: float

validation:
  allowed: true|false
  reason: string
  restricted_op: true|false
  env_ok: true|false
  backend_ok: true|false
  drift_ok: true|false
  lineage_ok: true|false

routing:
  backend: backend-id
  resonance_profile: r1|r2|r3
  drift_characteristic: low|medium|high
  frame_id: frame-###
  reason: string
```

### Operation Rules

- validation is recorded, not recomputed  
- routing is recorded, not recomputed  
- drift is recorded, not recomputed  
- params must be explicit  

---

# 7. Footer Schema

The footer finalizes the trace.

```yaml
footer:
  op_count: 42
  frame_count: 7
  hash: "sha256-..."
```

### Footer Rules

- `hash` covers the entire file except the footer  
- ensures integrity  
- ensures replay determinism  

---

# 8. Determinism Requirements

A `.qtrace` file must allow:

- deterministic reconstruction  
- deterministic routing  
- deterministic drift behavior  
- deterministic validation  
- deterministic environment transitions  

Replay must not:

- infer missing data  
- reinterpret policy  
- reinterpret drift  
- reinterpret routing  
- reinterpret lineage  

Replay is **strict**, not heuristic.

---

# 9. Backward Compatibility

The `.qtrace` format is:

- append‑only  
- forward‑compatible  
- backward‑compatible  

New fields may be added, but:

- no field may be removed  
- no field may be renamed  
- no semantic meaning may change  

---

# 10. Invariants

A `.qtrace` file must obey:

1. **Forward‑only environments**  
2. **Append‑only lineage**  
3. **Deterministic routing**  
4. **Backend binding per frame**  
5. **Drift cannot be ignored**  
6. **Archive is immutable**  
7. **No silent behavior**  
8. **Replay is strict**  
9. **Trace is append‑only**  

Violating any invariant invalidates the trace.

---

# 11. Summary

The `.qtrace` format is the **structural backbone** of qCompute.

It ensures:

- deterministic replay  
- deterministic routing  
- deterministic drift behavior  
- deterministic validation  
- lineage integrity  
- environment safety  
- backend correctness  

This file defines the **canonical schema** for all qCompute traces.

---

Here is the **canonical operator‑grammar + resonance‑semantics file** for qCompute.  
This is one of the *core structural documents* of the entire compute harness: it defines what an operator **is**, how it behaves, how it binds to resonance tiers, how it interacts with drift, and how it is validated and routed.

It belongs at:

```
/docs/rtt/Inside/qCompute/qc_Operators.md
```

Everything below is **drop‑in‑ready**, structural, minimal, and fully aligned with the 2026 RTT‑Inside compute architecture.

---

# ✅ **qc_Operators.md — Operator Grammar & Resonance Semantics (2026)**

# qCompute — Operator Grammar & Resonance Semantics  
**File:** qc_Operators.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This document defines the **operator grammar**, **resonance semantics**, **drift profiles**, and **backend compatibility rules** for all qCompute operators.

Operators are the **atomic resonance‑time primitives** of the qCompute module.  
They are structural, not symbolic.

---

# 1. Operator Identity

An operator in qCompute is:

- a **resonance‑time action**  
- with explicit parameters  
- with a defined resonance tier  
- with a defined drift profile  
- with backend compatibility  
- with environment constraints  
- validated deterministically  
- routed deterministically  
- recorded structurally in `.qtrace`  

Operators are **not** algebraic gates or symbolic expressions.  
They are **governed structural actions**.

---

# 2. Operator Grammar

The canonical grammar is:

```
operator_name(param=value, ...)
```

### 2.1 Required fields

Every operator defines:

- **name**  
- **category** (primitive, composite, pulse, measurement, meta)  
- **parameters** (explicit, typed)  
- **resonance tier** (r1/r2/r3)  
- **drift profile** (low/medium/high)  
- **backend compatibility**  
- **environment constraints**  

### 2.2 Parameter rules

- all parameters must be explicit  
- no positional parameters  
- no implicit defaults  
- no symbolic expressions  

Example:

```
cnot(control=0, target=1)
```

---

# 3. Operator Categories

Operators fall into five canonical categories:

## 3.1 Primitive Operators

Basic resonance‑time actions.

Examples:

- `x(qubit=0)`  
- `z(qubit=1)`  
- `hadamard(qubit=0)`  

**Resonance tier:** r1  
**Drift:** low  
**Backends:** r1/r2/r3  
**Environments:** sandbox, production  

---

## 3.2 Composite Operators

Multi‑step structural actions.

Examples:

- `cnot(control=0, target=1)`  
- `swap(q0=0, q1=1)`  

**Resonance tier:** r2  
**Drift:** medium  
**Backends:** r2/r3  
**Environments:** sandbox, production  

---

## 3.3 Pulse Operators

Hardware‑level resonance primitives.

Examples:

- `pulse(qubit=0, duration=32ns, amplitude=0.8)`  
- `rz_pulse(qubit=1, theta=1.57)`  

**Resonance tier:** r3  
**Drift:** high  
**Backends:** r3 only  
**Environments:** production only (token required)  

Pulse ops are **restricted**.

---

## 3.4 Measurement Operators

State‑extraction primitives.

Examples:

- `measure(qubit=0)`  
- `measure_all()`  

**Resonance tier:** r1  
**Drift:** low  
**Backends:** r1/r2/r3  
**Environments:** sandbox, production  

---

## 3.5 Meta‑Operators

Structural actions.

Examples:

- `barrier()`  
- `sync()`  
- `transition(env="production")`  
- `deploy_token(value="prod-2026-001")`  

**Resonance tier:** none  
**Drift:** none  
**Backends:** none  
**Environments:** governed by policy  

Meta‑operators do not execute on backends.

---

# 4. Resonance Semantics

Each operator declares a **resonance tier**:

| Tier | Meaning | Allowed Backends |
|------|---------|------------------|
| **r1** | simulation‑first | r1, r2, r3 |
| **r2** | hybrid resonance | r2, r3 |
| **r3** | hardware‑first | r3 only |

### 4.1 Resonance alignment rule

```
operator.resonance_tier ≤ backend.resonance_profile
```

Examples:

- r1 op → allowed everywhere  
- r2 op → hybrid or hardware  
- r3 op → hardware only  

### 4.2 Resonance escalation

If an operator requires a higher tier than the current frame:

- close current frame  
- open new frame with higher tier  
- bind backend accordingly  

Resonance tier **never decreases** within a frame.

---

# 5. Drift Semantics

Each operator declares a **drift profile**:

| Drift | Meaning |
|-------|---------|
| **low** | stable, predictable |
| **medium** | moderate drift |
| **high** | pulse‑level drift |

### 5.1 Drift enforcement rule

```
operator.drift_predicted ≤ session.drift_bound
```

Where drift_bound is:

- relaxed (Sandbox)  
- strict (Production)  
- immutable (Archive)  

If drift exceeds bound:

- operation blocked  
- frame closed  
- violation logged  

Drift is **never ignored**.

---

# 6. Backend Compatibility

Each operator declares backend compatibility:

| Category   | r1 | r2 | r3 |
|------------|----|----|----|
| primitive  | ✓  | ✓  | ✓  |
| composite  | ✓  | ✓  | ✓  |
| pulse      | ✗  | ✗  | ✓  |
| measurement| ✓  | ✓  | ✓  |
| meta       | n/a| n/a| n/a|

Pulse ops require r3.

---

# 7. Environment Constraints

Operators may be restricted by environment:

| Operator Type | Sandbox | Production | Archive |
|---------------|---------|------------|---------|
| primitive     | ✓       | ✓          | ✗       |
| composite     | ✓       | ✓          | ✗       |
| pulse         | restricted | ✓ (token) | ✗ |
| measurement   | ✓       | ✓          | ✗       |
| meta          | governed | governed   | governed |

Archive forbids all execution.

---

# 8. Validation Semantics

TriadicValidator enforces:

1. policy legality  
2. environment legality  
3. backend compatibility  
4. resonance alignment  
5. drift bounds  
6. restricted‑op rules  
7. lineage safety  

Validation is **deterministic** and **recorded**, not recomputed during replay.

---

# 9. Routing Semantics

TriadicRouter uses operator metadata to:

- select backend  
- enforce resonance tier  
- enforce drift envelope  
- open/close frames  
- produce routing metadata  

Routing is **deterministic** and **replay‑safe**.

---

# 10. Trace Semantics

Each operator is recorded in `.qtrace` with:

- name  
- params  
- resonance tier  
- drift predicted  
- drift measured  
- validation metadata  
- routing metadata  
- frame binding  

Operators are **never mutated** after recording.

---

# 11. Replay Semantics

During replay:

- operators are re‑executed deterministically  
- routing is read from trace  
- validation is read from trace  
- drift is read from trace  
- resonance tier is read from trace  

Replay does **not** recompute semantics.

---

# 12. Invariants

Operators obey:

1. **Explicit parameters only**  
2. **Resonance tier declared**  
3. **Drift profile declared**  
4. **Backend compatibility declared**  
5. **Environment constraints declared**  
6. **No silent behavior**  
7. **Replay determinism**  

Violating any invariant invalidates the operator.

---

# 13. Summary

This document defines the **canonical operator grammar** and **resonance semantics** for qCompute:

- structural  
- governed  
- resonance‑aligned  
- drift‑bounded  
- backend‑aware  
- environment‑aware  
- replay‑safe  

Operators are the atomic building blocks of the entire compute harness.

---

Here we go, **canonical session internals + lifecycle** for qCompute, in the same structural key as the rest.

Place at:

`/docs/rtt/Inside/qCompute/qc_Session.md`

---

### ✅ qc_Session.md — Session Internals & Lifecycle (2026)

# qCompute — Session Internals & Lifecycle  
**File:** qc_Session.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

A **qSession** is the unit of coherence in qCompute.  
It is the container for:

- environment  
- backend intent  
- drift bound  
- governance snapshot  
- lineage  
- frames  
- trace buffer  

All execution, routing, validation, and replay are scoped to a session.

---

# 1. Session Identity

A qSession is:

- a **triadic environment container**  
- a **drift‑bounded context**  
- a **backend‑intent container**  
- a **lineage root**  
- a **trace root**  

It is the smallest unit that can be:

- created  
- transitioned  
- archived  
- replayed  

---

# 2. Creation & Basic Fields

## 2.1 Creation

```python
session = qSession(env="sandbox", backend="auto")
```

## 2.2 Core fields

```text
session.id                 # immutable session identifier
session.env                # sandbox | production | archive
session.backend            # explicit backend id | "auto"
session.drift_bound        # relaxed | strict | immutable
session.governance_snapshot
session.lineage
session.trace_buffer
```

### 2.3 Drift bound by environment

| Environment | Drift bound |
|-------------|------------|
| sandbox     | relaxed    |
| production  | strict     |
| archive     | immutable  |

---

# 3. Lifecycle Overview

A session follows this lifecycle:

```text
create → operate → transition(s) → archive → replay
```

1. **create** — env + backend + governance snapshot  
2. **operate** — frames + operators + traces  
3. **transition(s)** — sandbox → production → archive  
4. **archive** — immutable, replay‑only  
5. **replay** — deterministic reconstruction

---

# 4. Environment Semantics

## 4.1 Allowed environments

```text
sandbox → production → archive
```

## 4.2 Rules

- **Sandbox**  
  - relaxed drift  
  - exploratory  
  - backend switching allowed (between frames)  

- **Production**  
  - strict drift  
  - governed  
  - restricted ops require token  

- **Archive**  
  - no execution  
  - no backend  
  - replay‑only  

Backward or skipping transitions are forbidden.

---

# 5. Lineage

`session.lineage` is the append‑only record of environment transitions.

Example:

```yaml
lineage:
  - env: "sandbox"
    timestamp: "2026-06-24T19:00:00Z"
    token_used: null

  - env: "production"
    timestamp: "2026-06-24T19:05:12Z"
    token_used: "prod-2026-001"

  - env: "archive"
    timestamp: "2026-06-24T19:07:44Z"
    token_used: "arch-2026-001"
```

Lineage is:

- forward‑only  
- append‑only  
- never mutated  

---

# 6. Tokens & Governance Snapshot

## 6.1 Tokens

Tokens authorize:

- production entry  
- archive entry  
- restricted operations  

Example:

```python
session.deploy_token("prod-2026-001")
session.transition("production")
```

## 6.2 Governance snapshot

On creation, the session captures:

```yaml
governance_snapshot:
  policy_version: "1.4.2"
  hash: "sha256-..."
```

This snapshot is:

- immutable for the session  
- recorded in `.qtrace` header  
- used for replay context  

Policy updates do **not** rewrite past sessions.

---

# 7. Frames Within a Session

A session owns a sequence of **ResonanceFrames**:

```text
session.frames = [frame-001, frame-002, ...]
```

Frames:

- inherit `session.env` and `session.drift_bound`  
- bind to a backend (explicit or auto‑resolved)  
- group operations temporally  
- are written to `.qtrace`  

Frame boundaries are driven by:

- `sync()` / `barrier()`  
- backend changes  
- resonance tier escalation  
- environment transitions  
- drift overflow  

---

# 8. Session Methods (Conceptual)

Conceptual API surface:

```python
session = qSession(env="sandbox", backend="auto")

session.deploy_token(value: str)
session.transition(env: str)      # sandbox→production→archive

session.save_trace(path: str)
session.close()                   # closes open frame, finalizes trace
```

All methods are:

- structural  
- deterministic  
- trace‑aware  

---

# 9. Trace Integration

A session is the root of a `.qtrace` file:

- `header` ← session identity + governance snapshot  
- `lineage` ← session transitions  
- `frames` ← session frames  
- `footer` ← counts + hash  

`session.save_trace("example.qtrace")`:

- closes any open frame  
- finalizes footer  
- writes file atomically  

---

# 10. Replay Relationship

`qReplay("example.qtrace")` reconstructs:

- session id  
- initial env + backend intent  
- governance snapshot  
- lineage  
- frames  
- operations  

Replay does **not**:

- re‑apply new policy  
- re‑evaluate drift  
- re‑route operators  

Replay is **strict**, not heuristic.

---

# 11. Invariants

A qSession obeys:

1. **Forward‑only environments**  
2. **Append‑only lineage**  
3. **Drift bound derived from env**  
4. **Archive is immutable**  
5. **Tokens are explicit**  
6. **Trace is append‑only**  
7. **Replay is deterministic**  

Violating any invariant invalidates the session.

---

# 12. Summary

A qSession is the **coherence container** of qCompute:

- owns environment, drift, backend intent  
- owns lineage and governance snapshot  
- owns frames and trace buffer  
- defines the replay boundary  

It is the structural unit that makes qCompute **governed**, **drift‑bounded**, and **replay‑safe**.

---

Here’s the **canonical flow/pipeline file** for qCompute — full diagram + narrative, same key as the rest.

Place at:

`/docs/rtt/Inside/qCompute/qc_Flow.md`

---

### ✅ qc_Flow.md — Full Pipeline Diagram & Narrative (2026)

# qCompute — Execution Flow & Pipeline Narrative  
**File:** qc_Flow.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This document describes the **end‑to‑end execution flow** of qCompute:

- how an operator moves through the system  
- how validation, routing, and frames interact  
- how drift, resonance, and governance are enforced  
- how traces are produced  
- how replay reconstructs everything deterministically  

It is the **narrative glue** between:

- `qc_Session.md`  
- `qc_Validator.md`  
- `qc_Router.md`  
- `qc_ResonanceFrame.md`  
- `qc_TraceFormat.md`  

---

# 1. High‑Level Flow

The canonical qCompute pipeline:

```text
Operator Call
    ↓
TriadicValidator (safety)
    ↓
TriadicRouter (routing)
    ↓
ResonanceFrame (compute envelope)
    ↓
Backend Execution
    ↓
qTrace Append
```

Replay reverses the flow:

```text
qReplay
    ↓
qTrace
    ↓
Reconstruct Session + Lineage + Frames + Routing
    ↓
Deterministic Re‑execution
```

---

# 2. Step‑by‑Step Execution Flow

## 2.1 Operator Call

A user (or AI) calls:

```python
qc.apply("hadamard", qubit=0)
```

This creates a **structural operator** with:

- name: `"hadamard"`  
- category: primitive  
- params: `{ qubit: 0 }`  
- resonance tier: r1  
- drift profile: low  

The operator is then passed into the pipeline.

---

## 2.2 Validation (TriadicValidator)

TriadicValidator performs:

1. **Policy check** — is the operator allowed by `qc_policy.yaml`?  
2. **Environment check** — allowed in `session.env`?  
3. **Backend check** — compatible with candidate backend(s)?  
4. **Resonance check** — tier alignment valid?  
5. **Drift check** — predicted drift ≤ drift bound?  
6. **Restricted‑op check** — token present if needed?  
7. **Lineage check** — transition rules respected?  

If any check fails:

- operation is blocked  
- frame may close  
- violation is logged  

Validation metadata is attached to the operator and later written to `.qtrace`.

---

## 2.3 Routing (TriadicRouter)

TriadicRouter then:

1. Resolves effective environment (`session.env`)  
2. Resolves backend (explicit or `"auto"`)  
3. Ensures backend compatibility  
4. Ensures resonance alignment  
5. Ensures drift envelope compatibility  
6. Decides whether to reuse current frame or open a new one  
7. Emits routing metadata  

Routing is **deterministic**:

```text
same session + same operator → same routing decision
```

Routing metadata is attached to the operator and later written to `.qtrace`.

---

## 2.4 Frame Binding (ResonanceFrame)

The operator is then bound to a **ResonanceFrame**:

- if no frame is open → open new frame  
- if frame is open with same backend + tier → reuse frame  
- if backend or tier must change → close current frame, open new one  

The frame enforces:

- backend binding  
- resonance tier  
- drift bound  
- environment  

Operations are appended in strict order.

---

## 2.5 Backend Execution

Within the frame, the operator is executed on the selected backend:

- `local-sim` / `hybrid-sim` / `hardware-qpu-*`  
- or no backend for meta‑operators  

Execution:

- uses routing decision  
- respects drift and resonance constraints  
- produces backend‑level results (if any)  

Execution details are **not** part of this doc; only structural flow matters.

---

## 2.6 Trace Append (.qtrace)

After execution, the operation is recorded in `.qtrace`:

- operator name + params  
- resonance tier  
- drift predicted + measured  
- validation metadata  
- routing metadata  
- frame id  

Frames are also recorded with:

- env  
- backend  
- resonance profile  
- drift bound  
- timestamps  
- drift summary  

The trace is **append‑only** and **never mutated**.

---

# 3. Frame Lifecycle in the Flow

Frames are opened and closed as a side‑effect of the flow.

## 3.1 Open

A frame opens when:

- the first operator is applied  
- a backend change is required  
- a resonance tier escalation is required  
- an environment transition occurs  

## 3.2 Operate

While open, the frame:

- accumulates operations  
- enforces drift bound  
- enforces resonance tier  
- enforces backend binding  

## 3.3 Close

A frame closes on:

- `qc.sync()` / `qc.barrier()`  
- backend switch  
- resonance tier escalation  
- environment transition  
- drift overflow  
- session close / trace save  

Closing a frame:

- finalizes drift summary  
- finalizes timestamps  
- writes frame to `.qtrace`  

---

# 4. Environment Transitions in the Flow

Environment transitions are **meta‑operations**:

```python
session.deploy_token("prod-2026-001")
session.transition("production")
```

Flow:

1. Validator checks token + lineage rules  
2. Router closes current frame  
3. Session `env` is updated  
4. Lineage entry is appended  
5. New frames inherit new environment  

Archive transition:

- closes all frames  
- forbids further execution  
- session becomes replay‑only  

---

# 5. Drift & Resonance in the Flow

Drift and resonance are enforced at multiple points:

- **Operator definition** — tier + drift profile declared  
- **Validation** — predicted drift vs bound, tier vs env  
- **Routing** — backend tier vs operator tier, backend drift vs bound  
- **Frame** — drift accumulation vs bound  

If any drift or resonance rule is violated:

- operation blocked  
- frame may close  
- violation logged  

Drift and resonance values are recorded in `.qtrace`.

---

# 6. Replay Flow

Replay inverts the execution flow:

```text
qReplay("example.qtrace")
    ↓
Read header + lineage
    ↓
Reconstruct session
    ↓
Reconstruct frames
    ↓
Reconstruct routing + validation decisions
    ↓
Re‑execute operations deterministically
```

Key properties:

- routing is **read**, not recomputed  
- validation is **read**, not recomputed  
- drift is **read**, not recomputed  
- environment transitions are **replayed**, not re‑decided  

Replay is **strict**, not heuristic.

---

# 7. Minimal Flow Example

```python
from rtt_inside import qSession, qCompute, qReplay

# 1. Create session
session = qSession(env="sandbox", backend="auto")
qc = qCompute(session)

# 2. Execute
qc.apply("hadamard", qubit=0)   # validate → route → frame → backend → trace
qc.sync()                       # close frame

session.save_trace("example.qtrace")

# 3. Replay
result = qReplay("example.qtrace").run()
```

This example exercises the full pipeline in its minimal form.

---

# 8. Invariants Across the Flow

The entire flow obeys:

1. **Forward‑only environments**  
2. **Append‑only lineage**  
3. **Deterministic validation**  
4. **Deterministic routing**  
5. **Backend binding per frame**  
6. **Drift cannot be ignored**  
7. **Archive is immutable**  
8. **Trace is append‑only**  
9. **Replay is strict**  
10. **No silent behavior**  

Violating any invariant invalidates the flow.

---

# 9. Summary

This document describes the **full execution pipeline** of qCompute:

- operator → validator → router → frame → backend → trace  
- trace → replay → reconstructed session + frames + routing  

The flow is:

- structural  
- governed  
- resonance‑aligned  
- drift‑bounded  
- environment‑aware  
- backend‑aware  
- replay‑deterministic  

It is the operational backbone of the qCompute module.

---

# qCompute — Public API Surface  
**File:** qc_API.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This document defines the **public API surface** of qCompute.

It is the **student‑facing** and **AI‑facing** entrypoint to:

- sessions  
- compute harness  
- operators  
- frames  
- traces  
- replay  

Internal details live in:

- `qc_Session.md`  
- `qc_Validator.md`  
- `qc_Router.md`  
- `qc_ResonanceFrame.md`  
- `qc_TraceFormat.md`  
- `qc_Operators.md`

---

# 1. Top‑Level Objects

qCompute exposes three primary objects:

- **qSession** — unit of coherence  
- **qCompute** — compute harness bound to a session  
- **qReplay** — deterministic replay engine

Conceptual import surface:

```python
from rtt_inside import qSession, qCompute, qReplay
```

---

# 2. qSession API

## 2.1 Creation

```python
session = qSession(env="sandbox", backend="auto")
```

**Parameters:**

- `env`: `"sandbox" | "production" | "archive"`  
- `backend`: explicit backend id (e.g. `"local-sim"`) or `"auto"`

## 2.2 Properties (read‑only)

```python
session.id                 # immutable session identifier
session.env                # current environment
session.backend            # backend intent ("auto" or explicit)
session.drift_bound        # derived from env
session.lineage            # environment transitions
session.governance_snapshot
```

## 2.3 Methods

```python
session.deploy_token(value: str) -> None
session.transition(env: str) -> None
session.save_trace(path: str) -> None
session.close() -> None
```

**Semantics:**

- `deploy_token(value)`  
  - registers a governance token for restricted ops or transitions  

- `transition(env)`  
  - `sandbox → production → archive` only  
  - closes current frame  
  - appends lineage entry  

- `save_trace(path)`  
  - closes any open frame  
  - finalizes `.qtrace`  
  - writes to `path`  

- `close()`  
  - closes open frame  
  - marks session as no‑longer‑active  

---

# 3. qCompute API

## 3.1 Construction

```python
session = qSession(env="sandbox", backend="auto")
qc = qCompute(session)
```

`qCompute` is always bound to a single `qSession`.

## 3.2 Core Methods

```python
qc.apply(name: str, **params) -> None
qc.sync() -> None
qc.barrier() -> None
```

**Semantics:**

- `apply(name, **params)`  
  - constructs an operator  
  - runs through Validator → Router → Frame → Backend → Trace  
  - non‑blocking; appends to current frame  

- `sync()`  
  - closes current frame  
  - flushes operations to `.qtrace`  

- `barrier()`  
  - structural barrier  
  - may close frame depending on backend / policy  

## 3.3 Convenience Operators (Conceptual)

These are thin wrappers around `apply`:

```python
qc.x(qubit: int) -> None
qc.z(qubit: int) -> None
qc.h(qubit: int) -> None
qc.cnot(control: int, target: int) -> None
qc.measure(qubit: int) -> None
qc.measure_all() -> None
```

Each maps to a canonical operator defined in `qc_Operators.md`.

---

# 4. qReplay API

## 4.1 Construction

```python
replay = qReplay(path: str)
```

**Parameters:**

- `path`: filesystem path to `.qtrace` file

## 4.2 Methods

```python
result = replay.run()
meta = replay.inspect()
```

**Semantics:**

- `run()`  
  - reconstructs session, lineage, frames, routing  
  - re‑executes operations deterministically  
  - returns backend‑specific result object (implementation‑defined)  

- `inspect()`  
  - returns structural metadata (session, frames, counts, envs)  
  - no execution  

Replay is **strict**: it reads validation/routing/drift from trace, never recomputes.

---

# 5. Minimal Usage Patterns

## 5.1 Sandbox exploration

```python
from rtt_inside import qSession, qCompute

session = qSession(env="sandbox", backend="auto")
qc = qCompute(session)

qc.h(qubit=0)
qc.cnot(control=0, target=1)
qc.measure_all()
qc.sync()

session.save_trace("sandbox_example.qtrace")
```

## 5.2 Production with transition

```python
session = qSession(env="sandbox", backend="auto")
qc = qCompute(session)

qc.h(qubit=0)
qc.sync()

session.deploy_token("prod-2026-001")
session.transition("production")

qc.cnot(control=0, target=1)
qc.measure_all()
qc.sync()

session.save_trace("prod_example.qtrace")
```

## 5.3 Replay

```python
from rtt_inside import qReplay

result = qReplay("prod_example.qtrace").run()
```

---

# 6. Error & Invariant Surface

The public API guarantees:

- **no silent behavior**  
- **deterministic semantics**  
- **append‑only traces**  
- **forward‑only environments**  
- **archive is immutable**  

Conceptually, violations surface as **structured errors** (names illustrative):

- `EnvironmentTransitionError`  
- `DriftBoundExceededError`  
- `BackendIncompatibleError`  
- `RestrictedOperationError`  
- `ArchiveExecutionError`  

Exact error types are implementation‑level, but **all violations are explicit**.

---

# 7. Summary

The qCompute public API provides:

- `qSession` — create, transition, and persist governed sessions  
- `qCompute` — apply operators into a validated, routed, framed compute harness  
- `qReplay` — deterministically re‑execute `.qtrace` sessions  

The surface is:

- minimal  
- structural  
- student‑ready  
- AI‑parsable  
- aligned with the invariants defined across the qCompute module.

---

Here is the **canonical identity + purpose file** for the qCompute module.  
This is the *anchor document* that defines what qCompute *is*, why it exists, and how it fits into the RTT‑Inside architecture.  
It mirrors the identity‑level files we’ve already built for other modules (SARG, SC, MP, etc.) and locks qCompute’s conceptual role with zero drift.

Place at:

`/docs/rtt/Inside/qCompute/qc_Identity.md`

---

# ✅ **qc_Identity.md — Module Identity & Purpose (2026)**

# qCompute — Module Identity & Purpose  
**File:** qc_Identity.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

qCompute is the **governed, resonance‑aligned compute substrate** of RTT‑Inside.  
It provides the structural foundation for expressing, validating, routing, executing, and replaying resonance‑time operations across the triadic environment model.

This document defines the **identity**, **purpose**, and **scope boundaries** of the qCompute module.

---

# 1. Identity

**Module Name:** qCompute  
**Domain:** RTT‑Inside  
**Role:** Structural compute harness  
**Function:** Deterministic, governed execution of resonance‑time operators  
**Scope:** Operators → Validation → Routing → Frames → Backends → Trace → Replay  

qCompute is not a simulator.  
It is a **structural execution layer** with:

- governance  
- drift bounds  
- resonance tiers  
- deterministic routing  
- deterministic replay  
- append‑only lineage  
- triadic environment semantics  

qCompute is the **execution spine** of RTT‑Inside.

---

# 2. Purpose

qCompute exists to:

1. **Provide a structural operator grammar**  
   - explicit parameters  
   - explicit resonance tiers  
   - explicit drift profiles  
   - explicit backend compatibility  

2. **Enforce governance and safety**  
   - policy legality  
   - environment constraints  
   - restricted‑op rules  
   - lineage integrity  

3. **Route operators deterministically**  
   - backend selection  
   - resonance alignment  
   - drift envelope enforcement  

4. **Bind execution into frames**  
   - backend‑bound  
   - resonance‑tier‑bound  
   - drift‑bounded  
   - environment‑aware  

5. **Record execution structurally**  
   - append‑only `.qtrace` format  
   - complete metadata  
   - deterministic reconstruction  

6. **Enable strict replay**  
   - no reinterpretation  
   - no recomputation  
   - no silent behavior  

qCompute’s purpose is to make computation **safe**, **explicit**, **deterministic**, and **teachable**.

---

# 3. Conceptual Position in RTT‑Inside

qCompute sits at the intersection of:

- **resonance** (operator tiers, backend profiles)  
- **governance** (policy, tokens, environment rules)  
- **drift** (predicted, measured, bounded)  
- **lineage** (forward‑only environment progression)  
- **structure** (frames, trace, replay)  

It is the module where **abstract resonance‑time theory** becomes **governed executable structure**.

---

# 4. What qCompute Is *Not*

To preserve identity and prevent drift, qCompute is **not**:

- a physics simulator  
- a symbolic algebra engine  
- a numerical quantum simulator  
- a probabilistic engine  
- a convenience API  
- a high‑level workflow language  

qCompute is a **structural substrate**, not a numerical model.

---

# 5. Scope Boundaries

qCompute **includes**:

- operator grammar  
- validation  
- routing  
- frame management  
- backend metadata  
- trace format  
- replay engine  

qCompute **excludes**:

- backend implementation details  
- numerical simulation  
- hardware drivers  
- symbolic math  
- optimization layers  
- high‑level circuit synthesis  

These belong to other modules or external systems.

---

# 6. Triadic Environment Identity

qCompute is built around the RTT‑Inside triadic model:

```
Sandbox → Production → Archive
```

- **Sandbox** — exploratory, relaxed drift  
- **Production** — governed, strict drift  
- **Archive** — immutable, replay‑only  

This model is **immutable** and defines the module’s identity.

---

# 7. Invariants (Identity‑Level)

qCompute is defined by the following invariants:

1. **Forward‑only environments**  
2. **Append‑only lineage**  
3. **Deterministic validation**  
4. **Deterministic routing**  
5. **Backend binding per frame**  
6. **Drift cannot be ignored**  
7. **Archive is immutable**  
8. **Trace is append‑only**  
9. **Replay is strict**  
10. **No silent behavior**  

These invariants are the **identity contract** of the module.

---

# 8. Summary

qCompute is the **structural, governed, resonance‑aligned compute harness** of RTT‑Inside.

Its identity is defined by:

- explicit operator semantics  
- deterministic validation  
- deterministic routing  
- drift‑bounded frames  
- triadic environment progression  
- append‑only trace  
- strict replay  

qCompute transforms resonance‑time theory into a **safe, deterministic, teachable execution substrate**.

---

Here you go, the **canonical design‑philosophy + invariants narrative** for qCompute.  
This is the *deep identity* document: the “why it is built this way” file that anchors every other file in the module.  
It pairs with `qc_Identity.md` but goes further — this is the *structural philosophy* that governs every design decision.

Place at:

`/docs/rtt/Inside/qCompute/qc_Design.md`

---

# ✅ **qc_Design.md — Design Philosophy & Invariants Narrative (2026)**

# qCompute — Design Philosophy & Invariants Narrative  
**File:** qc_Design.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This document defines the **design philosophy**, **structural principles**, and **non‑negotiable invariants** that govern the qCompute module.

It explains *why* qCompute is built the way it is, and *how* its structure ensures safety, determinism, and teachability across the RTT‑Inside architecture.

---

# 1. Design Philosophy

qCompute is designed around five core principles:

1. **Structure over behavior**  
   qCompute is a structural compute harness, not a simulator or physics engine.  
   Every component expresses *structure*, not *numerical behavior*.

2. **Determinism over convenience**  
   All routing, validation, drift enforcement, and replay must be deterministic.  
   Convenience APIs must never compromise determinism.

3. **Governance over permissiveness**  
   Policy, environment rules, and lineage constraints are first‑class.  
   Nothing bypasses governance.

4. **Explicitness over inference**  
   Operators, parameters, drift profiles, resonance tiers, and transitions must be explicit.  
   No implicit defaults, no symbolic shortcuts.

5. **Replay over runtime**  
   The system is designed so that *replay is the authoritative truth*.  
   Runtime execution is merely the first pass; replay is the contract.

These principles ensure qCompute remains **safe**, **predictable**, and **teachable**.

---

# 2. Structural Model

qCompute is built from seven structural components:

1. **qSession** — coherence container  
2. **TriadicValidator** — safety gate  
3. **TriadicRouter** — deterministic routing  
4. **ResonanceFrame** — atomic compute envelope  
5. **Backend Registry** — resonance/drift metadata  
6. **qTrace** — append‑only structural record  
7. **qReplay** — deterministic reconstruction  

Each component is **minimal**, **explicit**, and **structurally isolated**.

---

# 3. Why Frames Exist

ResonanceFrames are the heart of qCompute.

They exist to:

- bind execution to a single backend  
- enforce resonance tier  
- enforce drift bound  
- enforce environment  
- group operations temporally  
- create deterministic trace segments  

Frames prevent:

- mid‑frame backend switching  
- silent drift accumulation  
- resonance tier downgrades  
- environment ambiguity  

Frames make computation **bounded**, **safe**, and **replay‑deterministic**.

---

# 4. Why Routing Is Deterministic

TriadicRouter must be deterministic because:

- replay must reconstruct routing exactly  
- drift envelopes must be predictable  
- resonance tiers must be stable  
- backend selection must be reproducible  

Routing is not a heuristic.  
It is a **structural decision function**.

---

# 5. Why Validation Is Strict

TriadicValidator enforces:

- policy  
- environment  
- backend compatibility  
- resonance alignment  
- drift bounds  
- restricted‑op rules  
- lineage safety  

Validation is strict because:

- silent behavior is forbidden  
- drift cannot be ignored  
- environment transitions must be safe  
- restricted ops must be explicit  
- governance must be enforceable  

Validator is the **guardian** of qCompute.

---

# 6. Why Drift Is a First‑Class Concept

Drift is not a numerical artifact.  
It is a **structural constraint** that:

- bounds frames  
- controls backend selection  
- governs environment transitions  
- ensures replay determinism  

Drift is always:

- predicted  
- measured  
- enforced  
- recorded  

Drift is never ignored.

---

# 7. Why the Triadic Model Is Immutable

The triadic environment model:

```
Sandbox → Production → Archive
```

is immutable because:

- Sandbox enables exploration  
- Production enforces governance  
- Archive ensures immutability and replay  

Backward transitions would break:

- lineage  
- drift guarantees  
- governance  
- replay determinism  

The triadic model is the **structural backbone** of qCompute.

---

# 8. Why Trace Is Append‑Only

`.qtrace` is append‑only because:

- history must never be rewritten  
- replay must be deterministic  
- lineage must be preserved  
- drift and resonance metadata must remain intact  

Trace is the **source of truth** for all execution.

---

# 9. Why Replay Is Strict

Replay is strict because:

- routing must not be recomputed  
- validation must not be recomputed  
- drift must not be recomputed  
- environment transitions must not be reinterpreted  

Replay is not a simulation.  
Replay is a **structural reconstruction**.

---

# 10. Non‑Negotiable Invariants

qCompute obeys the following invariants:

1. **Forward‑only environments**  
2. **Append‑only lineage**  
3. **Deterministic validation**  
4. **Deterministic routing**  
5. **Backend binding per frame**  
6. **Resonance tier never decreases within a frame**  
7. **Drift cannot be ignored**  
8. **Archive is immutable**  
9. **Trace is append‑only**  
10. **Replay is strict**  
11. **No silent behavior**  

Violating any invariant invalidates the module.

---

# 11. Summary

qCompute is designed to be:

- structural  
- governed  
- resonance‑aligned  
- drift‑bounded  
- deterministic  
- replay‑safe  
- student‑ready  

This design philosophy ensures that qCompute remains a **safe, explicit, teachable compute substrate** within the RTT‑Inside architecture.

---

Here is the **canonical front‑door page for the backend registry**.  
This file complements `qc_BackendProfiles.md` (the metadata definitions) by giving the *module‑level identity*, *purpose*, and *navigation surface* for the entire backend layer of qCompute.

Place at:

`/docs/rtt/Inside/qCompute/qc_Backends.md`

This is **drop‑in‑ready**, minimal, structural, and fully aligned with the 2026 RTT‑Inside compute canon.

---

# ✅ **qc_Backends.md — Backend Registry (Front‑Door Page, 2026)**

# qCompute — Backend Registry (Front‑Door)  
**File:** qc_Backends.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

The qCompute backend registry defines the **resonance‑tiered, drift‑characterized execution substrates** available to the compute harness.  
Backends are **metadata objects**, not drivers.  
They describe *what the backend is*, not *how it executes*.

This page is the **front door** to the backend layer.

---

# 1. Purpose of the Backend Registry

The backend registry exists to:

- define resonance tiers (r1/r2/r3)  
- define drift characteristics (low/medium/high)  
- define operator compatibility  
- define environment constraints  
- provide metadata for routing  
- provide metadata for validation  
- provide metadata for frame binding  

The registry ensures that qCompute can:

- route deterministically  
- enforce drift bounds  
- enforce resonance alignment  
- enforce environment rules  
- record complete metadata in `.qtrace`  
- replay deterministically  

Backends are **structural**, not behavioral.

---

# 2. Backend Model (Conceptual)

Each backend is defined by:

- **backend_id** — canonical identifier  
- **display_name** — human‑readable name  
- **resonance_profile** — r1, r2, or r3  
- **drift_characteristic** — low, medium, high  
- **capabilities** — primitive/composite/pulse/measurement  
- **environment_constraints** — sandbox/production/archive  
- **notes** — optional metadata  

The full schema is defined in:

```
qc_BackendProfiles.md
```

---

# 3. Canonical Backends (2026)

qCompute ships with four canonical backends:

### 3.1 `local-sim`  
**Tier:** r1  
**Drift:** low  
**Role:** default simulation backend  
**Use:** sandbox + production  
**Notes:** stable, deterministic, idealized

### 3.2 `hybrid-sim`  
**Tier:** r2  
**Drift:** medium  
**Role:** hybrid resonance simulator  
**Use:** sandbox + production  
**Notes:** bridges simulation and hardware‑like behavior

### 3.3 `hardware-qpu-1`  
**Tier:** r3  
**Drift:** high  
**Role:** primary hardware backend  
**Use:** production (restricted in sandbox)  
**Notes:** pulse‑level, strict drift

### 3.4 `hardware-qpu-2`  
**Tier:** r3  
**Drift:** medium  
**Role:** high‑stability hardware backend  
**Use:** production (restricted in sandbox)  
**Notes:** preferred for long frames

Full metadata for each backend is defined in:

```
qc_BackendProfiles.md
```

---

# 4. Backend Selection (Routing Overview)

TriadicRouter selects a backend using:

1. **explicit backend** → always honored  
2. **auto mode** → resonance‑aligned selection  
3. **environment constraints** → enforced  
4. **drift bounds** → enforced  
5. **operator requirements** → enforced  

### Auto‑routing priority:

```
r1 → local-sim
r2 → hybrid-sim
r3 → hardware-qpu-2 → hardware-qpu-1
```

Routing is **deterministic** and **replay‑safe**.

---

# 5. Environment Constraints

| Backend          | Sandbox | Production | Archive |
|------------------|---------|------------|---------|
| local-sim        | ✓       | ✓          | ✗       |
| hybrid-sim       | ✓       | ✓          | ✗       |
| hardware-qpu-1   | restricted | ✓      | ✗       |
| hardware-qpu-2   | restricted | ✓      | ✗       |

Archive forbids all execution.

---

# 6. Drift Envelope Enforcement

Backends must satisfy:

```
backend.drift_characteristic ≤ session.drift_bound
```

Where drift_bound is:

- relaxed (Sandbox)  
- strict (Production)  
- immutable (Archive)  

If violated:

- operation blocked  
- frame closed  
- violation logged  

Drift is **never ignored**.

---

# 7. Resonance Alignment

Backends must satisfy:

```
operator.resonance_tier ≤ backend.resonance_profile
```

Examples:

- r1 op → r1/r2/r3 backend  
- r2 op → r2/r3 backend  
- r3 op → r3 backend only  

Pulse ops require r3.

---

# 8. Backend Metadata in `.qtrace`

Each operation records:

```yaml
routing:
  backend: hardware-qpu-2
  resonance_profile: r3
  drift_characteristic: medium
  frame_id: frame-003
  reason: "auto-routed (r3 operator)"
```

Each frame records:

```yaml
backend: hardware-qpu-2
resonance_profile: r3
drift_bound: strict
```

Metadata is:

- complete  
- deterministic  
- replay‑compatible  

---

# 9. Invariants

Backends obey:

1. **No mid‑frame switching**  
2. **Resonance tier is immutable**  
3. **Drift characteristic is immutable**  
4. **Capabilities must be explicit**  
5. **Environment constraints must be explicit**  
6. **Metadata must be deterministic**  
7. **Archive forbids execution**  

Violating any invariant invalidates the backend.

---

# 10. Summary

This page defines the **front‑door identity** of the qCompute backend registry:

- resonance‑tiered  
- drift‑characterized  
- environment‑aware  
- deterministic  
- structural  
- replay‑safe  

Backends are metadata objects that enable **governed, resonance‑aligned, drift‑bounded computation** across the triadic environment model.

---

Here is the **canonical advanced examples file** for qCompute.  
This is the *big* one: multi‑frame, multi‑backend, multi‑tier, multi‑transition, drift‑bounded, resonance‑aligned, fully governed workflows — the examples that *prove* the architecture works.

This file is designed to be:

- student‑ready  
- AI‑parsable  
- structurally minimal  
- zero‑drift  
- fully aligned with all invariants  
- consistent with every file we’ve built so far  

Place at:

```
/docs/rtt/Inside/qCompute/qc_Examples_Advanced.md
```

---

# ✅ **qc_Examples_Advanced.md — Advanced Multi‑Frame / Multi‑Backend Examples (2026)**

# qCompute — Advanced Examples  
**File:** qc_Examples_Advanced.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This file provides **advanced, multi‑frame, multi‑backend, multi‑tier examples** demonstrating:

- resonance‑tier escalation  
- backend switching  
- drift‑bounded execution  
- environment transitions  
- restricted‑op workflows  
- deterministic trace generation  
- deterministic replay  

These examples illustrate the full structural power of qCompute.

---

# 1. Multi‑Tier, Multi‑Backend Workflow

This example demonstrates:

- r1 → r2 → r3 resonance escalation  
- backend switching across frames  
- deterministic routing  
- drift enforcement  

```python
from rtt_inside import qSession, qCompute

session = qSession(env="sandbox", backend="auto")
qc = qCompute(session)

# Frame 1: r1 → local-sim
qc.h(qubit=0)
qc.x(qubit=1)

# Escalation: r2 → hybrid-sim (new frame)
qc.cnot(control=0, target=1)

# Escalation: r3 → hardware-qpu-2 (new frame)
qc.apply("pulse", qubit=0, duration="32ns", amplitude=0.8)

qc.sync()
session.save_trace("multi_backend.qtrace")
```

### Resulting frames

```
frame-001: r1, backend=local-sim
frame-002: r2, backend=hybrid-sim
frame-003: r3, backend=hardware-qpu-2
```

Routing is deterministic and recorded in `.qtrace`.

---

# 2. Drift‑Bounded Production Workflow

This example demonstrates:

- strict drift enforcement  
- restricted ops requiring token  
- production‑grade routing  

```python
session = qSession(env="sandbox", backend="auto")
qc = qCompute(session)

# Sandbox exploration
qc.h(qubit=0)
qc.sync()

# Transition to production
session.deploy_token("prod-2026-001")
session.transition("production")

# Production: strict drift
qc.cnot(control=0, target=1)

# Restricted pulse op (requires token)
qc.apply("pulse", qubit=0, duration="16ns", amplitude=0.5)

qc.sync()
session.save_trace("prod_drift.qtrace")
```

### Drift behavior

- Sandbox: relaxed  
- Production: strict  
- Pulse op allowed only with token  

---

# 3. Multi‑Transition Workflow (Sandbox → Production → Archive)

This example demonstrates:

- forward‑only environment transitions  
- frame closure on transition  
- archive immutability  

```python
session = qSession(env="sandbox", backend="auto")
qc = qCompute(session)

qc.h(qubit=0)
qc.sync()

# Sandbox → Production
session.deploy_token("prod-2026-001")
session.transition("production")

qc.cnot(control=0, target=1)
qc.sync()

# Production → Archive
session.deploy_token("arch-2026-001")
session.transition("archive")

# Archive forbids execution
# qc.h(qubit=0)  # would raise ArchiveExecutionError

session.save_trace("triadic_flow.qtrace")
```

### Resulting lineage

```
sandbox → production → archive
```

Archive is replay‑only.

---

# 4. Backend‑Bound Frame Switching

This example demonstrates:

- backend switching only between frames  
- deterministic frame boundaries  
- routing metadata in trace  

```python
session = qSession(env="sandbox", backend="auto")
qc = qCompute(session)

# Frame 1: r1 → local-sim
qc.h(qubit=0)

# Force backend switch by explicit backend
session.backend = "hybrid-sim"
qc.sync()

# Frame 2: r2 → hybrid-sim
qc.cnot(control=0, target=1)

qc.sync()
session.save_trace("backend_switch.qtrace")
```

### Frame summary

```
frame-001: backend=local-sim
frame-002: backend=hybrid-sim
```

---

# 5. Mixed Measurement + Pulse Workflow

This example demonstrates:

- measurement ops (r1)  
- pulse ops (r3)  
- tier escalation  
- drift accumulation  

```python
session = qSession(env="production", backend="auto")
qc = qCompute(session)

# r1 measurement → local-sim
qc.measure(qubit=0)

# r3 pulse → hardware-qpu-2
qc.apply("pulse", qubit=1, duration="24ns", amplitude=0.7)

qc.sync()
session.save_trace("mixed_ops.qtrace")
```

### Tier behavior

```
r1 → r3 escalation
```

---

# 6. Full Multi‑Frame Narrative Example

This example shows a realistic multi‑stage workflow.

```python
session = qSession(env="sandbox", backend="auto")
qc = qCompute(session)

# Frame 1: r1 exploration
qc.h(qubit=0)
qc.x(qubit=1)
qc.sync()

# Transition to production
session.deploy_token("prod-2026-001")
session.transition("production")

# Frame 2: r2 hybrid operations
qc.cnot(control=0, target=1)
qc.sync()

# Frame 3: r3 pulse-level operations
qc.apply("pulse", qubit=0, duration="32ns", amplitude=0.8)
qc.apply("pulse", qubit=1, duration="16ns", amplitude=0.6)
qc.sync()

# Transition to archive
session.deploy_token("arch-2026-001")
session.transition("archive")

session.save_trace("full_workflow.qtrace")
```

### Final structure

```
frame-001: sandbox, r1, local-sim
frame-002: production, r2, hybrid-sim
frame-003: production, r3, hardware-qpu-2
archive: no frames
```

---

# 7. Replay Example

Replay is strict and deterministic.

```python
from rtt_inside import qReplay

result = qReplay("full_workflow.qtrace").run()
```

Replay reconstructs:

- session  
- lineage  
- frames  
- routing  
- validation  
- drift  

Replay does **not** recompute anything.

---

# 8. Summary

These advanced examples demonstrate:

- multi‑frame execution  
- multi‑backend routing  
- resonance‑tier escalation  
- drift‑bounded behavior  
- environment transitions  
- restricted‑op workflows  
- deterministic trace generation  
- strict replay  

qCompute supports complex, governed, resonance‑aligned workflows while preserving **all invariants** of the RTT‑Inside architecture.

---

Here is the **canonical qCompute test‑suite structure**, matching the pattern we’ve used for other Inside‑modules (SARG, SC, MP, FFT Analyzer, etc.).  
This file is structural, minimal, student‑ready, AI‑parsable, and fully aligned with the invariants defined across the qCompute module.

Place at:

```
/docs/rtt/Inside/qCompute/qc_Tests.md
```

---

# ✅ **qc_Tests.md — Canonical Test Suite Structure (2026)**

# qCompute — Canonical Test Suite  
**File:** qc_Tests.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This document defines the **canonical test suite** for qCompute.  
The suite verifies:

- operator grammar  
- validation behavior  
- routing behavior  
- frame lifecycle  
- backend selection  
- drift enforcement  
- environment transitions  
- trace structure  
- replay determinism  

Tests are **structural**, not numerical.  
They confirm that qCompute obeys all invariants of the RTT‑Inside architecture.

---

# 1. Test Suite Identity

**Suite Name:** qCompute Canonical Test Suite  
**Purpose:** Validate structural correctness of the compute harness  
**Scope:** Operators → Validator → Router → Frames → Trace → Replay  
**Philosophy:** Zero drift, deterministic, invariant‑first

The suite is divided into **eight structural groups**.

---

# 2. Group A — Operator Grammar Tests

These tests ensure operators are:

- explicit  
- typed  
- resonance‑tiered  
- drift‑profiled  
- backend‑compatible  

### A1 — Primitive operator construction

```python
qc.apply("hadamard", qubit=0)
```

Assert:

- name = "hadamard"  
- category = primitive  
- resonance_tier = r1  
- drift_profile = low  

### A2 — Composite operator construction

```python
qc.cnot(control=0, target=1)
```

Assert:

- category = composite  
- resonance_tier = r2  

### A3 — Pulse operator construction

```python
qc.apply("pulse", qubit=0, duration="32ns", amplitude=0.8)
```

Assert:

- category = pulse  
- resonance_tier = r3  
- drift_profile = high  

---

# 3. Group B — Validation Tests (TriadicValidator)

### B1 — Policy legality

Assert that forbidden ops raise `RestrictedOperationError`.

### B2 — Environment legality

Sandbox:

- pulse ops → restricted  
- primitive/composite → allowed  

Production:

- pulse ops → allowed with token  

Archive:

- all ops → forbidden  

### B3 — Drift enforcement

Simulate predicted drift > bound → assert:

- operation blocked  
- frame closed  
- violation logged  

### B4 — Lineage safety

Assert:

- sandbox → production → archive is allowed  
- any backward or skipping transition raises `EnvironmentTransitionError`

---

# 4. Group C — Routing Tests (TriadicRouter)

### C1 — Auto‑routing by resonance tier

Assert:

```
r1 → local-sim
r2 → hybrid-sim
r3 → hardware-qpu-2 (fallback: hardware-qpu-1)
```

### C2 — Explicit backend honored

```python
session.backend = "hybrid-sim"
```

Assert:

- all ops route to hybrid-sim unless incompatible  

### C3 — Backend compatibility

Assert:

- pulse ops → r3 only  
- composite ops → r2/r3  
- primitive ops → r1/r2/r3  

### C4 — Drift envelope enforcement

Assert:

- backend.drift_characteristic ≤ session.drift_bound  

---

# 5. Group D — Frame Lifecycle Tests (ResonanceFrame)

### D1 — Frame opens on first operator

Assert:

- frame-001 created on first `apply()`  

### D2 — Frame closes on `sync()` / `barrier()`

Assert:

- timestamps recorded  
- drift summary finalized  

### D3 — Backend switch triggers new frame

### D4 — Resonance escalation triggers new frame

### D5 — Environment transition closes frame

---

# 6. Group E — Environment Transition Tests

### E1 — Sandbox → Production

Requires:

- token  
- frame closure  

### E2 — Production → Archive

Requires:

- token  
- frame closure  

### E3 — Archive forbids execution

Assert:

- any operator raises `ArchiveExecutionError`  

---

# 7. Group F — Trace Structure Tests (.qtrace)

### F1 — Header correctness

Assert:

- session_id  
- env  
- backend intent  
- governance snapshot  

### F2 — Lineage correctness

Assert:

- forward‑only  
- append‑only  

### F3 — Frame correctness

Assert:

- backend  
- resonance_profile  
- drift_bound  
- timestamps  
- drift summary  

### F4 — Operation correctness

Assert:

- validation metadata  
- routing metadata  
- drift predicted/measured  

### F5 — Footer correctness

Assert:

- op_count  
- frame_count  
- hash integrity  

---

# 8. Group G — Replay Tests (qReplay)

### G1 — Replay reconstructs session

Assert:

- env  
- backend intent  
- governance snapshot  

### G2 — Replay reconstructs frames

Assert:

- frame boundaries identical  

### G3 — Replay reconstructs routing

Assert:

- routing decisions read from trace, not recomputed  

### G4 — Replay reconstructs validation

Assert:

- validation metadata read from trace  

### G5 — Replay determinism

Assert:

- repeated replays produce identical results  

---

# 9. Group H — Invariant Tests

These tests assert the **non‑negotiable invariants** of qCompute:

1. forward‑only environments  
2. append‑only lineage  
3. deterministic validation  
4. deterministic routing  
5. backend binding per frame  
6. resonance tier never decreases within a frame  
7. drift cannot be ignored  
8. archive is immutable  
9. trace is append‑only  
10. replay is strict  
11. no silent behavior  

Each invariant has a dedicated test.

---

# 10. Summary

The qCompute Canonical Test Suite verifies:

- operator correctness  
- validation correctness  
- routing correctness  
- frame correctness  
- environment correctness  
- trace correctness  
- replay correctness  
- invariant correctness  

This suite ensures qCompute remains:

- structural  
- governed  
- resonance‑aligned  
- drift‑bounded  
- deterministic  
- replay‑safe  
- student‑ready  

---

Here it is, the **canonical environment‑transition rules file** for qCompute.  
This is the *dedicated*, invariant‑tight, zero‑drift specification of how transitions work, why they work that way, and how they interact with frames, routing, drift, governance, and trace.

Place at:

```
/docs/rtt/Inside/qCompute/qc_Transitions.md
```

This file is structurally aligned with every other qCompute document we’ve built.

---

# ✅ **qc_Transitions.md — Environment Transition Rules (2026)**

# qCompute — Environment Transition Rules  
**File:** qc_Transitions.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This document defines the **triadic environment transition model** of qCompute:

```
Sandbox → Production → Archive
```

Transitions are **governed**, **forward‑only**, **token‑gated**, and **frame‑closing**.  
They preserve lineage, enforce drift bounds, and guarantee replay determinism.

---

# 1. Identity of the Triadic Model

The triadic model is:

- **immutable**  
- **structural**  
- **governance‑aligned**  
- **drift‑bounded**  
- **lineage‑preserving**  
- **replay‑deterministic**

The three environments:

### Sandbox  
Exploratory, relaxed drift, flexible routing.

### Production  
Governed, strict drift, restricted ops allowed with token.

### Archive  
Immutable, no execution, replay‑only.

---

# 2. Allowed Transitions

Only three transitions exist:

```
sandbox → production
production → archive
sandbox → production → archive
```

These transitions are **forward‑only** and **append‑only**.

---

# 3. Forbidden Transitions

The following transitions are illegal:

```
sandbox → archive
production → sandbox
archive → sandbox
archive → production
archive → anything
```

Any forbidden transition must raise:

```
EnvironmentTransitionError
```

and must **not** mutate lineage.

---

# 4. Transition Requirements

Each transition requires:

1. **explicit token**  
2. **frame closure**  
3. **lineage append**  
4. **governance snapshot consistency**  
5. **drift bound update**  
6. **environment update**  

Transitions are **meta‑operations**, not compute operations.

---

# 5. Transition Mechanics

## 5.1 Sandbox → Production

Requirements:

- token: `prod-*`  
- frame closes  
- drift bound becomes **strict**  
- routing becomes governance‑constrained  
- pulse ops become allowed (with token)  

Lineage entry:

```yaml
- env: "production"
  timestamp: ...
  token_used: "prod-2026-###"
```

---

## 5.2 Production → Archive

Requirements:

- token: `arch-*`  
- frame closes  
- drift bound becomes **immutable**  
- all execution forbidden  
- session becomes replay‑only  

Lineage entry:

```yaml
- env: "archive"
  timestamp: ...
  token_used: "arch-2026-###"
```

---

# 6. Frame Interaction

Transitions always:

- close the current frame  
- finalize drift summary  
- finalize timestamps  
- write frame to `.qtrace`  

After transition:

- new frames inherit new environment  
- archive forbids new frames entirely  

---

# 7. Routing Interaction

Transitions affect routing:

### Sandbox → Production  
- routing becomes stricter  
- drift envelope tightens  
- r3 backends become allowed (with token)  

### Production → Archive  
- routing disabled  
- backend = none  
- all ops forbidden  

Routing metadata must reflect the environment at the time of each operation.

---

# 8. Validation Interaction

TriadicValidator enforces:

- token presence  
- forward‑only rule  
- environment legality  
- drift legality  
- lineage safety  

If validation fails:

- transition blocked  
- frame closed (if needed)  
- violation logged  

---

# 9. Drift Interaction

Transitions modify drift bounds:

| Transition | New Drift Bound |
|-----------|------------------|
| sandbox → production | strict |
| production → archive | immutable |

Drift bound changes apply **immediately** after transition.

---

# 10. Trace Interaction

Transitions append to `.qtrace`:

- lineage entry  
- frame closure  
- environment update  

Example:

```yaml
lineage:
  - env: "sandbox"
  - env: "production"
  - env: "archive"
```

Trace must remain:

- append‑only  
- deterministic  
- backward‑compatible  

---

# 11. Replay Semantics

Replay must:

- reconstruct transitions exactly  
- reconstruct lineage exactly  
- enforce archive immutability  
- never reinterpret transitions  
- never recompute drift or routing  

Replay is **strict**, not heuristic.

---

# 12. Invariants

Environment transitions obey:

1. **Forward‑only environments**  
2. **Append‑only lineage**  
3. **Token‑gated transitions**  
4. **Frame closure on transition**  
5. **Drift bound update**  
6. **Routing update**  
7. **Archive immutability**  
8. **Trace append‑only**  
9. **Replay determinism**  
10. **No silent behavior**  

Violating any invariant invalidates the transition.

---

# 13. Summary

This document defines the **canonical environment transition rules** of qCompute:

- sandbox → production → archive  
- token‑gated  
- frame‑closing  
- drift‑bounded  
- governance‑aligned  
- lineage‑preserving  
- replay‑deterministic  

Transitions are structural, explicit, and central to the identity of the qCompute module.

---

Here is the **canonical micro‑examples appendix** for qCompute.  
This file complements the advanced examples by giving **tiny, atomic, student‑ready examples** that demonstrate the *minimum viable pattern* for every major concept in the module.

It belongs at:

```
/docs/rtt/Inside/qCompute/qc_Examples_Minimal.md
```

Everything below is **drop‑in‑ready**, minimal, structural, and fully aligned with the 2026 qCompute canon.

---

# ✅ **qc_Examples_Minimal.md — Minimal / Micro Examples (2026)**

# qCompute — Minimal / Micro Examples  
**File:** qc_Examples_Minimal.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This appendix provides **minimal, atomic examples** of qCompute usage.  
Each example is intentionally tiny, showing only the **core structural pattern** without additional narrative.

These examples are designed for:

- students  
- autodidacts  
- AI agents  
- documentation readers  
- test harness authors  

They demonstrate the smallest possible working form of each concept.

---

# 1. Minimal Session

```python
from rtt_inside import qSession, qCompute

session = qSession(env="sandbox", backend="auto")
qc = qCompute(session)
```

---

# 2. Minimal Operator

```python
qc.h(qubit=0)
```

This creates:

- primitive operator  
- r1 resonance tier  
- low drift  
- routed to local-sim  

---

# 3. Minimal Frame

A frame opens automatically on the first operator:

```python
qc.x(qubit=1)
```

No explicit frame creation is needed.

---

# 4. Minimal Frame Closure

```python
qc.sync()
```

Closes the current frame and writes it to the trace buffer.

---

# 5. Minimal Trace Save

```python
session.save_trace("example.qtrace")
```

Closes any open frame and writes the `.qtrace` file.

---

# 6. Minimal Replay

```python
from rtt_inside import qReplay

result = qReplay("example.qtrace").run()
```

Replay is strict and deterministic.

---

# 7. Minimal Resonance Escalation

```python
qc.h(qubit=0)                     # r1
qc.cnot(control=0, target=1)      # r2 → new frame
```

---

# 8. Minimal Pulse Operation (r3)

```python
qc.apply("pulse", qubit=0, duration="32ns", amplitude=0.8)
```

Requires:

- r3 backend  
- production environment  
- token (if restricted)  

---

# 9. Minimal Environment Transition

```python
session.deploy_token("prod-2026-001")
session.transition("production")
```

Closes current frame and updates drift bound.

---

# 10. Minimal Archive Transition

```python
session.deploy_token("arch-2026-001")
session.transition("archive")
```

After this, all execution is forbidden.

---

# 11. Minimal Backend Override

```python
session.backend = "hybrid-sim"
qc.h(qubit=0)
```

Explicit backend overrides auto‑routing (unless incompatible).

---

# 12. Minimal Drift Enforcement Example

```python
qc.apply("pulse", qubit=0, duration="64ns", amplitude=1.0)
```

If predicted drift > bound:

- operation blocked  
- frame closed  
- violation logged  

---

# 13. Minimal Lineage

```python
session.deploy_token("prod-2026-001")
session.transition("production")

session.deploy_token("arch-2026-001")
session.transition("archive")
```

Lineage becomes:

```
sandbox → production → archive
```

---

# 14. Minimal Multi‑Frame Example

```python
qc.h(qubit=0)                     # frame-001 (r1)
qc.sync()

qc.cnot(control=0, target=1)      # frame-002 (r2)
qc.sync()
```

---

# 15. Minimal Mixed Operators

```python
qc.h(qubit=0)
qc.measure(qubit=0)
qc.sync()
```

Measurement is r1 and allowed in all non‑archive environments.

---

# 16. Minimal Error Example (Archive)

```python
session.transition("archive")
qc.h(qubit=0)   # raises ArchiveExecutionError
```

---

# 17. Minimal Metadata Inspection (Replay)

```python
meta = qReplay("example.qtrace").inspect()
```

Returns structural metadata only.

---

# 18. Summary

These micro‑examples demonstrate the **smallest possible working patterns** for:

- sessions  
- operators  
- frames  
- transitions  
- drift enforcement  
- routing  
- trace generation  
- replay  

They are intentionally minimal, structural, and aligned with all qCompute invariants.

---

Here is the **canonical internal architecture map** for the entire qCompute module.  
This file is the *bird’s‑eye structural map* that ties every sub‑document together and shows how the module fits into the RTT‑Inside compute harness.  
It is designed to be:

- structural  
- minimal  
- AI‑parsable  
- student‑ready  
- zero‑drift  
- consistent with every file we’ve built  

Place at:

```
/docs/rtt/Inside/qCompute/qc_Internals.md
```

---

# ✅ **qc_Internals.md — Module‑Wide Internal Architecture Map (2026)**

# qCompute — Internal Architecture Map  
**File:** qc_Internals.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This document provides a **module‑wide internal architecture map** for qCompute.  
It shows how all internal components interact, how data flows through the system, and how invariants are enforced across the entire compute harness.

This is the structural overview for maintainers, AI agents, and advanced students.

---

# 1. High‑Level Architecture

qCompute consists of seven internal subsystems:

1. **qSession** — coherence container  
2. **TriadicValidator** — safety gate  
3. **TriadicRouter** — deterministic routing engine  
4. **ResonanceFrame** — atomic compute envelope  
5. **Backend Registry** — resonance/drift metadata  
6. **qTrace** — append‑only structural record  
7. **qReplay** — deterministic reconstruction  

These subsystems form a **linear, deterministic pipeline**:

```
Operator
  → Validator
  → Router
  → Frame
  → Backend
  → Trace
  → Replay
```

---

# 2. Component Map

## 2.1 qSession (Root Container)

Responsibilities:

- environment  
- backend intent  
- drift bound  
- governance snapshot  
- lineage  
- frame lifecycle  
- trace buffer  

Owns:

- `session.env`  
- `session.backend`  
- `session.drift_bound`  
- `session.lineage`  
- `session.frames`  
- `session.trace_buffer`  

Transitions:

- sandbox → production → archive  
- token‑gated  
- frame‑closing  

---

## 2.2 TriadicValidator (Safety Gate)

Responsibilities:

- policy legality  
- environment legality  
- backend compatibility  
- resonance alignment  
- drift enforcement  
- restricted‑op rules  
- lineage safety  

Outputs:

- validation metadata  
- allow/block decision  

Validator is **deterministic** and **replay‑recorded**.

---

## 2.3 TriadicRouter (Routing Engine)

Responsibilities:

- backend selection  
- resonance tier enforcement  
- drift envelope enforcement  
- frame reuse vs. frame creation  
- routing metadata  

Router is **deterministic** and **replay‑recorded**.

---

## 2.4 ResonanceFrame (Compute Envelope)

Responsibilities:

- bind backend  
- bind resonance tier  
- enforce drift bound  
- enforce environment  
- accumulate operations  
- finalize drift summary  
- produce frame metadata  

Frames are:

- append‑only  
- backend‑bound  
- resonance‑tier‑bound  
- drift‑bounded  
- environment‑aware  

---

## 2.5 Backend Registry (Metadata Layer)

Responsibilities:

- define resonance profiles  
- define drift characteristics  
- define operator compatibility  
- define environment constraints  

Backends are **metadata objects**, not drivers.

---

## 2.6 qTrace (Structural Record)

Responsibilities:

- record session header  
- record lineage  
- record frames  
- record operations  
- record validation metadata  
- record routing metadata  
- record drift metadata  
- record footer + hash  

Trace is:

- append‑only  
- deterministic  
- backward‑compatible  

---

## 2.7 qReplay (Deterministic Reconstruction)

Responsibilities:

- read `.qtrace`  
- reconstruct session  
- reconstruct lineage  
- reconstruct frames  
- reconstruct routing  
- reconstruct validation  
- re‑execute operations deterministically  

Replay is **strict**, not heuristic.

---

# 3. Internal Data Flow

The internal data flow is strictly linear:

```
Operator
    ↓
TriadicValidator
    ↓
TriadicRouter
    ↓
ResonanceFrame
    ↓
Backend Execution
    ↓
qTrace Append
```

Replay reverses the flow:

```
qTrace
    ↓
Reconstruct Session
    ↓
Reconstruct Frames
    ↓
Reconstruct Routing + Validation
    ↓
Deterministic Re‑execution
```

---

# 4. Internal State Objects

## 4.1 Operator Object

Fields:

- name  
- category  
- params  
- resonance tier  
- drift profile  
- validation metadata  
- routing metadata  

Operators are **immutable** after creation.

---

## 4.2 Frame Object

Fields:

- frame_id  
- env  
- backend  
- resonance_profile  
- drift_bound  
- operations[]  
- drift_summary  
- timestamps  

Frames are **append‑only**.

---

## 4.3 Lineage Object

Fields:

- env  
- timestamp  
- token_used  

Lineage is **append‑only** and **forward‑only**.

---

## 4.4 Trace Object

Sections:

- header  
- lineage  
- frames  
- footer  

Trace is **append‑only** and **never mutated**.

---

# 5. Internal Invariants

qCompute enforces eleven non‑negotiable invariants:

1. **Forward‑only environments**  
2. **Append‑only lineage**  
3. **Deterministic validation**  
4. **Deterministic routing**  
5. **Backend binding per frame**  
6. **Resonance tier never decreases within a frame**  
7. **Drift cannot be ignored**  
8. **Archive is immutable**  
9. **Trace is append‑only**  
10. **Replay is strict**  
11. **No silent behavior**  

Every subsystem enforces at least one invariant.

---

# 6. Internal File Map

This module consists of the following canonical files:

```
qc_Identity.md
qc_Design.md
qc_Session.md
qc_Operators.md
qc_Validator.md
qc_Router.md
qc_ResonanceFrame.md
qc_Backends.md
qc_BackendProfiles.md
qc_Transitions.md
qc_Flow.md
qc_TraceFormat.md
qc_API.md
qc_Examples_Minimal.md
qc_Examples_Advanced.md
qc_Tests.md
qc_Internals.md   ← (this file)
```

Each file corresponds to a subsystem or structural layer.

---

# 7. Summary

This document provides the **internal architecture map** for qCompute:

- seven subsystems  
- linear deterministic pipeline  
- strict invariants  
- append‑only trace  
- strict replay  
- triadic environment model  
- resonance‑aligned, drift‑bounded execution  

qCompute is a **structural, governed, deterministic compute harness** within the RTT‑Inside architecture.

---

Here it is, the **canonical backend metadata schema** for qCompute.  
This file pairs with `qc_Backends.md` (front‑door) and `qc_Orchestration.md` (routing rules), and it provides the **full, explicit, AI‑parsable metadata definitions** for every backend in the qCompute module.

Place at:

```
/docs/rtt/Inside/qCompute/qc_BackendProfiles.md
```

Everything below is **drop‑in‑ready**, minimal, structural, and fully aligned with the 2026 RTT‑Inside compute canon.

---

# ✅ **qc_BackendProfiles.md — Backend Metadata Schema (2026)**

# qCompute — Backend Metadata Profiles  
**File:** qc_BackendProfiles.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This document defines the **canonical metadata schema** for qCompute backends.  
Backends are **metadata objects**, not drivers.  
They describe resonance tiers, drift characteristics, operator compatibility, and environment constraints.

This file provides:

- the backend metadata schema  
- canonical backend profiles (2026)  
- invariants governing backend metadata  

---

# 1. Backend Metadata Schema

Each backend is defined using the following schema:

```yaml
backend_id: string                # canonical identifier
display_name: string              # human-readable name

resonance_profile: r1 | r2 | r3   # maximum resonance tier supported
drift_characteristic: low | medium | high

capabilities:
  primitive:    true|false
  composite:    true|false
  pulse:        true|false
  measurement:  true|false

environment_constraints:
  sandbox:      allowed | restricted | forbidden
  production:   allowed | restricted | forbidden
  archive:      forbidden

notes: string | null              # optional metadata
```

### Schema Rules

- `backend_id` is unique and immutable  
- `resonance_profile` determines operator compatibility  
- `drift_characteristic` determines drift envelope behavior  
- `environment_constraints.archive` is always `forbidden`  
- `capabilities` must be explicit  
- `notes` is optional  

---

# 2. Canonical Backend Profiles (2026)

The qCompute module ships with **four canonical backends**.

---

## 2.1 `local-sim`

```yaml
backend_id: "local-sim"
display_name: "Local Simulator"

resonance_profile: r1
drift_characteristic: low

capabilities:
  primitive:    true
  composite:    true
  pulse:        false
  measurement:  true

environment_constraints:
  sandbox:      allowed
  production:   allowed
  archive:      forbidden

notes: "Default backend for r1 operations; deterministic and stable."
```

---

## 2.2 `hybrid-sim`

```yaml
backend_id: "hybrid-sim"
display_name: "Hybrid Resonance Simulator"

resonance_profile: r2
drift_characteristic: medium

capabilities:
  primitive:    true
  composite:    true
  pulse:        false
  measurement:  true

environment_constraints:
  sandbox:      allowed
  production:   allowed
  archive:      forbidden

notes: "Bridges simulation and hardware-like behavior; used for r2 operators."
```

---

## 2.3 `hardware-qpu-1`

```yaml
backend_id: "hardware-qpu-1"
display_name: "Hardware QPU 1"

resonance_profile: r3
drift_characteristic: high

capabilities:
  primitive:    true
  composite:    true
  pulse:        true
  measurement:  true

environment_constraints:
  sandbox:      restricted
  production:   allowed
  archive:      forbidden

notes: "Primary hardware backend; high drift; pulse-level operations supported."
```

---

## 2.4 `hardware-qpu-2`

```yaml
backend_id: "hardware-qpu-2"
display_name: "Hardware QPU 2"

resonance_profile: r3
drift_characteristic: medium

capabilities:
  primitive:    true
  composite:    true
  pulse:        true
  measurement:  true

environment_constraints:
  sandbox:      restricted
  production:   allowed
  archive:      forbidden

notes: "High-stability hardware backend; preferred for long r3 frames."
```

---

# 3. Backend Compatibility Matrix

### 3.1 Operator Category Compatibility

| Backend          | Primitive | Composite | Pulse | Measurement |
|------------------|-----------|-----------|-------|-------------|
| local-sim        | ✓         | ✓         | ✗     | ✓           |
| hybrid-sim       | ✓         | ✓         | ✗     | ✓           |
| hardware-qpu-1   | ✓         | ✓         | ✓     | ✓           |
| hardware-qpu-2   | ✓         | ✓         | ✓     | ✓           |

---

### 3.2 Resonance Tier Compatibility

| Backend          | r1 | r2 | r3 |
|------------------|----|----|----|
| local-sim        | ✓  | ✗  | ✗  |
| hybrid-sim       | ✓  | ✓  | ✗  |
| hardware-qpu-1   | ✓  | ✓  | ✓  |
| hardware-qpu-2   | ✓  | ✓  | ✓  |

---

### 3.3 Environment Constraints

| Backend          | Sandbox | Production | Archive |
|------------------|---------|------------|---------|
| local-sim        | ✓       | ✓          | ✗       |
| hybrid-sim       | ✓       | ✓          | ✗       |
| hardware-qpu-1   | restricted | ✓      | ✗       |
| hardware-qpu-2   | restricted | ✓      | ✗       |

---

# 4. Routing Integration

TriadicRouter uses backend metadata to:

- enforce resonance alignment  
- enforce drift envelopes  
- enforce environment constraints  
- select backend deterministically  
- open/close frames  

Routing decisions are recorded in `.qtrace`.

---

# 5. Invariants

Backend metadata obeys:

1. **resonance_profile is immutable**  
2. **drift_characteristic is immutable**  
3. **capabilities must be explicit**  
4. **environment constraints must be explicit**  
5. **archive always forbids execution**  
6. **metadata must be deterministic**  
7. **metadata must be replay‑compatible**  

Violating any invariant invalidates the backend.

---

# 6. Summary

This file defines the **canonical backend metadata schema** and the **2026 backend profiles** for qCompute.

Backends are:

- resonance‑tiered  
- drift‑characterized  
- environment‑aware  
- deterministic  
- structural  
- replay‑safe  

They enable qCompute to perform **governed, resonance‑aligned, drift‑bounded computation** across the triadic environment model.

---

Here is the **canonical `qc_Capture.md`** file, fully aligned with the entire qCompute module arc and with the file you currently have open in GitHub (tab 1774656502).  
Since you are *editing* that file, I will **not** summarize the page — I will deliver the **drop‑in‑ready canonical capture file** you asked for.

This file defines the **capture semantics**:  
how operators, frames, routing, drift, validation, and lineage are **captured into the `.qtrace` record**.

Place at:

```
/docs/rtt/Inside/qCompute/qc_Capture.md
```

---

# ✅ **qc_Capture.md — Capture Semantics (2026)**  
*(How operators, frames, routing, drift, and lineage are captured into trace)*

# qCompute — Capture Semantics  
**File:** qc_Capture.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This document defines the **capture semantics** of qCompute:  
how operators, frames, routing decisions, drift measurements, environment transitions, and lineage are **captured** into the `.qtrace` file.

Capture is the mechanism that transforms **runtime structure** into a **deterministic, replay‑safe record**.

---

# 1. Identity of Capture

Capture is:

- structural  
- append‑only  
- deterministic  
- invariant‑preserving  
- replay‑compatible  

Capture is **not**:

- a simulation  
- a numerical log  
- a backend‑specific trace  
- a symbolic representation  

Capture is the **structural serialization** of the qCompute execution pipeline.

---

# 2. Capture Pipeline

Capture occurs at the end of the execution pipeline:

```
Operator
    ↓
TriadicValidator
    ↓
TriadicRouter
    ↓
ResonanceFrame
    ↓
Backend Execution
    ↓
Capture → qTrace
```

Capture is triggered by:

- operator completion  
- frame closure  
- environment transition  
- session close  
- trace save  

---

# 3. What Capture Records

Capture records **exactly** the following:

1. **Operator metadata**  
2. **Validation metadata**  
3. **Routing metadata**  
4. **Drift predicted + measured**  
5. **Frame metadata**  
6. **Environment transitions**  
7. **Lineage entries**  
8. **Session header + footer**  

Capture does **not** record:

- backend internals  
- numerical amplitudes  
- hardware‑specific logs  
- simulator state  

Capture is structural only.

---

# 4. Operator Capture

Each operator is captured as:

```yaml
- op_id: "op-###"
  name: "operator_name"
  params: { ... }

  resonance_tier: "r1|r2|r3"
  drift_predicted: float
  drift_measured: float

  validation:
    allowed: true|false
    reason: string
    restricted_op: true|false
    env_ok: true|false
    backend_ok: true|false
    drift_ok: true|false
    lineage_ok: true|false

  routing:
    backend: backend-id
    resonance_profile: r1|r2|r3
    drift_characteristic: low|medium|high
    frame_id: frame-###
    reason: string
```

### Operator Capture Rules

- parameters must be explicit  
- validation is recorded, not recomputed  
- routing is recorded, not recomputed  
- drift is recorded, not recomputed  
- operator order is preserved  

---

# 5. Frame Capture

Each frame is captured as:

```yaml
frame_id: "frame-###"
timestamp_open: ...
timestamp_close: ...
env: "sandbox|production|archive"
backend: backend-id
resonance_profile: r1|r2|r3
drift_bound: relaxed|strict|immutable

operations: [ ... ]

drift_summary:
  predicted_total: float
  measured_total: float
```

### Frame Capture Rules

- backend is fixed per frame  
- resonance tier never decreases  
- drift bound is inherited from session  
- timestamps are monotonic  
- drift summary is finalized on closure  

---

# 6. Routing Capture

Routing metadata is captured **exactly as decided** by TriadicRouter.

Routing is **never recomputed** during replay.

Captured fields:

- backend  
- resonance_profile  
- drift_characteristic  
- frame_id  
- routing reason  

Routing is deterministic and must be preserved verbatim.

---

# 7. Drift Capture

Drift capture includes:

- predicted drift (pre‑execution)  
- measured drift (post‑execution)  
- accumulated drift per frame  

Drift is:

- enforced  
- recorded  
- immutable  
- replay‑read  

Drift is **never** recalculated during replay.

---

# 8. Environment Transition Capture

Transitions are captured as lineage entries:

```yaml
- env: "production"
  timestamp: ...
  token_used: "prod-2026-###"
```

Transition capture rules:

- forward‑only  
- append‑only  
- token‑gated  
- frame‑closing  
- immutable  

Archive transitions disable further capture of operators.

---

# 9. Lineage Capture

Lineage is the **environment history** of the session.

Captured as:

```yaml
lineage:
  - env: "sandbox"
  - env: "production"
  - env: "archive"
```

Lineage is:

- append‑only  
- forward‑only  
- replay‑deterministic  

---

# 10. Session Header Capture

The header is captured once at session creation:

```yaml
header:
  version: "2026.1"
  session_id: "sess-###"
  timestamp_start: ...
  env: "sandbox"
  backend: "auto"
  drift_bound: "relaxed"
  governance_snapshot:
    policy_version: "1.4.2"
    hash: "sha256-..."
```

Header is immutable.

---

# 11. Session Footer Capture

The footer is captured at trace finalization:

```yaml
footer:
  op_count: 42
  frame_count: 7
  hash: "sha256-..."
```

Footer ensures:

- integrity  
- completeness  
- replay determinism  

---

# 12. Capture Invariants

Capture obeys:

1. **Append‑only trace**  
2. **Forward‑only lineage**  
3. **Deterministic routing**  
4. **Deterministic validation**  
5. **Backend binding per frame**  
6. **Resonance tier never decreases**  
7. **Drift cannot be ignored**  
8. **Archive is immutable**  
9. **Replay is strict**  
10. **No silent behavior**  

Violating any invariant invalidates capture.

---

# 13. Summary

Capture is the mechanism that transforms qCompute execution into a **structural, deterministic, replay‑safe record**.

It records:

- operators  
- frames  
- routing  
- drift  
- validation  
- lineage  
- transitions  
- session metadata  

Capture is the **bridge** between runtime and replay.

---

Here is the **canonical `qc_Validator.md`** file: the full, invariant‑tight specification of the TriadicValidator, matching the structural key of the entire qCompute module arc.

This is one of the *core safety‑layer documents* of the Inside compute harness.  
It defines **exactly** how validation works, why it works that way, and how it integrates with routing, frames, drift, transitions, and `.qtrace`.

Place at:

```
/docs/rtt/Inside/qCompute/qc_Validator.md
```

---

# ✅ **qc_Validator.md — Full Validator Semantics (2026)**

# qCompute — TriadicValidator Semantics  
**File:** qc_Validator.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

The **TriadicValidator** is the safety gate of qCompute.  
It enforces all governance, drift, resonance, backend, and lineage rules before any operator is routed or executed.

Validation is:

- deterministic  
- structural  
- append‑only  
- replay‑recorded  
- invariant‑preserving  

Validation is **never** heuristic.

---

# 1. Identity

**Component:** TriadicValidator  
**Role:** Safety gate  
**Scope:** Operators → Frames → Routing → Transitions  
**Guarantee:** No unsafe or illegal operation enters the compute pipeline

Validator enforces:

1. policy legality  
2. environment legality  
3. backend compatibility  
4. resonance alignment  
5. drift bounds  
6. restricted‑op rules  
7. lineage safety  
8. archive immutability  

Validator is the **first structural checkpoint** in the qCompute pipeline.

---

# 2. Validation Pipeline

Validation occurs immediately after operator creation:

```
Operator
    ↓
TriadicValidator
    ↓
TriadicRouter
    ↓
ResonanceFrame
    ↓
Backend Execution
    ↓
Capture → qTrace
```

Validator produces:

- allow/block decision  
- validation metadata (captured in `.qtrace`)  

---

# 3. Validation Metadata Schema

Each operator receives a validation block:

```yaml
validation:
  allowed: true|false
  reason: string

  restricted_op: true|false
  env_ok: true|false
  backend_ok: true|false
  drift_ok: true|false
  lineage_ok: true|false
```

This metadata is:

- deterministic  
- immutable  
- captured verbatim  
- replay‑read  

Replay does **not** recompute validation.

---

# 4. Validation Rules

TriadicValidator enforces **seven rule families**.

---

## 4.1 Policy Legality

Checks:

- operator is defined in policy  
- operator category is allowed  
- operator parameters are valid  
- operator is not globally forbidden  

If illegal:

```
allowed = false
reason = "policy violation"
```

---

## 4.2 Environment Legality

Environment constraints:

| Operator Type | Sandbox | Production | Archive |
|---------------|---------|------------|---------|
| primitive     | ✓       | ✓          | ✗       |
| composite     | ✓       | ✓          | ✗       |
| pulse         | restricted | ✓      | ✗       |
| measurement   | ✓       | ✓          | ✗       |
| meta          | governed | governed   | governed |

If illegal:

```
allowed = false
reason = "environment violation"
```

Archive forbids **all** execution.

---

## 4.3 Backend Compatibility

Checks:

- operator category vs backend capabilities  
- operator resonance tier vs backend resonance profile  

If incompatible:

```
allowed = false
reason = "backend incompatibility"
```

---

## 4.4 Resonance Alignment

Rule:

```
operator.resonance_tier ≤ backend.resonance_profile
```

If violated:

```
allowed = false
reason = "resonance misalignment"
```

Resonance tier never decreases within a frame.

---

## 4.5 Drift Bound Enforcement

Rule:

```
operator.drift_predicted ≤ session.drift_bound
```

Where drift_bound is:

- relaxed (sandbox)  
- strict (production)  
- immutable (archive)  

If violated:

```
allowed = false
reason = "drift bound exceeded"
```

Drift is **never ignored**.

---

## 4.6 Restricted‑Op Rules

Pulse ops and certain meta‑ops require tokens.

If token missing:

```
allowed = false
reason = "restricted operation requires token"
```

---

## 4.7 Lineage Safety

Allowed transitions:

```
sandbox → production → archive
```

If operator implies illegal transition:

```
allowed = false
reason = "lineage violation"
```

Lineage is forward‑only and append‑only.

---

# 5. Archive Enforcement

Archive environment enforces:

- no operators  
- no frames  
- no routing  
- no drift  
- no execution  

Any operator in archive:

```
allowed = false
reason = "archive is immutable"
```

---

# 6. Frame Interaction

Validator interacts with frames by:

- closing frames on violations  
- closing frames on transitions  
- enforcing resonance tier monotonicity  
- enforcing drift accumulation  

If a violation occurs:

- frame closes  
- violation logged  
- operator blocked  

---

# 7. Routing Interaction

Validator runs **before** routing.

Routing only occurs if:

```
validation.allowed == true
```

Routing metadata is captured separately.

---

# 8. Capture Interaction

Validator metadata is captured in `.qtrace`:

- allowed  
- reason  
- restricted_op  
- env_ok  
- backend_ok  
- drift_ok  
- lineage_ok  

Replay reads this metadata **verbatim**.

---

# 9. Replay Semantics

Replay:

- reads validation metadata  
- does not recompute validation  
- enforces archive immutability  
- enforces lineage  
- enforces drift and resonance as recorded  

Replay is **strict**, not heuristic.

---

# 10. Invariants

TriadicValidator enforces:

1. **No silent behavior**  
2. **No illegal operator passes**  
3. **Forward‑only environments**  
4. **Append‑only lineage**  
5. **Deterministic validation**  
6. **Drift cannot be ignored**  
7. **Resonance tier never decreases**  
8. **Backend compatibility enforced**  
9. **Archive is immutable**  
10. **Replay is strict**  

Violating any invariant invalidates the session.

---

# 11. Summary

TriadicValidator is the **structural safety gate** of qCompute.

It ensures:

- policy legality  
- environment legality  
- backend compatibility  
- resonance alignment  
- drift enforcement  
- restricted‑op safety  
- lineage integrity  
- archive immutability  

Validation is deterministic, structural, and replay‑recorded — the foundation of qCompute’s governed compute model.

---

Here is the **canonical `qc_Router.md`** file: the full, invariant‑tight specification of the **TriadicRouter**, the deterministic routing engine of qCompute.

This file pairs directly with:

- `qc_Validator.md` (safety gate)  
- `qc_ResonanceFrame.md` (frame internals)  
- `qc_BackendProfiles.md` (backend metadata)  
- `qc_Flow.md` (pipeline narrative)  
- `qc_Capture.md` (trace capture semantics)

…and completes the core compute‑pipeline triad: **Validator → Router → Frame**.

Place at:

```
/docs/rtt/Inside/qCompute/qc_Router.md
```

---

# ✅ **qc_Router.md — Routing Engine Internals (2026)**

# qCompute — TriadicRouter Internals  
**File:** qc_Router.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

The **TriadicRouter** is the deterministic routing engine of qCompute.  
It selects the backend, enforces resonance alignment, enforces drift envelopes, and determines frame reuse vs. frame creation.

Routing is:

- deterministic  
- structural  
- invariant‑preserving  
- replay‑recorded  
- never heuristic  

Routing decisions are **captured verbatim** in `.qtrace`.

---

# 1. Identity

**Component:** TriadicRouter  
**Role:** Backend selection + frame management  
**Scope:** Operators → Frames → Backends  
**Guarantee:** Deterministic routing for all operators

TriadicRouter ensures:

1. backend compatibility  
2. resonance alignment  
3. drift envelope enforcement  
4. environment constraints  
5. frame reuse vs. frame creation  
6. deterministic routing metadata  

Routing is the **second structural checkpoint** after validation.

---

# 2. Routing Pipeline

Routing occurs immediately after validation:

```
Operator
    ↓
TriadicValidator
    ↓
TriadicRouter
    ↓
ResonanceFrame
    ↓
Backend Execution
    ↓
Capture → qTrace
```

Routing produces:

- backend selection  
- frame selection  
- routing metadata  

---

# 3. Routing Metadata Schema

Each operator receives a routing block:

```yaml
routing:
  backend: backend-id
  resonance_profile: r1|r2|r3
  drift_characteristic: low|medium|high
  frame_id: frame-###
  reason: string
```

This metadata is:

- deterministic  
- immutable  
- captured verbatim  
- replay‑read  

Replay does **not** recompute routing.

---

# 4. Routing Rules

TriadicRouter enforces **six rule families**.

---

## 4.1 Backend Selection

Backend selection follows this priority:

### 1. Explicit backend  
If `session.backend` is explicit:

```
use explicit backend
```

Unless incompatible → validation blocks.

### 2. Auto mode  
If backend = `"auto"`:

```
r1 → local-sim
r2 → hybrid-sim
r3 → hardware-qpu-2 (fallback: hardware-qpu-1)
```

### 3. Environment constraints  
If backend is restricted in current environment:

```
fallback to next compatible backend
```

If none exist → validation blocks.

---

## 4.2 Resonance Alignment

Rule:

```
operator.resonance_tier ≤ backend.resonance_profile
```

If violated:

- new backend selected (auto mode)  
- or validation blocks (explicit mode)  

Resonance tier never decreases within a frame.

---

## 4.3 Drift Envelope Enforcement

Rule:

```
backend.drift_characteristic ≤ session.drift_bound
```

Where drift_bound is:

- relaxed (sandbox)  
- strict (production)  
- immutable (archive)  

If violated:

- new backend selected (auto mode)  
- or validation blocks (explicit mode)  

Drift is **never ignored**.

---

## 4.4 Environment Constraints

Backends must satisfy:

| Backend          | Sandbox | Production | Archive |
|------------------|---------|------------|---------|
| local-sim        | ✓       | ✓          | ✗       |
| hybrid-sim       | ✓       | ✓          | ✗       |
| hardware-qpu-1   | restricted | ✓      | ✗       |
| hardware-qpu-2   | restricted | ✓      | ✗       |

If illegal:

- fallback (auto mode)  
- or validation blocks (explicit mode)  

Archive forbids all execution.

---

## 4.5 Frame Reuse vs. Frame Creation

Router decides whether to reuse the current frame or open a new one.

### Reuse frame if:

- backend unchanged  
- resonance tier unchanged  
- environment unchanged  
- drift bound unchanged  

### Create new frame if:

- backend changes  
- resonance tier escalates  
- environment transitions  
- drift overflow  
- explicit `qc.sync()` or `qc.barrier()`  

Frames are **backend‑bound** and **tier‑bound**.

---

## 4.6 Routing Reason

Router must record a human‑readable reason:

Examples:

```
"auto-routed (r1 operator)"
"explicit backend selected"
"resonance escalation (r2 → r3)"
"environment transition (sandbox → production)"
"backend restricted in sandbox; fallback applied"
```

Routing reason is captured in `.qtrace`.

---

# 5. Frame Interaction

TriadicRouter interacts with frames by:

- opening frames  
- reusing frames  
- closing frames (indirectly via transitions)  
- binding backend  
- binding resonance tier  
- enforcing drift bound  

Router never mutates existing frames.

---

# 6. Drift Interaction

Router enforces drift envelopes:

- predicted drift must fit backend drift characteristic  
- accumulated drift must fit frame drift bound  

If drift overflow:

- frame closes  
- new frame opens  
- routing metadata records overflow  

Drift is **never ignored**.

---

# 7. Environment Transition Interaction

Transitions force:

- frame closure  
- backend reevaluation  
- drift bound update  
- routing reason update  

Archive disables routing entirely.

---

# 8. Capture Interaction

Routing metadata is captured in `.qtrace`:

- backend  
- resonance_profile  
- drift_characteristic  
- frame_id  
- routing reason  

Replay reads this metadata **verbatim**.

---

# 9. Replay Semantics

Replay:

- reads routing metadata  
- reconstructs backend selection  
- reconstructs frame boundaries  
- reconstructs resonance tier  
- reconstructs drift envelopes  

Replay does **not** recompute routing.

Replay is **strict**, not heuristic.

---

# 10. Invariants

TriadicRouter enforces:

1. **Deterministic routing**  
2. **Backend binding per frame**  
3. **Resonance tier never decreases**  
4. **Drift cannot be ignored**  
5. **Environment constraints enforced**  
6. **Archive is immutable**  
7. **Trace is append‑only**  
8. **Replay is strict**  
9. **No silent behavior**  

Violating any invariant invalidates routing.

---

# 11. Summary

TriadicRouter is the **deterministic routing engine** of qCompute.

It ensures:

- backend compatibility  
- resonance alignment  
- drift envelope enforcement  
- environment legality  
- frame reuse vs. frame creation  
- deterministic routing metadata  

Routing is structural, governed, and replay‑safe — the backbone of qCompute’s execution semantics.

---

Here is the **canonical `qc_ResonanceFrame.md`** file.  
This completes the Validator → Router → Frame triad and locks in the *atomic compute envelope* of qCompute with full structural clarity, zero drift, and perfect alignment with every file we’ve built so far.

Place at:

```
/docs/rtt/Inside/qCompute/qc_ResonanceFrame.md
```

---

# ✅ **qc_ResonanceFrame.md — Frame Internals (2026)**

# qCompute — ResonanceFrame Internals  
**File:** qc_ResonanceFrame.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

A **ResonanceFrame** is the atomic compute envelope of qCompute.  
It binds execution to a single backend, resonance tier, drift bound, and environment.  
Frames group operations into deterministic, replay‑safe segments.

Frames are:

- backend‑bound  
- resonance‑tier‑bound  
- drift‑bounded  
- environment‑aware  
- append‑only  
- immutable after closure  

Frames are the structural unit that makes qCompute **safe**, **bounded**, and **replay‑deterministic**.

---

# 1. Identity

**Component:** ResonanceFrame  
**Role:** Atomic compute envelope  
**Scope:** Operators → Drift → Backend → Environment  
**Guarantee:** Deterministic, bounded execution segment

A frame is created when:

- the first operator is applied  
- backend changes  
- resonance tier escalates  
- environment transitions  
- drift overflow occurs  
- explicit `qc.sync()` or `qc.barrier()` is called  

A frame closes when:

- `qc.sync()` or `qc.barrier()` is called  
- backend must change  
- resonance tier escalates  
- environment transitions  
- drift overflow occurs  
- session closes  

---

# 2. Frame Metadata Schema

Each frame is captured in `.qtrace` as:

```yaml
frame_id: "frame-###"

timestamp_open: ...
timestamp_close: ...

env: "sandbox|production|archive"
backend: backend-id

resonance_profile: r1|r2|r3
drift_bound: relaxed|strict|immutable

operations:
  - op-001
  - op-002
  - ...

drift_summary:
  predicted_total: float
  measured_total: float
```

Frame metadata is:

- deterministic  
- immutable  
- replay‑compatible  

---

# 3. Frame Lifecycle

## 3.1 Opening a Frame

A frame opens when:

- the first operator arrives  
- backend changes  
- resonance tier escalates  
- environment transitions  
- drift overflow occurs  
- explicit sync/barrier  

Opening a frame sets:

- `frame_id`  
- `timestamp_open`  
- `env`  
- `backend`  
- `resonance_profile`  
- `drift_bound`  
- empty `operations[]`  
- zeroed drift accumulator  

---

## 3.2 Operating Within a Frame

While a frame is open:

- operators are appended in order  
- drift accumulates  
- resonance tier must not decrease  
- backend must not change  
- environment must not change  
- drift bound must not be exceeded  

If any rule is violated:

- frame closes  
- new frame opens  

---

## 3.3 Closing a Frame

A frame closes when:

- `qc.sync()`  
- `qc.barrier()`  
- backend change  
- resonance escalation  
- environment transition  
- drift overflow  
- session close  

Closing a frame:

- finalizes timestamps  
- finalizes drift summary  
- writes frame to `.qtrace`  
- marks frame immutable  

---

# 4. Resonance Tier Semantics

A frame has a **fixed resonance tier**:

```
r1 → r2 → r3 (allowed)
r3 → r2 or r1 (forbidden)
```

Rules:

- resonance tier may escalate within a session  
- resonance tier may not decrease within a frame  
- escalation forces a new frame  

This ensures:

- deterministic routing  
- deterministic replay  
- no silent tier downgrades  

---

# 5. Backend Binding

A frame binds to a **single backend**:

```
backend(frame) = backend(router decision at frame open)
```

Rules:

- backend cannot change mid‑frame  
- backend change forces new frame  
- backend metadata is captured in `.qtrace`  

This ensures:

- deterministic execution  
- deterministic replay  
- drift envelope stability  

---

# 6. Drift Semantics

Each frame enforces a **drift bound**:

```
drift_accumulated ≤ drift_bound
```

Where drift_bound is inherited from session:

- relaxed (sandbox)  
- strict (production)  
- immutable (archive)  

Drift semantics:

- predicted drift recorded per operator  
- measured drift recorded per operator  
- accumulated drift tracked per frame  
- drift overflow forces frame closure  

Drift is **never ignored**.

---

# 7. Environment Semantics

A frame inherits the session environment:

```
frame.env = session.env at frame open
```

Rules:

- environment cannot change mid‑frame  
- environment transition forces frame closure  
- archive forbids frame creation  

This ensures:

- lineage integrity  
- deterministic replay  
- environment‑aligned execution  

---

# 8. Operator Capture Within a Frame

Operators captured inside a frame include:

- operator metadata  
- validation metadata  
- routing metadata  
- drift predicted/measured  

Operators are appended in strict order.

Replay reconstructs:

- operator order  
- routing  
- validation  
- drift  
- frame boundaries  

Replay does **not** recompute anything.

---

# 9. Frame Invariants

ResonanceFrame enforces:

1. **Backend binding per frame**  
2. **Resonance tier never decreases**  
3. **Drift cannot be ignored**  
4. **Environment cannot change mid‑frame**  
5. **Append‑only operations**  
6. **Append‑only frames**  
7. **Archive forbids frame creation**  
8. **Trace is append‑only**  
9. **Replay is strict**  
10. **No silent behavior**  

Violating any invariant invalidates the frame.

---

# 10. Summary

A ResonanceFrame is the **atomic compute envelope** of qCompute.

It binds:

- backend  
- resonance tier  
- drift bound  
- environment  

It groups operations into deterministic, replay‑safe segments and ensures that qCompute remains:

- structural  
- governed  
- resonance‑aligned  
- drift‑bounded  
- environment‑aware  
- deterministic  
- replay‑safe  

Frames are the backbone of qCompute’s execution semantics.

---

Here is the **canonical `qc_Operators.md`** file: the full operator grammar, categories, resonance tiering, drift profiles, and structural semantics for qCompute.  
This file completes the core compute‑substrate triad and locks in the operator layer with zero drift and perfect alignment with Validator → Router → Frame → Capture → Replay.

Place at:

```
/docs/rtt/Inside/qCompute/qc_Operators.md
```

---

# ✅ **qc_Operators.md — Canonical Operator Grammar (2026)**

# qCompute — Operator Grammar & Categories  
**File:** qc_Operators.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This document defines the **canonical operator grammar** for qCompute:

- operator categories  
- resonance tiers  
- drift profiles  
- parameter grammar  
- backend compatibility  
- environment constraints  
- capture semantics  

Operators are **structural actions**, not numerical simulations.

---

# 1. Identity

**Component:** Operator  
**Role:** Atomic structural action in qCompute  
**Scope:** Validation → Routing → Frame → Backend → Capture → Replay  
**Guarantee:** Deterministic, explicit, invariant‑preserving

Operators are:

- explicit  
- typed  
- resonance‑tiered  
- drift‑profiled  
- backend‑compatible  
- environment‑aware  
- replay‑deterministic  

Operators are **immutable** after creation.

---

# 2. Operator Categories

qCompute defines **five canonical operator categories**:

| Category     | Description | Typical Tier | Drift |
|--------------|-------------|--------------|-------|
| primitive    | single‑qubit structural ops | r1 | low |
| composite    | multi‑qubit structural ops | r2 | medium |
| pulse        | hardware‑level pulse ops | r3 | high |
| measurement  | readout ops | r1 | low |
| meta         | structural/session ops | varies | none |

Each category has strict grammar and compatibility rules.

---

# 3. Resonance Tiers

Operators declare a **resonance tier**:

```
r1 — primitive + measurement
r2 — composite
r3 — pulse
```

Rules:

- tier must be explicit  
- tier determines backend compatibility  
- tier determines frame behavior  
- tier never decreases within a frame  
- tier escalation forces new frame  

---

# 4. Drift Profiles

Each operator declares a **drift profile**:

```
low     — r1
medium  — r2
high    — r3
```

Drift profile determines:

- drift prediction  
- drift accumulation  
- drift bound enforcement  
- frame overflow behavior  

Drift is **never ignored**.

---

# 5. Operator Grammar

All operators follow the canonical grammar:

```yaml
name: string
category: primitive|composite|pulse|measurement|meta
params: { ... }

resonance_tier: r1|r2|r3
drift_profile: low|medium|high

validation: { ... }
routing: { ... }
```

Operators are **fully explicit** — no implicit defaults.

---

# 6. Canonical Operators (2026)

## 6.1 Primitive Operators (r1)

```python
qc.x(qubit=0)
qc.z(qubit=1)
qc.h(qubit=0)
qc.y(qubit=0)
```

Metadata:

```
category: primitive
resonance_tier: r1
drift_profile: low
```

Backend compatibility:

- local-sim ✓  
- hybrid-sim ✓  
- hardware-qpu-* ✓  

---

## 6.2 Composite Operators (r2)

```python
qc.cnot(control=0, target=1)
qc.cz(control=0, target=1)
qc.swap(q0=0, q1=1)
```

Metadata:

```
category: composite
resonance_tier: r2
drift_profile: medium
```

Backend compatibility:

- hybrid-sim ✓  
- hardware-qpu-* ✓  
- local-sim ✗ (r2 unsupported)  

---

## 6.3 Pulse Operators (r3)

```python
qc.apply("pulse", qubit=0, duration="32ns", amplitude=0.8)
```

Metadata:

```
category: pulse
resonance_tier: r3
drift_profile: high
```

Backend compatibility:

- hardware-qpu-* ✓  
- hybrid-sim ✗  
- local-sim ✗  

Pulse ops require:

- production environment  
- token (restricted op)  

---

## 6.4 Measurement Operators (r1)

```python
qc.measure(qubit=0)
qc.measure_all()
```

Metadata:

```
category: measurement
resonance_tier: r1
drift_profile: low
```

Allowed in:

- sandbox ✓  
- production ✓  
- archive ✗  

---

## 6.5 Meta Operators

Meta operators modify session structure:

```python
qc.sync()
qc.barrier()
session.transition("production")
session.deploy_token("prod-2026-001")
```

Metadata:

```
category: meta
resonance_tier: none
drift_profile: none
```

Meta ops:

- close frames  
- update environment  
- update lineage  
- never enter backend execution  

---

# 7. Operator Compatibility Matrix

### 7.1 Category → Backend

| Category     | local-sim | hybrid-sim | hardware-qpu-1 | hardware-qpu-2 |
|--------------|-----------|------------|-----------------|----------------|
| primitive    | ✓         | ✓          | ✓               | ✓              |
| composite    | ✗         | ✓          | ✓               | ✓              |
| pulse        | ✗         | ✗          | ✓               | ✓              |
| measurement  | ✓         | ✓          | ✓               | ✓              |
| meta         | ✓         | ✓          | ✓               | ✓              |

---

### 7.2 Category → Environment

| Category     | Sandbox | Production | Archive |
|--------------|---------|------------|---------|
| primitive    | ✓       | ✓          | ✗       |
| composite    | ✓       | ✓          | ✗       |
| pulse        | restricted | ✓      | ✗       |
| measurement  | ✓       | ✓          | ✗       |
| meta         | governed | governed   | governed |

---

# 8. Operator Capture

Operators are captured with:

- name  
- params  
- resonance tier  
- drift predicted  
- drift measured  
- validation metadata  
- routing metadata  
- frame id  

Operators are **append‑only** in `.qtrace`.

Replay reads operator metadata **verbatim**.

---

# 9. Operator Invariants

Operators obey:

1. **Explicit category**  
2. **Explicit resonance tier**  
3. **Explicit drift profile**  
4. **No implicit defaults**  
5. **Tier never decreases within a frame**  
6. **Drift cannot be ignored**  
7. **Backend compatibility enforced**  
8. **Environment constraints enforced**  
9. **Archive forbids execution**  
10. **Trace is append‑only**  
11. **Replay is strict**  

Violating any invariant invalidates the operator.

---

# 10. Summary

This document defines the **canonical operator grammar** for qCompute:

- categories  
- resonance tiers  
- drift profiles  
- parameter grammar  
- backend compatibility  
- environment constraints  
- capture semantics  

Operators are the atomic structural actions of qCompute — explicit, governed, deterministic, and replay‑safe.

---

Here we go, the canonical **session internals + lifecycle** file for qCompute.  
This one ties a lot together: environment, backend intent, drift bound, lineage, frames, trace, transitions.

Place at:

`/docs/rtt/Inside/qCompute/qc_Session.md`

---

# qCompute — Session Internals & Lifecycle  
**File:** qc_Session.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

A **qSession** is the coherence container for qCompute.  
It owns environment, backend intent, drift bound, lineage, frames, and the trace buffer.  
All qCompute activity happens *inside* a session.

Sessions are:

- environment‑scoped  
- backend‑intent‑scoped  
- drift‑bounded  
- lineage‑tracked  
- frame‑aware  
- trace‑backed  
- replay‑deterministic  

---

# 1. Session identity

**Component:** qSession  
**Role:** Root container for qCompute  
**Scope:** env → backend intent → drift bound → lineage → frames → trace  
**Guarantee:** Coherent, governed execution context

A session is the **unit of governance** and the **unit of replay**.

---

# 2. Session state model

Core fields:

```yaml
session_id: string
env: sandbox | production | archive
backend: "auto" | backend-id
drift_bound: relaxed | strict | immutable

lineage: [ ... ]
frames: [ ... ]
trace_buffer: { ... }

governance_snapshot:
  policy_version: string
  hash: string
```

Rules:

- `session_id` is unique and immutable  
- `env` follows triadic model: sandbox → production → archive  
- `backend` is intent, not a driver  
- `drift_bound` is derived from env  
- `lineage` is append‑only  
- `frames` are append‑only  
- `trace_buffer` is append‑only  

---

# 3. Session lifecycle

## 3.1 Creation

Minimal pattern:

```python
from rtt_inside import qSession, qCompute

session = qSession(env="sandbox", backend="auto")
qc = qCompute(session)
```

On creation:

- `session_id` assigned  
- `env` set (default: sandbox)  
- `backend` set (default: auto)  
- `drift_bound` set from env  
- `lineage` initialized with `sandbox`  
- `frames` empty  
- `trace_buffer` initialized  
- `governance_snapshot` captured  

---

## 3.2 Active phase

During the active phase:

- operators are created via `qCompute`  
- TriadicValidator validates  
- TriadicRouter routes  
- ResonanceFrames open/close  
- drift accumulates per frame  
- environment may transition (forward‑only)  
- trace_buffer accumulates structural records  

The session remains active until:

- `session.save_trace(...)`  
- or explicit close (implementation‑specific)  

---

## 3.3 Finalization

Finalization pattern:

```python
session.save_trace("example.qtrace")
```

On finalization:

- any open frame closes  
- drift summaries finalize  
- footer written (op_count, frame_count, hash)  
- `.qtrace` file produced  
- session becomes replay‑only (conceptually)  

---

# 4. Environment & drift binding

Environment determines drift bound:

| Env        | Drift bound |
|------------|-------------|
| sandbox    | relaxed     |
| production | strict      |
| archive    | immutable   |

Session invariants:

- `env` follows sandbox → production → archive  
- `drift_bound` updates on transition  
- archive forbids execution  

Drift bound is read by:

- TriadicValidator  
- TriadicRouter  
- ResonanceFrame  

---

# 5. Backend intent

`session.backend` is **intent**, not a driver:

- `"auto"` → TriadicRouter selects backend by tier + env + drift  
- `"local-sim"` → explicit backend  
- `"hybrid-sim"` → explicit backend  
- `"hardware-qpu-*"` → explicit backend  

Rules:

- explicit backend honored unless incompatible (then validation blocks)  
- auto mode uses canonical mapping (r1→local‑sim, r2→hybrid‑sim, r3→hardware‑qpu‑2→hardware‑qpu‑1)  
- backend changes force new frame  

---

# 6. Lineage & transitions

Lineage is the environment history of the session.

Example:

```yaml
lineage:
  - env: "sandbox"
  - env: "production"
  - env: "archive"
```

Transitions:

```python
session.deploy_token("prod-2026-001")
session.transition("production")

session.deploy_token("arch-2026-001")
session.transition("archive")
```

Rules:

- forward‑only: sandbox → production → archive  
- token‑gated  
- frame‑closing  
- lineage append‑only  
- archive disables further execution  

---

# 7. Frames & session

Session owns all frames:

```yaml
frames:
  - frame-001
  - frame-002
  - ...
```

Session responsibilities:

- open first frame on first operator  
- close frames on sync/barrier/transition/overflow  
- ensure backend binding per frame  
- ensure tier monotonicity per frame  
- ensure drift bound per frame  

Frames are never mutated after closure.

---

# 8. Trace buffer & save

Session maintains an in‑memory trace buffer:

- header  
- lineage  
- frames  
- footer  

`session.save_trace(path)`:

- flushes buffer to `.qtrace`  
- computes integrity hash  
- finalizes footer  

Trace is:

- append‑only  
- deterministic  
- replay‑compatible  

---

# 9. Session invariants

qSession enforces:

1. **Forward‑only environments**  
2. **Append‑only lineage**  
3. **Environment‑driven drift bound**  
4. **Backend intent is explicit**  
5. **Frames are append‑only**  
6. **Trace is append‑only**  
7. **Archive forbids execution**  
8. **Replay is strict**  
9. **No silent behavior**  

Violating any invariant invalidates the session.

---

# 10. Summary

qSession is the **coherence container** of qCompute:

- owns env, backend intent, drift bound  
- owns lineage, frames, trace buffer  
- mediates transitions and finalization  

It ensures that all qCompute activity is:

- governed  
- drift‑bounded  
- environment‑aligned  
- frame‑structured  
- trace‑captured  
- replay‑deterministic  

---

Here is the **canonical `qc_Flow.md`** file.  
This is the *full pipeline narrative* for qCompute — the “how everything moves” document.  
It ties together **Operators → Validator → Router → Frame → Backend → Capture → Replay** into one coherent, structural flow.

This file is designed to be:

- minimal  
- canonical  
- AI‑parsable  
- student‑ready  
- zero‑drift  
- perfectly aligned with every qCompute file we’ve built  

Place at:

```
/docs/rtt/Inside/qCompute/qc_Flow.md
```

---

# ✅ **qc_Flow.md — Full Compute Pipeline Narrative (2026)**

# qCompute — Compute Pipeline Flow  
**File:** qc_Flow.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This document describes the **full structural flow** of qCompute:

```
Operator
  → Validator
  → Router
  → ResonanceFrame
  → Backend Execution
  → Capture
  → Replay
```

The pipeline is **deterministic**, **governed**, **drift‑bounded**, and **replay‑safe**.

---

# 1. Overview

The qCompute pipeline is a **linear, invariant‑preserving flow**:

1. Operator is created  
2. TriadicValidator checks legality  
3. TriadicRouter selects backend + frame  
4. ResonanceFrame groups operations  
5. Backend executes (structurally)  
6. Capture writes metadata to `.qtrace`  
7. Replay reconstructs deterministically  

Nothing in the pipeline is heuristic.  
Nothing is implicit.  
Nothing is recomputed during replay.

---

# 2. Stage 1 — Operator Creation

Operators are created via the `qCompute` interface:

```python
qc.h(qubit=0)
qc.cnot(control=0, target=1)
qc.apply("pulse", qubit=0, duration="32ns", amplitude=0.8)
```

Each operator is:

- explicit  
- typed  
- resonance‑tiered  
- drift‑profiled  
- immutable  

Operator metadata is structural, not numerical.

---

# 3. Stage 2 — TriadicValidator

Validator enforces:

- policy legality  
- environment legality  
- backend compatibility  
- resonance alignment  
- drift bound  
- restricted‑op rules  
- lineage safety  
- archive immutability  

Validator outputs:

```yaml
validation:
  allowed: true|false
  reason: "..."
  restricted_op: true|false
  env_ok: true|false
  backend_ok: true|false
  drift_ok: true|false
  lineage_ok: true|false
```

If validation fails:

- frame closes  
- violation logged  
- operator blocked  

Replay reads validation metadata **verbatim**.

---

# 4. Stage 3 — TriadicRouter

Router selects:

- backend  
- frame  
- resonance tier  
- drift envelope  

Router enforces:

- backend capabilities  
- resonance alignment  
- drift envelope  
- environment constraints  
- frame reuse vs. frame creation  

Router outputs:

```yaml
routing:
  backend: backend-id
  resonance_profile: r1|r2|r3
  drift_characteristic: low|medium|high
  frame_id: frame-###
  reason: "..."
```

Routing is **deterministic** and **replay‑recorded**.

---

# 5. Stage 4 — ResonanceFrame

A frame is the **atomic compute envelope**.

A frame binds:

- backend  
- resonance tier  
- drift bound  
- environment  

A frame opens when:

- first operator arrives  
- backend changes  
- resonance escalates  
- environment transitions  
- drift overflow occurs  
- explicit sync/barrier  

A frame closes when:

- sync/barrier  
- backend change  
- resonance escalation  
- environment transition  
- drift overflow  
- session close  

Frames are **append‑only** and **immutable after closure**.

---

# 6. Stage 5 — Backend Execution

Backend execution is structural:

- no simulation  
- no amplitudes  
- no hardware logs  
- no numerical state  

Execution produces:

- measured drift  
- backend‑level metadata  

Execution is bounded by:

- backend capabilities  
- drift characteristic  
- resonance profile  
- environment constraints  

Execution metadata is captured, not recomputed.

---

# 7. Stage 6 — Capture

Capture writes:

- operator metadata  
- validation metadata  
- routing metadata  
- drift predicted/measured  
- frame metadata  
- environment transitions  
- lineage  
- session header/footer  

Capture is **append‑only** and **deterministic**.

Example operator capture:

```yaml
- op_id: "op-003"
  name: "cnot"
  params: { control: 0, target: 1 }

  resonance_tier: r2
  drift_predicted: 0.004
  drift_measured: 0.003

  validation: { ... }
  routing: { ... }
```

Capture is the **bridge** between runtime and replay.

---

# 8. Stage 7 — Replay

Replay reconstructs:

- session  
- lineage  
- frames  
- routing  
- validation  
- drift  
- operator order  

Replay is **strict**, not heuristic:

- no recomputation  
- no re‑routing  
- no re‑validation  
- no re‑drift  
- no reinterpretation  

Replay is the **authoritative truth** of qCompute.

---

# 9. Full Pipeline Example

```python
session = qSession(env="sandbox", backend="auto")
qc = qCompute(session)

qc.h(qubit=0)                     # r1 → local-sim
qc.cnot(control=0, target=1)      # r2 → hybrid-sim (new frame)
qc.apply("pulse", qubit=0,
         duration="32ns",
         amplitude=0.8)           # r3 → hardware-qpu-2 (new frame)

qc.sync()
session.save_trace("flow_example.qtrace")
```

Produces:

```
frame-001: r1, backend=local-sim
frame-002: r2, backend=hybrid-sim
frame-003: r3, backend=hardware-qpu-2
```

Replay reconstructs this exactly.

---

# 10. Pipeline Invariants

The pipeline enforces:

1. **Forward‑only environments**  
2. **Append‑only lineage**  
3. **Deterministic validation**  
4. **Deterministic routing**  
5. **Backend binding per frame**  
6. **Resonance tier never decreases**  
7. **Drift cannot be ignored**  
8. **Archive is immutable**  
9. **Trace is append‑only**  
10. **Replay is strict**  
11. **No silent behavior**  

Violating any invariant invalidates the pipeline.

---

# 11. Summary

The qCompute pipeline is:

- structural  
- governed  
- resonance‑aligned  
- drift‑bounded  
- environment‑aware  
- deterministic  
- replay‑safe  

This flow is the **spine** of the qCompute module and the foundation of its safety, clarity, and teachability.

---

Here is the **canonical `qc_API.md`** file.  
This is the *public API surface* for qCompute: minimal, explicit, student‑ready, and perfectly aligned with every internal file we’ve built (Operators → Validator → Router → Frames → Capture → Session → Replay).

It is designed to be:

- zero‑drift  
- AI‑parsable  
- drop‑in‑ready  
- consistent with the 2026 qCompute canon  
- the *front‑door* for developers and students using the compute harness  

Place at:

```
/docs/rtt/Inside/qCompute/qc_API.md
```

---

# ✅ **qc_API.md — Canonical Public API Surface (2026)**

# qCompute — Public API Surface  
**File:** qc_API.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This document defines the **public API surface** for qCompute.  
It exposes the minimal, stable, student‑ready interface for:

- creating sessions  
- applying operators  
- managing frames  
- performing environment transitions  
- saving traces  
- replaying traces  

The API is intentionally small, explicit, and structural.

---

# 1. Import Surface

```python
from rtt_inside import qSession, qCompute, qReplay
```

These are the only public entry points.

---

# 2. qSession API

## 2.1 Create a session

```python
session = qSession(env="sandbox", backend="auto")
```

Parameters:

| Name    | Type   | Allowed Values                     | Notes |
|---------|--------|------------------------------------|-------|
| env     | str    | "sandbox" \| "production" \| "archive" | default: "sandbox" |
| backend | str    | "auto" \| backend-id               | intent, not a driver |

Session fields:

```python
session.env
session.backend
session.drift_bound
session.lineage
session.frames
```

---

## 2.2 Environment transitions

```python
session.deploy_token("prod-2026-001")
session.transition("production")

session.deploy_token("arch-2026-001")
session.transition("archive")
```

Rules:

- forward‑only  
- token‑gated  
- frame‑closing  
- archive forbids execution  

---

## 2.3 Save trace

```python
session.save_trace("example.qtrace")
```

Closes any open frame and writes the `.qtrace` file.

---

# 3. qCompute API

Create a compute handle:

```python
qc = qCompute(session)
```

Operators are methods on `qc`.

---

# 4. Operator API

Operators are grouped by category.

---

## 4.1 Primitive (r1)

```python
qc.x(qubit=0)
qc.y(qubit=0)
qc.z(qubit=1)
qc.h(qubit=0)
```

Parameters:

| Name  | Type | Notes |
|-------|------|--------|
| qubit | int  | required |

---

## 4.2 Composite (r2)

```python
qc.cnot(control=0, target=1)
qc.cz(control=0, target=1)
qc.swap(q0=0, q1=1)
```

Parameters:

| Name    | Type | Notes |
|---------|------|--------|
| control | int  | required |
| target  | int  | required |
| q0/q1   | int  | swap |

---

## 4.3 Pulse (r3)

```python
qc.apply("pulse", qubit=0, duration="32ns", amplitude=0.8)
```

Parameters:

| Name      | Type   | Notes |
|-----------|--------|--------|
| qubit     | int    | required |
| duration  | str    | required |
| amplitude | float  | required |

Pulse ops require:

- production environment  
- token (restricted op)  

---

## 4.4 Measurement (r1)

```python
qc.measure(qubit=0)
qc.measure_all()
```

Parameters:

| Name  | Type | Notes |
|-------|------|--------|
| qubit | int  | optional for `measure_all` |

---

## 4.5 Meta operators

```python
qc.sync()
qc.barrier()
```

Effects:

- close current frame  
- flush drift summary  
- enforce ordering  

---

# 5. Frame API (implicit)

Frames are not created directly.  
They are created automatically when:

- first operator arrives  
- backend changes  
- resonance escalates  
- environment transitions  
- drift overflow occurs  
- sync/barrier is called  

Frame metadata is accessible via:

```python
session.frames
```

---

# 6. Trace API

## 6.1 Save trace

```python
session.save_trace("example.qtrace")
```

## 6.2 Replay trace

```python
result = qReplay("example.qtrace").run()
```

Replay is:

- strict  
- deterministic  
- structural  
- non‑heuristic  

Replay reconstructs:

- session  
- lineage  
- frames  
- routing  
- validation  
- drift  
- operator order  

Replay does **not** recompute anything.

---

# 7. Error Model

qCompute raises structural errors:

| Error Name                 | Meaning |
|----------------------------|---------|
| `ValidationError`          | operator illegal |
| `BackendCompatibilityError`| backend cannot support operator |
| `ResonanceError`           | tier misalignment |
| `DriftBoundError`          | drift overflow |
| `EnvironmentTransitionError` | illegal transition |
| `ArchiveExecutionError`    | execution attempted in archive |

Errors are deterministic and captured in `.qtrace`.

---

# 8. Minimal Example

```python
session = qSession(env="sandbox", backend="auto")
qc = qCompute(session)

qc.h(qubit=0)
qc.cnot(control=0, target=1)

session.deploy_token("prod-2026-001")
session.transition("production")

qc.apply("pulse", qubit=0, duration="32ns", amplitude=0.8)

qc.sync()
session.save_trace("demo.qtrace")
```

Replay:

```python
qReplay("demo.qtrace").run()
```

---

# 9. Summary

The qCompute API exposes:

- `qSession` — environment, backend intent, drift, lineage, trace  
- `qCompute` — operator surface  
- `qReplay` — deterministic reconstruction  

The API is:

- minimal  
- explicit  
- governed  
- resonance‑aligned  
- drift‑bounded  
- environment‑aware  
- replay‑safe  

This is the **public front‑door** of the qCompute module.

---

Here is the **canonical `qc_Index.md`**, the *front‑door landing page* for the entire qCompute module.  
This is the page students, autodidacts, and AIs will hit first when entering the module.  
It is minimal, structural, zero‑drift, and perfectly aligned with the full qCompute arc we’ve built.

Place at:

```
/docs/rtt/Inside/qCompute/qc_Index.md
```

---

# ✅ **qc_Index.md — qCompute Module Index (2026)**

# qCompute — Module Index  
**File:** qc_Index.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

qCompute is the **compute harness** of the RTT‑Inside architecture.  
It provides a governed, resonance‑aligned, drift‑bounded execution model with deterministic routing, deterministic validation, and strict replay.

This index provides the **entry points** into the module.

---

# 1. What qCompute Is

qCompute is a:

- structural compute substrate  
- resonance‑tiered operator system  
- deterministic routing engine  
- drift‑bounded execution model  
- triadic environment container  
- append‑only trace generator  
- strict replay system  

It is **not** a simulator, numerical engine, or hardware driver.  
It is a **structural compute grammar**.

---

# 2. Start Here

If you are new to qCompute, begin with:

- **qc_Identity.md** — what the module *is*  
- **qc_Design.md** — why it is built this way  
- **qc_API.md** — the public API surface  
- **qc_Examples_Minimal.md** — smallest working examples  

These four files give you the complete conceptual foundation.

---

# 3. Core Compute Pipeline

The compute pipeline is:

```
Operator
  → Validator
  → Router
  → ResonanceFrame
  → Backend Execution
  → Capture
  → Replay
```

The following files define each stage:

- **qc_Operators.md** — operator grammar, categories, tiering  
- **qc_Validator.md** — full validator semantics  
- **qc_Router.md** — routing engine internals  
- **qc_ResonanceFrame.md** — frame internals  
- **qc_Capture.md** — capture semantics  
- **qc_Flow.md** — full pipeline narrative  
- **qc_Session.md** — session internals + lifecycle  
- **qc_BackendProfiles.md** — backend metadata schema  

Together, these files form the **structural spine** of qCompute.

---

# 4. Environment Model

qCompute uses the triadic environment model:

```
sandbox → production → archive
```

Environment rules are defined in:

- **qc_Transitions.md** — environment transition rules  
- **qc_Session.md** — environment binding + drift bound  
- **qc_Validator.md** — environment legality  
- **qc_Router.md** — environment‑aware routing  

Archive is immutable and replay‑only.

---

# 5. Backends

Backends are metadata objects, not drivers.

Defined in:

- **qc_Backends.md** (front‑door overview)  
- **qc_BackendProfiles.md** (full metadata schema)  

Backends define:

- resonance profile  
- drift characteristic  
- operator compatibility  
- environment constraints  

---

# 6. Examples

Two example sets are provided:

- **qc_Examples_Minimal.md** — micro‑examples  
- **qc_Examples_Advanced.md** — multi‑frame, multi‑backend workflows  

These demonstrate the full structural behavior of qCompute.

---

# 7. Testing & Internals

For maintainers and AI agents:

- **qc_Tests.md** — canonical test suite  
- **qc_Internals.md** — module‑wide architecture map  

These files define the internal invariants and structural guarantees.

---

# 8. File Map

The complete module consists of:

```
qc_Index.md                ← (this file)
qc_Identity.md
qc_Design.md
qc_API.md
qc_Operators.md
qc_Validator.md
qc_Router.md
qc_ResonanceFrame.md
qc_Backends.md
qc_BackendProfiles.md
qc_Session.md
qc_Transitions.md
qc_Capture.md
qc_Flow.md
qc_Examples_Minimal.md
qc_Examples_Advanced.md
qc_Tests.md
qc_Internals.md
```

---

# 9. Summary

qCompute is the **structural compute harness** of RTT‑Inside:

- governed  
- deterministic  
- resonance‑aligned  
- drift‑bounded  
- environment‑aware  
- trace‑captured  
- replay‑safe  

This index provides the **front door** into the module and links to every canonical file.

---

Here is the **canonical `qc_Backends.md`** file.  
This is the *front‑door overview* of the backend layer — the conceptual introduction that pairs with the deeper technical file (`qc_BackendProfiles.md`) and the routing/validator/frame documents.

This file is intentionally:

- minimal  
- structural  
- student‑ready  
- AI‑parsable  
- zero‑drift  
- consistent with the entire qCompute canon  

Place at:

```
/docs/rtt/Inside/qCompute/qc_Backends.md
```

---

# ✅ **qc_Backends.md — Backend Overview (2026)**

# qCompute — Backend Overview  
**File:** qc_Backends.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

Backends in qCompute are **metadata objects**, not drivers.  
They define the structural properties that govern routing, drift, resonance, and environment legality.

Backends do **not** simulate, emulate, or execute hardware.  
They provide the **metadata envelope** that the routing engine uses to make deterministic decisions.

---

# 1. Identity

A backend defines:

- resonance profile (r1/r2/r3)  
- drift characteristic (low/medium/high)  
- operator category compatibility  
- environment constraints  
- notes (optional metadata)  

Backends are:

- deterministic  
- immutable  
- structural  
- replay‑compatible  

Backends are **not**:

- hardware drivers  
- simulators  
- numerical engines  

---

# 2. Purpose of Backends

Backends serve four structural purposes:

1. **Resonance alignment**  
   - r1 → low‑tier ops  
   - r2 → mid‑tier ops  
   - r3 → pulse‑level ops  

2. **Drift envelope definition**  
   - low → stable  
   - medium → moderate  
   - high → hardware‑level  

3. **Environment constraints**  
   - sandbox: permissive  
   - production: governed  
   - archive: forbidden  

4. **Routing determinism**  
   - TriadicRouter uses backend metadata to select the correct backend for each operator  

Backends ensure qCompute remains **bounded**, **safe**, and **predictable**.

---

# 3. Canonical Backends (2026)

qCompute ships with **four canonical backends**.

These are defined fully in `qc_BackendProfiles.md`, but summarized here.

---

## 3.1 local-sim

- **Tier:** r1  
- **Drift:** low  
- **Ops:** primitive, composite, measurement  
- **Env:** sandbox ✓, production ✓, archive ✗  
- **Use:** default backend for r1 operators  

---

## 3.2 hybrid-sim

- **Tier:** r2  
- **Drift:** medium  
- **Ops:** primitive, composite, measurement  
- **Env:** sandbox ✓, production ✓, archive ✗  
- **Use:** r2 operators; bridge between simulation and hardware‑like behavior  

---

## 3.3 hardware-qpu-1

- **Tier:** r3  
- **Drift:** high  
- **Ops:** primitive, composite, pulse, measurement  
- **Env:** sandbox restricted, production ✓, archive ✗  
- **Use:** primary hardware‑aligned backend  

---

## 3.4 hardware-qpu-2

- **Tier:** r3  
- **Drift:** medium  
- **Ops:** primitive, composite, pulse, measurement  
- **Env:** sandbox restricted, production ✓, archive ✗  
- **Use:** stable hardware‑aligned backend; preferred for long r3 frames  

---

# 4. Backend Selection (Auto Mode)

When `session.backend = "auto"`:

```
r1 → local-sim
r2 → hybrid-sim
r3 → hardware-qpu-2 (fallback: hardware-qpu-1)
```

Auto mode is:

- deterministic  
- environment‑aware  
- drift‑aware  
- replay‑recorded  

Explicit backend overrides auto mode unless incompatible.

---

# 5. Backend Constraints

Backends enforce:

- operator category compatibility  
- resonance tier compatibility  
- drift envelope compatibility  
- environment legality  

If a backend cannot support an operator:

- auto mode → fallback  
- explicit mode → validation blocks  

Backends never silently downgrade or reinterpret operators.

---

# 6. Backend Interaction with Frames

Frames bind to a **single backend**:

```
frame.backend = backend selected at frame open
```

Rules:

- backend cannot change mid‑frame  
- backend change forces new frame  
- backend metadata is captured in `.qtrace`  

This ensures deterministic replay.

---

# 7. Backend Interaction with Routing

TriadicRouter uses backend metadata to:

- enforce resonance alignment  
- enforce drift envelopes  
- enforce environment constraints  
- select backend deterministically  
- open/close frames  

Routing metadata is captured verbatim.

---

# 8. Backend Interaction with Validation

TriadicValidator checks:

- backend compatibility  
- environment legality  
- drift legality  

If backend is incompatible:

- operator blocked  
- violation logged  
- frame closed (if needed)  

---

# 9. Backend Invariants

Backends obey:

1. **resonance_profile is immutable**  
2. **drift_characteristic is immutable**  
3. **capabilities must be explicit**  
4. **environment constraints must be explicit**  
5. **archive always forbids execution**  
6. **metadata must be deterministic**  
7. **metadata must be replay‑compatible**  

Violating any invariant invalidates the backend.

---

# 10. Summary

Backends are the **structural metadata layer** of qCompute.

They define:

- resonance  
- drift  
- compatibility  
- environment legality  

They enable:

- deterministic routing  
- bounded drift  
- safe execution  
- strict replay  

Backends are metadata, not drivers — the foundation of qCompute’s governed compute model.

---

Here is the **canonical `qc_Identity.md`** file.  
This is the *identity statement* for the qCompute module — the “what this module **is**” page.  
It is concise, structural, zero‑drift, and aligned with the entire qCompute arc we’ve built.

Place at:

```
/docs/rtt/Inside/qCompute/qc_Identity.md
```

---

# ✅ **qc_Identity.md — Module Identity (2026)**

# qCompute — Module Identity  
**File:** qc_Identity.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

qCompute is the **compute harness** of the RTT‑Inside architecture.  
It defines how structural quantum‑like operations are expressed, validated, routed, framed, drift‑bounded, captured, and replayed.

qCompute is not a simulator, not a numerical engine, and not a hardware driver.  
It is a **structural grammar** for governed computation.

---

# 1. What qCompute *Is*

qCompute is:

- a **resonance‑tiered operator system**  
- a **deterministic routing engine**  
- a **drift‑bounded execution model**  
- a **triadic environment container**  
- an **append‑only trace generator**  
- a **strict replay system**  
- a **governed compute substrate**  

It provides a **safe, bounded, deterministic** way to express structured computation inside RTT‑Inside.

---

# 2. What qCompute *Is Not*

qCompute is **not**:

- a quantum simulator  
- a numerical amplitude engine  
- a hardware abstraction layer  
- a probabilistic model  
- a physics simulator  
- a compiler or optimizer  

It does not compute amplitudes, wavefunctions, or hardware signals.  
It computes **structure**, not physics.

---

# 3. Core Identity Principles

qCompute is built on seven identity principles:

1. **Structural, not numerical**  
   Operators describe structure, not amplitudes.

2. **Deterministic, not heuristic**  
   Routing, validation, drift, and replay are deterministic.

3. **Governed, not permissive**  
   All operations pass through explicit safety gates.

4. **Resonance‑aligned**  
   Operators declare resonance tiers (r1/r2/r3).

5. **Drift‑bounded**  
   Every operation has predicted/measured drift; drift is never ignored.

6. **Environment‑aware**  
   sandbox → production → archive  
   Forward‑only, token‑gated, frame‑closing.

7. **Replay‑safe**  
   `.qtrace` is the authoritative record; replay never recomputes.

---

# 4. The Triadic Model

qCompute operates inside the triadic environment model:

```
sandbox → production → archive
```

- **sandbox** — exploratory, relaxed drift  
- **production** — governed, strict drift  
- **archive** — immutable, replay‑only  

Environment transitions are:

- forward‑only  
- token‑gated  
- frame‑closing  
- lineage‑tracked  

This model ensures safety, determinism, and reproducibility.

---

# 5. The Compute Spine

qCompute’s identity is defined by its pipeline:

```
Operator
  → Validator
  → Router
  → ResonanceFrame
  → Backend Execution
  → Capture
  → Replay
```

Each stage is:

- explicit  
- deterministic  
- invariant‑preserving  
- captured in `.qtrace`  

This pipeline is the **spine** of the module.

---

# 6. The Role of Backends

Backends are **metadata envelopes**, not drivers.

They define:

- resonance profile  
- drift characteristic  
- operator compatibility  
- environment constraints  

Routing uses backend metadata to make deterministic decisions.

---

# 7. The Role of Frames

A ResonanceFrame is the **atomic compute envelope**.

It binds:

- backend  
- resonance tier  
- drift bound  
- environment  

Frames are append‑only and immutable after closure.

---

# 8. The Role of Trace

`.qtrace` is the **structural record** of a session.

It captures:

- operators  
- validation  
- routing  
- drift  
- frames  
- lineage  
- transitions  
- header/footer  

Trace is append‑only and replay‑deterministic.

---

# 9. The Role of Replay

Replay reconstructs:

- session  
- lineage  
- frames  
- routing  
- validation  
- drift  
- operator order  

Replay is **strict**, not heuristic.  
Replay is the **authoritative truth** of qCompute.

---

# 10. Summary

qCompute is the **structural compute harness** of RTT‑Inside:

- resonance‑tiered  
- drift‑bounded  
- environment‑aware  
- deterministic  
- governed  
- trace‑captured  
- replay‑safe  

It provides a safe, explicit, invariant‑preserving grammar for structured computation.

---

Here is the **canonical `qc_Design.md`** file.  
This is the *design philosophy + invariants narrative* for the entire qCompute module — the “why this module is built this way” page.  
It completes the conceptual triad with `qc_Identity.md` (what it is) and `qc_Flow.md` (how it moves).

Place at:

```
/docs/rtt/Inside/qCompute/qc_Design.md
```

---

# ✅ **qc_Design.md — Design Philosophy & Invariants (2026)**

# qCompute — Design Philosophy & Invariants  
**File:** qc_Design.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

qCompute is designed as a **governed compute substrate** inside RTT‑Inside.  
Its design is shaped by three forces:

1. **Resonance-first structure**  
2. **Deterministic governance**  
3. **Replay as the authoritative truth**

This document explains *why* qCompute is built the way it is.

---

# 1. Design Goals

qCompute is designed to:

- provide a **structural compute grammar**  
- enforce **deterministic safety**  
- guarantee **drift-bounded execution**  
- maintain **environment integrity**  
- produce **replay-deterministic traces**  
- avoid numerical simulation  
- avoid hardware abstraction  

The goal is **clarity, safety, determinism, and teachability**.

---

# 2. Structural, Not Numerical

qCompute does **not** simulate amplitudes or physics.

It models:

- operator structure  
- resonance tier  
- drift envelope  
- backend metadata  
- environment legality  
- routing decisions  
- frame boundaries  
- lineage  

This makes qCompute:

- predictable  
- inspectable  
- replayable  
- safe for students and AIs  

Numerical engines are intentionally excluded.

---

# 3. Deterministic Governance

Every operator passes through:

1. **TriadicValidator**  
2. **TriadicRouter**  
3. **ResonanceFrame**  
4. **Capture**  

Each stage is:

- deterministic  
- explicit  
- invariant-preserving  
- replay-recorded  

Nothing is implicit.  
Nothing is heuristic.  
Nothing is recomputed during replay.

---

# 4. Resonance-Tiered Design

Operators declare a **resonance tier**:

```
r1 — primitive + measurement
r2 — composite
r3 — pulse
```

Design motivations:

- clarity for students  
- deterministic routing  
- backend compatibility  
- drift envelope alignment  
- frame boundary enforcement  

Tier escalation forces new frames.  
Tier downgrades are forbidden.

---

# 5. Drift-Bounded Execution

Every operator has:

- predicted drift  
- measured drift  
- drift profile (low/medium/high)

Drift is:

- accumulated per frame  
- bounded by environment  
- enforced by validator  
- enforced by router  
- captured in trace  
- replay-read  

Drift is **never ignored**.

This ensures:

- safety  
- determinism  
- reproducibility  

---

# 6. Triadic Environment Model

qCompute uses the triadic environment model:

```
sandbox → production → archive
```

Design motivations:

- sandbox: exploration, relaxed drift  
- production: governed, strict drift  
- archive: immutable, replay-only  

Transitions are:

- forward-only  
- token-gated  
- frame-closing  
- lineage-tracked  

This ensures:

- governance  
- safety  
- reproducibility  

---

# 7. Frames as Atomic Compute Envelopes

A **ResonanceFrame** binds:

- backend  
- resonance tier  
- drift bound  
- environment  

Frames are:

- append-only  
- immutable after closure  
- deterministic  
- replay-safe  

Design motivations:

- isolate drift  
- isolate backend  
- isolate environment  
- isolate resonance tier  
- provide structural clarity  

Frames are the backbone of qCompute.

---

# 8. Backends as Metadata, Not Drivers

Backends define:

- resonance profile  
- drift characteristic  
- operator compatibility  
- environment constraints  

Backends do **not**:

- simulate  
- emulate  
- execute hardware  

Design motivations:

- clarity  
- determinism  
- replay safety  
- pedagogical simplicity  

Backends are metadata envelopes.

---

# 9. Trace as the Authoritative Record

`.qtrace` captures:

- operators  
- validation  
- routing  
- drift  
- frames  
- lineage  
- transitions  
- header/footer  

Trace is:

- append-only  
- deterministic  
- replay-compatible  

Design motivation:

> **Replay is the authoritative truth.**

Replay never recomputes:

- validation  
- routing  
- drift  
- frame boundaries  

Replay reconstructs exactly what happened.

---

# 10. Invariants

qCompute enforces eleven non-negotiable invariants:

1. **Forward-only environments**  
2. **Append-only lineage**  
3. **Deterministic validation**  
4. **Deterministic routing**  
5. **Backend binding per frame**  
6. **Resonance tier never decreases**  
7. **Drift cannot be ignored**  
8. **Archive is immutable**  
9. **Trace is append-only**  
10. **Replay is strict**  
11. **No silent behavior**  

Violating any invariant invalidates the session.

---

# 11. Why This Design Works

This design gives qCompute:

- **predictability** — no hidden behavior  
- **safety** — drift, environment, and routing are governed  
- **clarity** — operators are explicit and typed  
- **teachability** — students can reason structurally  
- **reproducibility** — replay is exact  
- **AI-friendliness** — metadata is explicit and parseable  

qCompute is a **structural compute substrate**, not a numerical engine.

---

# 12. Summary

qCompute is designed to be:

- structural  
- deterministic  
- governed  
- resonance-aligned  
- drift-bounded  
- environment-aware  
- trace-captured  
- replay-safe  

Its design philosophy ensures clarity, safety, and reproducibility for students, autodidacts, and AI agents.

---

Here is the **canonical `qc_Transitions.md`** file.  
This is the *full environment‑transition semantics* for qCompute — the structural rules governing movement through the triadic model:

```
sandbox → production → archive
```

This file is one of the “hard law” documents of the module.  
It must be crisp, invariant‑tight, and perfectly aligned with Validator, Router, Session, Frames, and Capture.

Place at:

```
/docs/rtt/Inside/qCompute/qc_Transitions.md
```

---

# ✅ **qc_Transitions.md — Environment Transition Rules (2026)**

# qCompute — Environment Transition Rules  
**File:** qc_Transitions.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

qCompute uses the **triadic environment model**:

```
sandbox → production → archive
```

Transitions are:

- forward‑only  
- token‑gated  
- frame‑closing  
- lineage‑tracked  
- drift‑bound‑changing  
- replay‑recorded  

This document defines the **canonical rules** for environment transitions.

---

# 1. Identity

**Component:** Environment Transition  
**Role:** Move session between governance regimes  
**Scope:** Session → Frames → Drift → Routing → Validation → Capture  
**Guarantee:** Deterministic, governed, replay‑safe transitions

Transitions affect:

- drift bound  
- backend legality  
- operator legality  
- frame boundaries  
- lineage  
- routing  
- capture  

---

# 2. The Triadic Model

## 2.1 sandbox

- relaxed drift  
- permissive operator set  
- pulse ops restricted  
- backends: local‑sim, hybrid‑sim  
- hardware backends restricted  

## 2.2 production

- strict drift  
- governed operator set  
- pulse ops allowed with token  
- hardware backends allowed  
- routing becomes stricter  

## 2.3 archive

- immutable  
- no operators  
- no frames  
- no routing  
- no drift  
- replay‑only  

Archive is the **terminal state**.

---

# 3. Transition Rules

## 3.1 Allowed transitions

```
sandbox → production → archive
```

## 3.2 Forbidden transitions

```
production → sandbox
archive → production
archive → sandbox
sandbox → archive (direct)
```

Transitions are **forward‑only**.

---

# 4. Token Requirements

Transitions require explicit tokens:

```python
session.deploy_token("prod-2026-001")
session.transition("production")
```

```python
session.deploy_token("arch-2026-001")
session.transition("archive")
```

Tokens enforce:

- governance  
- auditability  
- replay‑determinism  

Tokens are captured in lineage.

---

# 5. Frame Interaction

Transitions are **frame‑closing events**.

When a transition occurs:

- current frame closes  
- drift summary finalizes  
- new frame opens (except archive)  
- routing reevaluates backend  
- drift bound updates  

Archive forbids new frames.

---

# 6. Drift Bound Changes

Environment determines drift bound:

| Env        | Drift Bound |
|------------|-------------|
| sandbox    | relaxed     |
| production | strict      |
| archive    | immutable   |

Transition effects:

- sandbox → production: relaxed → strict  
- production → archive: strict → immutable  

Immutable drift forbids all execution.

---

# 7. Backend Legality Changes

Transition effects:

### sandbox → production
- hardware backends become allowed  
- pulse ops become allowed (with token)  
- drift bound tightens  

### production → archive
- all backends forbidden  
- all operators forbidden  
- routing disabled  

Archive is replay‑only.

---

# 8. Operator Legality Changes

Transition effects:

### sandbox → production
- restricted ops become allowed  
- pulse ops allowed with token  
- composite ops unchanged  
- primitive ops unchanged  

### production → archive
- all ops forbidden  

Validator enforces these rules.

---

# 9. Lineage Capture

Each transition appends a lineage entry:

```yaml
- env: "production"
  timestamp: ...
  token_used: "prod-2026-001"
```

Lineage is:

- append‑only  
- forward‑only  
- replay‑deterministic  

Replay reconstructs lineage exactly.

---

# 10. Capture Semantics

Transitions are captured in `.qtrace`:

- environment change  
- token used  
- timestamp  
- frame closure  
- drift summary  
- new frame metadata (except archive)  

Archive finalizes the trace.

---

# 11. Replay Semantics

Replay:

- reads lineage  
- reconstructs transitions  
- enforces forward‑only model  
- enforces archive immutability  
- reconstructs frame boundaries  
- reconstructs drift bound changes  

Replay never recomputes transitions.

---

# 12. Transition Invariants

Environment transitions obey:

1. **Forward‑only environments**  
2. **Token‑gated transitions**  
3. **Frame‑closing transitions**  
4. **Drift bound updates**  
5. **Backend legality updates**  
6. **Operator legality updates**  
7. **Archive immutability**  
8. **Append‑only lineage**  
9. **Trace is append‑only**  
10. **Replay is strict**  
11. **No silent behavior**  

Violating any invariant invalidates the session.

---

# 13. Summary

Environment transitions are:

- forward‑only  
- token‑gated  
- drift‑bound‑changing  
- backend‑changing  
- operator‑legality‑changing  
- frame‑closing  
- lineage‑tracked  
- replay‑deterministic  

The triadic model ensures qCompute remains governed, safe, and reproducible.

---

Here is the **canonical `qc_Examples_Minimal.md`** file.  
This is the *smallest possible*, *student‑ready*, *zero‑drift*, *structural* example set for qCompute.  
It demonstrates the full pipeline using **only r1/r2/r3 operators**, **auto routing**, **frame boundaries**, **drift**, and **environment transitions** — all in the most compact form possible.

Place at:

```
/docs/rtt/Inside/qCompute/qc_Examples_Minimal.md
```

---

# ✅ **qc_Examples_Minimal.md — Minimal Examples (2026)**

# qCompute — Minimal Examples  
**File:** qc_Examples_Minimal.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

These examples demonstrate the **smallest possible patterns** that exercise the full qCompute pipeline:

```
Operator → Validator → Router → Frame → Backend → Capture → Replay
```

All examples are structural, deterministic, and replay‑safe.

---

# 1. Minimal r1 Example (single frame)

```python
from rtt_inside import qSession, qCompute

session = qSession(env="sandbox", backend="auto")
qc = qCompute(session)

qc.h(qubit=0)
qc.x(qubit=1)
qc.measure(qubit=0)

session.save_trace("r1_minimal.qtrace")
```

**What this demonstrates**

- r1 operators  
- local-sim backend  
- single frame  
- relaxed drift  
- sandbox environment  
- deterministic capture  

---

# 2. Minimal r1 → r2 Escalation (two frames)

```python
session = qSession(env="sandbox", backend="auto")
qc = qCompute(session)

qc.h(qubit=0)                     # r1 → local-sim (frame-001)
qc.cnot(control=0, target=1)      # r2 → hybrid-sim (frame-002)

session.save_trace("r1_r2.qtrace")
```

**What this demonstrates**

- resonance escalation  
- automatic backend change  
- automatic frame boundary  
- deterministic routing  

---

# 3. Minimal r3 Example (pulse op)

```python
session = qSession(env="production", backend="auto")
qc = qCompute(session)

qc.apply("pulse", qubit=0, duration="32ns", amplitude=0.8)

session.save_trace("r3_minimal.qtrace")
```

**What this demonstrates**

- r3 operator  
- hardware backend  
- strict drift  
- production environment  
- pulse legality  

---

# 4. Minimal Environment Transition

```python
session = qSession(env="sandbox", backend="auto")
qc = qCompute(session)

qc.h(qubit=0)

session.deploy_token("prod-2026-001")
session.transition("production")   # closes frame-001

qc.cnot(control=0, target=1)       # new frame-002 (r2 → hybrid-sim)

session.save_trace("transition_minimal.qtrace")
```

**What this demonstrates**

- sandbox → production transition  
- token requirement  
- frame closure on transition  
- drift bound tightening  
- deterministic lineage  

---

# 5. Minimal Multi-Backend Example

```python
session = qSession(env="production", backend="auto")
qc = qCompute(session)

qc.h(qubit=0)                     # r1 → local-sim (frame-001)
qc.cnot(control=0, target=1)      # r2 → hybrid-sim (frame-002)
qc.apply("pulse", qubit=0,
         duration="32ns",
         amplitude=0.8)           # r3 → hardware-qpu-2 (frame-003)

session.save_trace("multi_backend.qtrace")
```

**What this demonstrates**

- r1 → r2 → r3 tier progression  
- three backends  
- three frames  
- deterministic routing  
- drift envelope changes  

---

# 6. Minimal Sync/Barrier Example

```python
session = qSession(env="sandbox", backend="auto")
qc = qCompute(session)

qc.h(qubit=0)
qc.sync()                         # closes frame-001
qc.x(qubit=1)                     # opens frame-002

session.save_trace("sync_minimal.qtrace")
```

**What this demonstrates**

- explicit frame closure  
- deterministic frame boundaries  
- sync as structural operator  

---

# 7. Minimal Replay Example

```python
from rtt_inside import qReplay

result = qReplay("r1_minimal.qtrace").run()
```

**What this demonstrates**

- strict replay  
- deterministic reconstruction  
- no recomputation of routing/validation/drift  

---

# 8. Summary

These minimal examples demonstrate:

- r1/r2/r3 operators  
- resonance escalation  
- backend selection  
- frame boundaries  
- drift behavior  
- environment transitions  
- sync/barrier  
- trace generation  
- strict replay  

They form the **smallest complete demonstration** of the qCompute pipeline.

---

Here is the **canonical `qc_Examples_Advanced.md`** file.  
This is the *full‑pipeline*, *multi‑frame*, *multi‑backend*, *multi‑transition*, *drift‑heavy*, *structurally rich* example set.  
It is designed to exercise **every invariant** of qCompute in realistic, pedagogical, AI‑parsable form.

Place at:

```
/docs/rtt/Inside/qCompute/qc_Examples_Advanced.md
```

---

# ✅ **qc_Examples_Advanced.md — Advanced Examples (2026)**

# qCompute — Advanced Examples  
**File:** qc_Examples_Advanced.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

These examples demonstrate **full‑pipeline behavior** across:

- multi‑frame execution  
- multi‑backend routing  
- resonance escalation  
- drift accumulation + overflow  
- environment transitions  
- restricted operations  
- sync/barrier boundaries  
- deterministic capture  
- strict replay  

These examples are designed for students, autodidacts, and AI agents.

---

# 1. Multi‑Frame, Multi‑Backend, Multi‑Tier Example

```python
session = qSession(env="sandbox", backend="auto")
qc = qCompute(session)

# Frame 001 — r1 → local-sim
qc.h(qubit=0)
qc.x(qubit=1)

# Frame 002 — r2 → hybrid-sim
qc.cnot(control=0, target=1)

# Frame 003 — r3 → hardware-qpu-2 (restricted in sandbox)
session.deploy_token("prod-2026-001")
session.transition("production")

qc.apply("pulse", qubit=0, duration="32ns", amplitude=0.8)

session.save_trace("advanced_multiframe.qtrace")
```

**Demonstrates**

- r1 → r2 → r3 tier progression  
- backend changes  
- sandbox → production transition  
- token requirement  
- frame boundaries  
- drift bound tightening  

---

# 2. Drift Overflow Example (forced frame closure)

```python
session = qSession(env="production", backend="auto")
qc = qCompute(session)

# Frame 001 — r2 → hybrid-sim
qc.cnot(control=0, target=1)
qc.cnot(control=1, target=0)

# Drift overflow forces new frame
qc.cnot(control=0, target=1)   # opens frame-002

session.save_trace("drift_overflow.qtrace")
```

**Demonstrates**

- drift accumulation  
- drift bound enforcement  
- automatic frame closure  
- deterministic routing  

---

# 3. Multi‑Transition Example (sandbox → production → archive)

```python
session = qSession(env="sandbox", backend="auto")
qc = qCompute(session)

qc.h(qubit=0)

# Transition to production
session.deploy_token("prod-2026-001")
session.transition("production")

qc.cnot(control=0, target=1)

# Transition to archive
session.deploy_token("arch-2026-001")
session.transition("archive")

session.save_trace("multi_transition.qtrace")
```

**Demonstrates**

- forward‑only transitions  
- token gating  
- frame closure on transitions  
- archive immutability  
- lineage capture  

---

# 4. Pulse‑Heavy Example (r3‑dominant workflow)

```python
session = qSession(env="production", backend="auto")
qc = qCompute(session)

qc.apply("pulse", qubit=0, duration="16ns", amplitude=0.4)
qc.apply("pulse", qubit=1, duration="32ns", amplitude=0.7)
qc.apply("pulse", qubit=0, duration="48ns", amplitude=0.9)

qc.sync()   # closes r3 frame

qc.measure_all()

session.save_trace("pulse_heavy.qtrace")
```

**Demonstrates**

- r3 pulse sequences  
- hardware backend  
- strict drift  
- sync boundary  
- measurement after pulse frame  

---

# 5. Mixed‑Tier, Mixed‑Backend, Mixed‑Drift Example

```python
session = qSession(env="production", backend="auto")
qc = qCompute(session)

# Frame 001 — r1 → local-sim
qc.h(qubit=0)

# Frame 002 — r2 → hybrid-sim
qc.cnot(control=0, target=1)

# Frame 003 — r3 → hardware-qpu-2
qc.apply("pulse", qubit=0, duration="32ns", amplitude=0.8)

# Frame 004 — r1 again (new frame because tier cannot decrease)
qc.sync()
qc.x(qubit=1)

session.save_trace("mixed_tier_backend_drift.qtrace")
```

**Demonstrates**

- tier escalation  
- tier non‑decrease rule  
- backend changes  
- sync boundary  
- deterministic frame segmentation  

---

# 6. Full‑Pipeline Example (everything in one)

```python
session = qSession(env="sandbox", backend="auto")
qc = qCompute(session)

# r1 frame
qc.h(qubit=0)
qc.x(qubit=1)

# r2 frame
qc.cnot(control=0, target=1)

# transition to production
session.deploy_token("prod-2026-001")
session.transition("production")

# r3 frame
qc.apply("pulse", qubit=0, duration="32ns", amplitude=0.8)

# drift overflow → new r3 frame
qc.apply("pulse", qubit=1, duration="48ns", amplitude=0.9)

qc.sync()

# transition to archive
session.deploy_token("arch-2026-001")
session.transition("archive")

session.save_trace("full_pipeline.qtrace")
```

**Demonstrates**

- r1 → r2 → r3 tier progression  
- multi‑backend routing  
- drift overflow  
- sync boundary  
- sandbox → production → archive  
- token gating  
- deterministic capture  
- strict replay  

---

# 7. Replay Example (for any advanced trace)

```python
from rtt_inside import qReplay

result = qReplay("full_pipeline.qtrace").run()
```

**Demonstrates**

- strict replay  
- deterministic reconstruction  
- no re‑validation  
- no re‑routing  
- no re‑drift  
- no reinterpretation  

---

# 8. Summary

These advanced examples demonstrate:

- multi‑frame execution  
- multi‑backend routing  
- resonance escalation  
- drift accumulation + overflow  
- environment transitions  
- restricted operations  
- sync/barrier boundaries  
- deterministic capture  
- strict replay  

They form the **complete structural demonstration** of the qCompute module.

---

Here is the **canonical `qc_Tests.md`** file.  
This is the *test suite spine* for the entire qCompute module — the invariants, fixtures, structural expectations, and replay‑deterministic behaviors that every implementation must satisfy.

It is intentionally:

- minimal  
- structural  
- invariant‑first  
- AI‑parsable  
- zero‑drift  
- aligned with every file in the qCompute arc  

Place at:

```
/docs/rtt/Inside/qCompute/qc_Tests.md
```

---

# ✅ **qc_Tests.md — Canonical Test Suite Structure (2026)**

# qCompute — Canonical Test Suite  
**File:** qc_Tests.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This document defines the **canonical test suite** for qCompute.  
It ensures that all implementations preserve:

- structural invariants  
- deterministic routing  
- deterministic validation  
- drift‑bounded execution  
- environment integrity  
- frame correctness  
- trace correctness  
- strict replay  

Tests are structural, not numerical.

---

# 1. Test Philosophy

qCompute tests verify:

- **structure**, not physics  
- **determinism**, not probability  
- **governance**, not heuristics  
- **replay correctness**, not recomputation  

Every test must be:

- deterministic  
- invariant‑preserving  
- replay‑verifiable  
- minimal  

---

# 2. Test Categories

The canonical suite contains eight categories:

1. **Operator Tests**  
2. **Validation Tests**  
3. **Routing Tests**  
4. **Frame Tests**  
5. **Drift Tests**  
6. **Environment Transition Tests**  
7. **Trace Tests**  
8. **Replay Tests**

Each category contains structural fixtures.

---

# 3. Operator Tests

## 3.1 Primitive Operators

- `qc.h(qubit=0)`  
- `qc.x(qubit=1)`  

**Assertions**

- category = primitive  
- resonance_tier = r1  
- drift_profile = low  
- backend = local-sim  
- frame count = 1  

---

## 3.2 Composite Operators

- `qc.cnot(control=0, target=1)`  

**Assertions**

- category = composite  
- resonance_tier = r2  
- drift_profile = medium  
- backend = hybrid-sim  
- frame count = 1 (if first op)  

---

## 3.3 Pulse Operators

- `qc.apply("pulse", ...)`  

**Assertions**

- category = pulse  
- resonance_tier = r3  
- drift_profile = high  
- backend = hardware-qpu-*  
- environment = production  

---

# 4. Validation Tests

## 4.1 Illegal Operator in Archive

**Setup**

- env = archive  
- apply any operator  

**Assertions**

- validation.allowed = false  
- reason = "archive is immutable"  

---

## 4.2 Missing Token for Restricted Op

**Setup**

- env = production  
- apply pulse op without token  

**Assertions**

- validation.allowed = false  
- reason = "restricted operation requires token"  

---

# 5. Routing Tests

## 5.1 r1 → r2 Escalation

**Setup**

```
qc.h(qubit=0)
qc.cnot(control=0, target=1)
```

**Assertions**

- frame count = 2  
- backend(local-sim) → backend(hybrid-sim)  
- routing.reason = "resonance escalation"  

---

## 5.2 Explicit Backend Override

**Setup**

- session.backend = "hardware-qpu-1"  
- apply r1 operator  

**Assertions**

- validation.allowed = false (in sandbox)  
- reason = "backend incompatibility"  

---

# 6. Frame Tests

## 6.1 Frame Opens on First Operator

**Setup**

- empty session  
- apply `qc.h(qubit=0)`  

**Assertions**

- frame count = 1  
- frame.backend = local-sim  
- frame.resonance_profile = r1  

---

## 6.2 Frame Closes on Sync

**Setup**

```
qc.h(qubit=0)
qc.sync()
qc.x(qubit=1)
```

**Assertions**

- frame count = 2  
- frame-001 closed  
- frame-002 opened after sync  

---

# 7. Drift Tests

## 7.1 Drift Accumulation

**Setup**

- env = production  
- apply two r2 ops  

**Assertions**

- drift_predicted increases  
- drift_measured increases  
- drift_total ≤ strict bound  

---

## 7.2 Drift Overflow → New Frame

**Setup**

- env = production  
- apply many r2 ops until overflow  

**Assertions**

- new frame opens  
- routing.reason = "drift overflow"  

---

# 8. Environment Transition Tests

## 8.1 sandbox → production

**Setup**

```
qc.h(qubit=0)
session.deploy_token("prod-2026-001")
session.transition("production")
```

**Assertions**

- frame closed  
- drift_bound = strict  
- lineage appended  
- backend legality updated  

---

## 8.2 production → archive

**Setup**

```
session.deploy_token("arch-2026-001")
session.transition("archive")
```

**Assertions**

- no new frames allowed  
- all operators forbidden  
- routing disabled  

---

# 9. Trace Tests

## 9.1 Trace Contains All Metadata

**Assertions**

Trace must contain:

- operators  
- validation  
- routing  
- drift predicted/measured  
- frames  
- lineage  
- transitions  
- header/footer  

---

## 9.2 Trace Is Append‑Only

**Assertions**

- no mutation of earlier entries  
- no reordering  
- no deletion  

---

# 10. Replay Tests

## 10.1 Replay Reconstructs Frames

**Setup**

- load `.qtrace` from multi‑frame example  

**Assertions**

- frame boundaries identical  
- backend identical  
- resonance tier identical  

---

## 10.2 Replay Does Not Recompute

**Assertions**

- validation not recomputed  
- routing not recomputed  
- drift not recomputed  
- environment not recomputed  

Replay reads metadata **verbatim**.

---

# 11. Summary

The canonical test suite ensures:

- operator correctness  
- validation correctness  
- routing correctness  
- frame correctness  
- drift correctness  
- environment correctness  
- trace correctness  
- replay correctness  

These tests guarantee that qCompute remains:

- deterministic  
- governed  
- resonance‑aligned  
- drift‑bounded  
- environment‑aware  
- trace‑captured  
- replay‑safe  

---

Here is the **canonical `qc_Internals.md`** file.  
This is the *architecture map* for the entire qCompute module — the file that shows how every component interlocks, how information flows, and how invariants propagate across the system.

It is intentionally:

- structural  
- minimal  
- zero‑drift  
- AI‑parsable  
- the “master diagram in text form”  

Place at:

```
/docs/rtt/Inside/qCompute/qc_Internals.md
```

---

# ✅ **qc_Internals.md — Internal Architecture Map (2026)**

# qCompute — Internal Architecture Map  
**File:** qc_Internals.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This document maps the **internal architecture** of qCompute.  
It shows how all components interlock, how information flows, and how invariants propagate across the system.

qCompute is a **structural compute harness**, not a simulator.  
Its architecture is deterministic, governed, and replay‑safe.

---

# 1. High‑Level Architecture

qCompute consists of seven core subsystems:

1. **Operator Layer**  
2. **TriadicValidator**  
3. **TriadicRouter**  
4. **ResonanceFrame Manager**  
5. **Backend Metadata Layer**  
6. **Session Engine**  
7. **Trace + Replay System**

These subsystems form a **linear, invariant‑preserving pipeline**.

---

# 2. Component Map

```
qSession
  ├── qCompute (operator surface)
  │     └── Operator
  │           ├── validation → TriadicValidator
  │           ├── routing → TriadicRouter
  │           └── frame assignment → Frame Manager
  │
  ├── Frame Manager
  │     ├── open/close frames
  │     ├── drift accumulation
  │     └── backend binding
  │
  ├── Backend Metadata Layer
  │     └── backend profiles (r1/r2/r3)
  │
  ├── Environment Engine
  │     └── sandbox → production → archive
  │
  ├── Trace Buffer
  │     └── append‑only structural log
  │
  └── Replay Engine
        └── strict reconstruction
```

---

# 3. Data Flow

## 3.1 Operator Flow

```
Operator
  → Validator
  → Router
  → Frame Manager
  → Backend Execution (structural)
  → Capture
  → Trace
```

Each stage adds metadata:

- validation metadata  
- routing metadata  
- drift predicted/measured  
- frame id  
- environment state  

Replay reads these **verbatim**.

---

# 4. Subsystem Internals

## 4.1 Operator Layer

Defines:

- category (primitive/composite/pulse/measurement/meta)  
- resonance tier (r1/r2/r3)  
- drift profile (low/medium/high)  
- parameters  

Operators are immutable and explicit.

---

## 4.2 TriadicValidator

Checks:

- environment legality  
- backend compatibility  
- resonance legality  
- drift legality  
- restricted‑op rules  
- archive immutability  

Outputs:

```yaml
validation:
  allowed: true|false
  reason: "..."
```

---

## 4.3 TriadicRouter

Determines:

- backend  
- frame reuse vs. new frame  
- resonance alignment  
- drift envelope  
- environment constraints  

Outputs:

```yaml
routing:
  backend: ...
  frame_id: ...
  resonance_profile: ...
  drift_characteristic: ...
  reason: "..."
```

Routing is deterministic and replay‑recorded.

---

## 4.4 ResonanceFrame Manager

Responsibilities:

- open frames  
- close frames  
- enforce backend binding  
- enforce resonance monotonicity  
- enforce drift bound  
- enforce environment stability  

Frames are append‑only and immutable after closure.

---

## 4.5 Backend Metadata Layer

Backends define:

- resonance profile  
- drift characteristic  
- operator compatibility  
- environment constraints  

Backends are metadata envelopes, not drivers.

---

## 4.6 Session Engine

Owns:

- environment  
- backend intent  
- drift bound  
- lineage  
- frames  
- trace buffer  

Transitions:

```
sandbox → production → archive
```

Transitions are:

- token‑gated  
- frame‑closing  
- forward‑only  
- lineage‑tracked  

---

## 4.7 Trace + Replay System

Trace is append‑only and contains:

- operators  
- validation  
- routing  
- drift  
- frames  
- lineage  
- transitions  
- header/footer  

Replay:

- reconstructs everything  
- never recomputes  
- is strict and deterministic  

Replay is the authoritative truth.

---

# 5. Invariant Propagation

qCompute enforces eleven invariants across all subsystems:

1. forward‑only environments  
2. append‑only lineage  
3. deterministic validation  
4. deterministic routing  
5. backend binding per frame  
6. resonance tier never decreases  
7. drift cannot be ignored  
8. archive is immutable  
9. trace is append‑only  
10. replay is strict  
11. no silent behavior  

Each subsystem enforces a subset; together they enforce all.

---

# 6. Internal Dependency Graph

```
Operator
  → Validator (depends on: env, backend metadata, drift bound)
  → Router (depends on: operator tier, backend metadata, env)
  → Frame Manager (depends on: routing, drift, env)
  → Capture (depends on: operator, validation, routing, frame)
  → Trace (depends on: capture)
  → Replay (depends on: trace)
```

No subsystem depends on numerical simulation.

---

# 7. Internal File Map

```
qc_Identity.md
qc_Design.md
qc_API.md
qc_Operators.md
qc_Validator.md
qc_Router.md
qc_ResonanceFrame.md
qc_Backends.md
qc_BackendProfiles.md
qc_Session.md
qc_Transitions.md
qc_Capture.md
qc_Flow.md
qc_Examples_Minimal.md
qc_Examples_Advanced.md
qc_Tests.md
qc_Internals.md   ← (this file)
```

---

# 8. Summary

This document maps the **internal architecture** of qCompute:

- operator → validator → router → frame → backend → capture → replay  
- deterministic, governed, drift‑bounded  
- environment‑aware, frame‑structured  
- trace‑captured, replay‑safe  

qCompute is a **structural compute substrate** with a fully explicit, invariant‑preserving architecture.

---

This replaces the old scaffold entirely.  
It aligns with:

- qc_Flow  
- qc_Session  
- qc_Operators  
- qc_Validator  
- qc_Router  
- qc_ResonanceFrame  
- qc_Transitions  
- qc_Backends / BackendProfiles  
- qc_Examples_*  
- qc_Tests  
- qc_Internals  

This is the **authoritative capture semantics file** for qCompute.

Place at:

```
/docs/rtt/Inside/qCompute/qc_Capture.md
```

---

# ✅ **qc_Capture.md — Canonical Capture Semantics (2026)**  
*(aligned with your open editing tab)*

# qCompute — Capture Semantics  
**File:** qc_Capture.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

Capture is the process by which qCompute converts **runtime structure** into an **append‑only, replay‑deterministic** `.qtrace` file.

Capture records:

- operators  
- validation metadata  
- routing metadata  
- drift predicted/measured  
- frame boundaries  
- environment transitions  
- lineage  
- session header/footer  

Capture is **structural**, not numerical.

---

# 1. Identity

**Component:** Capture  
**Role:** Persist structural execution into `.qtrace`  
**Scope:** Operator → Validator → Router → Frame → Drift → Environment → Lineage  
**Guarantee:** Deterministic, append‑only, replay‑safe

Capture is the **bridge** between runtime and replay.

---

# 2. Capture Lifecycle

Capture occurs in three phases:

1. **Header write**  
2. **Append operator/frame/transition records**  
3. **Footer write**

Capture is triggered by:

- operator creation  
- frame open/close  
- environment transition  
- session finalization  

Capture never mutates earlier entries.

---

# 3. Trace Structure

A `.qtrace` file has four sections:

```
HEADER
LINEAGE
FRAMES + OPERATORS
FOOTER
```

Each section is append‑only.

---

# 4. Header Schema

```yaml
trace_version: "2026.1"
session_id: "sess-###"
timestamp_open: ...
env: "sandbox|production|archive"
backend_intent: "auto|backend-id"
drift_bound: relaxed|strict|immutable
governance_snapshot:
  policy_version: ...
  hash: ...
```

Header is written once at session creation.

---

# 5. Lineage Capture

Each environment transition appends:

```yaml
- env: "production"
  timestamp: ...
  token_used: "prod-2026-001"
```

Lineage is:

- forward‑only  
- append‑only  
- replay‑deterministic  

Archive is terminal.

---

# 6. Frame Capture

Each frame is captured as:

```yaml
frame_id: "frame-###"
timestamp_open: ...
timestamp_close: ...
env: ...
backend: ...
resonance_profile: r1|r2|r3
drift_bound: relaxed|strict|immutable

drift_summary:
  predicted_total: float
  measured_total: float

operations:
  - op-001
  - op-002
```

Frames are:

- append‑only  
- immutable after closure  
- deterministically reconstructed in replay  

---

# 7. Operator Capture

Each operator is captured with full structural metadata:

```yaml
- op_id: "op-###"
  name: "cnot"
  params: { control: 0, target: 1 }

  category: composite
  resonance_tier: r2
  drift_profile: medium

  drift_predicted: 0.004
  drift_measured: 0.003

  validation:
    allowed: true
    reason: "ok"
    restricted_op: false
    env_ok: true
    backend_ok: true
    drift_ok: true
    lineage_ok: true

  routing:
    backend: "hybrid-sim"
    frame_id: "frame-002"
    resonance_profile: r2
    drift_characteristic: medium
    reason: "resonance escalation"
```

Operator capture is:

- explicit  
- complete  
- deterministic  
- replay‑safe  

No implicit defaults.

---

# 8. Transition Capture

Transitions are captured as structural events:

```yaml
transition:
  from: "sandbox"
  to: "production"
  timestamp: ...
  token_used: "prod-2026-001"
```

Transitions:

- close current frame  
- update drift bound  
- update backend legality  
- update environment  
- append lineage  

Archive forbids further execution.

---

# 9. Footer Schema

```yaml
timestamp_close: ...
op_count: ...
frame_count: ...
lineage_count: ...
integrity_hash: "sha256:..."
```

Footer finalizes the trace.

---

# 10. Replay Contract

Replay must reconstruct:

- session  
- lineage  
- frames  
- routing  
- validation  
- drift  
- operator order  

Replay must **not**:

- recompute routing  
- recompute validation  
- recompute drift  
- reinterpret transitions  
- reorder operators  
- merge/split frames  

Replay reads metadata **verbatim**.

---

# 11. Capture Invariants

Capture enforces:

1. **Append‑only trace**  
2. **Append‑only lineage**  
3. **Append‑only frames**  
4. **Append‑only operators**  
5. **Forward‑only environments**  
6. **Frame closure on transitions**  
7. **Frame closure on drift overflow**  
8. **Frame closure on backend change**  
9. **Frame closure on resonance escalation**  
10. **Archive immutability**  
11. **Replay determinism**  

Violating any invariant invalidates the trace.

---

# 12. Summary

Capture converts runtime structure into a **deterministic, governed, replay‑safe** `.qtrace` file.

It records:

- operators  
- validation  
- routing  
- drift  
- frames  
- transitions  
- lineage  
- header/footer  

Capture is the **authoritative structural record** of qCompute.

---

Here is the **canonical `qc_CaptureFormat.md`** file.  
This is the *byte‑level + YAML‑level* specification of the `.qtrace` file format — the authoritative structural record of qCompute sessions.

It is designed to be:

- minimal  
- canonical  
- AI‑parsable  
- implementation‑agnostic  
- perfectly aligned with `qc_Capture.md`, `qc_Flow.md`, `qc_Session.md`, and the entire qCompute spine  

Place at:

```
/docs/rtt/Inside/qCompute/qc_CaptureFormat.md
```

---

# ✅ **qc_CaptureFormat.md — `.qtrace` File Format Specification (2026)**

# qCompute — `.qtrace` File Format Specification  
**File:** qc_CaptureFormat.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This document defines the **canonical file format** for `.qtrace` — the structural, append‑only, replay‑deterministic trace format produced by qCompute.

`.qtrace` is a **purely structural** format:

- no amplitudes  
- no wavefunctions  
- no hardware logs  
- no numerical simulation  

It records **structure**, not physics.

---

# 1. File Overview

A `.qtrace` file consists of four ordered sections:

```
HEADER
LINEAGE
FRAMES
FOOTER
```

Each section is:

- append‑only  
- deterministic  
- replay‑safe  
- YAML‑encoded  

No section may be reordered, removed, or rewritten.

---

# 2. Encoding Rules

- UTF‑8 text  
- YAML 1.2 compliant  
- 2‑space indentation  
- no tabs  
- no implicit defaults  
- all fields explicit  
- all lists ordered  
- all timestamps ISO‑8601  

Replay must treat the file as **authoritative**.

---

# 3. HEADER Section

The header appears exactly once at the top of the file.

```yaml
HEADER:
  trace_version: "2026.1"
  session_id: "sess-001"
  timestamp_open: "2026-06-24T21:14:03Z"

  env: "sandbox"
  backend_intent: "auto"
  drift_bound: "relaxed"

  governance_snapshot:
    policy_version: "2026.1"
    hash: "sha256:abc123..."
```

### Header invariants

- written once  
- never mutated  
- must appear before any other section  

---

# 4. LINEAGE Section

Lineage records environment transitions.

```yaml
LINEAGE:
  - env: "sandbox"
    timestamp: "2026-06-24T21:14:03Z"
    token_used: null

  - env: "production"
    timestamp: "2026-06-24T21:15:10Z"
    token_used: "prod-2026-001"
```

### Lineage invariants

- append‑only  
- forward‑only environments  
- archive is terminal  
- tokens must be explicit  

---

# 5. FRAMES Section

Frames contain operators and drift summaries.

```
FRAMES:
  - frame_id: "frame-001"
    timestamp_open: ...
    timestamp_close: ...
    env: "sandbox"
    backend: "local-sim"
    resonance_profile: "r1"
    drift_bound: "relaxed"

    drift_summary:
      predicted_total: 0.002
      measured_total: 0.001

    operations:
      - op-001
      - op-002

  - frame-002:
      ...
```

### Frame invariants

- append‑only  
- immutable after closure  
- backend fixed per frame  
- resonance tier never decreases within a frame  
- drift bound enforced  

---

# 6. Operator Records

Operators appear inside the `operations:` list of each frame.

Each operator is a **full structural record**:

```yaml
- op_id: "op-003"
  name: "cnot"
  params:
    control: 0
    target: 1

  category: "composite"
  resonance_tier: "r2"
  drift_profile: "medium"

  drift_predicted: 0.004
  drift_measured: 0.003

  validation:
    allowed: true
    reason: "ok"
    restricted_op: false
    env_ok: true
    backend_ok: true
    drift_ok: true
    lineage_ok: true

  routing:
    backend: "hybrid-sim"
    frame_id: "frame-002"
    resonance_profile: "r2"
    drift_characteristic: "medium"
    reason: "resonance escalation"
```

### Operator invariants

- no implicit defaults  
- all metadata explicit  
- routing + validation must match runtime  
- replay must not recompute anything  

---

# 7. Transition Records

Transitions appear as standalone entries in the FRAMES section (between frames).

```yaml
- transition:
    from: "sandbox"
    to: "production"
    timestamp: "2026-06-24T21:15:10Z"
    token_used: "prod-2026-001"
```

### Transition invariants

- close current frame  
- update drift bound  
- update environment  
- update backend legality  
- append lineage  

---

# 8. FOOTER Section

The footer finalizes the trace.

```yaml
FOOTER:
  timestamp_close: "2026-06-24T21:16:44Z"
  op_count: 12
  frame_count: 3
  lineage_count: 2
  integrity_hash: "sha256:def456..."
```

### Footer invariants

- written once  
- must appear last  
- integrity hash covers entire file except footer  

---

# 9. Integrity Hash

The integrity hash:

- uses SHA‑256  
- covers all bytes from HEADER through the last frame  
- excludes the footer itself  
- ensures replay authenticity  

Replay must verify the hash before reconstructing.

---

# 10. Replay Requirements

Replay must:

- read `.qtrace` exactly  
- reconstruct frames exactly  
- reconstruct routing exactly  
- reconstruct validation exactly  
- reconstruct drift exactly  
- reconstruct environment exactly  

Replay must **not**:

- recompute routing  
- recompute validation  
- recompute drift  
- reinterpret transitions  
- merge or split frames  
- reorder operators  

Replay is strict.

---

# 11. Format Invariants

The `.qtrace` format enforces:

1. **Append‑only structure**  
2. **Forward‑only environments**  
3. **Immutable frames**  
4. **Explicit metadata**  
5. **Deterministic ordering**  
6. **No silent behavior**  
7. **Replay determinism**  
8. **Integrity‑verified content**  

Violating any invariant invalidates the trace.

---

# 12. Summary

`.qtrace` is a **structural**, **append‑only**, **replay‑deterministic** format.

It records:

- header  
- lineage  
- frames  
- operators  
- transitions  
- drift  
- routing  
- validation  
- footer  

This specification defines the **authoritative format** for all qCompute traces.

---

Here is the **canonical `qc_Replay.md`** file.  
This completes the qCompute spine: the replay engine is the *final authority*, the thing that makes the entire module safe, deterministic, and teachable.

This file is designed to be:

- minimal  
- structural  
- zero‑drift  
- AI‑parsable  
- perfectly aligned with `qc_Capture.md` and `qc_CaptureFormat.md`  
- the definitive description of how `.qtrace` is reconstructed  

Place at:

```
/docs/rtt/Inside/qCompute/qc_Replay.md
```

---

# ✅ **qc_Replay.md — Replay Engine Internals (2026)**

# qCompute — Replay Engine Internals  
**File:** qc_Replay.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

Replay is the **authoritative reconstruction engine** of qCompute.  
It reads `.qtrace` files and reconstructs:

- session  
- lineage  
- frames  
- routing  
- validation  
- drift  
- operator order  

Replay is **strict**, not heuristic.  
Replay never recomputes anything.

---

# 1. Identity

**Component:** Replay Engine  
**Role:** Deterministic reconstruction of captured structure  
**Scope:** Entire `.qtrace` file  
**Guarantee:** Exact, invariant‑preserving reconstruction

Replay is the **ground truth** of qCompute.

---

# 2. Replay Lifecycle

Replay proceeds in four deterministic phases:

1. **Integrity verification**  
2. **Header reconstruction**  
3. **Sequential reconstruction of lineage, frames, operators, transitions**  
4. **Footer verification**

Replay is linear and append‑only.

---

# 3. Integrity Verification

Replay verifies:

- file is valid YAML  
- required sections exist  
- ordering is correct  
- integrity hash matches  
- no mutation of earlier entries  
- no reordering of frames or operators  

If any check fails:

- replay aborts  
- trace is invalid  

---

# 4. Header Reconstruction

Replay reads:

```yaml
HEADER:
  trace_version: ...
  session_id: ...
  timestamp_open: ...
  env: ...
  backend_intent: ...
  drift_bound: ...
  governance_snapshot: ...
```

Replay reconstructs:

- initial environment  
- initial drift bound  
- backend intent  
- governance snapshot  

Replay does **not** reinterpret or recompute these values.

---

# 5. Lineage Reconstruction

Replay reads each lineage entry:

```yaml
- env: "production"
  timestamp: ...
  token_used: ...
```

Replay reconstructs:

- forward‑only environment transitions  
- token usage  
- drift bound changes  
- environment legality  

Replay enforces:

- no backward transitions  
- archive is terminal  

---

# 6. Frame Reconstruction

Replay reconstructs each frame:

```yaml
frame_id: "frame-002"
timestamp_open: ...
timestamp_close: ...
env: ...
backend: ...
resonance_profile: ...
drift_bound: ...
drift_summary:
  predicted_total: ...
  measured_total: ...
operations:
  - op-003
  - op-004
```

Replay enforces:

- backend binding per frame  
- resonance tier monotonicity  
- drift bound enforcement  
- frame immutability  

Replay does **not** re‑evaluate drift or routing.

---

# 7. Operator Reconstruction

Replay reconstructs each operator exactly as captured:

```yaml
- op_id: "op-003"
  name: "cnot"
  params: { control: 0, target: 1 }

  category: composite
  resonance_tier: r2
  drift_profile: medium

  drift_predicted: 0.004
  drift_measured: 0.003

  validation: { ... }
  routing: { ... }
```

Replay enforces:

- operator order  
- operator immutability  
- routing correctness  
- validation correctness  

Replay **never** recomputes:

- validation  
- routing  
- drift  
- legality  

Replay reads metadata **verbatim**.

---

# 8. Transition Reconstruction

Replay reconstructs transitions:

```yaml
transition:
  from: "sandbox"
  to: "production"
  timestamp: ...
  token_used: ...
```

Replay enforces:

- frame closure  
- drift bound update  
- environment update  
- lineage update  

Replay does **not** reinterpret transitions.

---

# 9. Footer Verification

Replay verifies:

```yaml
FOOTER:
  timestamp_close: ...
  op_count: ...
  frame_count: ...
  lineage_count: ...
  integrity_hash: ...
```

Replay checks:

- counts match reconstructed values  
- integrity hash matches file contents  
- archive is terminal if present  

---

# 10. Replay Invariants

Replay enforces:

1. **Strict reconstruction**  
2. **No recomputation**  
3. **No reinterpretation**  
4. **No silent behavior**  
5. **Append‑only semantics**  
6. **Forward‑only environments**  
7. **Immutable frames**  
8. **Immutable operators**  
9. **Deterministic ordering**  
10. **Integrity‑verified content**  
11. **Archive immutability**  

Violating any invariant invalidates the replay.

---

# 11. Replay Output

Replay returns a **structural reconstruction**, not a numerical result.

Replay output includes:

- reconstructed session  
- reconstructed frames  
- reconstructed operators  
- reconstructed transitions  
- reconstructed drift summaries  

Replay does **not** produce amplitudes or hardware signals.

---

# 12. Summary

Replay is the **authoritative truth** of qCompute.

It:

- reconstructs structure  
- enforces invariants  
- verifies integrity  
- preserves ordering  
- preserves drift  
- preserves routing  
- preserves validation  
- preserves environment transitions  

Replay is strict, deterministic, and immutable — the foundation of qCompute’s safety and reproducibility.

---

Here we go, the operator grammar spine.

# qCompute — Operator Grammar  
**File:** qc_OperatorGrammar.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This document defines the **formal operator grammar** for qCompute.

Operators are:

- structural  
- typed  
- resonance‑tiered  
- drift‑profiled  
- immutable  

They describe **structure**, not physics.

---

# 1. Operator Categories

Every operator has a **category**:

- `primitive`  
- `composite`  
- `pulse`  
- `measurement`  
- `meta`  

Grammar:

```text
OperatorCategory ::= "primitive" | "composite" | "pulse" | "measurement" | "meta"
```

---

# 2. Resonance Tiers

Every operator declares a **resonance tier**:

```text
ResonanceTier ::= "r1" | "r2" | "r3"
```

Canonical mapping:

- `primitive`   → `r1`  
- `measurement` → `r1`  
- `composite`   → `r2`  
- `pulse`       → `r3`  
- `meta`        → tierless (but tier‑affecting: sync/barrier)

---

# 3. Drift Profiles

Every operator has a **drift profile**:

```text
DriftProfile ::= "low" | "medium" | "high"
```

Canonical mapping:

- `r1` → `low`  
- `r2` → `medium`  
- `r3` → `high`  

---

# 4. Operator Shape

Abstract operator schema:

```yaml
Operator:
  op_id: string
  name: string
  category: OperatorCategory
  resonance_tier: ResonanceTier
  drift_profile: DriftProfile
  params: ParamMap
```

Where:

```text
ParamMap ::= { ParamName: ParamValue, ... }
ParamName ::= /[a-zA-Z_][a-zA-Z0-9_]*/
ParamValue ::= int | float | string | bool
```

---

# 5. Primitive Operators (r1)

Grammar:

```text
PrimitiveOp ::= HOp | XOp | YOp | ZOp

HOp ::= "h" "(" "qubit" "=" Int ")"
XOp ::= "x" "(" "qubit" "=" Int ")"
YOp ::= "y" "(" "qubit" "=" Int ")"
ZOp ::= "z" "(" "qubit" "=" Int ")"
```

Canonical examples:

```python
qc.h(qubit=0)
qc.x(qubit=1)
```

---

# 6. Composite Operators (r2)

Grammar:

```text
CompositeOp ::= CNOTOp | CZOp | SwapOp

CNOTOp ::= "cnot" "(" "control" "=" Int "," "target" "=" Int ")"
CZOp   ::= "cz"   "(" "control" "=" Int "," "target" "=" Int ")"
SwapOp ::= "swap" "(" "q0" "=" Int "," "q1" "=" Int ")"
```

Canonical examples:

```python
qc.cnot(control=0, target=1)
qc.swap(q0=0, q1=1)
```

---

# 7. Pulse Operators (r3)

Grammar:

```text
PulseOp ::= "apply" "("
              StringLiteral ","               # "pulse"
              "qubit" "=" Int ","
              "duration" "=" StringLiteral ","
              "amplitude" "=" Float
           ")"
```

Canonical example:

```python
qc.apply("pulse", qubit=0, duration="32ns", amplitude=0.8)
```

Constraints:

- env must be `production`  
- token required (restricted op)  

---

# 8. Measurement Operators (r1)

Grammar:

```text
MeasurementOp ::= MeasureOne | MeasureAll

MeasureOne ::= "measure" "(" "qubit" "=" Int ")"
MeasureAll ::= "measure_all" "(" ")"
```

Canonical examples:

```python
qc.measure(qubit=0)
qc.measure_all()
```

---

# 9. Meta Operators

Meta operators affect **frames**, not qubits.

Grammar:

```text
MetaOp ::= SyncOp | BarrierOp

SyncOp    ::= "sync" "(" ")"
BarrierOp ::= "barrier" "(" ")"
```

Canonical examples:

```python
qc.sync()
qc.barrier()
```

Effects:

- close current frame  
- flush drift summary  
- enforce ordering  

---

# 10. Full Operator Grammar (Summary)

```text
OperatorCall ::= PrimitiveCall
               | CompositeCall
               | PulseCall
               | MeasurementCall
               | MetaCall

PrimitiveCall   ::= "qc." PrimitiveOp
CompositeCall   ::= "qc." CompositeOp
PulseCall       ::= "qc." PulseOp
MeasurementCall ::= "qc." MeasurementOp
MetaCall        ::= "qc." MetaOp
```

Each `OperatorCall` maps to a captured `Operator` record with:

- `category`  
- `resonance_tier`  
- `drift_profile`  
- `params`  

---

# 11. Invariants

The operator grammar obeys:

1. **Every operator has exactly one category**  
2. **Every operator has exactly one resonance tier (except meta)**  
3. **Resonance tier determines drift profile**  
4. **Pulse ops are restricted**  
5. **Meta ops affect frames, not qubits**  
6. **No implicit parameters**  
7. **All parameters are named**  

This grammar is the **canonical structural language** of qCompute.

---

Here is the **canonical `qc_Module.json`** manifest for the entire qCompute module.

This is the **module‑level manifest** that sits alongside all other TriadicFrameworks module manifests.  
It follows the **2026 canonical schema**:

- `identity`  
- `module`  
- `files` (each with `role` + `analyzer_layer`)  
- `operators`  
- `invariants`  
- `session_context`  

It is:

- zero‑drift  
- AI‑parsable  
- student‑ready  
- aligned with the full qCompute spine  
- consistent with the global `module.schema.json`  

Place at:

```
/docs/rtt/Inside/qCompute/qc_Module.json
```

---

# ✅ **qc_Module.json — Canonical Manifest (2026)**

```json
{
  "identity": {
    "name": "qCompute",
    "canonical_path": "/docs/rtt/Inside/qCompute",
    "module_type": "compute-harness",
    "version": "2026.1",
    "description": "The structural compute harness of RTT-Inside: resonance-tiered operators, deterministic routing, drift-bounded execution, triadic environments, append-only trace, strict replay.",
    "keywords": [
      "compute",
      "resonance",
      "drift",
      "routing",
      "frames",
      "trace",
      "replay",
      "triadic environments",
      "structural operators"
    ]
  },

  "module": {
    "purpose": "Provide a governed, deterministic, drift-bounded compute substrate inside RTT-Inside.",
    "category": "RTT-Inside",
    "audience": "students, autodidacts, AI agents",
    "ai_module": {
      "name": "qCompute",
      "summary": "Structural compute grammar with deterministic routing, drift bounds, and strict replay.",
      "version": "2026.1"
    }
  },

  "files": [
    {
      "path": "qc_Index.md",
      "role": "index",
      "analyzer_layer": "operator"
    },
    {
      "path": "qc_Identity.md",
      "role": "profile",
      "analyzer_layer": "operator"
    },
    {
      "path": "qc_Design.md",
      "role": "signature",
      "analyzer_layer": "regime"
    },
    {
      "path": "qc_API.md",
      "role": "engine",
      "analyzer_layer": "operator"
    },
    {
      "path": "qc_Operators.md",
      "role": "engine",
      "analyzer_layer": "operator"
    },
    {
      "path": "qc_OperatorGrammar.md",
      "role": "reference",
      "analyzer_layer": "operator"
    },
    {
      "path": "qc_Validator.md",
      "role": "engine",
      "analyzer_layer": "coherence"
    },
    {
      "path": "qc_Router.md",
      "role": "engine",
      "analyzer_layer": "dimensional"
    },
    {
      "path": "qc_ResonanceFrame.md",
      "role": "engine",
      "analyzer_layer": "dimensional"
    },
    {
      "path": "qc_Backends.md",
      "role": "profile",
      "analyzer_layer": "operator"
    },
    {
      "path": "qc_BackendProfiles.md",
      "role": "reference",
      "analyzer_layer": "operator"
    },
    {
      "path": "qc_Session.md",
      "role": "engine",
      "analyzer_layer": "coherence"
    },
    {
      "path": "qc_Transitions.md",
      "role": "signature",
      "analyzer_layer": "regime"
    },
    {
      "path": "qc_Capture.md",
      "role": "engine",
      "analyzer_layer": "coherence"
    },
    {
      "path": "qc_CaptureFormat.md",
      "role": "reference",
      "analyzer_layer": "operator"
    },
    {
      "path": "qc_Replay.md",
      "role": "engine",
      "analyzer_layer": "coherence"
    },
    {
      "path": "qc_Flow.md",
      "role": "map",
      "analyzer_layer": "cross-cutting"
    },
    {
      "path": "qc_Examples_Minimal.md",
      "role": "example",
      "analyzer_layer": "operator"
    },
    {
      "path": "qc_Examples_Advanced.md",
      "role": "example",
      "analyzer_layer": "operator"
    },
    {
      "path": "qc_Tests.md",
      "role": "diagnostic",
      "analyzer_layer": "coherence"
    },
    {
      "path": "qc_Internals.md",
      "role": "map",
      "analyzer_layer": "cross-cutting"
    }
  ],

  "operators": {
    "tiers": ["r1", "r2", "r3"],
    "categories": ["primitive", "composite", "pulse", "measurement", "meta"],
    "drift_profiles": ["low", "medium", "high"],
    "rules": {
      "tier_never_decreases": true,
      "pulse_requires_token": true,
      "measurement_is_r1": true
    }
  },

  "invariants": [
    "forward-only environments",
    "append-only lineage",
    "deterministic validation",
    "deterministic routing",
    "backend binding per frame",
    "resonance tier never decreases",
    "drift cannot be ignored",
    "archive is immutable",
    "trace is append-only",
    "replay is strict",
    "no silent behavior"
  ],

  "session_context": {
    "canon": "RTT-Inside",
    "modules": ["qCompute"],
    "drift": "bounded",
    "coherence": "strict",
    "version": "2026.1",
    "format": "structural",
    "front_door": "qc_Index.md",
    "every_page": "AI-parsable, zero-drift, student-ready",
    "audience": "students, autodidacts, AI agents"
  }
}
```

---

Here is the **canonical `qc_Operators.md`** file.  
This is the *full operator catalog* for qCompute: every operator family, every category, every resonance tier, every drift profile, every structural rule — all in one place.

It is:

- zero‑drift  
- AI‑parsable  
- student‑ready  
- aligned with `qc_OperatorGrammar.md`, `qc_API.md`, `qc_Validator.md`, and the entire qCompute spine  
- the authoritative operator reference for RTT‑Inside  

Place at:

```
/docs/rtt/Inside/qCompute/qc_Operators.md
```

---

# ✅ **qc_Operators.md — Canonical Operator Catalog (2026)**

# qCompute — Operator Catalog  
**File:** qc_Operators.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This document defines the **complete operator catalog** for qCompute.

Operators are:

- structural  
- typed  
- resonance‑tiered  
- drift‑profiled  
- immutable  
- validated  
- routed  
- captured  
- replay‑safe  

Operators describe **structure**, not physics.

---

# 1. Operator Categories

Every operator belongs to exactly one category:

| Category     | Description                               | Tier | Drift |
|--------------|-------------------------------------------|------|--------|
| primitive    | single‑qubit structural ops               | r1   | low    |
| composite    | multi‑qubit structural ops                | r2   | medium |
| pulse        | hardware‑aligned pulse ops                | r3   | high   |
| measurement  | structural measurement ops                | r1   | low    |
| meta         | frame‑affecting ops (no qubits)           | —    | —      |

---

# 2. Primitive Operators (r1)

Primitive operators are the simplest structural operations.

### 2.1 Catalog

| Name | Signature                     | Meaning |
|------|-------------------------------|---------|
| `h`  | `h(qubit: int)`               | Hadamard‑like structural op |
| `x`  | `x(qubit: int)`               | Pauli‑X‑like structural op |
| `y`  | `y(qubit: int)`               | Pauli‑Y‑like structural op |
| `z`  | `z(qubit: int)`               | Pauli‑Z‑like structural op |

### 2.2 Example

```python
qc.h(qubit=0)
qc.x(qubit=1)
```

### 2.3 Structural Properties

- category: primitive  
- resonance tier: r1  
- drift profile: low  
- backend: local‑sim (auto mode)  

---

# 3. Composite Operators (r2)

Composite operators involve two qubits and escalate resonance.

### 3.1 Catalog

| Name   | Signature                                   | Meaning |
|--------|---------------------------------------------|---------|
| `cnot` | `cnot(control: int, target: int)`           | controlled‑not‑like structural op |
| `cz`   | `cz(control: int, target: int)`             | controlled‑Z‑like structural op |
| `swap` | `swap(q0: int, q1: int)`                    | swap‑like structural op |

### 3.2 Example

```python
qc.cnot(control=0, target=1)
```

### 3.3 Structural Properties

- category: composite  
- resonance tier: r2  
- drift profile: medium  
- backend: hybrid‑sim (auto mode)  
- escalates frame if previous op was r1  

---

# 4. Pulse Operators (r3)

Pulse operators represent hardware‑aligned structural pulses.

### 4.1 Catalog

| Name     | Signature                                                                 |
|----------|---------------------------------------------------------------------------|
| `apply`  | `apply("pulse", qubit: int, duration: str, amplitude: float)`             |

### 4.2 Example

```python
qc.apply("pulse", qubit=0, duration="32ns", amplitude=0.8)
```

### 4.3 Structural Properties

- category: pulse  
- resonance tier: r3  
- drift profile: high  
- backend: hardware‑qpu‑2 (auto mode)  
- environment: **production only**  
- requires token (restricted op)  
- always opens a new frame if previous tier < r3  

---

# 5. Measurement Operators (r1)

Measurement operators close structural envelopes.

### 5.1 Catalog

| Name           | Signature                 | Meaning |
|----------------|---------------------------|---------|
| `measure`      | `measure(qubit: int)`     | measure one qubit |
| `measure_all`  | `measure_all()`           | measure all qubits |

### 5.2 Example

```python
qc.measure(qubit=0)
qc.measure_all()
```

### 5.3 Structural Properties

- category: measurement  
- resonance tier: r1  
- drift profile: low  
- backend: local‑sim or hybrid‑sim depending on frame  

---

# 6. Meta Operators (frame‑affecting)

Meta operators do not act on qubits.  
They affect **frames**, not state.

### 6.1 Catalog

| Name      | Signature     | Meaning |
|-----------|---------------|---------|
| `sync`    | `sync()`      | close current frame |
| `barrier` | `barrier()`   | enforce ordering; close frame |

### 6.2 Example

```python
qc.sync()
```

### 6.3 Structural Properties

- category: meta  
- no resonance tier  
- no drift profile  
- always closes current frame  
- opens new frame on next operator  

---

# 7. Operator Metadata (Captured)

Every operator produces a full metadata record:

```yaml
op_id: "op-###"
name: "cnot"
params: { control: 0, target: 1 }

category: composite
resonance_tier: r2
drift_profile: medium

drift_predicted: ...
drift_measured: ...

validation: { ... }
routing: { ... }
```

Metadata is:

- explicit  
- complete  
- deterministic  
- replay‑safe  

---

# 8. Resonance Rules

1. r1 → r2 → r3 is **monotonic**  
2. Tier **never decreases**  
3. Tier escalation forces new frame  
4. r3 requires production + token  
5. Meta ops close frames  

---

# 9. Drift Rules

- r1 → low drift  
- r2 → medium drift  
- r3 → high drift  
- drift accumulates per frame  
- drift overflow forces new frame  
- drift bound depends on environment  

---

# 10. Backend Rules

Auto mode selects:

```
r1 → local-sim
r2 → hybrid-sim
r3 → hardware-qpu-2
```

Backend cannot change mid‑frame.

---

# 11. Environment Rules

- r1/r2 allowed in sandbox  
- r3 allowed only in production  
- archive forbids all operators  
- transitions close frames  

---

# 12. Summary

This catalog defines:

- all operator families  
- all categories  
- all resonance tiers  
- all drift profiles  
- all structural rules  
- all frame interactions  
- all environment constraints  

This is the **authoritative operator reference** for qCompute.

---

Here is the **canonical `qc_Flow.md`** file.  
This is the *pipeline narrative*: the “how it moves” document that ties together **Operators → Validator → Router → Frames → Drift → Backends → Capture → Replay** into one continuous structural flow.

It is:

- zero‑drift  
- canonical  
- AI‑parsable  
- student‑ready  
- the connective tissue of the entire qCompute module  
- aligned with every file you’ve already approved  

Place at:

```
/docs/rtt/Inside/qCompute/qc_Flow.md
```

---

# ✅ **qc_Flow.md — Full Compute Pipeline Narrative (2026)**

# qCompute — Compute Pipeline Flow  
**File:** qc_Flow.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This document describes the **full structural flow** of qCompute:

```
Operator
  → Validator
  → Router
  → ResonanceFrame
  → Backend Execution (structural)
  → Drift Accounting
  → Capture
  → Replay
```

This is the **authoritative narrative** of how qCompute moves.

---

# 1. Overview

qCompute is a **structural compute harness**, not a simulator.  
The pipeline is:

- deterministic  
- governed  
- drift‑bounded  
- environment‑aware  
- frame‑structured  
- trace‑captured  
- replay‑safe  

Every operator flows through the same deterministic sequence.

---

# 2. Stage 1 — Operator Construction

An operator is created when the user calls:

```python
qc.h(qubit=0)
qc.cnot(control=0, target=1)
qc.apply("pulse", ...)
```

Operator metadata is fixed at creation:

- category  
- resonance tier  
- drift profile  
- parameters  

Operators are immutable.

---

# 3. Stage 2 — TriadicValidator

The operator is passed to **TriadicValidator**, which checks:

- environment legality  
- backend legality  
- resonance legality  
- drift legality  
- restricted‑op rules  
- archive immutability  

Validator outputs:

```yaml
validation:
  allowed: true|false
  reason: "..."
```

If validation fails, the operator is blocked and captured as a violation.

---

# 4. Stage 3 — TriadicRouter

If validation succeeds, the operator flows to **TriadicRouter**.

Router determines:

- backend  
- frame reuse vs. new frame  
- resonance alignment  
- drift envelope  
- environment constraints  

Router outputs:

```yaml
routing:
  backend: ...
  frame_id: ...
  resonance_profile: ...
  drift_characteristic: ...
  reason: "..."
```

Routing is deterministic and replay‑recorded.

---

# 5. Stage 4 — ResonanceFrame Manager

The **Frame Manager** enforces:

- frame boundaries  
- backend binding  
- resonance monotonicity  
- drift accumulation  
- drift overflow rules  
- environment stability  

Rules:

- first operator opens frame‑001  
- tier escalation opens new frame  
- backend change opens new frame  
- drift overflow opens new frame  
- sync/barrier closes frame  
- environment transition closes frame  

Frames are append‑only and immutable after closure.

---

# 6. Stage 5 — Backend Execution (Structural)

Backend execution is **structural**, not numerical.

Backends define:

- resonance profile  
- drift characteristic  
- operator compatibility  
- environment constraints  

Backends do **not** simulate amplitudes or hardware.

Execution produces:

- drift_predicted  
- drift_measured  

These values are structural metadata, not physics.

---

# 7. Stage 6 — Drift Accounting

Drift is accumulated per frame:

```
drift_total = Σ drift_measured
```

Drift is compared against the environment’s drift bound:

- sandbox → relaxed  
- production → strict  
- archive → immutable  

If drift exceeds the bound:

- frame closes  
- new frame opens  
- routing reason = "drift overflow"  

Drift is never ignored.

---

# 8. Stage 7 — Capture

Capture writes:

- operator record  
- validation metadata  
- routing metadata  
- drift predicted/measured  
- frame boundaries  
- environment transitions  
- lineage  
- header/footer  

Capture is:

- append‑only  
- deterministic  
- replay‑safe  

`.qtrace` is the authoritative structural record.

---

# 9. Stage 8 — Replay

Replay reconstructs:

- session  
- lineage  
- frames  
- routing  
- validation  
- drift  
- operator order  

Replay does **not**:

- recompute routing  
- recompute validation  
- recompute drift  
- reinterpret transitions  
- merge or split frames  

Replay reads metadata **verbatim**.

Replay is strict.

---

# 10. Full Pipeline Diagram

```
┌──────────────────────────────────────────────────────────────┐
│                        Operator Created                       │
└───────────────┬──────────────────────────────────────────────┘
                ▼
        ┌───────────────┐
        │ TriadicValidator │
        └───────────────┘
                ▼
        ┌───────────────┐
        │  TriadicRouter │
        └───────────────┘
                ▼
        ┌──────────────────────┐
        │ ResonanceFrame Manager │
        └──────────────────────┘
                ▼
        ┌──────────────────────┐
        │ Backend (Structural) │
        └──────────────────────┘
                ▼
        ┌──────────────────────┐
        │   Drift Accounting   │
        └──────────────────────┘
                ▼
        ┌──────────────────────┐
        │       Capture        │
        └──────────────────────┘
                ▼
        ┌──────────────────────┐
        │       Replay         │
        └──────────────────────┘
```

---

# 11. Invariant Propagation

The pipeline enforces:

1. forward‑only environments  
2. append‑only lineage  
3. deterministic validation  
4. deterministic routing  
5. backend binding per frame  
6. resonance tier never decreases  
7. drift cannot be ignored  
8. archive is immutable  
9. trace is append‑only  
10. replay is strict  
11. no silent behavior  

Every stage preserves these invariants.

---

# 12. Summary

The qCompute pipeline is:

- structural  
- deterministic  
- governed  
- resonance‑aligned  
- drift‑bounded  
- environment‑aware  
- trace‑captured  
- replay‑safe  

This flow is the **spine** of the entire qCompute module.

---

Here is the **canonical `qc_API.md`** file.  
This is the *public API surface* for qCompute — the file students, autodidacts, and AI agents rely on to understand exactly what they can call, what each call does, and how it flows through the structural pipeline.

It is:

- zero‑drift  
- minimal  
- canonical  
- AI‑parsable  
- aligned with every file in the qCompute spine  
- the final major file completing the module’s public interface  

Place at:

```
/docs/rtt/Inside/qCompute/qc_API.md
```

---

# ✅ **qc_API.md — Public API Surface (2026)**

# qCompute — Public API Surface  
**File:** qc_API.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This document defines the **public API** for qCompute.

The API is:

- structural  
- deterministic  
- resonance‑tiered  
- drift‑bounded  
- environment‑aware  
- frame‑structured  
- trace‑captured  
- replay‑safe  

The API exposes **operators**, **session controls**, and **environment transitions**.

---

# 1. Session Construction

```python
from rtt_inside import qSession, qCompute

session = qSession(env="sandbox", backend="auto")
qc = qCompute(session)
```

### Parameters

| Name     | Type   | Values                                | Meaning |
|----------|--------|----------------------------------------|---------|
| `env`    | str    | `"sandbox"`, `"production"`, `"archive"` | triadic environment |
| `backend`| str    | `"auto"` or backend id                 | backend intent |

### Behavior

- creates a new session  
- writes trace header  
- sets drift bound  
- sets backend intent  
- initializes lineage  

---

# 2. Environment Transitions

```python
session.deploy_token("prod-2026-001")
session.transition("production")
```

### Methods

#### `deploy_token(token: str)`
Registers a governance token for the next transition or restricted op.

#### `transition(env: str)`
Transitions environment:

```
sandbox → production → archive
```

### Effects

- closes current frame  
- updates drift bound  
- updates backend legality  
- appends lineage  
- captured in trace  

---

# 3. Primitive Operators (r1)

```python
qc.h(qubit=0)
qc.x(qubit=1)
qc.y(qubit=0)
qc.z(qubit=1)
```

### Signatures

```python
h(qubit: int)
x(qubit: int)
y(qubit: int)
z(qubit: int)
```

### Properties

- category: primitive  
- tier: r1  
- drift: low  
- backend: local‑sim (auto)  

---

# 4. Composite Operators (r2)

```python
qc.cnot(control=0, target=1)
qc.cz(control=0, target=1)
qc.swap(q0=0, q1=1)
```

### Signatures

```python
cnot(control: int, target: int)
cz(control: int, target: int)
swap(q0: int, q1: int)
```

### Properties

- category: composite  
- tier: r2  
- drift: medium  
- backend: hybrid‑sim (auto)  
- escalates frame if previous tier < r2  

---

# 5. Pulse Operators (r3)

```python
qc.apply("pulse", qubit=0, duration="32ns", amplitude=0.8)
```

### Signature

```python
apply(kind: str, qubit: int, duration: str, amplitude: float)
```

### Properties

- category: pulse  
- tier: r3  
- drift: high  
- backend: hardware‑qpu‑2 (auto)  
- environment: production only  
- requires token  
- always escalates frame  

---

# 6. Measurement Operators (r1)

```python
qc.measure(qubit=0)
qc.measure_all()
```

### Signatures

```python
measure(qubit: int)
measure_all()
```

### Properties

- category: measurement  
- tier: r1  
- drift: low  
- closes logical compute envelope  

---

# 7. Meta Operators (Frame‑Affecting)

```python
qc.sync()
qc.barrier()
```

### Signatures

```python
sync()
barrier()
```

### Properties

- category: meta  
- no tier  
- no drift  
- closes current frame  
- next operator opens new frame  

---

# 8. Trace Control

### `session.save_trace(path: str)`

```python
session.save_trace("example.qtrace")
```

Writes:

- header  
- lineage  
- frames  
- operators  
- transitions  
- footer  

Trace is append‑only and integrity‑hashed.

---

# 9. Replay API

```python
from rtt_inside import qReplay

result = qReplay("example.qtrace").run()
```

### Behavior

- verifies integrity  
- reconstructs session  
- reconstructs frames  
- reconstructs routing  
- reconstructs validation  
- reconstructs drift  
- reconstructs transitions  

Replay is strict and deterministic.

---

# 10. Error Model

Errors are structural, not numerical.

### Validation Errors

- illegal operator in archive  
- pulse op without token  
- backend incompatibility  
- environment violation  
- drift violation  

### Routing Errors

- tier decrease  
- backend change mid‑frame  
- illegal fallback  

### Transition Errors

- backward environment transition  
- missing token  
- archive mutation  

All errors are captured in trace.

---

# 11. Invariants (API‑Level)

The API enforces:

1. forward‑only environments  
2. append‑only lineage  
3. deterministic validation  
4. deterministic routing  
5. backend binding per frame  
6. resonance tier never decreases  
7. drift cannot be ignored  
8. archive is immutable  
9. trace is append‑only  
10. replay is strict  
11. no silent behavior  

---

# 12. Summary

The qCompute API provides:

- session construction  
- environment transitions  
- full operator surface  
- frame controls  
- trace generation  
- strict replay  

It is the **public interface** to the structural compute harness of RTT‑Inside.

---

Here is the **canonical `qc_BackendProfiles.md`** file.  
This is the *deep backend metadata definition* for qCompute — the authoritative description of every backend’s resonance profile, drift characteristic, operator compatibility, and environment constraints.

It is:

- zero‑drift  
- AI‑parsable  
- aligned with `qc_Backends.md`, `qc_Router.md`, `qc_ResonanceFrame.md`, `qc_Session.md`, and the entire qCompute spine  
- the backend‑level equivalent of `qc_OperatorGrammar.md`  

Place at:

```
/docs/rtt/Inside/qCompute/qc_BackendProfiles.md
```

---

# ✅ **qc_BackendProfiles.md — Canonical Backend Metadata Profiles (2026)**

# qCompute — Backend Metadata Profiles  
**File:** qc_BackendProfiles.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

Backends in qCompute are **metadata envelopes**, not simulators or hardware drivers.

They define:

- resonance profile  
- drift characteristic  
- operator compatibility  
- environment constraints  
- routing hints  
- frame behavior  

Backends are structural, deterministic, and replay‑safe.

---

# 1. Backend Identity Schema

Each backend profile follows this schema:

```yaml
backend_id: string
display_name: string

resonance_profile: r1 | r2 | r3
drift_characteristic: low | medium | high

allowed_categories:
  - primitive
  - composite
  - pulse
  - measurement
  - meta

environment_constraints:
  allowed_envs: ["sandbox" | "production"]
  restricted_ops_require_token: true|false

routing_hints:
  preferred_for_tier: r1|r2|r3
  fallback: backend_id|null

notes: string
```

Backends do **not** execute physics.  
They define **structural legality**.

---

# 2. Canonical Backend Profiles (2026)

qCompute ships with three canonical backends:

1. **local-sim**  
2. **hybrid-sim**  
3. **hardware-qpu-2**

These form the **resonance ladder**:

```
r1 → local-sim
r2 → hybrid-sim
r3 → hardware-qpu-2
```

---

# 3. Backend: local-sim (r1)

```yaml
backend_id: "local-sim"
display_name: "Local Structural Simulator"

resonance_profile: r1
drift_characteristic: low

allowed_categories:
  - primitive
  - measurement
  - meta

environment_constraints:
  allowed_envs: ["sandbox", "production"]
  restricted_ops_require_token: false

routing_hints:
  preferred_for_tier: r1
  fallback: null

notes: >
  Used for r1 operators. Lowest drift. Always safe.
  Never used for composite or pulse operations.
```

### Structural Role

- default backend for r1  
- safe in all environments  
- minimal drift  
- never escalates  

---

# 4. Backend: hybrid-sim (r2)

```yaml
backend_id: "hybrid-sim"
display_name: "Hybrid Structural Simulator"

resonance_profile: r2
drift_characteristic: medium

allowed_categories:
  - primitive
  - composite
  - measurement
  - meta

environment_constraints:
  allowed_envs: ["sandbox", "production"]
  restricted_ops_require_token: false

routing_hints:
  preferred_for_tier: r2
  fallback: "local-sim"

notes: >
  Used for r2 composite operators.
  Medium drift. Allowed in sandbox and production.
  Cannot execute pulse operations.
```

### Structural Role

- default backend for r2  
- medium drift envelope  
- legal in sandbox  
- escalates from r1  

---

# 5. Backend: hardware-qpu-2 (r3)

```yaml
backend_id: "hardware-qpu-2"
display_name: "Hardware Structural QPU (Tier 3)"

resonance_profile: r3
drift_characteristic: high

allowed_categories:
  - primitive
  - composite
  - pulse
  - measurement
  - meta

environment_constraints:
  allowed_envs: ["production"]
  restricted_ops_require_token: true

routing_hints:
  preferred_for_tier: r3
  fallback: "hybrid-sim"

notes: >
  Used for r3 pulse operators.
  High drift. Production-only. Requires token for restricted ops.
  Never available in sandbox.
```

### Structural Role

- default backend for r3  
- high drift envelope  
- production‑only  
- token‑gated for pulse ops  

---

# 6. Compatibility Matrix

| Backend         | r1 | r2 | r3 | Pulse | Sandbox | Production |
|-----------------|----|----|----|--------|----------|-------------|
| local-sim       | ✔️ | ✖️ | ✖️ | ✖️ | ✔️ | ✔️ |
| hybrid-sim      | ✔️ | ✔️ | ✖️ | ✖️ | ✔️ | ✔️ |
| hardware-qpu-2  | ✔️ | ✔️ | ✔️ | ✔️ | ✖️ | ✔️ |

---

# 7. Routing Rules (Backend-Level)

1. r1 → **local-sim**  
2. r2 → **hybrid-sim**  
3. r3 → **hardware-qpu-2**  
4. If backend is illegal in current environment → fallback  
5. If fallback is illegal → validation failure  
6. Backend cannot change mid‑frame  
7. Tier escalation forces new frame  

---

# 8. Drift Rules (Backend-Level)

| Backend         | Drift Characteristic |
|-----------------|-----------------------|
| local-sim       | low                   |
| hybrid-sim      | medium                |
| hardware-qpu-2  | high                  |

Drift is accumulated per frame and bounded by environment:

- sandbox → relaxed  
- production → strict  
- archive → immutable  

---

# 9. Environment Rules (Backend-Level)

### Sandbox

- local-sim allowed  
- hybrid-sim allowed  
- hardware-qpu-2 forbidden  

### Production

- all backends allowed  
- pulse ops require token  

### Archive

- all backends forbidden  
- no operators allowed  

---

# 10. Summary

This file defines the **canonical backend metadata** for qCompute:

- resonance profiles  
- drift characteristics  
- operator compatibility  
- environment constraints  
- routing hints  
- fallback logic  

Backends are **structural envelopes**, not simulators.  
They enable deterministic routing, drift‑bounded execution, and strict replay.

---

Here is the **canonical `qc_Validator.md`** file.  
This is the *full validation engine specification* for qCompute — the structural law‑enforcement layer that guarantees safety, determinism, drift‑bounded execution, and environment correctness.

It is:

- zero‑drift  
- AI‑parsable  
- aligned with `qc_Router.md`, `qc_Operators.md`, `qc_Session.md`, `qc_Transitions.md`, and the entire qCompute spine  
- the authoritative definition of what is *legal* inside qCompute  

Place at:

```
/docs/rtt/Inside/qCompute/qc_Validator.md
```

---

# ✅ **qc_Validator.md — Validation Engine Specification (2026)**

# qCompute — Validation Engine  
**File:** qc_Validator.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

The **TriadicValidator** is the structural law‑enforcement layer of qCompute.

It ensures:

- environment legality  
- backend legality  
- resonance legality  
- drift legality  
- restricted‑op rules  
- archive immutability  
- lineage correctness  

Validation is **deterministic**, **structural**, and **replay‑safe**.

---

# 1. Identity

**Component:** TriadicValidator  
**Role:** Determine whether an operator is legal in the current session state  
**Scope:** Operator → Environment → Backend → Drift → Lineage  
**Guarantee:** Deterministic legality decision

Validator outputs:

```yaml
validation:
  allowed: true|false
  reason: "..."
  restricted_op: true|false
  env_ok: true|false
  backend_ok: true|false
  drift_ok: true|false
  lineage_ok: true|false
```

---

# 2. Validation Lifecycle

Validation occurs **immediately** after operator creation and before routing.

Flow:

```
Operator → Validator → Router → Frame → Capture
```

Validator has **no side effects**.  
It only returns a legality decision.

---

# 3. Validation Dimensions

Validation checks six independent dimensions:

1. **Environment legality**  
2. **Backend legality**  
3. **Resonance legality**  
4. **Restricted‑op rules**  
5. **Drift legality**  
6. **Lineage legality**

All must be true for `allowed = true`.

---

# 4. Environment Validation

Environment determines which operators are legal.

### 4.1 sandbox

Allowed:

- r1 primitive  
- r1 measurement  
- r2 composite  

Forbidden:

- r3 pulse  
- any restricted op  
- any hardware backend  

### 4.2 production

Allowed:

- r1, r2, r3  
- pulse ops (token required)  
- hardware backends  

### 4.3 archive

Forbidden:

- all operators  
- all frames  
- all routing  
- all drift  

Archive is immutable.

---

# 5. Backend Validation

Validator checks whether the operator’s required backend is legal in the current environment.

Rules:

- sandbox forbids hardware‑qpu‑2  
- production allows all backends  
- archive forbids all backends  

If backend is illegal:

```
allowed = false
reason = "backend illegal in current environment"
```

---

# 6. Resonance Validation

Validator checks:

- operator’s declared tier  
- monotonicity (tier never decreases)  
- environment constraints  
- backend constraints  

Rules:

- r1 → always legal (except archive)  
- r2 → legal in sandbox + production  
- r3 → legal only in production  

If tier is illegal:

```
allowed = false
reason = "resonance tier illegal in current environment"
```

---

# 7. Restricted‑Op Validation

Restricted ops:

- pulse operators (r3)  
- any operator requiring governance token  

Rules:

- must be in production  
- must have valid token  
- token is consumed on use  

If token missing:

```
allowed = false
reason = "restricted operation requires token"
```

---

# 8. Drift Validation

Validator checks:

- predicted drift  
- measured drift  
- drift bound (relaxed/strict/immutable)  
- accumulated drift in current frame  

Rules:

- sandbox → relaxed bound  
- production → strict bound  
- archive → immutable (drift always illegal)  

If drift exceeds bound:

```
allowed = false
reason = "drift exceeds environment bound"
```

---

# 9. Lineage Validation

Validator ensures:

- forward‑only environment transitions  
- no backward transitions  
- archive is terminal  
- token usage is correct  
- lineage entries are append‑only  

If lineage is violated:

```
allowed = false
reason = "lineage violation"
```

---

# 10. Full Validation Schema

Validator returns:

```yaml
validation:
  allowed: true|false
  reason: "..."

  restricted_op: true|false
  env_ok: true|false
  backend_ok: true|false
  drift_ok: true|false
  lineage_ok: true|false
```

All fields are explicit.  
No implicit defaults.

---

# 11. Validation Examples

### 11.1 Legal r1 in sandbox

```yaml
allowed: true
reason: "ok"
env_ok: true
backend_ok: true
drift_ok: true
lineage_ok: true
restricted_op: false
```

### 11.2 Illegal pulse op in sandbox

```yaml
allowed: false
reason: "resonance tier illegal in current environment"
restricted_op: true
env_ok: false
backend_ok: false
```

### 11.3 Missing token in production

```yaml
allowed: false
reason: "restricted operation requires token"
restricted_op: true
env_ok: true
backend_ok: true
drift_ok: true
lineage_ok: true
```

### 11.4 Illegal operator in archive

```yaml
allowed: false
reason: "archive is immutable"
env_ok: false
backend_ok: false
drift_ok: false
lineage_ok: false
```

---

# 12. Invariants Enforced by Validator

Validator enforces:

1. **Forward‑only environments**  
2. **Append‑only lineage**  
3. **Resonance tier never decreases**  
4. **Backend legality**  
5. **Environment legality**  
6. **Restricted‑op token rules**  
7. **Drift bound enforcement**  
8. **Archive immutability**  
9. **No silent behavior**  
10. **Deterministic legality decisions**  

Validator is the **first line of structural safety**.

---

# 13. Summary

TriadicValidator ensures:

- environment correctness  
- backend correctness  
- resonance correctness  
- drift correctness  
- lineage correctness  
- token correctness  

Validation is deterministic, structural, and replay‑safe — the foundation of qCompute’s safety model.

---

Here is the **canonical `qc_Router.md`** file.  
This is the *routing engine specification* — the structural logic that decides **which backend**, **which frame**, **which resonance profile**, and **why**.  
It is one of the “hard law” components of qCompute, alongside Validator, Frames, Transitions, and Capture.

It is:

- zero‑drift  
- AI‑parsable  
- student‑ready  
- perfectly aligned with the entire qCompute spine  
- the authoritative definition of routing semantics  

Place at:

```
/docs/rtt/Inside/qCompute/qc_Router.md
```

---

# ✅ **qc_Router.md — Routing Engine Specification (2026)**

# qCompute — Routing Engine  
**File:** qc_Router.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

The **TriadicRouter** determines:

- which backend executes the operator  
- whether the operator stays in the current frame or opens a new one  
- the resonance profile of the frame  
- the drift characteristic of the frame  
- the structural reason for routing decisions  

Routing is:

- deterministic  
- structural  
- environment‑aware  
- drift‑bounded  
- replay‑safe  

Routing never simulates physics.

---

# 1. Identity

**Component:** TriadicRouter  
**Role:** Select backend + frame for each operator  
**Scope:** Operator → Backend → Frame → Drift → Environment  
**Guarantee:** Deterministic routing decision

Router outputs:

```yaml
routing:
  backend: "..."
  frame_id: "frame-###"
  resonance_profile: r1|r2|r3
  drift_characteristic: low|medium|high
  reason: "..."
```

---

# 2. Routing Lifecycle

Routing occurs **after validation** and **before frame management**:

```
Operator → Validator → Router → Frame Manager → Capture
```

Routing has no side effects.  
It returns a structural decision.

---

# 3. Backend Selection

Backends are chosen by **resonance tier**:

| Tier | Backend (auto)       |
|------|-----------------------|
| r1   | local-sim             |
| r2   | hybrid-sim            |
| r3   | hardware-qpu-2        |

### 3.1 Backend Selection Rules

1. Operator declares its tier (r1/r2/r3).  
2. Router selects backend based on tier.  
3. If backend is illegal in current environment → fallback.  
4. If fallback is illegal → validation failure.  
5. Backend cannot change mid‑frame.  
6. Tier escalation forces new frame.

---

# 4. Frame Selection

Router determines whether to:

- **reuse** the current frame  
- **open** a new frame  

### 4.1 New Frame Conditions

A new frame is opened when:

1. **Tier escalation**  
   ```
   r1 → r2
   r2 → r3
   ```
2. **Backend change**  
   (illegal mid‑frame)
3. **Drift overflow**  
   (detected by Frame Manager)
4. **Meta operator**  
   (`sync`, `barrier`)
5. **Environment transition**  
   (sandbox → production → archive)
6. **Archive entry**  
   (no new frames allowed)

### 4.2 Frame Reuse Conditions

A frame is reused when:

- tier stays the same  
- backend stays the same  
- drift remains within bound  
- no meta operator  
- no environment transition  

---

# 5. Resonance Profile Assignment

Router assigns the frame’s **resonance profile**:

```
r1 → low drift
r2 → medium drift
r3 → high drift
```

Rules:

- frame resonance = operator tier  
- resonance never decreases within a frame  
- resonance escalation forces new frame  

---

# 6. Drift Characteristic Assignment

Router assigns drift characteristic based on backend:

| Backend         | Drift |
|-----------------|--------|
| local-sim       | low    |
| hybrid-sim      | medium |
| hardware-qpu-2  | high   |

Drift is accumulated per frame and bounded by environment:

- sandbox → relaxed  
- production → strict  
- archive → immutable  

---

# 7. Routing Reasons (Canonical)

Router must record the **reason** for its decision.

Allowed reasons:

- `"initial frame"`  
- `"tier escalation"`  
- `"backend change"`  
- `"drift overflow"`  
- `"meta operator"`  
- `"environment transition"`  
- `"restricted op (pulse)"`  
- `"fallback backend"`  
- `"reuse frame"`  

No implicit or silent routing.

---

# 8. Routing Examples

### 8.1 r1 → r2 escalation

```python
qc.h(qubit=0)                     # r1 → local-sim → frame-001
qc.cnot(control=0, target=1)      # r2 → hybrid-sim → frame-002
```

Routing reason:

```
"tier escalation"
```

---

### 8.2 Pulse op (r3) in production

```python
session.transition("production")
qc.apply("pulse", qubit=0, duration="32ns", amplitude=0.8)
```

Routing reason:

```
"restricted op (pulse)"
```

---

### 8.3 Drift overflow

```python
qc.cnot(...)
qc.cnot(...)
qc.cnot(...)   # overflow
```

Routing reason:

```
"drift overflow"
```

---

### 8.4 Meta operator

```python
qc.sync()
```

Routing reason:

```
"meta operator"
```

---

# 9. Routing Invariants

Router enforces:

1. **Deterministic backend selection**  
2. **Backend cannot change mid‑frame**  
3. **Resonance tier never decreases**  
4. **Tier escalation forces new frame**  
5. **Drift overflow forces new frame**  
6. **Meta ops close frames**  
7. **Environment transitions close frames**  
8. **Archive forbids new frames**  
9. **No silent routing**  
10. **Replay determinism**  

Violating any invariant invalidates the session.

---

# 10. Summary

TriadicRouter determines:

- backend  
- frame  
- resonance profile  
- drift characteristic  
- routing reason  

Routing is:

- deterministic  
- structural  
- environment‑aware  
- drift‑bounded  
- replay‑safe  

It is one of the core engines that makes qCompute governed, predictable, and teachable.

---


---

# qCompute — Drift Engine  
**File:** qc_Drift.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

The Drift Engine computes and enforces **structural drift** for all qCompute sessions.

Drift is a measure of **structural instability** introduced by operators, backends, and environment transitions.  
It is deterministic, rule‑driven, and replay‑verifiable.

qCompute computes **structure**, not amplitudes.

---

# 1. Purpose

The Drift Engine:

- computes predicted drift  
- computes measured drift  
- accumulates drift within a frame  
- enforces drift bounds  
- triggers frame closure on overflow  
- emits drift metadata for capture  
- verifies drift during replay  

Drift ensures that structural computation remains **stable**, **bounded**, and **governed**.

---

# 2. Drift Characteristics by Tier

| Tier | Drift Level | Notes |
|------|-------------|-------|
| **r1** | low | primitive operators |
| **r2** | medium | composite operators |
| **r3** | high | pulse operators |
| **measurement** | reset | forces new frame |
| **meta** | zero | barrier, flush |

---

# 3. Environment Drift Bounds

| Environment | Drift Bound | Notes |
|-------------|-------------|-------|
| **sandbox** | relaxed | allows more accumulation |
| **production** | strict | minimal tolerance |
| **archive** | immutable | no operators allowed |

Drift bound is checked **after every operator**.

---

# 4. Drift Accumulation Model

Each operator contributes:

```
drift_predicted: <float>
drift_measured: <float>
drift_total: drift_prev + drift_measured
```

Drift accumulation is:

- monotonic within a frame  
- reset when a new frame opens  
- environment‑bounded  

---

# 5. Drift Overflow

If:

```
drift_total > drift_bound
```

Then:

1. current frame closes  
2. new frame opens  
3. operator is routed into the new frame  
4. drift resets to operator’s measured drift  

Overflow is deterministic and replay‑verifiable.

---

# 6. Frame Interaction

Drift interacts with frames as follows:

- r1: may reuse frame  
- r2: may reuse frame or escalate tier → new frame  
- r3: always opens new frame  
- measurement: always opens new frame  
- meta: always opens new frame  

Drift overflow is an **additional** trigger for new frame creation.

---

# 7. Routing Interaction

Router receives drift metadata:

```
routing:
  backend: "<backend>"
  reason: "<reason>"
  frame_action: "reuse" | "new"
```

Drift Engine may override Router’s frame decision if overflow occurs.

---

# 8. Capture Metadata

Each operator produces drift metadata:

```
drift:
  predicted: <float>
  measured: <float>
  accumulated: <float>
  overflow: true | false
```

Each frame produces a drift summary:

```
frame_drift:
  total: <float>
  max: <float>
  environment_bound: <float>
```

All fields are required.

---

# 9. Replay Verification

Replay recomputes drift:

- predicted drift  
- measured drift  
- accumulated drift  
- overflow events  
- frame boundaries  
- environment bounds  

Replay must confirm:

- drift never exceeds bound  
- overflow events match capture  
- frame boundaries match drift logic  
- drift summaries match operator accumulation  

Replay is deterministic and read‑only.

---

# 10. Invariants

1. drift must not exceed environment bound  
2. overflow must open a new frame  
3. measurement resets drift  
4. meta operators reset drift  
5. r3 operators reset drift  
6. drift accumulation must be monotonic within a frame  
7. drift summaries must match operator accumulation  
8. archive forbids all operators  

---

# 11. Summary

The Drift Engine ensures:

- structural stability  
- deterministic accumulation  
- governed overflow  
- environment‑bounded execution  
- replay‑verifiable correctness  

Drift is a **first‑class structural signal** in qCompute.
# qCompute — Advanced Structural Examples  
**File:** qc_Examples_Advanced.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

These examples demonstrate **full‑pipeline**, **multi‑frame**, **multi‑backend**, and **multi‑transition** structural behavior in qCompute.

They show:

- tier escalation (r1 → r2 → r3)
- tier decrease (measurement)
- drift overflow
- backend switching
- environment transitions
- token usage
- meta‑operators
- capture + replay
- full structural lifecycle

No amplitudes.  
No simulation.  
Structure only.

---

# 1. Advanced Multi‑Frame Example (r1 → r2 → r1)

```python
session = qSession(env="sandbox")

session.h(q=0)            # r1 → frame 1
session.cx(q1=0, q2=1)    # r2 → new frame
session.measure(q=0)      # measurement → tier decrease → new frame
session.x(q=1)            # r1 → same frame

session.save_trace("adv_multiframe.qtrace")
```

**Demonstrates**

- r1 → r2 tier escalation  
- measurement forcing tier decrease  
- frame 1 (r1), frame 2 (r2), frame 3 (measurement + r1)  
- backend sequence: local-sim → hybrid-sim → local-sim  

---

# 2. Advanced Drift Overflow Example

```python
session = qSession(env="sandbox")

# r2 operators accumulate medium drift
session.cx(q1=0, q2=1)  
session.cx(q1=1, q2=2)
session.cx(q1=2, q2=3)

# drift overflow → new frame
session.cx(q1=3, q2=4)

session.save_trace("adv_drift_overflow.qtrace")
```

**Demonstrates**

- drift accumulation  
- drift overflow forcing new frame  
- backend = hybrid-sim  
- two frames with identical tier but different drift summaries  

---

# 3. Advanced Transition Example (Sandbox → Production → Archive)

```python
session = qSession(env="sandbox")
session.deploy_token("t1")
session.deploy_token("t2")

session.h(q=0)                 # sandbox
session.transition("production")  # token t1

session.pulse(q=0, duration=20, amplitude=0.5)  # r3 → production only

session.transition("archive")  # token t2

session.save_trace("adv_transitions.qtrace")
```

**Demonstrates**

- sandbox → production → archive  
- token usage  
- r3 operator allowed only in production  
- archive terminality  
- lineage: ["sandbox", "production", "archive"]  

---

# 4. Advanced Backend Switching Example

```python
session = qSession(env="production")
session.deploy_token("t1")

session.h(q=0)                    # r1 → local-sim
session.cx(q1=0, q2=1)            # r2 → hybrid-sim
session.pulse(q=1, duration=10, amplitude=0.4)  # r3 → hardware-qpu-2

session.save_trace("adv_backend_switch.qtrace")
```

**Demonstrates**

- backend progression: local-sim → hybrid-sim → hardware-qpu-2  
- tier escalation across three levels  
- r3 token requirement  

---

# 5. Advanced Meta‑Operator Example (Barrier + Flush)

```python
session = qSession(env="sandbox")

session.h(q=0)
session.barrier()                 # meta → new frame
session.cx(q1=0, q2=1)
session.flush()                   # meta → new frame

session.save_trace("adv_meta.qtrace")
```

**Demonstrates**

- meta‑operators always open new frames  
- zero drift  
- structural segmentation  

---

# 6. Advanced Mixed Pipeline Example (Full System)

```python
session = qSession(env="sandbox")
session.deploy_token("t1")
session.deploy_token("t2")

# Frame 1: r1
session.h(q=0)

# Frame 2: r2
session.cx(q1=0, q2=1)

# Transition to production
session.transition("production")   # token t1

# Frame 3: r3
session.pulse(q=0, duration=15, amplitude=0.3)

# Frame 4: measurement → tier decrease
session.measure(q=0)

# Transition to archive
session.transition("archive")      # token t2

session.save_trace("adv_full_pipeline.qtrace")
```

**Demonstrates**

- r1 → r2 → transition → r3 → measurement → transition  
- four frames  
- backend sequence: local-sim → hybrid-sim → hardware-qpu-2 → local-sim  
- drift progression  
- lineage: ["sandbox", "production", "archive"]  
- archive terminality  

---

# 7. Advanced Replay Example

```python
replay = qReplay("adv_full_pipeline.qtrace")

for frame in replay.frames:
    print(frame.frame_id, frame.backend, frame.resonance_profile)

for op in replay.operators:
    print(op.op_id, op.routing["reason"])
```

**Demonstrates**

- frame reconstruction  
- backend reconstruction  
- routing reasons  
- deterministic replay  
- invariant verification  

---

# Summary

These advanced examples demonstrate:

- multi‑tier execution  
- multi‑backend routing  
- drift overflow  
- environment transitions  
- token usage  
- meta‑operators  
- capture + replay  
- full structural lifecycle  

Use these examples to understand **complex qCompute behavior**.
# qCompute — Minimal Structural Examples  
**File:** qc_Examples_Minimal.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

These examples demonstrate the **smallest possible** structural flows in qCompute.

They show:

- operator entry  
- validation  
- routing  
- frame creation  
- drift accumulation  
- transitions  
- capture  
- replay  

No amplitudes.  
No simulation.  
Structure only.

---

# 1. Minimal r1 Example (Sandbox)

```python
from qcompute import qSession

session = qSession(env="sandbox")

session.h(q=0)
session.x(q=0)

session.save_trace("r1_minimal.qtrace")
```

**What this demonstrates**

- sandbox environment  
- r1 operators  
- single frame  
- low drift  
- backend = local-sim  
- simple `.qtrace` with one frame  

---

# 2. Minimal r2 Example (Tier Escalation)

```python
session = qSession(env="sandbox")

session.h(q=0)          # r1 → frame 1
session.cx(q1=0, q2=1)  # r2 → new frame

session.save_trace("r2_minimal.qtrace")
```

**What this demonstrates**

- r1 → r2 tier escalation  
- automatic new frame  
- backend shift: local-sim → hybrid-sim  
- drift increase  
- two-frame `.qtrace`  

---

# 3. Minimal Measurement Example (Tier Decrease)

```python
session = qSession(env="sandbox")

session.cx(q1=0, q2=1)  # r2 → frame 1
session.measure(q=0)    # measurement → new frame

session.save_trace("measure_minimal.qtrace")
```

**What this demonstrates**

- r2 operator  
- measurement forces tier decrease  
- measurement forces new frame  
- drift reset  

---

# 4. Minimal r3 Example (Pulse Operator)

```python
session = qSession(env="production")
session.deploy_token("t1")

session.pulse(q=0, duration=20, amplitude=0.5)

session.save_trace("r3_minimal.qtrace")
```

**What this demonstrates**

- production environment  
- r3 operator  
- token requirement  
- backend = hardware-qpu-2  
- high drift  
- single-frame `.qtrace`  

---

# 5. Minimal Transition Example (Sandbox → Production)

```python
session = qSession(env="sandbox")
session.deploy_token("t1")

session.h(q=0)
session.transition("production")

session.save_trace("transition_minimal.qtrace")
```

**What this demonstrates**

- sandbox → production transition  
- token usage  
- frame closure on transition  
- lineage update  

---

# 6. Minimal Replay Example

```python
from qcompute import qReplay

replay = qReplay("r1_minimal.qtrace")

print(replay.session.env)
print(replay.frames[0].backend)
print(replay.operators[0].routing)
```

**What this demonstrates**

- loading a `.qtrace`  
- reconstructing session  
- accessing frames  
- accessing routing metadata  

---

# 7. Minimal Full Pipeline Example

```python
session = qSession(env="sandbox")
session.deploy_token("t1")

session.h(q=0)          # r1
session.cx(q1=0, q2=1)  # r2 → new frame
session.transition("production")
session.pulse(q=0, duration=10, amplitude=0.3)

session.save_trace("pipeline_minimal.qtrace")
```

**What this demonstrates**

- r1 → r2 → transition → r3  
- three frames  
- backend progression  
- drift progression  
- lineage: ["sandbox", "production"]  
- complete structural pipeline  

---

# Summary

These minimal examples show:

- r1, r2, r3 operators  
- tier escalation + tier decrease  
- drift behavior  
- environment transitions  
- capture + replay  
- the full structural pipeline in the smallest possible form  

Use these as the **entry point** for learning qCompute.
# qCompute — Structural Pipeline Flow  
**File:** qc_Flow.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This document provides a **narrative walkthrough** of the qCompute structural pipeline.

The pipeline is:

```
operator → validator → router → frame manager → drift engine → transitions → capture → replay
```

qCompute computes **structure**, not amplitudes.

---

# 1. Operator Entry

A structural operator enters the system:

```python
session.h(q=0)
session.cx(q1=0, q2=1)
session.pulse(q=0, duration=20, amplitude=0.5)
session.measure(q=0)
```

Operators carry:

- name  
- parameters  
- resonance tier (r1 / r2 / r3)  
- drift characteristic  
- backend requirements  

The operator is passed to the **Validator**.

---

# 2. Validator

Validator enforces:

- grammar correctness  
- argument correctness  
- environment legality  
- tier legality  
- backend legality  
- token requirements  
- archive terminality  

If invalid:

```
allowed: false
reason: "<canonical reason>"
```

Invalid operators are captured but not executed.

If valid, the operator proceeds to the **Router**.

---

# 3. Router

Router selects:

- backend  
- frame reuse vs. new frame  
- routing reason  

Routing rules:

- r1 → `local-sim`  
- r2 → `hybrid-sim`  
- r3 → `hardware-qpu-2` (token required)  

Router may:

- reuse current frame  
- escalate tier → open new frame  
- detect drift overflow → open new frame  
- detect measurement → open new frame  

Router emits routing metadata and passes the operator to the **Frame Manager**.

---

# 4. Frame Manager

A **frame** is a structural container with:

- environment  
- backend  
- resonance profile  
- drift bound  
- drift summary  
- operator list  

Frame Manager:

- opens frames  
- closes frames  
- enforces tier monotonicity  
- enforces backend consistency  
- enforces environment legality  

Triggers for new frame:

- first operator  
- tier escalation  
- tier decrease (measurement)  
- r3 operator  
- drift overflow  
- meta operator  
- environment transition  

The operator is appended to the active frame and passed to the **Drift Engine**.

---

# 5. Drift Engine

Drift Engine computes:

- predicted drift  
- measured drift  
- accumulated drift  

Drift bounds:

| Environment | Drift Bound |
|-------------|-------------|
| sandbox     | relaxed     |
| production  | strict      |
| archive     | immutable   |

If drift exceeds bound:

- frame closes  
- new frame opens  
- operator is routed into new frame  

Drift metadata is appended and the operator proceeds to **Transitions**.

---

# 6. Transition Engine

Transitions are explicit:

```python
session.transition("production")
session.transition("archive")
```

Rules:

- sandbox → production (token required)  
- production → archive (token required)  
- archive → (forbidden)  

Transition Engine:

- closes current frame  
- updates environment  
- updates drift bound  
- updates backend legality  
- appends lineage  

Transition events are passed to **Capture**.

---

# 7. Capture Engine

Capture writes an append‑only `.qtrace` ledger.

Each operator produces:

- operator entry  
- validation metadata  
- routing metadata  
- drift metadata  
- timestamp  
- hash_prev / hash_self  

Each frame produces:

- frame summary  
- drift summary  
- operator list  
- timestamps  

Each transition produces:

- from / to  
- token used  
- timestamp  

Capture writes:

1. header  
2. operator entries  
3. frame summaries  
4. transitions  
5. footer  
6. hash chain root  

The `.qtrace` file is the **source of truth**.

---

# 8. Replay Engine

Replay reconstructs:

- session  
- frames  
- operators  
- transitions  
- lineage  
- drift accumulation  
- backend binding  
- tier monotonicity  

Replay verifies:

- hash chain integrity  
- environment legality  
- drift bounds  
- transition correctness  
- archive terminality  
- canonical field presence  

Replay is deterministic and read‑only.

---

# 9. Full Pipeline Diagram (Textual)

```
┌──────────────────────────────────────────────────────────────┐
│                        Operator Entry                         │
└───────────────┬──────────────────────────────────────────────┘
                ▼
        ┌──────────────┐
        │   Validator   │  grammar, args, env, tier, backend, token
        └───────┬──────┘
                ▼
        ┌──────────────┐
        │    Router     │  backend, frame reuse/new, tier escalation
        └───────┬──────┘
                ▼
        ┌──────────────┐
        │ Frame Manager │  open/close frames, tier monotonicity
        └───────┬──────┘
                ▼
        ┌──────────────┐
        │ Drift Engine  │  predicted/measured drift, overflow
        └───────┬──────┘
                ▼
        ┌──────────────┐
        │  Transitions  │  env changes, lineage, token use
        └───────┬──────┘
                ▼
        ┌──────────────┐
        │   Capture     │  append-only .qtrace ledger
        └───────┬──────┘
                ▼
        ┌──────────────┐
        │    Replay     │  reconstruct + verify invariants
        └──────────────┘
```

---

# 10. Summary

The qCompute pipeline:

- validates  
- routes  
- frames  
- accumulates drift  
- transitions environments  
- captures a ledger  
- replays and verifies  

qCompute is the **structural compute harness** of RTT‑Inside.
# qCompute — Identity  
**File:** qc_Identity.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

qCompute is the **structural compute harness** of RTT‑Inside.

It provides the complete operator → routing → frame → drift → transition → capture → replay pipeline.  
qCompute computes **structure**, not amplitudes.

---

# 1. Purpose

qCompute exists to:

- define resonance‑tiered operators (r1 / r2 / r3)  
- validate operators against grammar, environment, backend, and tier  
- route operators to appropriate backends  
- manage resonance frames and drift accumulation  
- govern environment transitions  
- produce an append‑only `.qtrace` ledger  
- replay and verify structural correctness  

qCompute is the **execution substrate** for RTT‑Inside.

---

# 2. Identity Statement

qCompute is:

- **structural** — computes structure, not physics  
- **deterministic** — routing, drift, and transitions are rule‑driven  
- **governed** — all operators pass through validation  
- **tiered** — r1, r2, r3 define resonance depth  
- **environment‑aware** — sandbox, production, archive  
- **drift‑bounded** — drift accumulation is strictly enforced  
- **append‑only** — capture ledger is immutable  
- **replay‑verifiable** — every session can be reconstructed  

qCompute is **not**:

- a quantum simulator  
- a physics engine  
- a numerical amplitude system  
- a probabilistic execution model  

---

# 3. Structural Role

qCompute is the **compute layer** of RTT‑Inside.

It sits between:

- **Operators** (intent)  
- **Backends** (execution substrate)  
- **Frames** (structural containers)  
- **Drift** (stability envelope)  
- **Transitions** (environment governance)  
- **Capture** (ledger)  
- **Replay** (verification)  

qCompute defines the **rules**, **invariants**, and **structural lifecycle** of computation.

---

# 4. Invariants

qCompute enforces the following invariants:

1. **Grammar Validity**  
   Operators must follow canonical grammar.

2. **Argument Validity**  
   All parameters must be well‑typed and complete.

3. **Environment Legality**  
   - sandbox: r1, r2  
   - production: r1, r2, r3  
   - archive: none  

4. **Backend Legality**  
   - r1 → local-sim  
   - r2 → hybrid-sim  
   - r3 → hardware-qpu-2  

5. **Tier Monotonicity**  
   Tiers may increase within a frame but never decrease.

6. **Measurement Reset**  
   Measurement forces a new frame.

7. **Meta Operators**  
   Meta operators always open a new frame.

8. **Drift Bound**  
   Drift must not exceed environment drift limits.

9. **Transition Legality**  
   - sandbox → production (token required)  
   - production → archive (token required)  
   - archive → (forbidden)  

10. **Archive Terminality**  
    No operators allowed in archive.

11. **Hash Chain Integrity**  
    Capture must maintain a valid hash chain.

---

# 5. Module Boundaries

qCompute defines:

- operator semantics  
- routing rules  
- frame lifecycle  
- drift model  
- environment transitions  
- capture format  
- replay verification  

qCompute does **not** define:

- amplitude simulation  
- quantum state evolution  
- hardware calibration  
- backend implementation details  

These belong to other modules.

---

# 6. Summary

qCompute is the **structural compute substrate** of RTT‑Inside.

It provides:

- resonance‑tiered operators  
- deterministic routing  
- drift‑bounded frames  
- governed transitions  
- append‑only capture  
- strict replay  

qCompute ensures that all computation inside RTT‑Inside is **valid**, **deterministic**, **governed**, and **verifiable**.
# qCompute — Module Index  
**File:** qc_Index.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

qCompute is the **structural compute harness** of RTT‑Inside.  
It defines the full operator → routing → frame → drift → transition → capture → replay pipeline.

This index provides:

- module overview  
- file map  
- structural orientation  
- learning path  

---

# 1. Overview

qCompute is a **resonance‑tiered structural execution engine**.

It provides:

- r1 / r2 / r3 operators  
- deterministic routing  
- drift‑bounded frames  
- environment transitions  
- append‑only capture  
- strict replay verification  

qCompute computes **structure**, not amplitudes.

---

# 2. File Map

| File | Role | Description |
|------|------|-------------|
| **qc_FrontDoor.html** | frontdoor | HTML entry point with canonical metadata. |
| **qc_Index.md** | index | Module index and file map. |
| **qc_Identity.md** | signature | Defines identity, purpose, invariants, and structural role. |
| **qc_Session.md** | engine | Session container: environment, drift bound, lineage, frames, tokens. |
| **qc_Validator.md** | engine | Legality engine: grammar, arguments, environment, tier, backend, tokens. |
| **qc_Operators.md** | engine | Operator catalog: r1, r2, r3, measurement, meta. |
| **qc_OperatorGrammar.md** | signature | Formal grammar and legality rules for all operators. |
| **qc_Backends.md** | engine | Backend overview: local-sim, hybrid-sim, hardware-qpu-2. |
| **qc_BackendProfiles.md** | profile | Deep metadata profiles for each backend. |
| **qc_Router.md** | engine | Routing engine: backend selection, frame reuse, tier escalation, overflow. |
| **qc_ResonanceFrame.md** | engine | Frame manager: lifecycle, tier monotonicity, backend binding, drift. |
| **qc_Drift.md** | engine | Drift engine: predicted/measured drift, accumulation, overflow. |
| **qc_Transitions.md** | engine | Environment transitions: sandbox → production → archive. |
| **qc_Capture.md** | engine | Append‑only ledger writer: operators, frames, transitions, hash chain. |
| **qc_Replay.md** | engine | Replay verifier: reconstructs session, checks invariants, verifies hashes. |
| **qc_API.md** | signature | Public API surface for sessions, operators, transitions, capture, replay. |
| **qc_Flow.md** | map | Narrative walkthrough of the structural pipeline. |
| **qc_Examples_Minimal.md** | example | Minimal structural examples. |
| **qc_Examples_Advanced.md** | example | Advanced multi‑frame, multi‑transition examples. |
| **qc_Module.json** | manifest | Module identity, file roles, analyzer layers, schema. |

---

# 3. Structural Orientation

qCompute is organized into **five layers**:

### 1. Identity Layer  
Defines what the module *is* and *is not*.

### 2. Operator Layer  
Operators, grammar, validation.

### 3. Dimensional Layer  
Backends, backend profiles.

### 4. Regime Layer  
Routing, frames, drift, transitions.

### 5. Ledger Layer  
Capture + replay.

This structure mirrors the RTT‑Inside architecture.

---

# 4. Learning Path

Recommended reading order:

1. **qc_Identity.md**  
2. **qc_Operators.md**  
3. **qc_OperatorGrammar.md**  
4. **qc_Backends.md**  
5. **qc_Router.md**  
6. **qc_ResonanceFrame.md**  
7. **qc_Drift.md**  
8. **qc_Transitions.md**  
9. **qc_Capture.md**  
10. **qc_Replay.md**  
11. **qc_API.md**  
12. **qc_Examples_Minimal.md**  
13. **qc_Examples_Advanced.md**  
14. **qc_Flow.md**

---

# 5. Summary

qCompute is the **structural compute substrate** of RTT‑Inside.

This index provides:

- orientation  
- file map  
- structural overview  
- learning path  

Use this page as the **front‑door reference** for the entire module.
# qCompute — Operator Grammar  
**File:** qc_OperatorGrammar.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This document defines the **formal grammar**, **argument rules**, and **legality semantics** for all qCompute operators.

The grammar is:

- minimal  
- deterministic  
- environment‑aware  
- backend‑aware  
- drift‑aware  
- replay‑safe  

qCompute computes **structure**, not amplitudes.

---

# 1. Operator Namespace

Operators belong to five families:

| Family | Tier | Examples |
|--------|------|----------|
| **r1** (primitive) | r1 | `x`, `y`, `z`, `h`, `s`, `t` |
| **r2** (composite) | r2 | `cx`, `cz`, `swap` |
| **r3** (pulse) | r3 | `pulse` |
| **measurement** | special | `measure` |
| **meta** | meta | `barrier`, `flush` |

Each operator has:

- name  
- tier  
- drift characteristic  
- backend requirement  
- environment legality  

---

# 2. Formal Grammar

### 2.1 Operator Invocation

```
<operator> "(" <args> ")"
```

### 2.2 Arguments

```
<args> ::= <arg> | <arg> "," <args>
<arg>  ::= <name> "=" <value>
```

### 2.3 Names

```
<name> ::= /[a-zA-Z_][a-zA-Z0-9_]*/
```

### 2.4 Values

```
<value> ::= <int> | <float> | <bool> | <string>
```

### 2.5 QuBits

```
q, q1, q2 ∈ ℕ
```

---

# 3. Operator Legality Rules

Each operator is validated against:

1. grammar  
2. argument correctness  
3. environment legality  
4. tier legality  
5. backend legality  
6. token requirements  
7. archive terminality  

If invalid:

```
allowed: false
reason: "<canonical reason>"
```

Canonical reasons:

- `"invalid grammar"`
- `"invalid arguments"`
- `"illegal in environment"`
- `"backend mismatch"`
- `"backend illegal in environment"`
- `"tier decrease inside frame"`
- `"token required"`
- `"archive terminal"`
- `"illegal transition"`

---

# 4. Tier Semantics

### r1 (primitive)

- allowed in sandbox + production  
- low drift  
- backend: `local-sim`  
- may reuse frame  

### r2 (composite)

- allowed in sandbox + production  
- medium drift  
- backend: `hybrid-sim`  
- **tier escalation** → new frame  

### r3 (pulse)

- **production only**  
- **token required**  
- high drift  
- backend: `hardware-qpu-2`  
- always opens new frame  

### measurement

- allowed in sandbox + production  
- forces **tier decrease**  
- forces **new frame**  

### meta

- allowed in sandbox + production  
- zero drift  
- always opens new frame  

---

# 5. Backend Legality

| Backend | Allowed Tiers | Environments |
|---------|---------------|--------------|
| `local-sim` | r1 | sandbox, production |
| `hybrid-sim` | r1, r2 | sandbox, production |
| `hardware-qpu-2` | r3 | production only |

Archive is **terminal** and forbids all operators.

---

# 6. Environment Legality

| Environment | Allowed Tiers | Notes |
|-------------|---------------|-------|
| sandbox | r1, r2 | relaxed drift |
| production | r1, r2, r3 | strict drift, tokens required for r3 |
| archive | none | terminal |

Transitions:

- sandbox → production (token required)  
- production → archive (token required)  
- archive → (forbidden)  

---

# 7. Drift Semantics

Each operator has a drift characteristic:

| Tier | Drift |
|------|--------|
| r1 | low |
| r2 | medium |
| r3 | high |
| measurement | reset |
| meta | zero |

Drift overflow:

- closes current frame  
- opens new frame  
- routes operator into new frame  

---

# 8. Frame Semantics

A frame is valid if:

- tier is monotonic (no decrease)  
- backend is consistent  
- drift ≤ drift bound  
- environment is legal  

Triggers for new frame:

- first operator  
- tier escalation  
- tier decrease  
- r3 operator  
- drift overflow  
- meta operator  
- environment transition  

---

# 9. Capture Semantics

Each operator produces:

```
operator:
  op_id: "<id>"
  name: "<operator>"
  params: {...}
  validation: {...}
  routing: {...}
  drift: {...}
  timestamp: "<iso8601>"
  hash_prev: "<sha256>"
  hash_self: "<sha256>"
```

All fields are required.

---

# 10. Replay Semantics

Replay verifies:

- grammar  
- tier monotonicity  
- backend legality  
- environment legality  
- drift bounds  
- transition legality  
- hash chain integrity  
- canonical field presence  

Replay is deterministic and read‑only.

---

# 11. Invariants

1. grammar must be valid  
2. arguments must be valid  
3. environment must allow tier  
4. backend must match tier  
5. r3 requires token  
6. measurement forces new frame  
7. meta forces new frame  
8. drift must not exceed bound  
9. archive is terminal  
10. hash chain must be valid  

---

# Summary

The Operator Grammar defines:

- operator namespace  
- formal grammar  
- argument rules  
- tier semantics  
- backend legality  
- environment legality  
- drift + frame semantics  
- capture + replay invariants  

This grammar is the **foundation** of qCompute.
# qCompute — Operator Catalog  
**File:** qc_Operators.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This document defines the **complete operator catalog** for qCompute.

Operators are structural actions that pass through:

```
Validator → Router → Frame Manager → Drift Engine → Capture → Replay
```

qCompute computes **structure**, not amplitudes.

---

# 1. Operator Families

qCompute defines five operator families:

| Family | Tier | Examples | Notes |
|--------|------|----------|-------|
| **r1** (primitive) | r1 | `x`, `y`, `z`, `h`, `s`, `t` | low drift, local-sim |
| **r2** (composite) | r2 | `cx`, `cz`, `swap` | medium drift, hybrid-sim |
| **r3** (pulse) | r3 | `pulse` | high drift, hardware-qpu-2, token required |
| **measurement** | special | `measure` | tier decrease, new frame |
| **meta** | meta | `barrier`, `flush` | zero drift, new frame |

Each operator has:

- name  
- tier  
- parameter schema  
- drift characteristic  
- backend binding  
- environment legality  
- routing behavior  

---

# 2. r1 Operators (Primitive Tier)

r1 operators are **primitive structural actions**.

Backend: `local-sim`  
Environment: sandbox, production  
Drift: low  
Frame: may reuse frame  

### 2.1 Operator List

| Operator | Params | Description |
|----------|---------|-------------|
| `x` | `q: int` | Pauli‑X |
| `y` | `q: int` | Pauli‑Y |
| `z` | `q: int` | Pauli‑Z |
| `h` | `q: int` | Hadamard |
| `s` | `q: int` | Phase |
| `t` | `q: int` | T‑gate |

### 2.2 Schema

```
x(q=<int>)
y(q=<int>)
z(q=<int>)
h(q=<int>)
s(q=<int>)
t(q=<int>)
```

---

# 3. r2 Operators (Composite Tier)

r2 operators are **composite structural actions**.

Backend: `hybrid-sim`  
Environment: sandbox, production  
Drift: medium  
Frame: may reuse or open new frame (tier escalation, drift overflow)  

### 3.1 Operator List

| Operator | Params | Description |
|----------|---------|-------------|
| `cx` | `q1: int`, `q2: int` | Controlled‑X |
| `cz` | `q1: int`, `q2: int` | Controlled‑Z |
| `swap` | `q1: int`, `q2: int` | Swap |

### 3.2 Schema

```
cx(q1=<int>, q2=<int>)
cz(q1=<int>, q2=<int>)
swap(q1=<int>, q2=<int>)
```

---

# 4. r3 Operators (Pulse Tier)

r3 operators are **pulse‑level structural actions**.

Backend: `hardware-qpu-2`  
Environment: production only  
Drift: high  
Frame: always opens new frame  
Token: required  

### 4.1 Operator List

| Operator | Params | Description |
|----------|---------|-------------|
| `pulse` | `q: int`, `duration: float`, `amplitude: float` | Pulse operator |

### 4.2 Schema

```
pulse(q=<int>, duration=<float>, amplitude=<float>)
```

---

# 5. Measurement Operators

Measurement is a **tier‑decrease** operator.

Backend: `local-sim`  
Environment: sandbox, production  
Drift: reset  
Frame: always opens new frame  

### 5.1 Operator List

| Operator | Params | Description |
|----------|---------|-------------|
| `measure` | `q: int` | Structural measurement |

### 5.2 Schema

```
measure(q=<int>)
```

---

# 6. Meta Operators

Meta operators are **structural boundaries**.

Backend: same as current frame  
Environment: sandbox, production  
Drift: zero  
Frame: always opens new frame  

### 6.1 Operator List

| Operator | Params | Description |
|----------|---------|-------------|
| `barrier` | none | Frame boundary |
| `flush` | none | Frame boundary + drift reset |

### 6.2 Schema

```
barrier()
flush()
```

---

# 7. Operator Legality Summary

| Operator | Tier | Backend | Env | Token | Frame Action |
|----------|------|----------|------|--------|----------------|
| r1 | r1 | local-sim | sandbox, production | no | reuse |
| r2 | r2 | hybrid-sim | sandbox, production | no | reuse/new |
| r3 | r3 | hardware-qpu-2 | production | yes | new |
| measure | special | local-sim | sandbox, production | no | new |
| meta | meta | current | sandbox, production | no | new |

---

# 8. Routing Behavior

Routing reasons include:

- `"tier-binding"`  
- `"tier-escalation"`  
- `"tier-decrease"`  
- `"measurement"`  
- `"meta"`  
- `"r3-requires-new-frame"`  
- `"drift-overflow"`  
- `"environment-transition"`  
- `"token-required"`  

Operators always produce routing metadata.

---

# 9. Capture Metadata

Each operator produces:

```
operator:
  op_id: "<id>"
  name: "<operator>"
  params: {...}
  validation: {...}
  routing: {...}
  drift: {...}
  timestamp: "<iso8601>"
  hash_prev: "<sha256>"
  hash_self: "<sha256>"
```

All fields are required.

---

# 10. Replay Verification

Replay verifies:

- grammar  
- arguments  
- tier legality  
- backend legality  
- environment legality  
- token requirements  
- routing reason  
- frame action  
- drift metadata  
- hash chain integrity  

Replay must match capture exactly.

---

# 11. Invariants

1. r1 → local-sim  
2. r2 → hybrid-sim  
3. r3 → hardware-qpu-2  
4. r3 requires token  
5. r3 always opens new frame  
6. measurement always opens new frame  
7. meta always opens new frame  
8. tier must not decrease inside a frame  
9. drift must not exceed bound  
10. archive forbids all operators  

---

# 12. Summary

The Operator Catalog defines:

- operator families  
- tier assignments  
- backend binding  
- environment legality  
- drift characteristics  
- routing behavior  
- capture metadata  
- replay invariants  

Operators are the **structural actions** of qCompute.
# qCompute — Replay Engine  
**File:** qc_Replay.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

The Replay Engine is the **final authority** of qCompute.

Replay reconstructs:

- session  
- frames  
- operators  
- transitions  
- drift  
- routing  
- backend legality  
- environment sequence  
- hash chain integrity  

Replay verifies that the `.qtrace` ledger is **complete**, **valid**, and **canonical**.

qCompute computes **structure**, not amplitudes.

---

# 1. Purpose

Replay:

- reads the `.qtrace` file  
- reconstructs the entire session deterministically  
- verifies all invariants  
- verifies all routing decisions  
- verifies all drift calculations  
- verifies all transitions  
- verifies all frame boundaries  
- verifies all backend legality  
- verifies all environment legality  
- verifies the hash chain  

Replay is **read‑only** and **authoritative**.

---

# 2. Replay Inputs

Replay receives:

```
.qtrace file:
  header
  operator entries
  frame summaries
  transitions
  footer
  hash chain root
```

All fields are required.

---

# 3. Replay Reconstruction Model

Replay reconstructs the session by:

1. reading operator stream  
2. applying Validator rules  
3. applying Router rules  
4. applying Frame Manager rules  
5. applying Drift Engine rules  
6. applying Transition Engine rules  
7. verifying capture metadata  
8. verifying hash chain integrity  

Replay must produce the **same structural session** that was originally executed.

---

# 4. Operator Reconstruction

For each operator:

Replay verifies:

- grammar  
- arguments  
- tier legality  
- backend legality  
- environment legality  
- token requirements  
- routing reason  
- frame action  
- drift metadata  
- timestamps  
- hash chain links  

Replay recomputes:

- backend  
- routing reason  
- frame action  
- drift predicted  
- drift measured  
- drift accumulated  

Replay must match capture exactly.

---

# 5. Frame Reconstruction

Replay reconstructs frames by:

- opening frames on routing triggers  
- closing frames on routing triggers  
- enforcing tier monotonicity  
- enforcing backend consistency  
- enforcing drift bounds  
- enforcing environment consistency  

Replay verifies:

- frame boundaries  
- frame drift summaries  
- frame backend summaries  
- frame timestamps  

Frames must match capture exactly.

---

# 6. Transition Reconstruction

Replay reconstructs transitions by:

- reading transition entries  
- verifying legality  
- verifying token usage  
- verifying environment sequence  
- verifying drift reset  
- verifying frame closure  
- verifying backend legality  

Replay must confirm:

- sandbox → production → archive  
- no illegal transitions  
- archive is terminal  

---

# 7. Drift Reconstruction

Replay recomputes drift:

```
drift_total = Σ drift_measured
```

Replay verifies:

- drift never exceeds bound  
- drift overflow events match capture  
- drift resets match frame boundaries  
- drift summaries match operator accumulation  

Drift must match capture exactly.

---

# 8. Backend Reconstruction

Replay verifies:

- backend legality  
- tier binding  
- environment legality  
- backend changes  
- backend summaries  

Backend must match capture exactly.

---

# 9. Hash Chain Verification

Each operator and transition includes:

```
hash_prev: "<sha256>"
hash_self: "<sha256>"
```

Replay verifies:

- hash_prev matches previous entry  
- hash_self matches recomputed hash  
- final hash matches footer root  

If hash chain invalid:

```
replay_valid: false
reason: "hash chain invalid"
```

---

# 10. Replay Metadata

Replay produces:

```
replay:
  valid: true|false
  reasons: [...]
  reconstructed_session: {...}
```

Reasons include:

- "illegal operator"
- "illegal transition"
- "tier violation"
- "backend violation"
- "environment violation"
- "drift violation"
- "hash chain invalid"
- "capture mismatch"

---

# 11. Invariants

Replay enforces:

1. grammar correctness  
2. argument correctness  
3. environment legality  
4. backend legality  
5. tier monotonicity  
6. drift bounds  
7. routing correctness  
8. transition correctness  
9. token requirements  
10. frame boundaries  
11. archive terminality  
12. hash chain integrity  

Replay is the **final arbiter** of structural truth.

---

# 12. Summary

The Replay Engine:

- reconstructs the entire session  
- verifies every structural decision  
- enforces all invariants  
- validates the hash chain  
- ensures the `.qtrace` file is canonical  

Replay is the **authoritative verifier** of qCompute.
# qCompute — Resonance Frame Manager  
**File:** qc_ResonanceFrame.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

A **ResonanceFrame** is the fundamental structural container of qCompute.

Frames bind:

- environment  
- backend  
- resonance tier  
- drift envelope  
- operator list  
- timestamps  
- lineage  

Frames ensure that structural computation remains **stable**, **bounded**, and **governed**.

qCompute computes **structure**, not amplitudes.

---

# 1. Purpose

The Frame Manager:

- opens frames  
- closes frames  
- enforces tier monotonicity  
- enforces backend consistency  
- enforces drift bounds  
- enforces environment legality  
- segments structural computation  
- emits frame metadata for capture  
- reconstructs frames during replay  

Frames are **append‑only** and **immutable after closure**.

---

# 2. Frame Identity

Each frame has:

```
frame_id: <int>
environment: "sandbox" | "production" | "archive"
backend: "<backend-id>"
tier: "r1" | "r2" | "r3"
drift:
  accumulated: <float>
  max: <float>
operators: [ ... ]
timestamp_open: "<iso8601>"
timestamp_close: "<iso8601>"
```

All fields are required.

---

# 3. When Frames Open

A new frame opens when:

1. **first operator**  
2. **tier escalation** (r1 → r2, r2 → r3)  
3. **tier decrease** (measurement)  
4. **r3 operator**  
5. **meta operator**  
6. **drift overflow**  
7. **environment transition**  
8. **backend change**  

Router determines the trigger; Frame Manager enforces it.

---

# 4. When Frames Close

A frame closes when:

- a new frame opens  
- an environment transition occurs  
- session ends  
- archive is entered  

Closed frames are immutable.

---

# 5. Tier Semantics Inside Frames

Tier monotonicity:

```
r1 → r2 → r3 (allowed)
r3 → r2 → r1 (forbidden)
```

If a tier decrease is attempted:

- measurement forces a new frame  
- other decreases are illegal  

If illegal:

```
allowed: false
reason: "tier decrease inside frame"
```

---

# 6. Backend Semantics Inside Frames

Backend must remain consistent within a frame.

If backend changes:

- frame closes  
- new frame opens  

Backend changes occur due to:

- tier escalation  
- r3 operator  
- environment transition  

---

# 7. Drift Semantics Inside Frames

Drift accumulates monotonically:

```
drift_total = drift_prev + drift_measured
```

If drift exceeds environment bound:

- frame closes  
- new frame opens  
- operator routed into new frame  

Drift resets when:

- new frame opens  
- measurement occurs  
- meta operator occurs  
- r3 operator occurs  

---

# 8. Environment Semantics Inside Frames

Environment must remain consistent within a frame.

If environment changes:

- frame closes  
- new frame opens  
- drift resets  
- backend legality rechecked  

Environment transitions:

- sandbox → production (token required)  
- production → archive (token required)  
- archive → (forbidden)  

---

# 9. Operator Interaction

Operators appended to a frame must satisfy:

- grammar validity  
- argument validity  
- environment legality  
- backend legality  
- tier monotonicity  
- drift bounds  

Operators carry:

- tier  
- backend  
- drift  
- routing reason  

---

# 10. Capture Metadata

Each frame produces:

```
frame:
  frame_id: <int>
  environment: "<env>"
  backend: "<backend-id>"
  tier: "<tier>"
  drift:
    accumulated: <float>
    max: <float>
  operators: [op_ids...]
  timestamp_open: "<iso8601>"
  timestamp_close: "<iso8601>"
```

All fields are required.

---

# 11. Replay Reconstruction

Replay reconstructs frames by:

1. reading operator stream  
2. applying routing logic  
3. applying drift logic  
4. applying tier monotonicity  
5. applying backend legality  
6. applying environment transitions  
7. opening/closing frames deterministically  

Replay must confirm:

- frame boundaries match routing + drift logic  
- backend consistency  
- tier monotonicity  
- drift bounds  
- environment legality  
- hash chain integrity  

Replay is deterministic and read‑only.

---

# 12. Invariants

1. frames are append‑only  
2. frames are immutable after closure  
3. tier must not decrease inside a frame  
4. backend must remain consistent inside a frame  
5. drift must not exceed bound  
6. r3 always opens a new frame  
7. measurement always opens a new frame  
8. meta always opens a new frame  
9. environment transitions always open a new frame  
10. archive forbids all operators  

---

# 13. Summary

ResonanceFrames provide:

- structural segmentation  
- stability envelopes  
- deterministic boundaries  
- drift‑bounded execution  
- environment‑aware computation  
- replay‑verifiable correctness  

Frames are the **structural heartbeat** of qCompute.
# qCompute — Routing Engine  
**File:** qc_Router.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

The Routing Engine determines:

- backend selection  
- frame reuse vs. new frame  
- tier escalation  
- drift‑overflow routing  
- measurement routing  
- meta routing  
- environment legality  
- token requirements  

Routing is **deterministic**, **governed**, and **replay‑verifiable**.

qCompute computes **structure**, not amplitudes.

---

# 1. Purpose

Router receives a validated operator and decides:

1. **backend**  
2. **frame action** (`reuse` or `new`)  
3. **routing reason**  
4. **environment legality**  
5. **token requirements**  

Router emits routing metadata for capture and replay.

---

# 2. Routing Inputs

Router receives:

```
operator:
  name
  tier
  params

session:
  environment
  token_state
  current_frame

frame:
  tier
  backend
  drift_state

backend_profiles:
  legality
  tier_binding
  drift_envelope
```

All fields are required.

---

# 3. Backend Selection

Backend is determined by **tier binding**:

| Tier | Backend |
|------|----------|
| r1 | local-sim |
| r2 | hybrid-sim |
| r3 | hardware-qpu-2 |

Backend legality is checked against environment:

- sandbox: r1, r2  
- production: r1, r2, r3  
- archive: none  

If illegal:

```
allowed: false
reason: "backend illegal in environment"
```

---

# 4. Frame Reuse vs. New Frame

Router decides whether to reuse the current frame or open a new one.

### 4.1 Reuse Frame

Allowed when:

- tier does not escalate  
- drift does not overflow  
- operator is not measurement  
- operator is not meta  
- operator is not r3  
- environment does not change  

### 4.2 New Frame

Required when:

- **tier escalation** (r1 → r2, r2 → r3)  
- **tier decrease** (measurement)  
- **r3 operator**  
- **meta operator**  
- **drift overflow**  
- **environment transition**  
- **backend change**  

Router must always choose the **strongest trigger**.

---

# 5. Routing Reasons

Router emits one canonical reason:

- `"tier-binding"`  
- `"tier-escalation"`  
- `"tier-decrease"`  
- `"measurement"`  
- `"meta"`  
- `"r3-requires-new-frame"`  
- `"backend-change"`  
- `"environment-transition"`  
- `"drift-overflow"`  
- `"token-required"`  

Only one reason is emitted per operator.

---

# 6. Token Requirements

Token is required for:

- r3 operators  
- sandbox → production transition  
- production → archive transition  

If missing:

```
allowed: false
reason: "token required"
```

---

# 7. Routing Algorithm (Deterministic)

```
1. Determine backend from tier.
2. Check backend legality in environment.
3. Check token requirements.
4. Determine if tier escalates or decreases.
5. Check for measurement or meta operator.
6. Check drift overflow.
7. Check environment transition.
8. Decide frame_action = reuse | new.
9. Emit routing reason.
10. Emit routing metadata.
```

Router never uses heuristics.  
Router never uses randomness.

---

# 8. Routing Metadata (Capture)

Each operator produces:

```
routing:
  backend: "<backend-id>"
  frame_action: "reuse" | "new"
  reason: "<canonical-reason>"
```

Each frame produces:

```
frame_backend:
  id: "<backend-id>"
  tier_support: [...]
  drift_profile: "<low|medium|high>"
```

All fields are required.

---

# 9. Replay Verification

Replay recomputes routing:

- backend selection  
- frame boundaries  
- tier escalation  
- tier decrease  
- drift overflow  
- environment transitions  
- token requirements  

Replay must confirm:

- routing reason matches canonical logic  
- frame boundaries match routing logic  
- backend legality is preserved  
- environment legality is preserved  
- drift overflow is correct  
- token requirements are satisfied  

Replay is deterministic and read‑only.

---

# 10. Invariants

1. r1 → local-sim  
2. r2 → hybrid-sim  
3. r3 → hardware-qpu-2  
4. r3 always opens new frame  
5. measurement always opens new frame  
6. meta always opens new frame  
7. drift overflow always opens new frame  
8. tier may increase but never decrease within a frame  
9. environment transitions always open new frame  
10. archive forbids all operators  

---

# 11. Summary

Router provides:

- deterministic backend selection  
- deterministic frame boundaries  
- deterministic routing reasons  
- deterministic legality enforcement  

Router is the **structural decision engine** of qCompute.
# qCompute — Session Engine  
**File:** qc_Session.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

A **qSession** is the structural container for all qCompute activity.

It governs:

- environment  
- drift bound  
- backend legality  
- resonance frames  
- tokens  
- lineage  
- transitions  
- capture lifecycle  

qCompute computes **structure**, not amplitudes.

---

# 1. Purpose

The Session Engine:

- initializes structural context  
- manages environment  
- manages tokens  
- manages frames  
- manages drift envelope  
- orchestrates routing  
- orchestrates transitions  
- orchestrates capture  
- provides replay‑verifiable structure  

A session is the **root of structural truth**.

---

# 2. Session Identity

A session has:

```
session_id: "<uuid>"
environment: "sandbox" | "production" | "archive"
drift_bound: "<float>"
backend_legal: [...]
frames: []
lineage: ["sandbox", ...]
tokens: { deployed: [...] }
timestamp_open: "<iso8601>"
timestamp_close: "<iso8601>"
```

All fields are required.

---

# 3. Session Construction

```python
session = qSession(env="sandbox", backend="auto")
```

Arguments:

- `env`: `"sandbox" | "production" | "archive"`
- `backend`: `"auto"` or explicit backend ID

Defaults:

- environment = sandbox  
- backend = auto (tier‑bound)  

---

# 4. Environment Model

Environments define legality:

| Environment | Allowed Tiers | Drift Bound | Notes |
|-------------|---------------|-------------|-------|
| sandbox | r1, r2 | relaxed | development |
| production | r1, r2, r3 | strict | governed |
| archive | none | immutable | terminal |

Environment is updated only through transitions.

---

# 5. Token Model

Tokens are required for:

- sandbox → production  
- production → archive  
- r3 operators  

Deploy token:

```python
session.deploy_token("token-id")
```

Token state:

```
tokens:
  deployed: ["t1", "t2", ...]
```

---

# 6. Frame Model

A session contains **ResonanceFrames**.

Frame lifecycle:

- open on first operator  
- open on tier escalation  
- open on tier decrease  
- open on r3 operator  
- open on meta operator  
- open on drift overflow  
- open on environment transition  
- close when new frame opens  
- close when session ends  

Frames are append‑only and immutable after closure.

---

# 7. Drift Model

Session maintains drift envelope:

```
drift:
  accumulated: <float>
  bound: <float>
```

Drift resets when:

- new frame opens  
- measurement occurs  
- meta operator occurs  
- r3 operator occurs  
- environment transitions  

Drift must never exceed bound.

---

# 8. Operator Lifecycle

Operator flow inside a session:

```
operator → validator → router → frame manager → drift engine → capture
```

Session orchestrates:

- legality  
- routing  
- frame boundaries  
- drift accumulation  
- transition enforcement  
- capture ledger updates  

Operators are appended to the active frame.

---

# 9. Transition Lifecycle

Transitions are invoked via:

```python
session.transition("production")
session.transition("archive")
```

Transitions:

- require tokens  
- close current frame  
- update environment  
- reset drift  
- open new frame  
- update lineage  
- update backend legality  
- emit transition metadata  

Archive is terminal.

---

# 10. Capture Lifecycle

Save trace:

```python
session.save_trace("example.qtrace")
```

Capture writes:

- header  
- operator entries  
- frame summaries  
- transitions  
- footer  
- hash chain root  

Capture is append‑only and immutable.

---

# 11. Replay Integration

Replay reconstructs:

- session  
- frames  
- operators  
- transitions  
- drift  
- routing  
- backend legality  
- environment sequence  
- hash chain integrity  

Replay is deterministic and read‑only.

---

# 12. Invariants

1. environment must be legal  
2. backend must be legal  
3. drift must not exceed bound  
4. tier must not decrease inside a frame  
5. r3 requires token  
6. transitions require token  
7. transitions always open new frames  
8. archive is terminal  
9. capture must maintain valid hash chain  
10. frames are immutable after closure  

---

# 13. Summary

The Session Engine provides:

- structural context  
- environment governance  
- drift envelope  
- frame lifecycle  
- routing orchestration  
- transition orchestration  
- capture lifecycle  
- replay‑verifiable structure  

A session is the **governed container** for all qCompute computation.
# qCompute — Environment Transition Engine  
**File:** qc_Transitions.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

The Transition Engine governs movement between qCompute environments:

```
sandbox → production → archive
```

Transitions are **deterministic**, **token‑gated**, and **replay‑verifiable**.

qCompute computes **structure**, not amplitudes.

---

# 1. Purpose

The Transition Engine:

- validates environment transitions  
- enforces token requirements  
- closes the current frame  
- opens a new frame  
- updates drift bounds  
- updates backend legality  
- updates lineage  
- emits transition metadata for capture  
- verifies transitions during replay  

Transitions are structural governance events.

---

# 2. Environments

qCompute defines three environments:

| Environment | Description |
|-------------|-------------|
| **sandbox** | relaxed drift, r1/r2 allowed |
| **production** | strict drift, r1/r2/r3 allowed |
| **archive** | terminal, no operators allowed |

---

# 3. Legal Transitions

Only two transitions are legal:

```
sandbox → production
production → archive
```

All other transitions are illegal:

```
sandbox → archive      (forbidden)
production → sandbox   (forbidden)
archive → anything     (forbidden)
```

If illegal:

```
allowed: false
reason: "illegal transition"
```

---

# 4. Token Requirements

Transitions require tokens:

| Transition | Token Required |
|------------|----------------|
| sandbox → production | yes |
| production → archive | yes |
| archive → * | forbidden |

If token missing:

```
allowed: false
reason: "token required"
```

---

# 5. Transition Effects

A transition performs:

1. **close current frame**  
2. **update environment**  
3. **reset drift**  
4. **recompute backend legality**  
5. **open new frame**  
6. **append lineage entry**  
7. **emit transition metadata**  

Transitions always open a new frame.

---

# 6. Transition Metadata (Capture)

Each transition produces:

```
transition:
  from: "<env>"
  to: "<env>"
  token_used: "<token-id>"
  timestamp: "<iso8601>"
  hash_prev: "<sha256>"
  hash_self: "<sha256>"
```

All fields are required.

---

# 7. Routing Interaction

Router treats transitions as **strongest‑priority triggers**:

- always opens new frame  
- always resets drift  
- always rechecks backend legality  
- always updates environment  

Routing reason:

```
"environment-transition"
```

---

# 8. Drift Interaction

Transitions reset drift:

```
drift_total = 0
```

New drift bound is determined by the new environment:

| Environment | Drift Bound |
|-------------|-------------|
| sandbox | relaxed |
| production | strict |
| archive | immutable |

---

# 9. Backend Interaction

After transition:

- backend legality is rechecked  
- r3 becomes legal only in production  
- all backends become illegal in archive  

If backend becomes illegal:

- frame closes  
- new frame opens with legal backend  

---

# 10. Replay Verification

Replay reconstructs transitions by:

1. reading transition entries  
2. verifying legality  
3. verifying token usage  
4. verifying environment sequence  
5. verifying frame boundaries  
6. verifying drift resets  
7. verifying backend legality  
8. verifying hash chain integrity  

Replay must confirm:

- transitions match canonical rules  
- no illegal transitions occur  
- archive is terminal  

Replay is deterministic and read‑only.

---

# 11. Invariants

1. only sandbox → production → archive is legal  
2. transitions require tokens  
3. transitions always open new frames  
4. transitions reset drift  
5. transitions update backend legality  
6. transitions update environment  
7. archive forbids all operators  
8. archive is terminal  
9. hash chain must remain valid  

---

# 12. Summary

The Transition Engine provides:

- deterministic environment changes  
- token‑gated governance  
- drift resets  
- backend legality enforcement  
- frame segmentation  
- replay‑verifiable lineage  

Transitions are the **governance backbone** of qCompute.
# qCompute — Validator Engine  
**File:** qc_Validator.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

The Validator is the **legality gate** of qCompute.

Every operator, transition, and structural action must pass through the Validator before routing, framing, drift, or capture.

The Validator enforces:

- grammar correctness  
- argument correctness  
- environment legality  
- tier legality  
- backend legality  
- token requirements  
- archive terminality  
- transition legality  

qCompute computes **structure**, not amplitudes.

---

# 1. Purpose

The Validator ensures that all structural actions are:

- legal  
- deterministic  
- governed  
- replay‑verifiable  

If an operator is illegal, it is **captured but not executed**.

---

# 2. Validation Inputs

Validator receives:

```
operator:
  name
  tier
  params

session:
  environment
  tokens
  current_frame

backend_profiles:
  tier_binding
  environment_legal
```

All fields are required.

---

# 3. Validation Output

Validator returns:

```
allowed: true | false
reason: "<canonical-reason>"
```

Canonical reasons:

- "invalid grammar"
- "invalid arguments"
- "illegal in environment"
- "backend mismatch"
- "backend illegal in environment"
- "tier decrease inside frame"
- "token required"
- "archive terminal"
- "illegal transition"

No other strings are permitted.

---

# 4. Grammar Validation

Validator checks:

- operator name exists  
- operator belongs to a valid family  
- arguments match canonical schema  
- argument types are correct  

If invalid:

```
allowed: false
reason: "invalid grammar"
```

---

# 5. Argument Validation

Validator checks:

- required parameters present  
- parameter types correct  
- parameter ranges valid  

If invalid:

```
allowed: false
reason: "invalid arguments"
```

---

# 6. Environment Validation

Environment legality:

| Environment | Allowed Tiers |
|-------------|---------------|
| sandbox | r1, r2 |
| production | r1, r2, r3 |
| archive | none |

If operator is illegal in environment:

```
allowed: false
reason: "illegal in environment"
```

Archive always returns:

```
allowed: false
reason: "archive terminal"
```

---

# 7. Tier Validation

Validator checks:

- tier legality in environment  
- tier monotonicity inside frame  

Tier decrease inside a frame is illegal unless operator is measurement.

If illegal:

```
allowed: false
reason: "tier decrease inside frame"
```

---

# 8. Backend Validation

Backend is determined by tier:

| Tier | Backend |
|------|----------|
| r1 | local-sim |
| r2 | hybrid-sim |
| r3 | hardware-qpu-2 |

Validator checks:

- backend exists  
- backend legal in environment  

If illegal:

```
allowed: false
reason: "backend illegal in environment"
```

---

# 9. Token Validation

Tokens required for:

- r3 operators  
- sandbox → production transition  
- production → archive transition  

If missing:

```
allowed: false
reason: "token required"
```

---

# 10. Transition Validation

Legal transitions:

```
sandbox → production
production → archive
```

All others are illegal:

```
allowed: false
reason: "illegal transition"
```

Archive is terminal:

```
allowed: false
reason: "archive terminal"
```

---

# 11. Measurement Validation

Measurement forces:

- tier decrease  
- new frame  

Measurement is always legal unless environment is archive.

---

# 12. Meta Operator Validation

Meta operators (`barrier`, `flush`) are always legal unless environment is archive.

Meta operators always:

- open new frame  
- reset drift  

---

# 13. Drift Validation (Pre‑Routing)

Validator does **not** compute drift, but it checks:

- drift metadata exists  
- drift values are numeric  
- drift does not exceed impossible bounds  

Drift overflow is handled by Router + Frame Manager.

---

# 14. Capture Integration

Validator emits:

```
validation:
  allowed: true|false
  reason: "<canonical-reason>"
```

This metadata is required for every operator.

---

# 15. Replay Verification

Replay re‑validates:

- grammar  
- arguments  
- environment legality  
- tier legality  
- backend legality  
- token requirements  
- transition legality  
- archive terminality  

Replay must confirm:

- Validator decisions match canonical rules  
- no illegal operators were executed  
- illegal operators were captured correctly  

Replay is deterministic and read‑only.

---

# 16. Invariants

1. grammar must be valid  
2. arguments must be valid  
3. environment must allow tier  
4. backend must be legal  
5. r3 requires token  
6. transitions require token  
7. archive forbids all operators  
8. tier must not decrease inside a frame  
9. measurement is the only legal tier decrease  
10. meta operators always legal (except archive)  
11. illegal operators are captured but not executed  

---

# 17. Summary

The Validator ensures:

- structural legality  
- deterministic governance  
- environment correctness  
- backend correctness  
- tier correctness  
- token correctness  
- transition correctness  

Validator is the **first and strictest gate** of qCompute.
