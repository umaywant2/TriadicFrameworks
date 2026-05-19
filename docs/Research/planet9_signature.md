# 🔭 Signature — Planet 9 Observational Regime Expressions

**Role:** signature | **Layer:** regime | **Module:** planet9 | **Version:** 1.0

> The signature file maps the *observable outputs* of the Gravitational Clustering Operator (GCO) across each survey regime. A signature is not proof of a planet — it is a regime‑expression: a pattern that the GCO produces at the S‑layer surface, shaped by N‑layer distortions and sustained by R‑layer dynamics.

---

## Signature Summary Block

```
-
┌──────────────────────────────────────────────────────┐
│  SIGNATURE — PLANET 9 OBSERVABLE REGIME EXPRESSIONS  │
│  *What the GCO looks like in each survey regime*     │
├──────────────────────────────────────────────────────┤
│  SIG‑1  Apsidal Confinement      → S₁ surface        │
│  SIG‑2  Inclination Excess       → S₂ surface        │
│  SIG‑3  Detached‑Orbit Cluster   → S₁ + R₃ coupling  │
│  SIG‑4  High‑Perihelion Cluster  → R₁ + R₂ coupling  │
│  SIG‑5  Low‑Inclination Neptune‑ → S₂ + R₃ coupling  │
│         Crossers                                     │
├──────────────────────────────────────────────────────┤
│  REGIME STATUS: survey‑dependent | non‑invariant     │
│  STRONGEST IN: ZTF northern coverage zone            │
│  WEAKEST IN:   Galactic plane exclusion zones        │
└──────────────────────────────────────────────────────┘
```

---

## 1. What a Regime Signature Is

In OBA grammar, a "signature" is a fingerprint: direct evidence of an object. In RTT grammar, a signature is a **regime‑layer expression** — a pattern that appears at the S‑layer surface but whose cause may be distributed across N and R layers.

The distinction matters because:
- An object fingerprint should be **regime‑invariant**: it should not change when you correct for survey bias or update your dynamical model.
- A regime‑expression is **regime‑sensitive**: it shifts when any of S, N, or R are updated.

The Planet 9 signatures below are all regime‑sensitive. This is the signature file's core finding: **no currently observed Planet 9 signature is regime‑invariant.**

### 1.1 Signature Regime‑Invariance Test

```
REGIME‑INVARIANCE TEST:
  Does the signature persist when —
  ✗ Survey footprint bias (N₁) is modeled?
  ✗ Detection‑depth asymmetry (N₂) is corrected?
  ✗ Sample size doubles (N₃ resolved)?
  ✗ Galactic tides (R₂) are included in the dynamical model?

If any ✗ → signature is a regime‑expression, not an object fingerprint.
All five Planet 9 signatures currently fail this test.
```

---

## 2. SIG‑1 — Apsidal Confinement Signature

### 2.1 Description

The primary Planet 9 signature. The perihelia of extreme trans‑Neptunian objects (ETNOs, defined as a > 150 AU, q > 30 AU) appear clustered in ecliptic longitude of perihelion (ω̃), rather than uniformly distributed as expected for a dynamically relaxed population.

```
APSIDAL CONFINEMENT — REGIME MAP

Observed:     ETNO perihelia cluster near ω̃ ~ 0°–90°
Expected:     Uniform distribution over 0°–360°
Significance: ~1.9σ–3.0σ (method‑dependent)
Direction:    ω̃ ~ 40°–60° (cluster center; N₁‑uncorrected)

↓ shaped by N₁ (footprint bias)
↓ direction shifts ±30° when N₁ is partially corrected
↓ significance drops to ~1.9σ under conditional‑likelihood tests
```

### 2.2 Regime Sensitivity

| Variable | Effect on SIG‑1 |
|---|---|
| Add 5 new ETNOs | Direction shifts ~15°–25° |
| Apply N₁ footprint correction | Significance falls ~0.5–1.0σ |
| Include galactic‑tide model (R₂) | Partial coherence reproduced without planet |
| Use conditional‑likelihood method (N₄) | Significance falls to ~1.9σ |

**RTT classification:** SIG‑1 is an S₁‑layer surface expression amplified by N₁. It is the most N‑layer‑sensitive signature in the planet9 module. Under full N‑layer correction, SIG‑1 is not independently diagnostic of a compact planet.

---

## 3. SIG‑2 — Inclination Excess Signature

### 3.1 Description

The distant TNO population contains more high‑inclination objects (i > 40°) than standard giant‑planet‑only models predict. A significant fraction of these have orbital planes consistent with secular perturbation by a body inclined ~20° to the ecliptic.

