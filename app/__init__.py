# ==========================================
# Nama File: __init__.py
# Deskripsi: Inisialisasi aplikasi
# Penulis:   Fawwaz Yaqzhan
# Tanggal:   25-04-2026
# ==========================================

from flask import Flask

app = Flask(__name__)

# Import routes di bagian bawah untuk menghindari circular import
from app import routes