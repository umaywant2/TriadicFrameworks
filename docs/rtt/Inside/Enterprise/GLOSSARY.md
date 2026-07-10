# GLOSSARY.md — RTT/Inside Enterprise Identity Substrate
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

CRITICAL: RTT is NOT a physics framework. All terms in this glossary are structural
annotations — they describe document coherence, identity substrate state, and pipeline
alignment, not physical or metaphysical phenomena.

This module is EXPERIMENTAL (v0.1.0). All term definitions are subject to revision.
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
> Every term in this glossary is a **structural annotation** — a label for a position,
> state, or transition within the RTT/Inside Enterprise pipeline. No term describes a
> physical authentication system, a security mechanism, or a real-world identity service.
>
> Terms such as "identity substrate," "zero-trust layer," "coherence envelope," and
> "identity breach" are **pipeline structural states**, not security incident categories,
> authentication outcomes, or compliance findings.

---

## Inheritance Note

All terms from RTT/Inside are inherited by this module. Terms defined here either:
1. **Specialize** an RTT/Inside term for enterprise identity context (e.g., `e_Capture` specializes `CAPTURE_TEMPLATE`), or
2. **Introduce** enterprise-native constructs not present in the parent module (e.g., `Identity Substrate`, `Substrate Extensions`).

When a term is inherited without specialization, refer to `docs/rtt/Inside/GLOSSARY.md` for the canonical definition.

---

## Term Definitions (Alphabetical)

---

### Active Directory Substrate (L1)

| Field | Value |
|---|---|
| **Type** | Identity Substrate Layer |
| **Symbol** | `L1` |
| **Layer** | Identity Substrate — Layer 1 |
| **Agent** | Class A (Substrate Mapper) |
| **Annotation** | `[structural — no semantic inference]` |

**Definition:** The structural position within the Identity Substrate corresponding to Active Directory domain identity binding. L1 is the first external identity layer above local identity (L0). In the RTT/Inside Enterprise pipeline, L1 is a substrate position — not an implementation of Active Directory.

**Constraints:** L1 cannot be assigned without first resolving L0. L1 does not imply AD authentication; it marks structural position only.

**Inheritance source:** Enterprise-native (not present in RTT/Inside parent).

**Cross-references:** Identity Substrate (IS), Local Identity Substrate (L0), LDAP Substrate (L2).

**Disambiguation:** L1 in this module = AD domain identity structural position. Not a recursion depth (RTT/3), frame index (RTT/12), or benchmark tier (Benchmarks).

---

### Alignment Pattern (AP)

| Field | Value |
|---|---|
| **Type** | Coherence Annotation |
| **Symbol** | `AP` |
| **Layer** | Pipeline — LINEAGE_CHAIN output |
| **Agent** | Class E (Substrate Tracer) |
| **Annotation** | `[structural — no semantic inference]` |

**Definition:** A coherence annotation emitted by Class E (Substrate Tracer) when the DRIFT_GATE pass confirms that all substrate layer transitions (Lₙ → Lₙ₊₁) are within acceptable discontinuity thresholds. An Alignment Pattern indicates structural continuity across the identity substrate trace.

**Constraints:** AP is emitted only after a complete DRIFT_GATE pass. AP does not certify authentication validity or security coherence — it certifies structural substrate continuity.

**Inheritance source:** Inherited from RTT/Inside; applied specifically to identity substrate traces in this module.

**Cross-references:** DRIFT_GATE, LINEAGE_CHAIN, MISALIGNMENT, Class E.

---

### BKM (Benchmark Marker)

| Field | Value |
|---|---|
| **Type** | Position Marker |
| **Symbol** | `BKM` |
| **Layer** | Identity Substrate — Layer boundaries |
| **Agent** | Class A (Substrate Mapper) |
| **Annotation** | `[structural — no semantic inference]` |

**Definition:** Inherited from RTT/Inside. In the Enterprise module, BKM markers are emitted by Class A at each substrate layer boundary (L0/L1 boundary, L1/L2 boundary, etc.) during the IS annotation pass. BKM markers serve as structural waypoints in the layer trace.

**Constraints:** BKM markers are position annotations only — they do not authenticate layer assignments or confirm infrastructure presence.

**Inheritance source:** RTT/Inside (inherited without specialization).

