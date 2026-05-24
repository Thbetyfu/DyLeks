---
# `DyLeks`

**Ekosistem Edge-AI Offline & PWA Multi-Device untuk Skrining Dini serta Pembelajaran Adaptif Multisensori bagi Anak Disleksia di Daerah 3T**
---
## 1. Masalah: "The 3T Identification Vacuum" di Indonesia

Di balik pesatnya kemajuan EdTech di kota-kota besar, masih ada kesenjangan kualitas pendidikan yang masif di daerah **3T (Tertinggal, Terdepan, dan Terluar)**. Diperkirakan terdapat lebih dari **5 juta anak dengan disleksia** di Indonesia, namun **lebih dari 80% di antaranya tidak pernah terdiagnosis**.

Di daerah 3T, tantangannya berlipat ganda:

* **Zero-Internet Reality:** Ketiadaan koneksi internet stabil membuat platform berbasis *cloud* mustahil digunakan.
* **Infrastruktur Terbatas:** Sekolah tidak memiliki komputer berspesifikasi tinggi, melainkan laptop *legacy* standar bantuan pemerintah atau *smartphone* Android ramah anggaran milik guru/orang tua.
* **Scarcity of Experts:** Tidak adanya psikolog anak atau guru inklusi membuat gejala disleksia sering salah diidentifikasi sebagai "malas belajar", sehingga anak-anak kehilangan hak kesetaraan untuk berkembang.

**DyLeks** hadir sebagai solusi inklusif yang mendemokrasi akses skrining dan intervensi dini tanpa ketergantungan pada internet maupun perangkat mahal.

---

## 2. Solusi & Inovasi: Edge-AI Multi-Device Framework

**DyLeks** adalah platform hibrida (*Laptop-to-Mobile*) yang berjalan **100% secara lokal (OFFLINE)** memanfaatkan jaringan Wi-Fi lokal kelas (*Local Hotspot Setup*) tanpa kuota data:

* **Laptop-as-a-Server Hub:** Laptop guru bertindak sebagai pangkalan data lokal (`dyslexiai_local.db`) dan mesin pemroses AI utama.
* **Mobile-as-a-Client PWA:** Aplikasi *Front-End* dikemas sebagai *Progressive Web App* (PWA) yang dapat diakses dan diinstal langsung ke *smartphone* Android/iOS milik guru atau orang tua siswa via browser tanpa perlu akses ke Play Store/App Store.
* **Physical-to-Digital Pipeline:** Anak tetap menulis di atas kertas fisik menggunakan pensil untuk melatih motorik halus, lalu hasilnya difoto menggunakan kamera *smartphone* untuk dikirim ke *local server* laptop guna dianalisis.
* **Privacy-First Edge Computing:** Seluruh inferensi AI berjalan di sisi lokal perangkat, menjamin keamanan data tumbuh kembang anak-anak di pedalaman.

---

## 3. Tech Stack & Engineering Excellence (Optimized for Low-Spec Devices)

Sistem dioptimasi secara arsitektural agar mampu berjalan lancar pada perangkat komputasi standar sekolah pelosok melalui kompresi model ke format **ONNX Runtime**:

| Komponen                            | Teknologi                               | Peran & Optimalisasi 3T                                                                                                                                      |
| ----------------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Frontend Client**           | **Next.js 14 + PWA**              | Satu codebase responsif untuk Laptop & Mobile; performa rendering cepat dan interaksi multisensory luring.                                                   |
| **Backend Server**            | **FastAPI**                       | REST API asinkron berlatensi rendah yang ditanam di Laptop Guru untuk melayani banyak request HP siswa secara simultan.                                      |
| **AI OCR Engine**             | **TrOCR + ONNX Web**              | Model Vision-Transformer (Microsoft/trocr-base) yang dikompresi ke format ONNX agar inferensi tulisan tangan berjalan sangat ringan tanpa butuh GPU diskrit. |
| **Fuzzy Matching**            | **RapidFuzz**                     | Algoritma pencocokan kata lokal dengan efisiensi tinggi untuk toleransi kesalahan ketik ringan pada Listen Card.                                             |
| **Audio Scaffolding**         | **Python TTS Generator**          | Memproduksi petunjuk vokal luring (`gen_audio.py`) untuk memandu siswa pelosok dengan pendekatan multisensori.                                             |
| **Local Database**            | **SQLite**                        | Penyimpanan sesi, profil anak, dan rekam medis kognitif luring terpusat di server laptop kelas.                                                              |
| **Offline LLM Engine**        | **Ollama + Phi-3 / Qwen-1.5-B**   | Menjalankan Small Language Model (SLM) terkompresi secara lokal di laptop untuk mengotaki Teacher's Copilot tanpa internet.                                  |
| **Kinesthetic Tracer Engine** | **HTML5 Canvas / Pointer Events** | Menangkap koordinat, tekanan, dan stroke direction secara real-time di layar HP/Tablet tanpa membebani memori perangkat.                                     |

