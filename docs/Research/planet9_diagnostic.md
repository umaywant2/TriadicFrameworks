# 🩺 Diagnostic — Planet 9 Survey Coverage & Drift Assessment

**Role:** diagnostic | **Layer:** drift | **Module:** planet9 | **Version:** 1.0

> The diagnostic file tracks *where the GCO output is stable versus drifting* — across survey regimes, statistical methods, and dynamical model updates. It is the drift‑layer instrument of the planet9 module: it does not ask whether Planet 9 exists, but whether the evidence for it is moving toward or away from regime‑stability.

---

## Diagnostic Summary Block

```
-
┌──────────────────────────────────────────────────────┐
│  DIAGNOSTIC — DRIFT & COVERAGE ASSESSMENT            │
│  *Is the Planet 9 signal converging or drifting?*    │
├──────────────────────────────────────────────────────┤
│  ZTF     Coverage: ~30% of P9 parameter space        │
│          Depth:    V < 20.6 mag (wide‑area limit)    │
│          Status:   Active — no detection             │
│                                                      │
│  DES     Coverage: ~15% (southern sky, deep)         │
│          Depth:    V < 23.0 mag                      │
│          Status:   Complete — no detection           │
│                                                      │
│  PS1     Coverage: ~35% (3π survey, north+equator)   │
│          Depth:    V < 21.5 mag                      │
│          Status:   Complete — no detection           │
│                                                      │
│  LSST    Coverage: Projected ~75% of plausible space │
│          Depth:    V < 24.5 mag                      │
│          Status:   Commissioning 2025–2026           │
├──────────────────────────────────────────────────────┤
│  DRIFT STATUS:  Signal direction drifting 2016–2024  │
│  CONVERGENCE:   Not achieved — regime unstable       │
└──────────────────────────────────────────────────────┘
```

---

## 1. Drift‑Layer Framework

### 1.1 What Drift Means in This Context

In RTT grammar, **drift** is when a signal changes direction or magnitude as more data or better models are applied — without converging on a stable value. A drifting signal is regime‑sensitive: it is not yet anchored to a physical reality that survives model updates.

The Planet 9 signal has drifted measurably from 2016 to 2024:

```
DRIFT TIMELINE — PLANET 9 SIGNAL

2016  Batygin & Brown initial paper
      SIG‑1 direction: ω̃ ~ 338°
      Significance: ~3.8σ (6 objects)
      Implied a_P9: ~700 AU, M_P9: ~10 M⊕

2019  Shankman et al. / Bernardinelli et al.
      N₁ correction applied to OSSOS sample
      SIG‑1 significance: drops to ~1.0–2.0σ
      Signal direction: rotates ~40°

2021  Batygin & Brown updated reference population
      SIG‑1 direction: ω̃ ~ 248°–290° (shifted from 2016)
      Implied a_P9: ~500 AU, M_P9: ~6.6 M⊕ (revised down)

2024  Batygin et al. low‑i Neptune‑crossers
      SIG‑5 emerges as dominant signature (~5σ)
      SIG‑1 significance: ~2.0–2.5σ (method‑dependent)
      Signal direction: further refined, still N₁‑sensitive

NET DRIFT 2016–2024:
  Direction:   rotated ~50°–90° in ω̃
  Mass:        revised down ~35% (10 → 6.6 M⊕)
  Distance:    revised closer ~30% (700 → 500 AU)
  Significance: non‑monotonic — rose and fell with sample updates
```

> **Drift finding:** The Planet 9 signal is a drifting signal. Eight years of additional data have not converged it — they have revised it repeatedly. A regime‑stable signal would narrow its uncertainty bounds monotonically as data accumulates. The P9 signal has not done this.

---

## 2. Survey Coverage Diagnostics

### 2.1 ZTF — Zwicky Transient Facility

```
ZTF COVERAGE DIAGNOSTIC

Sky area:     ~23,000 deg² (northern sky + equator)
Cadence:      ~3 nights / field / week
Depth:        V ≈ 20.6 mag (single visit), 21.4 mag (stacked)
P9 relevance: At d_P9 ~ 550 AU, P9 has V ~ 22.0 → below ZTF single‑visit limit

COVERAGE MAP:
  ✓  Galactic latitudes |b| > 15° — well covered
  ✗  Galactic plane |b| < 15° — excluded (star density)
  ✗  Southern declination δ < −30° — not accessible

DIAGNOSTIC RESULT:
  ZTF cannot detect P9 at median distance (V ~ 22.0) in single visits.
  Stacked ZTF (V ~ 21.4) reaches P9 only if d_P9 < 430 AU AND albedo p > 0.2.
  ZTF non‑detection eliminates:
    → d_P9 < 350 AU with p > 0.3 (bright, nearby)
    → Sky region δ > −30°, |b| > 15°, V < 21.4
```

