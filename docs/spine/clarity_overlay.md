# Clarity Overlay
## S3 Spine · RTT::Clarity · v2.0 · R5

---

### Session Context

| Field | Value |
|---|---|
| Canon | active · s3-spine · clarity-overlay · r5 |
| Version | 2.0 |
| Coherence | declared |
| Drift | bounded |
| Generated | 2026-08-08 |
| Source | S3-Spine-Overlay-Pack-v2.0 |
| Format | spine-overlay |
| Audience | analysts · researchers · AIs · educators · framework students |
| AI-Ready | true |

**Front-door flags:** `clarity=active` · `rtt=1` · `metrics=live` · `regime=classified` · `interactive=yes`

---

### Overlay Identity

**Overlay ID:** `spine-clarity`
**Display Name:** Clarity Overlay
**Namespace:** `RTT::Clarity`
**Layer:** Cross-cutting — operates across all six S3 Spine overlays
**Canonical URL:** `https://www.triadicframeworks.org/spine/clarity/`
**Interactive Tool:** C-N-R Triad Analyzer (live instrumented app)

**Purpose statement:** The Clarity Overlay measures, scores, and repairs the epistemic clarity of any conceptual payload (φ) transmitted through or between Triadic system components. Clarity is defined along three orthogonal axes — Compression (C), Nuance (N), and Resonance (R) — and quantified via a composite score Ξ that gates payload delivery at Ξ ≥ 0.70. The overlay does not modify content; it diagnoses, classifies, and routes. It is the measurement layer between what an AI or author produces and what a receiver actually receives.

**Role in S3 Spine:** Clarity sits above the six numbered overlays as a cross-cutting diagnostic and repair layer. Any overlay output may be passed through the Clarity Field Engine before downstream consumption. At full Phase 3 deployment, every payload emitted by the spine passes through this layer before transmission.

---

### Primary RTT Engines

| Engine | Role | Function | Version |
|---|---|---|---|
| CLARITY_FIELD_ENGINE | Primary | Computes Hᵥ, Wᵥ, Iᵣ, Ξ for any payload φ; gates at Ξ ≥ 0.70 | RTT/3 |
| VALIDATOR_ENTROPY_SCANNER | Secondary | Runs V̂ operator; samples boundary distribution ∂φ; returns p(∂φᵢ) for k=8 neighbors | RTT/3 |
| REGIME_CLASSIFIER | Gatekeeper | Maps (c, n, r, τ) coordinates to one of six named regimes; emits repair path | RTT/3 |
| TORSION_RESOLVER | Tertiary | Detects τ > 0.70; inserts mediation operator M̂; recomputes until τ < τ_max | RTT/2 |

**Engine invocation sequence:**
```
φ → VALIDATOR_ENTROPY_SCANNER → CLARITY_FIELD_ENGINE → REGIME_CLASSIFIER
                                         ↓  (if τ > 0.70)
                                   TORSION_RESOLVER → CLARITY_FIELD_ENGINE [retry]
```

---

### Operator Grammar

| Symbol | Name | Action | Type Signature |
|---|---|---|---|
| Ĉ | Compression | Reduces surface complexity; strips redundant signifiers | φ → φ′ where \|φ′\| ≤ \|φ\| |
| N̂ | Nuance | Expands discriminative resolution; adds valid distinctions | φ → φ″ where dim(φ″) ≥ dim(φ) |
| R̂ | Resonance | Projects φ onto receiver's generative field G | φ × G → ρ ∈ [0,1] |
| V̂ | Validator | Samples conceptual boundary ∂φ; returns confusion probability vector | φ → Δ(∂φ) |
| T̂ | Torsion | Measures rotational stress between incompatible operator applications | (φ, Ô₁, Ô₂) → τ ∈ ℝ₀⁺ |
| Π | Projection | Projects φ into a target register (linguistic, visual, formal) | φ × ℛ → φ_ℛ |
| M̂ | Mediation | Inserted between conflicting operators to resolve torsion | identity on output register of Ô₂ |

**Canonical clarity pipeline (compression-first):**
```
Ĉ ∘ N̂ [φ]   →   high-clarity output
```
**Reverse pipeline (resonance-first, for novice receivers):**
```
R̂ ∘ N̂ ∘ Ĉ ∘ Π_narrative [φ]
```
**Non-commutativity:** Ĉ and N̂ do not commute. Order determines whether torsion τ is introduced.

---

### Clarity Triad (C-N-R)

Every payload φ occupies a point **q** = (c, n, r) in the triad space:

| Axis | Symbol | Meaning | Range |
|---|---|---|---|
| Compression | c | Degree to which φ has been stripped of redundancy | [0, 1] |
| Nuance | n | Degree to which φ retains necessary distinctions | [0, 1] |
| Resonance | r | Degree to which φ couples with receiver field G | [0, 1] |

**Clarity ideal:** q* = (1, 1, 1) — maximally compressed, nuanced, and resonant.
**Clarity defect:** `Δq(φ) = √[(1−c)² + (1−n)² + (1−r)²]` — Euclidean distance from q to q*.
**Orthogonality condition:** No axis may be functionally determined by the other two. Violation → degenerate payload → operator repair required.

