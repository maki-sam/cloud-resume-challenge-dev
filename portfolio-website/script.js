// script.js
async function fetchViews(retries = 3) {
    const viewsElement = document.getElementById('views');
    viewsElement.textContent = 'Loading...';

    try {
        const response = await fetch('https://m4bectfanfnhk4zuoc7uvlc7eu0akqpq.lambda-url.ap-southeast-1.on.aws/');
        if (!response.ok) {
            throw new Error(`Network response was not ok: ${response.statusText}`);
        }
        const data = await response.json();
        viewsElement.textContent = data.views;
    } catch (error) {
        console.error('Error fetching views:', error);
        if (retries > 0) {
            console.log(`Retrying... (${retries} attempts left)`);
            setTimeout(() => fetchViews(retries - 1), 1000);
        } else {
            viewsElement.textContent = 'Error fetching views';
        }
    }
}

document.addEventListener('DOMContentLoaded', fetchViews);