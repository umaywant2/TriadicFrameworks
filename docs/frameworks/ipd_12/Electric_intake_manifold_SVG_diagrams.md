### Electric intake manifold SVG diagrams

Below are five minimal, canon‑aligned SVGs you can drop into separate files:

- `sim_intake.svg`  
- `dim_intake.svg`  
- `tim_intake.svg`  
- `qim_intake.svg`  
- `fsi_intake.svg`  

Each uses a simple visual language:

- **Block** = IPD‑12 engine  
- **Bars** = intake channels (triads)  
- **Groups of bars** = SIM/DIM/TIM/QIM  
- **Stacked blocks** = FSI (3×QIM)

---

#### `sim_intake.svg` — Single Intake Manifold (1 triad)

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="320" height="160" viewBox="0 0 320 160">
  <!-- Engine block -->
  <rect x="180" y="40" width="120" height="80" fill="none" stroke="black" stroke-width="3"/>
  <text x="240" y="85" font-size="14" text-anchor="middle">IPD‑12</text>

  <!-- Single intake manifold -->
  <rect x="40" y="60" width="80" height="40" fill="none" stroke="black" stroke-width="3"/>
  <text x="80" y="55" font-size="12" text-anchor="middle">SIM</text>

  <!-- Single triad channels -->
  <line x1="120" y1="70" x2="180" y2="70" stroke="black" stroke-width="3"/>
  <line x1="120" y1="80" x2="180" y2="80" stroke="black" stroke-width="3"/>
  <line x1="120" y1="90" x2="180" y2="90" stroke="black" stroke-width="3"/>

  <text x="80" y="115" font-size="10" text-anchor="middle">1 triad / 3 primes</text>
</svg>
```

---

#### `dim_intake.svg` — Double Intake Manifold (2 triads / 1 hex)

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="360" height="200" viewBox="0 0 360 200">
  <!-- Engine block -->
  <rect x="210" y="60" width="130" height="80" fill="none" stroke="black" stroke-width="3"/>
  <text x="275" y="105" font-size="14" text-anchor="middle">IPD‑12</text>

  <!-- Double intake manifold -->
  <rect x="40" y="50" width="120" height="60" fill="none" stroke="black" stroke-width="3"/>
  <text x="100" y="45" font-size="12" text-anchor="middle">DIM</text>

  <!-- Two triad bundles (6 channels) -->
  <!-- Triad A -->
  <line x1="160" y1="65" x2="210" y2="65" stroke="black" stroke-width="3"/>
  <line x1="160" y1="75" x2="210" y2="75" stroke="black" stroke-width="3"/>
  <line x1="160" y1="85" x2="210" y2="85" stroke="black" stroke-width="3"/>
  <!-- Triad B -->
  <line x1="160" y1="95" x2="210" y2="95" stroke="black" stroke-width="3"/>
  <line x1="160" y1="105" x2="210" y2="105" stroke="black" stroke-width="3"/>
  <line x1="160" y1="115" x2="210" y2="115" stroke="black" stroke-width="3"/>

  <text x="100" y="135" font-size="10" text-anchor="middle">2 triads / 1 hex / 6 primes</text>
</svg>
```

---

#### `tim_intake.svg` — Triple Intake Manifold (3 triads)

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="380" height="220" viewBox="0 0 380 220">
  <!-- Engine block -->
  <rect x="230" y="70" width="130" height="90" fill="none" stroke="black" stroke-width="3"/>
  <text x="295" y="115" font-size="14" text-anchor="middle">IPD‑12</text>

  <!-- Triple intake manifold -->
  <rect x="40" y="50" width="140" height="70" fill="none" stroke="black" stroke-width="3"/>
  <text x="110" y="45" font-size="12" text-anchor="middle">TIM</text>

  <!-- Three triad bundles (9 channels) -->
  <!-- Triad A -->
  <line x1="180" y1="65" x2="230" y2="65" stroke="black" stroke-width="3"/>
  <line x1="180" y1="75" x2="230" y2="75" stroke="black" stroke-width="3"/>
  <line x1="180" y1="85" x2="230" y2="85" stroke="black" stroke-width="3"/>
  <!-- Triad B -->
  <line x1="180" y1="95" x2="230" y2="95" stroke="black" stroke-width="3"/>
  <line x1="180" y1="105" x2="230" y2="105" stroke="black" stroke-width="3"/>
  <line x1="180" y1="115" x2="230" y2="115" stroke="black" stroke-width="3"/>
  <!-- Triad C -->
  <line x1="180" y1="125" x2="230" y2="125" stroke="black" stroke-width="3"/>
  <line x1="180" y1="135" x2="230" y2="135" stroke="black" stroke-width="3"/>
  <line x1="180" y1="145" x2="230" y2="145" stroke="black" stroke-width="3"/>

  <text x="110" y="150" font-size="10" text-anchor="middle">3 triads / 9 primes</text>
