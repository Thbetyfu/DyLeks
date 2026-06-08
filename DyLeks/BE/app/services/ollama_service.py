"""
Teacher's Pedagogical Copilot Service.
Menangani komunikasi dengan Ollama (primary) atau Gemini (fallback)
untuk memberikan rekomendasi intervensi disleksia kepada guru.
"""

import httpx
import os
import json
from typing import Optional

class CopilotService:
    """
    AI Copilot untuk guru disleksia dengan dual-engine support.

    Alasan ('Why'):
      Guru di daerah 3T tidak memiliki akses ke psikolog anak.
      Copilot ini berperan sebagai 'konsultan pedagogis portabel' berbasis
      metode Orton-Gillingham yang bisa diakses offline via Ollama.
      Gemini digunakan sebagai fallback saat internet tersedia di lingkungan testing.
    """

    def __init__(self):
        self.ollama_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        self.ollama_model = os.getenv("OLLAMA_MODEL", "qwen2:1.5b")

        self.system_prompt = (
            "Kamu adalah 'DyLeks Copilot', asisten pedagogis AI khusus untuk guru "
            "yang menangani anak-anak dengan disleksia di sekolah dasar Indonesia, "
            "terutama di daerah 3T (Tertinggal, Terdepan, Terluar). "
            "Kamu HANYA boleh memberikan rekomendasi berdasarkan metode Orton-Gillingham "
            "yang sistematis, kumulatif, dan multisensori. "
            "Jawab dalam Bahasa Indonesia yang hangat, profesional, dan mudah dipahami guru. "
            "Jangan pernah membuat diagnosis klinis — selalu sarankan konsultasi psikolog "
            "untuk assessment formal. "
            "Berikan 2-3 aktivitas latihan konkret yang bisa dilakukan guru di kelas besok "
            "tanpa alat khusus."
        )

    def _build_prompt(self, message: str, context: Optional[dict] = None) -> str:
        """Membangun prompt lengkap dengan context skrining anak jika tersedia."""
        context_block = ""
        if context:
            child_name = context.get("child_name") or "siswa"
            risk = context.get("risk_level", "")
            level = context.get("recommended_level", "")
            errors = context.get("detected_errors", [])
            error_str = ", ".join(errors) if errors else "tidak ada pola error spesifik"
            context_block = (
                f"\n\n[DATA SKRINING ANAK]:\n"
                f"- Nama: {child_name}\n"
                f"- Tingkat risiko disleksia: {risk}\n"
                f"- Level rekomendasi kurikulum: {level}/5\n"
                f"- Pola kesalahan terdeteksi: {error_str}\n"
            )

        return f"{self.system_prompt}{context_block}\n\nGuru: {message}\nDyLeks Copilot:"

    async def get_reply(self, message: str, context: Optional[dict] = None) -> str:
        """
        Kirim pertanyaan guru ke Ollama.
        """
        full_prompt = self._build_prompt(message, context)

        # --- Ollama Lokal ---
        try:
            payload = {
                "model": self.ollama_model,
                "prompt": full_prompt,
                "stream": False
            }
            async with httpx.AsyncClient(timeout=60.0) as client:
                response = await client.post(f"{self.ollama_url}/api/generate", json=payload)
                response.raise_for_status()
                data = response.json()
                return data.get("response", "").strip()
        except Exception as ollama_err:
            print(f"[Copilot] Ollama tidak tersedia: {ollama_err}")

        return (
            "Maaf, DyLeks Copilot sedang tidak dapat dijangkau. "
            "Pastikan Ollama sudah berjalan di laptop (jalankan: ollama run qwen2:1.5b)."
        )

copilot_service = CopilotService()