**Cross-references:** Identity Substrate (IS), Class A, CORRIDOR.

---

### Clarity (Substrate Extension)

| Field | Value |
|---|---|
| **Type** | Substrate Extension |
| **Symbol** | `SE/clarity` |
| **Layer** | Substrate Extensions |
| **Agent** | Class B (Extension Manager) |
| **Annotation** | `[structural — no semantic inference]` |

**Definition:** A substrate extension that reduces ambiguity in substrate layer assignments. When a packet's IS annotation has overlapping or indeterminate layer assignments (e.g., a service that spans L2 and L3), the clarity extension disambiguates the assignment and selects the most structurally coherent layer position.

**Constraints:** Clarity may only be applied after a valid IS annotation from Class A. Clarity does not invent layer assignments — it resolves ambiguity between existing candidates.

**Inheritance source:** Enterprise-native substrate extension (not present in RTT/Inside parent).

**Cross-references:** Substrate Extensions (SE), Class B, OPERATOR_HOOK/clarity, Regime.

---

### Cloud Directory Substrate (L7)

| Field | Value |
|---|---|
| **Type** | Identity Substrate Layer |
| **Symbol** | `L7` |
| **Layer** | Identity Substrate — Layer 7 |
| **Agent** | Class A (Substrate Mapper) |
| **Annotation** | `[structural — no semantic inference]` |

**Definition:** The structural position within the Identity Substrate corresponding to cloud-native identity directory services (e.g., Entra ID, Okta, Google Workspace directory). L7 represents the cloud directory structural substrate — above modern identity federation (L6) and below zero-trust policy (L8).

**Constraints:** L7 assignment requires L6 to be resolved. L7 is a structural position, not a specific cloud provider reference.

**Inheritance source:** Enterprise-native.

**Cross-references:** Identity Substrate (IS), Modern Identity Substrate (L6), Zero-Trust Substrate (L8).

---

### Coherence Envelopes (Substrate Extension)

| Field | Value |
|---|---|
| **Type** | Substrate Extension |
| **Symbol** | `SE/coherence_envelopes` |
| **Layer** | Substrate Extensions |
| **Agent** | Class B (Extension Manager) |
| **Annotation** | `[structural — no semantic inference]` |

**Definition:** A substrate extension that wraps IS annotations in coherence boundary declarations. A coherence envelope specifies the boundaries within which the IS annotation is structurally valid — for example, declaring that an L4 (Kerberos) annotation is coherent within a specific domain boundary but not across trust boundaries.

**Constraints:** Coherence envelopes are structural declarations — they do not enforce authentication boundaries in any real system. They annotate the structural scope of an IS assignment.

**Inheritance source:** Enterprise-native substrate extension.

**Cross-references:** Substrate Extensions (SE), Class B, OPERATOR_HOOK/coherence_envelopes, Clarity, Regime.

**Disambiguation:** Not the same as "coherence" in RTT/12 (frame coherence) or The_Inverted_Star (inversion coherence). Enterprise coherence envelopes are identity substrate boundary annotations.

---

### CORRIDOR

| Field | Value |
|---|---|
| **Type** | Routing Construct |
| **Symbol** | `CR` |
| **Layer** | Pipeline — identity routing |
| **Agent** | Class A, Class F |
| **Annotation** | `[structural — no semantic inference]` |

**Definition:** Inherited from RTT/Inside. In the Enterprise module, a CORRIDOR is the structural routing path that a packet follows through the identity substrate layers. A CORRIDOR defines which layers (Lₙ) the packet traverses and in what order during the IS annotation pass.

**Constraints:** CORRIDOR routing does not authenticate packets — it defines structural traversal paths. CORRIDOR may not skip required substrate layers.

**Inheritance source:** RTT/Inside (inherited without specialization).

**Cross-references:** Identity Substrate (IS), BKM, Class A, Class F.

---

### DNS SRV Substrate (L3)

| Field | Value |
|---|---|
| **Type** | Identity Substrate Layer |
| **Symbol** | `L3` |
| **Layer** | Identity Substrate — Layer 3 |
| **Agent** | Class A (Substrate Mapper) |
| **Annotation** | `[structural — no semantic inference]` |

**Definition:** The structural position within the Identity Substrate corresponding to DNS service record resolution. L3 represents the service location substrate — the structural layer at which identity infrastructure is located via DNS SRV records before protocol-level binding occurs.

