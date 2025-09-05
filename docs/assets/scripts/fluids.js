(function(){
  function initFluids(container) {
    const canvas = document.createElement("canvas");
    container.appendChild(canvas);
    const ctx = canvas.getContext("2d");

    const lines = 3; // number of stacked wave lines
    const waveHeight = 25; // amplitude
    const speed = 0.02;

    function resize(){
      canvas.width = container.clientWidth;
      canvas.height = container.clientHeight;
    }
    window.addEventListener("resize", resize);
    resize();

    function drawEquation(eq, x, y, size){
      const span = document.createElement("span");
      katex.render(eq, span, { throwOnError: false });
      ctx.font = `${size}px Segoe UI, sans-serif`;
      ctx.fillStyle = "#00BFFF";
      ctx.textAlign = "left";
      ctx.textBaseline = "middle";
      ctx.fillText(span.textContent, x, y);
    }

    function animate(time){
      ctx.clearRect(0,0,canvas.width,canvas.height);
      const eqCount = window.TFT_EQUATIONS.length;
      const spacing = 100;

      for (let l = 0; l < lines; l++) {
        const yBase = (canvas.height / (lines + 1)) * (l + 1);
        for(let i=0;i<eqCount*5;i++){
          const eq = window.TFT_EQUATIONS[i % eqCount];
          const x = (i*spacing - (time*0.05) % (spacing*eqCount)) % (canvas.width + spacing) - spacing;
          const y = yBase + Math.sin((i + time*speed)/10) * waveHeight;
          drawEquation(eq, x, y, 12);
        }
      }
      requestAnimationFrame(animate);
    }
    requestAnimationFrame(animate);
  }

  document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".fluids-animation").forEach(initFluids);
  });
})();
