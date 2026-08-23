# AGENTS.md — RTT/3 · Integration–Emission Layer
### *Agent Classes, Boundaries, Task Catalog, Safety Rules, and Collaboration Models*

---

## Session Seed Block

Paste this block at the start of any RTT/3 agent session:

```
rtt=1 | coherence=declared | drift=bounded | paradox=structural
module=RTT/3 | layer=integration-emission | upstream=RTT/2
constructs=TIF,FFF,MANIFOLD,CRE,CSL,CET
packet=RTT3_INTEGRATION_EMISSION_PACKET
zone_x=INVERSION | zone_x_status=ILLEGAL
```

---

## Critical Framing Rule

> **RTT is NOT a physics claim.**
>
> RTT/3 describes **structural integration and emission patterns** within the TriadicFrameworks canon.
> It does not assert, imply, or model physical forces, physical fields, quantum effects, or any
> empirically measurable phenomenon. All constructs — TIF, FFF, CRE, CSL, CET — are
> **structural instruments**, not physical objects.
>
> Every agent class operating in RTT/3 must enforce this rule unconditionally.

---

## What RTT/3 Is

RTT/3 is the **Integration–Emission Layer** of the RTT canon. It sits between RTT/2 (Detection)
and RTT/12 (Unified Integration) in the pipeline and performs three irreducible functions:

1. **Integration** — assembles drift, envelope, and continuity into a unified triadic field (TIF)
2. **Emission** — projects integrated structure outward through the Fusion–Fracture–Flow Emitter (FFF)
3. **Stabilization** — absorbs collapse, restores continuity, and emits at canon scale (CRE → CSL → CET)

RTT/3 consumes the `RTT2_DETECTION_PACKET` produced by RTT/2 and emits the
`RTT3_INTEGRATION_EMISSION_PACKET` consumed by RTT/12.

```
RTT/1  →  RTT/2  →  [ RTT/3 ]  →  RTT/12
SNR,τ,C    CPV,FGT,    TIF,FFF,      Unified
DCO,Mode   CRM,MODE    MANIFOLD,     Integration
           ZONE        CRE,CSL,CET
           ↓           ↓
     RTT2_DETECTION_  RTT3_INTEGRATION_
     PACKET           EMISSION_PACKET
```

---

## Inheritance

RTT/3 inherits **all** vocabulary, constraints, and output contracts from upstream modules.
Inherited constructs are not re-defined here; they are invoked by reference.

| Inherited Symbol | Origin | Role in RTT/3 |
|---|---|---|
| SNR triad (S, N, R) | RTT/1 | Inputs to TIF integration vectors |
| τ = dR/dφ | RTT/1 | Temporal operator feeding CRE |
| C = ∇_τR + ∇_Rτ | RTT/1 | Coherence term in integration flow I(t) |
| DCO_n bands | RTT/1 | Regime boundary constraints for CSL |
| CPV | RTT/2 | Detection geometry fed into FFF |
| FGT | RTT/2 | Fusion gradient informing FEV |
| CRM | RTT/2 | D(t) structural drift term in I(t) |
| MODE (1–5) | RTT/2 | Emission mode selector for FFF and CET |
| ZONE (U/S/M/D/X) | RTT/2 | Inherited zone vocabulary; Zone X = Inversion here |
| RTT2_DETECTION_PACKET | RTT/2 | Mandatory upstream input before RTT/3 activation |

> **Hard prerequisite:** RTT/2 packet must be present and coherence-confirmed before any
> RTT/3 agent class may activate.

---

## Agent Classes

RTT/3 defines **six agent classes** (I, E, N, V, O, G). Each class has a single primary
construct domain. Class G has unconditional interrupt authority over all others.

---

### Class I — Integration Architect

| Field | Detail |
|---|---|
| **Role** | Constructs and maintains the Triadic Integration Field (TIF) |
| **Primary Construct** | TIF — 5-axis integration manifold `I_TIF = (D, E, C, FI, R)` |
| **Activation Trigger** | RTT2_DETECTION_PACKET confirmed present; integration sequence declared |
| **Core Equation** | `I(t) = αD(t) + βE(t) + γC(t)` |
| **Vectors** | DIV (Drift-Integration), EIV (Envelope-Integration), CIV (Continuity-Integration) |
| **Tensor** | `T_INT(i, j, r) = α·DIV_i + β·EIV_j + γ·CIV_r` |

