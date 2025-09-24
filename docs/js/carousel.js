// ===== CONFIG =====
const AUTO_SCROLL_INTERVAL = 6000; // ms between auto-scrolls
const RESUME_DELAY = 4000;         // ms to wait before resuming after interaction
const ITEMS_PER_SCROLL = 3;        // how many items to move per scroll
const CAROUSEL_IDS = ['papers', 'podcasts', 'projects', 'labs', 'navigation', 'lattice']; // all carousel section IDs
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

// ===== Unified Auto-Rotation Logic =====
let autoScrollIntervalId = null;
let resumeTimeoutId = null;

function startAutoScrollAll() {
  stopAutoScrollAll(); // prevent duplicates
  autoScrollIntervalId = setInterval(() => {
    CAROUSEL_IDS.forEach(id => scrollCarousel(id, 1));
  }, AUTO_SCROLL_INTERVAL);
}

function stopAutoScrollAll() {
  clearInterval(autoScrollIntervalId);
  autoScrollIntervalId = null;
}

function scheduleResumeAll() {
  clearTimeout(resumeTimeoutId);
  resumeTimeoutId = setTimeout(() => {
    if (!autoScrollIntervalId) {
      startAutoScrollAll();
    }
  }, RESUME_DELAY);
}

// ===== Event Binding =====
CAROUSEL_IDS.forEach(sectionId => {
  const carousel = document.querySelector(`#${sectionId}.carousel`);
  if (!carousel) return;

  // Pause/resume on hover/touch
  carousel.addEventListener('mouseenter', stopAutoScrollAll);
  carousel.addEventListener('mouseleave', scheduleResumeAll);
  carousel.addEventListener('touchstart', stopAutoScrollAll, { passive: true });
  carousel.addEventListener('touchend', scheduleResumeAll, { passive: true });

  // Auto-bind left/right buttons
  const leftBtn = document.querySelector(`#${sectionId}-left`);
  const rightBtn = document.querySelector(`#${sectionId}-right`);
  if (leftBtn) leftBtn.addEventListener('click', () => scrollCarousel(sectionId, -1));
  if (rightBtn) rightBtn.addEventListener('click', () => scrollCarousel(sectionId, 1));
});

// Page Visibility API
document.addEventListener('visibilitychange', () => {
  if (document.hidden) {
    stopAutoScrollAll();
  } else {
    scheduleResumeAll();
  }
});

// Start everything
startAutoScrollAll();
