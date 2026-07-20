document.addEventListener("DOMContentLoaded", () => {
  const rails = document.querySelectorAll(".rail");

  rails.forEach(rail => {
    rail.addEventListener("click", () => {
      rail.classList.toggle("scanned");
      rail.style.background = rail.classList.contains("scanned") ? "#0f0" : "#333";
      rail.style.boxShadow = rail.classList.contains("scanned") ? "0 0 15px #0f0" : "0 0 5px #555";
    });
  });

  // Optional: Auto-scan sequence
  let index = 0;
  function autoScan() {
    if (index < rails.length) {
      rails[index].click();
      index++;
      setTimeout(autoScan, 500);
    }
  }

  // Start auto-scan on load
  autoScan();
});

// To activate, link it in resonance_mapper.html:
// ```html
// <script src="emitter_overlay.js"></script>
