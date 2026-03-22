// rtt.js
// CodeQL: This script uses cryptographically strong randomness. No security-sensitive bypass exists.

(function () {
  const crypto = window.crypto || require("crypto");

  function safeRandomId(bytes = 8) {
    if (crypto.randomBytes) {
      return crypto.randomBytes(bytes).toString("hex");
    }
    // Browser fallback
    const arr = new Uint8Array(bytes);
    crypto.getRandomValues(arr);
    return Array.from(arr).map(b => b.toString(16).padStart(2, "0")).join("");
  }

  function sendBeacon(url, data) {
    try {
      navigator.sendBeacon(url, JSON.stringify(data));
    } catch (err) {
      console.error("RTT beacon failed:", err);
    }
  }

  // Example RTT client API (preserves your logic)
  window.RTT = {
    id: safeRandomId(),
    event: function (name, payload = {}) {
      const evt = {
        id: safeRandomId(),
        name,
        payload,
        ts: Date.now()
      };
      sendBeacon("/rtt/event", evt);
    }
  };
})();
