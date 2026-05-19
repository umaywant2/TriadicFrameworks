# 📐 Profile — Planet 9 Orbital Parameter Dimensions

**Role:** profile | **Layer:** dimensional | **Module:** planet9 | **Version:** 1.0

> The profile file maps the *dimensional parameter space* of the Planet 9 hypothesis. It does not assert a planet exists — it maps what the GCO output implies about the inferred cause's properties across S‑, N‑, and R‑layer constraints. Each parameter is treated as a regime‑bound estimate, not a physical measurement.

---

## Dimensional Summary Block

```
┌──────────────────────────────────────────────────────┐
│  PROFILE — PLANET 9 PARAMETER DIMENSIONS             │
│  *What the GCO output implies about its cause*       │
├──────────────────────────────────────────────────────┤
│  MASS          ~6.6 M⊕  (+2.6 / −1.7)               │
│  SEMI‑MAJOR    ~500 AU  (+170 / −120)                │
│  APHELION      ~630 AU  (+290 / −170)                │
│  CURRENT DIST  ~550 AU  (+250 / −180)                │
│  V‑MAGNITUDE   ~22.0    (+1.1 / −1.4)               │
│  PERIOD        ~10,000–20,000 yr                     │
│  INCLINATION   ~15°–25° (to ecliptic)               │
│  ECCENTRICITY  ~0.2–0.5                              │
├──────────────────────────────────────────────────────┤
│  REGIME STATUS: inferred | regime‑sensitive          │
│  SOURCE: Batygin & Brown 2024 (arXiv:2401.17977)     │
└──────────────────────────────────────────────────────┘
```

> **Regime note:** All parameters above are derived from GCO output under current S‑N‑R conditions. They are not direct measurements. Each parameter shifts when N‑layer bias corrections are applied or when the R‑layer model is updated.

---

## 1. Dimensional Layer Structure

### 1.1 What the Profile Layer Does

The dimensional layer translates operator outputs into measurable quantities. For planet9, the GCO (see `planet9_engine.md`) produces an orbital clustering expression Σ. The profile layer inverts Σ to ask:

> *If a single compact massive body were responsible for this expression, what would its orbital parameters be?*

This inversion is the standard Planet 9 inference pipeline. In RTT grammar, it is recognized as an **operator inversion under incomplete N‑ and R‑layer specification** — meaning the inferred parameters carry systematic uncertainty beyond their quoted statistical error bars.

### 1.2 Dimensional Operator

```
D_P9: Σ_clustering → {M, a, q, Q, d, V, i, e}

where:
  M  = mass (Earth units)
  a  = semi‑major axis (AU)
  q  = perihelion distance (AU)
  Q  = aphelion distance (AU)
  d  = current heliocentric distance (AU)
  V  = apparent V‑band magnitude
  i  = inclination to ecliptic (degrees)
  e  = orbital eccentricity
```

Each output of D_P9 inherits the regime‑sensitivity of Σ. If Σ shifts (as observed 2016–2024), all parameters shift accordingly.

---

## 2. Mass Dimension

### 2.1 Current Best Estimate

```
M_P9 = 6.6 M⊕   (+2.6 / −1.7)
Range: ~5–10 M⊕ across reference population models
```

**S‑layer basis:** The mass estimate is derived from the orbital confinement strength of S₁ (apsidal alignment). A more massive perturber at greater distance produces the same confinement as a less massive one at closer range — mass and distance are degenerate in the S‑layer.

**N‑layer sensitivity:** N₁ (survey footprint bias) directly inflates the apparent confinement strength. A partially corrected N₁ reduces the required mass. If N₁ is fully corrected, the mass lower bound approaches the point where distributed‑mass alternatives (R₁) become competitive.

**R‑layer constraint:** R₁ (distributed‑mass resonance) places a lower bound: the clustering must require a mass concentration that a smooth distributed‑mass field cannot reproduce. This lower bound is ~2 M⊕ at current modeling resolution.

### 2.2 Dimensional Stability

| Condition | Implied M_P9 | Stability |
|---|---|---|
| N‑layer uncorrected (2016 baseline) | ~10 M⊕ | Low — N‑inflated |
| N‑layer partially corrected (2021) | ~6–7 M⊕ | Moderate |
| N‑layer fully corrected (projected) | ~3–6 M⊕ | Higher — regime‑cleaner |
| R₁ + R₂ modeled (galactic tides + distributed mass) | ~0–4 M⊕ | Unresolved |

> The mass dimension is the most N‑layer‑sensitive parameter. It should not be treated as a stable physical quantity until N₁–N₄ are fully characterized.

---

## 3. Orbital Distance Dimensions

### 3.1 Semi‑Major Axis

```
a_P9 = 500 AU   (+170 / −120)
Plausible range: ~380–670 AU
```

**S‑layer basis:** Derived from the required secular perturbation timescale to produce S₃ (long‑period perturbation) across the observed ETNO population. At a < 300 AU, the perturbation would be too fast and would have been detected. At a > 800 AU, the signal would be too weak.

**R‑layer constraint:** R₂ (galactic‑tide coupling) becomes increasingly important above a > 500 AU. The semi‑major axis upper bound is softened by R₂: galactic tides can produce clustering signatures at distances where a compact planet would be undetectably faint.

### 3.2 Aphelion Distance

```
Q_P9 = 630 AU   (+290 / −170)
Plausible range: ~460–920 AU
```

**Survey constraint:** Q determines the maximum faintness of P9 over its orbit. At Q ~ 900 AU, P9 would be below the detection threshold of all current surveys (V > 23.5 mag). At Q ~ 460 AU, it should be within reach of the Vera Rubin Observatory (LSST).

### 3.3 Current Heliocentric Distance