---

## 4. Fitur Utama & Muatan Kurikulum STEM

### A. Progressive STEM-Infused Screening (5-Level Curriculum)

Proses skrining tidak hanya menguji bahasa baku, melainkan menyuntikkan muatan literasi sains dan matematika dasar (STEM) untuk sekaligus mengakselerasi pengetahuan sains anak:

* **Level 1 (Huruf Tunggal):** Deteksi awal orientasi karakter visual (e.g., Mengenali simbol angka/huruf 'A').
* **Level 2 (Suku Kata):** Menguji penggabungan konsonan-vokal bertema alam (e.g., 'BA' pada kata Batu).
* **Level 3 (Suku Kata Kompleks):** Deteksi inversi dan omisi pada istilah sains dasar (e.g., 'BAN' pada kata Banjir).
* **Level 4-5 (Kata & Morfologi STEM):** Analisis kelancaran penulisan kata utuh sains populer (e.g., 'NYALA' pada konsep api/energi, 'MENEMANI').

### B. Interactive Listen Card (Aksen & Dialek Lokal)

Antarmuka "Dengarkan-Lalu-Tulis" yang dilengkapi dengan *audio scaffolding* lokal (`gen_audio.py`). Aplikasi memberikan jeda intuitif dan kartu berubah warna secara visual saat audio dimainkan untuk menjaga fokus anak disleksia yang mudah terdistraksi.

### C. Comprehensive Local Summary & Risk Analytics

* **Risk Score Analysis:** Memberikan klasifikasi tingkat risiko disleksia anak (Rendah, Sedang, Tinggi) berdasarkan akurasi segmentasi gambar tulisan tangan.
* **Error Pattern Recognition:** Mendeteksi kesalahan khas disleksia seperti *reversal* (huruf tertukar/terbalik seperti b/d, p/q) atau *omission* (huruf yang hilang) secara otomatis menggunakan AI lokal.
* **Learning Roadmaps:** Secara otomatis menyusun modul rekomendasi belajar adaptif intervensi mandiri bagi guru di pelosok berdasarkan *error pattern* anak.

### D. Mode Belajar Adaptif Berbasis Orton-Gillingham

* Modul intervensi dinamis (`adaptive_engine.py`) yang melatih anak membaca menggunakan kombinasi tiga sensor: penglihatan (visual), pendengaran (auditori), dan gerakan tangan/sentuhan (kinestetik) secara berulang dan terstruktur.
* **Dynamic Feedback:** Kesulitan kata akan meningkat atau menurun secara otomatis menyesuaikan kecepatan respons dan ketepatan anak saat menyelesaikan tantangan membaca offline.

### E. Teacher’s Offline AI Pedagogical Copilot (Asisten Konsultasi Guru Luring)

* **Mekanisme AI:** Memanfaatkan modul `ollama_service.py` dan `chat.py` untuk menjalankan *Small Language Model* (SLM) yang telah dikompresi di dalam server laptop guru^^.
* **Cara Kerja:** Karena di daerah 3T tidak ada psikolog atau pakar disleksia, guru sering kebingungan menghadapi anak yang memiliki pola kesalahan tertentu. Fitur ini menyediakan ruang *chatting* 100% offline^^. Guru bisa bertanya: *"Anak X di Level 3 sering membalik huruf b dan d, latihan taktil apa yang paling cocok untuk besok?"* AI lokal akan memberikan rekomendasi pedagogis berbasis metode Orton-Gillingham secara instan^^.
* **Nilai Juri SFT:** Mengubah platform yang awalnya hanya "alat tes" menjadi **"asisten guru cerdas"** yang menyelesaikan kelangkaan tenaga ahli di pelosok.

### F. Interactive Kinesthetic Tracer (Digital Whiteboard Stroke Analysis)

* **Mekanisme STEM:** Memanfaatkan modul `digital_whiteboard.py` pada antarmuka *tablet* atau *smartphone*^^.
* **Cara Kerja:** Anak disleksia tidak hanya kesulitan melihat huruf, tetapi juga bingung arah menulisnya (misal menulis huruf 'd' dimulai dari garis vertikal dulu atau lingkaran dulu). Lewat fitur papan tulis digital ini, anak diminta menebalkan huruf di layar menggunakan jari^^. AI tidak hanya menilai hasil akhir tulisan, tetapi juga menganalisis **arah tarikan garis (stroke direction)** secara  *real-time* . Jika arahnya salah, sistem akan memberikan *feedback* visual yang interaktif.
* **Nilai Juri SFT:** Sangat menonjolkan pilar *Engineering* dan *Technology* dalam STEM.

### G. Local Mesh Dashboard & Analytics (Pusat Kendali Kelas Inklusi)

