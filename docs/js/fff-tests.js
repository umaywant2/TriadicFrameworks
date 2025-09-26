document.addEventListener("DOMContentLoaded", () => {
  const modules = [
    { id: "frequency-test", init: initFrequencyTest },
    { id: "fluids-test", init: initFluidsTest },
    { id: "forces-test", init: initForcesTest }
  ];

  modules.forEach(({ id, init }) => {
    const container = document.getElementById(id);
    if (container) {
      try {
        init(container);
      } catch (err) {
        console.error(`Error loading ${id}:`, err);
        container.innerHTML = `<p>⚠️ Failed to load ${id}</p>`;
      }
    } else {
      console.warn(`Missing container: ${id}`);
    }
  });
});
