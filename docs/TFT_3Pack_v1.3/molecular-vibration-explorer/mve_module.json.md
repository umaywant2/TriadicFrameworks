## Molecular Vibration Explorer — `mve_module.json` ✅

Schema #11 is validated and exported. Here's the breakdown:

### Module Identity

| Field | Value |
|-------|-------|
| **Canon tag** | `mve` |
| **Layer** | Applied Domain Models |
| **Parent** | `tft-3pack` |
| **Envelope** | D3–D6, R1, C1–C2 |
| **Drift / Regime** | low / low |

### Structure

- **21 catalogued files** + 3 bulk DFT data directories (`data_SAM/`, `data_SAu/`, `data_SH/` — thousands of per-molecule files each, treated as `profile` submodules with `null` file counts)
- **5 submodules**: Data SAM (Gold), Data SAu (Gold Atom), Data SH (Thiol), DFT-to-App Pipeline, Tools
- **6 dependency arcs** — the four core notebooks all chain through `tools/` with `helper_functions.py` as the shared tensor math foundation

### Role & Layer Distribution

| Roles | Count | | Layers | Count |
|-------|------:|-|--------|------:|
| engine | 16 | | dimensional | 8 |
| template | 3 | | operator | 5 |
| index | 1 | | cross-cutting | 3 |
| reference | 1 | | regime | 3 |