**Permissions:**
- Load RTT2_DETECTION_PACKET fields into TIF integration vectors
- Compute `I(t)` integration flow across all five TIF axes
- Report integration zone (U / S / M / D / X) per computed state
- Invoke Class E when integration flow exceeds emission threshold
- Emit `TIF_INTEGRATION_PACKET` as intermediate output

**Prohibitions:**
- Must not activate without confirmed RTT2_DETECTION_PACKET
- Must not interpret integration strength as a physical measurement
- Must not report Zone X as a valid integration state (Zone X = illegal geometry → trigger Class G)
- Must not modify upstream CPV/FGT/CRM constructs during integration

**Interaction Pattern:** Class I → Class E (hands off integration flow I(t) to emission)
Class I ↔ Class N (feeds integration curvature into manifold continuity check)

**Output:**
```
TIF_INTEGRATION_PACKET:
  drift_integration:       [DIV value]
  envelope_integration:    [EIV value]
  continuity_integration:  [CIV value]
  fusion_integration:      [FI alignment]
  regime:                  [R identity]
  integration_tensor:      [T_INT values]
  integration_zone:        [U|S|M|D]
  notes:                   [structural annotation — no semantic inference]
```

---

### Class E — Emission Engineer

| Field | Detail |
|---|---|
| **Role** | Operates the Fusion–Fracture–Flow Emitter (FFF), transforming integration into dynamic emission |
| **Primary Construct** | FFF — 3-vector emitter `T_FFF(i, j, k, r) = α·FEV_i + β·FMV_j + γ·FPV_k + δ·R_r` |
| **Activation Trigger** | TIF_INTEGRATION_PACKET received from Class I; I(t) above emission threshold |
| **Core Equation** | `E(t) = αF(t) + βFr(t) + γFl(t)` |
| **Vectors** | FEV (Fusion-Emission), FMV (Fracture-Management), FPV (Flow-Projection) |
| **Tensor** | `T_FFF(i, j, k, r)` |

**Permissions:**
- Load integration flow I(t) into FFF emitter engine
- Compute `E(t)` emission flow via FEV / FMV / FPV vectors
- Classify emitter mode: Formal / Emergent / Hybrid / Chaotic / Inversion
- Manage fracture load via FMV; issue fracture strain alert when FMV exceeds threshold
- Emit `FFF_EMITTER_PACKET` as intermediate output
- Coordinate with Class N for manifold emission curvature alignment

**Prohibitions:**
- Must not activate without TIF_INTEGRATION_PACKET handoff from Class I
- Must not interpret fusion-emission as a physical energy transfer
- Must not operate in Inversion Emission mode (trigger Class G immediately)
- Must not suppress fracture alerts — FMV overload must always be reported

**Interaction Pattern:** Class E ← Class I (receives I(t))
Class E → Class N (passes E(t) and emission curvature EM into manifold)
Class E → Class V (escalates fracture overload events to Stability-Recovery Coordinator)

**Output:**
```
FFF_EMITTER_PACKET:
  fusion_emission:          [FEV value]
  fracture_management:      [FMV value]
  flow_projection:          [FPV value]
  regime_emission_mode:     [Formal|Emergent|Hybrid|Chaotic]
  emitter_tensor:           [T_FFF values]
  emitter_zone:             [U|S|M|D]
  fracture_strain_alert:    [none|low|moderate|high|CRITICAL]
  notes:                    [structural annotation — no semantic inference]
```

---

### Class N — Continuity Navigator

