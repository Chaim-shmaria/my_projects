const counterValueElement = document.getElementById('counterValue');

async function fetchCounter() {
    try {
        const response = await fetch('http://localhost:3000/api/counter');
        const data = await response.json();
        counterValueElement.textContent = data.counter;
    } catch (error) {
        console.error('Error fetching counter:', error);
    }
}

async function incrementCounter() {
    try {
        const response = await fetch('http://localhost:3000/api/counter/increment', {
            method: 'POST'
        });
        const data = await response.json();
        counterValueElement.textContent = data.counter;
    } catch (error) {
        console.error('Error incrementing counter:', error);
    }
}
