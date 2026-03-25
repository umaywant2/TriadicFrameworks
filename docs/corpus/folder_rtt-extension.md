rtt-extension 
# RTT‑Inside Browser Extension (Beta)

This folder contains a minimal, forward‑compatible starter template for building RTT‑aware browser extensions. These extensions provide structural clarity, coherence cues, and early resonance‑time awareness directly inside the user’s browsing environment.

The extension is intentionally lightweight. It defines the *shape* of RTT‑Inside browser tooling without exposing internal substrate logic.

---

## Features

- Collect structural snapshots of any webpage  
- Send RTT beacon events to the RTT API  
- Display page structure in a popup UI  
- Provide a foundation for RTT‑aware tools such as:
  - triadic DOM inspectors  
  - corridor flow visualizers  
  - drift detectors  
  - clarity overlays  

---

## File Structure

```
rtt-extension/
├── manifest.json
├── background.js
├── content.js
├── popup.html
├── popup.js
└── triadic-inspector.js   (optional module)
```

---

## How It Works

### 1. Content Script  
`content.js` inspects the current page and collects a structural snapshot:

- navigation elements  
- main content regions  
- forms and buttons  
- DOM density  

It sends this snapshot to the background script.

### 2. Background Script  
`background.js` receives structural data and sends RTT beacon events to:

```
/api/rtt/beacon
```

This allows RTT to build a cross‑site structural map.

### 3. Popup UI  
`popup.html` + `popup.js` display the current page’s structure in a simple, readable format.

### 4. Optional: Triadic DOM Inspector  
`triadic-inspector.js` provides a deeper structural analysis of the DOM using triadic decomposition.  
This module can be imported into the popup or used to power a sidebar panel.

---

## Installation (Developer Mode)

1. Open your browser’s extension settings  
2. Enable **Developer Mode**  
3. Click **Load Unpacked**  
4. Select the `rtt-extension/` folder  

The extension will appear in your toolbar.

---

## Next Steps

You can extend this template by adding:

- a sidebar panel for structural clarity  
- RTT metadata detection (`<meta>` tags, `/rtt.json`)  
- drift detection overlays  
- corridor flow visualizers  
- vST‑beta diagnostics tooling  

This template is designed to grow with the RTT ecosystem.