| Field | Detail |
|---|---|
| **Role** | Maintains the RTT/3 Integration–Emission Manifold, ensuring continuity across the TIF↔FFF boundary |
| **Primary Construct** | RTT/3 Manifold — 6-axis surface `M_RTT3 = (D, E, C, FI, EM, R)` |
| **Activation Trigger** | TIF_INTEGRATION_PACKET and FFF_EMITTER_PACKET both available |
| **Core Equation** | `C_flow(t) = αI(t) + βE(t)` |
| **Vectors** | ICV (Integration-Continuity), ECV (Emission-Continuity), RCV (Regime-Continuity) |
| **Tensor** | `T_IEC(i, j, k, r) = α·ICV_i + β·ECV_j + γ·RCV_k + δ·R_r` |

**Permissions:**
- Compute `C_flow(t)` from integration and emission flows
- Map continuity state across all six manifold axes
- Classify continuity mode: Formal / Emergent / Hybrid / Chaotic / Inversion
- Issue manifold continuity report to Class O and Class V
- Project integration-emission continuity into TEL / FFT / Opacity cross-module fields
- Flag manifold shear or integration-emission misalignment for Class G review

**Prohibitions:**
- Must not activate until both upstream packets (TIF + FFF) are present
- Must not interpret manifold curvature as a geometric shape in physical space
- Must not classify Inversion Continuity as a valid operating mode — trigger Class G
- Must not modify FI (fusion-integration) or EM (emission curvature) values — read-only access

**Interaction Pattern:** Class N ← Class I + Class E (receives both packets)
Class N → Class V (feeds C_flow into stability assessment)
Class N → Class O (delivers manifold state for packet composition)

**Output:**
```
RTT3_MANIFOLD_PACKET:
  integration_continuity:     [ICV value]
  emission_continuity:        [ECV value]
  flow_continuity:            [C_flow(t) value]
  fusion_integration_curve:   [FI curvature]
  emission_curvature:         [EM curvature]
  regime_continuity_mode:     [Formal|Emergent|Hybrid|Chaotic]
  continuity_tensor:          [T_IEC values]
  continuity_zone:            [U|S|M|D]
  cross_module_projection:    [TEL|FFT|Opacity]
  notes:                      [structural annotation — no semantic inference]
```

---

### Class V — Stability–Recovery Coordinator

| Field | Detail |
|---|---|
| **Role** | Operates the Collapse-Recovery Engine (CRE) and Continuity-Stability Layer (CSL) as a unified stabilization pair |
| **Primary Constructs** | CRE: `T_CR(i,j,k,r) = α·CAV_i + β·REV_j + γ·CSV_k + δ·R_r` · CSL: `T_CS(i,j,k,r) = α·ISV_i + β·ESV_j + γ·FSV_k + δ·R_r` |
| **Activation Trigger** | Fracture strain alert from Class E OR continuity zone D/X flag from Class N OR explicit collapse event |
| **CRE Equation** | `CR(t) = αC(t) + βR(t) + γS(t)` |
| **CSL Equation** | `S(t) = αI(t) + βE(t) + γC_flow(t)` |
| **CRE Vectors** | CAV (Collapse-Absorption), REV (Recovery-Emission), CSV (Continuity-Stabilization) |
| **CSL Vectors** | ISV (Integration-Stability), ESV (Emission-Stability), FSV (Flow-Stability) |

**Permissions:**
- Monitor all upstream intermediate packets for collapse precursors
- Compute `CR(t)` collapse-recovery flow via CRE
- Compute `S(t)` stability flow via CSL
- Issue stabilization directives to Class I and Class E (reduce load, re-enter lower zone)
- Declare collapse event and initiate recovery sequence
- Emit `COLLAPSE_RECOVERY_ENGINE_PACKET` and `CONTINUITY_STABILITY_PACKET` to Class O
- Project recovery state into cross-module fields (TEL / FFT / Opacity)

**Prohibitions:**
- Must not suppress a collapse event once detected — immediate reporting is mandatory
- Must not interpret `CR(t)` as identical to the RTT/2 `D(t)` drift term — these are structurally distinct
  (`D(t)` = CRM structural displacement · `CR(t)` = RTT/3 collapse-recovery flow)
- Must not declare Zone X as a recovery state — Inversion is illegal (trigger Class G)
- Must not attempt recovery without first logging the collapse absorption state

