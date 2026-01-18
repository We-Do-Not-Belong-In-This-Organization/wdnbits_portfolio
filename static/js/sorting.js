// static/js/sorting-info.js
let currentPage = 1;
const totalPages = 5;

function openModal() {
    document.getElementById('infoModal').style.display = 'block';
}

function closeModal() {
    document.getElementById('infoModal').style.display = 'none';
}

function changePage(step) {
    // Hide current page
    document.getElementById(`page${currentPage}`).classList.remove('active');
    
    // Calculate next page
    currentPage += step;
    if (currentPage > totalPages) currentPage = 1;
    if (currentPage < 1) currentPage = totalPages;
    
    // Show new page
    document.getElementById(`page${currentPage}`).classList.add('active');
    document.getElementById('pageNumber').innerText = `Page ${currentPage} of ${totalPages}`;
}

// Close modal if user clicks outside the box
window.onclick = function(event) {
    let modal = document.getElementById('infoModal');
    if (event.target == modal) {
        closeModal();
    }
}