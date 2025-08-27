
#### docs/Hippocampus/scripts/init.js
```javascript
(function () {
  "use strict";
  const PROJECT = "Hippocampus";
  const KEYS = {
    theme: `${PROJECT}:theme`,
    lastNav: `${PROJECT}:lastNav`,
  };

  function ready(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn, { once: true });
  }

  function applyTheme(theme) {
    document.body.setAttribute("data-theme", theme);
  }

  function initTheme() {
    try {
      const stored = localStorage.getItem(KEYS.theme);
      let theme = stored || (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
      applyTheme(theme);
      const toggle = document.getElementById("theme-toggle");
      if (toggle) {
        toggle.addEventListener("click", () => {
          theme = theme === "dark" ? "light" : "dark";
          localStorage.setItem(KEYS.theme, theme);
          applyTheme(theme);
        });
      }
    } catch (_) {}
  }

  function initNavHighlight() {
    const nav = document.querySelector("nav");
    if (!nav) return;
    const links = Array.from(nav.querySelectorAll("a[href]"));
    try {
      const stored = localStorage.getItem(KEYS.lastNav);
      if (stored) links.forEach((l) => l.getAttribute("href") === stored && l.classList.add("active"));
    } catch (_) {}
    links.forEach((link) => {
      link.addEventListener("click", () => {
        links.forEach((l) => l.classList.remove("active"));
        link.classList.add("active");
        try {
          localStorage.setItem(KEYS.lastNav, link.getAttribute("href") || "");
        } catch (_) {}
      });
    });
  }

  function initSmoothScroll() {
    const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (reduce) return;
    document.querySelectorAll('a[href^="#"]').forEach((a) => {
      a.addEventListener("click", (e) => {
        const id = a.getAttribute("href").slice(1);
        const target = document.getElementById(id);
        if (target) {
          e.preventDefault();
          target.scrollIntoView({ behavior: "smooth" });
        }
      });
    });
  }

  function initA11yFocus() {
    function onFirstTab(e) {
      if (e.key === "Tab") {
        document.body.classList.add("user-is-tabbing");
        window.removeEventListener("keydown", onFirstTab);
      }
    }
    window.addEventListener("keydown", onFirstTab);
  }

  ready(() => {
    console.info(`[${PROJECT}] initialized`);
    initTheme();
    initNavHighlight();
    initSmoothScroll();
    initA11yFocus();
  });
})();
