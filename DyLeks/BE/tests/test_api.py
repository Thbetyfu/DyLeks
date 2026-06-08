import os
import sys
import pytest
from fastapi.testclient import TestClient
import base64

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/docs")
    assert response.status_code == 200

def test_upload_screening_empty_base64():
    # Test validasi input kosong
    response = client.post("/api/v1/screening/upload", json={
        "image_base64": "",
        "target_letter": "A"
    })
    assert response.status_code == 400
    assert "Data gambar tidak terdeteksi" in response.json()["detail"]

def test_upload_screening_invalid_base64():
    # Test bagaimana backend merespon base64 yang bukan gambar (misal teks biasa)
    # Ini harus ditangani dan tidak membuat server crash
    response = client.post("/api/v1/screening/upload", json={
        "image_base64": "data:image/jpeg;base64,aW52YWxpZF9pbWFnZV9ieXRlcw==",
        "target_letter": "A"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    # Karena gagal baca gambar, TrOCR akan mengembalikan skor 50 dan errors "Kesalahan internal mesin TrOCR"
    assert "Kesalahan internal mesin TrOCR" in data["detected_errors"][0]
    assert data["risk_score"] == 50.0

def test_get_exercises():
    # Test endpoint latihan adaptif
    response = client.get("/api/v1/learning/get-exercises/1")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "content" in data[0]
