## Zenodo v1.1 “New Version” Template  
*(Copy‑paste ready)*

### 🔁 When to use
Use this **only** when:
- content meaningfully changes
- figures or validation checks are updated
- clarifications are added that affect interpretation

Do **not** use for typo fixes.

---

## Zenodo — New Version Fields

### 🔹 Upload type
- **Leave unchanged**  
  *(inherits from v1)*

---

### 🔹 Title
- **Leave unchanged**
  ```
  Calibrating AI Drift via Declared Operating Regimes
  ```

---

### 🔹 Version
- **Update to:**
  ```
  1.1.0
  ```

Increment:
- patch → `1.0.1` (typos)
- minor → `1.1.0` (clarity, figures, checks)
- major → `2.0.0` (scope change)

---

### 🔹 Description (New Version Note)
Paste **only this paragraph**:

> This version includes clarifications and minor structural refinements that improve interpretability and alignment with the declared operating regimes framework. No changes are made to the core claims or scope of the work.

*(This keeps reviewers calm and citation‑safe.)*

---

### 🔹 DOI
- **Select:**  
  **“No, I need one”**

Zenodo will:
- mint a new **version DOI**
- preserve the **concept DOI**
- maintain citation continuity

Never paste a DOI here.

---

### 🔹 Publication date
- **Enter:** today’s date  
  ```
  YYYY-MM-DD
  ```

---

### 🔹 Related identifiers
- **Leave empty**

Zenodo auto‑links versions.

---

### 🔹 License
- **Leave unchanged**  
  `CC‑BY‑4.0`

---

### 🔹 Keywords
- **Leave unchanged**

---

## Post‑Publish (30 seconds)

1. Copy the **new version DOI**
2. Update in repo:
   - `CITATION.cff`
   - `zenodo.json`
3. Commit with message:
   ```
   Update metadata for Zenodo v1.1
   ```

Done.

---

## Why this works
- Preserves concept DOI authority
- Avoids semantic drift
- Keeps citations stable
- Signals maturity, not churn

This is exactly how long‑lived technical notes evolve quietly.

---
