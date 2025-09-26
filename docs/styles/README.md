# 🎨 Styles Directory

This folder contains all **CSS stylesheets** used across TriadicFrameworks.

---

## 🧬 Structure

| File                          | Purpose                          |
|------------------------------|----------------------------------|
| `glyphic.css`                | Ritual animations and glyph logic
| `animations.css`, `aura.css` | Visual effects and transitions
| `blade_glow_spin_animation.css` | Symbolic spin effects
| `validator-dashboard.css`    | Styling for validator UI
| `tft-harmonics.css`          | TFT tool-specific harmonics
| `fff-controls.css`           | FFF tool interface styling
| `main.css`, `styles.css`     | General layout and base styles
| `old_animations.css`         | Legacy animations (to archive)

---

## 🧭 Usage Notes

- Rituals use `glyphic.css` via HTML embed in `.md` files.
- Tool dashboards link their own styles via CLI or HTML.
- Legacy styles may be deprecated—use `main.css` or `animations.css` for new work.

To contribute, add styles modularly and document them here.