**Constraints:** L3 assignment requires L2 to be resolved. L3 is a structural position, not a DNS lookup implementation.

**Inheritance source:** Enterprise-native.

**Cross-references:** Identity Substrate (IS), LDAP Substrate (L2), Kerberos Substrate (L4).

---

### DRIFT_GATE (DG)

| Field | Value |
|---|---|
| **Type** | Discontinuity Detector |
| **Symbol** | `DG` |
| **Layer** | LINEAGE_CHAIN — layer transition |
| **Agent** | Class E (Substrate Tracer) |
| **Annotation** | `[structural — no semantic inference]` |

**Definition:** A gate applied by Class E at each substrate layer transition (Lₙ → Lₙ₊₁) within the LINEAGE_CHAIN. The DRIFT_GATE measures structural discontinuity between adjacent layers. If discontinuity exceeds threshold θ, the DRIFT_GATE emits a MISALIGNMENT annotation. If all transitions are within threshold, an ALIGNMENT_PATTERN is emitted.

**Equation:** `DRIFT_GATE(chain) = ∂(Lₙ → Lₙ₊₁) — if discontinuity > θ → MISALIGNMENT` `[structural — no semantic inference]`

**Constraints:** DRIFT_GATE is applied to LINEAGE_CHAIN entries — not to real-time identity traffic. DRIFT_GATE results are structural annotations, not security alerts.

**Inheritance source:** Inherited from RTT/Inside; specialized for identity substrate layer transitions.

**Cross-references:** LINEAGE_CHAIN, ALIGNMENT_PATTERN, MISALIGNMENT, Class E, Zone M, Zone D.

---

### e_Capture (Enterprise CAPTURE_TEMPLATE)

| Field | Value |
|---|---|
| **Type** | Capture Record |
| **Symbol** | `e_Capture` |
| **Layer** | Pipeline — provenance record |
| **Agent** | Class C (Capture Agent) |
| **Annotation** | `[structural — no semantic inference]` |

**Definition:** The enterprise-specialized form of the RTT/Inside CAPTURE_TEMPLATE. e_Capture records identity substrate state across five fields: scope, lineage, provenance, interoperability, and governance. It is the primary provenance artifact emitted by the Enterprise module.

**Structure:**
```
e_Capture {
  scope:            "..."  [structural — no semantic inference]
  lineage:          "..."  [structural — no semantic inference]
  provenance:       "..."  [structural — no semantic inference]
  interoperability: "..."  [structural — no semantic inference]
  governance:       "..."  [structural — no semantic inference]
}
```

**Constraints:** e_Capture may not be written for packets in Zone X (IDENTITY_BREACH). e_Capture fields are structural annotations — they do not constitute compliance records or audit logs.

**Inheritance source:** Specializes CAPTURE_TEMPLATE from RTT/Inside.

**Cross-references:** CAPTURE_TEMPLATE (RTT/Inside), LINEAGE_CHAIN, Class C, Scope, Lineage, Provenance, Interoperability, Governance.

---

### Enterprise Orchestration (EO)

| Field | Value |
|---|---|
| **Type** | Pipeline Coordination Construct |
| **Symbol** | `EO` |
| **Layer** | Pipeline — top-level coordination |
| **Agent** | Class F (Enterprise Orchestrator) |
| **Annotation** | `[structural — no semantic inference]` |

**Definition:** The end-to-end pipeline coordination construct managed by Class F. Enterprise Orchestration sequences Classes A → B → C → D → E, aggregates their outputs into a unified enterprise packet, and manages CLI tool invocations. EO does not compress or skip pipeline steps.

**Equation:** `EO = A → B → C → D → E [→ G if IDENTITY_BREACH]` `[structural — no semantic inference]`

**Constraints:** EO may not override Class G interrupt authority. EO may not skip any class in the standard pipeline sequence.

**Inheritance source:** Enterprise-native.

**Cross-references:** Class F, Class G, Identity Substrate (IS), Substrate Extensions (SE), e_Capture, RFC Alignment (RFA), LINEAGE_CHAIN.

---

### Governance (e_Capture field)

| Field | Value |
|---|---|
| **Type** | e_Capture Field |
| **Symbol** | `e_Capture.governance` |
| **Layer** | e_Capture record |
| **Agent** | Class C (Capture Agent) |
| **Annotation** | `[structural — no semantic inference]` |

