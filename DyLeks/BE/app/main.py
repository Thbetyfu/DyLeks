from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import engine, Base
from app.api.v1 import screening, chat, learning, auth

# Load all models explicitly before creating tables
# URUTAN IMPORT PENTING: User harus di-load sebelum ChildProfile
# karena ChildProfile memiliki ForeignKey ke tabel users.
from app.models import user, child_profile, exercise, screening_session

# Inisialisasi Database: Membuat semua tabel yang belum ada
# (termasuk tabel 'users' yang baru ditambahkan)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="DyslexiAI Backend API",
    description=(
        "API untuk platform deteksi dini disleksia DyLeks. "
        "Berjalan 100% offline di jaringan Wi-Fi lokal kelas."
    ),
    version="1.2.0"
)

# CORS: Mengizinkan akses dari semua origin untuk jaringan lokal kelas.
# Di lingkungan produksi sekolah, ganti "*" dengan IP spesifik laptop server.
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrasi Router
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth & User Management"])
app.include_router(screening.router, prefix="/api/v1/screening", tags=["Screening Mode"])
app.include_router(chat.router, prefix="/api/v1/chat", tags=["AI Tutor Chat"])
app.include_router(learning.router, prefix="/api/v1/learning", tags=["Learning Mode"])

@app.on_event("startup")
async def startup_event():
    from app.services.trocr_service import get_trocr_engine
    print("[Startup] Menyiapkan Otak AI (TrOCR)...")
    get_trocr_engine()
    print("[Startup] Otak AI Siap!")

@app.get("/")
def read_root():
    return {
        "status": "ok",
        "version": "1.2.0",
        "message": "DyslexiAI API is running. Auth system aktif.",
    }
