(function () {
  const CONFIG = {
    TEST_MODE: window.FFF_CONFIG?.TEST_MODE ?? true,
    BANDS: 3,
    EQUATIONS_PER_LANE: 36,
    SCROLL_DURATION: [22, 16, 11], // seconds per lane
    COLORS: {
      base: 'c1',
      after3: 'c3',
      after6: 'c6',
      after9: 'c9',
    }
  };

  function getColorClass(position) {
    // Harmonic cadence: base → 3 → 6 → 9
    if (position >= 9) return CONFIG.COLORS.after9;
    if (position >= 6) return CONFIG.COLORS.after6;
    if (position >= 3) return CONFIG.COLORS.after3;
    return CONFIG.COLORS.base;
  }

  function makeEquation(label, position) {
    const span = document.createElement('span');
    span.className = `eq-chip ${getColorClass(position)}`;
    try {
      if (window.katex) {
        span.innerHTML = window.katex.renderToString(label, { throwOnError: false });
      } else {
        span.textContent = label;
      }
    } catch {
      span.textContent = label;
    }
    return span;
  }

  function buildLane(equations, speed, reverse = false) {
    const lane = document.createElement('div');
    lane.className = `freq-lane ${speed}`;
    lane.style.animationDirection = reverse ? 'reverse' : 'normal';
    lane.style.direction = reverse ? 'ltr' : 'rtl';
    lane.style.minWidth = '220%'; // ensures full scroll span

    // Duplicate for seamless scroll
    const doubled = equations.concat(equations);
    doubled.forEach((eq, i) => {
      const chip = makeEquation(eq, i % CONFIG.EQUATIONS_PER_LANE);
      lane.appendChild(chip);
    });

    return lane;
  }

  function buildBand(index) {
    const band = document.createElement('div');
    band.className = 'freq-band';

    const phase = index + 1;
    const equations = Array.from({ length: CONFIG.EQUATIONS_PER_LANE }, (_, i) => {
      const n = i + 1;
      return String.raw`\sin(${phase}t) + \frac{${n}}{${phase}}`;
    });

    const speedClass = ['slow', 'medium', 'fast'][index % 3];
    const laneLTR = buildLane(equations, speedClass, true);  // left-to-right
    const laneRTL = buildLane(equations, speedClass, false); // right-to-left

    band.appendChild(laneLTR);
    band.appendChild(laneRTL);
    return band;
  }

  function mount(container) {
    const root = document.createElement('div');
    root.className = 'overlay-layer overlay-frequencies';

    for (let i = 0; i < CONFIG.BANDS; i++) {
      root.appendChild(buildBand(i));
    }

    container.appendChild(root);
    return root;
  }

  function initFrequencies() {
    const targets = [];
    if (CONFIG.TEST_MODE) {
      document.querySelectorAll('.frequencies-animation').forEach(el => targets.push(el));
    } else {
      const lattice = document.getElementById('lattice-container');
      if (lattice) targets.push(lattice);
    }
    targets.forEach(mount);
    console.log('[FFF] Frequencies initialized', { test: CONFIG.TEST_MODE });
  }

  window.initFrequencies = initFrequencies;
})();
