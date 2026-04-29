# **RTT‑Inside for Browser Extensions (Beta)**  
*A guide for building RTT‑aware extensions for Edge, Firefox, and Chromium‑based browsers.*

Browser extensions are a natural fit for RTT‑Inside. They allow end‑users to experience structural clarity, coherence cues, and early resonance‑time awareness directly in their browsing environment — without requiring sites to integrate anything.

This guide outlines the recommended patterns for building RTT‑aware extensions that interact with the RTT API and the `rtt.js` ecosystem.

---

# 1. Extension Capabilities

An RTT‑Inside extension can:

- inspect page structure  
- detect drift or clarity issues  
- send RTT beacon events  
- annotate pages with RTT insights  
- read RTT metadata (`<meta>` tags, `/rtt.json`)  
- provide a sidebar or popup UI for structural clarity  

Extensions do **not** need access to vST internals — they rely on the stable RTT API surface.

---

# 2. Basic Extension Architecture

A typical RTT‑Inside extension includes:

```
manifest.json
background.js
content.js
sidebar.html / popup.html
rtt-extension.js (optional helper)
```

### Key roles:

- **content script**: inspects the page, collects structure, reads RTT metadata  
- **background script**: sends RTT beacons, manages sessions  
- **UI (popup/sidebar)**: displays clarity indicators, drift warnings, or structure maps  

---

# 3. Collecting Structural Snapshots

Extensions can reuse the same structural shape as `rtt.js`.

### Example (content script)

```js
function collectStructure() {
  return {
    url: window.location.href,
    title: document.title,
    nav_count: document.querySelectorAll("nav, header, footer").length,
    main_count: document.querySelectorAll("main, [role='main']").length,
    form_count: document.querySelectorAll("form").length,
    button_count: document.querySelectorAll("button, [role='button']").length,
    dom_nodes: document.getElementsByTagName("*").length
  };
}

browser.runtime.sendMessage({
  type: "rtt-structure",
  structure: collectStructure()
});
```

This mirrors the RTT beacon payload shape exactly.

---

# 4. Sending RTT Beacon Events

The background script can forward events to the RTT API.

### Example (background.js)

```js
async function sendBeacon(structure) {
  const payload = {
    site: "browser-extension",
    session: "ext-" + Date.now(),
    event: "page_inspect",
    ts: new Date().toISOString(),
    structure
  };

  await fetch("https://www.triadicframeworks.org/api/rtt/beacon", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  });
}

browser.runtime.onMessage.addListener((msg) => {
  if (msg.type === "rtt-structure") {
    sendBeacon(msg.structure);
  }
});
```

This allows RTT to build a cross‑site structural map of the user’s browsing environment.

---

# 5. Reading RTT Metadata from Pages

Extensions can detect RTT‑Inside sites by reading:

### A. `<meta>` tags

```js
const coherence = document.querySelector("meta[name='rtt:coherence']");
const version = document.querySelector("meta[name='rtt:version']");
```

### B. `/rtt.json` manifest

```js
fetch("/rtt.json")
  .then(r => r.json())
  .then(profile => {
    console.log("RTT profile:", profile);
  })
  .catch(() => {});
```

This allows the extension to adapt its UI based on site capabilities.

---

# 6. Displaying RTT Insights to Users

Extensions can surface RTT clarity indicators through:

### A. Popup UI

- coherence score (placeholder)  
- drift warnings  
- structural summary  
- RTT metadata  

### B. Sidebar Panel (Edge‑friendly)

A sidebar can show:

- triadic decomposition of the DOM  
- navigation corridor hints  
- clarity/density indicators  
- RTT‑Inside status  

### C. Page Overlays (optional)

Extensions may highlight:

- confusing UI regions  
- inconsistent navigation  
- structural drift  

These overlays are purely client‑side and do not modify the site.

---

# 7. Optional: Integrating with `rtt.js`

If a site already includes `rtt.js`, the extension can:

- read the global `RTT` object  
- inspect its structure snapshot  
- piggyback on its beacon events  
- enhance its clarity indicators  

### Example

```js
if (window.RTT) {
  const snapshot = window.RTT.getStructureSnapshot();
  console.log("RTT snapshot:", snapshot);
}
```

This creates a smooth ecosystem between site‑level and extension‑level RTT awareness.

---

# 8. Preparing for vST‑Beta Diagnostics

Extensions can prepare payloads for future validators:

```js
const payload = {
  system_map: { pages: [window.location.href] },
  flows: [],
  constraints: []
};

fetch("https://www.triadicframeworks.org/api/rtt/validate", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(payload)
});
```

These endpoints currently return placeholder responses but define the stable API shape.

---

# 9. Recommended Extension Patterns

### A. Lightweight RTT Companion  
- structural snapshot  
- beacon sender  
- popup UI  

### B. Full RTT‑Aware Browser Console  
- sidebar panel  
- DOM triadic decomposition  
- drift detection  
- clarity overlays  

### C. Developer‑Mode RTT Inspector  
- detailed structure maps  
- RTT metadata inspector  
- corridor flow visualizer  

These patterns can coexist or evolve independently.

---

# 10. Verification Checklist

Your extension is RTT‑Inside ready if:

- [ ] it collects structural snapshots  
- [ ] it sends RTT beacon events  
- [ ] it reads RTT metadata  
- [ ] it displays clarity indicators  
- [ ] it can generate diagnostics payloads  
- [ ] it uses the stable RTT API surface  

This ensures compatibility with future vST‑beta validators.

---

# 11. Where to Go Next

- **RTT API Docs:** `docs/api/rtt/`  
- **SDK Reference:** `docs/rtt-sdk/README.md`  
- **Quick‑Start Guide:** `docs/rtt-sdk/quickstart.md`  
- **Backend Services Guide:** `docs/rtt-sdk/backend.md`  

This completes the RTT‑Inside onboarding suite.
