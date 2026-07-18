# 🗺️ Map — Planet 9 Sky‑Plane & Parameter‑Space Coverage

**Role:** map | **Layer:** coherence | **Module:** planet9 | **Version:** 1.0

> The map file charts *where the GCO remains spatially and parametrically unconstrained* — the surviving search space after all completed surveys are accounted for. It is the coherence‑layer instrument of the planet9 module: it holds the structural picture of what is known, what is excluded, and what remains open.

---

## Map Summary Block

```
-
┌──────────────────────────────────────────────────────┐
│  MAP — PLANET 9 SURVIVING SEARCH SPACE               │
│  *Where the GCO output is spatially unconstrained*   │
├──────────────────────────────────────────────────────┤
│  CONSTRAINED:   ~50% of plausible parameter space    │
│  UNCONSTRAINED: ~50% — concentrated in:              │
│                 → Southern galactic plane ±15°       │
│                 → Northern galactic plane ±15°       │
│                 → Deep‑faint zone V > 21.5 mag       │
│                 → Ultra‑distant zone d > 700 AU      │
├──────────────────────────────────────────────────────┤
│  BEST CURRENT POSITION WINDOW:                       │
│  RA ~ 40°–80°, Dec ~ −60° to −75°                    │
│  (2024 ω̃ estimate, southern galactic plane adjacent) │
├──────────────────────────────────────────────────────┤
│  COHERENCE STATUS: partial — ~50% constrained        │
│  LSST PROJECTED:   ~80% constrained by 2030          │
└──────────────────────────────────────────────────────┘
```

---

## 1. Coherence‑Layer Framework

### 1.1 What the Map Layer Does

In RTT grammar, the **coherence layer** holds the structural integrity of the module — the map of what has been resolved versus what remains open. For planet9, coherence is assessed spatially (sky‑plane coverage) and parametrically (parameter‑space coverage). A fully coherent module would have either:

- A detection at a specific sky position (coherence by resolution), or
- Complete survey coverage of all plausible parameter space (coherence by elimination)

Neither condition is met. The planet9 module is in **partial coherence** — a significant fraction of the plausible search space remains genuinely open.

### 1.2 Coherence Metric

```
COHERENCE METRIC — PLANET 9 MODULE (May 2026)

  Parameter-space coverage:
    Bright / nearby (d < 500 AU, V < 21.5):   ~70% covered
    Faint / moderate (500–750 AU, V 21.5–23):  ~25% covered
    Faint / distant (d > 750 AU, V > 23):       ~5% covered

  Sky-plane coverage:
    Northern sky (δ > 0°):                     ~60% covered (ZTF + PS1)
    Equatorial (−30° < δ < 0°):               ~65% covered (PS1 + DES edge)
    Southern sky (δ < −30°):                   ~35% covered (DES)
    Galactic plane exclusion zones:             ~0% covered (all surveys)

  Combined coherence score:   ~50%
  Remaining open space:       ~50%
```

---

## 2. Sky‑Plane Map

### 2.1 Full‑Sky Coverage Grid

The map below uses a schematic Mollweide‑style grid in ASCII, oriented in ecliptic coordinates (λ = ecliptic longitude, β = ecliptic latitude). Galactic plane crossing is marked.

```
PLANET 9 SKY‑PLANE MAP (Ecliptic coordinates)
══════════════════════════════════════════════════════

β = +90° (ecliptic north pole)
         │
+60° ────┼──── [PS1 coverage — good depth]
         │
+30° ────┼──── [PS1 + ZTF overlap — best northern coverage]
         │
  0° ────┼──── ECLIPTIC PLANE ────────────────────────
         │     [PS1 + ZTF + DES edge — well covered]
−30° ────┼──── [DES primary zone — deep southern coverage]
         │
−60° ────┼──── [DES partial + uncovered gaps]
         │
−90° ────┘ (ecliptic south pole)

         λ:  0°      90°     180°     270°     360°

GALACTIC PLANE CROSSINGS (ecliptic coords):
  λ ~ 270°–290°, β ~ −60° to −30°   (southern galactic plane)
  λ ~ 90°–110°,  β ~ +30° to +60°   (northern galactic plane)

LEGEND:
  ████  Well covered (V < 21.5, any survey)
  ▓▓▓▓  Partially covered (DES deep, V < 23)
  ▒▒▒▒  Poorly covered (V > 21.5, survey edge)
  ····  Uncovered (galactic exclusion or survey gap)

COVERAGE OVERLAY (schematic):
  λ 0°–180°,   β > −30°:  ████ (PS1 + ZTF)
  λ 0°–90°,    β < −30°:  ▓▓▓▓ (DES)
  λ 180°–360°, β < −30°:  ▒▒▒▒ (partial / gap)
  All galactic plane ±15°:  ···· (uncovered)
```

