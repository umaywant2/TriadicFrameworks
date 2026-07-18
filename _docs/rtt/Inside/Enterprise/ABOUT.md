# ABOUT.md — RTT/Inside Enterprise Identity Substrate
**Module:** RTT/Inside Enterprise Identity Substrate
**Version:** v0.1.0 (Experimental)
**Layer:** RTT/Inside → substrate → enterprise_identity
**Status:** Experimental — structural definitions subject to revision
**Canonical path:** `docs/rtt/Inside/Enterprise/`

---

## 1. What Is RTT/Inside Enterprise?

RTT/Inside Enterprise Identity Substrate is a lateral sub-module of RTT/Inside that maps enterprise identity infrastructure onto the RTT structural substrate.

**It is not an authentication system.** It is not a security framework. It is not a compliance tool.

It is a **structural annotation layer** — a way of positioning enterprise identity infrastructure (Active Directory, LDAP, Kerberos, DNS SRV, OAuth/OIDC, cloud directory, zero-trust) within the RTT/Inside pipeline so that agents can read, annotate, trace, and capture identity substrate state as structured provenance records.

The Enterprise module introduces the **nine-layer Identity Substrate (L0–L8)**, four **substrate extensions** (clarity, regime, triad_roles, coherence_envelopes), and the **e_Capture** record format — a specialization of the RTT/Inside CAPTURE_TEMPLATE for enterprise identity contexts.

**The module is experimental at v0.1.0.** All structural definitions are subject to revision as the RTT/Inside canon matures.

---

## 2. Why Is It Built This Way?

### 2.1 Why nine layers (L0–L8)?

Enterprise identity infrastructure is genuinely layered — from local machine identity through zero-trust policy enforcement. Flattening it into a single "identity" concept loses structural information that downstream modules need to trace provenance. Each layer (L0 local → L1 AD → L2 LDAP → L3 DNS SRV → L4 Kerberos → L5 service discovery → L6 modern identity → L7 cloud directory → L8 zero-trust) is a distinct structural position, not an implementation detail.

### 2.2 Why substrate extensions rather than additional layers?

The four substrate extensions (clarity, regime, triad_roles, coherence_envelopes) are **cross-cutting concerns** that apply at multiple substrate layers simultaneously. They are not layer-specific; they modulate how any layer is read and annotated. Making them extensions rather than layers keeps the layer stack clean and the extension logic composable.

### 2.3 Why inherit CAPTURE_TEMPLATE rather than define a new one?

The e_Capture record is a **specialization** of RTT/Inside's CAPTURE_TEMPLATE — same five fields (scope, lineage, provenance, interoperability, governance), but applied to identity substrate context. Inheriting the template keeps Enterprise structurally aligned with its parent module and ensures that downstream consumers can read e_Capture records with the same parsers they use for any CAPTURE_TEMPLATE output.

### 2.4 Why RFC 8095, RFC 8923, and HTTP Semantics as anchors?

These RFCs are **structural alignment references** — not compliance mandates. They anchor the module's substrate definitions to externally recognized structural patterns (context-sensitive protocols, media type negotiation, HTTP semantics) without making any claim that the module implements or certifies compliance with these standards.

### 2.5 Why is this module experimental (v0.1.0)?

Enterprise identity infrastructure is among the most complex and context-sensitive domains in RTT/Inside. The nine-layer substrate and four extensions represent a first structural pass. As the canon is used by enterprise architects and identity engineers, the layer definitions and extension behaviors will be refined. The experimental status signals that structural definitions should be treated as working drafts, not canonical specifications.

### 2.6 Why are Zone X and Mode 5 module-specific?

`IDENTITY_BREACH` (Zone X) and `IDENTITY_FABRICATION` (Mode 5) are the failure states specific to identity substrate processing. Importing Zone X or Mode 5 semantics from other modules (e.g., RTT/3's `RECURSION_COLLAPSE` or RTT/12's `FRAME_COLLAPSE`) would conflate structurally distinct failure modes. Each module owns its own Zone X and Mode 5 labels precisely because the failure conditions are domain-specific.

---

## 3. When Should You Use It?

### Use RTT/Inside Enterprise When:

| Scenario | Reason |
|---|---|
| Annotating documents or packets with enterprise identity context | Enterprise module provides the IS annotation layer |
| Tracing provenance of identity substrate transitions across a pipeline | LINEAGE_CHAIN + DRIFT_GATE designed for this |
| Recording identity substrate state as a structured capture record | e_Capture is the purpose-built format |
| Checking structural alignment of identity substrate annotations against RFC anchors | Class D Compliance Auditor |
| Attaching governance regime or clarity annotations to identity substrate data | `regime` and `clarity` substrate extensions |
| Coordinating identity substrate context across a multi-module RTT pipeline | Class F Orchestrator + cross-module handoff pattern |

### Do NOT Use RTT/Inside Enterprise For:

