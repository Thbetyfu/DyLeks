---
name: be-manager
description: Mengelola backend FastAPI server, running unit tests, dan instalasi dependensi Python untuk DyLeks.
---

# be-manager (Backend FastAPI Manager)

Skill ini digunakan untuk mengelola, menjalankan, memantau, dan menguji backend FastAPI server dari aplikasi DyLeks.

## Setup & Dependensi

Pastikan python environment sudah aktif dan dependensi terpasang:
1. Pindah ke direktori backend: `cd BE`
2. Instal pustaka pendukung: `pip install -r requirements.txt`

## Menjalankan Backend Server

Untuk menjalankan backend FastAPI secara offline di jaringan lokal kelas (menggunakan port 3002):

```bash
python wsgi.py
# atau jika ingin hot-reload untuk development:
uvicorn app.main:app --host 0.0.0.0 --port 3002 --reload
```

> [!NOTE]
> Parameter `--host 0.0.0.0` sangat penting agar server FastAPI dapat diakses oleh perangkat client (smartphone/tablet siswa) yang terhubung dalam satu jaringan Wi-Fi lokal kelas (simulasi daerah 3T).

## Menjalankan Unit Test

Untuk memverifikasi integrasi backend, database, dan logika algoritma adaptif:

```bash
cd BE
pytest
```

## Struktur File Backend Utama

- `app/main.py`: Titik masuk utama aplikasi FastAPI, inisialisasi database SQLite.
- `app/api/v1/`: Endpoint REST API untuk `screening.py`, `learning.py`, dan `chat.py`.
- `app/services/`:
  - `adaptive_engine.py`: Mengelola Orton-Gillingham Spaced-Repetition.
  - `scoring_service.py`: Mengolah metrik dan menghitung skor risiko disleksia.
  - `trocr_service.py`: Wrapper ONNX Runtime untuk deteksi tulisan tangan.
  - `mqtt_handler.py`: Subscriber MQTT untuk Smart Writing Grip.
