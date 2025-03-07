import { Application, Graphics } from "pixi.js";

const CIRCLE_RADIUS = [1, 5];
const CIRCLE_FILL_COLOR = 0xffffff;

// ------------- //
// -- Helpers -- //
// ------------- //

// ------------------------ //
// -- Main Program Loops -- //
// ------------------------ //

/** Initialises the application */
async function init() {
  const app = new Application();
  await app.init({ background: "#1099bb", resizeTo: window });

  document.getElementById("pixi-container")!.appendChild(app.canvas);

  return app;
}

/** Draws the screen */
async function draw(app: Application) {
  for (let i = 0; i < 10; i++) {
    const x = Math.round(Math.random() * app.screen.width);
    const y = Math.round(Math.random() * app.screen.height);
    const r =
      Math.round(Math.random() * (CIRCLE_RADIUS[1] - CIRCLE_RADIUS[0])) +
      CIRCLE_RADIUS[0];

    const circle = new Graphics().circle(x, y, r).fill(CIRCLE_FILL_COLOR);
    app.stage.addChild(circle);
  }
}

(async () => {
  const app = await init();

  app.ticker.add(async () => {
    await draw(app);
  });
})();
