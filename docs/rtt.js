// rtt.js  —  triadicframeworks RTT hook (beta)
//
// usage:
// <script src="https://www.triadicframeworks.org/rtt.js" data-site="example.com"></script>
//
// goals (vST-ready shape, low friction now):
// - register the site with RTT
// - send lightweight structural/beacon data
// - expose a tiny client API for future features
// - never break the page if RTT is offline

(function () {
  const RTT_ENDPOINT = "https://www.triadicframeworks.org/api/rtt";
  const SCRIPT_TAG = document.currentScript || (function () {
    const scripts = document.getElementsByTagName("script");
    return scripts[scripts.length - 1];
  })();

  const SITE_ID =
    (SCRIPT_TAG && SCRIPT_TAG.getAttribute("data-site")) ||
    window.location.hostname ||
    "unknown-site";

  const SESSION_ID = (() => {
    try {
      const key = "rtt_session_id";
      let id = sessionStorage.getItem(key);
      if (!id) {
        id = "rtt-" + Math.random().toString(36).slice(2) + Date.now().toString(36);
        sessionStorage.setItem(key, id);
      }
      return id;
    } catch (e) {
      return "rtt-" + Math.random().toString(36).slice(2);
    }
  })();

  function safeFetch(url, options) {
    if (!("fetch" in window)) return;
    try {
      fetch(url, options).catch(() => {});
    } catch (e) {}
  }

  function collectBasicStructure() {
    const nav = document.querySelectorAll("nav, header, footer").length;
    const main = document.querySelectorAll("main, [role='main']").length;
    const forms = document.querySelectorAll("form").length;
    const buttons = document.querySelectorAll("button, [role='button']").length;

    return {
      url: window.location.href,
      title: document.title || "",
      nav_count: nav,
      main_count: main,
      form_count: forms,
      button_count: buttons,
      dom_nodes: document.getElementsByTagName("*").length
    };
  }

  function sendBeacon(eventType) {
    const payload = {
      site: SITE_ID,
      session: SESSION_ID,
      event: eventType,
      ts: new Date().toISOString(),
      structure: collectBasicStructure()
    };

    safeFetch(RTT_ENDPOINT + "/beacon", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
      keepalive: true
    });
  }

  // public API (minimal, vST-ready shape)
  const RTT = {
    site: SITE_ID,
    session: SESSION_ID,
    version: "0.1-beta",
    ping: function (label) {
      sendBeacon(label || "manual_ping");
    },
    getStructureSnapshot: function () {
      return collectBasicStructure();
    }
  };

  // expose globally in a non-invasive way
  if (!window.RTT) {
    window.RTT = RTT;
  }

  // initial auto-beacon
  if (document.readyState === "complete" || document.readyState === "interactive") {
    sendBeacon("page_load");
  } else {
    document.addEventListener("DOMContentLoaded", function () {
      sendBeacon("page_load");
    });
  }

  // optional: visibility-based pings (lightweight)
  document.addEventListener("visibilitychange", function () {
    if (document.visibilityState === "hidden") {
      sendBeacon("page_hidden");
    } else if (document.visibilityState === "visible") {
      sendBeacon("page_visible");
    }
  });
})();
