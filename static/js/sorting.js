// ============================
// DOM Elements
// ============================
const arrayContainer = document.getElementById('array-container');
const sortButton = document.getElementById('sortButton');
const numbersInput = document.getElementById('numbersInput');
const algoSelect = document.getElementById('algoSelect');
const speedInput = document.getElementById('speedInput');

let delay = 300; 
let maxValGlobal = 1; 

// ============================
// Helper Functions
// ============================
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// Get the height for bars, leaving room for the numbers at the bottom/top
function getUsableHeight() {
    return arrayContainer.clientHeight - 30; 
}

// Create bars dynamically
function createBars(numbers) {
    arrayContainer.innerHTML = '';
    maxValGlobal = Math.max(...numbers, 1);

    const usableH = getUsableHeight();
    const containerWidth = arrayContainer.clientWidth;

    const gap = 2; 
    const barWidth = Math.floor((containerWidth - (numbers.length - 1) * gap) / numbers.length);

    numbers.forEach(num => {
        const bar = document.createElement('div');
        bar.classList.add('bar');
        bar.style.width = `${barWidth}px`;
        bar.style.marginRight = `${gap}px`;
        bar.style.height = `${(num / maxValGlobal) * usableH}px`;

        const span = document.createElement('span');
        span.textContent = num;
        bar.appendChild(span);

        arrayContainer.appendChild(bar);
    });
}

// Highlight bars
function highlightBars(indices, color) {
    const bars = arrayContainer.querySelectorAll('.bar');
    indices.forEach(i => {
        if (bars[i]) bars[i].style.backgroundColor = color;
    });
}

// Reset bar colors
function resetBars() {
    const bars = arrayContainer.querySelectorAll('.bar');
    bars.forEach(bar => bar.style.backgroundColor = '#00e5ff');
}

// ============================
// Sorting Algorithms
// ============================

async function bubbleSort(numbers) {
    const bars = arrayContainer.querySelectorAll('.bar');
    const n = numbers.length;
    const usableH = getUsableHeight();

    for (let i = 0; i < n - 1; i++) {
        for (let j = 0; j < n - i - 1; j++) {
            highlightBars([j, j + 1], '#ff4d4d');
            await sleep(delay);

            if (numbers[j] > numbers[j + 1]) {
                [numbers[j], numbers[j + 1]] = [numbers[j + 1], numbers[j]];

                bars[j].style.height = `${(numbers[j] / maxValGlobal) * usableH}px`;
                bars[j].querySelector('span').textContent = numbers[j];

                bars[j + 1].style.height = `${(numbers[j + 1] / maxValGlobal) * usableH}px`;
                bars[j + 1].querySelector('span').textContent = numbers[j + 1];
            }
            resetBars();
        }
    }
}

async function insertionSort(numbers) {
    const bars = arrayContainer.querySelectorAll('.bar');
    const usableH = getUsableHeight();

    for (let i = 1; i < numbers.length; i++) {
        let key = numbers[i];
        let j = i - 1;

        while (j >= 0 && numbers[j] > key) {
            highlightBars([j, j + 1], '#ff4d4d');
            await sleep(delay);

            numbers[j + 1] = numbers[j];
            bars[j + 1].style.height = `${(numbers[j + 1] / maxValGlobal) * usableH}px`;
            bars[j + 1].querySelector('span').textContent = numbers[j + 1];

            resetBars();
            j--;
        }

        numbers[j + 1] = key;
        bars[j + 1].style.height = `${(key / maxValGlobal) * usableH}px`;
        bars[j + 1].querySelector('span').textContent = key;
    }
}

async function selectionSort(numbers) {
    const bars = arrayContainer.querySelectorAll('.bar');
    const usableH = getUsableHeight();

    for (let i = 0; i < numbers.length; i++) {
        let minIdx = i;
        for (let j = i + 1; j < numbers.length; j++) {
            highlightBars([minIdx, j], '#ff4d4d');
            await sleep(delay);
            if (numbers[j] < numbers[minIdx]) minIdx = j;
            resetBars();
        }

        if (minIdx !== i) {
            [numbers[i], numbers[minIdx]] = [numbers[minIdx], numbers[i]];
            bars[i].style.height = `${(numbers[i] / maxValGlobal) * usableH}px`;
            bars[i].querySelector('span').textContent = numbers[i];
            bars[minIdx].style.height = `${(numbers[minIdx] / maxValGlobal) * usableH}px`;
            bars[minIdx].querySelector('span').textContent = numbers[minIdx];
        }
    }
}

