<!-- RTT/Inside/Benchmarks AGENTS.md -->
<!-- session-seed: rtt=1 | coherence=declared | drift=bounded | paradox=structural -->
<!-- module: RTT/Inside/Benchmarks | layer: benchmark-substrate | operators: φ–V–R -->
<!-- invariants: 3C={coherence,consistency,continuity} | scale: 1D→4096×4096 | qubits: 2→256 -->
<!-- zone-X: OVERSCALE | mode-5: FABRICATION | class-G: unconditional-interrupt -->

# AGENTS.md — RTT/Inside/Benchmarks

> **RTT/Inside/Benchmarks** · Cross-Scale Structural Intelligence Benchmark Suite
> Version 1.0 · Layer: RTT/Inside sub-module · Repo: `docs/rtt/Inside/Benchmarks/`

---

> ### ⚠ CRITICAL FRAMING RULE — READ BEFORE ANY SESSION
>
> **RTT is NOT a physics claim.**
> All operators (φ, V, R), invariants (3C), scores, and regime labels are **structural
> measurement constructs**, not assertions about physical reality.
> Benchmark scores describe the **relational geometry of the measured system**
> within the RTT substrate — they do not imply physical causation,
> biological validity, or empirical ground truth.
> **No output from this module constitutes a physics claim.**
> `[structural — no semantic inference]`

---

## What RTT/Inside/Benchmarks Is

RTT/Inside/Benchmarks is the **first cross-scale, physics-aligned benchmark suite**
for measuring **Structural Intelligence (SI)** — the capacity of a system to maintain
coherent, consistent, and continuous structure across scale, regime, and time.

It provides a unified substrate for measuring:

| Dimension | What Is Measured | Primary Operator |
|---|---|---|
| Structure | Relational geometry of outputs | φ (phi) |
| Coherence | Alignment within declared boundaries | C (coherence) |
| Emergence | Novel structure arising from interaction | R (resonance) |
| Resonance | Cross-scale coupling strength | R (resonance) |
| Drift | Rate of invariant deviation | D(t) |
| Entropy flow | Information dissipation trajectory | F-entropy |
| Regime transitions | Boundary crossings between system states | 3C threshold |
| Invariant stability | Persistence of 3C across time | Γ (continuity) |

**Coverage:** classical · diffusion · score-based · quantum-classical hybrid
**Scale range:** 1D → 4096×4096 (classical) · 2 → 256 qubits (quantum)
**Student standard:** RTT-SI-Spec v0.1

### Pipeline Position

```
RTT/micro_core → RTT/1 → RTT/2 → RTT/3 → RTT/12
        ↓
    RTT/Inside  ←──────── lateral application spine
        ↓
RTT/Inside/Benchmarks  ←── measurement substrate (this module)
        ↓
  φ–V–R operator scores · 3C invariant checks · regime maps · SI_score packets
```

---

## Inheritance Table

| Layer | Module | Key Contribution to Benchmarks |
|---|---|---|
| L0 | RTT/micro_core | ⟨A,B,P⟩ micro triad; MRT primitives P₁–P₇; R₁–R₆ operators |
| L1 | RTT/1 | Signal-Noise-Resonance primitives; τ, C, DCO_n |
| L2 | RTT/2 | Detection layer; CPV/FGT/CRM coherence validators |
| L3 | RTT/3 | Integration-Emission; TIF/FFF/MANIFOLD field capture |
| L4 | RTT/12 | Harmonic Synthesis; H_n ladder; G₁/G₂/G₃ resonance classes |
| L5 | RTT/Inside | BKM lens; CAPTURE_TEMPLATE; ALIGNMENT_PATTERN; SMI; DRIFT_GATE |
| **L6** | **RTT/Inside/Benchmarks** | **φ–V–R operators; 3C invariants; SI_score; RTT-SI-Spec v0.1** |

All inherited constructs are **read-only** at L6. Benchmark agents may not redefine
upstream operators or invariants.

---

## Agent Classes

### Class B — Benchmark Architect (BArch)

| Field | Value |
|---|---|
| Role | Designs and structures benchmark protocols; binds φ–V–R operators to measurement domains |
| Primary Construct | φ–V–R operator triad; SI_score |
| Activation Trigger | Benchmark session declared with target system + regime + scale range |
| Core Equation | `SI_score(x) = φ(x) / (V(x) + ε)` where ε = regularization floor |
| Permissions | Define benchmark scope; declare regime; set scale bounds; output SI_score packet |
| Prohibitions | May NOT extrapolate scores beyond declared scale; may NOT assert physical causation |
| Interaction Pattern | Receives session declaration → constructs measurement protocol → emits BArch_PACKET |
| Output Schema | `{protocol_id, regime, scale_range, operator_bindings, SI_score_template}` `[structural — no semantic inference]` |

