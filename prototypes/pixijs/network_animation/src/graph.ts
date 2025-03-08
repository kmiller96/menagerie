import { Application } from "pixi.js";

/** Creates a coordinate for the graph about some central point. */
function generateGraphCoordinates(center: { x: number; y: number }) {
  const randomPositionAboutX0 = (x0: number, r: number) =>
    x0 + 2 * (Math.random() - 0.5) * r;

  const x = randomPositionAboutX0(center.x, 200);
  const y = randomPositionAboutX0(center.y, 200);

  return { x, y };
}

/** Creates an abstract representation of the graph */
export function createGraph(app: Application, nodes: number = 3) {
  const centroid = { x: app.screen.width / 2, y: app.screen.height / 2 };
  const graph = [];

  for (let i = 0; i < nodes; i++) {
    graph.push(generateGraphCoordinates(centroid));
  }

  return graph;
}
