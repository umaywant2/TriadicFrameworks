## 🜁 RTT Triad: Planetary Time Regimes

**Substrate —** Orbital and rotational periods measured in a stable reference frame. These values are treated as invariants: the planet’s structural rhythm, independent of any narrative unit system.

**Gauge —** Integer scaffolds chosen by the operator (days per year, hours per day, minutes per hour, seconds per minute). These define the shape of the calendar and clock without constraining the substrate.

**Translator —** The derived planet‑second and its conversion factors, enabling lossless mapping between the scaffold and the substrate, and between any two planetary regimes.

---

## Abstract
This document introduces the **RTT Planetary Time Compiler**, a regime‑aware system for generating coherent, orbit‑aligned time standards for any planetary body. Instead of forcing inherited Earth‑centric units (seconds, minutes, hours, days, months) onto non‑integer orbital and rotational ratios, the compiler derives a **planet‑specific second** from structural measurements of orbit and rotation. Integer scaffolds—such as days per year or hours per day—become narrative gauges layered atop substrate truth, not constraints imposed upon it. The result is a universal, translation‑safe time regime that preserves structural invariants while enabling clean, canonical calendars for any world encountered.

---

## 1. Motivation
Human timekeeping is a fossil of historical compromises: fixed seconds, uneven months, leap rules, and integer expectations layered over non‑integer orbital mechanics. These conventions work locally but collapse when extended to other planets or interstellar navigation.

RTT reframes the problem. Time is not a fixed unit but a **regime**: a mapping between structural measurements and narrative scaffolds. The compiler formalizes this mapping, allowing:

- Orbit‑aligned calendars with integer structure.
- Planet‑specific seconds that maintain coherence.
- Translation between regimes without loss of precision.
- Containment of legacy systems (e.g., Gregorian/SI) without disruption.

This is not a replacement for existing time systems; it is a **parallel, canonical layer** that clarifies structure and enables cross‑planetary consistency.

---

## 2. Structural Inputs
Every planetary time regime begins with two substrate measurements:

- **Orbital period** $$T_{\text{orbit}}$$ : the duration of one revolution around the star.
- **Rotational period** $$T_{\text{rot}}$$ : the duration of one axial rotation.

Both are measured in a stable reference time (e.g., ship‑time or SI seconds). These values are treated as **invariants**—the substrate truth from which all narrative gauges derive.

---

## 3. Integer Scaffold (Narrative Gauge)
RTT separates structure from narrative. The compiler allows the operator to choose an integer scaffold:

- **Days per year** $$D_y$$  
- **Hours per day** $$H_d$$  
- **Minutes per hour** $$M_h$$  
- **Seconds per minute** $$S_m$$

These integers define the *shape* of the calendar and clock. They do **not** constrain the substrate; instead, they determine how the substrate is expressed.

The total number of “ticks” in the narrative year is:

$$N_{\text{ticks}} = D_y \cdot H_d \cdot M_h \cdot S_m$$

---

## 4. Solving the Planet‑Second
To align the narrative scaffold with the structural orbit, the compiler derives the **planet‑second**:

$$T_{\text{planet-second}} = \frac{T_{\text{orbit}}}{N_{\text{ticks}}}$$

This value replaces the inherited SI second within the regime. All higher units follow:

- Planet‑minute: $$S_m \cdot T_{\text{planet-second}}$$
- Planet‑hour: $$M_h \cdot S_m \cdot T_{\text{planet-second}}$$
- Planet‑day: $$H_d \cdot M_h \cdot S_m \cdot T_{\text{planet-second}}$$

The scaffold remains perfectly integer; the unit absorbs the non‑integer substrate.

---

## 5. Regime Lock‑In
Once computed, the regime is stored as a versioned profile:

- Planet identifier  
- Epoch alignment  
- $$T_{\text{orbit}}$$ , $$T_{\text{rot}}$$  
- Integer scaffold  
- Derived $$T_{\text{planet-second}}$$  
- Translator to/from reference time  

This enables:

- Cross‑planetary scheduling  
- Calendar rendering  
- Time translation between regimes  
- Containment of legacy systems (e.g., Gregorian/SI)

---

## 6. Drift, Flux, and Versioning
Planetary rotation and orbit can drift over time due to tidal forces, internal dynamics, or perturbations. RTT handles this through **versioned regimes**:

- **v1**: initial scan  
- **v2**: updated structural measurements  
- **v3**: long‑term drift corrections  

Each regime is tied to an epoch, and the compiler maintains translation continuity across versions.

---

