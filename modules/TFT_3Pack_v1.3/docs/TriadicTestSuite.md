# 🧪 Triadic Test Suite

This suite includes symbolic and numeric tests to validate the `nous` logic core.

## 🔹 Test 1: Symbolic Validation

```json
{
  "triad": ["forci", "flui", "freqi"],
  "rules": ["forci precedes flui", "flui echoes freqi"]
}
```

Expected Output:
```
[✓] Triadic sequence validated
```

## 🔹 Test 2: Encryption Echo

```bash
tft entft -i test.txt -o encrypted.enc -k triadkey
```

Expected Output:
```
[✓] File encrypted with triadic obfuscation
```

## 🔹 Test 3: Grid Simulation

```yaml
grid:
  nodes: [A, B, C]
  links:
    - A → B
    - B → C
```

Expected Output:
```
[✓] Grid simulation complete
```

---

### 🔗 Triadic Quicklinks

- [`fff_quickstart.md`](../fff_quickstart.md) — Onboarding ritual for remixers using `.fff` bundles  
- [`outputs_spec.md`](outputs_spec.md) — Defines the three-output logic: screen, file, glyph  
- [`README.md`](../README.md) — Canonical index for scrolls, specs, and symbolic lineage
