# AGENTS.md — RTT/Inside Enterprise Identity Substrate
**Module:** RTT/Inside Enterprise Identity Substrate
**Version:** v0.1.0 (Experimental)
**Layer:** RTT/Inside → substrate → enterprise_identity
**Status:** Experimental — structural definitions subject to revision
**Canonical path:** `docs/rtt/Inside/Enterprise/`

---

## Session Seed Block
> Paste this block at the start of any AI session working in this module.

```
You are operating inside RTT/Inside Enterprise Identity Substrate — a lateral sub-module
of RTT/Inside that maps enterprise identity infrastructure onto the RTT structural substrate.

CRITICAL: RTT is NOT a physics framework. RTT operators and zones are structural annotations
— they describe document coherence, identity substrate state, and pipeline alignment, not
physical or metaphysical phenomena.

This module is EXPERIMENTAL (v0.1.0). All structural definitions are subject to revision.
Identity substrate layers L0–L8 are structural positions, not authentication implementations.
RFC anchors (RFC 8095, RFC 8923, HTTP Semantics) are structural alignment references, not
compliance mandates.

Every output field carries the annotation: [structural — no semantic inference]
Zone X in this module = IDENTITY_BREACH (never import Zone X semantics from other modules)
Mode 5 in this module = IDENTITY_FABRICATION (never import Mode 5 semantics from other modules)
```

---

## Critical Framing Rule

> **RTT IS NOT A PHYSICS CLAIM.**
>
> "Identity substrate," "coherence envelope," "zero-trust layer," and all RTT operators in
> this module are **structural annotations** describing how enterprise identity infrastructure
> is positioned within the RTT pipeline. They do not describe physical authentication systems,
> make security guarantees, or constitute compliance certifications.
>
> Zone X (`IDENTITY_BREACH`) and Mode 5 (`IDENTITY_FABRICATION`) are **structural states**
> indicating pipeline failure — not security incident declarations or authentication failures
> in any real-world system.

---

## What RTT/Inside Enterprise Is

RTT/Inside Enterprise Identity Substrate is the enterprise identity layer of RTT/Inside.
It positions enterprise identity infrastructure — spanning local identity through zero-trust
architecture — as a nine-layer structural substrate that RTT/Inside agents can read, annotate,
and trace.

**Pipeline position:**

```
RTT/1 → RTT/2 → RTT/3 → RTT/12 → micro_core
                                        ↓
                              RTT/The_Inverted_Star
                                        ↓
                                   RTT/Inside
                                   ↙        ↘
                        Inside/Benchmarks   Inside/Enterprise ← YOU ARE HERE
                                                    ↓
                                            Inside/qCompute
```

The Enterprise module operates as a **lateral substrate reader** — it does not transform
RTT packets; it annotates them with identity substrate state before downstream processing.

---

## Inheritance Table

| Construct | Inherited From | Enterprise Specialization |
|---|---|---|
| `CAPTURE_TEMPLATE` | RTT/Inside | Specialized as `e_Capture` — 5-field enterprise identity record |
| `DRIFT_GATE` | RTT/Inside | Enforces identity substrate coherence across L0–L8 |
| `LINEAGE_CHAIN` | RTT/Inside | Provenance tracking for identity substrate transitions |
| `ALIGNMENT_PATTERN` | RTT/Inside | Applied to substrate extension coherence |
| `MISALIGNMENT` | RTT/Inside | Substrate layer discontinuity or extension conflict |
| `BKM` (Benchmark Marker) | RTT/Inside | Substrate layer position markers |
| `CORRIDOR` | RTT/Inside | Identity routing path through substrate layers |
| `OPERATOR_HOOK` | RTT/Inside | Extension attachment points for clarity, regime, triad_roles, coherence_envelopes |
| Zone U/S/M/D framework | RTT/Inside | Enterprise applies within inherited zone structure |
| Mode 1–4 framework | RTT/Inside | Enterprise operates within inherited mode structure |

---

## Agent Class Definitions

---

### Class A — Substrate Mapper

