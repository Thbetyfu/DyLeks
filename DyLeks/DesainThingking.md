
# Desain Thinking

## 1. Panduan & Hasil Wawancara (User Interview Insights)

**Target Stakeholder:** Guru SD di Wilayah 3T & Orang Tua Murid

**Pertanyaan Pemantik Utama**
- Bagaimana Ibu/Bapak mengidentifikasi siswa yang tertinggal dalam membaca atau sering menulis terbalik?
- Fasilitas apa saja yang tersedia jika ada anak yang terindikasi membutuhkan perhatian khusus?

**Kutipan Wawancara Nyata (Insights)**
> **Guru (Ibu Rahma):** "Kami sering menganggap anak yang menulis terbalik atau tidak bisa mengeja itu malas belajar atau kurang bimbingan orang tua. Kami tidak punya instrumen tes psikologi sama sekali di sini, dan akses ke kota kabupaten sangat jauh dan mahal."

> **Orang Tua (Pak Joko):** "Anak saya sering menangis kalau disuruh sekolah karena merasa tidak bisa mengeja seperti teman-temannya. Kami tidak tahu harus meminta bantuan ke siapa karena di puskesmas pelosok pun tidak ada ahli saraf atau psikolog anak."

---

## 2. Klasifikasi Data (Primer, Sekunder, Tersier)

**Data Primer**
- Transkrip wawancara langsung dan observasi lapangan terhadap guru dan anak-anak di SD wilayah 3T.
- Data telemetri trajektori sensor kinematik (akselerasi & rotasi) dari unit Smart Writing Grip (ESP32 + MPU6050).
- Hasil pengujian inferensi lokal model Vision-Transformer (TrOCR) yang dikonversi ke ONNX pada laptop berspesifikasi rendah.

**Data Sekunder**
- Estimasi Asosiasi Disleksia Indonesia: ~5 juta anak disleksia di Indonesia, >80% tidak terdeteksi dini.
- Literatur mengenai efektivitas metode multisensori Orton-Gillingham.

**Data Tersier**
- Laporan Kemdikbud tentang peta infrastruktur digital di area tertinggal.
- Jurnal tentang spesifikasi rata-rata komputer BOS di daerah pelosok.

---

## 3. Empathy Map (Peta Empati)

> *Catatan:* istilah yang benar adalah *Empathy Map* (Peta Empati).

**Says (Kata-kata pengguna)**
- "Anak ini sepertinya tidak punya masa depan karena membaca saja tidak bisa."
- "Gawai kami tidak punya kuota internet untuk membuka aplikasi belajar daring."

**Thinks (Pikiran pengguna)**
- Apakah anak saya bodoh, atau saya yang gagal mendidiknya?
- Mengapa fasilitas inklusi hanya tersedia di sekolah premium di kota?

**Does (Perilaku pengguna)**
- Memaksa anak menghafal huruf secara berulang dengan metode konvensional.
- Membiarkan anak tertinggal tanpa intervensi terstruktur.

**Feels (Perasaan pengguna)**
- Frustrasi, cemas, dan hilangnya kepercayaan diri pada anak.
- Terisolasi dari keuntungan EdTech karena keterbatasan infrastruktur.

**Pains (Kesulitan utama)**
- Biaya diagnosis formal, ketiadaan internet, minimnya perangkat yang mumpuni.

**Gains (Harapan/Keuntungan)**
- Alat skrining gratis, 100% offline, dan panduan intervensi mudah dijalankan oleh guru awam.

---

## 4. POV (Point of View)

**User:** Guru SD dan anak berkebutuhan khusus (disleksia/disgrafia) di wilayah 3T.

**Need:** Instrumen deteksi dini valid dan modul intervensi ramah perangkat berspesifikasi rendah, bisa dijalankan tanpa internet.

**Insight:** Tanpa diagnosis dini yang inklusif, anak disleksia di daerah terpencil berisiko mendapat label negatif yang menutupi potensi sebenarnya.

---

## 5. User Persona

**Ibu Rahma, 34 Tahun — Guru SD Negeri Pelosok (Wilayah 3T)**

**Profil & Bio:** Mengajar 8 tahun, berdedikasi tetapi terbatas fasilitas.

**Perangkat yang digunakan:** Laptop inventaris sekolah lawas; smartphone Android anggaran rendah.

**Frustrasi utama**
- Tidak memiliki keahlian inklusi untuk mendiagnosis.
- Aplikasi EdTech saat ini membutuhkan koneksi internet.

**Goals:** Memiliki asisten cerdas lokal di kelas yang bisa memetakan kesulitan membaca dan memberikan panduan latihan hibrida (kertas + gawai) luring.

---

## 6. Value Proposition Canvas (VPC)

### A. Customer Profile (Anak & Guru 3T)

**Customer Jobs**
- Memetakan kemampuan membaca siswa.
- Melatih perkembangan motorik halus.
- Menyusun materi intervensi literasi dasar.

