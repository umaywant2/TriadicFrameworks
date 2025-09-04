(function(){
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

    const centerEq = window.TFT_EQUATIONS[0];
    const orbits = [
      { eq: window.TFT_EQUATIONS[1], radius: 40, angle: 0, speed: 0.01 },
      { eq: window.TFT_EQUATIONS[2], radius: 70, angle: 1, speed: 0.008 },
      { eq: window.TFT_EQUATIONS[3], radius: 100, angle: 2, speed: 0.006 }
    ];

    function drawEquation(eq, x, y, size){
      const span = document.createElement("span");
      katex.render(eq, span, { throwOnError: false });
      ctx.font = `${size}px Segoe UI, sans-serif`;
      ctx.fillStyle = "#FFCB05";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText(span.textContent, x, y);
    }

    function animate(){
      ctx.clearRect(0,0,canvas.width,canvas.height);
      const cx = canvas.width/2;
      const cy = canvas.height/2;

      ctx.save();
      ctx.translate(cx, cy);
      ctx.rotate(Date.now()/1000);
      drawEquation(centerEq, 0, 0, 16);
      ctx.restore();

      orbits.forEach(o=>{
        o.angle += o.speed;
        const ox = cx + Math.cos(o.angle) * o.radius;
        const oy = cy + Math.sin(o.angle) * o.radius;
        drawEquation(o.eq, ox, oy, 12);
      });

      requestAnimationFrame(animate);
    }
    animate();
  }

  document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".forces-animation").forEach(initForces);
  });
})();
