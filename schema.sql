-- ==========================================
-- Nama File: schema.sql
-- Deskripsi: Skema database SQLite
-- Penulis:   Fawwaz Yaqzhan
-- Tanggal:   25-04-2026
-- ==========================================

-- Tabel Daftar Skrip
CREATE TABLE scripts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    type TEXT NOT NULL,
    path TEXT NOT NULL,
    description TEXT,
    status TEXT DEFAULT 'ready'
);

-- Tabel Log Eksekusi
CREATE TABLE logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    script_id INTEGER,
    exit_code INTEGER,
    duration REAL,
    output TEXT,
    error TEXT,
    executed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(script_id) REFERENCES scripts(id)
);