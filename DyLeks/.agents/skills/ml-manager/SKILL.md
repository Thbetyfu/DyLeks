---
name: ml-manager
description: Mengelola ML Pipeline, ekspor model TrOCR ke format ONNX, dan validasi kuantisasi model AI.
---

# ml-manager (Machine Learning Pipeline Manager)

Skill ini digunakan untuk mengelola pipeline pembelajaran mesin, memicu ekspor model Vision-Transformer TrOCR ke ONNX, serta menguji performa kuantisasi model agar di bawah 100MB untuk kebutuhan luring di daerah 3T.

## Setup & Dependensi ML

Sebelum melakukan ekspor model, pastikan dependensi Hugging Face, Optimum, dan ONNX Runtime terpasang:

```bash
pip install optimum[onnxruntime] transformers onnxruntime-quantization
```

## Mengekspor Model TrOCR ke ONNX & Kuantisasi INT8

Model `microsoft/trocr-base-handwritten` digunakan untuk mengenali tulisan tangan anak disleksia. Karena laptop guru di daerah 3T berspesifikasi rendah, model harus dikompresi menggunakan kuantisasi INT8 dinamis.

Jalankan skrip ekspor:

```bash
cd ML_Pipeline/src
python export_onnx.py
```

## Hasil Ekspor Model

Model yang berhasil diekspor akan tersimpan di:
- `ML_Pipeline/src/onnx_model/`
- Berkas model utama terkompresi: `model_quantized.onnx` (~100MB)

## Struktur Direktori ML Pipeline

- `ML_Pipeline/notebooks/`: File eksplorasi data analisis tulisan tangan anak.
- `ML_Pipeline/src/train.py`: Skrip untuk fine-tuning model TrOCR dengan data lokal Indonesia.
- `ML_Pipeline/src/export_onnx.py`: Skrip utama ekspor dan kuantisasi model ONNX.
- `BE/app/services/image_processor.py`: Pipeline image-processing (resize ke 384x384, Otsu binarization, deskewing) sebelum diumpankan ke model ONNX.
