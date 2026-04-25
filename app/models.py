# ==========================================
# Nama File: models.py
# Deskripsi: Penerapan skema SQLite
# Penulis:   Fawwaz Yaqzhan
# Tanggal:   25-04-2026
# ==========================================

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Script(db.Model):
    __tablename__ = 'scripts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50)) # Contoh: 'Data Handling', 'Maintenance'
    path = db.Column(db.String(255), nullable=False) # Lokasi file .bat/.ps1
    description = db.Column(db.String(255))
    status = db.Column(db.String(20), default='ready')
    
    # Relationship untuk mempermudah pemanggilan logs dari objek script
    logs = db.relationship('Log', backref='script', lazy=True)

class Log(db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer, primary_key=True)
    script_id = db.Column(db.Integer, db.ForeignKey('scripts.id'), nullable=False)
    output = db.Column(db.Text)
    error = db.Column(db.Text)
    executed_at = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f'<Log {self.id} for Script {self.script_id}>'