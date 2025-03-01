import { Application, Assets, Sprite } from "pixi.js";

type Velocity = { x: number; y: number };

(async () => {
  // Create application
  const app = new Application();
  await app.init({ background: "#1099bb", resizeTo: window });

  // Add to document body
  document.getElementById("pixi-container")!.appendChild(app.canvas);

  // Load bunny
  const texture = await Assets.load("/assets/bunny.png");
  const bunny = new Sprite(texture);

  // Position bunny
  bunny.anchor.set(0.5);
  bunny.position.set(app.screen.width / 2, app.screen.height / 2);

  // Add the bunny to the stage
  app.stage.addChild(bunny);

  // Add event listeners
  const v = { x: 0, y: 0 } as Velocity;
  window.onkeydown = (e) => {
    switch (e.key) {
      case "ArrowUp":
        v.y = -10;
        break;
      case "ArrowDown":
        v.y = +10;
        break;
      case "ArrowLeft":
        v.x = -10;
        break;
      case "ArrowRight":
        v.x = +10;
        break;
    }
  };

  window.onkeyup = (e) => {
    switch (e.key) {
      case "ArrowUp":
      case "ArrowDown":
        v.y = 0;
        break;
      case "ArrowLeft":
      case "ArrowRight":
        v.x = 0;
        break;
    }
  };

  // Animate
  app.ticker.add((time) => {
    bunny.position.x += v.x;
    bunny.position.y += v.y;
  });
})();
