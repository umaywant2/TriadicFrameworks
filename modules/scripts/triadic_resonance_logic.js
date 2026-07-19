// Blade validation function
function validateBlade(bladeId, score, contributor, lineageText) {
  const blade = document.getElementById(bladeId);
  blade.classList.add('validated');

  // Update score and status
  const scoreCell = document.getElementById(`score-${bladeId.split('-')[0]}`);
  const statusCell = document.getElementById(`status-${bladeId.split('-')[0]}`);
  scoreCell.textContent = score;

  let status = "Unstable";
  if (score === 1) status = "Partial Resonance";
  else if (score === 2) status = "Validated";
  else if (score === 3) status = "Mythic Resonance";
  statusCell.textContent = status;

  // Update contributor name
  document.getElementById(`validator-${bladeId.split('-')[0]}`).textContent = contributor;

  // Update lineage echo
  document.getElementById("lineage-info").textContent = lineageText;

  // Check for full resonance
  checkResonance();
}

// Check if all blades are fully validated
function checkResonance() {
  const scores = [
    parseInt(document.getElementById("score-forces").textContent),
    parseInt(document.getElementById("score-fluids").textContent),
    parseInt(document.getElementById("score-frequency").textContent)
  ];

  if (scores.every(score => score === 3)) {
    const glyph = document.getElementById("triadic-glyph");
    glyph.classList.add("spin");

    // Optional: add poetic echo
    const echo = "Triadic Resonance Achieved — All logic pillars aligned.";
    document.getElementById("lineage-info").textContent = echo;
  }
}
