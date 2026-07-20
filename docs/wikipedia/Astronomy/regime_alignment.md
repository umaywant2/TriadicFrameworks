# Astronomy — Regime Alignment

> **Purpose:** Map where Astronomy sits in the R0–R3 regime stack as declared
> by Wikipedia's own articles, categories, governance structures, and
> editorial practices. This file reads the regime structure that Wikipedia's
> community has **already built** for Astronomy and translates it into RTT
> vocabulary.
>
> **Reference:** [Wikipedia_RTT_Structural_Mapping.md](../Wikipedia_RTT_Structural_Mapping.md)
> for the notation conventions and regime level definitions used here.

---

## 1 — The Full Regime Stack for Astronomy

```
┌──────────────────────────────────────────────────────────────────┐
│  R0 — OPERATOR ASSUMPTIONS                                       │
│                                                                   │
│  • The universe is intelligible through observation               │
│  • Physical laws discovered on Earth apply everywhere             │
│  • Light (electromagnetic radiation) is the primary information   │
│    carrier from celestial sources                                 │
│  • The universe had a beginning and evolves over time             │
│  • Distance can be inferred from indirect proxies (parallax,      │
│    standard candles, redshift)                                    │
│  • Celestial objects can be classified into types with shared      │
│    properties                                                     │
│  • Observation is primary; direct experiment is (mostly)          │
│    impossible                                                     │
│                                                                   │
│  Wikipedia governance layer:                                      │
│  • WP:SCIRS — peer-reviewed astronomical journals have primacy    │
│  • WP:FRINGE — non-mainstream cosmological claims are bounded     │
│  • WP:ASTRO (WikiProject Astronomy scope)                         │
│  • IAU as naming and classification authority                     │
│  • Consensus that Astronomy is observation-constrained science    │
├──────────────────────────────────────────────────────────────────┤
│  R1 — DIRECTIONAL AIMS                                            │
│                                                                   │
│  • Map the observable universe at all scales                      │
│  • Understand the origin and fate of the universe                 │
│  • Detect and characterize exoplanets and potential habitability   │
│  • Resolve dark matter and dark energy                            │
│  • Detect gravitational waves from new source types               │
│  • Unify observational data with theoretical astrophysics models  │
│  • Catalog all observable objects with increasing precision        │
│                                                                   │
│  Wikipedia editorial layer:                                       │
│  • Astronomy articles should be accessible to a broad audience    │
│  • Articles should distinguish confirmed observation from         │
│    theoretical prediction                                         │
│  • Ancient and cultural astronomy should be represented           │
│  • Spectacular imagery should illustrate articles where possible  │
│  • Object articles should follow standard catalog conventions     │
│  • Discovery frontier articles should be updated as new data      │
│    arrives from active missions                                   │
├──────────────────────────────────────────────────────────────────┤
│  R2 — COHERENCE TEMPLATES                                         │
│                                                                   │
│  • Infobox templates (Infobox star, Infobox planet, Infobox       │
│    galaxy, Infobox constellation, Infobox comet, Infobox          │
│    spacecraft)                                                    │
│  • Standard section structure varies by article type              │
│    (object articles vs. concept articles vs. instrument articles) │
│  • IAU naming conventions as default                              │
│  • Catalog designations (Messier, NGC, HD, HIP, Gliese, Kepler)  │
│  • Epoch conventions (J2000.0 for coordinates)                    │
│  • SI + astronomical units (AU, ly, pc, solar masses/radii/       │
│    luminosities)                                                  │
│  • Category:Astronomy taxonomy (objects + branches + instruments) │
│  • Citation format (ApJ, A&A, MNRAS, Nature, arXiv)              │
│                                                                   │
│  Wikipedia structural layer:                                      │
│  • WikiProject Astronomy assessment scale                         │
│  • Quality ratings (Stub → FA)                                    │
│  • Importance ratings (Top/High/Mid/Low)                          │
│  • Navbox templates (Solar System, Stellar classification,        │
│    Messier objects, Constellations)                                │
├──────────────────────────────────────────────────────────────────┤
│  R3 — MEASURABLE OUTPUTS                                          │
│                                                                   │
│  • Article text: observational data, theoretical models,          │
│    discovery narratives, historical accounts                      │
│  • Wikidata statements: coordinates, magnitudes, distances,       │
│    spectral types, orbital elements, physical dimensions          │
│  • 700,000+ individual celestial object Wikidata entities         │
│  • Revision counts, page views, editor statistics                 │
│  • FA/GA counts (among the highest of any science domain)         │
│  • Category membership across object types and branches           │
│  • Cross-language article coverage (300+ editions)                │
│  • NASA/ESA image integration (public domain imagery)             │
└──────────────────────────────────────────────────────────────────┘
```

