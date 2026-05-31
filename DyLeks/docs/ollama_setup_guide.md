# Panduan Setup Ollama Luring (Offline) — DyLeks Teacher's Copilot

Panduan ini ditujukan bagi tim lapangan atau pendidik untuk memasang server *Small Language Model* (SLM) secara luring di laptop server sekolah daerah 3T (tanpa koneksi internet).

---

## 📋 Prasyarat Spesifikasi Laptop
*   **Sistem Operasi:** Windows 10/11 (64-bit) atau Linux Ubuntu 20.04+.
*   **Prosesor:** Minimal Intel Core i3 (Generasi ke-8 ke atas) atau AMD Ryzen 3.
*   **RAM:** Minimal 4 GB (Sangat direkomendasikan 8 GB untuk kelancaran multi-device).
*   **Penyimpanan:** Menyediakan sisa ruang minimal 5 GB di SSD.

---

## 1. Persiapan Bahan Luring (Dilakukan di Kota / Area Berinternet)

Sebelum berangkat ke lokasi sekolah 3T, Anda harus mengunduh berkas installer dan model AI terlebih dahulu ke dalam **Flashdisk USB**:

1.  **Unduh Installer Ollama:**
    *   Unduh untuk Windows: [OllamaSetup.exe](https://ollama.com/download/OllamaSetup.exe) (Ukuran ~180MB).
2.  **Unduh Model SLM Ringan:**
    *   Buka terminal di komputer berinternet yang sudah terpasang Ollama, jalankan perintah untuk mengunduh model:
        ```bash
        ollama pull qwen2.5:1.5b
        ```
        *(Catatan: Model Qwen 2.5 berukuran 1.5B (1.5 Milyar Parameter / ~980MB) sangat direkomendasikan karena ringan, hemat RAM, dan memahami Bahasa Indonesia dengan sangat baik).*
3.  **Ekspor Berkas Model dari Komputer Berinternet:**
    *   Secara default, Ollama menyimpan berkas model di direktori:
        *   **Windows:** `%USERPROFILE%\.ollama\models`
        *   **Linux/Mac:** `~/.ollama/models`
    *   Salin seluruh isi folder `models` tersebut ke dalam Flashdisk USB Anda.

---

## 2. Instalasi Luring di Laptop Sekolah (Lokasi 3T - Tanpa Internet)

Setelah tiba di lokasi sekolah pilot 3T:

### Langkah A: Instalasi Aplikasi Ollama
1.  Masukkan Flashdisk USB ke laptop guru.
2.  Salin file `OllamaSetup.exe` ke laptop, lalu jalankan instalasi hingga selesai.
3.  Pastikan aplikasi Ollama sudah berjalan (ikon gajah abu-abu muncul di *System Tray* pojok kanan bawah desktop).

### Langkah B: Impor Berkas Model AI
1.  Tutup aplikasi Ollama terlebih dahulu (Klik kanan ikon Ollama di *System Tray* -> Pilih **Quit**).
2.  Salin seluruh folder `models` yang ada di Flashdisk USB ke direktori laptop sekolah:
    *   Tempel ke path: `C:\Users\<Nama_User_Laptop>\.ollama\models` (Gantikan folder `models` kosong yang ada di sana).
3.  Jalankan kembali aplikasi Ollama dari *Start Menu*.
4.  Buka **Command Prompt (CMD)** di laptop sekolah, lalu verifikasi keberadaan model dengan mengetik:
    ```cmd
    ollama list
    ```
    Pastikan model `qwen2.5:1.5b` (atau model yang Anda pilih) terdaftar dalam list.
5.  Uji model secara langsung di CMD secara luring dengan perintah:
    ```cmd
    ollama run qwen2.5:1.5b
    ```
    Ketikkan pertanyaan uji coba (misal: "Halo, siapa kamu?") untuk memastikan respon luring keluar dengan sukses.

---

## 3. Penyelarasan Konfigurasi Backend FastAPI
Agar backend **DyLeks** terhubung ke model luring ini, buka file konversi environment variabel backend `.env` di direktori `BE/` laptop server:

```env
# Konfigurasi LLM luring
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=qwen2.5:1.5b
```

Jalankan backend FastAPI. Server akan secara otomatis menyalurkan pesan chat asisten guru ke server Ollama lokal tanpa memerlukan kuota internet.
