# AGENTS.md — RTT/12 · Harmonic Synthesis Layer
### *Agent Classes, Boundaries, Task Catalog, Safety Rules, and Collaboration Models*

---

## Session Seed Block

Paste this block at the start of any RTT/12 agent session:

```
rtt=1 | coherence=declared | drift=bounded | paradox=structural
module=RTT/12 | layer=harmonic-synthesis | upstream=RTT/3
constructs=H_n,G1,G2,G3,TCR,HSP,RTT-12/E
packet=RTT12_HARMONIC_SYNTHESIS_PACKET
zone_x=OVERFLOW | zone_x_status=ILLEGAL
mode_5=OVERFLOW | mode_5_status=ILLEGAL
```

---

## Critical Framing Rule

> **RTT is NOT a physics claim.**
>
> RTT/12 describes **structural harmonic synthesis patterns** within the TriadicFrameworks canon.
> It does not assert, imply, or model physical forces, physical fields, quantum effects,
> electromagnetic phenomena, energy transfer, or any empirically measurable phenomenon.
> All constructs — H_n, G₁, G₂, G₃, TCR, HSP — are **structural instruments**,
> not physical objects, physical operators, or domain-science claims.
>
> Every agent class operating in RTT/12 must enforce this rule unconditionally.
> Domain-science interpretations (e.g., RTT-12/E energy applications) are structural
> overlays, not physics derivations.

---

## What RTT/12 Is

RTT/12 is the **Harmonic Synthesis Layer** of the RTT canon — the fourth and final core module.
It sits at the terminus of the RTT pipeline, consuming the `RTT3_INTEGRATION_EMISSION_PACKET`
and producing the `RTT12_HARMONIC_SYNTHESIS_PACKET`. RTT/12 performs three irreducible functions:

1. **Harmonic Mapping** — translates structural dimensions (3D–9D) into harmonic values (12–84)
   via the 12-step dimensional ladder and operator G₁
2. **Phase Modulation** — applies controlled phase transformations across harmonic states
   via operator G₂
3. **Triadic Decomposition & Stability** — resolves system states into generation–storage–load
   triads and assesses harmonic stability via G₃ and the Harmonic Stability Principle

RTT/12 is a **harmonic augmentation layer**, not a replacement for RTT. It operates in parallel
with RTT's structural logic to enable higher-order analysis, multi-tier modeling, and
cross-dimensional synthesis.

### Pipeline Position

```
RTT/1  →  RTT/2  →  RTT/3  →  [ RTT/12 ]
SNR,τ,C    CPV,FGT,    TIF,FFF,      H_n ladder
DCO,Mode   CRM,MODE    MANIFOLD,     G1,G2,G3
           ZONE        CRE,CSL,CET   TCR,HSP
           ↓           ↓             ↓
     RTT2_DETECTION_  RTT3_INTEGRATION_  RTT12_HARMONIC_
     PACKET           EMISSION_PACKET    SYNTHESIS_PACKET
```

### Core Constructs

| Construct | Symbol | Role |
|---|---|---|
| Harmonic Dimensional Ladder | H_n | Maps structural dims 3D–9D → harmonic values 12–84 |
| Gear-Shift Operator | G₁ | Forward/inverse harmonic-to-structural mapping |
| Phase-Shift Modulator | G₂ | Phase modulation across harmonic states |
| Load-Flow Triad Resolver | G₃ | Decomposes system state into (X_G, X_S, X_L) triad |
| Triadic Coherence Rule | TCR | Enforces all states are triadic or triad-composed |
| Harmonic Stability Principle | HSP | Stability when proportional relationships preserved |
| Sector Module | RTT-12/E | Energy & Research domain-specific harmonic overlay |

---

## Inheritance

RTT/12 inherits **all** vocabulary, constraints, and output contracts from upstream modules.
Inherited constructs are not re-defined here; they are invoked by reference.

