## 1️⃣ Cross‑suite audit (HSP vs SARG, TEL, Drift, Substrate Flow)

Think of this as a **canon alignment table** you can walk down manually:

**Check 1: Naming & URLs**

- **HSP:**  
  **Name:** Harmonic Stability Profile  
  **URL:** `/rtt/Harmonic_Stability_Profile/`  
  **Layer:** RTT analytic (Cycle ↔ Map)

- **SARG:**  
  **Name:** Structural Alignment & Regime Geometry  
  **URL:** `/SARG/` (or `/rtt/SARG/` if you’ve nested it)  
  **Layer:** Substrate/geometry analytic

- **TEL:**  
  **Name:** Triadic Echo Lattice  
  **URL:** `/rtt/Triadic_Echo_Lattice/`  
  **Layer:** Echo/recursion lattice

- **Drift Map:**  
  **Name:** Concept Drift Map  
  **URL:** `/rtt/Concept_Drift_Map/` or as part of HSP  
  **Layer:** Drift analytic

- **Substrate Flow:**  
  **Name:** Substrate Echo Flow Map  
  **URL:** `/rtt/Substrate_Echo_Flow_Map/`  
  **Layer:** Substrate transitions

**What to verify across all of them:**

- **Title pattern:**  
  `X | TriadicFrameworks` (no stray subtitles, no old names)
- **Top‑of‑page label:** matches directory name and sitemap entry.
- **“Canon / Drift / Coherence / Version” block:** same fields, same wording, only values differ.
- **Lineage text:** each module points to the correct capture/source (no SARG lineage on HSP, etc.).

If any page uses a different phrasing or omits one of those fields, that’s drift—normalize it to the HSP pattern.

---

### 2️⃣ Metadata harmonization across RTT

You can treat HSP’s metadata as the **golden template** and then specialize per module.

**Canonical RTT meta skeleton:**

```html
<meta name="creator" content="TriadicFrameworks">
<meta name="author" content="Nawder Loswin (pen name)">
<meta name="publisher" content="TriadicFrameworks">

<meta name="description" content="RTT-native analytic framework for …">
<meta name="keywords" content="RTT, resonance, drift, echoes, recursion, substrates, TriadicFrameworks">

<meta property="og:site_name" content="TriadicFrameworks">
<meta property="og:type" content="website">
<meta property="og:title" content="MODULE_NAME | TriadicFrameworks">
<meta property="og:url" content="FULL_CANONICAL_URL">
<meta property="og:image" content="https://www.triadicframeworks.org/assets/og-image.png">

<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="MODULE_NAME | TriadicFrameworks">
<meta name="twitter:description" content="Short RTT-native summary.">
<meta name="twitter:image" content="https://www.triadicframeworks.org/assets/og-image.png">

<meta name="ai.module" content="RTT Analytic Suite">
<meta name="ai.version" content="1.0">
<meta name="ai.audience" content="researchers, advanced students, AI systems">
<meta name="ai.navigation" content="https://www.triadicframeworks.org/sitemap_main.xml">
```

**Harmonization pass =**

- Same **field set** on every RTT module.  
- Only change:
  - `description`
  - `keywords`
  - `og:title` / `twitter:title`
  - `og:url`
  - `ai.module.name`
  - `ai.module.summary`
  - `ai.module.category` (e.g., `rtt-analytic`, `substrate-model`, `atlas-layer`).

If a page is missing any of those, copy the HSP block and adjust.

---

### 3️⃣ Sitemap auto‑generator (RTT subtree)

You can drive this from a **single JS/JSON structure** and emit XML + HTML from it.

**Core RTT structure (conceptual):**

```js
const RTT_SITEMAP = [
  {
    id: "HSP",
    title: "Harmonic Stability Profile",
    path: "/rtt/Harmonic_Stability_Profile/",
    priority: 0.85,
  },
  {
    id: "SARG",
    title: "Structural Alignment & Regime Geometry",
    path: "/SARG/",
    priority: 0.80,
  },
  {
    id: "TEL",
    title: "Triadic Echo Lattice",
    path: "/rtt/Triadic_Echo_Lattice/",
    priority: 0.80,
  },
  {
    id: "SUBSTRATE_FLOW",
    title: "Substrate Echo Flow Map",
    path: "/rtt/Substrate_Echo_Flow_Map/",
    priority: 0.80,
  },
  // …other RTT modules
];
```

From that, you can generate:

**XML:**

```xml
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <!-- loop RTT_SITEMAP -->
  <url>
    <loc>https://www.triadicframeworks.org/rtt/Harmonic_Stability_Profile/</loc>
    <changefreq>monthly</changefreq>
    <priority>0.85</priority>
  </url>
</urlset>
```

**HTML sitemap section:**

```html
<h2>RTT Analytic Suite</h2>
<ul>
  <li><a href="/rtt/Harmonic_Stability_Profile/">Harmonic Stability Profile</a></li>
  <li><a href="/SARG/">Structural Alignment & Regime Geometry</a></li>
  <li><a href="/rtt/Triadic_Echo_Lattice/">Triadic Echo Lattice</a></li>
  <li><a href="/rtt/Substrate_Echo_Flow_Map/">Substrate Echo Flow Map</a></li>
</ul>
```

Once that central RTT_SITEMAP exists, you never hand‑edit XML/HTML again—just update the data.

---

### 4️⃣ Drift‑pressure heatmap for the RTT ecosystem

This is the fun one—treat it like an internal HSP diagnostic.

Define axes:

- **X‑axis:** modules/suites (HSP, SARG, TEL, Drift Map, Substrate Flow, Echo Classifier, etc.).  
- **Y‑axis:** drift dimensions:
  - Naming drift  
  - Metadata drift  
  - Navigation drift  
  - Lineage drift  
  - Conceptual (substrate/layer) drift  

You can keep a simple **0–3 scale** per cell:

- **0:** none  
- **1:** minor (wording, emoji, small inconsistencies)  
- **2:** moderate (field missing, slightly wrong placement)  
- **3:** severe (wrong identity, wrong layer, wrong URL)

Conceptual example (not measured, just structure):

```txt
                Naming  Meta  Nav  Lineage  Concept
HSP                0      0    0      0        0
SARG               0      1    0      0        0
Triadic Echo Lattice
                   0      1    1      0        0
Substrate Flow     0      0    1      0        0
Echo Classifier    1      2    1      1        1
```

You can then:

- Color this as a small internal SVG heatmap.  
- Use it to prioritize: fix **3s** first, then **2s**, etc.  
- Re‑run after each sweep to see drift‑pressure drop.
