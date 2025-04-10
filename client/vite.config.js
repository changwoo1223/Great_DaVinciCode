import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  root: '.'  // Vite 프로젝트의 루트를 client 폴더로 설정

})
