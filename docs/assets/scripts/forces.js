(function(){
  const TFT_EQUATIONS = [
    "F = -\\frac{\\pi^2 \\hbar c}{240 d^4}",
    "\\rho_0 = \\frac{\\hbar \\omega^2}{V}",
    "\\tau = \\frac{dR}{d\\phi}",
    "\\Psi(x,t) = A e^{i(kx - \\omega t)}",
    "\\Phi = \\int_0^{\\infty} S(\\lambda) R(\\lambda)\\, d\\lambda",
    "E = m R^2 \\phi^2",
    "X(\\omega) = \\int_{-\\infty}^{\\infty} x(t) e^{-i\\omega t} dt"
  ];

  function initForces(container) {
    const canvas = document.createElement("canvas");
    container.appendChild(canvas);
    const ctx = canvas.getContext("2d");

    function resize(){
      canvas.width = container.clientWidth;
      canvas.height = container.clientHeight;
    }
    window.addEventListener("resize", resize);
    resize();

    const centerEq = TFT_EQUATIONS[0];
    const orbits = [
      { eq: TFT_EQUATIONS[1], radius: 40, angle: 0, speed: 0.01 },
      { eq: TFT_EQUATIONS[2], radius: 70, angle: 1, speed: 0.008 },
      { eq: TFT_EQUATIONS[3], radius: 100, angle: 2, speed: 0.006 }
    ];

    function drawText(eq, x, y, size){
      ctx.font = `${size}px Segoe UI, sans-serif`;
      ctx.fillStyle = "#FFCB05";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText(eq, x, y);
    }

    function animate(){
      ctx.clearRect(0,0,canvas.width,canvas.height);
      const cx = canvas.width/2;
      const cy = canvas.height/2;

      ctx.save();
      ctx.translate(cx, cy);
      ctx.rotate(Date.now()/1000);
      drawText(centerEq, 0, 0, 16);
      ctx.restore();

      orbits.forEach(o=>{
        o.angle += o.speed;
        const ox = cx + Math.cos(o.angle) * o.radius;
        const oy = cy + Math.sin(o.angle) * o.radius;
        drawText(o.eq, ox, oy, 12);
      });

      requestAnimationFrame(animate);
    }
    animate();
  }

  document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".forces-animation").forEach(initForces);
  });
})();
