import sys
import os
import json

# Tambahkan path BE ke sys.path agar bisa mengimpor app
sys.path.append(r"d:\4. Thoriq_KULIAH\1.Lomba Thoriq\SEMESTER 4\05. Samsung\DyLeks\BE")

try:
    from app.core.database import SessionLocal
    from app.models.exercise import Exercise
    
    db = SessionLocal()
    
    # Bersihkan data lama agar tidak duplikat saat seeding ulang
    db.query(Exercise).delete()
    db.commit()
    
    # 1. Soal Level 1: Huruf Vokal Tunggal (10 soal)
    l1_exercises = [
        Exercise(level=1, type="auditory", content={"text": "Huruf apakah aku?", "audio_url": "audio_a.mp3", "options": ["A", "I", "U", "E", "O"]}, correct_answer="A"),
        Exercise(level=1, type="auditory", content={"text": "Huruf apakah aku?", "audio_url": "audio_i.mp3", "options": ["A", "I", "U", "E", "O"]}, correct_answer="I"),
        Exercise(level=1, type="auditory", content={"text": "Huruf apakah aku?", "audio_url": "audio_u.mp3", "options": ["A", "I", "U", "E", "O"]}, correct_answer="U"),
        Exercise(level=1, type="auditory", content={"text": "Huruf apakah aku?", "audio_url": "audio_e.mp3", "options": ["A", "I", "U", "E", "O"]}, correct_answer="E"),
        Exercise(level=1, type="auditory", content={"text": "Huruf apakah aku?", "audio_url": "audio_o.mp3", "options": ["A", "I", "U", "E", "O"]}, correct_answer="O"),
        Exercise(level=1, type="visual", content={"text": "Tebak huruf vokal besar ini", "options": ["A", "B", "C", "D"]}, correct_answer="A"),
        Exercise(level=1, type="visual", content={"text": "Tebak huruf vokal kecil ini", "options": ["i", "j", "l", "t"]}, correct_answer="i"),
        Exercise(level=1, type="visual", content={"text": "Tebak huruf vokal besar ini", "options": ["U", "V", "W", "X"]}, correct_answer="U"),
        Exercise(level=1, type="visual", content={"text": "Tebak huruf vokal besar ini", "options": ["E", "F", "G", "H"]}, correct_answer="E"),
        Exercise(level=1, type="visual", content={"text": "Tebak huruf vokal besar ini", "options": ["O", "Q", "D", "P"]}, correct_answer="O"),
    ]
    
    # 2. Soal Level 2: Suku Kata Dasar (10 soal)
    l2_exercises = [
        Exercise(level=2, type="visual", content={"text": "Kata apakah aku?", "options": ["BUKU", "MAMA", "IBU", "BOLA"]}, correct_answer="BUKU"),
        Exercise(level=2, type="visual", content={"text": "Kata apakah aku?", "options": ["BUKU", "MAMA", "IBU", "BOLA"]}, correct_answer="MAMA"),
        Exercise(level=2, type="visual", content={"text": "Kata apakah aku?", "options": ["BUKU", "MAMA", "IBU", "BOLA"]}, correct_answer="IBU"),
        Exercise(level=2, type="visual", content={"text": "Kata apakah aku?", "options": ["BUKU", "MAMA", "IBU", "BOLA"]}, correct_answer="BOLA"),
        Exercise(level=2, type="visual", content={"text": "Kata apakah aku?", "options": ["BUKU", "MAMA", "IBU", "BATU"]}, correct_answer="BATU"),
        Exercise(level=2, type="visual", content={"text": "Kata apakah aku?", "options": ["SAPI", "KERA", "KUDA", "BABI"]}, correct_answer="SAPI"),
        Exercise(level=2, type="visual", content={"text": "Kata apakah aku?", "options": ["SAPI", "KERA", "KUDA", "BABI"]}, correct_answer="KERA"),
        Exercise(level=2, type="visual", content={"text": "Kata apakah aku?", "options": ["SAPI", "KERA", "KUDA", "BABI"]}, correct_answer="KUDA"),
        Exercise(level=2, type="visual", content={"text": "Kata apakah aku?", "options": ["PITA", "JALA", "TOPI", "SEPATU"]}, correct_answer="PITA"),
        Exercise(level=2, type="visual", content={"text": "Kata apakah aku?", "options": ["PITA", "JALA", "TOPI", "SEPATU"]}, correct_answer="JALA"),
    ]
    
    # 3. Soal Level 3: Suku Kata Kompleks (10 soal)
    l3_exercises = [
        Exercise(level=3, type="writing", content={"text": "Kata apakah aku?", "options": ["BAN", "BUS", "CAT", "MOBIL"]}, correct_answer="BAN"),
        Exercise(level=3, type="writing", content={"text": "Kata apakah aku?", "options": ["BAN", "BUS", "CAT", "MOBIL"]}, correct_answer="BUS"),
        Exercise(level=3, type="writing", content={"text": "Kata apakah aku?", "options": ["BAN", "BUS", "CAT", "MOBIL"]}, correct_answer="CAT"),
        Exercise(level=3, type="writing", content={"text": "Kata apakah aku?", "options": ["BAN", "BUS", "CAT", "MOBIL"]}, correct_answer="MOBIL"),
        Exercise(level=3, type="writing", content={"text": "Kata apakah aku?", "options": ["BAN", "BUS", "CAT", "KAPAL"]}, correct_answer="KAPAL"),
        Exercise(level=3, type="writing", content={"text": "Kata apakah aku?", "options": ["PISANG", "NANGKA", "APEL", "JERUK"]}, correct_answer="PISANG"),
        Exercise(level=3, type="writing", content={"text": "Kata apakah aku?", "options": ["PISANG", "NANGKA", "APEL", "JERUK"]}, correct_answer="NANGKA"),
        Exercise(level=3, type="writing", content={"text": "Kata apakah aku?", "options": ["PISANG", "NANGKA", "APEL", "JERUK"]}, correct_answer="APEL"),
        Exercise(level=3, type="writing", content={"text": "Kata apakah aku?", "options": ["BUNGA", "POHON", "DAUN", "RANTING"]}, correct_answer="BUNGA"),
        Exercise(level=3, type="writing", content={"text": "Kata apakah aku?", "options": ["BUNGA", "POHON", "DAUN", "RANTING"]}, correct_answer="POHON"),
    ]
    
    db.add_all(l1_exercises + l2_exercises + l3_exercises)
    db.commit()
    
    print("SUCCESS: 30 exercises successfully seeded to SQLite.")
    db.close()
    
except Exception as e:
    import traceback
    print("ERROR:")
    traceback.print_exc()