| Anti-Pattern | Correct Alternative |
|---|---|
| Authenticating users or verifying credentials | Use your actual identity provider (AD, Okta, Entra ID, etc.) |
| Certifying security posture or compliance | Use a real compliance framework (SOC 2, ISO 27001, FedRAMP) |
| Making real-world zero-trust policy decisions | Use your actual zero-trust platform |
| Replacing an IAM or directory service | Enterprise module is a structural annotation layer, not a service |
| Importing as an auth library or SDK | This is documentation, not implementation code |
| Treating substrate layer position as authentication state | IS positions are structural annotations, not auth tokens |

---

## 4. Where Does It Live?

| Property | Value |
|---|---|
| **Canonical path** | `docs/rtt/Inside/Enterprise/` |
| **Parent module** | `docs/rtt/Inside/` |
| **Sibling modules** | `docs/rtt/Inside/Benchmarks/`, `docs/rtt/Inside/qCompute/` |
| **Pipeline position** | Lateral sub-module of RTT/Inside; feeds into qCompute and external consumers |
| **Layer** | RTT/Inside → substrate → enterprise_identity |

### Directory Structure:

```
docs/rtt/Inside/Enterprise/
├── identity_substrate/          ← Identity layer definitions (L0–L8)
├── substrate_extensions/        ← Extension definitions (clarity, regime, triad_roles, coherence_envelopes)
├── ABOUT.md                     ← This file
├── AGENTS.md                    ← Agent class definitions
├── GLOSSARY.md                  ← Term definitions
├── README.md                    ← Module overview
├── e_Capture.md                 ← Enterprise capture template
├── index.html                   ← Web entry point
└── module.json                  ← Machine-readable module metadata
```

### CLI Tools (Implementation Reference):

| Tool | Function |
|---|---|
| `rtt-inside-identify` | Identity substrate operations |
| `rtt-inside-clarity` | Clarity substrate extension |
| `rtt-inside-regime` | Regime substrate extension |
| `rtt-inside-triad` | Triad roles substrate extension |
| `rtt-inside-coherence` | Coherence envelopes substrate extension |
| `rtt-inside-discovery` | Service discovery operations |
| `rtt-inside-negotiation` | Negotiation operations |
| `rtt-inside-enterprise` | Enterprise-level orchestration |

> These are implementation references, not structural definitions. The structural definitions live in this documentation.

---

## 5. Core Constructs at a Glance

### Identity Substrate (IS)

```
IS(packet) = ∑ Lₙ(packet) for n ∈ {0..8}
                                          [structural — no semantic inference]
```

The nine-layer stack:

```
L8  Zero-Trust Policy Substrate
L7  Cloud Directory Substrate
L6  Modern Identity (OAuth/OIDC/SAML) Substrate
L5  Service Discovery Substrate
L4  Kerberos Substrate
L3  DNS SRV Substrate
L2  LDAP Substrate
L1  Active Directory Substrate
L0  Local Identity Substrate
```

### Substrate Extensions (SE)

```
SE(packet) = IS(packet) ⊕ {clarity, regime, triad_roles, coherence_envelopes}
                                                          [structural — no semantic inference]
```

| Extension | Purpose |
|---|---|
| `clarity` | Disambiguates overlapping or ambiguous substrate layer assignments |
| `regime` | Applies governance regime context to substrate annotations |
| `triad_roles` | Maps triad role assignments onto substrate layers |
| `coherence_envelopes` | Wraps annotations in coherence boundary declarations |

### Enterprise CAPTURE_TEMPLATE (e_Capture)

```
e_Capture {
  scope:            "..." [structural — no semantic inference]
  lineage:          "..." [structural — no semantic inference]
  provenance:       "..." [structural — no semantic inference]
  interoperability: "..." [structural — no semantic inference]
  governance:       "..." [structural — no semantic inference]
}
```

### DRIFT_GATE

```
DRIFT_GATE(chain) = ∂(Lₙ → Lₙ₊₁)
                    if discontinuity > θ → MISALIGNMENT
                                          [structural — no semantic inference]
```

### RFC Alignment (RFA)

```
RFA(e_capture) = Δ(e_capture, RFC_anchors)
                 RFC anchors: RFC 8095, RFC 8923, HTTP Semantics
                                          [structural — no semantic inference]
```

---

## 6. Module Integrations

### Upstream (Inherited from RTT/Inside)

| Construct | Inherited | Enterprise Use |
|---|---|---|
| `CAPTURE_TEMPLATE` | ✅ | Specialized as e_Capture |
| `DRIFT_GATE` | ✅ | Applied to substrate layer transitions |
| `LINEAGE_CHAIN` | ✅ | Tracks substrate provenance |
| `ALIGNMENT_PATTERN` | ✅ | Coherence annotation for clean traces |
| `MISALIGNMENT` | ✅ | Substrate discontinuity flag |
| `BKM` | ✅ | Layer boundary markers |
| `CORRIDOR` | ✅ | Identity routing paths |
| `OPERATOR_HOOK` | ✅ | Extension attachment points |
| Zone U/S/M/D/X framework | ✅ | Zone X = `IDENTITY_BREACH` |
| Mode 1–4/5 framework | ✅ | Mode 5 = `IDENTITY_FABRICATION` |