---

### Metrics

| Metric | Formula | Range | Ship Threshold |
|---|---|---|---|
| ĥᵥ (Validator Entropy) | Hᵥ / log₂(k) | [0, 1] | < 0.67 recommended |
| Wᵥ (Validator Width) | \|{ ∂φᵢ : d(φ,∂φᵢ) ≤ δ }\| | [1, k] | ≤ 5 (Miller limit) |
| Bφ (Boundary Chaos) | Wᵥ · ĥᵥ | [0, k] | < 3.0 |
| Iᵣ (Resonance-Integration) | 1 − σ(ρ)/μ(ρ) | [0, 1] | ≥ 0.70 |
| Ξ (Composite Clarity) | wc·(1−ĥᵥ) + wn·(1−Bφ/k) + wr·Iᵣ | [0, 1] | ≥ 0.70 |
| τ (Torsion) | T̂(φ, Ô₁, Ô₂) | [0, ∞) | < 0.70 |
| Δq (Clarity Defect) | √[(1−c)²+(1−n)²+(1−r)²] | [0, √3] | < 0.80 |

**Default protocol parameters:** k=8 · δ=0.25 · τ_max=0.70 · m=5 receivers · Ξ_ship=0.70

---

### Regime Map

| Regime | Symbol | Conditions | Characteristic |
|---|---|---|---|
| Crystal | Ξ-I | c≥0.8, n≥0.8, r≥0.8 | All axes healthy — ideal transmission |
| Blade | Ξ-II | c≥0.8, n<0.5, r≥0.6 | Sharp but brittle — nuance sacrificed |
| Fog | Ξ-III | c<0.5, n≥0.8, r<0.6 | Rich but non-transmissible — coupling fails |
| Echo | Ξ-IV | c<0.5, n<0.5, r≥0.8 | High social traction, thin epistemic content |
| Void | Ξ-V | c<0.4, n<0.4, r<0.4 | All axes suppressed — payload is noise |
| Torsion | Ξ-VI | τ≥0.70, any (c,n,r) | Operator conflict dominates — resolve M̂ first |

**Natural repair paths:**
```
VOID  →[N̂]→  FOG   →[Ĉ]→  CRYSTAL
BLADE →[N̂]→  CRYSTAL
FOG   →[Ĉ]→  CRYSTAL
ECHO  →[N̂]→  CRYSTAL  (maintain Iᵣ)
```

---

### Detection Pipeline

| Step | Action | Engine |
|---|---|---|
| 1. Ingest | Accept φ + receiver profiles G₁…Gₘ + domain weight preset | CLARITY_FIELD_ENGINE |
| 2. Boundary Sample | V̂ applied — sample k=8 boundary concepts at δ=0.25 | VALIDATOR_ENTROPY_SCANNER |
| 3. Hᵥ | Compute ĥᵥ = Hᵥ/log₂(k) | CLARITY_FIELD_ENGINE |
| 4. Wᵥ | Count neighbors within δ; compute Bφ = Wᵥ·ĥᵥ; check false precision | CLARITY_FIELD_ENGINE |
| 5. Iᵣ | Run R̂ across {G₁…Gₘ}; compute CV-inverted integration score | CLARITY_FIELD_ENGINE |
| 6. Torsion | Compute τ from operator log; if τ≥0.70 → TORSION_RESOLVER | TORSION_RESOLVER |
| 7. Ξ + Regime | Compute composite score; classify regime; emit repair path | REGIME_CLASSIFIER |
| 8. Gate | Ξ≥0.70 → PASS emit φ; Ξ<0.70 → HOLD queue repair | CLARITY_FIELD_ENGINE |

---

### Signal Flow

| Source | Signal | Type | Destination | Condition |
|---|---|---|---|---|
| Any S3 Spine overlay | Raw payload φ | Conceptual payload | CLARITY_FIELD_ENGINE | On submission |
| VALIDATOR_ENTROPY_SCANNER | ∂φ distribution | Boundary probability vector | CLARITY_FIELD_ENGINE | After V̂ |
| CLARITY_FIELD_ENGINE | Ξ, regime, repair path | Clarity Report | Requesting overlay | After pipeline |
| CLARITY_FIELD_ENGINE | τ spike | Torsion alert | TORSION_RESOLVER | τ ≥ 0.70 |
| TORSION_RESOLVER | M̂ applied φ | Repaired payload | CLARITY_FIELD_ENGINE | Retry loop |
| CLARITY_FIELD_ENGINE | PASS signal | Gate authorization | Downstream consumer | Ξ ≥ 0.70 |

---

### Domain Weight Presets

| Domain | wc | wn | wr | Rationale |
|---|---|---|---|---|
| Legal | 0.20 | 0.55 | 0.25 | Nuance load-bearing; false precision catastrophic |
| Executive | 0.45 | 0.20 | 0.35 | Speed and resonance dominate |
| Scientific | 0.30 | 0.50 | 0.20 | Precision/nuance priority; expert audience |
| Educational | 0.30 | 0.25 | 0.45 | Germane load is primary objective |
| Philosophical | 0.15 | 0.65 | 0.20 | Nuance is the value proposition |
| AI Prompt | 0.40 | 0.35 | 0.25 | Compression reduces hallucination surface |

