import os
import sys
import sqlite3

def get_db_path():
    # Look for database in standard BE directory relative to this script
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "BE", "dyslexiai_local.db"))

def print_summary():
    db_path = get_db_path()
    if not os.path.exists(db_path):
        print(f"[ERROR] Database file tidak ditemukan di: {db_path}")
        print("        Silakan jalankan backend FastAPI terlebih dahulu untuk membuat database.")
        return

    print(f"[INFO] Menghubungkan ke database: {db_path}")
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Get list of tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row[0] for row in cursor.fetchall()]
        
        if not tables:
            print("[WARNING] Database kosong. Tidak ada tabel yang ditemukan.")
            conn.close()
            return
            
        print("\n=== RINGKASAN TABEL DATABASE ===")
        for table in tables:
            cursor.execute(f"SELECT COUNT(*) FROM {table}")
            count = cursor.fetchone()[0]
            print(f" - {table:<30}: {count} baris data")
            
        conn.close()
    except Exception as e:
        print(f"[ERROR] Terjadi kesalahan saat membaca database: {str(e)}")

def print_profiles():
    db_path = get_db_path()
    if not os.path.exists(db_path):
        print(f"[ERROR] Database file tidak ditemukan di: {db_path}")
        return

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check if table child_profiles exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='child_profiles';")
        if not cursor.fetchone():
            print("[WARNING] Tabel 'child_profiles' belum dibuat di database.")
            conn.close()
            return
            
        cursor.execute("SELECT id, name, gender, birth_date FROM child_profiles")
        rows = cursor.fetchall()
        
        print("\n=== DAFTAR PROFIL ANAK (STUDENTS) ===")
        if not rows:
            print("Belum ada data siswa terdaftar.")
        else:
            print(f"{'ID':<5} | {'Nama Lengkap':<30} | {'Gender':<8} | {'Tanggal Lahir':<12}")
            print("-" * 65)
            for row in rows:
                gender_str = "Laki-laki" if row[2] == "M" else ("Perempuan" if row[2] == "F" else str(row[2]))
                print(f"{row[0]:<5} | {row[1]:<30} | {gender_str:<8} | {row[3]:<12}")
                
        conn.close()
    except Exception as e:
        print(f"[ERROR] Terjadi kesalahan: {str(e)}")

def print_sessions():
    db_path = get_db_path()
    if not os.path.exists(db_path):
        print(f"[ERROR] Database file tidak ditemukan.")
        return

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check if table screening_sessions exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='screening_sessions';")
        if not cursor.fetchone():
            print("[WARNING] Tabel 'screening_sessions' belum dibuat.")
            conn.close()
            return
            
        # Select session data joined with child profile
        query = """
        SELECT s.id, c.name, s.level, s.created_at
        FROM screening_sessions s
        LEFT JOIN child_profiles c ON s.child_id = c.id
        ORDER BY s.created_at DESC
        LIMIT 10
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        
        print("\n=== 10 SESI SKRINING TERAKHIR ===")
        if not rows:
            print("Belum ada riwayat sesi skrining.")
        else:
            print(f"{'Session ID':<12} | {'Nama Anak':<30} | {'Level':<5} | {'Waktu Mulai':<20}")
            print("-" * 75)
            for row in rows:
                print(f"{row[0]:<12} | {str(row[1]):<30} | {row[2]:<5} | {str(row[3]):<20}")
                
        conn.close()
    except Exception as e:
        print(f"[ERROR] Terjadi kesalahan: {str(e)}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python db_inspector.py [option]")
        print("Options:")
        print("  --summary    : Menampilkan ringkasan seluruh tabel dan baris")
        print("  --profiles   : Menampilkan daftar lengkap profil anak")
        print("  --sessions   : Menampilkan 10 sesi skrining terakhir")
        return

    option = sys.argv[1]
    if option == "--summary":
        print_summary()
    elif option == "--profiles":
        print_profiles()
    elif option == "--sessions":
        print_sessions()
    else:
        print(f"[ERROR] Pilihan '{option}' tidak dikenal.")

if __name__ == "__main__":
    main()
