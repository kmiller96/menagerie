import { Application, Sprite } from "pixi.js";

export function addBackground(app: Application) {
  const background = Sprite.from("background");

  background.anchor.set(0.5);

  console.log({ widht: background.width, height: background.height });

  const widthRatio = app.screen.width / background.width;
  const heightRatio = app.screen.height / background.height;

  if (widthRatio > heightRatio) {
    background.width = app.screen.width;
    background.scale.y = background.scale.x;
  } else {
    background.height = app.screen.height;
    background.scale.x = background.scale.y;
  }

  background.x = app.screen.width / 2;
  background.y = app.screen.height / 2;

  app.stage.addChild(background);
}
