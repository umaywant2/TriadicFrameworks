async function sendBeacon(structure) {
  const payload = {
    site: "browser-extension",
    session: "ext-" + Date.now(),
    event: "page_inspect",
    ts: new Date().toISOString(),
    structure
  };

  try {
    await fetch("https://www.triadicframeworks.org/api/rtt/beacon", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
  } catch (e) {
    console.warn("[RTT] Beacon failed:", e);
  }
}

browser.runtime.onMessage.addListener((msg) => {
  if (msg.type === "rtt-structure") {
    sendBeacon(msg.structure);
  }
});

