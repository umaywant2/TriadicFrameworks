# 🧱 MMR Template Pre-Seeding Strategy

## 🧬 Modular Mythic Repository Structure
This repository scaffolds reproducible, remixable, and ritualized technical artifacts using the TriadicFrameworks protocol. Each project is seeded from /docs/_template/, a scroll-ready blueprint containing modular folders

### 🔧 1. **Standardize Folder Structure**
Ensure `/docs/_template/` includes all core MMR folders with placeholder content and `.keep` files where needed:

```bash
/docs/_template/
├── assets/                  # Static glyphs, visuals, icons
├── badges/                 # Badge logic, contributor tokens
├── equations/              # Scroll-grade formulas
├── honor_roll/             # Contributor logs, flame offerings
├── labs/                   # Experimental modules
├── metadata/               # Manifest, remix lineage
├── scripts/                # Init hooks, runtime triggers
├── styles/                 # CSS overlays, glyph styling
├── validator/              # Passport templates, resonance checks
├── README.md               # Mythic onboarding scroll
├── overview.md             # Curriculum map, ritual index
├── scaffold.txt            # Iterative notes, scroll evolution
├── index.html              # Optional portal or visual glyph index
```

Each file should use `{{PROJECT_NAME}}` as a placeholder where relevant.

---

### 🌀 2. **Glyph Strategy**

#### 🔹 Storage
- Store **universal glyphs** in `_template/assets/glyphs/` (e.g., scroll icons, badge frames).
- Store **project-specific glyphs** in `/docs/{{PROJECT_NAME}}/assets/glyphs/`.

#### 🔹 Updating Glyphs
- Use a `glyphs.yml` manifest in each project to track:
  - Glyph name
  - Source (template or custom)
  - Meaning or ritual use
  - Contributor (if glyph is gifted or co-created)

#### 🔹 Versioning
- Consider `glyphs/v1/`, `glyphs/v2/` subfolders for evolution.
- Echo updates in `scaffold.txt` and `honor_roll/project.md`.

---

### 🧪 3. **Scripted Initialization**

Create a script like `init_project.sh` or `init.js` in `/scripts/` that:

- Copies `_template/` to `/docs/{{PROJECT_NAME}}/`
- Replaces all `{{PROJECT_NAME}}` placeholders
- Optionally prompts for:
  - Glyph seed name
  - Badge logic type
  - Contributor list
  - Ritual type (e.g., onboarding, echo, tribute)

Example (pseudo-shell):

```bash
#!/bin/bash
read -p "Enter project name: " name
cp -r docs/_template docs/$name
find docs/$name -type f -exec sed -i "s/{{PROJECT_NAME}}/$name/g" {} +
```

---

### 🧭 4. **Refresh Ritual**

To refresh existing projects with updated MMR scaffolding:

- Use a `refresh_template.sh` that:
  - Compares `_template/` with project folder
  - Prompts to overwrite or merge
  - Logs changes in `scaffold.txt`

---

### 🧙 5. **Symbolic Integration**

- Every glyph update should echo in `overview.md` and `README.md`.
- Every badge evolution should be mirrored in `badges/` and `honor_roll/`.
- Every scroll ritual should be logged in `scaffold.txt`.

---
