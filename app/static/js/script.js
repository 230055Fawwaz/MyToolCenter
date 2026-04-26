// ==========================================
// Nama File: script.js
// Deskripsi: Interaksi user dengan web
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

// ==========================================
// Scripts.html
// ==========================================

document.addEventListener('DOMContentLoaded', () => {
    const addCardBtn = document.getElementById('addCardBtn');
    const cardGrid = document.getElementById('cardGrid');
    let counter = 1;

    addCardBtn.addEventListener('click', () => {
        const cardTitle = `Custom Script #${counter++}`;
        
        // Buat elemen card
        const newCard = document.createElement('div');
        newCard.className = 'script-card';
        
        newCard.innerHTML = `
            <h4>${cardTitle}</h4>
            <p>Script baru yang ditambahkan secara dinamis ke dalam daftar.</p>
        `;
        
        cardGrid.appendChild(newCard);
    });
});