```
INCLINATION EXCESS — REGIME MAP

Observed:    Excess of i > 40° objects in distant TNO population
             Orbital planes cluster in a preferred direction
Expected:    Smooth inclination distribution from Neptune scattering
Significance: ~2.5σ (depends on sample definition)

↓ R₂ (galactic‑tide coupling) elevates inclinations at a > 200 AU
↓ N₁ (galactic‑plane avoidance) suppresses detection of low‑ecliptic objects
↓ Combined: SIG‑2 cannot be disentangled from R₂ + N₁ without full modeling
```

### 3.2 Regime Sensitivity

| Variable | Effect on SIG‑2 |
|---|---|
| Include galactic‑tide model (R₂) | Partial inclination excess reproduced |
| Correct galactic‑plane avoidance (N₁) | Significance reduces |
| Extend sample beyond 500 AU | Inclination clustering direction may rotate |

**RTT classification:** SIG‑2 is an S₂‑layer expression with strong R₂ contamination. It is the most R‑layer‑sensitive signature in the planet9 module. A galactic‑tide‑inclusive model is required before SIG‑2 can serve as independent evidence.

---

## 4. SIG‑3 — Detached‑Orbit Cluster Signature

### 4.1 Description

Detached TNOs — objects with large semi‑major axes and perihelia too distant to be Neptune‑controlled (q > 50 AU, a > 150 AU) — show orbital configurations inconsistent with pure Neptune scattering. Their perihelia are "detached" from Neptune's influence zone and appear to require an additional perturbing mechanism.

```
DETACHED‑ORBIT CLUSTER — REGIME MAP

Objects:     Sedna (q=76 AU), 2012 VP₁₁₃, 2015 BP₅₁₉, 2014 SR₃₄₉
Property:    Perihelion too high for Neptune to have emplaced them
             Apsidal angles non‑random at ~2σ

↓ S₁ + R₃ coupling: secular resonance could detach orbits without planet
↓ R₂ (galactic tides): for a > 250 AU, tides detach perihelion naturally
↓ R₁ (distributed mass): outer disk models reproduce q > 50 AU without planet
```

### 4.2 Detached Object Catalog (RTT format)

```
-
┌──────────────┬────────┬────────┬──────────────────────────┐
│  Object      │  a(AU) │  q(AU) │  RTT Regime Note         │
├──────────────┼────────┼────────┼──────────────────────────┤
│  Sedna       │  506   │  76    │  R₂‑detachable at a>300  │
│  2012 VP₁₁₃  │  265   │  80    │  R₁+R₃ competitive       │
│  2015 BP₅₁₉  │  449   │  36    │  S₁ confinement zone     │
│  2014 SR₃₄₉  │  300   │  50    │  R₃ secular drift zone   │
└──────────────┴────────┴────────┴──────────────────────────┘
```

**RTT classification:** SIG‑3 is an S₁ + R₃ coupling expression. The detachment mechanism is multiply realizable: a compact planet, distributed mass, or galactic tides can all produce it. SIG‑3 is not uniquely diagnostic of a compact perturber.

---

## 5. SIG‑4 — High‑Perihelion Cluster Signature

### 5.1 Description

Objects with very high perihelia (q > 65 AU) and large semi‑major axes (a > 200 AU) appear preferentially in orbital configurations predicted by Planet 9 secular models: anti‑aligned apsidal angles, moderate inclinations, and stable libration zones. These are the most direct orbital‑dynamics signatures of the Planet 9 model.

```
HIGH‑PERIHELION CLUSTER — REGIME MAP

Signature:   Objects occupy predicted stable libration zones
             Anti‑aligned with P9 orbital model at ω̃ ~ anti‑phase
             q > 65 AU: Neptune cannot emplace these perihelia

↓ R₁ (distributed mass field): can emplace q > 65 AU perihelia
↓ R₂ (galactic tides): contributes at a > 300 AU
↓ Sample: only ~6 confirmed q > 65 AU objects — N₃ instability severe
```

### 5.2 Libration Zone Map

```
PLANET 9 PREDICTED LIBRATION ZONES (OBA model)
═══════════════════════════════════════════

  Anti‑aligned zone (stable):  ω̃ ~ 180° from P9 perihelion
  Aligned zone (unstable):     ω̃ ~ 0° from P9 perihelion
  High‑i zone (stable):        i ~ 50°–100°, any ω̃

RTT reread:
  "Libration zones" = R₃ secular‑drift attractors
  Objects in these zones → secular resonance, not necessarily a planet
  Attractor structure emerges from giant planets alone at moderate strength
```