---

## 2 — R0: Operator Assumptions

### 2.1 — Astronomy's Foundational Assumptions

Every Astronomy article on Wikipedia implicitly operates under structural
assumptions that are **specific to an observational science**:

| Assumption | Where It's Visible | Structural Consequence |
|-----------|-------------------|----------------------|
| **Physical laws are universal** | Articles apply terrestrial physics (spectroscopy, gravity, thermodynamics) to objects billions of light-years away without qualification | The same equations used in a lab describe a quasar — universality is assumed, not proven for every case |
| **Light is the primary messenger** | Nearly all observational data comes from electromagnetic radiation; non-EM astronomy (neutrinos, gravitational waves) is explicitly marked as novel | Articles structurally default to EM observation; multi-messenger astronomy articles note their paradigm-expanding nature |
| **Distance is inferrable** | Articles state distances to objects as facts, but the methods (parallax, standard candles, redshift) are chains of inference | The "cosmic distance ladder" is itself a regime — each rung depends on the one below it |
| **Classification is possible** | Stars are sorted into spectral types, galaxies into Hubble types, planets into categories | Astronomical taxonomy is a regime declaration: these classification systems organize the entire domain |
| **The universe has a history** | Cosmology articles present a temporal narrative (Big Bang → nucleosynthesis → recombination → structure formation → present) | Astronomy assumes **cosmic chronology** — a single, linear temporal framework for the entire universe |
| **Observation cannot be repeated on demand** | Unlike lab science, astronomers cannot re-create a supernova or repeat a transit | Articles rely on archival data and multi-observer confirmation rather than experimental replication |

### 2.2 — The Observational Constraint as R0

Astronomy's deepest R0 assumption — the one that distinguishes it from all
other natural sciences — is the **observational constraint**:

> *We cannot touch, manipulate, or experiment on our subjects. We can only
> watch and listen.*

This constraint produces structural consequences across the entire Wikipedia
Astronomy domain:

| Consequence | Wikipedia Manifestation |
|------------|------------------------|
| **Indirect measurement** | Articles always specify measurement method and uncertainty — "distance: 2.5 ± 0.1 Mly (based on Cepheid variable calibration)" |
| **Technology dependence** | Major instrument articles (Hubble, JWST, ALMA, LIGO) are regime-defining — each new instrument opens new observational windows |
| **Historical layering** | The same object has been observed with increasing precision over centuries — articles accumulate historical observation layers |
| **Dual presentation** | Articles present both "what we observe" and "what we infer" — maintaining structural separation between data and interpretation |
| **Model plurality** | Where observations underdetermine theory, multiple models coexist — dark matter articles present WIMP, axion, MOND, and other candidates |

### 2.3 — Wikipedia's Governance of R0

| Wikipedia R0 Element | Effect on Astronomy Articles |
|---------------------|----------------------------|
| **WP:SCIRS** | Peer-reviewed astronomy journals (ApJ, MNRAS, A&A) have highest source standing; NASA/ESA press releases are acceptable for discovery announcements |
| **WP:FRINGE** | Non-mainstream cosmological claims (steady state revivalism, plasma cosmology, electric universe) are bounded — they get brief mention or separate articles, never equal standing with ΛCDM |
| **IAU authority** | The International Astronomical Union is recognized as the **naming and classification authority** — IAU decisions on nomenclature (planet definitions, constellation boundaries, object names) are treated as definitive |
| **WP:CRYSTALBALL** | Predicted but unconfirmed phenomena (hypothetical planets, predicted supernovae) are treated cautiously — articles must distinguish prediction from observation |
| **WP:NPOV** | Competing cosmological models (ΛCDM vs. alternatives) must be presented proportionally — but ΛCDM has overwhelming consensus standing |

### 2.4 — R0 Friction Points

