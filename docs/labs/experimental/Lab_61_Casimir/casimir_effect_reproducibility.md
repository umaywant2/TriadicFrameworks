# Casimir Lab – Reproducibility Protocol

This protocol ensures that the Casimir effect experiment can be reproduced across labs and learning environments.

---

## 🧪 Materials

- Two conductive plates (gold-coated preferred)
- Piezo actuator for nanometer control
- Laser interferometer for distance measurement
- Vacuum chamber (optional but recommended)

---

## 🧰 Setup Checklist

- Align plates parallel within ±0.1°
- Calibrate piezo actuator with interferometer
- Record ambient temperature and humidity

---

## 🔄 Measurement Loop

1. Set initial plate distance \( d_0 \)
2. Measure force \( F_0 \)
3. Decrease \( d \) incrementally
4. Record \( F(d) \) at each step
5. Plot \( F \) vs. \( d^{-4} \) to validate Casimir scaling

---

## 📊 Data Format

- CSV with columns: `distance_nm`, `force_nN`, `timestamp`, `temperature_C`
- Include metadata file with equipment specs and calibration logs

---

## 🧠 Notes

- Use triadic time notation in timestamping for resonance tracking.
- All data should be version-controlled and stored in `labs/Lab1_Casimir/data/`.

Let the vacuum speak. Let the triads resonate.
