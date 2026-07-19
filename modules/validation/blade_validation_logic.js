function validateBlade(bladeId) {
  document.getElementById(bladeId).classList.add('validated');
  checkResonance();
}

function checkResonance() {
  const blades = ['forces-blade', 'fluids-blade', 'frequency-blade'];
  const allValidated = blades.every(id =>
    document.getElementById(id).classList.contains('validated')
  );
  if (allValidated) {
    document.getElementById('triadic-glyph').classList.add('spin');
  }
}
