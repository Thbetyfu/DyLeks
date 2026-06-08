"""
Child Profile Model Definition.

Alasan ('Why'):
  ChildProfile adalah entitas inti DyLeks — setiap profil mewakili satu anak
  yang sedang dievaluasi. Dengan adanya foreign key 'teacher_id', sistem
  memastikan isolasi data antar guru secara struktural di level database,
  bukan hanya di level aplikasi. Ini adalah desain Privacy-First.
"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.core.database import Base


class ChildProfile(Base):
    """
    Profil anak yang dikaitkan dengan satu guru (teacher).
    Satu Guru (User) -> Banyak ChildProfile (One-to-Many).
    """
    __tablename__ = "child_profiles"

    id = Column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        index=True,
    )

    # Kepemilikan: Foreign Key ke tabel users (Guru)
    teacher_id = Column(
        String(36),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=True,  # nullable=True untuk kompatibilitas backward dengan data lama (Anonymous Mode)
        index=True,
    )

    # Data Dasar Anak
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=True)
    gender = Column(String(10), nullable=True)  # "L" atau "P"
    grade = Column(String(20), nullable=True)   # Contoh: "Kelas 2 SD"

    # Status Belajar & Risiko
    current_level = Column(Integer, default=1)       # Level saat ini (1-5)
    risk_score = Column(Float, default=0.0)          # Skor risiko terakhir (0-100)
    risk_level = Column(String(20), default="Belum Dianalisis")  # Rendah/Sedang/Tinggi

    # Catatan Pedagogi (opsional dari guru)
    teacher_notes = Column(Text, nullable=True)

    # Timestamp
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relasi ke riwayat sesi belajar dan skrining
    learning_sessions = relationship("LearningSession", backref="child", lazy=True)
    screening_sessions = relationship("ScreeningSession", backref="child", lazy=True)
