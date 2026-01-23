<script>
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-include]").forEach(async el => {
    const file = el.getAttribute("data-include");
    const resp = await fetch(file);
    el.innerHTML = await resp.text();
  });
});
</script>
