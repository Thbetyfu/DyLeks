---
name: ui-designer
description: Mendesain antarmuka pengguna (UI/UX) premium (High-Fidelity) ramah disleksia menggunakan Vanilla CSS dan Next.js, mematuhi Global Rules dan standar aksesibilitas WCAG AA.
---

# ui-designer (Otak Desain Visual Premium & Ramah Disleksia)

Skill ini memberikan pedoman instruksi terperinci, token desain, dan potongan kode bagi agen AI untuk merancang serta mengimplementasikan antarmuka pengguna (UI/UX) premium kelas atas untuk ekosistem DyLeks.

## Prinsip Desain Utama (UCD & Aksesibilitas)

Aplikasi DyLeks melayani anak-anak disleksia dan disgrafia di daerah 3T. Desain visual harus memberikan **efek WOW** yang instan namun tetap fungsional, tidak melelahkan mata (*anti-glare*), dan memudahkan pembacaan huruf.

### 1. Palet Warna Premium (Curated HSL)
Jangan gunakan warna standar bawaan browser. Gunakan warna pastel hangat berbasis HSL untuk mengurangi efek stres kognitif visual (*visual stress*):

| Kategori | Token Warna | Nilai HSL | Contoh Penggunaan |
| :--- | :--- | :--- | :--- |
| **Warm Canvas (Background)** | `--bg-warm` | `hsl(36, 33%, 97%)` | Latar belakang dasar (krem lembut) |
| **Dark Slate (Text)** | `--text-dark` | `hsl(215, 25%, 15%)` | Warna teks utama agar kontras tinggi tapi tidak silau |
| **Soft Emerald (Success)** | `--color-success`| `hsl(150, 45%, 40%)` | Umpan balik benar pada Listen Card / game |
| **Warm Amber (Warning)** | `--color-warning`| `hsl(35, 85%, 50%)` | Indikator risiko sedang / perhatian |
| **Soft Coral (Error)** | `--color-danger` | `hsl(5, 75%, 60%)` | Umpan balik salah / indikator risiko tinggi |
| **Dyleks Blue (Primary)** | `--color-primary`| `hsl(210, 80%, 45%)` | Tombol utama, progress bar, link aktif |
| **Glass border** | `--border-glass` | `hsla(210, 20%, 80%, 0.4)`| Garis tepi kartu transparan |

### 2. Glassmorphism & UI Layers
Gunakan desain lapisan kaca (*glassmorphism*) untuk memberikan kesan premium, modern, dan kedalaman taktil:
- Gunakan latar belakang semi-transparan: `background: rgba(255, 255, 255, 0.65)` atau `hsla(0, 0%, 100%, 0.65)`.
- Gunakan efek kabur (*blur*): `backdrop-filter: blur(12px)`.
- Pasangkan dengan bayangan lembut: `box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.08)`.

### 3. Tipografi & Tata Letak Khusus Disleksia
- **Font**: Gunakan `OpenDyslexic` untuk konten teks intervensi anak, dan `Inter` atau `Roboto` untuk antarmuka guru dan dasbor.
- **Letter Spacing**: Berikan ruang ekstra antar huruf (`letter-spacing: 0.12em`) dan kata (`word-spacing: 0.18em`).
- **Line Height**: Gunakan tinggi baris setidaknya `line-height: 1.6` untuk menghindari penumpukan visual.
- **Align**: Jangan gunakan rata kanan-kiri (*justify*). Gunakan rata kiri (*text-align: left*) karena margin kanan yang tidak rata membantu mata anak disleksia membedakan baris baru.

---

## Pedoman Pembuatan Kode CSS Premium

Gunakan standar CSS kustom properti di file gaya utama (misalnya `FE/styles/globals.css`):

```css
:root {
  /* Design Tokens */
  --bg-warm: hsl(36, 33%, 97%);
  --text-dark: hsl(215, 25%, 15%);
  --text-muted: hsl(215, 12%, 45%);
  --color-primary: hsl(210, 80%, 45%);
  --color-primary-hover: hsl(210, 85%, 38%);
  
  --glass-bg: rgba(255, 255, 255, 0.7);
  --glass-border: rgba(255, 255, 255, 0.4);
  --glass-shadow: 0 8px 24px 0 rgba(31, 38, 135, 0.06);
  --radius-lg: 16px;
  
  --transition-smooth: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
}

/* Base Stylings */
body {
  background-color: var(--bg-warm);
  color: var(--text-dark);
  font-family: 'Inter', system-ui, sans-serif;
  line-height: 1.6;
}

/* Glass Card Component */
.glass-card {
  background: var(--glass-bg);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid var(--glass-border);
  box-shadow: var(--glass-shadow);
  border-radius: var(--radius-lg);
  padding: 24px;
  transition: var(--transition-smooth);
}

.glass-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 36px 0 rgba(31, 38, 135, 0.1);
}

/* Premium Button Component */
.btn-primary {
  background-color: var(--color-primary);
  color: #ffffff;
  border: none;
  padding: 12px 24px;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition-smooth);
  box-shadow: 0 4px 12px rgba(33, 150, 243, 0.2);
}

.btn-primary:hover {
  background-color: var(--color-primary-hover);
  transform: scale(1.02);
  box-shadow: 0 6px 16px rgba(33, 150, 243, 0.3);
}

.btn-primary:active {
  transform: scale(0.98);
}
```

---

## Langkah Kerja Mendesain Halaman (Workflow)

Saat diperintahkan membuat halaman baru, lakukan urutan langkah spesifik berikut:
1. **Analisis Semantik**: Buat struktur kerangka semantik HTML5 (`<header>`, `<main>`, `<section>`, `<article>`, `<footer>`).
2. **Definisikan Token**: Hubungkan properti warna, margin, dan radius ke CSS kustom variabel yang telah didefinisikan.
3. **Tambahkan Micro-Animations**:
   - Berikan transisi halus (`transition`) pada setiap interaksi tombol, link, dan hover card.
   - Tambahkan efek interaktif (*ripple effect* atau *card flip* pada Listen Card).
4. **Validasi Aksesibilitas**:
   - Uji kontras warna menggunakan alat pengujian (pastikan rasio kontras teks dasar vs latar belakang minimal 4.5:1).
   - Pastikan setiap tombol dan input memiliki deskripsi `aria-label` yang jelas untuk pembaca layar (screen reader).
5. **Tanpa Placeholder**: Gunakan gambar fungsional riil (misalnya hasil gambar dari model atau rendering SVG kustom yang indah), dilarang menggunakan placeholder gambar kosong seperti `https://via.placeholder.com/150`.
