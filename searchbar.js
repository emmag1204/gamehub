function searchFunction() {
    const searchQuery = document.getElementById('searchInput').value;
    const resultDiv = document.getElementById('results');

    if (searchQuery) {
        resultDiv.dispatchEvent.innerHTML = 'You searched for: <strong>${searchQuery}</strong?';
    } else {
        resultDiv.innerHTML = 'Please enter a search term.';
    }
}