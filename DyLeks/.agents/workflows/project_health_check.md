# Workflow: Project Health Check (Diagnosis Kesehatan Proyek)

Workflow ini digunakan untuk memverifikasi kesehatan seluruh komponen ekosistem luring DyLeks secara menyeluruh sebelum melakukan deployment atau testing terintegrasi.

---

## Langkah 1: Memeriksa Port Jaringan Lokal (3001 & 3002)

Pastikan port target terbebas dari proses zombie atau siap digunakan.

1. Buka terminal/command prompt.
2. Jalankan perintah pemeriksaan port:
   - **Windows PowerShell:**
     ```powershell
     Get-NetTCPConnection -LocalPort 3001, 3002 -ErrorAction SilentlyContinue
     ```
   - **Linux/macOS terminal:**
     ```bash
     lsof -i :3001 && lsof -i :3002
     ```

> [!CAUTION]
> Jika ada proses yang menempati port ini namun server dev sedang tidak berjalan secara sah, matikan proses tersebut menggunakan perintah `Kill-Process` atau `kill -9` sebelum memulai.

---

## Langkah 2: Memeriksa Status Database SQLite Lokal

Gunakan skrip pembantu untuk memeriksa apakah file `dyslexiai_local.db` ada dan terisi tabel yang valid.

```bash
# Jalankan dari direktori root proyek DyLeks
python .agents/skills/db-manager/scripts/db_inspector.py --summary
```

**Verifikasi:**
- Tabel `child_profiles`, `screening_sessions`, dan `risk_assessments` harus ada.
- Jika database belum terbuat atau error, restart backend FastAPI untuk menginisialisasinya.

---

## Langkah 3: Menjalankan Pengujian Unit Backend

Jalankan rangkaian unit test menggunakan pytest untuk memverifikasi logika algoritma scoring dan adaptive engine.

```bash
# Jalankan dari direktori root proyek DyLeks
python .agents/skills/be-manager/scripts/be_helper.py --test
```

**Verifikasi:**
- Pastikan semua test case lulus (`pytest` mengembalikan exit code 0).

---

## Langkah 4: Memeriksa Build Frontend Next.js

Verifikasi bahwa aplikasi web Next.js dapat dibangun menjadi aset statis PWA dengan sukses tanpa error kompilasi TypeScript.

```bash
cd FE
npm run build
```

**Verifikasi:**
- Periksa konsol untuk memastikan tidak ada kesalahan tipe data TypeScript atau file yang hilang.
- Folder `.next/` harus berhasil dibuat.

---

## Langkah 5: Memeriksa Koneksi Ollama Offline (Teacher's Copilot)

Asisten guru membutuhkan Ollama yang terpasang secara lokal untuk memproses konsultasi secara offline.

1. Pastikan aplikasi Ollama sedang berjalan di latar belakang laptop.
2. Uji kueri lokal melalui command line:
   ```bash
   ollama list
   ```
3. Pastikan model bahasa super-ringan seperti `qwen1.5:1.8b` atau `phi3:mini` terpasang di server lokal.

---

## Hasil Diagnosis Akhir

Jika kelima langkah di atas berhasil lolos tanpa error kritis:
- **Status Sistem:** 🟢 **HEALTHY (SIAP PAKAI)**
- Sistem siap digunakan untuk simulasi uji coba luring di lingkungan hotspot lokal kelas!