**Pains**
- Biaya kuota mahal / sinyal nihil.
- Laptop sekolah sering lag.
- Stigma negatif terhadap anak lambat belajar.

**Gains**
- Penanganan yang tepat, pembelajaran tanpa stres, administrasi perkembangan yang mudah.

### B. Value Map (Solusi DyLeks)

**Products & Services**
- PWA luring (Next.js) + FastAPI lokal, terintegrasi dengan Smart Writing Grip (ESP32).

**Pain Relievers**
- Operasi 100% offline melalui local mesh hotspot.
- Model TrOCR dikompresi ke ONNX agar ringan untuk laptop tua.
- Tatakan taktil lokal (Sandbox Companion) untuk menggantikan perangkat mahal.

**Gain Creators**
- Teacher's Offline AI Copilot (SLM lokal via Ollama).
- Analisis otomatis pola reversal untuk rencana belajar personal.

---

## 7. Brainwriting (6-3-5 Ideation Matrix)

**Tim dan fokus**
- Hacker 1 (Thoriq) — AI & Jaringan
- Hacker 2 (Karov) — Hardware
- Hipster (Casta) — UI/UX & Taktil

**Ronde 1: Skrining**
- Pipa inferensi TrOCR lokal (ONNX Runtime Web).
- Sirkuit grip pensil (ESP32 + MPU6050) nirkabel.
- UI Next.js dengan kontras warna ramah disleksia.

**Ronde 2: Intervensi**
- ollama_service.py untuk konsultasi guru (SLM lokal).
- Transmisi data pergerakan menulis via MQTT lokal.
- Metode Trace–Copy–Cover–Close (TCCC) interaktif.

**Ronde 3: Lokalisasi**
- Skema SQLite `dyslexiai_local.db` untuk matriks fonogram Bahasa Indonesia.
- Integrasi sensor GSR untuk memantau stres.
- Media taktil pasir lokal sebagai Sandbox Companion.

---

## 8. Impact Canvas (Impact vs Effort Matrix)

**Quick wins (High impact, Low effort)**
- Implementasi Next.js PWA lintas platform.
- Pemanfaatan media taktil kasar lokal.
- Skema DB lokal berbasis SQLite untuk fonogram.

**Major projects (High impact, High effort)**
- Kompresi model TrOCR ke ONNX luring.
- Kalibrasi data sensor IMU ESP32 → FastAPI.
- Finetuning SLM Ollama lokal.

**Additional initiatives**
- Modul generator audio TTS luring (Low effort / Medium impact).
- Pengembangan casing grip pensil via 3D printing (High effort).

---

## 9. SMART KPI (Smart Formula)

- **Specific:** Implementasi ekosistem DyLeks (PWA, laptop server, Smart Writing Grip) untuk deteksi dini dan intervensi mandiri.
- **Measurable:** Skrining luring ≥ 500 anak; akurasi klasifikasi reversal ≥ 85%.
- **Achievable:** Menjalankan pada laptop inventaris sekolah; biaya hardware ≤ Rp150.000/unit.
- **Relevant:** Menjawab tema Education Samsung SFT 2026 — pemerataan AI inklusif.
- **Time-bound:** Hardware, kompresi model, & uji lapangan di 10 SD selesai dalam 6 bulan.

---

## 10. Business Model Canvas (BMC)

**Key Partners**
- Dinas Pendidikan Daerah (3T)
- Asosiasi Disleksia Indonesia
- Komunitas Guru Penggerak Pelosok
- Lab manufaktur kampus (cetak 3D casing)

**Key Activities**
- Pemeliharaan algoritma Edge-AI (`trocr_service.py`).
- Perakitan & kalibrasi hardware ESP32.
- Pelatihan Orton-Gillingham untuk guru.

**Value Propositions**
- Ekosistem EdTech inklusif 100% offline.
- Diagnosis siber-fisik (citra kertas + telemetri kinematik).
- Asisten konsultasi guru luring berbasis SLM lokal.

**Customer Relationships**
- Pelatihan luring (Train the Trainer).
- Local Mesh Dashboard untuk monitoring kelas.

**Customer Segments**
- Primary: Anak SD (6–12 tahun) di wilayah 3T.
- Secondary: Guru SD & orang tua di pelosok.

**Key Resources**
- Repositori kode (Next.js, FastAPI, ONNX Runtime).
- Skema database fonogram Indonesia.
- Desain open-source Smart Writing Grip.

**Channels**
- Distribusi installer offline via USB.
- Workshop guru daerah tertinggal.

**Cost Structure**
- Komponen hardware (ESP32, MPU6050, filament 3D).
- Logistik & pelatihan.
- R&D optimasi model AI lokal.

**Revenue Streams / Sustainability**
- Hibah (Samsung SFT), CSR, atau integrasi anggaran BOS.

---

*File diformat ulang untuk keterbacaan; beri tahu jika mau penyesuaian gaya atau penambahan tabel.*
