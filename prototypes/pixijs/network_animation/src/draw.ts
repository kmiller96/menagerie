import { Application, Graphics, GraphicsContext } from "pixi.js";

const CIRCLE_RADIUS = 10;
const CIRCLE_COLOR = 0x000000;

const CIRCLE = new GraphicsContext()
  .circle(0, 0, CIRCLE_RADIUS)
  .fill(CIRCLE_COLOR);

/** Draws the network. */
export async function drawNetwork(
  app: Application,
  graph: { x: number; y: number }[]
) {
  // Draw the graph
  for (const node of graph) {
    const graphics = new Graphics(CIRCLE);
    graphics.position.set(node.x, node.y);
    app.stage.addChild(graphics);
  }
}
