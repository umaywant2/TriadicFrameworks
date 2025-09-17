function scrollCarousel(sectionId, direction) {
  const carousel = document.querySelector(`#${sectionId}.carousel`);
  if (!carousel) return;

  const itemWidth = carousel.querySelector('.carousel-item').offsetWidth;
  const scrollAmount = itemWidth * 3; // move 3 items at a time

  carousel.scrollBy({
    left: direction * scrollAmount,
    behavior: 'smooth'
  });
}

function toggleTheme() {
  document.body.classList.toggle('dark-mode');
}
