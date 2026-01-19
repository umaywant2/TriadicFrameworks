// # 📦 **Triadic DOM Inspector Module**  
// *A drop‑in module for RTT‑Inside browser extensions.*
// 
// This module performs a **triadic decomposition** of the DOM — grouping elements into three structural layers:
// 
// 1. **Frame** (navigation, layout, scaffolding)  
// 2. **Content** (primary information regions)  
// 3. **Controls** (interactive elements)  
// 
// It’s intentionally simple, stable, and substrate‑agnostic.


// # 📄 **triadic-inspector.js**
// triadic-inspector.js — triadic DOM inspector (beta)
//
// Provides a structural decomposition of the DOM into:
// 1. Frame    — nav, header, footer, layout containers
// 2. Content  — main content regions
// 3. Controls — forms, buttons, inputs, interactive elements
//
// This module is safe to import into popup.js, background.js, or a sidebar panel.

export function inspectTriadicDOM() {
  return {
    frame: collectFrameElements(),
    content: collectContentElements(),
    controls: collectControlElements(),
    summary: buildSummary()
  };
}

function collectFrameElements() {
  return Array.from(
    document.querySelectorAll("header, nav, footer, aside, [role='navigation']")
  ).map(el => describe(el));
}

function collectContentElements() {
  return Array.from(
    document.querySelectorAll("main, article, section, [role='main']")
  ).map(el => describe(el));
}

function collectControlElements() {
  return Array.from(
    document.querySelectorAll("button, input, select, textarea, [role='button']")
  ).map(el => describe(el));
}

function describe(el) {
  return {
    tag: el.tagName.toLowerCase(),
    id: el.id || null,
    classes: el.className ? el.className.split(/\s+/) : [],
    text_preview: el.textContent.trim().slice(0, 60)
  };
}

function buildSummary() {
  return {
    frame_count: document.querySelectorAll("header, nav, footer, aside").length,
    content_count: document.querySelectorAll("main, article, section").length,
    control_count: document.querySelectorAll("button, input, select, textarea").length,
    dom_nodes: document.getElementsByTagName("*").length
  };
}

// # 🔌 **How to Use the Triadic Inspector in the Extension**
// 
// ### In `popup.js`:


import { inspectTriadicDOM } from "./triadic-inspector.js";

browser.tabs.query({ active: true, currentWindow: true }).then((tabs) => {
  browser.tabs.sendMessage(tabs[0].id, { type: "rtt-request-triadic" });
});

browser.runtime.onMessage.addListener((msg) => {
  if (msg.type === "rtt-triadic-response") {
    document.getElementById("structure").textContent =
      JSON.stringify(msg.triadic, null, 2);
  }
});


// ### In `content.js`:

import { inspectTriadicDOM } from "./triadic-inspector.js";

browser.runtime.onMessage.addListener((msg) => {
  if (msg.type === "rtt-request-triadic") {
    browser.runtime.sendMessage({
      type: "rtt-triadic-response",
      triadic: inspectTriadicDOM()
    });
  }
});

// This gives the popup (or sidebar) a full triadic decomposition of the current page.
