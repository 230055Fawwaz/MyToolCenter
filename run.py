# ==========================================
# Nama File: run.py
# Deskripsi: Entry point aplikasi (Tombol power server Flask)
# Penulis:   Fawwaz Yaqzhan
# Tanggal:   25-04-2026
# ==========================================

from app import app

if __name__ == "__main__":
    # Menjalankan aplikasi dalam mode debug
    app.run(debug=True)