# Scripts — CoConsciousness

Keep behaviors collaborative, ethical, and minimal. Prefer progressive enhancement.

- Storage prefix: `CoConsciousness:*`
- Auto-wired elements: `#theme-toggle`, same-page anchor links, `nav a`
- Respect: Reduced motion and keyboard navigation

Suggested CSS hooks:
```css
nav a.active { text-decoration: underline; }
body[data-theme="dark"] { background:#12101a; color:#f1eef7; }
body.user-is-tabbing a:focus { outline: 2px solid #c850c0; outline-offset: 2px; }
