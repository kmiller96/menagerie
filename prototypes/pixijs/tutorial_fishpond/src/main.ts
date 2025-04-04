import { Application, Assets } from "pixi.js";

import assets from "./assets";

import { Fish } from "./types";
import { addBackground } from "./addBackground";
import { addFishes, animateFishes } from "./addFishes";
import { addWaterOverlay, animateWaterOverlay } from "./addWaterOverlay";
import { addDisplacementEffect } from "./addDisplacementEffect";

(async () => {
  // Create a PixiJS application.
  const app = new Application();

  const fishes: Array<Fish> = [];

  // Asynchronous IIF
  (async () => {
    await setup();
    await preload();

    addBackground(app);
    addFishes(app, fishes);
    addWaterOverlay(app);
    addDisplacementEffect(app);

    app.ticker.add((time) => {
      animateFishes(app, fishes, time);
      animateWaterOverlay(app, time);
    });
  })();

  async function setup() {
    await app.init({ background: "#1099bb", resizeTo: window });
    document.getElementById("pixi-container")!.appendChild(app.canvas);
  }

  async function preload() {
    await Assets.load(assets);
  }
})();
