function scrollCarousel(id, direction) {
  const container = document.getElementById(id);
  container.scrollBy({ left: direction * 300, behavior: 'smooth' });
}
function toggleTheme() {
  document.body.classList.toggle('dark-mode');
}
