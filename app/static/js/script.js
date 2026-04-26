// ==========================================
// Nama File: script.js
// Deskripsi: Interaksi user dengan web (base.html)
// Penulis:   Fawwaz Yaqzhan
// Tanggal:   25-04-2026
// ==========================================

document.addEventListener('DOMContentLoaded', function() {
    const toggleBtn = document.getElementById('menu-toggle');
    const sidebar = document.getElementById('sidebar');

    toggleBtn.addEventListener('click', function() {
        sidebar.classList.toggle('collapsed');
    });
});