| Friction Point | Astronomy R0 | Wikipedia R0 | Tension |
|---------------|-------------|-------------|---------|
| IAU authority vs. public naming | IAU assigns official designations (e.g., "2003 UB₃₁₃" → "Eris") | Public/media use informal names; Wikipedia must decide which to privilege | Wikipedia follows IAU as naming authority but acknowledges popular alternatives |
| Discovery priority | Astronomers care intensely about who discovered what first | Wikipedia must present discovery history neutrally, not advocate for claimants | WP:NPOV prevents Wikipedia from adjudicating priority disputes |
| Press release science | Space agencies issue press releases before peer review completes | WP:SCIRS prefers peer-reviewed sources | Wikipedia often cites press releases initially, then upgrades to journal citations — a visible temporal regime shift |
| Speculative habitability claims | Public fascination drives media coverage of "potentially habitable" exoplanets | WP:EXTRAORDINARY requires strong evidence for extraordinary claims | Articles must carefully contextualize habitability claims to avoid WP:UNDUE weight on speculation |
| Astrophotography and visual appeal | Astronomy produces spectacular imagery that drives public engagement | WP:NOTGALLERY limits the use of images to those that serve encyclopedic purpose | Tension between Astronomy's visual richness and Wikipedia's encyclopedic restraint |

---

## 3 — R1: Directional Aims

### 3.1 — Astronomy's Internal Directional Aims

| Aim | Wikipedia Evidence | Structural Function |
|----|-------------------|-------------------|
| **Complete the cosmic inventory** | Thousands of individual object articles; growing exoplanet catalog articles; systematic survey articles (Sloan, 2MASS, Gaia) | The domain aims to **catalog everything observable** — regime completeness through enumeration |
| **Understand cosmic origins** | Big Bang, Stellar nucleosynthesis, Planet formation articles form a connected origin narrative | The domain aims to tell the **complete temporal story** — from first light to present |
| **Find life beyond Earth** | Astrobiology, Habitable zone, Drake equation, Fermi paradox articles | The domain aims to answer humanity's **most profound observational question** |
| **Resolve dark sector** | Dark matter, Dark energy, ΛCDM model articles with open-problem framing | The domain acknowledges that ~95% of the universe's content is **structurally unresolved** |
| **Push observational boundaries** | Next-generation telescope articles, Multi-messenger astronomy, Gravitational-wave astronomy | The domain aims to **expand the observational window** — each new instrument is a regime expansion tool |
| **Preserve cultural astronomy** | Archaeoastronomy, Ethnoastronomy, Constellation mythology articles | The domain aims to honor its **pre-scientific heritage** — Astronomy is the only natural science that does this systematically on Wikipedia |

### 3.2 — Wikipedia's Editorial Directional Aims for Astronomy

| Editorial Aim | How It Manifests |
|--------------|-----------------|
| **Broad accessibility** | Astronomy articles typically have more accessible introductions than Physics articles — the domain's visual nature and public appeal encourages this |
| **Observation/theory distinction** | Major articles maintain structural separation between "what we see" and "what we think it means" — critical for a passive observational science |
| **Cultural inclusion** | History sections include ancient and non-Western astronomical traditions (Chinese, Islamic, Mesoamerican) more consistently than other science domains |
| **Image-rich presentation** | Astronomy articles use more images per word than any other science domain — NASA/ESA public-domain imagery is extensively utilized |
| **Active mission updates** | Articles on active missions (JWST, Mars rovers, Voyager) are expected to be updated as new results arrive — a living-document expectation not found in most science domains |
| **Catalog consistency** | Object articles are expected to follow standardized naming and data conventions from IAU and major catalogs |

### 3.3 — R1 as Visible in Article Scope Statements

| Article | Scope Declaration (paraphrased) | R1 Reading |
|---------|-------------------------------|-----------|
| Astronomy | "Studies celestial objects and phenomena originating outside Earth's atmosphere" | Aims to be the complete science of everything beyond Earth |
| Cosmology | "Studies the origin, evolution, and eventual fate of the universe" | Aims to be the complete temporal narrative of reality itself |
| Exoplanet | "A planet outside the Solar System" | Aims to catalog and characterize every planet in the galaxy — a scopeof billions |
| Stellar evolution | "The process by which a star changes over the course of time" | Aims to describe the complete lifecycle of the most common visible objects |
| Observational astronomy | "Observing celestial objects using telescopes and other astronomical apparatus" | Aims to be the methodological backbone — the observational regime itself |
| Astrobiology | "Studies the origins, early evolution, distribution, and future of life in the universe" | Aims to bridge Astronomy and Biology at their speculative frontier |

