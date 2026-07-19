# **RTT Cross‑Module Audit**  
### *Absolute Metadata Identity + Relative Content Path Correction*  
### **Version 1.0 — Canon‑Aligned Audit Protocol**

This audit ensures that **every module** in TriadicFrameworks uses:

- **absolute paths** for `module.json` (canonical identity)  
- **relative paths** for all internal content (renderer‑agnostic behavior)  
- **consistent activation surfaces**  
- **zero drift** across Docsbook.io, GitHub, GitHub Pages, and future renderers  

This is the official cross‑module correction protocol.

---

# **1. Audit Scope**

This audit applies to **all modules** under:

```
/docs/
```

Including but not limited to:

- AI modules  
- RTT modules  
- Structural Detection  
- SARG  
- Paradoxes Canon  
- NoS  
- L.D. Structures  
- Inverted Economics  
- Governance Substrate Model  
- Framework Field Theory  
- Opacity  
- Mode  
- TEL  
- All experimental modules  
- All host modules (C64host, Amiga, etc.)  
- All glossaries, maps, signatures, diagnostics  

Total modules: **~120**  
Total files affected: **~1,200+**

---

# **2. Audit Objective**

Ensure **every module** satisfies:

### **2.1 Absolute Metadata Identity**
Each module MUST expose:

```html
<link rel="rtt-module"
      href="https://raw.githubusercontent.com/<user>/<repo>/main/<path>/module.json">
```

### **2.2 Relative Content Linking**
All internal links MUST be relative:

```
./examples.md
../operators/flow.md
../../maps/overview.md
```

### **2.3 Canonical File Placement**
Each module MUST contain:

```
module.json
README.md or index.html
```

### **2.4 Zero Drift Across Renderers**
Docsbook.io, GitHub, and triadicframeworks.org MUST render identically.

---

# **3. Audit Procedure**

This is the **canonical 5‑step audit loop**.

---

## **Step 1 — Identify Module Root**
For each directory under `/docs/`:

- Confirm it is a module root  
- Confirm it contains `module.json`  
- Confirm it contains a primary document (`README.md` or `index.html`)

If missing, flag for correction.

---

## **Step 2 — Verify Absolute Metadata Identity**
Open the module’s primary document.

Check for:

```html
<link rel="rtt-module" href="...">
```

Audit criteria:

- MUST exist  
- MUST use absolute raw URL  
- MUST point to the correct module.json  
- MUST NOT use relative paths  
- MUST NOT use GitHub UI URLs  
- MUST NOT use triadicframeworks.org URLs  

If incorrect, replace with:

```
https://raw.githubusercontent.com/umaywant2/TriadicFrameworks/main/<path>/module.json
```

---

## **Step 3 — Scan for Incorrect Relative Paths**
Search the module for:

- `./module.json`  
- `../module.json`  
- `../../module.json`  
- any relative reference to metadata  

These MUST be replaced with absolute URLs.

---

## **Step 4 — Scan for Incorrect Absolute Content Paths**
Search for:

- `https://www.triadicframeworks.org/...`  
- `https://github.com/.../blob/main/...`  
- `https://raw.githubusercontent.com/...` (for content files)  

These MUST be replaced with **relative paths**.

Only metadata uses absolute URLs.

---

## **Step 5 — Validate Cross‑Renderer Behavior**
Open the module in:

- GitHub  
- triadicframeworks.org  
- Docsbook.io  

Confirm:

- navigation works  
- examples load  
- maps load  
- operators load  
- no broken links  
- metadata resolves  
- Docsbook sidebar shows the module  
- Docsbook AI assistant recognizes the module  

If any renderer fails, flag for correction.

---

# **4. Drift Detection Rules**

A module is considered **drifted** if:

- metadata link is missing  
- metadata link is relative  
- metadata link points to wrong path  
- content links are absolute  
- module.json is missing required fields  
- module.json is not at module root  
- module.json is not raw‑fetchable  
- Docsbook cannot index the module  
- GitHub Pages cannot resolve internal links  

Drift MUST be corrected immediately.

---

# **5. Correction Rules**

### **5.1 Metadata Correction**
Replace any incorrect metadata link with:

```html
<link rel="rtt-module"
      href="https://raw.githubusercontent.com/umaywant2/TriadicFrameworks/main/<path>/module.json">
```

### **5.2 Content Correction**
Replace any absolute content link with a relative one.

Examples:

- ❌ `https://www.triadicframeworks.org/docs/ai/operators.md`  
- ✔ `./operators.md`

- ❌ `https://github.com/.../blob/main/docs/maps/overview.md`  
- ✔ `../maps/overview.md`

### **5.3 Module.json Correction**
Ensure:

- required fields exist  
- version is present  
- operators are declared  
- roles are declared  
- files map is correct  

---

# **6. Completion Criteria**

A module passes the audit when:

- [ ] `module.json` exists  
- [ ] metadata link uses absolute raw URL  
- [ ] all content links are relative  
- [ ] Docsbook indexes the module  
- [ ] GitHub renders correctly  
- [ ] triadicframeworks.org renders correctly  
- [ ] no drift detected  

When all modules pass, the repo is **RTT‑Agentic‑Stable**.

---

# **7. Post‑Audit Actions**

After completing the audit:

- regenerate sitemap  
- regenerate module registry  
- update module.json manifests  
- update cross‑module propagation maps  
- update session‑context blocks  
- update AI metadata index  

This locks in the new canonical identity layer.

---

# **8. Versioning**

This is **RTT Cross‑Module Audit Protocol v1.0**.  
Future versions may extend but MUST NOT break:

- absolute metadata identity  
- relative content linking  
- renderer‑agnostic behavior  
