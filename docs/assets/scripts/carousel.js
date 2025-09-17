function scrollCarousel(sectionId, direction) {
  const carousel = document.querySelector(`#${sectionId}.carousel`);
  if (!carousel) return;

  const itemWidth = carousel.querySelector('.carousel-item').offsetWidth;
  const scrollAmount = itemWidth * 3;

  if (direction > 0 && carousel.scrollLeft + carousel.offsetWidth >= carousel.scrollWidth) {
    carousel.scrollTo({ left: 0, behavior: 'smooth' });
  } else if (direction < 0 && carousel.scrollLeft === 0) {
    carousel.scrollTo({ left: carousel.scrollWidth, behavior: 'smooth' });
  } else {
    carousel.scrollBy({ left: direction * scrollAmount, behavior: 'smooth' });
  }
}

function toggleTheme() {
  document.body.classList.toggle('dark-mode');
}

// Auto-rotate with pause-on-hover and pause-on-touch
['papers', 'podcasts'].forEach(sectionId => {
  const carousel = document.querySelector(`#${sectionId}.carousel`);
  if (!carousel) return;

  let intervalId = startAutoScroll();

  function startAutoScroll() {
    return setInterval(() => {
      scrollCarousel(sectionId, 1); // move right by 3 items
    }, 6000);
  }

  function stopAutoScroll() {
    clearInterval(intervalId);
  }

  // Desktop hover events
  carousel.addEventListener('mouseenter', stopAutoScroll);
  carousel.addEventListener('mouseleave', () => {
    intervalId = startAutoScroll();
  });

  // Mobile touch events
  carousel.addEventListener('touchstart', stopAutoScroll, { passive: true });
  carousel.addEventListener('touchend', () => {
    intervalId = startAutoScroll();
  }, { passive: true });
});
