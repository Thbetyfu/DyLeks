---
name: fe-manager
description: Mengelola frontend Next.js server, running Playwright tests, dan build verifikasi untuk DyLeks.
---

# fe-manager (Frontend Next.js Manager)

Skill ini digunakan untuk mengelola, menjalankan, memantau, dan menguji aplikasi Next.js frontend (PWA) dari ekosistem DyLeks.

## Setup & Dependensi

Pastikan node_modules terpasang:
1. Pindah ke direktori frontend: `cd FE`
2. Instal pustaka pendukung: `npm install`

## Menjalankan Frontend Dev Server

Untuk menjalankan Next.js dev server pada port `3001` (sesuai spesifikasi port bebas tabrakan untuk DyLeks):

```bash
cd FE
npm run dev
```

> [!NOTE]
> Konfigurasi dev server telah disetel untuk berjalan di port `3001` (lihat `package.json`). Pastikan tidak ada proses zombie yang menempati port ini sebelum dijalankan.

## Build Verifikasi

Untuk memverifikasi kompatibilitas tipe TypeScript dan keberhasilan build statik Next.js:

```bash
cd FE
npm run build
```

## Menjalankan Pengujian Playwright

Untuk menjalankan pengujian integrasi UI secara otomatis menggunakan Playwright:

```bash
cd FE
npx playwright test
```

## Struktur File Frontend Utama

- `pages/`:
  - `index.tsx`: Halaman dasbor guru (Local Mesh Dashboard).
  - `screening.tsx`: Antarmuka pengambilan gambar tulisan tangan siswa.
  - `latihan.tsx`: Modul Listen Card (dengar-lalu-tulis).
  - `game.tsx`: Halaman gamifikasi & reward system.
  - `summary.tsx`: Halaman ringkasan hasil risiko & pola kesalahan.
- `public/`: Menyimpan static assets, service worker manifest, dan modul audio.
- `styles/`: Kumpulan styling UI glassmorphism ramah disleksia.
