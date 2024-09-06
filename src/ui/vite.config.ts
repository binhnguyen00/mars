import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';

export default defineConfig({
  root: path.resolve(__dirname),                            // Set the root to current dir
  publicDir: path.resolve(__dirname, 'public'),             // this is default, dont have to add
  cacheDir: path.resolve(__dirname, 'node_modules/.vite'),  // this is default, dont have to add
  plugins: [
    react()
  ],
  server: {
    port: 3000,
    open: true,
  },
  css: {
    devSourcemap: true,
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
    },
  },
  build: {
    outDir: path.resolve(__dirname, './dist'),              // this is default, dont have to add
    emptyOutDir: true,
  }
});
