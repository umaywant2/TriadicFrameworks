# Scripts — VictorG

Use this folder for VictorG-specific JavaScript. Keep behavior small, accessible, and portable.

- Purpose: Enhance navigation, theme toggling, and small UI niceties without external dependencies.
- Scope: Only affect elements inside this project’s pages. Prefix storage keys with `VictorG`.
- Accessibility: Respect reduced-motion preferences and keyboard users.

## Conventions
- File naming: `init.js` (bootstrap), optional helpers like `charts.js`, `render.js`.
- Local storage keys: `VictorG:*` (e.g., `VictorG:theme`, `VictorG:lastNav`).
- Theme toggle: If you add a button with `id="theme-toggle"`, the script will wire it automatically.

## helper-snippet.js
- Press "?" to open or close the overlay.
- Lists project name, quick actions, and references to core docs.
- Auto-styles itself; no HTML changes needed.
- Fork‑safe: works in any project folder as long as `helper-snippet.js` is loaded.

## Suggested CSS hooks
Add styles for:
```css
nav a.active { text-decoration: underline; font-weight: 600; }
body[data-theme="dark"] { background:#0b1320; color:#e6edf3; }
body.user-is-tabbing a:focus { outline: 2px solid #66afe9; outline-offset: 2px; }
