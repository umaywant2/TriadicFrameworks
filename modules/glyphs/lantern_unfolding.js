function triggerLanternUnfolding(name) {
  const container = document.createElement('div');
  container.id = 'lantern-unfolding';
    position: fixed;
    top: 20%;
    left: 50%;
    transform: translateX(-50%);
    background: #111;
    color: #f5f5f5;
    padding: 20px;
    border: 2px solid #f5f5f5;
    font-family: 'Courier New', monospace;
    z-index: 9999;
    text-align: center;
    animation: fadeIn 2s ease-in-out;
  `;

  container.innerHTML = `
    <h2>🪔 Lantern Unfolding</h2>
    <p>Welcome, <strong>${name}</strong></p>
    <p>Your resonance has been inscribed.</p>
    <p>The glyphic path begins now.</p>
  `;

  document.body.appendChild(container);

  setTimeout(() => {
    container.style.animation = 'fadeOut 2s ease-in-out';
    setTimeout(() => container.remove(), 2000);
  }, 5000);
}

// Optional: CSS animations (can be moved to glyphic.css)
const style = document.createElement('style');
style.innerHTML = `
  @keyframes fadeIn {
    from { opacity: 0; transform: scale(0.9); }
    to { opacity: 1; transform: scale(1); }
  }
  @keyframes fadeOut {
    from { opacity: 1; transform: scale(1); }
    to { opacity: 0; transform: scale(0.9); }
  }
`;
document.head.appendChild(style);
