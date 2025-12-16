// 1. UI Updater
function updateDequeUI(items) {
    const container = document.getElementById('deque-display-box');
    container.innerHTML = ''; 

    if (items.length === 0) {
        container.innerHTML = '<p class="empty-text">The deque is empty.</p>';
        return;
    }

    items.forEach((item, index) => {
        const div = document.createElement('div');
        div.className = 'queue-item';
        div.textContent = `${index + 1}. ${item}`; 
        container.appendChild(div);
    });
}

// 2. Fetch Helper (Reduces repetitive code)
async function sendRequest(url, bodyData = {}) {
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(bodyData)
        });

        if (response.ok) {
            const data = await response.json();
            updateDequeUI(data.queue);
            return true; // Success
        }
    } catch (err) {
        console.error(`Error calling ${url}:`, err);
    }
    return false; // Failure
}

// --- BUTTON ACTIONS ---

async function enqueueFront() {
    const input = document.getElementById('deque-input');
    const value = input.value;
    if (!value) return;

    // Send 'item' to match Python's expectation
    if (await sendRequest('enqueue_front', { item: value })) {
        input.value = '';
        input.focus();
    }
}

async function enqueueRear() {
    const input = document.getElementById('deque-input');
    const value = input.value;
    if (!value) return;

    if (await sendRequest('enqueue_rear', { item: value })) {
        input.value = '';
        input.focus();
    }
}

async function dequeueFront() {
    await sendRequest('dequeue_front');
}

async function dequeueRear() {
    await sendRequest('dequeue_rear');
}

async function clearDeque() {
    await sendRequest('clear_dob_queue');
}

// Optional: Pressing Enter defaults to Enqueue Rear (Standard Queue behavior)
document.getElementById('deque-input').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        enqueueRear();
    }
});