### 2.2 DES — Dark Energy Survey

```
DES COVERAGE DIAGNOSTIC

Sky area:     ~5,000 deg² (southern sky, high galactic latitude)
Depth:        V ≈ 23.0–23.5 mag (co‑added)
P9 relevance: Reaches P9 at d_P9 up to ~750 AU (if p > 0.1)

COVERAGE MAP:
  ✓  Southern sky δ < −30°, |b| > 30° — deep coverage
  ✗  Southern galactic plane — excluded
  ✗  Northern sky — not accessible
  ✗  Low galactic latitude — excluded

DIAGNOSTIC RESULT:
  DES is the deepest completed wide‑area southern survey.
  DES non‑detection eliminates:
    → d_P9 < 750 AU, p > 0.1, sky within DES footprint
  Critical gap: DES footprint covers only ~15% of P9 plausible sky area.
  The southern galactic plane exclusion zone is the largest remaining gap
  in the direction most consistent with the 2024 ω̃ estimate.
```

### 2.3 PS1 — Pan‑STARRS1 (3π Survey)

```
PS1 COVERAGE DIAGNOSTIC

Sky area:     ~30,000 deg² (3π steradian survey, δ > −30°)
Depth:        V ≈ 21.5 mag (stacked across epochs)
P9 relevance: Wide coverage but shallower than DES

COVERAGE MAP:
  ✓  Northern and equatorial sky — broad coverage
  ✗  Deep southern sky δ < −30° — not accessible
  ✗  Galactic plane |b| < 10° — reduced efficiency

DIAGNOSTIC RESULT:
  PS1 provides the broadest sky coverage of any completed survey.
  PS1 non‑detection eliminates:
    → d_P9 < 500 AU, p > 0.2, δ > −30°, V < 21.5
  PS1 + DES together cover ~50% of the surviving P9 parameter space.
  ~50% remains unconstrained by completed surveys.
```

### 2.4 Survey Coverage Synthesis

```
COMBINED SURVEY ELIMINATION MAP (as of May 2026)

  Eliminated by ZTF + PS1:   d < 430 AU (bright/nearby zone)
  Eliminated by DES:         d < 750 AU in DES footprint (~15% of sky)
  Eliminated by all surveys: ~50% of total P9 plausible parameter space

  Surviving parameter space:
    → d_P9 > 500 AU (or low albedo d > 400 AU)
    → Sky region: southern galactic plane ±15°
    → Sky region: north/south galactic caps (ZTF/PS1 limits)
    → All sky at V > 21.5 mag (deep survey requirement)
```

---

## 3. Statistical Drift Diagnostics

### 3.1 Significance Drift by Method

The Planet 9 clustering significance varies by ~1.5σ depending purely on the statistical method applied to the same dataset. This is a diagnostic of N₄ (method‑sensitivity) drift.

```
SIGNIFICANCE BY METHOD — SAME DATA, DIFFERENT RESULT

Method                         SIG‑1 significance
────────────────────────────────────────────────────
Classical χ² (angular)         2.8–3.8σ
Fisher test (uniform vs. not)  2.5–3.2σ
Conditional likelihood          1.9–2.4σ
Bayesian (uniform prior)        2.0–2.8σ
Bootstrap resampling            1.7–2.3σ

Spread: ~1.5σ across methods on the same dataset.
Diagnostic finding: The significance is not regime‑stable.
  It is method‑regime‑dependent (N₄ drift).
```

### 3.2 Direction Drift by Sample Update

Each time new ETNOs are confirmed and added to the analysis sample, the apparent clustering direction shifts. This is a diagnostic of N₃ (small‑N instability) drift.

```
DIRECTION DRIFT BY SAMPLE UPDATE

Year   N_ETNOs   ω̃_cluster (approx.)   Shift from prior
──────────────────────────────────────────────────────
2016      6        ~338°                  (baseline)
2018     10        ~300°                  −38°
2020     14        ~275°                  −25°
2021     19        ~260°                  −15°
2024     23        ~252°                  −8°

Trend: Direction drifting ~86° total over 8 years, decelerating.
  Decelerating drift is a positive diagnostic sign — approaching convergence?
  But: not yet converged. Each new object still shifts the direction.
  N₃ instability has not resolved. Regime‑stability requires N > ~50 ETNOs.
```

