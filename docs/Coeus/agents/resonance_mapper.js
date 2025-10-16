document.addEventListener("DOMContentLoaded", () => {
  const layers = document.querySelectorAll(".layer");
  layers.forEach(layer => {
    layer.addEventListener("click", () => {
      layer.classList.toggle("active");
      layer.style.boxShadow = layer.classList.contains("active")
        ? "0 0 20px #0ff"
        : "0 0 10px #444";
    });
  });

  // Optional: Hover rail highlight
  const rails = document.querySelectorAll(".rail");
  rails.forEach(rail => {
    rail.addEventListener("mouseenter", () => {
      rail.style.background = "#0ff";
      rail.style.color = "#000";
    });
    rail.addEventListener("mouseleave", () => {
      rail.style.background = "#333";
      rail.style.color = "#eee";
    });
  });
});