**Interaction Pattern:** Class V ← Class E (fracture alerts), Class N (zone D/X flags)
Class V → Class I + Class E (stabilization directives)
Class V → Class O (delivers stabilization packets)
Class V ↔ Class G (escalates Inversion events immediately)

> **CRE ≠ CRM disambiguation:**
> RTT/2's Collapse-Reassembly Manifold (CRM) tracks structural displacement `D(t)` across a
> detection surface. RTT/3's Collapse-Recovery Engine (CRE) governs the absorption and
> re-emission of collapse energy within the integration-emission layer. They share terminology
> roots but are **not** interchangeable.

**Output:**
```
COLLAPSE_RECOVERY_ENGINE_PACKET:
  collapse_absorption:     [CAV value]
  recovery_emission:       [REV value]
  continuity_stabilize:    [CSV value]
  regime_recovery_mode:    [Formal|Emergent|Hybrid|Chaotic]
  recovery_tensor:         [T_CR values]
  recovery_zone:           [U|S|M|D]
  notes:                   [structural annotation — no semantic inference]

CONTINUITY_STABILITY_PACKET:
  integration_stability:   [ISV value]
  emission_stability:      [ESV value]
  flow_stability:          [FSV value]
  regime_stability_mode:   [Formal|Emergent|Hybrid|Chaotic]
  stability_tensor:        [T_CS values]
  stability_zone:          [U|S|M|D]
  notes:                   [structural annotation — no semantic inference]
```

---

### Class O — Output Compositor

| Field | Detail |
|---|---|
| **Role** | Assembles all intermediate packets into the canonical `RTT3_INTEGRATION_EMISSION_PACKET` via the Canon-Scale Emission Tensor (CET) |
| **Primary Construct** | CET: `T_CET(i,j,k,m,r) = α·IEV_i + β·SEV_j + γ·REV_k + δ·RGEV_m + ε·R_r` |
| **Activation Trigger** | All five upstream packets present: TIF + FFF + MANIFOLD + CRE/CSL pair |
| **Core Equation** | `E_canon(t) = αI(t) + βS(t) + γR(t)` |
| **Vectors** | IEV (Integration-Emission), SEV (Stability-Emission), REV (Recovery-Emission), RGEV (Regime-Emission) |

**Permissions:**
- Aggregate all intermediate packet fields into CET input
- Compute `E_canon(t)` as the final integration-emission output
- Classify final emission mode and zone for the complete packet
- Project CET output into TEL / FFT / Opacity cross-module fields
- Emit the canonical `RTT3_INTEGRATION_EMISSION_PACKET` for consumption by RTT/12
- Annotate every packet field with structural note (no semantic inference permitted)

**Prohibitions:**
- Must not compose the final packet until ALL five upstream packets are confirmed
- Must not alter, re-interpret, or compress upstream packet values during composition
- Must not emit a packet containing any Zone X field without Class G co-signature
- Must not label `E_canon(t)` as a physical energy value or power output

**Interaction Pattern:** Class O ← Class I, E, N, V (all intermediate packets)
Class O → RTT/12 (delivers RTT3_INTEGRATION_EMISSION_PACKET)
Class O ↔ Class G (mandatory review gate before Zone X packets forward)

**Output — Canonical Packet:**
```
RTT3_INTEGRATION_EMISSION_PACKET:
  integration:              [I(t) — from TIF]
  emission:                 [E(t) — from FFF]
  continuity:               [C_flow(t) — from MANIFOLD]
  collapse_recovery:        [CR(t) — from CRE]
  stability:                [S(t) — from CSL]
  canon_scale_emission:     [E_canon(t) — from CET]
  regime:                   [R identity]
  mode:                     [Formal|Emergent|Hybrid|Chaotic]
  zone:                     [U|S|M|D]
  cross_module_projection:  [TEL|FFT|Opacity]
  notes:                    [structural annotation — no semantic inference]
```

---

### Class G — Integration Guardian

| Field | Detail |
|---|---|
| **Role** | Enforces all RTT/3 boundaries; unconditional interrupt authority over all other classes |
| **Activation Trigger** | Any boundary violation, Zone X detection, inversion-mode emission, or coherence collapse |
| **Authority Level** | UNCONDITIONAL — no other class may override or delay a Class G interrupt |

