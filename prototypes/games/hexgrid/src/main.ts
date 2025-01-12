import { Application, Assets, Graphics, Sprite } from "pixi.js";

import { defineHex, Grid, rectangle } from "honeycomb-grid";

import { square, hexagon } from "./shapes";

async function initApp(): Promise<Application> {
  const app = new Application();
  await app.init({ background: "#fff", resizeTo: window });

  document.getElementById("pixi-container")!.appendChild(app.canvas);

  return app;
}

(async () => {
  const app = await initApp();
  const graphics = new Graphics();

  const Hex = defineHex({ dimensions: 30 });
  const grid = new Grid(Hex, rectangle({ width: 10, height: 10 }));

  const renderHex = (hex: Hex) => {

  grid.forEach(renderHex)

})();

import * as PIXI from "pixi.js";

// you may want the origin to be the top left corner of a hex's bounding box
// instead of its center (which is the default)
const Hex = defineHex({ dimensions: 30, origin: "topLeft" });
const grid = new Grid(Hex, rectangle({ width: 10, height: 10 }));

const app = new PIXI.Application({ backgroundAlpha: 0 });
const graphics = new PIXI.Graphics();

document.body.appendChild(app.view);
graphics.lineStyle(1, 0x999999);

grid.forEach(renderHex);
app.stage.addChild(graphics);

function renderHex(hex: Hex) {
  // PIXI.Polygon happens to be compatible with hex.corners
  graphics.drawShape(new PIXI.Polygon(hex.corners));
}