**RTT classification:** SIG‑4 is the strongest candidate for planet‑exclusive evidence but is degraded by N₃ (only ~6 objects). A planet‑free R₃ + R₁ model has not been ruled out at sufficient confidence. SIG‑4 requires sample growth to ~30 q > 65 AU objects to be regime‑stable.

---

## 6. SIG‑5 — Low‑Inclination Neptune‑Crosser Signature

### 6.1 Description

Batygin, Morbidelli, Brown & Nesvorny (2024, arXiv:2404.11594) identified a population of low‑inclination, high‑eccentricity Neptune‑crossers whose orbital distribution is inconsistent (~5σ) with standard Neptune‑scattering models but consistent with Planet 9 secular perturbation over Gyr timescales.

```
LOW‑i NEPTUNE‑CROSSER — REGIME MAP

Population:  Objects with a ~ 50–150 AU, q ~ 25–38 AU, i < 10°
Anomaly:     Over‑dense in orbital phase space predicted by P9 model
Significance: ~5σ against Planet‑9‑free model
              (strongest single statistical claim in P9 literature)

↓ This is the most regime‑stable signature currently identified
↓ N₁ (footprint) has weaker effect — these objects are brighter/closer
↓ N₃ (small‑N) less severe — population is larger
↓ R₂ (galactic tides) is weak at a < 150 AU
```

### 6.2 Why SIG‑5 Is the Most Significant

```
SIGNATURE HIERARCHY (current, 2024–2026)

  SIG‑5  Low‑i Neptune‑crossers   ~5σ  (most robust)
  SIG‑2  Inclination excess        ~2.5σ
  SIG‑1  Apsidal confinement       ~1.9–3.0σ (method‑dependent)
  SIG‑4  High‑perihelion cluster   ~2σ  (N₃‑limited)
  SIG‑3  Detached orbits           ~2σ  (R‑layer‑competitive)
```

**RTT classification:** SIG‑5 is the least N‑layer‑contaminated signature. It operates in a regime where N₁ and N₂ effects are reduced, and it survives conditional‑likelihood correction. If Planet 9 has a regime‑invariant signature, SIG‑5 is the current best candidate — but a Planet‑9‑free model has not been fully constructed at sufficient detail to rule out R₁ + R₃ explanations.

---

## 7. Signature Cross‑Regime Summary

```
-
┌─────────┬───────────────────────┬──────────┬─────────────┬──────────────────┐
│  SIG    │  Description          │  Signif. │  Regime     │  RTT Status      │
├─────────┼───────────────────────┼──────────┼─────────────┼──────────────────┤
│  SIG‑1  │  Apsidal confinement  │  ~1.9–3σ │  N₁‑heavy   │  Regime artifact │
│  SIG‑2  │  Inclination excess   │  ~2.5σ   │  R₂‑heavy   │  Regime artifact │
│  SIG‑3  │  Detached orbits      │  ~2σ     │  R₁+R₃      │  Multiply realiz.│
│  SIG‑4  │  High‑q cluster       │  ~2σ     │  N₃‑limited │  Requires growth │
│  SIG‑5  │  Low‑i Neptune‑cross  │  ~5σ     │  Moderate   │  Best candidate  │
└─────────┴───────────────────────┴──────────┴─────────────┴──────────────────┘
```

**Signature‑layer conclusion:** The Planet 9 signature set is a graded regime‑expression. No single signature is currently regime‑invariant. SIG‑5 is the most planet‑like expression — but until a full R‑layer‑inclusive model is tested against it, the signature layer cannot support an object‑level conclusion.

---

## Cross‑Module Links

| Module | Relation | Path |
|---|---|---|
| planet9_engine | GCO that produces the drifting signal | `./planet9_engine.md` |
| planet9_signature | Signatures being diagnosed here | `./planet9_signature.md` |
| planet9_map | Spatial coverage gaps being diagnosed | `./planet9_map.md` |
| planet9_profile | Parameters that drift as signal shifts | `./planet9_profile.md` |
| RTT Core | Drift operator definitions | `../rtt/1/core_definitions.md` |
| Planet9 (main) | Parent article | `./Planet9.md` |

---

## Session Context

```
Canon:      active (planet9)
Modules:    hub → rtt-core → science → planet9 → signature
Role:       signature
Layer:      regime
Drift:      bounded (observational-epistemic)
Coherence:  stable (gravitational-clustering-regime)
Version:    1.0 (planet9-stable)
Format:     markdown
Every page: stands alone + AI-parsable
Audience:   students + researchers + AIs
```

---

*🔭 planet9_signature.md — TriadicFrameworks Planet 9 Research | v1.0*