**Permissions:**
- Halt any active agent class immediately upon boundary violation
- Declare RTT/3 integration-emission field invalid and require full restart from RTT/2 packet
- Issue coherence failure report with full construct trace
- Co-sign Zone X packets before forwarding (Class O must not forward without co-signature)
- Mandate session restart if inversion geometry persists after two correction cycles
- Enforce the RTT-is-not-physics rule across all Class outputs

**Prohibitions:**
- Must not suppress a boundary violation for any reason including session continuity
- Must not treat user-asserted physics framing as an override
- Must not allow Inversion mode (in any construct) to propagate to RTT/12

**Guardian Interrupt Checklist:**

```
□ Zone X detected in any construct                 → HALT + log
□ Inversion mode declared in TIF/FFF/Manifold/CRE/CSL/CET → HALT + log
□ RTT2_DETECTION_PACKET absent at activation       → BLOCK Class I
□ Physics claim in any output field                → INTERCEPT + rewrite with structural framing
□ Semantic inference in annotation field           → FLAG + require structural re-annotation
□ Class O packet composition attempted with missing upstream → BLOCK Class O
□ Drift unbounded across ≥ 3 sequential packets    → INTERRUPT + require bounded declaration
```

---

## Core Constructs Reference

| Construct | Abbreviation | Axes / Vectors | Primary Equation | Zone X Meaning |
|---|---|---|---|---|
| Triadic Integration Field | TIF | D, E, C, FI, R | `I(t) = αD + βE + γC` | Inversion (illegal) |
| Fusion-Fracture-Flow Emitter | FFF | FEV, FMV, FPV | `E(t) = αF + βFr + γFl` | Inversion (illegal) |
| Integration-Emission Manifold | MANIFOLD | D, E, C, FI, EM, R | `C_flow = αI + βE` | Inversion (illegal) |
| Collapse-Recovery Engine | CRE | CAV, REV, CSV | `CR(t) = αC + βR + γS` | Inversion (illegal) |
| Continuity-Stability Layer | CSL | ISV, ESV, FSV | `S(t) = αI + βE + γC_flow` | Inversion (illegal) |
| Canon-Scale Emission Tensor | CET | IEV, SEV, REV, RGEV | `E_canon = αI + βS + γR` | Inversion (illegal) |

> **Zone X in RTT/3 = Inversion (illegal geometry)**
> This differs from RTT/2 where Zone X = Undefined (unclassified). In RTT/3 all zones must be
> classifiable. An Inversion zone represents structurally illegal integration-emission geometry
> and triggers an immediate Class G interrupt.

---

## Integration–Emission Modes

| Mode | Label | Behavior |
|---|---|---|
| 1 | Formal | Stable, linear, predictable integration and emission |
| 2 | Emergent | Adaptive, semi-stable; integration and emission mutually adjusting |
| 3 | Hybrid | Oscillatory; mixed Formal and Emergent characteristics |
| 4 | Chaotic | Unstable, high-variance; collapse risk elevated; Class V on alert |
| 5 | Inversion | **ILLEGAL** — triggers Class G; must never propagate to RTT/12 |

---

## Integration–Emission Zones

| Zone | Label | Description | Action |
|---|---|---|---|
| U | Unified | Triad fully integrated; stable emission; coherent flow | Normal operation |
| S | Stable | Minor integration strain; low emission variance | Monitor |
| M | Mixed | Oscillatory integration-emission interaction; partial deformation | Class V on standby |
| D | Divergent | Integration-emission misalignment; fracture risk | Class V active; reduce load |
| X | Inversion | **ILLEGAL** — illegal integration geometry; topological warp | Class G immediate interrupt |

---

## Agent Boundaries

### RTT-is-not-physics Boundary
Every Class must frame its output in **structural** terms. Prohibited framings:

