<script>
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-include]").forEach(async el => {
    const file = el.getAttribute("data-include");
    const resp = await fetch(file);
    el.innerHTML = await resp.text();
  });

  setTimeout(() => {
    const toggle = document.getElementById("navToggle");
    const drawer = document.getElementById("navDrawer");
    if (toggle && drawer) {
      toggle.addEventListener("click", () => {
        drawer.classList.toggle("open");
      });
    }
  }, 50);
});

const pages = [
  "index.html",
  "products.html",
  "docs.html",
  "developer-zone.html",
  "canon.html",
  "licensing.html",
  "about.html",
  "coeus.html",
  "wrapped-core-l3.html",
  "multi-helix.html",
  "rtof.html"
];

document.addEventListener("input", e => {
  if (e.target.id === "rttSearch") {
    const q = e.target.value.toLowerCase();
    const results = pages.filter(p => p.includes(q));
    const box = document.getElementById("rttSearchResults");
    box.innerHTML = results.map(r => `<div><a href="${r}">${r}</a></div>`).join("");
    box.style.display = results.length ? "block" : "none";
  }
});

setTimeout(() => {
  const toggle = document.getElementById("navToggle");
  const drawer = document.getElementById("navDrawer");
  if (toggle && drawer) {
    toggle.addEventListener("click", () => {
      drawer.classList.toggle("open");
    });
  }
}, 50);

</script>

function renderTierGraph(nodes, edges) {
  const container = document.getElementById("tierGraph");
  const w = container.clientWidth;
  const h = container.clientHeight;
  const cx = w / 2;
  const cy = h / 2;

  const rings = {
    foundations: w * 0.15,
    systems: w * 0.25,
    intelligence: w * 0.35,
    aeonic: w * 0.45
  };

  const tierGroups = {
    foundations: [],
    systems: [],
    intelligence: [],
    aeonic: []
  };

  nodes.forEach(n => tierGroups[n.tier || "foundations"].push(n));

  Object.entries(tierGroups).forEach(([tier, group]) => {
    const r = rings[tier];
    group.forEach((n, i) => {
      const angle = (i / group.length) * Math.PI * 2;
      n.x = cx + r * Math.cos(angle);
      n.y = cy + r * Math.sin(angle);
    });
  });

  // Draw edges + nodes (same as mandala)
}