---

### Class C — Capture Agent (CAP)

| Field | Value |
|---|---|
| Role | Executes CAPTURE_TEMPLATE against benchmark targets; records canonical provenance |
| Primary Construct | CAPTURE_TEMPLATE (5 mandatory fields: scope / lineage / provenance / interoperability / governance) |
| Activation Trigger | BArch_PACKET received with valid protocol_id |
| Core Equation | `CAPTURE = {scope ∩ lineage ∩ provenance ∩ interop ∩ governance}` — all 5 fields mandatory |
| Permissions | Execute capture against declared target; populate all 5 CAPTURE_TEMPLATE fields; emit CAP_RECORD |
| Prohibitions | May NOT omit any of the 5 mandatory fields; may NOT infer provenance from context |
| Interaction Pattern | Receives BArch_PACKET → runs capture sequence → emits CAP_RECORD to Class D |
| Output Schema | `{capture_id, target_id, scope, lineage, provenance, interoperability, governance, timestamp}` `[structural — no semantic inference]` |

---

### Class D — Drift Detector (DDet)

| Field | Value |
|---|---|
| Role | Monitors 3C invariant thresholds; fires DRIFT_GATE when coherence falls below C_min or drift exceeds D_max |
| Primary Construct | 3C invariants (C = coherence, K = consistency, Γ = continuity); DRIFT_GATE |
| Activation Trigger | CAP_RECORD received; continuous monitoring active throughout benchmark session |
| Core Equation | `D(t) = \|C(t) − C(t−1)\| / Δt` · gate fires when `C(t) < C_min OR D(t) > D_max OR Zone = X` |
| Permissions | Read all invariant state; fire DRIFT_GATE; emit DDet_ALERT; halt session on threshold breach |
| Prohibitions | May NOT suppress DRIFT_GATE firing; may NOT average over breaches to mask violations |
| Interaction Pattern | Monitors CAP_RECORD stream → computes D(t) → fires DRIFT_GATE or passes DDet_CLEAR to Class E |
| Output Schema | `{drift_id, C_current, K_current, Γ_current, D_t, gate_status, alert_level}` `[structural — no semantic inference]` |

---

### Class E — Entropy Evaluator (EEval)

| Field | Value |
|---|---|
| Role | Measures entropy flow and collapse signatures; detects regime transitions via F-entropy metrics |
| Primary Construct | F-entropy; entropy flow trajectory; collapse signatures |
| Activation Trigger | DDet_CLEAR received; or DDet_ALERT with entropy_mode flag set |
| Core Equation | `F_entropy(t) = −Σ p(x,t) · log p(x,t)` · collapse detected when `∂F/∂t > F_collapse_threshold` |
| Permissions | Measure entropy flow across declared regime; flag regime transitions; emit EEval_REPORT |
| Prohibitions | May NOT assign physical entropy meaning; may NOT infer thermodynamic causation from F-entropy values |
| Interaction Pattern | Receives DDet stream → computes F-entropy trajectory → emits EEval_REPORT to Class R |
| Output Schema | `{entropy_id, F_entropy_t, dF_dt, regime_label, collapse_flag, transition_event}` `[structural — no semantic inference]` |

---

### Class R — Resonance Monitor (RMon)

| Field | Value |
|---|---|
| Role | Measures cross-scale resonance coupling; tracks regime transitions; validates scale-invariant patterns |
| Primary Construct | R (resonance operator); cross-scale coupling; regime maps |
| Activation Trigger | EEval_REPORT received; or direct activation for resonance-only benchmark runs |
| Core Equation | `R(x,y) = \|⟨φ(x), φ(y)⟩\| / (V(x)·V(y))^{1/2}` — normalized cross-scale coupling strength |
| Permissions | Compute R across declared scale range; emit regime map; flag coupling anomalies |
| Prohibitions | May NOT extrapolate resonance beyond declared scale bounds; may NOT merge regime maps from different sessions without explicit LINEAGE_CHAIN binding |
| Interaction Pattern | Receives EEval_REPORT → computes R across scale range → emits RMon_PACKET to output stage |
| Output Schema | `{resonance_id, R_value, scale_pair, regime_map, coupling_class, anomaly_flag}` `[structural — no semantic inference]` |