---

## 4 — R2: Coherence Templates

### 4.1 — Astronomy Infobox Templates

Astronomy uses a rich set of domain-specific infobox templates — each defines
the **minimum structural schema** for a type of Astronomy article:

| Template | Used For | Key Required Fields | RTT Function |
|----------|---------|-------------------|-------------|
| `{{Infobox star}}` | Individual stars | Constellation, RA/Dec (J2000), apparent magnitude, spectral type, distance, mass, radius, luminosity, temperature | **Regime schema for stars** — defines the minimum structural declaration for the most fundamental astronomical object |
| `{{Infobox planet}}` | Solar System planets and dwarf planets | Orbital elements, physical characteristics, atmosphere, satellites | **Regime schema for planets** — comprehensive template reflecting centuries of observation |
| `{{Infobox exoplanet}}` | Extrasolar planets | Host star, detection method, orbital period, semi-major axis, mass/radius (if known), equilibrium temperature | **Discovery-era schema** — fields reflect what current detection methods can measure |
| `{{Infobox galaxy}}` | Galaxies | Type (Hubble classification), RA/Dec, distance, apparent magnitude, size, number of stars | **Regime schema for galaxies** — organizes the large-scale universe |
| `{{Infobox constellation}}` | Constellations | Symbolism, RA/Dec range, area, main stars, Bayer/Flamsteed stars, meteor showers | **Cultural-scientific hybrid schema** — uniquely blends ancient naming with modern coordinates |
| `{{Infobox comet}}` | Comets | Discovery date/discoverer, orbital elements, eccentricity, period, next perihelion | **Transient object schema** — structured around orbital dynamics and observational windows |
| `{{Infobox nebula}}` | Nebulae | Type (emission, reflection, planetary, supernova remnant), RA/Dec, distance, dimensions | **Extended object schema** — organized by physical type and observational properties |
| `{{Infobox spacecraft}}` | Space telescopes and missions | Operator, launch date, mission type, orbit, instruments, status | **Instrument regime schema** — bridges Astronomy and Spaceflight |

### 4.2 — The Infobox as Regime Declaration

Astronomy's infoboxes are structurally richer than most domains because
each object type requires a **different minimum schema**:

| Object Type | Fields Always Filled | Fields Often Empty | What Emptiness Means |
|------------|---------------------|-------------------|---------------------|
| Star | Spectral type, RA/Dec, magnitude | Mass, radius (for distant stars) | Observational limit — distance prevents direct measurement |
| Exoplanet | Host star, detection method, period | Radius, atmosphere, temperature | Discovery-frontier signal — most exoplanets have only partial characterization |
| Galaxy | Type, distance, magnitude | Rotation velocity, metallicity, AGN type | Depends on observational resolution and research attention |
| Constellation | All fields filled | — | Culturally defined — no observational gaps because boundaries are arbitrary |

**RTT reading:** The pattern of **filled vs. empty infobox fields** across
a domain reveals the domain's **observational frontier**. In Astronomy,
the fields that are systematically empty are the measurements we cannot yet
make — each empty field is a **regime gap marker**, a structural acknowledgment
of the observational constraint.

### 4.3 — Standard Section Structures

Astronomy articles follow different section templates depending on article type:

#### Object Articles (Stars, Galaxies, Planets, Nebulae)

```
1. Lead paragraph (regime summary — what the object IS)
2. Observation history (regime discovery and evolution)
3. Physical characteristics (regime properties — measured values)
4. Orbit / Position (regime coordinates — where it sits)
5. Structure / Composition (regime internals — what it's made of)
6. Formation / Evolution (regime dynamics — how it got here)
7. Satellites / Companion objects (regime relationships)
8. Exploration (regime investigation — missions, instruments)
9. Cultural significance (regime in human context)
10. See also / References
```

#### Concept Articles (Big Bang, Stellar Evolution, Dark Matter)

```
1. Lead paragraph (regime summary)
2. Overview / Description (conceptual regime declaration)
3. History (regime origin — who proposed it and when)
4. Theory / Mathematical framework (formal regime declaration)
5. Observational evidence (regime validation — what supports it)
6. Current status / Open problems (regime completeness — what's unresolved)
7. Alternative theories (competing regime declarations)
8. See also / References
```

