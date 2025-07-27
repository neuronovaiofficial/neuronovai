window.addEventListener('DOMContentLoaded', () => {
  const canvas = document.getElementById("neural-bg");
  const ctx = canvas.getContext("2d");

  let width, height;
  function resize() {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
  }
  window.addEventListener("resize", resize);
  resize();

  const neurons = Array.from({ length: 60 }, () => ({
    x: Math.random() * width,
    y: Math.random() * height,
    vx: (Math.random() - 0.5) * 1.5,
    vy: (Math.random() - 0.5) * 1.5
  }));

  function animate() {
    ctx.clearRect(0, 0, width, height);

    for (let i = 0; i < neurons.length; i++) {
      for (let j = i + 1; j < neurons.length; j++) {
        const dx = neurons[i].x - neurons[j].x;
        const dy = neurons[i].y - neurons[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < 120) {
          ctx.strokeStyle = `rgba(0,255,200,${1 - dist / 120})`;
          ctx.lineWidth = 1;
          ctx.beginPath();
          ctx.moveTo(neurons[i].x, neurons[i].y);
          ctx.lineTo(neurons[j].x, neurons[j].y);
          ctx.stroke();
        }
      }
    }

    for (const n of neurons) {
      n.x += n.vx;
      n.y += n.vy;

      if (n.x < 0 || n.x > width) n.vx *= -1;
      if (n.y < 0 || n.y > height) n.vy *= -1;

      ctx.fillStyle = "#00ffcc";
      ctx.beginPath();
      ctx.arc(n.x, n.y, 2, 0, Math.PI * 2);
      ctx.fill();
    }

    requestAnimationFrame(animate);
  }

  animate();
});
