# 🌈 **RTT Phase‑Mapping Rules (v1.0 Minimal Edition)**  
These rules align directly with the phase descriptions already in your repo’s README   [github.com](https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/resonance_atlas) but express them as **operational logic** for the harvester.

---

## **`map_phase()` — RTT Phase Mapping Logic**

Below is the conceptual version (the code version would be trivial to implement):

---

## **Phase I — ⚛️ Atomic / Molecular (10¹¹–10¹⁴ Hz)**  
**Corridor:** IR/Raman vibrational bands  
**Sources:** NIST, RSC, Bowserinator atomic JSON  
**Rule:**  
If the frequency is in the **terahertz** range or corresponds to **molecular vibration**, map to Phase I.

---

## **Phase II — 🧬 Biological (10⁻⁵–10¹ Hz)**  
**Corridor:** heartbeat, neural rhythms, circadian cycles  
**Sources:** biological datasets  
**Rule:**  
If the frequency corresponds to **organism‑scale cycles**, map to Phase II.

---

## **Phase III — 🍃 Ecological / Seasonal (10⁻⁷–10⁻³ Hz)**  
**Corridor:** seasonal, ecological, environmental cycles  
**Rule:**  
If the frequency corresponds to **environmental rhythms**, map to Phase III.

---

## **Phase IV — ⛰️ Geological (10⁻¹²–10⁻⁸ Hz)**  
**Corridor:** seismic, tectonic, geomagnetic  
**Sources:** USGS, geophysical datasets  
**Rule:**  
If the frequency corresponds to **planetary‑scale cycles**, map to Phase IV.

---

## **Phase V — 📜 Mythic / Civilizational (10⁻¹⁴–10⁻¹² Hz)**  
**Corridor:** cultural epochs, civilizational cycles  
**Rule:**  
If the frequency corresponds to **multi‑century human cycles**, map to Phase V.

---

## **Phase VI — ⭐ Cosmic (10⁹–10¹¹ Hz)**  
**Corridor:** CMB, stellar spectra  
**Sources:** NASA, Planck, WMAP  
**Rule:**  
If the frequency corresponds to **cosmic background or stellar resonance**, map to Phase VI.

---

# ⭐ **Minimal Pseudocode Version**

```python
def map_phase(freq_range_hz):
    f = parse_frequency(freq_range_hz)

    if 1e11 <= f <= 1e14:
        return "I", "⚛️"
    if 1e-5 <= f <= 1e1:
        return "II", "🧬"
    if 1e-7 <= f <= 1e-3:
        return "III", "🍃"
    if 1e-12 <= f <= 1e-8:
        return "IV", "⛰️"
    if 1e-14 <= f <= 1e-12:
        return "V", "📜"
    if 1e9 <= f <= 1e11:
        return "VI", "⭐"

    return None, None  # drift or out-of-corridor
```

This matches your existing phase definitions exactly, but expresses them in a way that a validator or scanner can use.