#### Instrument Articles (Hubble, JWST, ALMA, LIGO)

```
1. Lead paragraph (regime summary — what the instrument is and does)
2. History / Development (regime origin)
3. Design / Specifications (regime capabilities — what it can observe)
4. Science objectives (regime aims — what it's designed to answer)
5. Key discoveries (regime outputs — what it has found)
6. Operations / Status (regime current state)
7. Successor instruments (regime continuity — what comes next)
8. See also / References
```

**RTT reading:** The existence of **three distinct section templates**
within a single domain is structurally unusual. Most science domains use
a single default template. Astronomy maintains three because it organizes
around three fundamentally different regime types: **objects** (what exists),
**concepts** (what we understand), and **instruments** (how we observe).
This triple-template structure is the R2 manifestation of Astronomy's
dual object/process organization described in `overview.md` Section 3.3.

### 4.4 — The Astronomical Unit Regime

Astronomy uses a **multi-scale unit system** that varies by context:

| Scale | Default Unit | SI Equivalent | Where Used |
|-------|-------------|---------------|-----------|
| Solar System | Astronomical unit (AU) | 1.496 × 10¹¹ m | Planetary distances, orbital elements |
| Stellar | Light-year (ly) or parsec (pc) | 9.461 × 10¹⁵ m / 3.086 × 10¹⁶ m | Distances to nearby stars |
| Galactic | Kiloparsec (kpc) | 3.086 × 10¹⁹ m | Galactic structure, distances within Milky Way |
| Extragalactic | Megaparsec (Mpc) | 3.086 × 10²² m | Galaxy distances, Hubble constant |
| Cosmological | Redshift (z) | Non-linear (expansion-dependent) | Distances at cosmological scales |
| Stellar mass | Solar mass (M☉) | 1.989 × 10³⁰ kg | Mass of stars, galaxies, black holes |
| Stellar radius | Solar radius (R☉) | 6.957 × 10⁸ m | Size of stars |
| Luminosity | Solar luminosity (L☉) | 3.828 × 10²⁶ W | Brightness of stars |
| Brightness | Apparent/Absolute magnitude | Logarithmic scale | Observational brightness (inverted — lower = brighter) |

**RTT reading:** Astronomy's unit system is a **multi-scale coherence
template** — it uses different units at different scales because no
single unit is practical across the domain's enormous range. The unit
switch itself is a **regime boundary marker**: when an article switches
from AU to parsecs, the reader has crossed from Solar System to stellar
scale. When it switches from parsecs to redshift, the reader has crossed
into cosmological territory where Euclidean distance loses meaning.

The magnitude system deserves special note — it is an **inverted logarithmic
scale** inherited from the ancient Greek astronomer Hipparchus (c. 190–120 BCE).
The fact that modern Astronomy still uses a 2,100-year-old brightness scale
is a structural testament to the domain's **deep historical regime continuity**.

---

## 5 — R3: Measurable Outputs

### 5.1 — Article-Level Metrics

| Metric | Astronomy Domain Value | Interpretation |
|--------|----------------------|---------------|
| Total articles in Category:Astronomy | ~80,000+ (including subcategories; heavily populated by individual object articles) | One of the largest regime inventories on Wikipedia |
| Featured Articles | ~400+ | Among the highest of any science domain — spectacular imagery and clear scope aid validation |
| Good Articles | ~800+ | Healthy pipeline; many object articles are natural GA candidates |
| Average revision count (core articles) | 5,000–12,000 | High editorial attention driven by both expert and public interest |
| Average revert rate | 2–6% | Very low conflict; strong consensus domain |
| Individual object articles | Tens of thousands (stars, galaxies, exoplanets, asteroids, comets) | **Catalog-scale R3 output** — no other science domain approaches this volume of individual entity articles |

### 5.2 — Wikidata Output Layer

Astronomy's Wikidata layer is the **most extensively populated** individual
entity dataset in any science domain:

| Entity Type | Estimated Wikidata Count | Key Properties |
|------------|------------------------|----------------|
| Stars | 100,000+ | P215 (spectral class), P2583 (distance from Earth), P1457 (absolute magnitude), P881 (constellation) |
| Exoplanets | 5,000+ | P397 (parent astronomical body), P2120 (radius), P2067 (mass), P2146 (orbital period) |
| Galaxies | 10,000+ | P31 (instance of: galaxy), P59 (constellation), P1215 (apparent magnitude), P2583 (distance) |
| Asteroids | 600,000+ | P31 (instance of: asteroid), P196 (minor planet designation), P2146 (orbital period) |
| Constellations | 88 | P5765 (constellation area), P1943 (location of first/best observation) |
| Space missions | 1,000+ | P619 (launch date), P137 (operator), P375 (space launch vehicle) |

