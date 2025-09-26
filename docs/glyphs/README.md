# 🔮 Glyphs Directory

This folder contains **ritual scripts and symbolic animations** used across TriadicFrameworks.

---

## 🧬 Structure

| File                        | Purpose                                |
|----------------------------|----------------------------------------|
| `lantern_unfolding.js`     | Initiation ritual animation (badge trigger)
| `aura_pulse.js`            | Symbolic aura expansion (used in events)
| `blade_glow_spin.js`       | Spin effect for glyphic transitions
| `validator_flash.js`       | Visual feedback for validator dashboards

---

## 🧭 Usage Notes

- Scripts are triggered via embedded HTML in `.md` files.
- Use relative paths for compatibility:
```html
<script src="../../glyphs/lantern_unfolding.js"></script>
```
- Each script should define a callable function (e.g., `triggerLanternUnfolding(name)` ).

To contribute, add modular scripts and document their triggers here.