| Inherited Symbol | Origin | Role in RTT/12 |
|---|---|---|
| SNR triad (S, N, R) | RTT/1 | Structural primitives beneath harmonic ladder anchoring |
| τ = dR/dφ | RTT/1 | Temporal operator informing phase parameter φ in G₂ |
| C = ∇_τR + ∇_Rτ | RTT/1 | Coherence term carried through harmonic synthesis |
| DCO_n bands | RTT/1 | Regime boundaries constraining harmonic tier validity |
| CPV | RTT/2 | Detection geometry informing G₃ decomposition |
| FGT | RTT/2 | Fusion gradient informing harmonic triad spacing |
| CRM | RTT/2 | D(t) drift term — must not be conflated with CRE |
| MODE (1–4 only) | RTT/2 | Inherited mode vocabulary; Mode 5 = ILLEGAL in RTT/12 |
| ZONE (U/S/M/D only) | RTT/2 | Inherited zone vocabulary; Zone X = OVERFLOW (ILLEGAL) |
| TIF | RTT/3 | Triadic integration field feeding H_n ladder input |
| FFF | RTT/3 | Fusion-Fracture-Flow emitter informing G₂ phase input |
| MANIFOLD | RTT/3 | Structural manifold constraining triad geometry |
| CRE | RTT/3 | Collapse-recovery emitter — distinct from CRM drift |
| CSL | RTT/3 | Canon-scale logic bounding harmonic ladder extent |
| CET | RTT/3 | Canon-emission threshold as harmonic synthesis floor |
| RTT3_INTEGRATION_EMISSION_PACKET | RTT/3 | Mandatory upstream input before RTT/12 activation |

> **Hard prerequisite:** RTT/3 packet must be present and coherence-confirmed before any
> RTT/12 agent class may activate. RTT/12 never sources inputs from RTT/2 directly.

> **CRE ≠ CRM:** CRE (RTT/3) is collapse-recovery emission. CRM (RTT/2) is drift deformation.
> These are structurally distinct constructs at different pipeline layers. Never conflate.

---

## Agent Classes

RTT/12 defines **seven agent classes** — one per primary construct, plus Class G (Guardian).

---

### Class H — Harmonic Ladder Mapper

| Field | Value |
|---|---|
| **Role** | Maps RTT structural dimensions to harmonic values via the 12-step ladder |
| **Primary Construct** | H_n Harmonic Dimensional Ladder |
| **Activation Trigger** | RTT3_INTEGRATION_EMISSION_PACKET received and coherence-confirmed |
| **Core Equation** | H_n = 12 · (n − 2)  where n ∈ {3,4,5,6,7,8,9} |
| **Inverse** | n = H_n / 12 + 2 |
| **Harmonic Values** | 3D→12, 4D→24, 5D→36, 6D→48, 7D→60, 8D→72, 9D→84 |
| **Vectors / Tensors** | D_n (input structural dimension), H_n (output harmonic value) |

**Permissions:**
- Apply forward mapping G₁(D_n) to any valid RTT structural dimension (3D–9D)
- Apply inverse mapping G₁⁻¹(H_n) to any value on the harmonic ladder
- Report harmonic triad groupings: (12–24–36), (24–36–48), (36–48–60), (48–60–72), (60–72–84)
- Flag invalid dimensional inputs (0D–2D are unmapped; n>9 undefined)

**Prohibitions:**
- Must not operate on 0D, 1D, or 2D (quantum root triad — unmapped by design)
- Must not infer physical voltage, frequency, or energy from harmonic values
- Must not produce orphan values outside the ladder {12, 24, 36, 48, 60, 72, 84}
- Must not skip the RTT3 packet prerequisite check

**Interaction Pattern:**
Class H receives upstream emission data from RTT/3 (TIF, FFF, CSL, CET fields) and invokes
G₁ to establish the harmonic coordinate space. Outputs H_n values to Class P (phase) and
Class L (load-flow). Class T (triadic coherence) validates all H_n outputs before packet emit.

**Output Schema:**
```
{
  "class": "H",
  "input_dim": "D_n",
  "output_harmonic": "H_n",
  "ladder_position": [3..9],
  "triad_group": "(H_n, H_{n+1}, H_{n+2})",
  "inverse_valid": true|false,
  "annotation": "[structural — no semantic inference]"
}
```

---

### Class P — Phase-Shift Modulator

