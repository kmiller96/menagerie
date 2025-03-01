import { Application, Assets } from "pixi.js";

import assets from "./assets";
import { addBackground } from "./addBackground";

(async () => {
  // Create a PixiJS application.
  const app = new Application();

  // Asynchronous IIFE
  (async () => {
    await setup();
    await preload();

    addBackground(app);
  })();

  async function setup() {
    await app.init({ background: "#1099bb", resizeTo: window });
    document.getElementById("pixi-container")!.appendChild(app.canvas);
  }

  async function preload() {
    await Assets.load(assets);
  }
})();
