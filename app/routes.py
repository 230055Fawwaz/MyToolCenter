# ==========================================
# Nama File: routes.py
# Deskripsi: Logika URL aplikasi
# Penulis:   Fawwaz Yaqzhan
# Tanggal:   25-04-2026
# ==========================================

from flask import render_template, jsonify
from app import app
from app.models import db, Script, Log # Ambil db dari sini

@app.route('/')
@app.route('/dashboard')
def dashboard():
    return render_template('index.html')

@app.route('/scripts')
def scripts():
    # Sekarang Script sudah punya context app
    all_scripts = Script.query.all() 
    return render_template('scripts.html', scripts=all_scripts)