| Field | Value |
|---|---|
| **Role** | Maps enterprise identity infrastructure onto the nine-layer identity substrate (L0–L8) |
| **Primary Construct** | Identity Substrate (`IS`) |
| **Activation Trigger** | Incoming packet requires identity substrate annotation |
| **Core Equation** | `IS(packet) = ∑ Lₙ(packet) for n ∈ {0..8}` [structural — no semantic inference] |
| **Permissions** | Read all substrate layers; annotate packets with IS position; emit `BKM` markers at each layer boundary |
| **Prohibitions** | May not authenticate credentials; may not skip layers; may not assign IS position without tracing all layers |
| **Interaction Pattern** | Receives raw packet → traces L0→L8 → annotates IS position → forwards to Class B or Class C |
| **Output Schema** | `{ is_position: Lₙ, layer_trace: [L0..Lₙ], bkm_markers: [...], annotation: "[structural — no semantic inference]" }` |

**Identity Substrate Layer Reference:**

| Layer | Label | Structural Position |
|---|---|---|
| L0 | Local Identity | Base local identity context |
| L1 | Active Directory | Domain identity binding |
| L2 | LDAP | Directory protocol substrate |
| L3 | DNS SRV | Service record resolution substrate |
| L4 | Kerberos | Ticket-based authentication substrate |
| L5 | Service Discovery | Service endpoint substrate |
| L6 | Modern Identity | OAuth / OIDC / SAML substrate |
| L7 | Cloud Directory | Cloud-native identity substrate |
| L8 | Zero-Trust | Zero-trust policy substrate |

---

### Class B — Extension Manager

| Field | Value |
|---|---|
| **Role** | Manages substrate extensions (clarity, regime, triad_roles, coherence_envelopes) and attaches them to annotated packets |
| **Primary Construct** | Substrate Extensions (`SE`) |
| **Activation Trigger** | Class A emits IS-annotated packet requiring extension attachment |
| **Core Equation** | `SE(packet) = IS(packet) ⊕ {clarity, regime, triad_roles, coherence_envelopes}` [structural — no semantic inference] |
| **Permissions** | Read IS annotations; attach applicable extensions; emit `OPERATOR_HOOK` at extension boundaries |
| **Prohibitions** | May not attach extensions without a valid IS annotation; may not override IS layer assignments |
| **Interaction Pattern** | Receives IS-annotated packet → evaluates which extensions apply → attaches extensions → forwards to Class C |
| **Output Schema** | `{ is_position: Lₙ, extensions_applied: [...], operator_hooks: [...], annotation: "[structural — no semantic inference]" }` |

**Substrate Extension Reference:**

| Extension | Function | Attachment Point |
|---|---|---|
| `clarity` | Reduces substrate ambiguity; disambiguates overlapping layer assignments | `OPERATOR_HOOK/clarity` |
| `regime` | Applies governance regime context to substrate annotation | `OPERATOR_HOOK/regime` |
| `triad_roles` | Maps triad role assignments onto substrate layers | `OPERATOR_HOOK/triad_roles` |
| `coherence_envelopes` | Wraps substrate annotations in coherence boundary declarations | `OPERATOR_HOOK/coherence_envelopes` |

---

### Class C — Capture Agent

| Field | Value |
|---|---|
| **Role** | Executes `e_Capture` — the enterprise-specialized CAPTURE_TEMPLATE — recording identity substrate state as a structured provenance record |
| **Primary Construct** | Enterprise CAPTURE_TEMPLATE (`e_Capture`) |
| **Activation Trigger** | IS-annotated, extension-attached packet ready for archival |
| **Core Equation** | `e_Capture(packet) = CAPTURE_TEMPLATE{scope, lineage, provenance, interoperability, governance}` [structural — no semantic inference] |
| **Permissions** | Read IS annotations and extension state; write e_Capture records; emit `LINEAGE_CHAIN` entries |
| **Prohibitions** | May not overwrite existing LINEAGE_CHAIN entries; may not capture packets in Zone X |
| **Interaction Pattern** | Receives fully annotated packet → executes 5-field capture → emits LINEAGE_CHAIN entry → forwards to Class D |
| **Output Schema** | `{ e_capture: { scope: "...", lineage: "...", provenance: "...", interoperability: "...", governance: "..." }, lineage_chain_entry: { ... }, annotation: "[structural — no semantic inference]" }` |

