import { Application, Assets, Sprite } from "pixi.js";
import { square, hexagon } from "./shapes";

async function initApp(): Promise<Application> {
  const app = new Application();
  await app.init({ background: "#fff", resizeTo: window });

  document.getElementById("pixi-container")!.appendChild(app.canvas);

  return app;
}

(async () => {
  const app = await initApp();

  const length = 100;
  const hexWidth = 2 * length;
  const hexHeight = Math.sqrt(3) * length;

  const horizontalSpacing = (3 / 4) * hexWidth;
  const verticalSpacing = hexHeight;

  const x = 100;
  const y = 100;

  // Starting hex
  app.stage.addChild(hexagon({ x, y, length }));

  app.stage.addChild(hexagon({ x, y: y + verticalSpacing / 2, length }));
  app.stage.addChild(hexagon({ x, y: y + (2 * verticalSpacing) / 2, length }));

  app.stage.addChild(
    hexagon({
      x: x + horizontalSpacing / 2,
      y: y + verticalSpacing / 4,
      length,
    })
  );
  app.stage.addChild(hexagon({ x, y: y + (2 * verticalSpacing) / 2, length }));
})();
