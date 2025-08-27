# Scripts — Hippocampus

Lightweight behaviors for memory engine demos and narrative UX.

- Storage prefix: `Hippocampus:*`
- Features: Theme toggle, nav highlight, smooth scrolling, keyboard focus ring
- Keep scripts framework-free and small for forkability.

Suggested CSS hooks:
```css
nav a.active { border-bottom: 2px solid #2a6f6f; }
body[data-theme="dark"] { background:#0f1c1a; color:#e8f5f2; }
body.user-is-tabbing a:focus { outline: 2px solid #2a6f6f; outline-offset: 2px; }
