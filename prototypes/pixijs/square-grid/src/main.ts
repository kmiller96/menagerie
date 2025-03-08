import { Application, Graphics, GraphicsContext } from "pixi.js";

const BACKGROUND_COLOR = 0xffffff;

let ISLEFTHOLDING = false;
let ISRIGHTHOLDING = false;

async function init(): Promise<Application> {
  const app = new Application();
  await app.init({ background: BACKGROUND_COLOR, resizeTo: window });

  document.getElementById("pixi-container")!.appendChild(app.canvas);

  return app;
}

async function registerPointerEvents() {
  window.addEventListener("mousedown", (e) => {
    e.preventDefault();
    if (e.button === 0) ISLEFTHOLDING = true;
    if (e.button === 2) ISRIGHTHOLDING = true;
  });

  window.addEventListener("mouseup", (e) => {
    e.preventDefault();
    if (e.button === 0) ISLEFTHOLDING = false;
    if (e.button === 2) ISRIGHTHOLDING = false;
  });
}

/** Creates the grid graphic */
async function drawGrid(
  app: Application,
  { gridSize = 50 }: { gridSize?: number }
) {
  // Determine grid geometry
  const nRows = Math.floor(app.screen.height / gridSize);
  const nCols = Math.floor(app.screen.width / gridSize);

  const xPadding = (app.screen.width - nCols * gridSize) / 2;
  const yPadding = (app.screen.height - nRows * gridSize) / 2;

  // Draw graphics context
  const squareContext = new GraphicsContext()
    .rect(0, 0, gridSize, gridSize)
    .fill(BACKGROUND_COLOR)
    .stroke(0x000000);

  // Draw grid
  for (let i = 0; i < nRows; i++) {
    for (let j = 0; j < nCols; j++) {
      const square = new Graphics(squareContext);

      square.position.set(j * gridSize + xPadding, i * gridSize + yPadding);

      const paintSquare = () => {
        if (ISLEFTHOLDING) square.tint = 0x0000ff;
        if (ISRIGHTHOLDING) square.tint = 0xff0000;
      };

      square.eventMode = "static";

      square.on("mousedown", paintSquare);
      square.on("pointerenter", paintSquare);

      app.stage.addChild(square);
    }
  }
}

(async () => {
  const app = await init();

  await registerPointerEvents();
  await drawGrid(app, { gridSize: 70 });
})();
