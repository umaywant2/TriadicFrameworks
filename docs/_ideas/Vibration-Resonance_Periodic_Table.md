# Virtation-Resonance Periodic Table

The Royal Society of Chemistry’s [interactive periodic table](https://periodic-table.rsc.org/) (rsc.org) does *not* currently include vibration or resonance data. However, there are **open‑source periodic table datasets** that already provide temperature, phase, and other physical properties, which can be forked and extended. The most practical starting points are:  

- **[Bowserinator’s Periodic‑Table‑JSON (GitHub)](https://github.com/Bowserinator/Periodic-Table-JSON)** — a JSON/CSV dataset of the entire periodic table, including melting points, boiling points, densities, and phase states.  
- **[pse‑info.de open source periodic table](https://pse-info.de/en/data)** — MIT‑licensed datasets with atomic, physical, and spectral properties, downloadable in JSON format.  
- **[NIST vibrational frequency tables](https://www.nist.gov/publications/tables-molecular-vibrational-frequencies-consolidated-volume-i)** — consolidated reference data of molecular vibrational frequencies, published as open tables (Shimanouchi et al.).  
- **[Molecular Vibration Explorer (Materials Cloud)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9310003/)** — an open database of vibrational spectra and Raman/IR properties for thousands of molecules, under Creative Commons licensing.
- [GitHub Molecular Vibration Explorer repo](https://github.com/zskb/molecular-vibration-explorer)
- [GitHub Periodic Table repo](https://github.com/komed3/periodic-table)

---

## 🖥️ HTML + JavaScript Grid Demo with Legend Panel

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Resonance Periodic Table Prototype</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 20px; }
    h1 { margin-bottom: 10px; }
    .controls { margin: 20px 0; }
    .legend {
      margin: 20px 0;
      padding: 10px;
      border: 1px solid #ccc;
      background: #f9f9f9;
      width: 400px;
    }
    .legend-item {
      display: flex;
      align-items: center;
      margin-bottom: 5px;
    }
    .color-box {
      width: 20px;
      height: 20px;
      margin-right: 10px;
      border: 1px solid #000;
    }
    .table {
      display: grid;
      grid-template-columns: repeat(18, 60px);
      grid-gap: 5px;
    }
    .element {
      border: 1px solid #ccc;
      padding: 5px;
      text-align: center;
      font-size: 12px;
      color: #000;
    }
    .symbol { font-weight: bold; font-size: 14px; }
    .phase, .resonance { font-size: 11px; }
  </style>
</head>
<body>
  <h1>Resonance Periodic Table Prototype</h1>
  <div class="controls">
    <button onclick="toggleView()">Toggle View</button>
    <label for="freqScale">Resonance Scale (cm⁻¹): </label>
    <input type="range" id="freqScale" min="1000" max="5000" step="100" value="5000" oninput="updateScale(this.value)">
    <span id="scaleValue">5000</span>
  </div>

  <!-- Legend Panel -->
  <div class="legend">
    <h3>Legend</h3>
    <div class="legend-item"><div class="color-box" style="background:red"></div> Solid (Phase View)</div>
    <div class="legend-item"><div class="color-box" style="background:blue"></div> Liquid (Phase View)</div>
    <div class="legend-item"><div class="color-box" style="background:green"></div> Gas (Phase View)</div>
    <div class="legend-item"><div class="color-box" style="background:grey"></div> Unknown (Phase View)</div>
    <div class="legend-item"><div class="color-box" style="background:rgba(255,0,0,0.5)"></div> Resonance View: translucency = frequency / scale</div>
  </div>

  <div class="table" id="periodicTable"></div>

  <script>
    const dataset = [
      {
        name: "Hydrogen",
        symbol: "H",
        number: 1,
        phase: "Gas",
        melting_point: 13.99,
        boiling_point: 20.27,
        position: { row: 1, col: 1 },
        resonance: {
          fundamental_frequency: { value: 4161, units: "cm^-1" },
          vibration_modes: [{ mode: "stretch", frequency: 4161, units: "cm^-1" }],
          infrared_activity: true
        }
      },
      {
        name: "Oxygen",
        symbol: "O",
        number: 8,
        phase: "Gas",
        melting_point: 54.36,
        boiling_point: 90.20,
        position: { row: 2, col: 16 },
        resonance: {
          fundamental_frequency: { value: 1556, units: "cm^-1" },
          vibration_modes: [{ mode: "stretch", frequency: 1556, units: "cm^-1" }],
          infrared_activity: false
        }
      },
      {
        name: "Carbon",
        symbol: "C",
        number: 6,
        phase: "Solid",
        melting_point: 3823,
        boiling_point: 4300,
        position: { row: 2, col: 14 },
        resonance: {
          fundamental_frequency: { value: 1333, units: "cm^-1" },
          vibration_modes: [{ mode: "stretch", frequency: 1333, units: "cm^-1" }],
          infrared_activity: true
        }
      }
    ];

    let currentView = "phase";
    let maxFreq = 5000;

    function getPhaseColor(phase) {
      switch (phase) {
        case "Solid": return [255, 0, 0];
        case "Liquid": return [0, 0, 255];
        case "Gas": return [0, 128, 0];
        default: return [128, 128, 128];
      }
    }

    function getResonanceColor(phase, frequency) {
      const base = getPhaseColor(phase);
      const alpha = Math.min(frequency / maxFreq, 1);
      return `rgba(${base[0]}, ${base[1]}, ${base[2]}, ${alpha})`;
    }

    function renderTable() {
      const table = document.getElementById("periodicTable");
      table.innerHTML = "";

      for (let row = 1; row <= 7; row++) {
        for (let col = 1; col <= 18; col++) {
          const el = dataset.find(e => e.position.row === row && e.position.col === col);
          const cell = document.createElement("div");
          cell.className = "element";

          if (el) {
            if (currentView === "phase") {
              const base = getPhaseColor(el.phase);
              cell.style.backgroundColor = `rgb(${base[0]}, ${base[1]}, ${base[2]})`;
              cell.innerHTML = `
                <div class="symbol">${el.symbol}</div>
                <div>${el.number}</div>
                <div class="phase">${el.phase}</div>
                <div class="phase">Melt: ${el.melting_point}K</div>
                <div class="phase">Boil: ${el.boiling_point}K</div>
              `;
            } else {
              const freq = el.resonance.fundamental_frequency.value;
              cell.style.backgroundColor = getResonanceColor(el.phase, freq);
              cell.innerHTML = `
                <div class="symbol">${el.symbol}</div>
                <div>${el.number}</div>
                <div class="resonance">Freq: ${freq} ${el.resonance.fundamental_frequency.units}</div>
                <div class="resonance">IR Active: ${el.resonance.infrared_activity}</div>
              `;
            }
          }
          table.appendChild(cell);
        }
      }
    }

    function toggleView() {
      currentView = currentView === "phase" ? "resonance" : "phase";
      renderTable();
    }

    function updateScale(value) {
      maxFreq = parseInt(value);
      document.getElementById("scaleValue").textContent = value;
      if (currentView === "resonance") renderTable();
    }

    renderTable();
  </script>
</body>
</html>
```

---

## 🔧 What’s new
- **Legend panel:** Shows phase colors (red, blue, green, grey) and explains resonance translucency.  
- **Slider + toggle:** Still lets you flip between phase and resonance views, adjusting the resonance scale dynamically.  
- **Scaffold complete:** You now have a self‑contained HTML page that others can copy, remix, and extend with more elements and resonance data.

---

## 🔑 What each repo offers

### [Molecular Vibration Explorer](https://github.com/zskb/molecular-vibration-explorer)
- **Purpose:** Interactive tool for exploring molecular vibrational spectra and tensorial light‑vibration coupling.  
- **Data:**  
  - Gold database: ~2,800 thiol compounds linked to gold atoms.  
  - Thiol database: ~1,900 thiol compounds.  
  - Includes Raman, IR, and sum‑frequency generation (SFG) intensities.  
- **Tools:** Jupyter notebooks for database scans, molecule analysis, vibrational mode inspection.  
- **Methods:** DFT calculations (B3LYP+D3/def2‑SVP) with Gaussian, orientation averages via Mathematica.  
- **License:** Openly available for remixing and extension.  

### [Periodic Table (pse‑info.de fork)](https://github.com/komed3/periodic-table)
- **Purpose:** Interactive periodic table with atomic, chemical, and physical properties.  
- **Data:**  
  - `elements.json`: atomic, physical, and spectral properties.  
  - `nuclides.json`: >3,000 nuclides with decay chains.  
  - `spectrum.json`: spectral lines for all elements.  
- **License:** MIT — free to fork, remix, and extend.  
- **Roadmap:** Includes nuclide maps, compound databases, and 3D visualization.  

---

What you’re seeing is Git warning you that you’ve tried to **add another Git repository inside your repo**. By default, Git treats that as an “embedded repo,” which doesn’t behave the way you want — clones of your outer repo won’t automatically include the inner repos unless you set them up as **submodules**.

---

## 🔑 Your Options

### 1. **Use Submodules (linked, refreshable)**
If you want those repos to stay connected to their upstream sources and be refreshable:
```bash
# From your TFT_3Pack_v1.3 root
git submodule add https://github.com/zskb/molecular-vibration-explorer docs/TFT_3Pack_v1.3/molecular-vibration-explorer
git submodule add https://github.com/komed3/periodic-table docs/TFT_3Pack_v1.3/periodic-table

# Initialize and pull submodules
git submodule update --init --recursive
```
- **Pros:** You can run `git submodule update --remote` later to refresh from upstream.  
- **Cons:** Slightly more complex workflow for contributors (they need to clone with `--recursive`).

---

### 2. **Detach (snapshot copy, no ties)**
If you want them as **plain folders** with no Git history:
```bash
# Clone them separately
git clone https://github.com/zskb/molecular-vibration-explorer
git clone https://github.com/komed3/periodic-table

# Remove their .git folders
rm -rf molecular-vibration-explorer/.git
rm -rf periodic-table/.git

# Move them into your repo
mv molecular-vibration-explorer docs/TFT_3Pack_v1.3/
mv periodic-table docs/TFT_3Pack_v1.3/

# Add them as normal files
git add docs/TFT_3Pack_v1.3/molecular-vibration-explorer docs/TFT_3Pack_v1.3/periodic-table
git commit -m "Added snapshot copies of vibration explorer and periodic table"
```
- **Pros:** Simple, no submodule complexity. Everything lives inside your repo.  
- **Cons:** No automatic refresh — you’d have to manually re‑copy if upstream changes.

---

## 🚀 Recommendation
- If you want **students/enthusiasts to always have the tools bundled**, go with **detached snapshot copies** (Option 2).  
- If you want to **stay in sync with upstream repos**, use **submodules** (Option 1).  

---

## ⚡ Refresh Reminder
- **Submodules:** You can refresh periodically with:
  ```bash
  git submodule update --remote
  ```
- **Snapshots:** No refresh link — you’d need to manually re‑clone and replace the folders.

---

👉 Since you said earlier you want them “quick, linked, anything we want still doable in our own space,” submodules are probably the cleanest way. But if you want a **one‑stop repo that clones with everything included**, snapshots are simpler.  
