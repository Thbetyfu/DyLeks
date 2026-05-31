"""
TrOCR ONNX Exporter and Quantization Script.
Mengekspor model PyTorch TrOCR dari Hugging Face ke format ONNX 
dan melakukan kuantisasi INT8 dinamis agar ringan dijalankan di laptop 3T.
"""
import os
import sys

def main():
    print("=== TrOCR ONNX Exporter ===")
    
    # 1. Pastikan dependensi terpasang
    try:
        import optimum
        from optimum.onnxruntime import ORTModelForVision2Seq
        from transformers import TrOCRProcessor
        from onnxruntime.quantization import quantize_dynamic, QuantType
    except ImportError:
        print("[Error] Pustaka pendukung ('optimum', 'transformers', 'onnxruntime') belum terpasang.")
        print("Silakan jalankan: pip install optimum[onnxruntime] transformers")
        sys.exit(1)

    model_id = "microsoft/trocr-base-handwritten"
    output_dir = "onnx_model/"
    quantized_model_path = "onnx_model/model_quantized.onnx"

    print(f"1. Mengekspor '{model_id}' ke format ONNX...")
    try:
        # Load and export model
        model = ORTModelForVision2Seq.from_pretrained(model_id, export=True)
        processor = TrOCRProcessor.from_pretrained(model_id)

        # Save model and processor locally
        model.save_pretrained(output_dir)
        processor.save_pretrained(output_dir)
        print(f"[Sukses] Model ONNX berhasil disimpan di folder: {output_dir}")
        
    except Exception as e:
        print(f"[Gagal] Proses ekspor model gagal: {str(e)}")
        sys.exit(1)

    # 2. Lakukan Kuantisasi INT8 Dinamis untuk memangkas memori
    print("\n2. Melakukan Kuantisasi INT8 Dinamis pada model ONNX...")
    original_model_path = os.path.join(output_dir, "model.onnx")
    
    if not os.path.exists(original_model_path):
        # Cari file .onnx di dalam direktori output
        onnx_files = [f for f in os.listdir(output_dir) if f.endswith(".onnx")]
        if onnx_files:
            original_model_path = os.path.join(output_dir, onnx_files[0])
            quantized_model_path = os.path.join(output_dir, onnx_files[0].replace(".onnx", "_quantized.onnx"))
        else:
            print("[Error] Berkas model.onnx tidak ditemukan untuk proses kuantisasi.")
            sys.exit(1)

    try:
        quantize_dynamic(
            model_input=original_model_path,
            model_output=quantized_model_path,
            weight_type=QuantType.QUInt8
        )
        print(f"[Sukses] Model terkuantisasi berhasil disimpan di: {quantized_model_path}")
        
        # Cetak perbandingan ukuran file
        orig_size = os.path.getsize(original_model_path) / (1024 * 1024)
        quant_size = os.path.getsize(quantized_model_path) / (1024 * 1024)
        print(f"  - Ukuran Asli: {orig_size:.2f} MB")
        print(f"  - Ukuran Kuantisasi: {quant_size:.2f} MB (Terkompresi ~{(1 - quant_size/orig_size)*100:.1f}%)")

    except Exception as e:
        print(f"[Gagal] Proses kuantisasi gagal: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
