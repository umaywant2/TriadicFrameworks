// ===== CONFIG =====
const AUTO_SCROLL_INTERVAL = 6000; // ms between auto-scrolls
const RESUME_DELAY = 4000;         // ms to wait before resuming after interaction
const ITEMS_PER_SCROLL = 3;        // how many items to move per scroll
// ==================

function scrollCarousel(sectionId, direction) {
  const carousel = document.querySelector(`#${sectionId}.carousel`);
  if (!carousel) return;

  const itemWidth = carousel.querySelector('.carousel-item').offsetWidth;
  const scrollAmount = itemWidth * ITEMS_PER_SCROLL;

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

// Auto-rotate with pause-on-hover, pause-on-touch, resume delay, and Page Visibility API
['papers', 'podcasts'].forEach(sectionId => {
  const carousel = document.querySelector(`#${sectionId}.carousel`);
  if (!carousel) return;

  let intervalId = startAutoScroll();
  let resumeTimeout;

  function startAutoScroll() {
    return setInterval(() => {
      scrollCarousel(sectionId, 1); // move right
    }, AUTO_SCROLL_INTERVAL);
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
    }, RESUME_DELAY);
  }

  // Desktop hover events
  carousel.addEventListener('mouseenter', stopAutoScroll);
  carousel.addEventListener('mouseleave', scheduleResume);

  // Mobile touch events
  carousel.addEventListener('touchstart', stopAutoScroll, { passive: true });
  carousel.addEventListener('touchend', scheduleResume, { passive: true });

  // Page Visibility API
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
      stopAutoScroll();
    } else {
      scheduleResume();
    }
  });
});