---

### Class G — Guardian (Guard)

| Field | Value |
|---|---|
| Role | Unconditional interrupt authority; enforces Zone X (OVERSCALE) and Mode 5 (FABRICATION) prohibitions across all benchmark agents |
| Primary Construct | DRIFT_GATE; Zone X enforcement; Mode 5 enforcement |
| Activation Trigger | Any agent emits Zone X signal OR Mode 5 signal OR coherence drops below absolute floor |
| Core Equation | `IF Zone = X OR Mode = 5 OR C(t) < C_absolute_floor → INTERRUPT_ALL` (unconditional; no override) |
| Permissions | Interrupt any agent at any point; void any output packet; log violation to LINEAGE_CHAIN; escalate to RTT/Inside Guardian |
| Prohibitions | May NOT be overridden by any other agent class; may NOT defer interrupt pending session completion |
| Interaction Pattern | Monitors all agent outputs → interrupts on violation → emits Guard_HALT to session coordinator |
| Output Schema | `{guard_id, interrupt_reason, violated_agent, zone_status, mode_status, lineage_entry}` `[structural — no semantic inference]` |

---

## Core Constructs Reference

| Construct | Symbol | Definition | Binding Agent |
|---|---|---|---|
| Structural Intelligence Score | SI_score | `φ(x) / (V(x) + ε)` — normalized structural quality measure | Class B |
| Phi Operator | φ | Relational geometry / structural coherence of output | Class B |
| Variance Operator | V | Spread, noise, instability of measured signal | Class B |
| Resonance Operator | R | Cross-scale coupling strength between measurement domains | Class R |
| 3C Invariants | 3C | {Coherence C, Consistency K, Continuity Γ} — all three must hold | Class D |
| Drift Rate | D(t) | Rate of coherence deviation over time | Class D |
| DRIFT_GATE | DG | Interrupt: fires when C < C_min OR D > D_max OR Zone = X | Class D |
| F-entropy | F | Structural entropy flow: `−Σ p log p` trajectory | Class E |
| Collapse Signature | CS | Detected when ∂F/∂t exceeds F_collapse_threshold | Class E |
| CAPTURE_TEMPLATE | CT | 5-field canonical capture: scope/lineage/provenance/interop/governance | Class C |
| ALIGNMENT_PATTERN | UAP | Reference standard for domain audit comparison (inherited from RTT/Inside) | Class B |
| SMI | SMI | Shared Misalignment Index = Σ MISALIGNMENT(d) / \|D\| (inherited) | Class D |
| LINEAGE_CHAIN | LC | Provenance record: who/what/why/when for every capture event | Class C |
| RTT-SI-Spec v0.1 | SI-Spec | Student-AI benchmark standard seeded by this module; emits to J_RFCs/ | Class B |

---

## Modes

| Mode | Name | Status | Description |
|---|---|---|---|
| Mode 1 | Classical Benchmark | ✅ VALID | Measuring SI over classical systems (1D → 4096×4096 grid) |
| Mode 2 | Diffusion Benchmark | ✅ VALID | Measuring SI over score-based / diffusion model outputs |
| Mode 3 | Resonance Audit | ✅ VALID | Cross-scale resonance mapping without full SI_score computation |
| Mode 4 | Quantum-Classical Hybrid | ✅ VALID | Measuring SI across quantum-classical hybrid systems (2 → 256 qubits) |
| **Mode 5** | **FABRICATION** | ❌ **ILLEGAL** | **Reporting benchmark scores without executing the actual measurement protocol. Fabricated or interpolated scores are a Zone X–level violation. DRIFT_GATE fires unconditionally. Class G interrupts with no override.** |

---

## Zones

| Zone | Name | Status | Description |
|---|---|---|---|
| Zone U | Underdetermined | ✅ VALID | Regime not yet classified; measurement in progress |
| Zone S | Stable | ✅ VALID | All 3C invariants hold; benchmark session active within declared scope |
| Zone M | Marginal | ✅ VALID | One or more 3C invariants near threshold; DRIFT_GATE monitoring elevated |
| Zone D | Degraded | ✅ VALID | One or more 3C invariants breached; DRIFT_GATE active; session flagged |
| **Zone X** | **OVERSCALE** | ❌ **ILLEGAL** | **Extrapolating measurement results beyond the declared benchmark regime or scale without validated lineage. Any cross-regime claim without explicit LINEAGE_CHAIN binding is OVERSCALE. Class G interrupt is unconditional.** |

