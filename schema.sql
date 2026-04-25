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
    path TEXT NOT NULL,
    description TEXT,
    status TEXT DEFAULT 'ready' -- 'ready', 'running', 'error'
);

-- Tabel Log Eksekusi
CREATE TABLE logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    script_id INTEGER,
    output TEXT,
    error TEXT,
    executed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(script_id) REFERENCES scripts(id)
);