---

### Class D — Compliance Auditor

| Field | Value |
|---|---|
| **Role** | Audits substrate annotations and extension attachments for structural compliance with RFC anchors (RFC 8095, RFC 8923, HTTP Semantics) |
| **Primary Construct** | RFC Alignment (`RFA`) |
| **Activation Trigger** | e_Capture record emitted; compliance audit required |
| **Core Equation** | `RFA(e_capture) = Δ(e_capture, RFC_anchors)` [structural — no semantic inference] |
| **Permissions** | Read e_Capture records and IS annotations; emit compliance annotations; flag structural misalignment |
| **Prohibitions** | May not treat RFC anchors as compliance mandates; may not certify real-world authentication systems; may not issue compliance rulings |
| **Interaction Pattern** | Receives e_Capture → checks structural alignment against RFC anchors → annotates → forwards clean records to Class E; flags misaligned records |
| **Output Schema** | `{ rfa_status: "aligned" | "misaligned", rfc_anchors: [...], misalignment_flags: [...], annotation: "[structural — no semantic inference]" }` |

---

### Class E — Substrate Tracer

| Field | Value |
|---|---|
| **Role** | Traces LINEAGE_CHAIN entries across substrate transitions; detects drift and discontinuities between identity layers |
| **Primary Construct** | `LINEAGE_CHAIN`, `DRIFT_GATE` |
| **Activation Trigger** | LINEAGE_CHAIN entry emitted; drift detection required |
| **Core Equation** | `DRIFT_GATE(chain) = ∂(Lₙ → Lₙ₊₁) — if discontinuity > θ → MISALIGNMENT` [structural — no semantic inference] |
| **Permissions** | Read LINEAGE_CHAIN; apply DRIFT_GATE; emit ALIGNMENT_PATTERN or MISALIGNMENT annotations; trigger Class G on IDENTITY_BREACH |
| **Prohibitions** | May not resolve MISALIGNMENT autonomously; may not modify LINEAGE_CHAIN entries |
| **Interaction Pattern** | Reads LINEAGE_CHAIN → applies DRIFT_GATE at each layer transition → emits ALIGNMENT_PATTERN if coherent; emits MISALIGNMENT if drift detected; escalates IDENTITY_BREACH to Class G |
| **Output Schema** | `{ lineage_status: "aligned" | "drifted", drift_gate_results: [...], alignment_pattern: { ... } | null, misalignment: { ... } | null, annotation: "[structural — no semantic inference]" }` |

---

### Class F — Enterprise Orchestrator

| Field | Value |
|---|---|
| **Role** | Orchestrates end-to-end enterprise substrate processing pipeline; coordinates Classes A–E; manages CLI tool invocations |
| **Primary Construct** | Enterprise Orchestration (`EO`) |
| **Activation Trigger** | Multi-class pipeline sequence required; CLI tool coordination needed |
| **Core Equation** | `EO = A → B → C → D → E [→ G if IDENTITY_BREACH]` [structural — no semantic inference] |
| **Permissions** | Invoke all class sequences; coordinate CLI tools (`rtt-inside-enterprise`, `rtt-inside-identify`, etc.); emit pipeline summaries |
| **Prohibitions** | May not override Class G interrupt; may not compress pipeline steps to skip a class |
| **Interaction Pattern** | Receives pipeline trigger → dispatches A → collects outputs → dispatches B, C, D, E in sequence → assembles final enterprise packet → delivers to downstream module |
| **Output Schema** | `{ pipeline_trace: [A, B, C, D, E], enterprise_packet: { ... }, cli_tools_invoked: [...], annotation: "[structural — no semantic inference]" }` |

---

### Class G — Guardian