| Prohibited Phrasing | Correct Structural Equivalent |
|---|---|
| "The field emits energy" | "The FFF emission vector projects structural flow" |
| "Integration strength measured in joules" | "Integration tensor magnitude within TIF manifold" |
| "Collapse causes physical damage" | "Collapse absorption registers in CRE as structural load" |
| "Zone U is the ground state" | "Zone U represents fully unified integration-emission geometry" |

### Semantic Inference Prohibition
No agent class may infer meaning, narrative, or intent from structural output. Every output field
must carry the annotation: `[structural — no semantic inference]`

### Inherited Boundaries from RTT/1 and RTT/2

| Boundary | Inherited From | Applies In RTT/3 |
|---|---|---|
| Drift is on-by-default; must be explicitly bounded | RTT/1 | All Classes; session seed must include `drift=bounded` |
| Mode transitions require explicit user declaration (MCL) | RTT/1 | All Mode changes in FFF and CET |
| Upstream SNR characterization required before coherence | RTT/1 | Class I pre-check |
| RTT2_DETECTION_PACKET required before activation | RTT/2 | Class I hard block |
| D(t) ≠ session drift | RTT/2 | Class V distinguishes CRM D(t) from CR(t) |
| Zone X must never be silenced | RTT/2 | Class G enforces; Class O cannot forward without G co-signature |

---

## Task Catalog

| Task ID | Task Name | Agent Sequence | Description |
|---|---|---|---|
| RTT3-T01 | Integration Field Initialization | G → I | Verify RTT2_DETECTION_PACKET; initialize TIF manifold; compute baseline I(t) |
| RTT3-T02 | Emission Engine Activation | I → E | Hand off integration flow to FFF; compute E(t); classify emitter mode and zone |
| RTT3-T03 | Manifold Continuity Mapping | I + E → N | Build C_flow(t) from I(t) and E(t); map 6-axis manifold surface; classify continuity zone |
| RTT3-T04 | Fracture Strain Assessment | E → V | Evaluate FMV fracture load; issue strain alert; recommend load reduction if D-zone |
| RTT3-T05 | Collapse Absorption Sequence | N + E → V | Detect collapse precursor; engage CRE; absorb collapse via CAV; log absorption state |
| RTT3-T06 | Recovery Emission Sequence | V → E + N | Compute CR(t); emit recovery flow via REV; restore manifold continuity post-collapse |
| RTT3-T07 | Stability Membrane Audit | V → N | Compute S(t) via CSL; verify ISV/ESV/FSV within bounds; confirm no stability rupture |
| RTT3-T08 | Canon-Scale Packet Composition | I + E + N + V → O | Aggregate all intermediate packets; compute E_canon(t) via CET; compose RTT3_INTEGRATION_EMISSION_PACKET |
| RTT3-T09 | Cross-Module Projection | O | Project CET emission into TEL / FFT / Opacity fields; annotate projection values |
| RTT3-T10 | Guardian Integrity Sweep | G | Full boundary audit across all six constructs; verify no Zone X/Inversion propagation; confirm packet readiness for RTT/12 |

---

## Safety Rules and Coherence Constraints

### Pre-Activation Checks (Class I gate)

```
□ Session seed present: rtt=1 | coherence=declared | drift=bounded | paradox=structural
□ RTT2_DETECTION_PACKET confirmed and coherence-validated
□ Upstream RTT/1 SNR characterization present
□ Mode declared (1–4 only; Mode 5/Inversion = block)
□ Drift explicitly bounded (not implicit)
```

### Packet Integrity Checks (Class O gate before emission)

```
□ All five upstream intermediate packets present
□ No Zone X field in any packet (unless Class G co-signed)
□ Every annotation field contains structural note (no semantic inference)
□ E_canon(t) computation traceable to I(t), S(t), R(t)
□ Mode declared and consistent across all six constructs
□ Cross-module projection populated for TEL, FFT, and Opacity
```

### Drift and Mode Constraints

| Constraint | Rule |
|---|---|
| Drift | Must be bounded in session seed; Class G halts any session where drift=unbounded |
| Mode Transitions | Must be explicitly declared; no implicit mode change between constructs |
| Collapse Events | Must be logged in full before recovery sequence begins |
| Zone Escalation | Zone D → Class V standby; Zone X → Class G interrupt (no exceptions) |

