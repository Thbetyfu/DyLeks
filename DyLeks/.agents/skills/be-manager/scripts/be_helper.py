import os
import sys
import socket
import subprocess

def check_port(port):
    """Check if a port is in use."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('127.0.0.1', port)) == 0

def check_db():
    """Verify if SQLite database exists and report its size."""
    db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "BE", "dyslexiai_local.db"))
    if os.path.exists(db_path):
        size = os.path.getsize(db_path)
        print(f"[SUCCESS] Database SQLite ditemukan di: {db_path}")
        print(f"          Ukuran File: {size / 1024:.2f} KB")
        return True
    else:
        print(f"[WARNING] Database SQLite belum terinisialisasi di: {db_path}")
        print(f"          Database akan otomatis terbuat saat backend FastAPI dijalankan.")
        return False

def run_tests():
    """Run pytest in the BE directory."""
    be_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "BE"))
    print(f"\n--- MENJALANKAN UNIT TEST DI: {be_dir} ---")
    try:
        # Run pytest
        result = subprocess.run([sys.executable, "-m", "pytest"], cwd=be_dir, capture_output=False, text=True)
        if result.returncode == 0:
            print("[SUCCESS] Semua unit test berhasil lolos!")
        else:
            print(f"[FAILED] pytest keluar dengan kode error: {result.returncode}")
    except Exception as e:
        print(f"[ERROR] Gagal menjalankan pytest: {str(e)}")

def main():
    print("====================================================")
    print("       DyLeks Backend Helper Tool v1.0              ")
    print("====================================================")
    
    # 1. Check SQLite DB
    check_db()
    
    # 2. Check Port 3002
    port = 3002
    is_in_use = check_port(port)
    if is_in_use:
        print(f"[WARNING] Port {port} sedang digunakan oleh proses lain!")
        print("          Pastikan Anda mematikan server backend sebelumnya jika ingin restart.")
    else:
        print(f"[SUCCESS] Port {port} bebas dan siap digunakan.")
    
    # 3. Check arguments for running tests
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        run_tests()

if __name__ == "__main__":
    main()
