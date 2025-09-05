// forces.js

// Canvas setup
const canvas = document.getElementById("forcesCanvas");
const ctx = canvas.getContext("2d");
canvas.width = canvas.offsetWidth;
canvas.height = canvas.offsetHeight;

// Glow + ripple control
let glowEnabled = true;
let rippleIntensity = 1.0; // Range: 0.5 (subtle) to 2.0 (strong)

// Draw loop
function drawForces() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Simulated gravitational sphere
  const centerX = canvas.width / 2;
  const centerY = canvas.height / 2;
  const radius = 40;

  // Ripple distortion
  const time = performance.now() / 1000;
  const ripple = Math.sin(time * 2) * rippleIntensity;

  // Apply ripple to radius
  const distortedRadius = radius + ripple * 5;

  // Draw glowing sphere
  ctx.beginPath();
  ctx.arc(centerX, centerY, distortedRadius, 0, Math.PI * 2);
  ctx.fillStyle = "rgba(255, 100, 0, 0.6)";
  ctx.shadowColor = glowEnabled ? "rgba(255, 80, 0, 0.9)" : "transparent";
  ctx.shadowBlur = glowEnabled ? 20 : 0;
  ctx.fill();
  ctx.closePath();

  requestAnimationFrame(drawForces);
}

// Start animation
drawForces();