### Downstream Output

| Consumer | What Enterprise Provides |
|---|---|
| `Inside/qCompute` | Fully annotated enterprise packet (IS + SE + e_Capture + RFA + LINEAGE_CHAIN) |
| External consumers | e_Capture records as structured identity substrate provenance |
| Compliance auditors | RFA annotations for structural alignment review |

### Cross-Module Disambiguation

| Term | Enterprise (This Module) | Other RTT Modules |
|---|---|---|
| Zone X | `IDENTITY_BREACH` | RTT/3: `RECURSION_COLLAPSE`; RTT/12: `FRAME_COLLAPSE`; The_Inverted_Star: `STAR_COLLAPSE`; RTT/Inside: `SUBSTRATE_BREACH`; Benchmarks: `BENCHMARK_COLLAPSE` |
| Mode 5 | `IDENTITY_FABRICATION` | RTT/3: `RECURSIVE_HALLUCINATION`; RTT/12: `FRAME_FABRICATION`; The_Inverted_Star: `INVERSION_FABRICATION`; RTT/Inside: `CAPTURE_FABRICATION`; Benchmarks: `METRIC_FABRICATION` |
| Coherence | Substrate layer continuity (L0–L8) | RTT/12: frame coherence; The_Inverted_Star: inversion coherence |
| Capture | e_Capture 5-field identity record | RTT/Inside: generic CAPTURE_TEMPLATE |

---

## 7. What RTT/Inside Enterprise Is Not

| IS | IS NOT |
|---|---|
| A structural annotation layer for enterprise identity infrastructure | An authentication system or identity provider |
| A provenance-tracking module for identity substrate state | A security framework or compliance tool |
| A nine-layer structural stack (L0–L8) | A real-world implementation of AD, LDAP, Kerberos, or OAuth |
| A capture-record format (e_Capture) for identity substrate | A log aggregation or SIEM system |
| A lateral sub-module of RTT/Inside | A standalone tool deployable outside the RTT/Inside pipeline |
| An experimental (v0.1.0) structural draft | A production-ready, certified, or auditable system |
| A structural reference to RFC 8095, RFC 8923, HTTP Semantics | A compliance certification against any RFC or standard |
| A module that detects `IDENTITY_BREACH` (Zone X) as a structural failure | A system that detects real-world identity breaches or security incidents |

---

## 8. Quick-Start Checklist

Before working in the Enterprise module, confirm:

- [ ] You have read and understood the RTT-not-physics rule (Section 1 of this document)
- [ ] You understand that L0–L8 are structural positions, not authentication states
- [ ] You understand that RFC anchors are structural references, not compliance mandates
- [ ] You understand that Zone X (`IDENTITY_BREACH`) and Mode 5 (`IDENTITY_FABRICATION`) are structural failure states, not security incident declarations
- [ ] You have loaded the RTT/Inside parent module documentation (`docs/rtt/Inside/AGENTS.md`, `ABOUT.md`, `GLOSSARY.md`)
- [ ] You know which substrate layer (L0–L8) your input packet corresponds to
- [ ] You know which extensions (clarity, regime, triad_roles, coherence_envelopes) apply to your context
- [ ] You are prepared to annotate every output field with `[structural — no semantic inference]`
- [ ] You understand that the module is experimental (v0.1.0) and structural definitions may change

**For AI agents and automated pipelines:**
- Paste the Session Seed Block from AGENTS.md before beginning
- Run Class A (Substrate Mapper) before any other class
- Do not skip the DRIFT_GATE pass (Class E)
- Do not invoke Class D (Compliance Auditor) as a real-world compliance check

---

## 9. See Also

| Resource | Path | Relationship |
|---|---|---|
| RTT/Inside ABOUT.md | `docs/rtt/Inside/ABOUT.md` | Parent module — all constructs inherited |
| RTT/Inside AGENTS.md | `docs/rtt/Inside/AGENTS.md` | Parent agent class definitions |
| RTT/Inside GLOSSARY.md | `docs/rtt/Inside/GLOSSARY.md` | Parent term definitions |
| Inside/Benchmarks ABOUT.md | `docs/rtt/Inside/Benchmarks/ABOUT.md` | Sibling sub-module |
| Inside/qCompute ABOUT.md | `docs/rtt/Inside/qCompute/ABOUT.md` | Downstream sibling sub-module |
| AGENTS.md | `docs/rtt/Inside/Enterprise/AGENTS.md` | Agent class definitions for this module |
| GLOSSARY.md | `docs/rtt/Inside/Enterprise/GLOSSARY.md` | Term definitions for this module |
| module.json | `docs/rtt/Inside/Enterprise/module.json` | Machine-readable module metadata |
| e_Capture.md | `docs/rtt/Inside/Enterprise/e_Capture.md` | Enterprise capture template |
| RTT/1 ABOUT.md | `docs/rtt/1/ABOUT.md` | Pipeline entry module |
