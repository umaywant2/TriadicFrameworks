# Scripts — CoConsciousness

Keep behaviors collaborative, ethical, and minimal. Prefer progressive enhancement.

- Storage prefix: `CoConsciousness:*`
- Auto-wired elements: `#theme-toggle`, same-page anchor links, `nav a`
- Respect: Reduced motion and keyboard navigation

## helper-snippet.js
- Press "?" to open or close the overlay.
- Lists project name, quick actions, and references to core docs.
- Auto-styles itself; no HTML changes needed.
- Fork‑safe: works in any project folder as long as `helper-snippet.js` is loaded.

Suggested CSS hooks:
```css
nav a.active { text-decoration: underline; }
body[data-theme="dark"] { background:#12101a; color:#f1eef7; }
body.user-is-tabbing a:focus { outline: 2px solid #c850c0; outline-offset: 2px; }
