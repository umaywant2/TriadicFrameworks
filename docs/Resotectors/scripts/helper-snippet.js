(function () {
  "use strict";
  const PROJECT = document.title.split("–")[0] || "Project"; // infer from <title>

  function ready(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn, { once: true });
  }

  function createOverlay() {
    const overlay = document.createElement("div");
    overlay.id = "helper-overlay";
    overlay.innerHTML = `
      <div class="helper-content">
        <h2>${PROJECT} — Quick Help</h2>
        <ul>
          <li><strong>Theme toggle:</strong> Click the 🌗 icon or press <kbd>T</kbd></li>
          <li><strong>Smooth scroll:</strong> Click any in‑page link</li>
          <li><strong>Last visited:</strong> Nav remembers your last click</li>
          <li><strong>Need more?</strong> Check README.md & overview.md</li>
        </ul>
        <p>Press <kbd>?</kbd> again or <kbd>Esc</kbd> to close</p>
      </div>
    `;
    document.body.appendChild(overlay);
    styleOverlay(overlay);
    return overlay;
  }

  function styleOverlay(el) {
    Object.assign(el.style, {
      position: "fixed",
      top: 0, left: 0, right: 0, bottom: 0,
      backgroundColor: "rgba(0,0,0,0.85)",
      color: "#fff",
      zIndex: 9999,
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      padding: "2rem",
      fontFamily: "sans-serif",
    });
    const inner = el.querySelector(".helper-content");
    Object.assign(inner.style, {
      maxWidth: "500px",
      backgroundColor: "#222",
      padding: "1.5rem",
      borderRadius: "8px",
    });
    inner.querySelectorAll("kbd").forEach(k => {
      Object.assign(k.style, {
        backgroundColor: "#444",
        padding: "0.2rem 0.4rem",
        borderRadius: "4px",
        fontSize: "0.85em",
      });
    });
  }

  function toggleOverlay() {
    let overlay = document.getElementById("helper-overlay");
    if (overlay) {
      overlay.remove();
    } else {
      overlay = createOverlay();
      overlay.addEventListener("click", () => overlay.remove());
    }
  }

  ready(() => {
    document.addEventListener("keydown", (e) => {
      if (e.key === "?") {
        e.preventDefault();
        toggleOverlay();
      } else if (e.key === "Escape") {
        const overlay = document.getElementById("helper-overlay");
        if (overlay) overlay.remove();
      }
    });
    console.info(`[${PROJECT}] helper snippet loaded — press "?" for help`);
  });
})();
