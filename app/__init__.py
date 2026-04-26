# ==========================================
# Nama File: __init__.py
# Deskripsi: Inisialisasi aplikasi
# Penulis:   Fawwaz Yaqzhan
# Tanggal:   25-04-2026
# ==========================================

import os
from flask import Flask
from app.models import db # Import db dari models

app = Flask(__name__, instance_relative_config=True)

# 1. Tentukan base directory (lokasi folder 'app')
basedir = os.path.abspath(os.path.dirname(__file__))

# 2. Gabungkan ke folder 'instance' yang ada di luar folder 'app'
# '..' artinya naik satu tingkat ke root project, lalu masuk ke 'instance'
instance_path = os.path.join(basedir, '..', 'instance', 'database.db')

# 3. Set path absolut ke config (pastikan ada 3 atau 4 slash untuk sqlite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.normpath(instance_path)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Hubungkan db ke app
db.init_app(app)

with app.app_context():
    # Membuat tabel secara otomatis jika belum ada di folder instance
    db.create_all()

from app import routes