---

### Cross-Framework Mappings

| Framework | Compression | Nuance | Resonance | Noise Model | Scalar Metric |
|---|---|---|---|---|---|
| Plain Language / FK | Sentence/syllable length | Not modeled | Grade-level match | Not modeled | FK score |
| Grice's Maxims | Quantity maxim | Manner (partial) | Relation maxim | Maxim violation | Qualitative |
| Shannon (1948) | Source coding | Source entropy H(X) | Mutual information I(X;Y) | Channel noise | H, C, I(X;Y) |
| CLT (Sweller) | Extraneous load reduction | Intrinsic load | Germane load | Extraneous load | IL+EL+GL |
| Double-Crux (CFAR) | Crux isolation | Crux resolution | Mutual update | Missing crux | Agreement |
| **RTT (native)** | **Ĉ operator** | **N̂ operator** | **R̂ operator** | **Torsion τ** | **Ξ ∈ [0,1]** |

All five external frameworks are recoverable as special cases or projections of RTT under appropriate parameter constraints. RTT is the only framework with full operator non-commutativity, six-regime awareness, and formal composability.

---

### State Machine

| State | Entry Condition | Exit Conditions |
|---|---|---|
| IDLE | No payload | φ submitted → SCORING |
| SCORING | φ received | Ξ computed → GATING |
| GATING | Ξ computed | Ξ≥0.70 → PASS; Ξ<0.70 → REPAIR |
| REPAIR | Ξ < 0.70 | Repaired φ ready → SCORING [retry] |
| TORSION_HOLD | τ ≥ 0.70 | τ < 0.70 after M̂ → SCORING [retry] |
| PASS | Ξ ≥ 0.70 | Consumed → IDLE |
| FALSE_PRECISION | ĥᵥ<0.2, c>0.7, n<0.5 | N̂ applied → SCORING [retry] |

---

### Module Registry

| Module | Type | Path |
|---|---|---|
| clarity-equations-v2 | Formal specification | docs/spine/clarity/clarity-equations-v2.md |
| clarity-equations-v2-examples | Companion guide | docs/spine/clarity/clarity-equations-v2-examples.md |
| clarity_overlay_module | JSON registration | docs/spine/clarity_overlay_module.json |
| cnr-triad-analyzer | Interactive tool | docs/spine/clarity/index.html |

---

### Signal Vocabulary

| Term | Abbrev | Definition |
|---|---|---|
| Conceptual payload | φ | Any unit of meaning: claim, explanation, argument, model output |
| Generative field | G | Receiver's existing conceptual schema; shapes resonance ρ |
| Clarity defect | Δq | Euclidean distance from current (c,n,r) to ideal (1,1,1) |
| Boundary chaos | Bφ | Wᵥ·ĥᵥ — scalar proxy for conceptual crowding |
| False precision | — | Artificially low ĥᵥ from over-compression, not genuine isolation |
| Ξ_ship | — | Minimum Ξ for transmission without review (default 0.70) |

---

### Integration Map

```
S3 Spine Overlays (1–6)
  │  │  │  │  │  │
  └──┴──┴──┴──┴──┘
          │
          ▼  φ (payload)
  ┌─────────────────────────────┐
  │   RTT::Clarity Overlay      │
  │                             │
  │  V̂ → Hᵥ → Wᵥ → Iᵣ → Ξ    │
  │            ↓                │
  │    REGIME_CLASSIFIER        │
  │            ↓                │
  │  Ξ≥0.70? → PASS            │
  │  Ξ<0.70? → REPAIR          │
  └─────────────────────────────┘
          │
          ▼  φ (cleared)
  Downstream Consumer
```

---

### Cross-Links

| Resource | URL |
|---|---|
| C-N-R Triad Analyzer (live) | https://www.triadicframeworks.org/spine/clarity/ |
| S3 Spine | https://www.triadicframeworks.org/spine/ |
| Coherence Overlay | https://www.triadicframeworks.org/spine/coherence/ |
| Structural Overlay | https://www.triadicframeworks.org/spine/structural/ |
| Drift Overlay | https://www.triadicframeworks.org/spine/drift/ |
| GitHub Repository | https://github.com/umaywant2/TriadicFrameworks |
| Overlay JSON | docs/spine/clarity_overlay_module.json |

---

### Publication Notes

| Field | Value |
|---|---|
| Status | Active Canonical |
| Version | 2.0 |
| Round | R5 |
| Published | 2026-08-08 |
| AI-parsability | Declared — all metrics, thresholds, formulas, and operator grammars are machine-readable |
| Source Pack | S3-Spine-Overlay-Pack-v2.0 |

---

*End of overlay · `RTT::Clarity` · S3 Spine · v2.0 · R5 · 2026-08-08*