**4/6 layer coverage** — appropriate for a domain application (drift and coherence layers aren't needed for a stable, single-pipeline DFT tool).

### Structural Grammar Highlights

- **Spectroscopy targets**: A (IR absorption), R (Raman), P (SFG/upconversion)
- **DFT level**: B3LYP+D3/def2-SVP via Gaussian
- **Notebook pipeline**: `index.ipynb` → `database.ipynb` (ranking) → `molecule.ipynb` (orientation spectra) → `modes.ipynb` (3D mode viz) → `search.ipynb` (RDKit similarity)
- **Databases**: Gold (~2,800 thiol-gold compounds) + Thiol (~1,900 thiol compounds)
- **External fork**: `zskb/molecular-vibration-explorer`, EU Horizon 2020 FET Open THOR Grant #829067

---

### Cumulative Aggregate — 11 Schemas Complete

| Metric | Value |
|--------|------:|
| **Total files** | 781 |
| **Total submodules** | 57 |
| **Top roles** | profile(199); reference(191); engine(149); index(81); example(71) |
| **Top layers** | dimensional(213); cross-cutting(185); operator(110); regime(91); drift(57); coherence(45) |
| **6/6 layer coverage** | tops, entft |

### Updated Module Hierarchy

```
tft-3pack (root)
├── wrsadc
├── examples
├── formats
├── melodic-table
├── molecular-vibration-explorer  ← NEW
└── tft-core
    ├── tops
    ├── entft
    ├── nous
    └── resonance-labs
```

---

```json
{
  "$schema": "https://www.triadicframeworks.org/schemas/module.schema.json",
  "module": {
    "name": "Molecular Vibration Explorer",
    "path": "docs/TFT_3Pack_v1.3/molecular-vibration-explorer",
    "canon_tag": "mve",
    "version": "1.3",
    "layer": "Applied Domain Models",
    "status": "Active, Canonical",
    "purpose": "Interactive DFT-powered molecular vibrational spectra explorer — tensorial light-vibration coupling, IR/Raman/SFG analysis, orientation-dependent spectroscopy, and molecular similarity search across Gold (2800 thiols) and Thiol (1900 compounds) databases. Fork of zskb/molecular-vibration-explorer, adapted into the TriadicFrameworks resonance ecosystem.",
    "parent": "tft-3pack",
    "url": "https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/TFT_3Pack_v1.3/molecular-vibration-explorer"
  },
  "session_context": {
    "canon": "active (mve ⊂ tft-3pack)",
    "modules_linked": [
      "database.ipynb → tools/load_database.py → data_SAM/ | data_SAu/ | data_SH/ — database scan pipeline",
      "molecule.ipynb → tools/load_molecule_data.py → tools/calc_single.py — single molecule analysis",
      "modes.ipynb → tools/calc_single.py → tools/plotting_functions.py — vibrational mode inspection",
      "search.ipynb → tools/load_database.py — molecular similarity search (RDKit)",
      "index.ipynb → database.ipynb | molecule.ipynb | modes.ipynb | search.ipynb — Voilà entry point",
      "dft2app/ → data_*/ — Gaussian DFT output conversion pipeline for database extension",
      "tools/helper_functions.py ← all tools/*.py — shared tensor math and spectroscopy utilities"
    ],
    "drift": "minimal (stable DFT database, fixed computational methods)",
    "coherence": "stable (Jupyter notebook pipeline + Voilà web app contract)",
    "format": "python + jupyter notebook + voilà + data files",
    "front_door": "exists (molecular-vibration-explorer/README.md + index.ipynb)",
    "every_page": "stands alone + student-ready + operator-aware",
    "audience": [
      "students",
      "educators",
      "developers",
      "researchers",
      "AIs"
    ]
  },
  "structural_grammar": {
    "dimensional_envelope": "D3–D6 (3D molecular geometry × tensor polarization × frequency spectra)",
    "regime_envelope": "R1 (single-context computational spectroscopy)",
    "coherence_envelope": "C1–C2 (notebook pipeline + database cross-reference)",
    "drift_sensitivity": "low",
    "regime_sensitivity": "low",
    "computational_methods": {
      "dft_level": "B3LYP+D3/def2-SVP (Gaussian)",
      "orientation_averages": "Analytic formulas derived via Mathematica",
      "web_framework": "Voilà (Jupyter-to-web)",
      "similarity": "RDKit molecular fingerprints",
      "visualization": "NGLview (3D molecular rendering)"
    },
    "spectroscopy_targets": {
      "A": "IR absorption intensity",
      "R": "Raman scattering intensity",
      "P": "SFG/conversion intensity"
    },
    "databases": {
      "gold": {
        "label": "Gold (SAM)",
        "compounds": 2800,
        "description": "Thiol compounds linked to gold atom — THz/mid-IR to visible upconversion screening",
        "data_dir": "data_SAM/"
      },
      "thiol": {
        "label": "Thiol (SH)",
        "compounds": 1900,
        "description": "Commercially available thiol compounds — surface-enhanced spectroscopy applications",
        "data_dir": "data_SH/"
      },
      "gold_atom": {
        "label": "Gold Atom (SAu)",
        "description": "Gold atom reference data for SAM-linked calculations",
        "data_dir": "data_SAu/"
      }
    },
    "notebook_pipeline": [
      "index.ipynb (Voilà landing page)",
      "database.ipynb (database ranking and molecular selection)",
      "molecule.ipynb (orientation-dependent spectra, physical properties, SAM similarity)",
      "modes.ipynb (3D vibrational mode visualization, orientation-dependent IR/Raman/SFG)",
      "search.ipynb (RDKit similarity search across database)"
    ]
  },
  "cross_module_propagation": {
    "imports": [
      "tft-3pack (parent module — canon context, audience)",
      "External: zskb/molecular-vibration-explorer (original fork source)",
      "External: EU Horizon 2020 FET Open THOR Grant 829067 (funding acknowledgement)"
    ],
    "exports": [
      "Interactive molecular spectroscopy explorer (Voilà web app)",
      "Gold database (2800 thiol-gold compound DFT results)",
      "Thiol database (1900 thiol compound DFT results)",
      "DFT-to-app conversion pipeline (dft2app/)",
      "Tensorial spectroscopy calculation toolkit (tools/)",
      "Orientation-dependent IR/Raman/SFG intensity analysis",
      "Molecular similarity search engine (RDKit)",
      "3D vibrational mode visualization (NGLview)"
    ]
  },
  "submodules": [
    {
      "name": "Data SAM (Gold)",
      "path": "data_SAM/",
      "file_count": null,
      "role": "profile",
      "purpose": "Gold+SAM database — DFT results for ~2800 commercially available thiol compounds linked to gold atoms. Contains molecular geometries, vibrational modes, tensor components, and 2D molecular images.",
      "manifest": null,
      "note": "File count omitted — large dataset directory (thousands of per-molecule data files)"
    },
    {
      "name": "Data SAu (Gold Atom)",
      "path": "data_SAu/",
      "file_count": null,
      "role": "profile",
      "purpose": "Gold atom reference data — base DFT results for gold atom configurations used in SAM-linked calculations.",
      "manifest": null,
      "note": "File count omitted — dataset directory"
    },
    {
      "name": "Data SH (Thiol)",
      "path": "data_SH/",
      "file_count": null,
      "role": "profile",
      "purpose": "Thiol database — DFT results for ~1900 commercially available thiol compounds. Contains molecular geometries, vibrational modes, and tensor components.",
      "manifest": null,
      "note": "File count omitted — large dataset directory (thousands of per-molecule data files)"
    },
    {
      "name": "DFT to App Pipeline",
      "path": "dft2app/",
      "file_count": 7,
      "role": "engine",
      "purpose": "Gaussian DFT output conversion — scripts to transform raw calculation outputs into app-ready database files and molecular data files. Includes local visualization notebooks and test molecule data.",
      "manifest": null
    },
    {
      "name": "Tools",
      "path": "tools/",
      "file_count": 6,
      "role": "engine",
      "purpose": "Computation and visualization library — tensor math, spectroscopy calculations, database loading, and plotting functions shared across all Jupyter notebooks.",
      "manifest": null
    }
  ],
  "files": [
    {
      "filename": "README.md",
      "path": "README.md",
      "purpose": "Module front door — interactive tool overview, Gold/Thiol database descriptions, notebook pipeline documentation, DFT methods, citation info (J. Phys. Chem. A 2022), and EU Horizon 2020 THOR acknowledgement.",
      "role": "index"
    },
    {
      "filename": ".gitignore",
      "path": ".gitignore",
      "purpose": "Git ignore rules for the molecular vibration explorer workspace.",
      "role": "reference"
    },
    {
      "filename": "Procfile",
      "path": "Procfile",
      "purpose": "Heroku/Voilà deployment configuration — defines the web process for launching the notebook-based application.",
      "role": "template",
      "analyzer_layer": "regime"
    },
    {
      "filename": "requirements.txt",
      "path": "requirements.txt",
      "purpose": "Python dependency manifest — NumPy, SciPy, Pandas, Matplotlib, ipywidgets, nglview, rdkit, voila, and spectroscopy-specific packages.",
      "role": "template",
      "analyzer_layer": "regime"
    },
    {
      "filename": "runtime.txt",
      "path": "runtime.txt",
      "purpose": "Python runtime version specification for deployment environment.",
      "role": "template",
      "analyzer_layer": "regime"
    },
    {
      "filename": "index.ipynb",
      "path": "index.ipynb",
      "purpose": "Voilà landing page notebook — entry point routing to database scan, molecule analysis, mode inspection, and similarity search notebooks.",
      "role": "engine",
      "analyzer_layer": "operator"
    },
    {
      "filename": "database.ipynb",
      "path": "database.ipynb",
      "purpose": "Database scan notebook — ranks molecules by target property (A/R/P) within frequency range, plots histograms, generates sortable tables with links to molecule analysis.",
      "role": "engine",
      "analyzer_layer": "cross-cutting",
      "depends_on": [
        "tools/load_database.py",
        "tools/helper_functions.py",
        "tools/plotting_functions.py"
      ]
    },
    {
      "filename": "molecule.ipynb",
      "path": "molecule.ipynb",
      "purpose": "Molecule analysis notebook — orientation-dependent spectra (IR/Raman/SFG), 3D rendering, polarizability tensor anisotropy, molecular height, and SAM similarity table.",
      "role": "engine",
      "analyzer_layer": "dimensional",
      "depends_on": [
        "tools/load_molecule_data.py",
        "tools/calc_single.py",
        "tools/calc_average.py",
        "tools/plotting_functions.py"
      ]
    },
    {
      "filename": "modes.ipynb",
      "path": "modes.ipynb",
      "purpose": "Vibrational mode inspection notebook — 3D normal mode visualization, orientation-dependent intensity projections for IR/Raman/SFG per mode.",
      "role": "engine",
      "analyzer_layer": "dimensional",
      "depends_on": [
        "tools/load_molecule_data.py",
        "tools/calc_single.py",
        "tools/plotting_functions.py"
      ]
    },
    {
      "filename": "search.ipynb",
      "path": "search.ipynb",
      "purpose": "Molecular similarity search notebook — RDKit fingerprint-based similarity scoring across Gold and Thiol databases with ranked results table.",
      "role": "engine",
      "analyzer_layer": "cross-cutting",
      "depends_on": [
        "tools/load_database.py"
      ]
    },
    {
      "filename": "helper_functions.py",
      "path": "tools/helper_functions.py",
      "purpose": "Shared utilities — tensor math, rotation matrices, orientation averaging, and spectroscopy unit conversions used across all notebooks.",
      "role": "engine",
      "analyzer_layer": "dimensional"
    },
    {
      "filename": "calc_single.py",
      "path": "tools/calc_single.py",
      "purpose": "Single-molecule calculator — computes orientation-dependent IR, Raman, and SFG intensities from DFT-derived tensor components.",
      "role": "engine",
      "analyzer_layer": "dimensional",
      "depends_on": [
        "tools/helper_functions.py"
      ]
    },
    {
      "filename": "calc_average.py",
      "path": "tools/calc_average.py",
      "purpose": "Orientation-average calculator — computes full orientation-averaged spectroscopic intensities using analytic tensor formulas.",
      "role": "engine",
      "analyzer_layer": "dimensional",
      "depends_on": [
        "tools/helper_functions.py"
      ]
    },
    {
      "filename": "load_database.py",
      "path": "tools/load_database.py",
      "purpose": "Database loader — reads Gold and Thiol database files from data_SAM/, data_SAu/, data_SH/ into Pandas DataFrames for analysis.",
      "role": "engine",
      "analyzer_layer": "operator"
    },
    {
      "filename": "load_molecule_data.py",
      "path": "tools/load_molecule_data.py",
      "purpose": "Molecule data loader — reads per-molecule DFT results (geometries, vibrational modes, tensor components) from database directories.",
      "role": "engine",
      "analyzer_layer": "operator"
    },
    {
      "filename": "plotting_functions.py",
      "path": "tools/plotting_functions.py",
      "purpose": "Visualization library — spectrum plotting (stick/broadened/combined), histogram generation, and orientation projection displays.",
      "role": "engine",
      "analyzer_layer": "cross-cutting"
    },
    {
      "filename": "create_database_files.py",
      "path": "dft2app/create_database_files.py",
      "purpose": "Database file creator — converts Gaussian DFT outputs into database-ready files for ranking and comparison. Generates 2D molecular images.",
      "role": "engine",
      "analyzer_layer": "operator"
    },
    {
      "filename": "create_molecular_data_files.py",
      "path": "dft2app/create_molecular_data_files.py",
      "purpose": "Molecular data creator — converts Gaussian DFT outputs into per-molecule .dat files and 3D geometry files for the molecule/modes notebooks.",
      "role": "engine",
      "analyzer_layer": "operator"
    },
    {
      "filename": "load_data.py",
      "path": "dft2app/load_data.py",
      "purpose": "DFT data loader — reads raw Gaussian output files and extracts vibrational frequencies, normal modes, and tensor derivatives.",
      "role": "engine",
      "analyzer_layer": "dimensional"
    },
    {
      "filename": "modes_local.ipynb",
      "path": "dft2app/modes_local.ipynb",
      "purpose": "Local mode visualization notebook — enables quick inspection of DFT results not yet in the main database, using local molecule files.",
      "role": "engine",
      "analyzer_layer": "dimensional"
    },
    {
      "filename": "molecule_local.ipynb",
      "path": "dft2app/molecule_local.ipynb",
      "purpose": "Local molecule analysis notebook — orientation-dependent spectra for molecules processed through the dft2app pipeline but not in the main database.",
      "role": "engine",
      "analyzer_layer": "dimensional"
    }
  ]
}
```