### 2.2 Predicted P9 Position Window

Based on 2024 ω̃ estimate (~252°–290°) and inclination (~20°), the most probable current sky position of P9 falls in:

```
PREDICTED POSITION WINDOW (2024 reference population)

  Ecliptic longitude: λ ~ 60°–100°  (anti‑perihelion direction)
  Ecliptic latitude:  β ~ −15° to −45°
  Equatorial coords:  RA ~ 40°–80°, Dec ~ −55° to −75°

  Sky region: South of the Large Magellanic Cloud,
              approaching southern galactic plane.

  Survey coverage of this window:
    DES: Partial — DES footprint clips this region at its eastern edge.
    PS1: Not accessible (δ < −30° excluded).
    ZTF: Not accessible (δ < −30° excluded).
    LSST: PRIMARY TARGET — this region is within LSST's southern coverage.

  ⚠️  This window lies adjacent to the southern galactic plane exclusion
      zone — the single largest unconstrained region in the entire
      P9 sky‑plane map.
```

### 2.3 Exclusion Zone Map

```
GALACTIC PLANE EXCLUSION ZONES — DETAIL

  All current wide‑area surveys avoid |b| < 10°–15° (galactic latitude)
  due to stellar crowding and transient contamination.

  Southern galactic plane (b ~ −10° to +10°, l ~ 260°–320°):
    → Ecliptic overlap: λ ~ 250°–310°, β ~ −30° to −50°
    → This is EXACTLY the ω̃ direction preferred by the 2024 P9 model
    → P9 may currently reside in the deepest part of this exclusion zone
    → No current survey can access this region to V < 23 mag

  Northern galactic plane (b ~ −10° to +10°, l ~ 60°–120°):
    → Ecliptic overlap: λ ~ 80°–130°, β ~ +20° to +50°
    → Less likely based on current ω̃ estimates but not eliminated

  LSST galactic plane coverage:
    → LSST will attempt partial galactic‑plane scanning with specialized
       processing pipelines (crowded‑field photometry)
    → Not guaranteed to reach P9 sensitivity in this region
    → Expected 50–70% efficiency at V < 23 in galactic plane
```

---

## 3. Parameter‑Space Map

### 3.1 Mass × Distance Grid

```
PARAMETER‑SPACE MAP: Mass (M_P9) × Distance (d_P9)

         d_P9 (AU)
         300   400   500   600   700   800   900  1000
    ┌─────────────────────────────────────────────────
  3 │  ████  ████  ████  ▓▓▓▓  ▒▒▒▒  ····  ····  ····
  4 │  ████  ████  ▓▓▓▓  ▓▓▓▓  ▒▒▒▒  ····  ····  ····
  5 │  ████  ▓▓▓▓  ▓▓▓▓  ▒▒▒▒  ▒▒▒▒  ····  ····  ····
  6 │  ████  ▓▓▓▓  ▒▒▒▒  ▒▒▒▒  ····  ····  ····  ····
  7 │  ████  ▓▓▓▓  ▒▒▒▒  ▒▒▒▒  ····  ····  ····  ····
M⊕ 8 │  ████  ▓▓▓▓  ▒▒▒▒  ····  ····  ····  ····  ····
  9 │  ████  ▒▒▒▒  ▒▒▒▒  ····  ····  ····  ····  ····
 10 │  ▓▓▓▓  ▒▒▒▒  ····  ····  ····  ····  ····  ····
    └─────────────────────────────────────────────────

LEGEND:
  ████  Eliminated — survey non‑detection rules out this zone
  ▓▓▓▓  Constrained — partially covered, low albedo survives
  ▒▒▒▒  Open — within LSST reach (2026–2030)
  ····  Unconstrained — beyond all near‑term survey capability

REFERENCE POPULATION PEAK: M ~ 6.6 M⊕, d ~ 500–550 AU (marked ▒▒▒▒)
→ The best‑fit parameter point is in the LSST‑reachable zone.
→ LSST will either find it or significantly constrain this region.
```

### 3.2 Albedo × Distance Grid

Albedo is the largest unresolved brightness uncertainty. The map below shows how the detectable distance horizon shifts with albedo:

