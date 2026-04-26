# ==========================================
# Nama File: db_init.py
# Deskripsi: Inisialisasi database SQLite
# Penulis:   Fawwaz Yaqzhan
# Tanggal:   26-04-2026
# ==========================================

import sqlite3
import os

# Buat folder instance jika belum ada
if not os.path.exists('instance'):
    os.makedirs('instance')

# Hubungkan ke database (akan otomatis membuat file jika belum ada)
connection = sqlite3.connect('instance/database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

connection.commit()
connection.close()
print("Database berhasil dibuat di /instance/database.db")
