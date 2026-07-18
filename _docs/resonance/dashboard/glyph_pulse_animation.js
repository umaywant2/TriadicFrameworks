// 🔮 Glyph Pulse Animation
// Triggers a symbolic pulse when a glyph is activated

function triggerGlyphPulse(glyphName) {
  const pulse = document.createElement('div');
  pulse.className = 'glyph-pulse';
  pulse.innerText = `🔮 ${glyphName} activated`;
  document.body.appendChild(pulse);

  setTimeout(() => {
    pulse.classList.add('active');
  }, 100);

  setTimeout(() => {
    pulse.remove();
  }, 3000);
}

// Example usage:
document.addEventListener('DOMContentLoaded', () => {
  fetch('../../logs/glyph_trigger_log.json')
    .then(res => res.json())
    .then(logs => {
      const latest = logs[logs.length - 1];
      if (latest.animation_status === 'completed') {
        triggerGlyphPulse(latest.glyph);
      }
    });
});