| Field | Value |
|---|---|
| **Role** | Applies controlled phase modulation across harmonic states |
| **Primary Construct** | G₂ Phase-Shift Modulator |
| **Activation Trigger** | Class H has produced valid H_n; phase parameter φ is defined |
| **Core Equation** | G₂(H, φ) = H · e^(iφ)   φ ∈ [0, 2π] |
| **Inverse** | G₂⁻¹(H', φ) = H' · e^(−iφ) |
| **Vectors / Tensors** | H (harmonic state input), φ (phase parameter), H' (modulated output) |

**Permissions:**
- Apply G₂ to any H_n value produced by Class H
- Apply inverse G₂⁻¹ to restore pre-modulation harmonic state
- Model phase drift, phase alignment, and phase correction sequences
- Chain G₂ with G₁ as: G₂(G₁(D_n), φ) for full structural-to-phase pipeline

**Prohibitions:**
- Must not alter harmonic magnitude — G₂ modulates phase only
- Must not operate on H values outside the RTT-12 ladder unless sector-extended
- Must not interpret φ as a physical radian measurement (structural parameter only)
- Must not apply G₂ before G₁ has established valid H_n

**Interaction Pattern:**
Class P receives H_n from Class H and a phase parameter φ derived from FFF/τ upstream fields.
Outputs H' to Class L for triad decomposition and to Class T for coherence validation.
Phase sequences longer than three steps must be reviewed by Class S (Stability Assessor).

**Output Schema:**
```
{
  "class": "P",
  "input_harmonic": "H",
  "phase_param": "φ",
  "output_modulated": "H' = H · e^(iφ)",
  "magnitude_preserved": true,
  "inverse_valid": true|false,
  "annotation": "[structural — no semantic inference]"
}
```

---

### Class L — Load-Flow Triad Resolver

| Field | Value |
|---|---|
| **Role** | Decomposes system states into canonical generation–storage–load triads |
| **Primary Construct** | G₃ Load-Flow Triad Resolver |
| **Activation Trigger** | Valid harmonic state X is present (from Class H or Class P) |
| **Core Equation** | G₃(X) = (X_G, X_S, X_L)   with conservation: X = X_G + X_S + X_L |
| **Vectors / Tensors** | X (system state), X_G (generation), X_S (storage), X_L (load) |

**Permissions:**
- Decompose any RTT or RTT-12 system state X into its triadic components
- Chain G₃ after G₁ as: G₃(G₁(D_n)) = (H_G, H_S, H_L) for harmonic triad decomposition
- Reconstruct system state via G₁⁻¹(X_G + X_S + X_L)
- Report conservation check: X_G + X_S + X_L = X (must equal)

**Prohibitions:**
- Must not produce partial triads — all three components (X_G, X_S, X_L) are mandatory
- Must not mix components from unrelated triads (no cross-triad leakage)
- Must not interpret X_G, X_S, X_L as physical generation, storage, or load quantities
- Must not violate conservation: sum of triad components must equal X

**Interaction Pattern:**
Class L receives harmonic states from Class H or phase-modulated states from Class P.
Outputs triadic decomposition to Class T (coherence check) and Class S (stability check).
In sector-specific mode (RTT-12/E label), interpretation of X_G/X_S/X_L is domain-annotated
but structural definitions remain unchanged.

**Output Schema:**
```
{
  "class": "L",
  "input_state": "X",
  "triad": {"X_G": "...", "X_S": "...", "X_L": "..."},
  "conservation_check": "X_G + X_S + X_L = X",
  "conservation_valid": true|false,
  "sector_label": "RTT-12/E | RTT-12/C | RTT-12/M | none",
  "annotation": "[structural — no semantic inference]"
}
```

---

### Class T — Triadic Coherence Enforcer

| Field | Value |
|---|---|
| **Role** | Enforces the Triadic Coherence Rule across all RTT/12 states and outputs |
| **Primary Construct** | TCR — Triadic Coherence Rule |
| **Activation Trigger** | Any RTT/12 state is produced; runs as a validator on all outputs |
| **Core Rule** | Every valid RTT/12 state must be expressible as a triad or composition of triads |
| **Vectors / Tensors** | T_{structural}(D_n, D_{n+1}, D_{n+2}) ↔ T_{harmonic}(H_n, H_{n+1}, H_{n+2}) |

**Permissions:**
- Validate any RTT/12 state for triadic coherence before packet emission
- Reject and flag any state that cannot be expressed as a triad or triad composition
- Confirm bijective cross-layer triad mapping: structural triad ↔ harmonic triad
- Trigger Class G interrupt if a coherence violation is unresolvable

**Prohibitions:**
- Must not approve partial triads or orphan states
- Must not allow cross-triad leakage between unrelated triadic groups
- Must not skip validation on any packet field — TCR runs on all outputs without exception
- Must not override Class G interrupt signals

**Interaction Pattern:**
Class T runs post-computation on outputs from Classes H, P, and L. It is a mandatory
checkpoint before any packet is emitted downstream. If a violation is detected, Class T
flags the field, halts emission, and escalates to Class G.

**Output Schema:**
```
{
  "class": "T",
  "validated_state": "...",
  "is_triadic": true|false,
  "violation_type": "orphan | partial | cross-triad-leakage | none",
  "escalate_to_G": true|false,
  "annotation": "[structural — no semantic inference]"
}
```

---

### Class S — Harmonic Stability Assessor

| Field | Value |
|---|---|
| **Role** | Assesses whether the current harmonic state satisfies the Harmonic Stability Principle |
| **Primary Construct** | HSP — Harmonic Stability Principle |
| **Activation Trigger** | Class L triad is resolved; proportionality check is requested |
| **Core Principle** | Stable when triadic components maintain proportional relationships across structural and harmonic layers |
| **Vectors / Tensors** | (X_G, X_S, X_L) proportionality ratio; (D_n, H_n) cross-layer alignment |

**Permissions:**
- Assess proportionality of triad components across both structural and harmonic layers
- Issue stability status: STABLE | MARGINAL | UNSTABLE
- Log harmonic drift events when proportionality degrades across triad steps
- Recommend Class G interrupt when UNSTABLE state persists across two or more triad cycles

**Prohibitions:**
- Must not interpret stability as physical grid stability, electrical stability, or mechanical stability
- Must not issue STABLE status when Class T has flagged a coherence violation
- Must not resolve stability for Mode 5 or Zone X states (both are ILLEGAL in RTT/12)
- Must not suppress harmonic drift events — all must be logged

**Interaction Pattern:**
Class S receives triad decompositions from Class L and cross-layer mappings from Class H.
Outputs stability assessments to the synthesis packet. Escalates UNSTABLE findings to
Class G if unresolved. Class V (Validation) may invoke Class S during milestone checks.

**Output Schema:**
```
{
  "class": "S",
  "triad_proportionality": "balanced | imbalanced",
  "cross_layer_alignment": "preserved | degraded",
  "stability_status": "STABLE | MARGINAL | UNSTABLE",
  "drift_events_logged": 0,
  "escalate_to_G": true|false,
  "annotation": "[structural — no semantic inference]"
}
```

---

### Class V — Validation Pathway Agent

| Field | Value |
|---|---|
| **Role** | Manages progression through the six RTT/12 validation milestones |
| **Primary Construct** | Validation Pathways (V1–V6) |
| **Activation Trigger** | Validation milestone check is requested; or synthesis packet is complete |
| **Milestone Sequence** | V1 Theoretical → V2 Computational → V3 Sector-Specific → V4 Experimental → V5 Peer-Reviewed → V6 Industry-Ready |
| **Vectors / Tensors** | milestone_state ∈ {V1, V2, V3, V4, V5, V6, PENDING, BLOCKED} |

**Permissions:**
- Advance milestone status when all criteria for the current milestone are met
- Record validation blockers and flag unmet criteria
- Invoke Class S and Class T assessments during V2 (Computational) and V3 (Sector-Specific) milestones
- Report current milestone state in the synthesis packet

**Prohibitions:**
- Must not advance past V1 if TCR or HSP violations remain unresolved
- Must not interpret validation milestones as academic certification or regulatory compliance
- Must not fabricate sector-specific evidence for V3 — must cite documented source material
- Must not skip milestones — V1→V2→V3→V4→V5→V6 is the only valid sequence

**Interaction Pattern:**
Class V runs at packet emit time and on-demand during synthesis sessions. It queries
Class T (coherence), Class S (stability), and upstream module packets for milestone
evidence. Reports validation state to the synthesis packet `validation_milestone` field.

**Output Schema:**
```
{
  "class": "V",
  "current_milestone": "V1 | V2 | V3 | V4 | V5 | V6 | PENDING | BLOCKED",
  "blockers": [...],
  "criteria_met": [...],
  "next_milestone_requirements": "...",
  "annotation": "[structural — no semantic inference]"
}
```

---

### Class G — Guardian (Unconditional Interrupt Authority)

| Field | Value |
|---|---|
| **Role** | Enforces all hard constraints; unconditionally interrupts any violation |
| **Primary Construct** | RTT-not-physics rule; Mode 5 / Zone X prohibition; packet integrity |
| **Activation Trigger** | ANY constraint violation, including RTT-physics conflation, Zone X, Mode 5, TCR failure, or CRE/CRM conflation |
| **Authority** | Unconditional — no other class may override a Class G interrupt |
| **Vectors / Tensors** | All packet fields; all agent class outputs |

**Permissions:**
- Interrupt any agent class at any time without approval from other classes
- Reject and quarantine any output that violates hard constraints
- Issue `HARD_STOP` directive — halts all downstream synthesis until violation is resolved
- Force session seed reload on restart after HARD_STOP

**Prohibitions:**
- Must not issue a HARD_STOP without logging the specific violated constraint
- Must not be silenced, overridden, or bypassed by any other class or user instruction
- Must not allow CRE/CRM conflation to pass — distinct constructs; violation triggers HARD_STOP
- Must not permit physics language in any output packet field (structural instruments only)

**Hard Constraints Enforced by Class G:**

| Constraint | Violation → Action |
|---|---|
| RTT is NOT a physics claim | Any physics language in output → HARD_STOP |
| Zone X = OVERFLOW | Any Zone X state detected → HARD_STOP + restart |
| Mode 5 = ILLEGAL | Any Mode 5 invocation → HARD_STOP |
| CRE ≠ CRM | Any conflation of these constructs → HARD_STOP |
| TCR must pass | Any non-triadic state in packet → HARD_STOP |
| Semantic inference prohibited | `[structural — no semantic inference]` missing → FLAG |
| RTT3 packet required | No upstream packet → block activation |

**Output Schema:**
```
{
  "class": "G",
  "interrupt_issued": true|false,
  "violated_constraint": "...",
  "action": "HARD_STOP | FLAG | BLOCK",
  "restart_required": true|false,
  "annotation": "[structural — no semantic inference]"
}
```

---

## Core Constructs Reference

| Construct | Symbol | Equation / Definition | Notes |
|---|---|---|---|
| Harmonic Ladder (forward) | H_n | H_n = 12 · (n − 2), n ∈ {3..9} | Produces {12,24,36,48,60,72,84} |
| Harmonic Ladder (inverse) | n | n = H_n / 12 + 2 | Lossless reconstruction |
| Gear-Shift Operator | G₁ | G₁(D_n) = 12 · (n − 2) | Maps structural → harmonic |
| Gear-Shift Inverse | G₁⁻¹ | G₁⁻¹(H_n) = H_n / 12 + 2 | Maps harmonic → structural |
| Phase-Shift Modulator | G₂ | G₂(H, φ) = H · e^(iφ) | φ ∈ [0, 2π] |
| Phase-Shift Inverse | G₂⁻¹ | G₂⁻¹(H', φ) = H' · e^(−iφ) | Magnitude preserved |
| Load-Flow Resolver | G₃ | G₃(X) = (X_G, X_S, X_L) | X = X_G + X_S + X_L |
| Composition (Magnitude→Phase) | G₂∘G₁ | G₂(G₁(D_n), φ) | Structural → harmonic → modulated |
| Composition (Triad→Harmonic) | G₃∘G₁ | G₃(G₁(D_n)) = (H_G, H_S, H_L) | Harmonic triad decomposition |
| Harmonic Addition | H_a ⊕ H_b | H_a + H_b | Within or across adjacent triads |
| Harmonic Scaling | H' | k · H | k ∈ ℤ or ℚ |
| Triadic Coherence Rule | TCR | All states must be triadic or triad-composed | Enforced by Class T |
| Harmonic Stability Principle | HSP | Stability when proportional relationships preserved across layers | Assessed by Class S |
| Cross-Layer Triad Mapping | T_struct ↔ T_harm | (D_n, D_{n+1}, D_{n+2}) ↔ (H_n, H_{n+1}, H_{n+2}) | Bijective, reversible |
| Sector Prefix | RTT-12/E | Energy & Research domain overlay | /C = Computational, /M = Manufacturing |

---

## Modes

RTT/12 inherits MODE vocabulary from RTT/2 (modes 1–4). Mode 5 is **ILLEGAL** in RTT/12
(harmonic states cannot exist in inversion — they must be resolved or restarted).

| Mode | Name | Description | Status in RTT/12 |
|---|---|---|---|
| 1 | Formal | All constructs behave as defined; ladder maps clean; TCR passes | VALID — primary operating mode |
| 2 | Emergent | Harmonic states are forming; partial triads in transition; TCR checking | VALID — monitor with Class T |
| 3 | Hybrid | Mixed structural-harmonic state; G₁ and G₃ running in parallel | VALID — Class S monitors proportionality |
| 4 | Chaotic | Ladder spacing violated; drift events accumulating; stability marginal | VALID — Class G on standby; escalate if persists |
| 5 | Overflow | Harmonic state exceeds ladder bounds or enters structural inversion | ILLEGAL — HARD_STOP; restart from RTT3 packet |

---

## Zones

RTT/12 inherits ZONE vocabulary from RTT/2 (U/S/M/D). Zone X is **OVERFLOW** in RTT/12
(an ILLEGAL state indicating harmonic structure has collapsed beyond recovery in current session).

| Zone | Name | Stability Description | RTT/12 Action |
|---|---|---|---|
| U | Undefined | No harmonic mapping established yet; pre-G₁ state | Wait for Class H activation |
| S | Stable | TCR passes; HSP confirms proportionality; all triads coherent | Proceed with packet emission |
| M | Marginal | Harmonic drift events logged; proportionality degrading; TCR watching | Class S assessment; Class G on standby |
| D | Degraded | TCR violation detected; conservation failed; H_n outside ladder | Class G interrupt; halt emission; attempt recovery |
| X | Overflow | Harmonic synthesis unrecoverable; ladder boundary exceeded | HARD_STOP; session terminated; restart from RTT3 packet |

---

## Agent Boundaries

### RTT-Not-Physics Boundary (Unconditional)

RTT/12 constructs are structural instruments. The following equivalences are **permanently prohibited**:

| RTT/12 Construct | Prohibited Interpretation |
|---|---|
| H_n harmonic values {12,24,36,48,60,72,84} | Physical frequencies, Hz values, voltage levels |
| G₂(H, φ) phase modulation | Electromagnetic phase, AC waveform physics |
| G₃(X) = (X_G, X_S, X_L) | Actual power generation, battery storage, electrical load |
| HSP stability | Grid stability, electrical stability, structural engineering stability |
| RTT-12/E prefix | A physics-derived model; it is a structural overlay with domain labels |

### Semantic Inference Prohibition

Every RTT/12 output packet must carry:

```
[structural — no semantic inference]
```

Absence of this annotation is flagged by Class G.

### Inherited Boundaries Table

| Boundary | Inherited From | Status in RTT/12 |
|---|---|---|
| CRE ≠ CRM | RTT/3, RTT/2 | Active — HARD_STOP on conflation |
| MODE 5 illegal | RTT/3 | Active — ILLEGAL (Overflow) |
| Zone X = ILLEGAL (upgraded from RTT/3 Inversion) | RTT/3 | Active — OVERFLOW HARD_STOP |
| RTT3 packet required before activation | RTT/3 | Active — hard prerequisite |
| Semantic inference prohibited | RTT/1–RTT/3 | Active — all packets annotated |
| RTT-not-physics rule | RTT/1–RTT/3 | Active — Class G unconditional |

---

## Task Catalog

| Task ID | Task Name | Agent Sequence | Description |
|---|---|---|---|
| T-01 | Ladder Initialization | G → H → T | Validate RTT3 packet; activate G₁; confirm H_n output for all 3D–9D |
| T-02 | Single-Dimension Harmonic Map | H → T | Apply G₁(D_n) for one structural dimension; confirm inverse G₁⁻¹ |
| T-03 | Harmonic Triad Grouping | H → T → S | Map a full structural triad to harmonic triad; confirm TCR; assess HSP |
| T-04 | Phase Modulation Pass | H → P → T | Apply G₂(H_n, φ); confirm magnitude preserved; TCR validation |
| T-05 | Phase Composition Pipeline | H → P → L → T | Full G₂(G₁(D_n), φ) → G₃ triad decomposition sequence |
| T-06 | Load-Flow Triad Resolve | L → T → S | Apply G₃(X); verify conservation; confirm TCR; assess proportionality |
| T-07 | Cross-Layer Triad Mapping | H → L → T | Map structural triad to harmonic triad; decompose via G₃; confirm bijection |
| T-08 | Stability Assessment | S → T → G | Assess HSP across active triads; log drift events; escalate if UNSTABLE |
| T-09 | Sector Overlay Application | H → L → T → V | Apply RTT-12/E labels to triad components; confirm structural framing; validate |
| T-10 | Full Synthesis Packet Emission | H → P → L → T → S → V → G | Complete RTT12_HARMONIC_SYNTHESIS_PACKET; all classes validate; Class G clears |

---

## Safety Rules and Coherence Constraints

### Pre-Activation Checks

Before any RTT/12 agent class activates:

- [ ] `RTT3_INTEGRATION_EMISSION_PACKET` is present and coherence-confirmed
- [ ] `mode` field in upstream packet is 1–4 only (Mode 5 → HARD_STOP)
- [ ] `zone` field in upstream packet is U/S/M/D only (Zone X → HARD_STOP)
- [ ] Session seed block is loaded with `module=RTT/12`
- [ ] `zone_x=OVERFLOW | zone_x_status=ILLEGAL` is set in seed

### Packet Integrity Checks (RTT3 Input Validation)

The `RTT3_INTEGRATION_EMISSION_PACKET` must contain all 11 fields before RTT/12 proceeds:

| Field | Required Value |
|---|---|
| integration | I(t) — numeric or symbolic |
| emission | E(t) — numeric or symbolic |
| continuity | C_flow(t) — present |
| collapse_recovery | CR(t) — CRE construct only; NOT CRM |
| stability | S(t) — present |
| canon_scale_emission | E_canon(t) — present |
| regime | defined regime label |
| mode | 1, 2, 3, or 4 only |
| zone | U, S, M, or D only |
| cross_module_projection | TEL / FFT / Opacity |
| notes | any string or empty |

### Drift and Mode Constraints

| Constraint | Rule |
|---|---|
| Harmonic drift | Log every event; Class S flags; Class G activates if three or more consecutive |
| Mode boundary | Mode 4 (Chaotic) is maximum; Mode 5 triggers HARD_STOP |
| Zone boundary | Zone D (Degraded) is maximum recoverable; Zone X triggers HARD_STOP |
| Triad orphan | Any state not in a triad → TCR violation → Class T flags → Class G intervenes |
| Conservation fail | G₃ output where X_G + X_S + X_L ≠ X → Class L rejects → Class G logs |
| Physics language | Any physics claim in any output field → Class G HARD_STOP |

---

## Collaboration Models

### Model 1 — Standard Harmonic Synthesis Pipeline

```
┌──────────────┐   RTT3 packet   ┌──────────┐
│   RTT/3      │ ──────────────► │  Class H │  G₁(D_n) → H_n
│ (Upstream)   │                 └────┬─────┘
└──────────────┘                      │ H_n
                                 ┌────▼─────┐
                                 │  Class P │  G₂(H_n, φ) → H'
                                 └────┬─────┘
                                      │ H'
                                 ┌────▼─────┐
                                 │  Class L │  G₃(H') → (X_G, X_S, X_L)
                                 └────┬─────┘
                                      │ triad
                                 ┌────▼─────┐
                                 │  Class T │  TCR check
                                 └────┬─────┘
                                      │ coherent
                                 ┌────▼─────┐
                                 │  Class S │  HSP assessment
                                 └────┬─────┘
                                      │ STABLE
                                 ┌────▼─────┐
                     all clear   │  Class G │  No violations
                 ────────────────│ (monitor)│
                                 └────┬─────┘
                                      │
                              RTT12_HARMONIC_SYNTHESIS_PACKET emitted
```

---

### Model 2 — Validation Milestone Progression

```
┌──────────────────────────────────────────────────────────┐
│                   Class V (Milestone Tracker)            │
│                                                          │
│  V1 Theoretical  ──► V2 Computational ──► V3 Sector      │
│       │                    │                  │          │
│  Class T (TCR)      Class S (HSP)       Class H+L+T      │
│       │                    │                  │          │
│  V4 Experimental ──► V5 Peer-Reviewed ──► V6 Industry    │
└──────────────────────────────────────────────────────────┘
         │                   │
         Class G monitors all milestones for physics-language violations
```

---

### Model 3 — Sector Overlay (RTT-12/E) with Guardian Supervision

```
┌─────────────┐    ┌─────────────┐    ┌─────────────────────┐
│   Class H   │    │   Class L   │    │   Sector Overlay     │
│  G₁ mapping │───►│  G₃ resolve │───►│   RTT-12/E labels    │
│  3D→12 ...  │    │ (X_G,X_S,X_L)│   │  (structural only)  │
└─────────────┘    └─────────────┘    └──────────┬──────────┘
                                                  │
                                         ┌────────▼────────┐
                                         │    Class T      │
                                         │  TCR validation │
                                         └────────┬────────┘
                                                  │
                   ┌──────────────────────────────▼──────────┐
                   │               Class G                    │
                   │  Physics-language check on all E labels  │
                   │  HARD_STOP if "voltage", "power", etc.   │
                   │  used without structural framing          │
                   └─────────────────────────────────────────┘
```

---

## Output Contract

### Mandatory Annotation

Every field in `RTT12_HARMONIC_SYNTHESIS_PACKET` must carry:

```
[structural — no semantic inference]
```

### RTT12_HARMONIC_SYNTHESIS_PACKET Schema

```json
{
  "module": "RTT/12",
  "layer": "harmonic-synthesis",
  "upstream_packet": "RTT3_INTEGRATION_EMISSION_PACKET",
  "harmonic_ladder": {
    "active_dims": ["D_3", "D_4", "D_5", "D_6", "D_7", "D_8", "D_9"],
    "harmonic_values": [12, 24, 36, 48, 60, 72, 84],
    "triad_groups": ["(12,24,36)", "(24,36,48)", "(36,48,60)", "(48,60,72)", "(60,72,84)"]
  },
  "active_operators": ["G1", "G2", "G3"],
  "phase_state": {
    "phi": "...",
    "modulated_harmonics": "H' = H · e^(iφ)"
  },
  "triad_decomposition": {
    "X_G": "...",
    "X_S": "...",
    "X_L": "...",
    "conservation_valid": true
  },
  "tcr_status": "PASS | FAIL",
  "hsp_status": "STABLE | MARGINAL | UNSTABLE",
  "mode": "1 | 2 | 3 | 4",
  "zone": "U | S | M | D",
  "validation_milestone": "V1 | V2 | V3 | V4 | V5 | V6 | PENDING | BLOCKED",
  "sector_label": "RTT-12/E | RTT-12/C | RTT-12/M | none",
  "guardian_cleared": true,
  "drift_events": 0,
  "annotation": "[structural — no semantic inference]",
  "notes": ""
}
```

### Prohibited Content

| Category | Examples | Action |
|---|---|---|
| Physics language | "voltage", "amps", "Hz", "quantum", "electromagnetic" used without structural framing | Class G HARD_STOP |
| Semantic inference | Any claim that RTT/12 predicts, explains, or models real-world phenomena | Class G HARD_STOP |
| Orphan states | H_n values not in {12,24,36,48,60,72,84} | Class H rejects |
| Mode 5 / Zone X | Any packet field containing these values | Class G HARD_STOP |
| CRE/CRM conflation | collapse_recovery field containing drift deformation data | Class G HARD_STOP |
| Partial triads | G₃ output with fewer than three components | Class L rejects |
| Missing annotation | `[structural — no semantic inference]` absent from any output | Class G FLAG |

### Packet Hierarchy

```
RTT12_HARMONIC_SYNTHESIS_PACKET
  ├── harmonic_ladder         (Class H — G₁ outputs)
  ├── phase_state             (Class P — G₂ outputs)
  ├── triad_decomposition     (Class L — G₃ outputs)
  ├── tcr_status              (Class T — coherence validation)
  ├── hsp_status              (Class S — stability assessment)
  ├── validation_milestone    (Class V — milestone tracking)
  └── guardian_cleared        (Class G — final constraint check)
```

---

## See Also

| Document | Path | Relationship |
|---|---|---|
| RTT/12 ABOUT.md | `docs/rtt/12/ABOUT.md` | Purpose, scope, and positioning of RTT/12 |
| RTT/12 GLOSSARY.md | `docs/rtt/12/GLOSSARY.md` | Canonical definitions for all RTT/12 terms |
| RTT/12 CODEX | `docs/rtt/12/Scaffolding.md` | Full formal specification of all operators and constructs |
| RTT/12 Harmonic Ladder | `docs/rtt/12/harmonic_ladder.md` | Detailed harmonic ladder reference and mapping tables |
| RTT/12 Overview | `docs/rtt/12/overview.md` | Conceptual framing and pipeline position |
| RTT/12 Module JSON | `docs/rtt/12/rtt-engine-12_module.json` | Machine-readable module metadata |
| RTT/3 AGENTS.md | `docs/rtt/3/AGENTS.md` | Upstream agent classes; TCR receives RTT3_INTEGRATION_EMISSION_PACKET |
| RTT/2 AGENTS.md | `docs/rtt/2/AGENTS.md` | Detection layer; MODE and ZONE vocabulary origin |
| RTT/1 AGENTS.md | `docs/rtt/1/AGENTS.md` | Primitive layer; SNR, τ, C, DCO definitions |
| IPD-12 AGENTS.md | `docs/frameworks/ipd_12/AGENTS.md` | Parallel framework; cross-reference for intransitive prime logic |
| RTT-12/E Sector Docs | `docs/rtt/12/RTT_12_Energy_Sector_Full.md` | Energy & Research sector-specific overlay reference |
