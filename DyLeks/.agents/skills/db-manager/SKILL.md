---
name: db-manager
description: Memantau dan memeriksa database SQLite lokal (dyslexiai_local.db) untuk DyLeks.
---

# db-manager (SQLite Local Database Manager)

Skill ini digunakan untuk mengontrol, menginspeksi, dan memeriksa status data luring di database SQLite (`dyslexiai_local.db`) milik DyLeks.

## Database Location

Database SQLite tersimpan di direktori backend:
`BE/dyslexiai_local.db`

## Menggunakan SQLite DB Inspector CLI

Kami telah menyediakan skrip pembantu `db_inspector.py` untuk menginspeksi tabel database secara interaktif lewat terminal.

1. Buka folder script: `cd .agents/skills/db-manager/scripts`
2. Jalankan tool:

```bash
python db_inspector.py --summary
```

Atau untuk menampilkan semua data profil anak:

```bash
python db_inspector.py --profiles
```

## Daftar Tabel Utama

- `users`: Data guru atau administrator sekolah.
- `child_profiles`: Data profil anak yang diuji (nama, tanggal lahir, sekolah, dll).
- `screening_sessions`: Riwayat sesi skrining tulisan tangan anak.
- `exercise_progress`: Riwayat latihan multisensori / Listen Card anak.
- `risk_assessments`: Hasil kalkulasi tingkat risiko disleksia (Rendah/Sedang/Tinggi).
- `indonesian_phonogram_matrix`: Pemetaan tingkat kesulitan fonem bahasa Indonesia (Fase Orton-Gillingham).

## Melakukan Kueri Manual via Terminal

Jika Anda ingin memeriksa database secara manual via SQLite CLI:

```bash
sqlite3 BE/dyslexiai_local.db
```

Kueri SQL populer:
- `.tables` (melihat semua tabel)
- `.schema child_profiles` (melihat skema tabel profil anak)
- `SELECT * FROM child_profiles;` (melihat daftar siswa terdaftar)
