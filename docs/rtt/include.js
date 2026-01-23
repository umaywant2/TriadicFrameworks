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
</script>