**RTT reading:** This massive R3 layer is what makes Astronomy structurally
unique among Wikipedia science domains. Each Wikidata entity is a
**micro-regime declaration** — a structured set of claims about a specific
object, with stated values, uncertainties, and source references. The
aggregate of 700,000+ entity declarations constitutes a machine-readable
**atlas of the observable universe** — the most comprehensive open
dimensional addressing system for celestial objects ever created.

### 5.3 — Cross-Language Coverage

| Language | Astronomy Article Count (approx.) | Structural Interpretation |
|----------|----------------------------------|--------------------------|
| English | ~80,000+ | Largest; includes most individual object articles |
| German | ~20,000+ | Strong tradition (Kepler, Herschel, Schwarzschild) |
| French | ~15,000+ | Strong tradition (Messier, Lagrange, Laplace) |
| Japanese | ~12,000+ | Active community; strong amateur tradition |
| Russian | ~10,000+ | Strong Soviet-era space science tradition |
| Arabic | ~5,000+ | Historical significance (Islamic Golden Age astronomy) — but lower modern coverage |
| Chinese | ~8,000+ | Ancient tradition (oldest continuous astronomical records); growing modern coverage |

**RTT reading:** Astronomy's cross-language coverage reveals a unique
**cultural depth pattern**. Arabic and Chinese Wikipedias have culturally
significant historical astronomy articles that English Wikipedia may
underrepresent. The ancient astronomical traditions of these cultures
predate Western astronomy by centuries — their Wikipedia coverage adds
regime dimensions that the English edition's science-focused articles
may lack.

---

## 6 — Regime Boundaries: Where Astronomy Meets Other Domains

### 6.1 — The Inter-Domain Boundary Map

| Boundary | Astronomy Side | Other Domain Side | Wikipedia Boundary Article(s) |
|----------|---------------|-------------------|------------------------------|
| Astronomy ↔ Physics | Astrophysics, physical cosmology, gravitational dynamics | Fundamental physics, particle physics, general relativity | Astrophysics, Physical cosmology, Astroparticle physics |
| Astronomy ↔ Earth Sciences | Planetary science, planetary geology, meteorology of other worlds | Geology, volcanology, atmospheric science | Planetary science, Comparative planetology, Planetary geology |
| Astronomy ↔ Biology | Astrobiology, extremophiles, habitable zones | Biology, microbiology, evolutionary biology | Astrobiology, Panspermia, Habitable zone |
| Astronomy ↔ Engineering | Telescope design, spacecraft instrumentation, detector technology | Optical engineering, aerospace engineering, electronics | Telescope, Space telescope, Adaptive optics |
| Astronomy ↔ Mathematics | Celestial mechanics, astrodynamics, orbital mechanics | Applied mathematics, dynamical systems | Celestial mechanics, N-body problem, Orbital mechanics |
| Astronomy ↔ History/Culture | Archaeoastronomy, constellation mythology, calendar systems | Archaeology, anthropology, mythology | Archaeoastronomy, Chinese astronomy, Islamic astronomy, Mayan astronomy |
| Astronomy ↔ Computer Science | Astroinformatics, virtual observatory, survey data processing | Data science, machine learning, image processing | Astroinformatics, Virtual observatory |
| Astronomy ↔ Philosophy | Cosmological implications, fine-tuning, Fermi paradox, anthropic principle | Philosophy of science, metaphysics, epistemology | Fine-tuned universe, Anthropic principle, Fermi paradox |

### 6.2 — The Astronomy↔Physics Boundary: Astrophysics

The Astronomy↔Physics boundary is Astronomy's **most structurally significant**
inter-domain interface:

