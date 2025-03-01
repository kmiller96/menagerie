import { Application, Texture, Ticker, TilingSprite } from "pixi.js";

let overlay: TilingSprite;

export function addWaterOverlay(app: Application) {
  const texture = Texture.from("overlay");

  overlay = new TilingSprite({
    texture,
    width: app.screen.width,
    height: app.screen.height,
  });

  app.stage.addChild(overlay);
}

export function animateWaterOverlay(app: Application, time: Ticker) {
  const delta = time.deltaTime;

  overlay.tilePosition.x += delta;
  overlay.tilePosition.y += delta;
}
