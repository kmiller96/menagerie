import type { Config } from "tailwindcss";

import daisyui from "daisyui";

export default {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "var(--background)",
        foreground: "var(--foreground)",
      },
    },
  },
  plugins: [daisyui],
  daisyui: {
    themes: [
      {
        mytheme: {
          primary: "#8c00ff",
          secondary: "#00a8b9",
          accent: "#0080ff",
          neutral: "#131c07",
          "base-100": "#fff5ff",
          info: "#00ebff",
          success: "#50ad00",
          warning: "#ac5500",
          error: "#ea2e42",
        },
      },
      "dark",
    ],
  },
} satisfies Config;