* **Mekanisme Sistem:** Sinkronisasi multi-device terenkripsi berbasis Wi-Fi lokal ke pangkalan data `dyslexiai_local.db`^^.
* **Cara Kerja:** Menyediakan halaman dasbor khusus untuk guru di laptop server^^. Ketika 5 hingga 10 siswa sedang melakukan tes menggunakan HP Android secara serentak di kelas, guru dapat memantau progres, kecepatan respons, dan skor risiko masing-masing anak secara *live* dari satu layar laptop^^.
* **Nilai Juri SFT:** Memperkuat kriteria Kelayakan Implementasi. Juri melihat bahwa sistem ini sangat efisien dan siap pakai untuk skala satu kelas di sekolah pedalaman.

---

## 5. Struktur Arsitektur Kode Utama

Peta repositori aplikasi untuk memudahkan pembagian tugas tim pengembang:

```text
DyLeks/
├── BE/                           # Python FastAPI Backend (Local Server Hub)
│   ├── app/
│   │   ├── api/v1/
│   │   │   ├── screening.py      # Endpoint manajemen sesi skrining anak
│   │   │   ├── learning.py       # Endpoint mesin belajar adaptif
│   │   │   └── chat.py           # Endpoint asisten panduan guru luring
│   │   ├── models/               # ORM Skema SQLite (user, child_profile, session)
│   │   ├── schemas/              # Pydantic data validation schemas
│   │   └── services/
│   │       ├── adaptive_engine.py# Otak algoritma personalisasi tingkat kesulitan
│   │       ├── image_processor.py# Pipeline prapemrosesan gambar tulisan tangan
│   │       ├── trocr_service.py  # Model Vision-Transformer berbasis ONNX Runtime
│   │       └── ocr_service.py    # Abstraksi utilitas OCR teks luring
│   ├── gen_audio.py              # Skrip generator audio instruksi multisensori
│   ├── requirements.txt          # Dependensi dependensi Python backend
│   └── wsgi.py
│
├── FE/                           # Next.js Frontend (Multi-Device PWA Client)
│   ├── pages/
│   │   ├── index.tsx             # Halaman utama dasbor DyLeks
│   │   ├── screening.tsx         # Antarmuka ambil foto tulisan & tes anak
│   │   ├── latihan.tsx           # Antarmuka Listen Card mode multisensori
│   │   └── summary.tsx           # Visualisasi pola kesalahan dan rekomendasi guru
│   ├── public/assets/            # File audio instruksi (instruksi_ba.mp3, dsb)
│   ├── styles/                   # Glassmorphic UI/UX styling ramah anak disleksia
│   └── package.json
│
└── ML_Pipeline/                  # Repositori Pelatihan & Kompresi Model AI
    ├── notebooks/                # Eksplorasi Data Analisis (EDA) tulisan tangan anak
    └── src/
        ├── train.py              # Finetuning model TrOCR dengan dataset lokal
        └── export_onnx.py        # Skrip konversi model PyTorch ke format ringan (.onnx)

```

---

## 6. Langkah Memulai Pengembangan (Local Development Guide)

### Prasyarat Infrastruktur Kelas 3T (Simulasi):

1. Sediakan satu router Wi-Fi tanpa internet (atau aktifkan fitur *Tethering/Hotspot* dari *smartphone*).
2. Hubungkan Laptop (Server) dan *smartphone* (Client) ke jaringan Wi-Fi yang sama.

### Langkah Menjalankan Server Utama (Laptop Guru):

1. Masuk ke direktori backend: `cd BE`
2. Instal pustaka pendukung: `pip install -r requirements.txt`
3. Jalankan server FastAPI dengan mengekspos IP lokal jaringan:

```bash

```

uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload


### Tambahan untuk Fitur Teacher's Copilot (Ollama Setup):

1. Unduh dan instal Ollama di perangkat server (Laptop).
2. Jalankan model bahasa super ringan (SLM) yang dioptimasi untuk spesifikasi rendah:
   > ollama run qwen1.5:1.8b  (atau menggunakan phi3:mini)
   >
3. Pastikan konfigurasi URL Ollama pada `BE/app/core/config.py` sudah mengarah ke instans lokal tersebut.

```
   *(Catatan: Penggunaan `--host 0.0.0.0` wajib dilakukan agar server FastAPI dapat menerima koneksi dari HP pintar siswa yang terhubung dalam satu jaringan Wi-Fi lokal).*

### Langkah Menjalankan Aplikasi Klien (Mobile / Laptop Siswa):
1. Masuk ke direktori frontend: `cd FE`[cite: 1]
2. Instal dependensi node: `npm install`[cite: 1]
3. Sesuaikan konfigurasi URL dasar API klien ke alamat IP lokal server Laptop Guru.
4. Jalankan aplikasi web: `npm run dev`[cite: 1]
5. Buka browser di ponsel pintar, ketik alamat IP lokal laptop server, klik *"Add to Home Screen"* untuk menginstalnya sebagai aplikasi PWA luring murni.

```
