import sys
import os

# Tambahkan path BE ke sys.path agar bisa mengimpor app
sys.path.append(r"d:\4. Thoriq_KULIAH\1.Lomba Thoriq\SEMESTER 4\05. Samsung\DyLeks\BE")

try:
    from app.core.database import Base, engine
    # Impor semua model secara eksplisit
    from app.models import child_profile, exercise, screening_session
    
    print("Models loaded successfully.")
    print("Registered tables in metadata:", list(Base.metadata.tables.keys()))
    
    # Buat tabel
    Base.metadata.create_all(bind=engine)
    print("Database tables initialized.")
    
    # Cek tabel secara fisik
    import sqlite3
    conn = sqlite3.connect(r"d:\4. Thoriq_KULIAH\1.Lomba Thoriq\SEMESTER 4\05. Samsung\DyLeks\BE\dyslexiai_local.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Physical tables in SQLite:", [t[0] for t in tables])
    conn.close()
    
except Exception as e:
    import traceback
    print("ERROR:")
    traceback.print_exc()
