# 🧪 Triadic Test Suite

This suite includes symbolic and numeric tests to validate the `nous` logic core.

## 🔹 Test 1: Symbolic Validation

```json
{
  "triad": ["alpha", "beta", "gamma"],
  "rules": ["alpha precedes beta", "beta echoes gamma"]
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