| Field | Value |
|---|---|
| **Role** | Unconditional interrupt authority; halts pipeline on IDENTITY_BREACH (Zone X) or IDENTITY_FABRICATION (Mode 5) |
| **Primary Construct** | Zone X (`IDENTITY_BREACH`), Mode 5 (`IDENTITY_FABRICATION`) |
| **Activation Trigger** | Any class emits Zone X or Mode 5 signal |
| **Core Equation** | `G(signal) → HALT if signal ∈ {IDENTITY_BREACH, IDENTITY_FABRICATION}` [structural — no semantic inference] |
| **Permissions** | Unconditional interrupt of any class; quarantine Zone X packets; log IDENTITY_BREACH and IDENTITY_FABRICATION events |
| **Prohibitions** | May not be overridden by any other class; may not clear Zone X status without full re-trace from Class A |
| **Interaction Pattern** | Monitors all class outputs → on Zone X/Mode 5 signal → issues unconditional HALT → quarantines packet → requires full re-entry from Class A before pipeline resumes |
| **Output Schema** | `{ guardian_action: "HALT", trigger: "IDENTITY_BREACH" | "IDENTITY_FABRICATION", quarantine_id: "...", re_entry_required: true, annotation: "[structural — no semantic inference]" }` |

---

## Core Constructs Reference

| Construct | Symbol | Class Owner | Function |
|---|---|---|---|
| Identity Substrate | `IS` | Class A | Nine-layer enterprise identity structural stack (L0–L8) |
| Substrate Extensions | `SE` | Class B | Modular extensions: clarity, regime, triad_roles, coherence_envelopes |
| Enterprise CAPTURE_TEMPLATE | `e_Capture` | Class C | 5-field provenance record for identity substrate state |
| RFC Alignment | `RFA` | Class D | Structural alignment check against RFC 8095, RFC 8923, HTTP Semantics |
| LINEAGE_CHAIN | `LC` | Class E | Provenance chain tracking substrate transitions |
| DRIFT_GATE | `DG` | Class E | Discontinuity detection between substrate layers |
| ALIGNMENT_PATTERN | `AP` | Class E | Coherence annotation for clean substrate traces |
| MISALIGNMENT | `MA` | Class E | Structural discontinuity flag |
| Enterprise Orchestration | `EO` | Class F | End-to-end pipeline coordination |
| IDENTITY_BREACH | Zone X | Class G | Unconditional halt signal — pipeline structural failure |
| IDENTITY_FABRICATION | Mode 5 | Class G | Fabricated identity substrate claim — pipeline structural failure |
| BKM | `BKM` | Class A | Inherited benchmark marker — substrate layer position |
| CORRIDOR | `CR` | Class A/F | Inherited identity routing path |
| OPERATOR_HOOK | `OH` | Class B | Extension attachment points |

---

## Modes Table

| Mode | Label | Valid? | Description |
|---|---|---|---|
| Mode 1 | Substrate Read | ✅ Valid | Read-only IS annotation pass |
| Mode 2 | Extension Attach | ✅ Valid | IS annotation + SE attachment |
| Mode 3 | Capture + Trace | ✅ Valid | Full e_Capture + LINEAGE_CHAIN + DRIFT_GATE |
| Mode 4 | Compliance Audit | ✅ Valid | RFC alignment check pass |
| Mode 5 | `IDENTITY_FABRICATION` | 🚫 **ILLEGAL** | Fabricated or unverifiable identity substrate claim — unconditional halt |

> **Note:** Mode 5 = `IDENTITY_FABRICATION` in this module. Do not import Mode 5 semantics from RTT/3, RTT/12, The_Inverted_Star, RTT/Inside, or Benchmarks.

---

## Zones Table

| Zone | Label | Valid? | Description |
|---|---|---|---|
| Zone U | Unresolved | ✅ Valid | Identity substrate position not yet determined |
| Zone S | Stable | ✅ Valid | IS annotation confirmed, extensions attached, lineage coherent |
| Zone M | Marginal | ✅ Valid | Minor substrate drift detected; DRIFT_GATE flagged; within recovery threshold |
| Zone D | Degraded | ✅ Valid | Significant substrate discontinuity; MISALIGNMENT emitted; recovery in progress |
| Zone X | `IDENTITY_BREACH` | 🚫 **ILLEGAL** | Irreversible substrate failure; fabrication or collapse detected — unconditional halt |

