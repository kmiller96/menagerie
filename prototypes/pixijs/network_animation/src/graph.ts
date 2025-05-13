/** Generates a graph with N nodes about (0, 0) */
export async function createGraph(N: number = 3) {
  // Create the nodes in a circle around the origin
  const nodes = Array.from({ length: N }, (_, i) => ({
    x: Math.cos((i / N) * 2 * Math.PI),
    y: Math.sin((i / N) * 2 * Math.PI),
  }));

  return nodes;
}
