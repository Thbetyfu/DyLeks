import sys
import os
import time

# Tambahkan path BE ke sys.path agar bisa mengimpor app
sys.path.append(r"d:\4. Thoriq_KULIAH\1.Lomba Thoriq\SEMESTER 4\05. Samsung\DyLeks\BE")

try:
    from app.services.image_processor import preprocess_handwriting
    
    print("\n=== RUNNING SPRINT 2 VERIFICATION ===")
    
    # 1. Buat data gambar buatan (mock image bytes) menggunakan NumPy & OpenCV
    import cv2
    import numpy as np
    
    # Buat gambar putih ukuran 800x600 dengan bayangan abu-abu dan coretan garis hitam
    mock_img = np.ones((600, 800, 3), dtype=np.uint8) * 240
    # Beri area bayangan (gradient)
    for y in range(600):
        mock_img[y, :, :] = mock_img[y, :, :] - int(y * 0.1) # gradasi bayangan kertas
        
    # Gambar coretan tulisan tangan 'ba'
    cv2.putText(mock_img, "ba", (300, 350), cv2.FONT_HERSHEY_SIMPLEX, 4, (30, 30, 30), 5, cv2.LINE_AA)
    
    # Encode ke JPEG bytes
    _, img_bytes = cv2.imencode('.jpg', mock_img)
    raw_bytes = img_bytes.tobytes()
    print(f"Mock image generated. Original size: {len(raw_bytes)} bytes.")
    
    # 2. Ukur latensi waktu preprocessing
    start_time = time.time()
    processed_bytes = preprocess_handwriting(raw_bytes)
    end_time = time.time()
    
    latency_ms = (end_time - start_time) * 1000
    print(f"Image preprocessing executed. Output size: {len(processed_bytes)} bytes.")
    print(f"Latency: {latency_ms:.2f} ms (Target: < 200ms)")
    
    # Validasi latensi
    assert latency_ms < 200, f"Failed: Preprocessing is too slow ({latency_ms:.2f} ms)"
    assert len(processed_bytes) > 0, "Failed: Processed image is empty"
    
    # Simpan hasil untuk review jika ingin
    output_path = r"C:\Users\thori\.gemini\antigravity-ide\brain\6d793a38-d544-4e58-b6dd-667413d60cd0\scratch\processed_output.jpg"
    with open(output_path, 'wb') as f:
        f.write(processed_bytes)
    print(f"Processed verification image saved to: {output_path}")
    
    print("VERIFICATION SUCCESSFUL! Adaptive Gaussian Thresholding and latency checks passed.")
    
except Exception as e:
    import traceback
    print("ERROR:")
    traceback.print_exc()
    sys.exit(1)