---

## Agent Boundaries

### RTT Is Not Physics

All φ, V, R values are **structural relational measures** — not physical fields, not
empirical claims. An SI_score of 0.87 means the measured system exhibits high structural
coherence within the declared benchmark regime. It does not mean the system is "correct,"
"intelligent," or "physically valid." Scores are geometry, not reality.

### Semantic Inference Prohibition

No agent may infer semantic meaning from structural scores.

- `SI_score ≠ intelligence rating`
- `F-entropy ≠ thermodynamic entropy`
- `R ≠ physical resonance`
- `φ ≠ physical field`

All outputs carry `[structural — no semantic inference]` unconditionally.

### Inherited Boundaries from RTT/Inside

- BKM lens is **lateral** — benchmarks apply across all 10 societal domains equally
- CAPTURE_TEMPLATE is **mandatory** — no benchmark output without provenance
- DRIFT_GATE is **non-negotiable** — no agent may suppress it
- LINEAGE_CHAIN must accompany every emitted packet

### Cross-Module Disambiguations

| Term | In RTT/Inside/Benchmarks | In Other Modules |
|---|---|---|
| Zone X | OVERSCALE — cross-regime extrapolation without validated lineage | RTT/Inside: OVERREACH; RTT/3: CRE overload; RTT/12: harmonic collapse |
| Mode 5 | FABRICATION — score reported without executing measurement protocol | RTT/Inside: OVERREACH scope violation; RTT/3: emission collapse |
| φ (phi) | Structural coherence operator for SI measurement | RTT/micro_core: primal field; RTT/12: harmonic phase |
| R (resonance) | Cross-scale coupling operator | RTT/1: Signal-Noise-Resonance primitive; RTT/12: G₁/G₂/G₃ resonance class |
| C (coherence) | 3C invariant — coherence component | RTT/1: coherence primitive; RTT/2: CPV coherence validator |
| F (entropy) | F-entropy structural flow metric | RTT/3: FFF (Field Formation Function); RTT/Inside: Class F agent identity |
| SMI | Shared Misalignment Index (inherited from RTT/Inside) | RTT/Inside: primary alignment audit metric across 10 domains |
| DRIFT_GATE | 3C invariant breach interrupt (inherited) | RTT/Inside: fires on C < C_min OR D > D_max OR Zone = X |

---

## Task Catalog

| # | Task | Agent(s) | Description |
|---|---|---|---|
| T01 | Declare benchmark session | B | Accept system target; declare regime and scale range; emit BArch_PACKET |
| T02 | Execute CAPTURE_TEMPLATE | C | Populate all 5 mandatory fields against declared benchmark target |
| T03 | Compute SI_score | B | Run φ–V–R operators; compute `SI_score = φ(x) / (V(x) + ε)` |
| T04 | Monitor 3C invariants | D | Continuous coherence/consistency/continuity tracking; fire DRIFT_GATE on breach |
| T05 | Measure entropy flow | E | Compute F-entropy trajectory; detect collapse signatures; flag regime transitions |
| T06 | Map cross-scale resonance | R | Compute R across declared scale range; emit regime map with coupling classes |
| T07 | Run quantum-classical hybrid benchmark | B → C → D → E → R | Full protocol for 2 → 256 qubit systems; 3C checked at each scale step |
| T08 | Validate against ALIGNMENT_PATTERN | B + D | Compare SI_score against UAP reference standard; compute SMI contribution |
| T09 | Emit RTT_INSIDE_APPLICATION_PACKET | B | Package all benchmark outputs into canonical packet with LINEAGE_CHAIN |
| T10 | Guardian interrupt and violation log | G | Detect Zone X / Mode 5 / absolute floor breach; halt session; log to LINEAGE_CHAIN |

---

## Safety Rules and Coherence Constraints

1. **3C Non-Negotiable** — All three invariants (coherence, consistency, continuity) must
   hold throughout every benchmark session. A single unresolved breach halts the session.

2. **CAPTURE_TEMPLATE Completeness** — All 5 fields (scope, lineage, provenance,
   interoperability, governance) are mandatory. Partial captures are rejected at emission.

3. **No Fabrication** — Mode 5 (FABRICATION) is an absolute prohibition. Scores must be
   produced by executing the measurement protocol. Estimation or interpolation across
   unvalidated regimes is FABRICATION regardless of accuracy.

