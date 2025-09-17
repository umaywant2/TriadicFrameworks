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

// Auto-rotate with pause-on-hover
['papers', 'podcasts'].forEach(sectionId => {
  const carousel = document.querySelector(`#${sectionId}.carousel`);
  if (!carousel) return;

  let intervalId = setInterval(() => {
    scrollCarousel(sectionId, 1); // move right by 3 items
  }, 6000);

  carousel.addEventListener('mouseenter', () => {
    clearInterval(intervalId);
  });

  carousel.addEventListener('mouseleave', () => {
    intervalId = setInterval(() => {
      scrollCarousel(sectionId, 1);
    }, 6000);
  });
});

