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

// Auto-rotate with pause-on-hover, pause-on-touch, and resume delay
['papers', 'podcasts'].forEach(sectionId => {
  const carousel = document.querySelector(`#${sectionId}.carousel`);
  if (!carousel) return;

  let intervalId = startAutoScroll();
  let resumeTimeout;

  function startAutoScroll() {
    return setInterval(() => {
      scrollCarousel(sectionId, 1); // move right by 3 items
    }, 6000);
  }

  function stopAutoScroll() {
    clearInterval(intervalId);
    intervalId = null;
  }

  function scheduleResume() {
    clearTimeout(resumeTimeout);
    resumeTimeout = setTimeout(() => {
      if (!intervalId) {
        intervalId = startAutoScroll();
      }
    }, 4000); // 4-second delay before resuming
  }

  // Desktop hover events
  carousel.addEventListener('mouseenter', () => {
    stopAutoScroll();
  });
  carousel.addEventListener('mouseleave', () => {
    scheduleResume();
  });

  // Mobile touch events
  carousel.addEventListener('touchstart', () => {
    stopAutoScroll();
  }, { passive: true });
  carousel.addEventListener('touchend', () => {
    scheduleResume();
  }, { passive: true });
});
