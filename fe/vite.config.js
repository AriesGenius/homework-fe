import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";


export default defineConfig({
  plugins: [react()],

  css: {
    devSourcemap: true,
    
    modules: {
      
      generateScopedName: "[name]__[local]___[hash:base64:5]",
      hashPrefix: "prefix",
    },
    preprocessorOptions: {
      less: {
        javascriptEnabled: true,
        math: "parens-division",
      },
    },
  },

  server: {
    
    proxy: {
      "/api": {
        
        target: "http://127.0.0.1:5000",
        // target: "http://localhost:5000", 
        changeOrigin: true, 
        ws: true, 
       
        rewrite: (path) => path.replace(/^\/api/, ""),
      },
    },
  },

});
