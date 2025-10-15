import { defineConfig } from "vite";
import tailwindcss from "@tailwindcss/vite";

// https://vite.dev/config/
export default defineConfig({
  plugins: [tailwindcss()],
  base: "/static/",
  build: {
    manifest: true,
    rollupOptions: {
      input: {
        main: "./src/main.js",
        styles: "./src/main.css",
      },
    },
  },
  server: {
    host: "0.0.0.0",
    port: 5173,
    strictPort: true,
    origin: "http://localhost:8000",
    watch: {
      usePolling: true,
      ignored: ['!**/node_modules/**', '**/.*/**'],
    },
  },
});