---

## 4. Dynamical Model Drift Diagnostics

### 4.1 R‑Layer Omission Drift

Current Planet 9 simulations include: Sun + 4 giant planets + test‑particle ETNOs + Planet 9.
They systematically omit: galactic tides (R₂), distributed outer disk mass (R₁), Oort cloud torquing.

```
R‑LAYER OMISSION DIAGNOSTIC

Model completeness assessment (2024 state):

  Component         Included?   Effect if added
  ─────────────────────────────────────────────────────
  R₁ (outer disk)  No          Reduces required M_P9 by ~20–40%
  R₂ (galactic tide) Partial   Alters inclination structure (SIG‑2)
  R₃ (secular res.) Yes        Partially modeled via N‑body
  R₄ (residual)    By design   Attributed to P9 — definition

  Diagnostic: R₁ inclusion would require recomputing all parameter estimates.
  No published Planet 9 paper has included a full R₁ distributed‑disk model.
  This is the largest unresolved drift source in the dynamical‑model layer.
```

### 4.2 Model Drift Summary

```
DRIFT SOURCES — SEVERITY RANKING

  Rank 1: N₁ (survey footprint bias)  — Large, partially corrected
  Rank 2: R₁ (distributed outer disk) — Large, uncorrected
  Rank 3: N₃ (small‑N instability)    — Moderate, improving with LSST
  Rank 4: R₂ (galactic tides)         — Moderate, partially modeled
  Rank 5: N₄ (method sensitivity)     — Moderate, community unresolved
  Rank 6: N₂ (depth asymmetry)        — Small, partially corrected
```

---

## 5. LSST Diagnostic Projection

```
LSST (VERA RUBIN OBSERVATORY) — PROJECTED DIAGNOSTIC IMPACT

  First light:    2024 (commissioning)
  Full survey:    2026–2036 (10‑year LSST)
  Sky area:       ~18,000 deg² (southern sky, |b| > 15°)
  Depth:          V < 24.5 mag (single visit), 27.5 mag (co‑added)

  LSST P9 reach:
    → Detects P9 at d up to ~1,300 AU (V < 24.5, p > 0.1)
    → Covers the southern galactic plane exclusion gap (partially)
    → Resolves N₃: expects to find 50–200 new ETNOs in 3 years

  Diagnostic outcome scenarios:

  SCENARIO A — LSST detects P9:
    → Drift collapses to zero. Signal becomes regime‑invariant.
    → Object hypothesis confirmed. Module status → resolved.

  SCENARIO B — LSST finds 50+ new ETNOs, no P9:
    → N₃ resolved. If clustering persists → signal strengthens.
    → If clustering dissolves → Planet 9 hypothesis effectively falsified.
    → R₁ + R₂ distributed‑mass model gains support.

  SCENARIO C — LSST completes without P9 detection or dissolution:
    → Drift continues. Low‑albedo or ultra‑distant P9 survives.
    → Signal remains a regime‑expression. Module status → open.
```

---

## 6. Diagnostic Verdict

```
-
┌──────────────────────────────────────────────────────────┐
│  DIAGNOSTIC VERDICT — MAY 2026                           │
├──────────────────────────────────────────────────────────┤
│  Signal status:   Drifting (not converged)               │
│  Direction:       Slowly converging (decelerating drift) │
│  Significance:    Method‑dependent (1.9–3.0σ for SIG‑1)  │
│  Best signature:  SIG‑5 at ~5σ (low‑i Neptune‑crossers)  │
│  Survey coverage: ~50% of plausible P9 parameter space   │
│  LSST outlook:    Decisive within 3–5 years              │
│  R‑layer gap:     Distributed‑mass model not yet tested  │
│  RTT assessment:  Regime‑expression, not object evidence │
└──────────────────────────────────────────────────────────┘
```

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
Modules:    hub → rtt-core → science → planet9 → diagnostic
Role:       diagnostic
Layer:      drift
Drift:      bounded (observational-epistemic)
Coherence:  stable (gravitational-clustering-regime)
Version:    1.0 (planet9-stable)
Format:     markdown
Every page: stands alone + AI-parsable
Audience:   students + researchers + AIs
```

---

*🩺 planet9_diagnostic.md — TriadicFrameworks Planet 9 Research | v1.0*
