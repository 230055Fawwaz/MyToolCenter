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
    statusSpan.innerText = "Running...";

    fetch(`/run-script/${scriptId}`, { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            if (data.status === "success") {
                statusSpan.innerText = "Success";
                alert("Output: " + data.output);
            } else {
                statusSpan.innerText = "Error";
                alert("Error: " + data.message);
            }
        })
        .catch(err => {
            statusSpan.innerText = "Error";
            console.error(err);
        });
}