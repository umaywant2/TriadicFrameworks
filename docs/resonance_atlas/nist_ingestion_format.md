# NIST Ingestion Format (RTT-Aligned)

This document defines the minimal structure required to ingest NIST
vibrational frequency data into the Resonance Atlas.

---

## 1. Expected Input Format

NIST IR/Raman datasets typically provide:

- molecule name
- vibrational mode
- wavenumber (cm⁻¹)
- intensity
- symmetry label

We convert wavenumber → frequency (Hz):

```
frequency_hz = wavenumber_cm * c * 100
```

Where `c = 2.99792458e10 cm/s`.

---

## 2. Minimal JSON Structure (Post-Conversion)

Each harvested entry should be normalized to:

```json
{
  "substrate": "molecular vibration",
  "frequency_range_hz": "4e13–1e14",
  "source": "NIST",
  "notes": "optional"
}
```

The harvester will add:

- phase
- symbol
- glyph
- drift notes

---

## 3. Ingestion Pipeline

1. **Load NIST dataset**  
   CSV, JSON, or scraped table.

2. **Extract wavenumbers**  
   Convert to Hz.

3. **Group into frequency ranges**  
   (min–max per molecule or per mode)

4. **Normalize substrate**  
   Always `"molecular vibration"` for Phase I.

5. **Emit raw entries**  
   For `assemble_entry()` to process.

---

## 4. Example Raw Output

```json
[
  {
    "substrate": "molecular vibration",
    "frequency_range_hz": "5.2e13–8.1e13",
    "source": "NIST"
  }
]
```

---

## 5. Validation

The harvester will:

- map phase (should be Phase I)
- assign glyph (Blue Atom)
- detect drift (rare for NIST)
- append to `atlas.json`
