const btn = document.getElementById('newQuoteBtn');

btn.addEventListener('click', () => {
    fetch('/') // call Flask route
        .then(response => response.text())
        .then(html => {
            const parser = new DOMParser();
            const doc = parser.parseFromString(html, 'text/html');
            const newQuote = doc.querySelector('.quote').innerText;
            const newTimestamp = doc.querySelector('.timestamp').innerText;
            document.querySelector('.quote').innerText = newQuote;
            document.querySelector('.timestamp').innerText = newTimestamp;
        });
});
