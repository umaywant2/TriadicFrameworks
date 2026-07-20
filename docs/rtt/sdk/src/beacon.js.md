```javascript
// beacon.js — helper utilities for RTT beacon events (beta)

export function createSessionId() {
  return "rtt-" + Math.random().toString(36).slice(2) + Date.now().toString(36);
}

export function collectStructureSnapshot() {
  return {
    url: typeof window !== "undefined" ? window.location.href : "",
    title: typeof document !== "undefined" ? document.title : "",
    nav_count: count("nav, header, footer"),
    main_count: count("main, [role='main']"),
    form_count: count("form"),
    button_count: count("button, [role='button']"),
    dom_nodes: typeof document !== "undefined"
      ? document.getElementsByTagName("*").length
      : 0
  };
}

function count(selector) {
  if (typeof document === "undefined") return 0;
  return document.querySelectorAll(selector).length;
}

export function buildBeaconPayload({ site, session, event }) {
  return {
    site,
    session,
    event,
    ts: new Date().toISOString(),
    structure: collectStructureSnapshot()
  };
}
```