| Dimension | Astronomy Perspective | Physics Perspective |
|-----------|---------------------|---------------------|
| Method | Observational — "What do we see in the sky?" | Experimental + theoretical — "What do the equations predict?" |
| Primary object | Celestial bodies and phenomena | Fundamental forces and particles |
| Scale focus | Macroscopic to cosmological | Microscopic to macroscopic |
| Naming authority | IAU | IUPAC (for particles), consensus (for theories) |
| Cultural heritage | Deep (5,000+ years of stargazing) | Moderate (400 years of modern physics) |
| Wikipedia treatment | Separate WikiProject, separate portal, separate category tree | Separate WikiProject, separate portal, separate category tree |

**Key insight:** Astrophysics sits precisely at this boundary — it is
**claimed by both domains** and has dual WikiProject banners on its talk
page. Wikipedia structurally acknowledges that Astrophysics is not
"Physics applied to Astronomy" or "Astronomy using Physics" — it is a
**boundary regime** with its own structural identity.

### 6.3 — The Astronomy↔Culture Boundary: Ancient Astronomy

Astronomy has a **culturally layered boundary** that no other natural
science domain on Wikipedia possesses at comparable depth:

| Cultural Tradition | Wikipedia Articles | Regime Character |
|-------------------|-------------------|-----------------|
| Babylonian astronomy | Star catalogs, mathematical astronomy, omen texts | **Proto-scientific regime** — systematic observation without modern physics |
| Chinese astronomy | Continuous records from ~2000 BCE, guest star (supernova) observations | **Archival regime** — unbroken observational record spanning 4,000 years |
| Greek astronomy | Geocentric models, mathematical cosmology, constellations | **Theoretical regime** — first attempts at physical explanation |
| Islamic astronomy | Refined instruments, star name legacy (Aldebaran, Betelgeuse, Rigel), zij tables | **Technological regime** — advanced instrumentation and catalog precision |
| Mesoamerican astronomy | Venus cycles, eclipse prediction, calendar systems | **Calendrical regime** — astronomy as temporal infrastructure |
| Indian astronomy | Siddhantas, observatory complexes (Jantar Mantar) | **Computational regime** — astronomical calculation traditions |

**RTT reading:** These cultural astronomy articles are not merely historical
footnotes — they represent **regime layers** that still structurally influence
modern Astronomy on Wikipedia. Star names (Sirius, Aldebaran, Betelgeuse,
Rigel) carry their Arabic/Greek/Latin regime origins. Constellation boundaries
are cultural constructs formalized by the IAU. The magnitude system preserves
Greek regime conventions. Modern Astronomy's Wikipedia articles sit atop
these cultural layers — the past regimes are **embedded in the present
regime's vocabulary and conventions**.

---

## 7 — Regime Nesting: Astronomy's Internal Hierarchy

### 7.1 — By Scale

Astronomy's internal hierarchy follows a **scale-based nesting**:

```
Cosmology (universe as a whole)
    │
    ├── Extragalactic astronomy (beyond the Milky Way)
    │       │
    │       └── Galactic astronomy (the Milky Way itself)
    │               │
    │               └── Stellar astronomy (individual stars and systems)
    │                       │
    │                       └── Planetary science (planets, moons, small bodies)
    │                               │
    │                               └── Planetary geology (surfaces, atmospheres)
    │
    └── Observational astronomy (cross-cutting — serves all scales)
            │
            ├── Radio astronomy (long wavelengths)
            ├── Infrared astronomy
            ├── Optical astronomy (visible light)
            ├── Ultraviolet astronomy
            ├── X-ray astronomy
            └── Gamma-ray astronomy (shortest wavelengths)
```

### 7.2 — By Wavelength

The observational branch has a **parallel nesting by wavelength** — each
wavelength window reveals different physical phenomena:

| Window | Reveals | Wikipedia Articles | Structural Role |
|--------|---------|-------------------|----------------|
| Radio | Pulsars, quasars, cosmic microwave background, HI clouds | Radio astronomy, Radio telescope, VLA, SKA | Cool and diffuse universe |
| Infrared | Dust-obscured stars, planet-forming disks, distant galaxies | Infrared astronomy, Spitzer, WISE | Hidden universe (behind dust) |
| Optical | Stars, nebulae, nearby galaxies — the "visible" universe | Optical astronomy, Reflecting telescope | Classical astronomical domain |
| Ultraviolet | Hot stars, stellar winds, active galactic nuclei | Ultraviolet astronomy, IUE, GALEX | Energetic stellar phenomena |
| X-ray | Black holes, neutron stars, galaxy cluster gas | X-ray astronomy, Chandra, XMM-Newton | Extreme physics regime |
| Gamma-ray | Gamma-ray bursts, pulsars, cosmic rays | Gamma-ray astronomy, Fermi, INTEGRAL | Most energetic phenomena in the universe |
| Gravitational waves | Black hole mergers, neutron star collisions | Gravitational-wave astronomy, LIGO, Virgo | Non-EM window — fundamentally new regime |
| Neutrino | Supernovae, solar interior, cosmic neutrino background | Neutrino astronomy, IceCube, Super-K | Particle window — complementary to EM |

