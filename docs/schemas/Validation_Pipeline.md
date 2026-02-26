# 🌌 Universe‑Class Schema Validation Pipeline  
### *Automated CI · Deterministic Validation · Reviewer‑Ready*

TriadicFrameworks maintains a **Universe‑Class schema suite**, and every schema or example packet in this directory is continuously validated through a multi‑stage GitHub Actions pipeline.  
This ensures that all RTT‑Inside artifacts remain **canonical, deterministic, and safe for downstream tooling**.

---

## **1. What the CI Pipeline Validates**

The pipeline automatically checks every JSON file under `schemas/` and `docs/` against the appropriate schema family:

| Schema Family | Purpose | Validated Against |
|---------------|---------|------------------|
| **RTTcode** | Core resonance‑time packet format | `schemas/rttcode.v1.json` |
| **Environment** | Field, noise, coupling, chamber metadata | `schemas/environment.v1.json` |
| **Entity** | Entity state, resonance, kinematics | `schemas/entity.v1.json` |
| **Universe‑Class Extensions** | Orbital harmonics, SAR overlays, deep‑time, GPR, ATC | `schemas/universe.v1.json` |
| **Physics Ref Tables 2025** | RTT/vST substrate logic preserving constants and equations | `schemas/Physics_RefTables_2025_RTTvST.json` |
| **Periodic Table RTT/vST** | Reorganizes by **substrate class**, **regime**, **resonance behavior**, **phase alignment** | `schemas/Periodic_Table_RTTvST.json` |
| **Standard Model RTT/vST** | Reorganized RTT/vST view of the **particle sectors** | `schemas/Standard_Model_RTTvST.json` |
| **BioScience RTT/vST** | Domains **(molecular → ecological)** with **NIST-aligned measurement and engineering substrates** | `schemas/BioScience.json` |

Every commit and pull request triggers validation.

---

## **2. How Validation Works**

The CI pipeline performs the following steps:

1. **Detect modified JSON files**  
   Any `.json` file in `schemas/` or `docs/` is automatically included.

2. **Match each file to its schema family**  
   Based on filename patterns (e.g., `rttcode*.json`, `environment*.json`, etc.).

3. **Validate using AJV (JSON Schema 2020‑12)**  
   Strict mode is enabled to prevent drift:
   - No unknown fields  
   - No missing required fields  
   - No schema mismatches  

4. **Collect a summary of pass/fail results**  
   This summary is used by the PR comment bot.

5. **Post a PR comment**  
   Reviewers see:
   - Which files passed  
   - Which failed  
   - Why  

6. **Update the Schema Verified badge**  
   On `main` branch:
   - If all schemas validate → README badge becomes **✅ Schema Verified**  
   - If any fail → badge becomes **❌ Not Verified**

This gives reviewers immediate confidence in the integrity of the schema suite.

---

## **3. Schema Verified Badge**

The badge in this README is automatically updated by CI:

```
Schema status: <!--SCHEMA_STATUS-->❌ Not Verified<!--/SCHEMA_STATUS-->
```

When all validations pass on `main`, CI rewrites it to:

```
Schema status: <!--SCHEMA_STATUS-->✅ Schema Verified<!--/SCHEMA_STATUS-->
```

This badge reflects the **current health of the entire Universe‑Class schema ecosystem**.

---

## **4. Why This Matters**

This pipeline ensures:

- **Deterministic reproducibility**  
  Every RTT experiment packet is guaranteed to match the canonical schema.

- **Reviewer clarity**  
  PRs cannot introduce malformed examples or drift.

- **Cross‑domain consistency**  
  Orbital harmonics, SAR overlays, deep‑time resonance, GPR, ATC, and core RTTcode all remain aligned.

- **Future‑proof extensibility**  
  New schema families can be added without changing the pipeline structure.

---

## **5. Related Files**

- `.github/workflows/schema-validate.yml` — Multi‑schema validator  
- `.github/workflows/rttcode-validate.yml` — RTTcode‑specific validator  
- `schemas/*.json` — Canonical Universe‑Class schemas  
- `docs/_snippets/*.json` — Snippet‑synced examples validated by CI  