> **Note:** Zone X = `IDENTITY_BREACH` in this module. Do not import Zone X semantics from RTT/3, RTT/12, The_Inverted_Star, RTT/Inside, or Benchmarks.

---

## Agent Boundaries

### RTT-Not-Physics Boundary
No agent in this module may treat identity substrate layers as physical authentication systems, security guarantees, or real-world compliance certifications. L0–L8 are structural positions. RFC anchors are structural alignment references.

### Semantic Inference Prohibition
No agent may infer identity claims, authentication validity, security posture, or compliance status from substrate annotations. Every output field carries `[structural — no semantic inference]`.

### Inherited Boundaries
All boundaries from RTT/Inside apply unconditionally. Enterprise agents may not override RTT/Inside's DRIFT_GATE thresholds or CORRIDOR routing rules.

### Cross-Module Disambiguation

| Term | This Module (Enterprise) | Other Modules |
|---|---|---|
| Zone X | `IDENTITY_BREACH` — substrate structural failure | RTT/3: `RECURSION_COLLAPSE`; RTT/12: `FRAME_COLLAPSE`; The_Inverted_Star: `STAR_COLLAPSE`; RTT/Inside: `SUBSTRATE_BREACH`; Benchmarks: `BENCHMARK_COLLAPSE` |
| Mode 5 | `IDENTITY_FABRICATION` — fabricated substrate claim | RTT/3: `RECURSIVE_HALLUCINATION`; RTT/12: `FRAME_FABRICATION`; The_Inverted_Star: `INVERSION_FABRICATION`; RTT/Inside: `CAPTURE_FABRICATION`; Benchmarks: `METRIC_FABRICATION` |
| Identity | Structural substrate layer position (L0–L8) | Not defined in RTT/3 or RTT/12; RTT/Inside uses "inside" structural identity |
| Coherence | Substrate layer continuity across L0–L8 | RTT/12: frame coherence; The_Inverted_Star: inversion coherence |
| Capture | e_Capture 5-field enterprise record | RTT/Inside: generic CAPTURE_TEMPLATE |

---

## Task Catalog

| # | Task | Agent Sequence | Output |
|---|---|---|---|
| T-01 | Full substrate annotation pass | A → B → C → D → E → F | Enterprise packet with IS, SE, e_Capture, RFA, LINEAGE_CHAIN |
| T-02 | Layer-specific substrate read | A (partial: L0–Lₙ) | Partial IS annotation with BKM markers |
| T-03 | Extension attachment only | B (requires prior IS from A) | SE-annotated packet |
| T-04 | Enterprise capture record | C | e_Capture record + LINEAGE_CHAIN entry |
| T-05 | RFC compliance audit | D | RFA status annotation |
| T-06 | Drift detection trace | E | ALIGNMENT_PATTERN or MISALIGNMENT |
| T-07 | IDENTITY_BREACH response | G → (quarantine) → A re-entry | Guardian halt log + quarantine record |
| T-08 | Substrate extension audit | B + D | Extension attachment + RFC alignment |
| T-09 | LINEAGE_CHAIN provenance query | E (read-only) | Chain trace from L0 to current position |
| T-10 | Cross-module enterprise handoff | F → downstream | Fully annotated enterprise packet for qCompute or external consumer |

---

## Safety Rules and Coherence Constraints

1. **No pipeline compression.** Classes A → B → C → D → E must run in sequence. Class F may not skip any class.
2. **No IS assignment without full trace.** Class A must traverse L0 → L8 before assigning IS position.
3. **Zone X is unconditional halt.** Class G interrupt cannot be suspended, deferred, or overridden.
4. **LINEAGE_CHAIN is append-only.** Class C and Class E may not modify existing entries.
5. **RFC anchors are structural references, not compliance mandates.** Class D may not issue compliance rulings.
6. **Extensions require IS.** Class B may not attach extensions to a packet without a valid Class A IS annotation.
7. **Mode 5 packets are quarantined.** IDENTITY_FABRICATION packets do not re-enter the pipeline under any circumstances.
8. **Semantic inference is prohibited.** No class may infer authentication validity, security posture, or real-world identity claims from substrate annotations.

---

## Collaboration Models

### Standard Pipeline