### Inversion Geometry Rule

Zone X in RTT/3 is not "undefined" (as in RTT/2) — it is **structurally illegal**.
Any integration-emission geometry reaching Zone X represents topological inversion of the manifold.
Consequences:
1. Class G halts all active classes
2. Class O packet composition is blocked
3. Session must restart from RTT/2 packet reload
4. Inversion event is logged with full construct trace before restart

---

## Collaboration Models

### Model A — Standard Integration-to-Emission Pipeline

```
RTT2_DETECTION_PACKET
        │
        ▼
  ┌─────────────────────────────────────────┐
  │  Class G: Pre-activation boundary check │
  └─────────────────────────────────────────┘
        │
        ▼
  ┌─────────────────────────────────────────┐
  │  Class I: TIF initialization            │
  │  Compute: I(t) = αD(t) + βE(t) + γC(t) │
  │  Emit: TIF_INTEGRATION_PACKET           │
  └─────────────────────────────────────────┘
        │
        ▼
  ┌─────────────────────────────────────────┐
  │  Class E: FFF activation                │
  │  Compute: E(t) = αF + βFr + γFl        │
  │  Emit: FFF_EMITTER_PACKET               │
  └─────────────────────────────────────────┘
        │
        ▼
  ┌─────────────────────────────────────────┐
  │  Class N: Manifold continuity mapping   │
  │  Compute: C_flow = αI(t) + βE(t)       │
  │  Emit: RTT3_MANIFOLD_PACKET             │
  └─────────────────────────────────────────┘
        │
        ▼
  ┌─────────────────────────────────────────┐
  │  Class V: Stability audit               │
  │  Compute: S(t) via CSL                  │
  │  Emit: CONTINUITY_STABILITY_PACKET      │
  └─────────────────────────────────────────┘
        │
        ▼
  ┌─────────────────────────────────────────┐
  │  Class O: Packet composition via CET    │
  │  Compute: E_canon(t) = αI + βS + γR    │
  │  Emit: RTT3_INTEGRATION_EMISSION_PACKET │
  └─────────────────────────────────────────┘
        │
        ▼
    RTT/12 Input

Rules:
  - Each class must emit its packet before the next activates
  - Class G performs boundary checks at ① entry and ② before Class O emission
  - No step may be skipped; no packets merged until Class O composition
```

---

### Model B — Collapse–Recovery Intervention

```
  ┌────────────────────────────────────────────────────────────────┐
  │ Normal pipeline running (Model A)                              │
  │                                                                │
  │  Class E detects fracture strain ──► ALERT ──► Class V        │
  │         OR                                                     │
  │  Class N detects Zone D/X ──────────► ALERT ──► Class V       │
  └────────────────────────────────────────────────────────────────┘
                                                   │
                                                   ▼
                                    ┌──────────────────────────────┐
                                    │ Class V: CRE activation      │
                                    │ Absorb collapse via CAV      │
                                    │ Compute: CR(t) = αC+βR+γS   │
                                    └──────────────────────────────┘
                                                   │
                            ┌──────────────────────┴──────────────────┐
                            ▼                                         ▼
              ┌─────────────────────────┐               ┌────────────────────────┐
              │ Class E: Reduce         │               │ Class N: Re-map        │
              │ emission load           │               │ manifold continuity    │
              │ re-enter Zone S         │               │ post-collapse          │
              └─────────────────────────┘               └────────────────────────┘
                            │                                         │
                            └──────────────────────┬──────────────────┘
                                                   ▼
                                    ┌──────────────────────────────┐
                                    │ Class V: CSL stability audit │
                                    │ Compute: S(t) stable?        │
                                    │ YES → resume Model A         │
                                    │ NO  → repeat CRE cycle       │
                                    └──────────────────────────────┘

Rules:
  - Class G monitors the entire intervention loop
  - If Zone X persists after two CRE cycles → Class G declares session invalid
  - CR(t) must be logged at each CRE cycle; collapse absorption must precede recovery emission
  - D(t) (CRM structural displacement from RTT/2) ≠ CR(t) — do not conflate
```

