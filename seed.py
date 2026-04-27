# ==========================================
# Nama File: seed.py
# Deskripsi: File pengisi data awal
# Penulis:   Fawwaz Yaqzhan
# Tanggal:   27-04-2026
# ==========================================

import os
from app import app, db
from app.models import Script

# 1. Tentukan lokasi folder proyek (MyToolCenter)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# 2. Naik satu tingkat ke folder 'Tool Center'
TOOL_CENTER_DIR = os.path.dirname(BASE_DIR)

# 3. Tentukan path ke folder skrip eksternal
BATCH_DIR = os.path.join(TOOL_CENTER_DIR, 'batch')
PS1_DIR = os.path.join(TOOL_CENTER_DIR, 'ps1')

# Pastikan foldernya ada secara fisik (opsional, tapi disarankan)
for folder in [BATCH_DIR, PS1_DIR]:
    if not os.path.exists(folder):
        os.makedirs(folder)

def seed_data():
    with app.app_context():
        if Script.query.count() == 0:
            # Contoh File .bat di folder batch
            bat_path = os.path.join(BATCH_DIR, "hello.bat")
            
            # Buat file fisik hello.bat jika belum ada (untuk testing)
            if not os.path.exists(bat_path):
                with open(bat_path, "w") as f:
                    f.write("@echo off\necho Hello World dari folder batch!")

            hello_bat = Script(
                name="Hello Batch",
                category="Testing",
                type=".bat", 
                path=bat_path,
                description="Skrip Hello World dari folder batch.",
                status="ready"
            )
            
            db.session.add(hello_bat)
            db.session.commit()
            print(f"Seed Berhasil! Path: {bat_path}")
        else:
            print("Data sudah ada.")

if __name__ == '__main__':
    seed_data()
