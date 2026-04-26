// ==========================================
// Nama File: script_manager.js
// Deskripsi: Interaksi user dengan web (scripts.html)
// Penulis:   Fawwaz Yaqzhan
// Tanggal:   26-04-2026
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

function runScript(scriptId) {
    const statusSpan = document.getElementById(`status-${scriptId}`);
    
    // Ubah UI menjadi loading
    statusSpan.innerText = 'running...';
    
    fetch(`/run/${scriptId}`, { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            statusSpan.innerText = data.status;
            // Opsional: tampilkan alert sederhana jika error
            if (data.status === 'error') {
                alert(`Script gagal dijalankan (Exit Code: ${data.exit_code})`);
            }
        })
        .catch(error => {
            statusSpan.innerText = 'error';
            console.error('Fetch error:', error);
        });
}