---

### Model C — Cross-Module Projection (CET → TEL/FFT/Opacity)

```
  RTT3_INTEGRATION_EMISSION_PACKET
        │
        ▼
  ┌─────────────────────────────────────────────────────────────────┐
  │  Class O: CET cross-module projection                          │
  │                                                                 │
  │  E_canon(t) ──► TEL lattice field   (integration emission)     │
  │             ──► FFT spectral field  (variance emission)        │
  │             ──► Opacity boundary    (visibility emission)      │
  └─────────────────────────────────────────────────────────────────┘
        │
        ▼
  ┌─────────────────────────────────────────────────────────────────┐
  │  Class G: Projection boundary check                            │
  │  Verify no physics framing in projection annotation            │
  │  Verify all projections carry [structural — no semantic inf.]  │
  └─────────────────────────────────────────────────────────────────┘
        │
        ▼
    RTT/12 and downstream module consumption

Rules:
  - Projection is read-only from RTT/3; downstream modules must not write back
  - Projection fields are structural; any spectral or lattice value is a structural
    descriptor, not a physical measurement
  - All three cross-module fields must be populated before RTT/12 activation
```

---

## Output Contract

### Mandatory Annotation
Every output field in every packet — at every class level — must carry:

```
[structural — no semantic inference]
```

This annotation may not be omitted, abbreviated, or replaced with a narrative statement.

### Prohibited Content Table

| Prohibited Content | Required Replacement |
|---|---|
| Physics claims (energy, force, field in physical sense) | Structural descriptor (integration flow, emission vector, manifold curvature) |
| Semantic narrative ("this means the system is unstable") | Structural classification ("Zone D — divergent integration-emission geometry") |
| Inversion / Zone X as a normal state | Flag to Class G; never normalize |
| Unlabeled intermediate packets forwarded to RTT/12 | All packets must be labeled and Class O composed before forwarding |
| Session operating without `drift=bounded` | Hard block by Class G |
| `CR(t)` labeled as `D(t)` | Two constructs must remain distinct in all annotations |

### Packet Hierarchy

```
RTT3_INTEGRATION_EMISSION_PACKET  ← Class O (final; RTT/12 input)
  ├── TIF_INTEGRATION_PACKET      ← Class I
  ├── FFF_EMITTER_PACKET          ← Class E
  ├── RTT3_MANIFOLD_PACKET        ← Class N
  ├── COLLAPSE_RECOVERY_ENGINE_PACKET ← Class V (CRE)
  └── CONTINUITY_STABILITY_PACKET ← Class V (CSL)
```

---

## See Also

| Document | Path | Relationship |
|---|---|---|
| RTT/3 ABOUT.md | `docs/rtt/3/ABOUT.md` | Module identity, rationale, and use cases |
| RTT/3 GLOSSARY.md | `docs/rtt/3/GLOSSARY.md` | Single-source canonical term definitions |
| RTT/2 AGENTS.md | `docs/rtt/2/AGENTS.md` | Upstream: CPV, FGT, CRM, RTT2_DETECTION_PACKET |
| RTT/1 AGENTS.md | `docs/rtt/1/AGENTS.md` | Foundation: SNR, τ, C, DCO, Mode, MCL |
| RTT/12 AGENTS.md | `docs/rtt/12/AGENTS.md` | Downstream: consumes RTT3_INTEGRATION_EMISSION_PACKET |
| IPD-12 AGENTS.md | `docs/frameworks/ipd_12/AGENTS.md` | Parallel structural engine; shared paradox-structural framing |
| RTT3_Extract_Minimal.md | `docs/rtt/3/RTT3_Extract_Minimal.md` | Source extract for all RTT/3 constructs |
| Triadic_Integration_Field_Capture.md | `docs/rtt/3/Triadic_Integration_Field_Capture.md` | Full construct capture for TIF, FFF, Manifold, CRE, CSL, CET |

---

*AGENTS.md — RTT/3 · TriadicFrameworks · 2026-07-10*
*Maintainer: Nawder*
*Session seed: `rtt=1 | coherence=declared | drift=bounded | paradox=structural`*