async function mergeSort(numbers, start = 0, end = numbers.length - 1) {
    const bars = arrayContainer.querySelectorAll('.bar');
    const usableH = getUsableHeight();
    if (start >= end) return;

    const mid = Math.floor((start + end) / 2);
    await mergeSort(numbers, start, mid);
    await mergeSort(numbers, mid + 1, end);

    let left = numbers.slice(start, mid + 1);
    let right = numbers.slice(mid + 1, end + 1);
    let i = start, li = 0, ri = 0;

    while (li < left.length && ri < right.length) {
        highlightBars([i], '#ff4d4d');
        await sleep(delay);
        if (left[li] <= right[ri]) {
            numbers[i] = left[li++];
        } else {
            numbers[i] = right[ri++];
        }
        bars[i].style.height = `${(numbers[i] / maxValGlobal) * usableH}px`;
        bars[i].querySelector('span').textContent = numbers[i];
        resetBars();
        i++;
    }
    while (li < left.length) {
        numbers[i] = left[li++];
        bars[i].style.height = `${(numbers[i] / maxValGlobal) * usableH}px`;
        bars[i].querySelector('span').textContent = numbers[i];
        i++;
    }
    while (ri < right.length) {
        numbers[i] = right[ri++];
        bars[i].style.height = `${(numbers[i] / maxValGlobal) * usableH}px`;
        bars[i].querySelector('span').textContent = numbers[i];
        i++;
    }
}

async function quickSort(numbers, low = 0, high = numbers.length - 1) {
    if (low < high) {
        const pi = await partition(numbers, low, high);
        await quickSort(numbers, low, pi - 1);
        await quickSort(numbers, pi + 1, high);
    }
}

async function partition(numbers, low, high) {
    const bars = arrayContainer.querySelectorAll('.bar');
    const usableH = getUsableHeight();
    const pivot = numbers[high];
    let i = low - 1;

    for (let j = low; j < high; j++) {
        highlightBars([j, high], '#ff4d4d');
        await sleep(delay);
        if (numbers[j] < pivot) {
            i++;
            [numbers[i], numbers[j]] = [numbers[j], numbers[i]];
            bars[i].style.height = `${(numbers[i] / maxValGlobal) * usableH}px`;
            bars[i].querySelector('span').textContent = numbers[i];
            bars[j].style.height = `${(numbers[j] / maxValGlobal) * usableH}px`;
            bars[j].querySelector('span').textContent = numbers[j];
        }
        resetBars();
    }
    [numbers[i + 1], numbers[high]] = [numbers[high], numbers[i + 1]];
    bars[i + 1].style.height = `${(numbers[i + 1] / maxValGlobal) * usableH}px`;
    bars[i + 1].querySelector('span').textContent = numbers[i + 1];
    bars[high].style.height = `${(numbers[high] / maxValGlobal) * usableH}px`;
    bars[high].querySelector('span').textContent = numbers[high];
    return i + 1;
}

// ============================
// Event Listeners
// ============================
sortButton.addEventListener('click', async () => {
    const values = numbersInput.value.split(',')
        .map(x => parseInt(x.trim()))
        .filter(x => !isNaN(x));

    if (!values.length) return;

    createBars(values);
    const inputDelay = parseInt(speedInput.value);
    delay = (inputDelay >= 10 && inputDelay <= 1000) ? inputDelay : 300;

    const algo = algoSelect.value;
    switch(algo) {
        case 'bubble': await bubbleSort(values); break;
        case 'insertion': await insertionSort(values); break;
        case 'selection': await selectionSort(values); break;
        case 'merge': await mergeSort(values); break;
        case 'quick': await quickSort(values); break;
    }
    resetBars();

    const resultContainer = document.getElementById('serverResult');
    resultContainer.innerHTML = `<div><h3>Result (${algo.toUpperCase()} Sort)</h3><p>${values.join(', ')}</p></div>`;
});

// Resizing support
window.addEventListener('resize', () => {
    const values = numbersInput.value.split(',').map(x => parseInt(x.trim())).filter(x => !isNaN(x));
    if (values.length) createBars(values);
});

// ============================
// Modal Controls (Keep your original logic)
// ============================
const infoModal = document.getElementById('infoModal');
const pageNumberText = document.getElementById('pageNumber');
let currentPage = 1;
const totalPages = 5;

function openModal() { infoModal.style.display = 'block'; showPage(currentPage); }
function closeModal() { infoModal.style.display = 'none'; }
function changePage(delta) {
    currentPage = Math.max(1, Math.min(totalPages, currentPage + delta));
    showPage(currentPage);
}
function showPage(page) {
    const pages = document.querySelectorAll('.info-page');
    pages.forEach((p, i) => p.classList.toggle('active', i === page - 1));
    pageNumberText.textContent = `Page ${page} of ${totalPages}`;
}
window.addEventListener('click', (e) => { if (e.target === infoModal) closeModal(); });