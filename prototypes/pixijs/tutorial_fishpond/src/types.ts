import { Sprite } from "pixi.js";

export type Fish = Sprite & {
  direction: number;
  speed: number;
  turnSpeed: number;
};
