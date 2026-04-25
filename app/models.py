# ==========================================
# Nama File: models.py
# Deskripsi: Penerapan skema SQLite
# Penulis:   Fawwaz Yaqzhan
# Tanggal:   25-04-2026
# ==========================================

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Model Skema Daftar Skrip
class Script(db.Model):
    __tablename__ = 'scripts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50))
    type = db.Column(db.String(10), nullable=False)
    path = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255))
    status = db.Column(db.String(20), default='ready')
    
    logs = db.relationship('Log', backref='script', lazy=True)

# Model Skema Log Eksekusi
class Log(db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer, primary_key=True)
    script_id = db.Column(db.Integer, db.ForeignKey('scripts.id'), nullable=False)
    exit_code = db.Column(db.Integer)
    duration = db.Column(db.Float)
    output = db.Column(db.Text)
    error = db.Column(db.Text)
    executed_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Log {self.id} for Script {self.script_id} (Code: {self.exit_code})>'