**Definition:** The fifth field of the e_Capture record. Governance captures the structural governance context of the identity substrate state — which regime, policy framework, or triad role assignment governs the annotated substrate position. Governance is a structural annotation, not a policy enforcement declaration.

**Constraints:** Governance field may not claim policy enforcement authority. It annotates structural governance context only.

**Inheritance source:** Specializes the governance concept from RTT/Inside CAPTURE_TEMPLATE.

**Cross-references:** e_Capture, Regime (substrate extension), Triad Roles (substrate extension), Class C.

---

### HTTP Semantics (RFC Anchor)

| Field | Value |
|---|---|
| **Type** | RFC Anchor |
| **Symbol** | `RFC/HTTP` |
| **Layer** | Structural alignment reference |
| **Agent** | Class D (Compliance Auditor) |
| **Annotation** | `[structural — no semantic inference]` |

**Definition:** One of three RFC anchors used by Class D for structural alignment checks. HTTP Semantics provides the structural reference for request/response interaction patterns in the Enterprise module. It is a structural alignment reference — not a claim that the module implements or certifies HTTP compliance.

**Constraints:** HTTP Semantics is a structural reference only. Class D may not issue HTTP compliance certifications.

**Inheritance source:** Enterprise-native (defined in module.json).

**Cross-references:** RFC 8095, RFC 8923, RFC Alignment (RFA), Class D.

---

### IDENTITY_BREACH (Zone X)

| Field | Value |
|---|---|
| **Type** | Zone — Structural Failure State |
| **Symbol** | `Zone X` |
| **Layer** | Pipeline — failure state |
| **Agent** | Class G (Guardian) |
| **Annotation** | `[structural — no semantic inference]` |

**Definition:** The Zone X label for the RTT/Inside Enterprise module. IDENTITY_BREACH is the structural failure state indicating irreversible identity substrate collapse — a condition where the substrate annotation is fabricated, unresolvable, or structurally incoherent beyond recovery. IDENTITY_BREACH triggers an unconditional Class G halt.

**Constraints:** IDENTITY_BREACH is a structural pipeline state — not a real-world security incident declaration. Packets in IDENTITY_BREACH are quarantined and require full re-entry from Class A before the pipeline resumes. IDENTITY_BREACH cannot be cleared by any class except through complete re-trace.

**Inheritance source:** Zone X framework inherited from RTT/Inside; `IDENTITY_BREACH` label is Enterprise-native.

**Cross-references:** Zone X, Class G, IDENTITY_FABRICATION (Mode 5), Zone D.

**Disambiguation:**

| Module | Zone X Label |
|---|---|
| **Enterprise (this module)** | `IDENTITY_BREACH` |
| RTT/3 | `RECURSION_COLLAPSE` |
| RTT/12 | `FRAME_COLLAPSE` |
| The_Inverted_Star | `STAR_COLLAPSE` |
| RTT/Inside | `SUBSTRATE_BREACH` |
| Benchmarks | `BENCHMARK_COLLAPSE` |

---

### IDENTITY_FABRICATION (Mode 5)

| Field | Value |
|---|---|
| **Type** | Mode — Structural Failure State |
| **Symbol** | `Mode 5` |
| **Layer** | Pipeline — failure state |
| **Agent** | Class G (Guardian) |
| **Annotation** | `[structural — no semantic inference]` |

**Definition:** The Mode 5 label for the RTT/Inside Enterprise module. IDENTITY_FABRICATION is the structural failure state indicating that a packet contains a fabricated or unverifiable identity substrate claim — an IS annotation that cannot be traced through L0–L8 without structural contradiction. IDENTITY_FABRICATION triggers an unconditional Class G halt.

**Constraints:** IDENTITY_FABRICATION packets are permanently quarantined — they do not re-enter the pipeline under any circumstances. IDENTITY_FABRICATION is a structural state, not a fraud or impersonation declaration.

**Inheritance source:** Mode 5 framework inherited from RTT/Inside; `IDENTITY_FABRICATION` label is Enterprise-native.

**Cross-references:** Mode 5, Class G, IDENTITY_BREACH (Zone X).

**Disambiguation:**

