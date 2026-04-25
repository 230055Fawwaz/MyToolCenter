# ==========================================
# Nama File: routes.py
# Deskripsi: Logika URL aplikasi
# Penulis:   Fawwaz Yaqzhan
# Tanggal:   25-04-2026
# ==========================================

from flask import render_template
from app import app  # Mengimpor instance app dari package 'app'

@app.route('/')
@app.route('/dashboard')
def dashboard():
    return render_template('index.html')

@app.route('/scripts')
def scripts():
    return render_template('scripts.html')