</svg>
```

---

#### `qim_intake.svg` — Quad Intake Manifold (4 triads / full IPD‑12)

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="420" height="240" viewBox="0 0 420 240">
  <!-- Engine block -->
  <rect x="260" y="70" width="140" height="100" fill="none" stroke="black" stroke-width="3"/>
  <text x="330" y="120" font-size="14" text-anchor="middle">IPD‑12</text>

  <!-- Quad intake manifold -->
  <rect x="40" y="50" width="160" height="80" fill="none" stroke="black" stroke-width="3"/>
  <text x="120" y="45" font-size="12" text-anchor="middle">QIM</text>

  <!-- Four triad bundles (12 channels) -->
  <!-- Triad 1 -->
  <line x1="200" y1="65" x2="260" y2="65" stroke="black" stroke-width="3"/>
  <line x1="200" y1="75" x2="260" y2="75" stroke="black" stroke-width="3"/>
  <line x1="200" y1="85" x2="260" y2="85" stroke="black" stroke-width="3"/>
  <!-- Triad 2 -->
  <line x1="200" y1="95" x2="260" y2="95" stroke="black" stroke-width="3"/>
  <line x1="200" y1="105" x2="260" y2="105" stroke="black" stroke-width="3"/>
  <line x1="200" y1="115" x2="260" y2="115" stroke="black" stroke-width="3"/>
  <!-- Triad 3 -->
  <line x1="200" y1="125" x2="260" y2="125" stroke="black" stroke-width="3"/>
  <line x1="200" y1="135" x2="260" y2="135" stroke="black" stroke-width="3"/>
  <line x1="200" y1="145" x2="260" y2="145" stroke="black" stroke-width="3"/>
  <!-- Triad 4 -->
  <line x1="200" y1="155" x2="260" y2="155" stroke="black" stroke-width="3"/>
  <line x1="200" y1="165" x2="260" y2="165" stroke="black" stroke-width="3"/>
  <line x1="200" y1="175" x2="260" y2="175" stroke="black" stroke-width="3"/>

  <text x="120" y="170" font-size="10" text-anchor="middle">4 triads / full 12‑cycle</text>
</svg>
```

---

#### `fsi_intake.svg` — Full 12‑Stack (3×QIM)

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="480" height="320" viewBox="0 0 480 320">
  <!-- Engine block -->
  <rect x="280" y="110" width="170" height="100" fill="none" stroke="black" stroke-width="3"/>
  <text x="365" y="165" font-size="14" text-anchor="middle">IPD‑12</text>

  <!-- Three stacked QIM manifolds -->
  <!-- QIM 1 -->
  <rect x="40" y="40" width="180" height="60" fill="none" stroke="black" stroke-width="3"/>
  <text x="130" y="35" font-size="12" text-anchor="middle">QIM₁</text>
  <line x1="220" y1="55" x2="280" y2="55" stroke="black" stroke-width="3"/>
  <line x1="220" y1="65" x2="280" y2="65" stroke="black" stroke-width="3"/>
  <line x1="220" y1="75" x2="280" y2="75" stroke="black" stroke-width="3"/>

  <!-- QIM 2 -->
  <rect x="40" y="130" width="180" height="60" fill="none" stroke="black" stroke-width="3"/>
  <text x="130" y="125" font-size="12" text-anchor="middle">QIM₂</text>
  <line x1="220" y1="145" x2="280" y2="145" stroke="black" stroke-width="3"/>
  <line x1="220" y1="155" x2="280" y2="155" stroke="black" stroke-width="3"/>
  <line x1="220" y1="165" x2="280" y2="165" stroke="black" stroke-width="3"/>

  <!-- QIM 3 -->
  <rect x="40" y="220" width="180" height="60" fill="none" stroke="black" stroke-width="3"/>
  <text x="130" y="215" font-size="12" text-anchor="middle">QIM₃</text>
  <line x1="220" y1="235" x2="280" y2="235" stroke="black" stroke-width="3"/>
  <line x1="220" y1="245" x2="280" y2="245" stroke="black" stroke-width="3"/>
  <line x1="220" y1="255" x2="280" y2="255" stroke="black" stroke-width="3"/>

  <text x="130" y="305" font-size="10" text-anchor="middle">FSI: 3×QIM / full 12‑stack intake</text>
</svg>
```

If you want, next we can do a **headers/output manifold** SVG set that mirrors these intakes on the engine’s “exhaust” side for RTT/GU/Pantheon/FFT.