**RTT reading:** This dual nesting (by scale AND by wavelength) is unique
to Astronomy. It means that the same object can be studied from multiple
regime perspectives — a galaxy article may reference radio, optical, X-ray,
and infrared observations, each revealing different structural information.
The article integrates these **multi-wavelength regime views** into a single
coherent declaration. This is Astronomy's version of dimensional integration.

---

## 8 — Regime Alignment Summary Table

| Regime Level | Astronomy Intrinsic | Wikipedia Governance | Alignment Quality |
|-------------|-------------------|---------------------|-------------------|
| **R0** | Universe is observable, lawful, classifiable; physical laws are universal; observation is primary (no manipulation) | WP:SCIRS, WP:FRINGE, IAU naming authority, WP:CRYSTALBALL | **Strong** — Wikipedia's source hierarchy aligns well with Astronomy's evidence hierarchy; IAU authority simplifies naming disputes; minor friction on speculative habitability claims |
| **R1** | Catalog everything, understand origins, find life, resolve dark sector, expand observational boundaries, preserve cultural heritage | Accessibility, observation/theory distinction, cultural inclusion, image-rich presentation, active mission updates | **Very strong** — Astronomy's visual appeal and public interest align exceptionally well with Wikipedia's encyclopedic accessibility aims |
| **R2** | Multiple infobox types per object class, triple section template (object/concept/instrument), multi-scale unit system, catalog conventions, epoch standards | WikiProject assessment, quality ratings, navbox templates | **Very strong** — Astronomy's rich observational tradition has produced standardized formats that map naturally to Wikipedia's template system |
| **R3** | 700,000+ individual entity articles, massive Wikidata coverage, NASA/ESA public-domain imagery, high FA/GA density | Page views, editor statistics, category membership, cross-language coverage | **Strongest of any science domain** — Astronomy's catalog tradition and public-domain imagery produce R3 outputs at a scale no other science domain matches |

**Overall alignment:** Astronomy is the **best-aligned science domain** on
Wikipedia for R3 output production. Its catalog tradition, public-domain
imagery (NASA/ESA), visual spectacularity, and public interest combine to
produce more validated, well-illustrated, and well-maintained articles per
concept than any other science domain. The only misalignment occurs at the
**cosmological frontier** (R0–R1), where competing theoretical models
create moderate NPOV stress.

---

## 9 — Connection to Other Module Files

| File | Connection |
|------|-----------|
| `overview.md` | This file assumes familiarity with the domain overview — start there for context |
| `student_exercises.md` | Exercises apply the regime alignment framework to specific Astronomy articles |
| `triadic_awareness.md` | Triadic analysis (structural, energetic, relational) provides an alternative lens on the same domain |
| `../Cross_Domain_Meta_Operators.md` | Astronomy contributes Operator 11 (Infobox Template as Regime Schema) — Astronomy's multi-type infobox system is the clearest example |
| `../NPOV_As_Coherence_Operator.md` | Astronomy's NPOV stress profile (predominantly Level 1–2 with frontier exceptions) is referenced in Section 3.2 |
| `../Revision_History_Regime_Analysis.md` | Astronomy's dual perturbation pattern (scientific + public events) is a distinctive temporal regime signature |
| `../Category_Taxonomy_Regime_Hierarchy.md` | Astronomy's dual organization (objects + processes) is one of the deepest category structures on Wikipedia |
| `../Wikidata_Ingestion_Format.md` | Astronomy's 700,000+ Wikidata entities are the largest science domain population in the knowledge graph |
| `../Physics/regime_alignment.md` | Physics provides Astronomy's theoretical substrate; the Astrophysics boundary zone is the most active inter-domain interface |

---

*This file is part of the [Astronomy domain directory](.) in the
[Wikipedia Awareness Module](../README.md) of the
[TriadicFrameworks](https://www.triadicframeworks.org/) canon.*
