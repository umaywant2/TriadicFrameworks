// Lattice entrypoint: controls mount mode and init order.
// Forces must apply last in overlay mode.

(function () {
  // Single source of truth for mode
  window.FFF_CONFIG = window.FFF_CONFIG || {
    TEST_MODE: true // true = render in test areas; false = overlay into #lattice-container
  };

  function initLattice() {
    if (window.FFF_CONFIG.TEST_MODE) {
      // Test each independently in its own area
      window.initFrequencies && window.initFrequencies();
      window.initFluids && window.initFluids();
      window.initForces && window.initForces();
    } else {
      // Overlay: strict order and z-index handles stacking
      window.initFrequencies && window.initFrequencies();
      window.initFluids && window.initFluids();
      // Force last visually and temporally
      setTimeout(() => window.initForces && window.initForces(), 100);
    }
  }

  // Public toggles for quick verify
  window.enableFFFLatticeOverlay = function () {
    window.FFF_CONFIG.TEST_MODE = false;
    remount();
  };

  window.enableFFFTestMode = function () {
    window.FFF_CONFIG.TEST_MODE = true;
    remount();
  };

  function clearMounts() {
    // Clear test areas
    document.querySelectorAll('.frequencies-animation, .fluids-animation, .forces-animation')
      .forEach(el => (el.innerHTML = ''));
    // Clear lattice overlay
    const lattice = document.getElementById('lattice-container');
    if (lattice) lattice.innerHTML = '';
  }

  function remount() {
    clearMounts();
    initLattice();
  }

  window.addEventListener('load', initLattice);
})();
