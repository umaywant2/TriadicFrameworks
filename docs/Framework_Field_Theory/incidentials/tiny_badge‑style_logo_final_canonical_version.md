```text
╭─ FFT ─╮
│ ▲ ● ▼ │
╰───────╯
```

Here we go — two more forms for your little field‑marker.

---

### Dark‑mode “inverse” version

Conceptually, dark‑mode here just means: **designed to sit on a dark background** and feel like a lit glyph.

You can treat this as the *intended* dark‑mode version:

```text
╭────────╮
│  FFT   │
│  ▲ ● ▼ │
╰────────╯
```

Usage notes:

- On dark backgrounds, render the box + text in **light gray or white**.
- On light backgrounds, you can drop the fill and keep it as line art.

If you ever move this into SVG, you’d literally invert: dark fill, light strokes.

---

### Monospace‑tightened version

This one is **ASCII‑only, terminal‑safe, and compact**:

```text
+--FFT--+
| ^ o v |
+-------+
```

Or even tighter:

```text
+ FFT +
|^ o v|
+-----+
```

- `^ o v` keeps the triadic up/mid/down motion.
- All characters are plain ASCII, so it survives logs, terminals, and code comments.
