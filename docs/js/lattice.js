function initLattice() {
  initFrequencies(); // First
  initFluids();      // Second
  setTimeout(() => {
    initForces();    // Last, after slight delay
  }, 500); // Delay ensures overlay order
}
window.onload = initLattice;
