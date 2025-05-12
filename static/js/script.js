// static/js/script.js
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search');
    const cafeCards = document.querySelectorAll('.card');

    searchInput.addEventListener('input', function() {
        const searchTerm = this.value.toLowerCase();
        cafeCards.forEach(card => {
            const cafeName = card.querySelector('.card-title').textContent.toLowerCase();
            const cafeLocation = card.querySelector('p').textContent.toLowerCase();
            if (cafeName.includes(searchTerm) || cafeLocation.includes(searchTerm)) {
                card.style.display = '';
            } else {
                card.style.display = 'none';
            }
        });
    });
});