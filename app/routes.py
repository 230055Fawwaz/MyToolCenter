# ==========================================
# Nama File: routes.py
# Deskripsi: Logika URL aplikasi
# Penulis:   Fawwaz Yaqzhan
# Tanggal:   25-04-2026
# ==========================================

import subprocess
import os
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

@app.route('/run-script/<int:script_id>', methods=['POST'])
def run_script(script_id):
    script = Script.query.get_or_404(script_id)
    
    # Cek apakah file fisik ada
    if not os.path.exists(script.path):
        return jsonify({"status": "error", "message": "File skrip tidak ditemukan!"}), 404

    try:
        # Menentukan command berdasarkan tipe file
        if script.type == ".bat":
            command = [script.path]
        elif script.type == ".ps1":
            command = ["powershell.exe", "-ExecutionPolicy", "Bypass", "-File", script.path]
        else:
            return jsonify({"status": "error", "message": "Tipe file tidak didukung"}), 400

        # Eksekusi skrip
        result = subprocess.run(command, capture_output=True, text=True, shell=True)

        # Simpan log ke database
        new_log = Log(
            script_id=script.id,
            exit_code=result.returncode,
            output=result.stdout,
            error=result.stderr
        )
        db.session.add(new_log)
        db.session.commit()

        return jsonify({
            "status": "success",
            "output": result.stdout,
            "error": result.stderr
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500