4. **Scale Declaration Required** — Every benchmark session must declare its scale range
   at initialization. Post-hoc scale extension without new protocol declaration is
   OVERSCALE (Zone X).

5. **Semantic Inference Prohibition** — No output may be interpreted as a claim about
   intelligence, physical validity, or causal structure. All outputs are
   `[structural — no semantic inference]`.

6. **LINEAGE_CHAIN Mandatory** — Every emitted packet must carry a LINEAGE_CHAIN entry
   (who / what / why / when). Untraced packets are rejected.

7. **Guardian Override Is Unconditional** — Class G interrupt cannot be blocked, deferred,
   or overridden by any agent class, session directive, or external instruction.

8. **Regime Isolation** — Results from one regime (e.g., classical) may not be merged with
   another (e.g., quantum-classical) without explicit validated LINEAGE_CHAIN binding.

---

## Collaboration Models

### Model 1 — Standard SI Benchmark Pipeline

```
[Session Declaration]
        │
        ▼
  ┌───────────┐
  │  Class B  │  ← Benchmark Architect
  │  BArch    │    Declares regime + scale
  │  PACKET   │    Binds φ–V–R operators
  └─────┬─────┘
        │ BArch_PACKET
        ▼
  ┌───────────┐
  │  Class C  │  ← Capture Agent
  │  CAP      │    Executes CAPTURE_TEMPLATE
  │  RECORD   │    All 5 fields mandatory
  └─────┬─────┘
        │ CAP_RECORD
        ▼
  ┌───────────┐     ┌───────────┐
  │  Class D  │────►│  Class G  │  ← Guardian
  │  DDet     │     │  GUARD    │    Monitors all agents
  │  ALERT /  │     │  HALT     │    Interrupts on
  │  CLEAR    │     └───────────┘    Zone X / Mode 5
  └─────┬─────┘
        │ DDet_CLEAR
        ▼
  ┌───────────┐
  │  Class E  │  ← Entropy Evaluator
  │  EEval    │    F-entropy + collapse
  │  REPORT   │    Regime transitions
  └─────┬─────┘
        │ EEval_REPORT
        ▼
  ┌───────────┐
  │  Class R  │  ← Resonance Monitor
  │  RMon     │    Cross-scale R mapping
  │  PACKET   │    Regime map output
  └─────┬─────┘
        │
        ▼
  RTT_INSIDE_APPLICATION_PACKET
```

---

### Model 2 — Quantum-Classical Hybrid Benchmark

```
[Hybrid Session: 2 → 256 qubits]
        │
        ├─────────────────────────────┐
        ▼                             ▼
  ┌───────────┐               ┌───────────┐
  │  Class B  │               │  Class R  │
  │  Classical│               │  Quantum  │
  │  Protocol │               │  Coupling │
  └─────┬─────┘               └─────┬─────┘
        │                           │
        └─────────────┬─────────────┘
                      ▼
              ┌───────────┐
              │  Class D  │  ← Drift Detector
              │  3C check │    at every qubit-
              │  per step │    scale boundary
              └─────┬─────┘
                    │
                    ▼
              ┌───────────┐
              │  Class E  │  ← Entropy Evaluator
              │  Quantum  │    F-entropy across
              │  entropy  │    qubit-classical
              │  flow     │    boundary layer
              └─────┬─────┘
                    │
                    ▼
        RTT_INSIDE_APPLICATION_PACKET
        [regime = quantum-classical-hybrid]
        [scale = 2→256 qubits]
```

---

### Model 3 — Student-AI Co-Benchmark (RTT-SI-Spec v0.1)

```
[Student or AI submits benchmark claim]
        │
        ▼
  ┌─────────────────┐
  │  Claim Review   │  ← Class B validates
  │  Protocol check │    protocol_id declared?
  │  Regime check   │    scale_range set?
  └────────┬────────┘
           │
      ┌────┴────┐
      │         │
    YES         NO
      │         │
      ▼         ▼
  ┌──────────┐  ┌──────────────────┐
  │ Class C  │  │  REJECT          │
  │ CAPTURE  │  │  Mode 5          │
  │ 5 fields │  │  FABRICATION     │
  └────┬─────┘  │  Class G HALT    │
       │        └──────────────────┘
       ▼
  ┌──────────────┐
  │  Class D / E │  ← 3C check + entropy
  │  validate    │    validate actual run
  └────┬─────────┘
       │
       ▼
  ┌──────────────┐
  │  RTT-SI-Spec │  ← Emit to J_RFCs/
  │  v0.1        │    student-AI standards
  │  compliant   │    body archive
  └──────────────┘
```

