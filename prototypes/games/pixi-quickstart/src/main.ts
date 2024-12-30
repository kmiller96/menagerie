import { Application, Assets, Sprite } from "pixi.js";

(async () => {
  // Create a new application
  const app = new Application();

  // Initialize the application
  await app.init({ background: "#1099bb", resizeTo: window });

  // Append the application canvas to the document body
  document.getElementById("pixi-container")!.appendChild(app.canvas);

  // Load the bunny texture
  const texture = await Assets.load("/assets/bunny.png");

  // Create a bunny Sprite
  const bunny = new Sprite(texture);

  // Center the sprite's anchor point
  bunny.anchor.set(0.5);

  // Move the sprite to the center of the screen
  bunny.position.set(app.screen.width / 2, app.screen.height / 2);

  // Add the bunny to the stage
  app.stage.addChild(bunny);

  // Listen for animate update
  let vx = 0;
  let vy = 0;

  onkeydown = (e) => {
    if (["ArrowRight", "d"].includes(e.key)) {
      vx = 10;
    }
    if (["ArrowLeft", "a"].includes(e.key)) {
      vx = -10;
    }
    if (["ArrowUp", "w"].includes(e.key)) {
      vy = -10;
    }
    if (["ArrowDown", "s"].includes(e.key)) {
      vy = 10;
    }
  };

  onkeyup = (e) => {
    if (["ArrowRight", "ArrowLeft", "d", "a"].includes(e.key)) {
      vx = 0;
    }
    if (["ArrowUp", "ArrowDown", "w", "s"].includes(e.key)) {
      vy = 0;
    }
  };

  app.ticker.add((time) => {
    bunny.x += vx;
    bunny.y += vy;

    bunny.rotation += 0.1 * time.deltaTime;
  });
})();
