// 1. Helper function to redraw the queue matching your CSS
function updateQueueUI(items) {
    const container = document.getElementById('queue-display-box');
    container.innerHTML = ''; // Wipe current HTML

    if (items.length === 0) {
        container.innerHTML = '<p class="empty-text">No items in queue</p>';
        return;
    }

    // Loop through items and recreate the div structure
    items.forEach((item, index) => {
        const div = document.createElement('div');
        div.className = 'queue-item';
        // Add 1 to index because programming starts at 0, but humans count from 1
        div.textContent = `${index + 1}. ${item}`; 
        container.appendChild(div);
    });
}

// 2. Enqueue Function
async function enqueueItem() {
    const inputField = document.getElementById('queue-input');
    const value = inputField.value;

    if (!value) return; // Stop if empty

    try {
        const response = await fetch('enqueue', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ item: value })
        });

        if (response.ok) {
            const data = await response.json();
            updateQueueUI(data.queue);
            inputField.value = ''; // Clear input
            inputField.focus();    // Keep cursor in box
        }
    } catch (err) {
        console.error("Error enqueuing:", err);
    }
}

// 3. Dequeue Function
async function dequeueItem() {
    try {
        const response = await fetch('dequeue', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        });

        if (response.ok) {
            const data = await response.json();
            updateQueueUI(data.queue);
        }
    } catch (err) {
        console.error("Error dequeuing:", err);
    }
}

// 4. Clear Function
async function clearQueue() {
    try {
        const response = await fetch('clear_queue', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        });

        if (response.ok) {
            const data = await response.json();
            updateQueueUI(data.queue);
        }
    } catch (err) {
        console.error("Error clearing:", err);
    }
}

// Optional: Allow pressing "Enter" key to submit
document.getElementById('queue-input').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        enqueueItem();
    }
});