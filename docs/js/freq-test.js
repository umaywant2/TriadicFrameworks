(function () {
  const CONFIG = {
    BANDS: 3,
    EQUATIONS_PER_LANE: 36,
    LOOP: [3, 1, 6, 3, 9, 6],
    COLORS: ['c1', 'c3', 'c6', 'c9'],
    SPEEDS: ['slow', 'medium', 'fast']
  };

  function getColorClass(position) {
    const cycleLength = CONFIG.LOOP.reduce((a, b) => a + b, 0);
    const cyclePos = position % cycleLength;
    let sum = 0;
    for (let i = 0; i < CONFIG.LOOP.length; i++) {
      sum += CONFIG.LOOP[i];
      if (cyclePos < sum) return CONFIG.COLORS[i];
    }
    return CONFIG.COLORS[0];
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
    lane.style.minWidth = '220%';

    equations.concat(equations).forEach((eq, i) => {
      lane.appendChild(makeEquation(eq, i));
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

    const speedClass = CONFIG.SPEEDS[index % CONFIG.SPEEDS.length];
    const laneLTR = buildLane(equations, speedClass, true);
    const laneRTL = buildLane(equations, speedClass, false);

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
  }

  function initFreqTest() {
    const container = document.querySelector('.freq-test-zone');
    if (container) mount(container);
    console.log('[TFT] Frequencies test initialized');
  }

  window.initFreqTest = initFreqTest;
  window.addEventListener('load', initFreqTest);
})();