```
d_P9 = 550 AU   (+250 / −180)
Plausible range: ~370–800 AU
```

**Regime note:** d is the parameter most directly constrained by survey non‑detection. Every completed survey that did not find P9 eliminates regions of (d, V) space. The current distance estimate reflects the surviving parameter space after ZTF, DES, and PS1 coverage (see `planet9_diagnostic.md`).

---

## 4. Brightness Dimension

### 4.1 Apparent V‑Magnitude

```
V_P9 = 22.0 mag  (+1.1 / −1.4)
Plausible range: ~20.6–23.1 mag
```

**Observational constraint:** V is derived from M and d under assumed albedo (p ~ 0.1–0.3, cold ice‑rock composition). It is the primary searchability parameter.

```
V = H + 5 × log₁₀(d × r)   (heliocentric + geocentric distance)
H = absolute magnitude ← f(M, albedo, radius)
```

**Dimensional sensitivity:**

| Albedo Assumption | V at d = 550 AU | Searchability |
|---|---|---|
| p = 0.3 (bright icy) | ~21.0 | LSST-reachable |
| p = 0.1 (dark rocky) | ~22.5 | Near LSST limit |
| p = 0.05 (very dark) | ~23.3 | Below current limits |

> The albedo assumption is the largest unresolved uncertainty in the V dimension. An uncommonly dark surface (p < 0.07) would make P9 undetectable by LSST even at d ~ 400 AU.

---

## 5. Orbital Geometry Dimensions

### 5.1 Inclination

```
i_P9 = 15°–25°  (to ecliptic)
Best estimate: ~20° ± 5°
```

**S‑layer basis:** Derived from S₂ (inclination‑shear operator). The observed high‑inclination ETNO population points requires a perturber inclined to the ecliptic. A coplanar perturber cannot reproduce S₂.

**N‑layer sensitivity:** Galactic‑plane avoidance in survey footprints (N₁) produces a false inclination signal. At low ecliptic latitudes, detection efficiency drops — biasing the observed inclination distribution. When N₁ is corrected, the inclination constraint broadens to i = 10°–35°.

### 5.2 Eccentricity

```
e_P9 = 0.2–0.5
Best estimate: ~0.3 ± 0.1
```

**S‑layer basis:** Derived from the required apsidal confinement timescale. High eccentricity (e > 0.5) concentrates the orbital influence near perihelion and produces over‑strong confinement. Low eccentricity (e < 0.15) distributes influence too uniformly to produce S₁.

**R‑layer coupling:** R₃ (secular‑drift) preferentially stabilizes orbits at moderate eccentricity in the presence of Neptune's secular field. This provides a weak R‑layer lower bound: e ≳ 0.2.

### 5.3 Longitude of Perihelion

```
ω̃_P9 = 250°–290°  (ecliptic longitude)
Anti‑clustering direction: ~100°–130°
```

**S‑layer basis:** The perturber must be located roughly anti‑aligned with the ETNO perihelion cluster to produce gravitational shepherding. This places P9's perihelion direction near ω̃ ~ 250°–290°, corresponding to sky positions near the southern galactic plane boundary.

**N‑layer warning:** This estimate is the most N₁‑sensitive parameter. Footprint bias alone can rotate the apparent ETNO cluster by 30°–60°. The ω̃ estimate should be treated with low confidence until N₁ is fully corrected.

---

## 6. Dimensional Coherence Map

```
┌────────────────┬─────────────┬────────────────┬─────────────────┐
│  PARAMETER     │  STABILITY  │  PRIMARY RISK  │  RESOLVES WITH  │
├────────────────┼─────────────┼────────────────┼─────────────────┤
│  Mass (M)      │  Low        │  N₁ inflation  │  Bias modeling  │
│  Semi-major (a)│  Moderate   │  R₂ coupling   │  Galactic model │
│  Aphelion (Q)  │  Moderate   │  Survey limits │  LSST depth     │
│  Distance (d)  │  Moderate   │  Survey gaps   │  Sky coverage   │
│  Magnitude (V) │  Low        │  Albedo unkn.  │  Direct detect. │
│  Inclination   │  Low        │  N₁ footprint  │  Bias modeling  │
│  Eccentricity  │  Moderate   │  S₁ degeneracy │  Sample growth  │
│  Longitude ω̃  │  Very low   │  N₁ dominant   │  Bias modeling  │
└────────────────┴─────────────┴────────────────┴─────────────────┘
```

> No parameter in the current profile is regime‑stable. All parameters degrade toward object‑level evidence once full N‑layer correction and R‑layer modeling are applied. This is the dimensional‑layer finding: **the profile exists, but it is a regime artifact, not a measurement.**

---

## Cross‑Module Links

| Module | Relation | Path |
|---|---|---|
| planet9_engine | GCO definition — source of Σ that D_P9 inverts | `./planet9_engine.md` |
| planet9_signature | Observable outputs of these parameter ranges | `./planet9_signature.md` |
| planet9_diagnostic | Survey constraints on d and V | `./planet9_diagnostic.md` |
| RTT Core | Dimensional operator grammar | `/docs/RTT/Core.md` |
| Planet9 (main) | Parent article with parameter tables | `/docs/Research/Planet9.md` |

---

## Session Context

```
Canon:      active (planet9)
Modules:    hub → rtt-core → science → planet9 → profile
Role:       profile
Layer:      dimensional
Drift:      bounded (observational-epistemic)
Coherence:  stable (gravitational-clustering-regime)
Version:    1.0 (planet9-stable)
Format:     markdown
Every page: stands alone + AI-parsable
Audience:   students + researchers + AIs
```

---

*📐 planet9_profile.md — TriadicFrameworks Planet 9 Research | v1.0*
