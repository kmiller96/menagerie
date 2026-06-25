import { defineConfig } from "vite";
import react, { reactCompilerPreset } from "@vitejs/plugin-react";

import tailwindcss from "@tailwindcss/vite";
import babel from "@rolldown/plugin-babel";
import { viteSingleFile } from "vite-plugin-singlefile";

// https://vite.dev/config/
export default defineConfig({
  build: {
    assetsInlineLimit: Number.MAX_SAFE_INTEGER,
  },
  plugins: [
    react(),
    babel({ presets: [reactCompilerPreset()] }),
    tailwindcss(),
    viteSingleFile({ removeViteModuleLoader: true }),
  ],
});
