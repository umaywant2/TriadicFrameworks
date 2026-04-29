function requestStructure() {
  browser.tabs.query({ active: true, currentWindow: true }).then((tabs) => {
    const tabId = tabs[0].id;

    browser.tabs.sendMessage(tabId, { type: "rtt-request-structure" })
      .catch(() => {
        document.getElementById("structure").textContent =
          "Unable to read structure on this page.";
      });
  });
}

browser.runtime.onMessage.addListener((msg) => {
  if (msg.type === "rtt-structure-response") {
    document.getElementById("structure").textContent =
      JSON.stringify(msg.structure, null, 2);
  }
});

requestStructure();

