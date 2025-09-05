// frequencies.js

const canvas = document.getElementById("frequenciesCanvas");
const ctx = canvas.getContext("2d");
canvas.width = canvas.offsetWidth;
canvas.height = canvas.offsetHeight;

let freqSpeed = 60;
let charMode = false;
let charSymbol = "_";

const speedInput = document.getElementById("frequenciesSpeed");
const charInput = document.getElementById("frequenciesChar");

speedInput.addEventListener("input", () => {
  freqSpeed = parseFloat(speedInput.value);
});

charInput.addEventListener("change", () => {
  charMode = charInput.checked;
  charSymbol = charInput.dataset.symbol || "_";
});

let waves = Array.from({ length: 20 }, () => ({
  x: Math.random() * canvas.width,
  y: Math.random() * canvas.height,
  dir: Math.random() > 0.5 ? 1 : -1
}));

function drawFrequencies() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  const dt = 0.016;

  waves.forEach(w => {
    w.x += w.dir * freqSpeed * dt;

    if (charMode) {
      ctx.font = "14px monospace";
      ctx.fillStyle = "#cc00ff";
      ctx.fillText(charSymbol, w.x, w.y);
    } else {
      ctx.beginPath();
      ctx.arc(w.x, w.y, 3, 0, Math.PI * 2);
      ctx.fillStyle = "rgba(200, 0, 255, 0.6)";
      ctx.fill();
      ctx.closePath();
    }

    if (w.x < 0 || w.x > canvas.width) w.dir *= -1;
  });

  requestAnimationFrame(drawFrequencies);
}

drawFrequencies();
