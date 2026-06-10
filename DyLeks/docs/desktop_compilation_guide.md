# Panduan Kompilasi Aplikasi Desktop DyLeks (Inno Setup Guide)

Dokumen ini memandu pengembang dalam mengompilasi ekosistem luring **DyLeks** (Next.js PWA, FastAPI, SQLite, dan Electron) menjadi satu berkas installer mandiri Windows (`.exe` atau `.msi`) menggunakan **Inno Setup Compiler**.

---

## 📋 Prasyarat Kompilasi

Sebelum memulai proses pembuatan berkas installer, pastikan Anda telah menyiapkan prasyarat berikut di komputer pengembang:

1. **Inno Setup Compiler (v6.0+)**: Unduh dan pasang secara gratis dari [jrsoftware.org](https://www.jrsoftware.org/isdl.php).
2. **Node.js & Python**: Pastikan Node.js dan Python telah terpasang di komputer target, serta terdaftar di dalam environment variables Windows (`PATH`).
3. **Instalasi Dependensi**:
   * Jalankan `npm install` di dalam direktori `FE` untuk memasang Next.js, PWA, dan Electron.
   * Jalankan `pip install -r requirements.txt` di dalam direktori `BE` untuk memastikan seluruh pustaka Python tersedia.
4. **Build Produksi Next.js**:
   * Masuk ke folder `FE` dan jalankan perintah:
     ```bash
     npm run build
     ```
     Langkah ini wajib dilakukan agar Next.js menghasilkan direktori `.next` teroptimasi sebelum dibundel ke installer.

---

## 🛠️ Langkah-Langkah Kompilasi (.exe Installer)

Setelah semua prasyarat siap, ikuti langkah berikut untuk memproduksi berkas installer:

1. **Buka Berkas Script Inno Setup**:
   * Buka aplikasi **Inno Setup Compiler** di Windows Anda.
   * Pilih menu **File > Open**, lalu arahkan ke berkas script:
     `FE/desktop/inno_setup.iss`

2. **Kompilasi Script**:
   * Tekan tombol **Compile** (ikon tombol hijau bertuliskan **Run** atau tekan tombol `Ctrl + F9` di keyboard).
   * Inno Setup akan mulai memindai dan memadatkan seluruh berkas backend `BE`, frontend `FE` (termasuk folder `node_modules`), dan orkestrator Electron `main.js`.

3. **Hasil Output**:
   * Setelah proses kompilasi selesai tanpa galat, berkas installer mandiri akan terbentuk di folder baru bernama `Output` di dalam direktori `FE/desktop/`.
   * Nama berkas default hasil kompilasi adalah **`DyLeks_Setup_v2.0.exe`**.

---

## 🚀 Cara Penggunaan oleh Guru di Lapangan

Setelah berkas `DyLeks_Setup_v2.0.exe` didistribusikan ke sekolah sasaran, guru cukup mengikuti langkah mudah berikut:

1. **Instalasi Satu-Klik**:
   * Guru mengklik ganda berkas `DyLeks_Setup_v2.0.exe`.
   * Ikuti panduan wizard instalasi modern (pilih opsi *Create a desktop shortcut* jika ingin menampilkan ikon di layar utama desktop).
   * Proses instalasi akan secara otomatis menyalin semua berkas dan menambahkan pengecualian firewall port `3001` (klien PWA) dan `3002` (backend API) pada Windows Defender Firewall agar bisa diakses oleh HP siswa dalam jaringan lokal.

2. **Menjalankan Aplikasi**:
   * Klik ganda ikon shortcut **DyLeks Local AI Platform** di layar utama desktop komputer.
   * Jendela aplikasi native desktop (Electron) akan terbuka.
   * Orkestrator Electron akan menyalakan server Next.js & FastAPI secara senyap di latar belakang (*silent background process*), lalu memuat halaman Dashboard Guru (`http://localhost:3001/dashboard`).

3. **Menutup Aplikasi**:
   * Guru cukup mengklik tanda silang (`✕`) di pojok kanan atas jendela aplikasi.
   * Jendela Electron akan menutup dan secara otomatis mendeteksi lalu menghentikan seluruh proses latar belakang (*kill background processes*) di port 3001 & 3002 secara bersih untuk mencegah *zombie process* atau *port leakage*.
