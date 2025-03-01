import { Application, Assets, Sprite } from "pixi.js";

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

  // Animate
  app.ticker.add((time) => {
    bunny.rotation += 0.1 * time.deltaTime;
  });
})();
