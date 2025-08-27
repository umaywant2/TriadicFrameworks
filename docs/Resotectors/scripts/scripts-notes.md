# Scripts — Resotectors

Small, precise scripts aligned with sensor and spectral workflows.

- Storage prefix: `Resotectors:*`
- Features: Theme, nav, smooth scrolling, a11y focus rings
- Extend with sensor demo scripts as needed (e.g., `spectrum-demo.js`)

Suggested CSS hooks:
```css
nav a.active { border-bottom: 2px solid #00ffcc; }
body[data-theme="dark"] { background:#0d0d1a; color:#e6fdf8; }
body.user-is-tabbing a:focus { outline: 2px solid #00cc99; outline-offset: 2px; }
