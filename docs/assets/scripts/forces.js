// forces.js

const canvas = document.getElementById("forcesCanvas");
const ctx = canvas.getContext("2d");
canvas.width = canvas.offsetWidth;
canvas.height = canvas.offsetHeight;

let baseSpeed = 1.0;
let charMode = false;
let charSymbol = "@";

const speedInput = document.getElementById("forcesSpeed");
const charInput = document.getElementById("forcesChar");

speedInput.addEventListener("input", () => {
  baseSpeed = parseFloat(speedInput.value);
});

charInput.addEventListener("change", () => {
  charMode = charInput.checked;
  charSymbol = charInput.dataset.symbol || "@";
});

function drawForces() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  const centerX = canvas.width / 2;
  const centerY = canvas.height / 2;
  const radius = 40 + Math.sin(performance.now() / 500) * baseSpeed * 5;

  if (charMode) {
    ctx.font = `${20 + baseSpeed * 5}px monospace`;
    ctx.fillStyle = "#ff6600";
    ctx.textAlign = "center";
    ctx.fillText(charSymbol, centerX, centerY);
  } else {
    ctx.beginPath();
    ctx.arc(centerX, centerY, radius, 0, Math.PI * 2);
    ctx.fillStyle = "rgba(255, 100, 0, 0.6)";
    ctx.shadowColor = "rgba(255, 80, 0, 0.9)";
    ctx.shadowBlur = 20;
    ctx.fill();
    ctx.closePath();
  }

  requestAnimationFrame(drawForces);
}

drawForces();
