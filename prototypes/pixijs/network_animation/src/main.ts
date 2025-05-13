import { Application } from "pixi.js";
import { createGraph } from "./graph";
import { drawNetwork } from "./draw";

async function init(): Promise<Application> {
  // Change context menu handler to require shift-right click
  window.addEventListener("contextmenu", (e) => {
    if (!e.shiftKey) {
      e.preventDefault();
    }
  });

  // Create app
  const app = new Application();
  await app.init({ background: "#fff", resizeTo: window });

  // Add to document and return
  document.getElementById("pixi-container")!.appendChild(app.canvas);
  return app;
}

(async () => {
  // Initialize application
  const app = await init();

  // Create graph
  const graph = await createGraph(12);
  console.log(graph);

  // Draw
  // drawNetwork(app, graph);
})();