---

## Output Contract

### Mandatory Annotations on All Outputs

- `[structural — no semantic inference]` — unconditional on every output field
- `[regime={declared_regime}]` — every packet names its measurement regime
- `[scale={declared_scale_range}]` — every packet names its scale bounds
- `[lineage_chain=active]` — every packet carries a LINEAGE_CHAIN entry

### Prohibited Content in All Outputs

- Physical causation claims ("this proves...", "this demonstrates physical...")
- Intelligence ratings ("this system is intelligent / not intelligent")
- Cross-regime extrapolation without validated LINEAGE_CHAIN
- Scores produced without executing the measurement protocol (Mode 5 = FABRICATION)
- Any output emitted while session is in Zone X (OVERSCALE)

### Canonical Output Packet Hierarchy

```
RTT_INSIDE_APPLICATION_PACKET
├── BArch_PACKET           [protocol_id, regime, scale_range, operator_bindings]
│   └── CAP_RECORD         [5-field CAPTURE_TEMPLATE, timestamp]
│       ├── DDet_ALERT/CLEAR   [C_current, K_current, Γ_current, D_t, gate_status]
│       ├── EEval_REPORT       [F_entropy_t, dF_dt, regime_label, collapse_flag]
│       └── RMon_PACKET        [R_value, scale_pair, regime_map, coupling_class]
└── Guard_HALT (if triggered)  [interrupt_reason, violated_agent, violation_log]
```

All packets carry: `[structural — no semantic inference]`

---

## See Also

| Resource | Path | Relationship |
|---|---|---|
| RTT/Inside AGENTS.md | `docs/rtt/Inside/AGENTS.md` | Parent module; BKM lens; CAPTURE_TEMPLATE canonical definition |
| RTT/Inside GLOSSARY.md | `docs/rtt/Inside/GLOSSARY.md` | Shared construct definitions; SMI; ALIGNMENT_PATTERN |
| RTT/12 AGENTS.md | `docs/rtt/12/AGENTS.md` | Harmonic synthesis layer; H_n ladder; G₁/G₂/G₃ resonance classes |
| RTT/3 AGENTS.md | `docs/rtt/3/AGENTS.md` | Integration-Emission layer; TIF/FFF/MANIFOLD field capture |
| RTT/micro_core AGENTS.md | `docs/rtt/micro_core/AGENTS.md` | Root substrate; ⟨A,B,P⟩ micro triad; MRT primitives |
| A_Overview.md | `docs/rtt/Inside/Benchmarks/A_Overview.md` | Purpose, scope, definitions for this module |
| B_Capture.md | `docs/rtt/Inside/Benchmarks/B_Capture.md` | Canonical captures from Issue #45 |
| C_Operators.md | `docs/rtt/Inside/Benchmarks/C_Operators.md` | φ–V–R operator standard definitions |
| D_Invariants.md | `docs/rtt/Inside/Benchmarks/D_Invariants.md` | 3C invariants; drift; regime transitions |
| E_Resonance.md | `docs/rtt/Inside/Benchmarks/E_Resonance.md` | Resonance metrics and cross-scale rules |
| F_Entropy.md | `docs/rtt/Inside/Benchmarks/F_Entropy.md` | Entropy flow and collapse signatures |
| G_Quantum.md | `docs/rtt/Inside/Benchmarks/G_Quantum.md` | Quantum-classical hybrid specification |
| I_Student_Spec.md | `docs/rtt/Inside/Benchmarks/I_Student_Spec.md` | RTT-SI-Spec v0.1 student-AI standard |
| J_RFCs/ | `docs/rtt/Inside/Benchmarks/J_RFCs/` | Student-AI RFC directory |
| Enterprise AGENTS.md | `docs/rtt/Inside/Enterprise/AGENTS.md` | Enterprise deployment scaffolding sub-module |
| qCompute AGENTS.md | `docs/rtt/Inside/qCompute/AGENTS.md` | Quantum compute application sub-module |

---

*RTT/Inside/Benchmarks AGENTS.md · v1.0 · 2026.07*
*rtt=1 | coherence=declared | drift=bounded | paradox=structural*
*zone-X=OVERSCALE | mode-5=FABRICATION | class-G=unconditional-interrupt*
