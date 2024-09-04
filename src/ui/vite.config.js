import react from "@vitejs/plugin-react";
import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
  root: 'public', 
  base: './',
  build: {
    outDir: resolve(__dirname, './dist'),
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'public/index.html'),
      },
    },
    emptyOutDir: true,
  },
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: `@import "@/scss/stylesheet.scss";`,
      },
    },
  },
  plugins: [
    react()
  ],
  resolve: {
    alias: {
      '@': resolve(__dirname, 'src'),
    },
  },
  server: {
    port: 3000, // Default port for Vite server
    open: true, // Open the browser automatically when the server starts
  },
});