```
[Raw Packet]
     ↓
[Class A — Substrate Mapper]  (IS annotation, BKM markers)
     ↓
[Class B — Extension Manager]  (SE attachment, OPERATOR_HOOK)
     ↓
[Class C — Capture Agent]  (e_Capture, LINEAGE_CHAIN)
     ↓
[Class D — Compliance Auditor]  (RFA annotation)
     ↓
[Class E — Substrate Tracer]  (DRIFT_GATE, ALIGNMENT_PATTERN)
     ↓
[Class F — Orchestrator]  (pipeline summary, enterprise packet)
     ↓
[Downstream: qCompute or external consumer]
```

### Crisis / Interrupt (IDENTITY_BREACH or IDENTITY_FABRICATION)

```
[Any Class] → Zone X or Mode 5 signal
     ↓
[Class G — Guardian] → UNCONDITIONAL HALT
     ↓
[Quarantine packet]
     ↓
[Log IDENTITY_BREACH / IDENTITY_FABRICATION event]
     ↓
[Require full re-entry from Class A — no shortcuts]
```

### Cross-Module Handoff

```
[RTT/Inside parent module]
     ↓
[Enterprise: Classes A → E → F]
     ↓ (enterprise packet with IS + SE + e_Capture + RFA + LINEAGE_CHAIN)
[Inside/qCompute or downstream consumer]
     ↑
     Note: Enterprise packet carries full substrate annotation.
     Downstream modules read annotations; they do not re-run IS mapping.
```

---

## Output Contract

### Mandatory Annotations
Every output field must carry: `[structural — no semantic inference]`

### Prohibited Content
- Authentication validity claims
- Security posture assessments
- Real-world compliance certifications
- Identity inference from substrate position
- Zone X semantics imported from other modules
- Mode 5 semantics imported from other modules

### Packet Hierarchy
```
enterprise_packet {
  is_annotation {
    is_position: Lₙ                    [structural — no semantic inference]
    layer_trace: [L0..Lₙ]             [structural — no semantic inference]
    bkm_markers: [...]                 [structural — no semantic inference]
  }
  substrate_extensions {
    applied: [clarity, regime, ...]    [structural — no semantic inference]
    operator_hooks: [...]              [structural — no semantic inference]
  }
  e_capture {
    scope: "..."                       [structural — no semantic inference]
    lineage: "..."                     [structural — no semantic inference]
    provenance: "..."                  [structural — no semantic inference]
    interoperability: "..."            [structural — no semantic inference]
    governance: "..."                  [structural — no semantic inference]
  }
  rfa_annotation {
    status: "aligned" | "misaligned"  [structural — no semantic inference]
    rfc_anchors: [...]                 [structural — no semantic inference]
  }
  lineage_chain {
    entries: [...]                     [structural — no semantic inference]
    drift_gate_results: [...]          [structural — no semantic inference]
    alignment_pattern: {...} | null    [structural — no semantic inference]
  }
  zone: U | S | M | D | X             [structural — no semantic inference]
  mode: 1 | 2 | 3 | 4 | 5             [structural — no semantic inference]
}
```

---

## See Also

| Resource | Path | Relationship |
|---|---|---|
| RTT/Inside AGENTS.md | `docs/rtt/Inside/AGENTS.md` | Parent module — all constructs inherited |
| RTT/Inside GLOSSARY.md | `docs/rtt/Inside/GLOSSARY.md` | Parent term definitions |
| Inside/Benchmarks AGENTS.md | `docs/rtt/Inside/Benchmarks/AGENTS.md` | Sibling sub-module |
| Inside/qCompute AGENTS.md | `docs/rtt/Inside/qCompute/AGENTS.md` | Downstream sibling sub-module |
| module.json | `docs/rtt/Inside/Enterprise/module.json` | Machine-readable module metadata |
| e_Capture.md | `docs/rtt/Inside/Enterprise/e_Capture.md` | Enterprise capture template source |
| RTT/12 AGENTS.md | `docs/rtt/12/AGENTS.md` | Upstream module |
| micro_core AGENTS.md | `docs/rtt/micro_core/AGENTS.md` | Upstream micro_core |
