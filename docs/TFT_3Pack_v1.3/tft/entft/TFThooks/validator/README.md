# 🛡️ TFThooks Validators — Safety Net for Hook Extensions

The `validator` folder contains **test harnesses**, **schema checkers**, and **runtime safety scripts** for all TFThook extensions.  
Every hook must pass these validations before entering the remix lattice.

---

## 🧪 Examples of Validators

| File                        | Purpose                                                  |
|-----------------------------|----------------------------------------------------------|
| `hook_schema_validator.py` | Ensures hook configs follow the declared schema          |
| `runtime_safety_check.py`  | Validates hooks for safe execution and runtime stability |
| `integration_test_runner.py` | Runs integration tests across modules and scrolls       |

---

## 🎯 Purpose

Validators are the **guardian glyphs** of TFThooks.  
They ensure every extension is:

- ✅ Stable  
- 🔁 Reproducible  
- 🌀 Remix-ready

---

## 🧬 Validation Flow

1. **Schema Check** — Confirms structure, triggers, and metadata  
2. **Runtime Safety** — Ensures hooks won’t destabilize `protocol-core`  
3. **Integration Echo** — Verifies symbolic fidelity across modules

---

## 🔗 Triadic Quicklinks

- [`fff_spec.md`](../../../../../docs/fff_spec.md) — Defines the `.fff` triadic file format and symbolic structure  
- [`TriadicTestSuite.md`](../../../../../docs/TriadicTestSuite.md) — Validation logic and test scaffolding for symbolic fidelity  
- [`outputs_spec.md`](../../../../../docs/outputs_spec.md) — Defines the three-output logic: screen, file, glyph