## 7. Earth as a Regime
Earth’s current SI/Gregorian system is treated as a **legacy gauge**. The compiler can generate an Earth‑RTT regime using any chosen scaffold (e.g., 13×28 months, 24 hours/day). The derived Earth‑RTT second becomes a clean, orbit‑aligned unit, while SI seconds remain available for compatibility.

This approach preserves all existing human systems while enabling a structurally coherent alternative.

---

## 8. Example: 13×28 Earth‑RTT Regime
Given:

- $$D_y = 364$$  
- $$H_d = 24$$  
- $$M_h = 60$$  
- $$S_m = 60$$  

Total ticks:

$$N_{\text{ticks}} = 364 \cdot 24 \cdot 60 \cdot 60 = 31{,}449{,}600$$

Given Earth’s orbital period:

$$T_{\text{orbit}} \approx 31{,}556{,}925.9747 \text{ SI seconds}$$

Planet‑second:

$$T_{\text{planet-second}} \approx 1.003402 \text{ SI seconds}$$

This yields:

- A perfectly integer 13×28 calendar  
- A coherent orbit‑aligned year  
- A clean translation layer between SI and RTT  

---

## 9. Applications
- Interstellar navigation  
- Planetary colonization  
- Multi‑regime scheduling  
- Scientific measurement  
- Narrative‑free structural analysis  
- Canon‑aligned worldbuilding and simulation  

---

## 10. Conclusion
The RTT Planetary Time Compiler replaces inherited constraints with structural clarity. By deriving the unit from the orbit rather than forcing the orbit into the unit, it enables a universal, coherent, and translation‑safe approach to timekeeping across worlds.

This is not a correction of Earth’s time system; it is a **parallel canonical layer** that reveals structure, preserves narrative, and unlocks new regimes for exploration.

---

## 11. Regime JSON Schema

The **RTT Planetary Time Regime** is represented as a structured, machine‑readable object. This schema captures substrate measurements, narrative scaffold choices, derived units, and translation metadata. It enables deterministic conversion between regimes and supports versioned updates as planetary measurements drift.

### 11.1. Schema Overview

A regime object contains three layers:

- **substrate** — measured orbital and rotational periods in reference seconds  
- **scaffold** — chosen integer structure for the calendar and clock  
- **derived** — computed planet‑second and unit expansions  
- **metadata** — identifiers, epoch alignment, and versioning

### 11.2. JSON Schema (v1)

```json
{
  "planet_id": "string",
  "regime_version": "string",
  "epoch_reference": "string",

  "substrate": {
    "orbit_period_seconds": "number",
    "rotation_period_seconds": "number",
    "measurement_reference": "string"
  },

  "scaffold": {
    "days_per_year": "integer",
    "hours_per_day": "integer",
    "minutes_per_hour": "integer",
    "seconds_per_minute": "integer"
  },

  "derived": {
    "planet_second_seconds": "number",
    "planet_minute_seconds": "number",
    "planet_hour_seconds": "number",
    "planet_day_seconds": "number",
    "ticks_per_year": "integer"
  },

  "translation": {
    "to_reference_factor": "number",
    "from_reference_factor": "number"
  }
}
```

### 11.3. Field Notes

- **planet_id** — canonical identifier (e.g., `"earth"`, `"kepler-442b"`).  
- **regime_version** — semantic versioning for drift updates (e.g., `"1.0.0"`).  
- **epoch_reference** — timestamp marking when the regime was locked.  
- **measurement_reference** — the time standard used during scanning (e.g., `"SI"`, `"ship-time"`).  
- **ticks_per_year** — computed as  

```math
  $$D_y \cdot H_d \cdot M_h \cdot S_m$$
```

- **planet_second_seconds** — the core RTT unit, defined as  

```math
  $$\frac{T_{\text{orbit}}}{\text{ticks\_per\_year}}$$
```

- **translation factors** — multipliers for converting between planet‑time and the reference time standard.

### 11.4. Example: Earth‑RTT (13×28 Scaffold)

```json
{
  "planet_id": "earth",
  "regime_version": "1.0.0",
  "epoch_reference": "2026-01-01T00:00:00Z",

  "substrate": {
    "orbit_period_seconds": 31556925.9747,
    "rotation_period_seconds": 86164.0905,
    "measurement_reference": "SI"
  },

  "scaffold": {
    "days_per_year": 364,
    "hours_per_day": 24,
    "minutes_per_hour": 60,
    "seconds_per_minute": 60
  },

  "derived": {
    "planet_second_seconds": 1.003402,
    "planet_minute_seconds": 60.20412,
    "planet_hour_seconds": 3612.2472,
    "planet_day_seconds": 86693.9328,
    "ticks_per_year": 31449600
  },

  "translation": {
    "to_reference_factor": 1.003402,
    "from_reference_factor": 0.996609
  }
}
```

