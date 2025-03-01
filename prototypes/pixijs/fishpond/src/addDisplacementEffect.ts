import { DisplacementFilter, Sprite, Application, WRAP_MODES } from "pixi.js";

export function addDisplacementEffect(app: Application) {
  const sprite = Sprite.from("displacement");
  sprite.texture.baseTexture.wrapMode = WRAP_MODES.REPEAT;

  const filter = new DisplacementFilter({
    sprite,
    scale: 50,
  });

  app.stage.filters = [filter];
}
