// fluids.js

const canvas = document.getElementById("fluidsCanvas");
const ctx = canvas.getContext("2d");
canvas.width = canvas.offsetWidth;
canvas.height = canvas.offsetHeight;

let flowSpeed = 1.0;
let charMode = false;
let charSymbol = "*";

const speedInput = document.getElementById("fluidsSpeed");
const charInput = document.getElementById("fluidsChar");

speedInput.addEventListener("input", () => {
  flowSpeed = parseFloat(speedInput.value);
});

charInput.addEventListener("change", () => {
  charMode = charInput.checked;
  charSymbol = charInput.dataset.symbol || "*";
});

let particles = Array.from({ length: 30 }, () => ({
  x: Math.random() * canvas.width,
  y: Math.random() * canvas.height,
  vx: Math.random() * 2 - 1,
  vy: Math.random() * 2 - 1
}));

function drawFluids() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  particles.forEach(p => {
    p.x += p.vx * flowSpeed;
    p.y += p.vy * flowSpeed;

    if (charMode) {
      ctx.font = "16px monospace";
      ctx.fillStyle = "#00ccff";
      ctx.fillText(charSymbol, p.x, p.y);
    } else {
      ctx.beginPath();
      ctx.arc(p.x, p.y, 4, 0, Math.PI * 2);
      ctx.fillStyle = "rgba(0, 200, 255, 0.6)";
      ctx.fill();
      ctx.closePath();
    }

    if (p.x < 0 || p.x > canvas.width) p.vx *= -1;
    if (p.y < 0 || p.y > canvas.height) p.vy *= -1;
  });

  requestAnimationFrame(drawFluids);
}

drawFluids();