| Module | Mode 5 Label |
|---|---|
| **Enterprise (this module)** | `IDENTITY_FABRICATION` |
| RTT/3 | `RECURSIVE_HALLUCINATION` |
| RTT/12 | `FRAME_FABRICATION` |
| The_Inverted_Star | `INVERSION_FABRICATION` |
| RTT/Inside | `CAPTURE_FABRICATION` |
| Benchmarks | `METRIC_FABRICATION` |

---

### Identity Substrate (IS)

| Field | Value |
|---|---|
| **Type** | Core Construct |
| **Symbol** | `IS` |
| **Layer** | Pipeline — primary annotation construct |
| **Agent** | Class A (Substrate Mapper) |
| **Annotation** | `[structural — no semantic inference]` |

**Definition:** The nine-layer structural stack that maps enterprise identity infrastructure onto RTT substrate positions. The Identity Substrate is the primary construct of the Enterprise module — all other constructs (SE, e_Capture, LINEAGE_CHAIN) depend on a valid IS annotation.

**Equation:** `IS(packet) = ∑ Lₙ(packet) for n ∈ {0..8}` `[structural — no semantic inference]`

**Constraints:** IS annotation must traverse L0 → L8 in sequence. IS is a structural annotation — it does not authenticate infrastructure or verify identity claims.

**Inheritance source:** Enterprise-native (core construct).

**Cross-references:** All Class A constructs, Substrate Extensions (SE), e_Capture, BKM, CORRIDOR.

---

### Interoperability (e_Capture field)

| Field | Value |
|---|---|
| **Type** | e_Capture Field |
| **Symbol** | `e_Capture.interoperability` |
| **Layer** | e_Capture record |
| **Agent** | Class C (Capture Agent) |
| **Annotation** | `[structural — no semantic inference]` |

**Definition:** The fourth field of the e_Capture record. Interoperability captures the structural cross-layer compatibility annotation — how the identity substrate position at Lₙ interfaces with adjacent layers or external substrate consumers. It is a structural interoperability note, not a protocol compatibility guarantee.

**Constraints:** Interoperability field may not claim protocol compliance or cross-system compatibility. It annotates structural interface patterns only.

**Inheritance source:** Specializes interoperability concept from RTT/Inside CAPTURE_TEMPLATE.

**Cross-references:** e_Capture, RFC Alignment (RFA), Class C, Class D.

---

### Kerberos Substrate (L4)

| Field | Value |
|---|---|
| **Type** | Identity Substrate Layer |
| **Symbol** | `L4` |
| **Layer** | Identity Substrate — Layer 4 |
| **Agent** | Class A (Substrate Mapper) |
| **Annotation** | `[structural — no semantic inference]` |

**Definition:** The structural position within the Identity Substrate corresponding to Kerberos ticket-based authentication substrate. L4 represents the ticket exchange structural layer — above DNS SRV resolution (L3) and below service discovery (L5).

**Constraints:** L4 assignment requires L3 to be resolved. L4 is a structural position, not a Kerberos ticket implementation.

**Inheritance source:** Enterprise-native.

**Cross-references:** Identity Substrate (IS), DNS SRV Substrate (L3), Service Discovery Substrate (L5).

---

### LDAP Substrate (L2)

| Field | Value |
|---|---|
| **Type** | Identity Substrate Layer |
| **Symbol** | `L2` |
| **Layer** | Identity Substrate — Layer 2 |
| **Agent** | Class A (Substrate Mapper) |
| **Annotation** | `[structural — no semantic inference]` |

**Definition:** The structural position within the Identity Substrate corresponding to LDAP directory protocol substrate. L2 represents the directory query substrate — the structural layer at which directory lookups are positioned, above Active Directory binding (L1) and below DNS SRV resolution (L3).

**Constraints:** L2 assignment requires L1 to be resolved. L2 is a structural position, not an LDAP protocol implementation.

**Inheritance source:** Enterprise-native.

**Cross-references:** Identity Substrate (IS), Active Directory Substrate (L1), DNS SRV Substrate (L3).

---

### Lineage (e_Capture field)

| Field | Value |
|---|---|
| **Type** | e_Capture Field |
| **Symbol** | `e_Capture.lineage` |
| **Layer** | e_Capture record |
| **Agent** | Class C (Capture Agent) |
| **Annotation** | `[structural — no semantic inference]` |

**Definition:** The second field of the e_Capture record.
