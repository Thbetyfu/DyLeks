"""
Auth & User Management API Router.

Alasan ('Why'):
  Router ini adalah gerbang pertama DyLeks. Ia mengelola:
  1. Registrasi Guru baru ke server lokal (POST /register).
  2. Login Guru dan penerbitan session token (POST /login).
  3. CRUD profil anak di bawah kepemilikan Guru yang sedang login.

  Desain 'teacher_id-centric': Setiap operasi CRUD pada ChildProfile
  diisolasi menggunakan teacher_id dari session token, bukan dari parameter URL.
  Ini mencegah guru A mengakses data siswa milik guru B secara tidak sengaja.
"""
from fastapi import APIRouter, HTTPException, Depends, Header
from sqlalchemy.orm import Session
from typing import Optional

from app.core.database import get_db
from app.models.user import User
from app.models.child_profile import ChildProfile
from app.schemas.user_schema import (
    UserCreate, UserLogin, UserResponse,
    ChildProfileCreate, ChildProfileResponse
)
from app.services.auth_service import (
    hash_password, verify_password,
    create_session_token, decode_session_token
)

router = APIRouter()


# ============================================================
# DEPENDENCY: Ekstrak user_id dari header Authorization
# ============================================================
def get_current_teacher(
    authorization: Optional[str] = Header(None),
    db: Session = Depends(get_db)
) -> User:
    """
    Dependency untuk melindungi endpoint yang butuh autentikasi.
    Membaca token dari header 'Authorization: Bearer <token>'.

    Alasan ('Why'):
      Menggunakan Header Authorization adalah standar REST API.
      Frontend cukup menyimpan token di localStorage dan menyertakannya
      di setiap request ke protected endpoint.
    """
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token autentikasi tidak ditemukan.")

    token = authorization.removeprefix("Bearer ").strip()
    payload = decode_session_token(token)

    if not payload:
        raise HTTPException(status_code=401, detail="Token tidak valid atau sudah kadaluarsa.")

    user = db.query(User).filter(User.id == payload["user_id"]).first()
    if not user or not user.is_active:
        raise HTTPException(status_code=401, detail="Akun guru tidak ditemukan atau tidak aktif.")

    return user


# ============================================================
# AUTH ENDPOINTS
# ============================================================

@router.post("/register", response_model=UserResponse, status_code=201)
def register_teacher(payload: UserCreate, db: Session = Depends(get_db)):
    """
    Mendaftarkan Guru baru ke server lokal DyLeks.
    Username harus unik dalam satu instans server.
    """
    existing = db.query(User).filter(User.username == payload.username).first()
    if existing:
        raise HTTPException(
            status_code=409,
            detail=f"Username '{payload.username}' sudah digunakan. Pilih username lain."
        )

    new_user = User(
        full_name=payload.full_name,
        username=payload.username,
        hashed_password=hash_password(payload.password),
        school_name=payload.school_name,
        school_region=payload.school_region,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/login")
def login_teacher(payload: UserLogin, db: Session = Depends(get_db)):
    """
    Login Guru dan mengembalikan session token.
    Token disimpan di sisi FE dan digunakan untuk request berikutnya.
    """
    user = db.query(User).filter(User.username == payload.username).first()
    if not user or not verify_password(payload.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Username atau password salah.")

    if not user.is_active:
        raise HTTPException(status_code=403, detail="Akun tidak aktif. Hubungi administrator.")

    # Update last_login timestamp
    from datetime import datetime
    user.last_login = datetime.utcnow()
    db.commit()

    token = create_session_token(user.id)
    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "full_name": user.full_name,
            "username": user.username,
            "school_name": user.school_name,
        }
    }


# ============================================================
# CHILD PROFILE ENDPOINTS (Protected - Butuh Login Guru)
# ============================================================

@router.post("/children", response_model=ChildProfileResponse, status_code=201)
def create_child_profile(
    payload: ChildProfileCreate,
    db: Session = Depends(get_db),
    current_teacher: User = Depends(get_current_teacher)
):
    """
    Menambahkan profil siswa baru di bawah kepemilikan Guru yang sedang login.
    teacher_id di-set otomatis dari session — Guru tidak perlu menginputnya.
    """
    child = ChildProfile(
        teacher_id=current_teacher.id,
        name=payload.name,
        age=payload.age,
        gender=payload.gender,
        grade=payload.grade,
        teacher_notes=payload.teacher_notes,
    )
    db.add(child)
    db.commit()
    db.refresh(child)
    return child


@router.get("/children", response_model=list[ChildProfileResponse])
def list_children(
    db: Session = Depends(get_db),
    current_teacher: User = Depends(get_current_teacher)
):
    """
    Mengambil daftar SEMUA siswa milik Guru yang sedang login.
    Tidak bisa mengakses siswa milik guru lain.
    """
    children = db.query(ChildProfile).filter(
        ChildProfile.teacher_id == current_teacher.id
    ).all()
    return children


@router.get("/children/{child_id}", response_model=ChildProfileResponse)
def get_child_profile(
    child_id: str,
    db: Session = Depends(get_db),
    current_teacher: User = Depends(get_current_teacher)
):
    """
    Mengambil detail profil satu siswa — hanya jika siswa tersebut milik guru yang login.
    """
    child = db.query(ChildProfile).filter(
        ChildProfile.id == child_id,
        ChildProfile.teacher_id == current_teacher.id
    ).first()

    if not child:
        raise HTTPException(
            status_code=404,
            detail="Profil siswa tidak ditemukan atau bukan milik Anda."
        )
    return child


@router.patch("/children/{child_id}", response_model=ChildProfileResponse)
def update_child_profile(
    child_id: str,
    payload: ChildProfileCreate,
    db: Session = Depends(get_db),
    current_teacher: User = Depends(get_current_teacher)
):
    """
    Memperbarui data profil siswa (nama, usia, catatan guru, dll).
    """
    child = db.query(ChildProfile).filter(
        ChildProfile.id == child_id,
        ChildProfile.teacher_id == current_teacher.id
    ).first()

    if not child:
        raise HTTPException(status_code=404, detail="Profil siswa tidak ditemukan.")

    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(child, field, value)

    db.commit()
    db.refresh(child)
    return child


@router.delete("/children/{child_id}", status_code=204)
def delete_child_profile(
    child_id: str,
    db: Session = Depends(get_db),
    current_teacher: User = Depends(get_current_teacher)
):
    """
    Menghapus profil siswa beserta seluruh riwayat sesinya (cascade delete).
    """
    child = db.query(ChildProfile).filter(
        ChildProfile.id == child_id,
        ChildProfile.teacher_id == current_teacher.id
    ).first()

    if not child:
        raise HTTPException(status_code=404, detail="Profil siswa tidak ditemukan.")

    db.delete(child)
    db.commit()
