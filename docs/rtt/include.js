<script>
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-include]").forEach(async el => {
    const file = el.getAttribute("data-include");
    const resp = await fetch(file);
    el.innerHTML = await resp.text();
  });

  const toggle = () => {
    document.body.classList.toggle("light-mode");
    document.body.classList.toggle("dark-mode");
  };

  setTimeout(() => {
    const btn = document.getElementById("themeToggle");
    if (btn) btn.addEventListener("click", toggle);
  }, 50);
});
</script>