```
DETECTION HORIZON: Albedo × Distance (V < 24.5, LSST)

  Albedo (p)   Max detectable d_P9    Survey reachable?
  ─────────────────────────────────────────────────────
  p = 0.30     ~1,300 AU              Yes (LSST + targeted)
  p = 0.20     ~1,100 AU              Yes (LSST)
  p = 0.10     ~  850 AU              Yes (LSST, marginal)
  p = 0.05     ~  650 AU              Marginal (LSST deep)
  p = 0.03     ~  520 AU              No — below LSST limit
  p = 0.01     ~  360 AU              No — already eliminated

  RTT note: p < 0.03 is physically unusual but not impossible
  (ultra‑processed carbonaceous surface). This is the "dark P9"
  escape hatch — the parameter zone that survives all surveys.
```

### 3.3 Orbital Period × Survey Cadence Constraint

```
ORBITAL PERIOD — SURVEY CADENCE CONSTRAINT

  P9 orbital period: ~10,000–20,000 years
  P9 sky‑plane motion: ~0.1–0.5 arcsec/year (extremely slow)

  Survey cadence requirement:
    Minimum: Multi‑epoch coverage over 1–3 years (proper motion detection)
    LSST cadence: ~4 visits/field/year → proper motion detectable
    ZTF cadence: ~3 visits/field/week → proper motion detectable
    DES: Single‑season, proper motion unreliable beyond 700 AU

  Motion constraint:
    At d = 550 AU: μ ~ 0.25 arcsec/year → detectable with 2‑year baseline
    At d = 900 AU: μ ~ 0.10 arcsec/year → marginal with 5‑year baseline
    At d > 1,200 AU: μ < 0.05 arcsec/year → undetectable without 10yr+ data
```

---

## 4. Coherence Projection

### 4.1 LSST Coherence Impact (2026–2030)

```
LSST COHERENCE PROJECTION

  Coverage added: ~18,000 deg² southern sky to V < 24.5
  P9 parameter space reached after 3 years (2029):

    Covered:      ~75% of M × d plausible space
    Remaining:    ~25% (ultra‑dark, ultra‑distant, or in galactic plane)

  Coherence status after LSST Year 3:
    SCENARIO A (detection):     Coherence = 100% (resolved)
    SCENARIO B (no detection):  Coherence = ~75% (strong constraint)
    SCENARIO C (partial):       Coherence = ~60% (galactic plane gap persists)

  Residual incoherence after LSST:
    → Southern galactic plane exclusion (requires dedicated crowded‑field survey)
    → Ultra‑distant zone (d > 900 AU, V > 24.5) — requires 30m‑class telescope
    → Ultra‑dark P9 (p < 0.03) — requires thermal IR follow‑up (WISE/NEO Surveyor)
```

### 4.2 Long‑Term Coherence Roadmap

```
COHERENCE ROADMAP

  2026:  LSST full survey begins
         → Resolves ~30% of remaining open parameter space per year

  2027:  LSST Year 1 results
         → N₃ resolved (50+ new ETNOs expected)
         → SIG‑1 direction stabilizes or dissolves

  2029:  LSST Year 3 results
         → ~75% parameter space covered
         → If no detection: strongest constraint in P9 history

  2030+: Dedicated galactic‑plane survey (proposed)
         → Addresses largest remaining exclusion zone
         → Requires specialized crowded‑field pipeline

  2035:  Thirty Meter Telescope / ELT era
         → Reaches d > 1,000 AU for p > 0.05
         → Addresses ultra‑distant zone

  COHERENCE ENDPOINT: Full coherence requires detection OR complete
  coverage including galactic plane + ultra‑distant zone.
  Earliest possible: 2029 (LSST detection)
  Latest realistic:  2040s (TMT/ELT era)
```

---

## 5. Map‑Layer Coherence Assessment

```
-
┌──────────────────────────────────────────────────────────┐
│  COHERENCE ASSESSMENT — MAP LAYER — MAY 2026             │
├──────────────────────────────────────────────────────────┤
│  Sky coverage:        ~50% of plausible area             │
│  Parameter coverage:  ~50% of plausible M×d space        │
│  Largest gap:         Southern galactic plane            │
│  Second gap:          Ultra‑distant / ultra‑dark zone    │
│  Best position est.:  RA~40°–80°, Dec~−55° to −75°       │
│  Next decisive event: LSST Year 1 ETNO catalog (2027)    │
│  Coherence trend:     Improving — LSST will be decisive  │
│  RTT assessment:      Partial coherence — open module    │
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
Modules:    hub → rtt-core → science → planet9 → map
Role:       map
Layer:      coherence
Drift:      bounded (observational-epistemic)
Coherence:  partial (~50% — southern galactic plane gap)
Version:    1.0 (planet9-stable)
Format:     markdown
Every page: stands alone + AI-parsable
Audience:   students + researchers + AIs
```

---

*🗺️ planet9_map.md — TriadicFrameworks Planet 9 Research | v1.0*
