import { Graphics } from "pixi.js";

export function square({
  x,
  y,
  length,
}: {
  x: number;
  y: number;
  length: number;
}) {
  const points = [
    { x: x, y: y },
    { x: x + length, y: y },
    { x: x + length, y: y + length },
    { x: x, y: y + length },
  ];
  return new Graphics().poly(points).fill(0xff0000);
}

/** Renders a hexagon. */
export function hexagon({
  x,
  y,
  length,
}: {
  x: number;
  y: number;
  length: number;
}) {
  // -- Build points -- //
  const radius = length / 2;
  const points = [
    { x: x + radius, y: y },
    { x: x + radius / 2, y: y + (Math.sqrt(3) * radius) / 2 },
    { x: x - radius / 2, y: y + (Math.sqrt(3) * radius) / 2 },
    { x: x - radius, y: y },
    { x: x - radius / 2, y: y - (Math.sqrt(3) * radius) / 2 },
    { x: x + radius / 2, y: y - (Math.sqrt(3) * radius) / 2 },
  ];

  // -- Create shape -- //
  return new Graphics()
    .poly(points)
    .stroke({ color: "#000", width: 5 })
    .fill(0xff0000);
}