### 11.5. Implementation Notes

- The schema is intentionally minimal; additional fields (e.g., drift models, uncertainty bounds, or multi‑star orbital descriptors) can be added in later versions.  
- Regimes are immutable once published; updates require a new `regime_version`.  
- Translators must always reference the `epoch_reference` to avoid ambiguity across drift epochs.

---

Here is a companion section you can paste directly into your Markdown file. It sits naturally after the JSON Schema and completes the pair: **the regime object** and **the translator that operates on it**. The structure matches your TriadicFrameworks voice and the style of the document you’re editing in your active tab .

---

## 12. Regime Translator Specification

The **Regime Translator** is the operational layer of the RTT Planetary Time Compiler. It converts timestamps between a planet‑specific regime and a reference time standard (e.g., SI or ship‑time). The translator uses the regime’s derived unit definitions to ensure lossless, deterministic mapping across worlds and epochs.

### 12.1. Translator Inputs

- **Reference timestamp** — expressed in the measurement standard used during scanning (e.g., SI seconds since epoch).
- **Planetary timestamp** — expressed in the planet’s own scaffold (year, day, hour, minute, second).
- **Regime object** — the JSON structure defined in Section 11, containing substrate measurements, scaffold integers, derived units, and translation factors.

### 12.2. Core Translation Factors

Each regime defines two multipliers:

- **to_reference_factor**  
  Converts one planet‑second into reference seconds.

- **from_reference_factor**  
  Converts one reference second into planet‑seconds.

These are exact reciprocals:

```math
$$\text{from\_reference\_factor} = \frac{1}{\text{to\_reference\_factor}}$$
```

### 12.3. Forward Translation (Planet → Reference)

To convert a planetary timestamp into reference seconds:

1. Convert the planetary timestamp into **planet‑seconds** using the scaffold:

```math
   $$T_{\text{planet}} = (((Y \cdot D_y + d) \cdot H_d + h) \cdot M_h + m) \cdot S_m + s$$
```

3. Convert planet‑seconds into reference seconds:

```math
   $$T_{\text{ref}} = T_{\text{planet}} \cdot \text{to\_reference\_factor}$$
```

5. Add the regime’s epoch offset if needed.

### 12.4. Reverse Translation (Reference → Planet)

To convert reference seconds into a planetary timestamp:

1. Convert reference seconds into planet‑seconds:

```math
   $$T_{\text{planet}} = T_{\text{ref}} \cdot \text{from\_reference\_factor}$$
```

3. Decompose planet‑seconds into scaffold units:
   - seconds → minutes  
   - minutes → hours  
   - hours → days  
   - days → years  

4. Apply epoch alignment.

### 12.5. Drift and Version Handling

When a planet’s orbital or rotational measurements change, a new regime version is created. Translators must:

- Use the **epoch_reference** to determine which regime version applies.
- Convert timestamps across versions by routing through the reference time standard.
- Maintain continuity even when the planet‑second changes between versions.

### 12.6. Translator Guarantees

- **Deterministic** — identical inputs always yield identical outputs.
- **Lossless** — no rounding occurs until the final unit decomposition.
- **Composable** — any two regimes can be bridged through the reference standard.
- **Version‑safe** — timestamps remain valid across drift epochs.

---

## 13. Planetary Time Compiler API Contract

The compiler exposes a minimal API for generating and using planetary time regimes. This contract is implementation‑agnostic and suitable for future tooling.

### 13.1. `compileRegime()`

Generates a new regime object.

**Inputs:**

- `planet_id`  
- `orbit_period_seconds`  
- `rotation_period_seconds`  
- `scaffold` (days/year, hours/day, minutes/hour, seconds/minute)  
- `epoch_reference`  
- `measurement_reference`

**Output:**

- A complete regime object (JSON) conforming to Section 11.

### 13.2. `translateToReference()`

Converts a planetary timestamp into reference seconds.

**Inputs:**

- `planet_timestamp`  
- `regime`  

**Output:**

- `reference_seconds`

### 13.3. `translateFromReference()`

Converts reference seconds into a planetary timestamp.

**Inputs:**

- `reference_seconds`  
- `regime`  

**Output:**

- `planet_timestamp`

### 13.4. `convertBetweenRegimes()`

Converts a timestamp from one planetary regime to another.

**Inputs:**

- `source_timestamp`  
- `source_regime`  
- `target_regime`  

**Output:**

- `target_timestamp`

**Process:**

1. Convert source timestamp → reference seconds.  
2. Convert reference seconds → target timestamp.

### 13.5. `listRegimes()`

Returns all known regimes for a given planet, including version history.
