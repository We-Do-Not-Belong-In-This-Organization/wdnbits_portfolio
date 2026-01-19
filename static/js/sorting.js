// ============================
// Sorting Visualizer JS
// ============================

let speed = 300; // default speed
const arrayContainer = document.getElementById("array-container");
const numbersInput = document.getElementById("numbersInput");
const algoSelect = document.getElementById("algoSelect");
const sortButton = document.getElementById("sortButton");
const speedInput = document.getElementById("speedInput");

// Read speed from input
speedInput.addEventListener("input", () => {
    let value = parseInt(speedInput.value);

    if (isNaN(value)) return;

    // Clamp value to allowed range
    if (value < 10) value = 10;
    if (value > 1000) value = 1000;

    speed = value;
    speedInput.value = value; // ensure input shows clamped value
});

// Create bars dynamically scaled
function createBars(arr, highlightIndices = []) {
    arrayContainer.innerHTML = "";
    if (!arr || arr.length === 0) return;

    const maxVal = Math.max(...arr);
    const containerHeight = arrayContainer.clientHeight;
    const gap = 2;
    const barCount = arr.length;
    const barWidth = Math.floor((arrayContainer.clientWidth - (gap * (barCount - 1))) / barCount);

    arr.forEach((num, index) => {
        const bar = document.createElement("div");
        bar.classList.add("bar");
        bar.style.width = `${barWidth}px`;
        const scaledHeight = (num / maxVal) * containerHeight;
        bar.style.height = `${scaledHeight}px`;
        bar.style.backgroundColor = highlightIndices.includes(index) ? "#ff4d4d" : "#4a90ff";
        arrayContainer.appendChild(bar);
    });
}

// Sleep utility for animation
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// ============================
// Sorting Algorithms
// ============================

// Bubble Sort
async function bubbleSort(arr) {
    const nums = arr.slice();
    for (let i = 0; i < nums.length; i++) {
        for (let j = 0; j < nums.length - i - 1; j++) {
            if (nums[j] > nums[j + 1]) {
                [nums[j], nums[j + 1]] = [nums[j + 1], nums[j]];
            }
            createBars(nums, [j, j + 1]);
            await sleep(speed);
        }
    }
    createBars(nums);
    return nums;
}

// Insertion Sort
async function insertionSort(arr) {
    const nums = arr.slice();
    for (let i = 1; i < nums.length; i++) {
        let key = nums[i];
        let j = i - 1;
        while (j >= 0 && nums[j] > key) {
            nums[j + 1] = nums[j];
            j--;
            createBars(nums, [j + 1, i]);
            await sleep(speed);
        }
        nums[j + 1] = key;
        createBars(nums, [j + 1]);
        await sleep(speed);
    }
    return nums;
}

// Selection Sort
async function selectionSort(arr) {
    const nums = arr.slice();
    for (let i = 0; i < nums.length; i++) {
        let minIdx = i;
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[j] < nums[minIdx]) minIdx = j;
            createBars(nums, [i, j, minIdx]);
            await sleep(speed);
        }
        [nums[i], nums[minIdx]] = [nums[minIdx], nums[i]];
        createBars(nums, [i, minIdx]);
        await sleep(speed);
    }
    return nums;
}

// Merge Sort
async function mergeSort(arr) {
    const nums = arr.slice();

    async function merge(start, mid, end) {
        const left = nums.slice(start, mid);
        const right = nums.slice(mid, end);

        let i = 0, j = 0, k = start;

        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) {
                nums[k] = left[i++];
            } else {
                nums[k] = right[j++];
            }

            createBars(nums, [k]); // 🔴 overwrite position
            await sleep(speed);
            k++;
        }

        while (i < left.length) {
            nums[k] = left[i++];
            createBars(nums, [k]); // 🔴 overwrite
            await sleep(speed);
            k++;
        }

        while (j < right.length) {
            nums[k] = right[j++];
            createBars(nums, [k]); // 🔴 overwrite
            await sleep(speed);
            k++;
        }
    }

    async function mergeSortRecursive(start, end) {
        if (end - start <= 1) return;
        const mid = Math.floor((start + end) / 2);
        await mergeSortRecursive(start, mid);
        await mergeSortRecursive(mid, end);
        await merge(start, mid, end);
    }

    await mergeSortRecursive(0, nums.length);
    createBars(nums); // clear highlights
    return nums;
}

// Quick Sort
async function quickSort(arr) {
    const nums = arr.slice();

    async function partition(low, high) {
        const pivot = nums[high];
        let i = low;

        for (let j = low; j < high; j++) {
            createBars(nums, [j, high]); // 🔴 compare with pivot
            await sleep(speed);

            if (nums[j] < pivot) {
                [nums[i], nums[j]] = [nums[j], nums[i]];
                createBars(nums, [i, j]); // 🔴 swap
                await sleep(speed);
                i++;
            }
        }

        [nums[i], nums[high]] = [nums[high], nums[i]];
        createBars(nums, [i, high]); // 🔴 pivot placement
        await sleep(speed);

        return i;
    }

    async function quickSortRecursive(low, high) {
        if (low < high) {
            const p = await partition(low, high);
            await quickSortRecursive(low, p - 1);
            await quickSortRecursive(p + 1, high);
        }
    }

    await quickSortRecursive(0, nums.length - 1);
    createBars(nums); // clear highlights
    return nums;
}

// ============================
// Button click to start sorting
// ============================
sortButton.addEventListener("click", async () => {
    const input = numbersInput.value.trim();
    if (!input) return alert("Please enter numbers!");

    const numbers = input.split(/[, ]+/).map(Number);
    const algo = algoSelect.value;

    createBars(numbers); // initial state

    let sorted;
    switch (algo) {
        case "bubble": sorted = await bubbleSort(numbers); break;
        case "insertion": sorted = await insertionSort(numbers); break;
        case "selection": sorted = await selectionSort(numbers); break;
        case "merge": sorted = await mergeSort(numbers); break;
        case "quick": sorted = await quickSort(numbers); break;
    }

    // Update server-side result div
    const serverResultDiv = document.getElementById("serverResult");
    serverResultDiv.innerHTML = `
        <div style="background:#f0f0f0; padding:10px; margin-top:20px; color:black;">
            <h3>Result (${algo.charAt(0).toUpperCase() + algo.slice(1)} Sort)</h3>
            <p>${sorted.join(", ")}</p>
        </div>
    `;
});

// ============================
// Info Modal Functions
// ============================
let currentPage = 1;
const totalPages = 5;

/* ---------- MODAL CONTROL ---------- */
function openModal() {
    currentPage = 1;
    hideAllPages();
    showPage(currentPage);
    document.getElementById('infoModal').style.display = 'block';
}

function closeModal() {
    document.getElementById('infoModal').style.display = 'none';
}

/* ---------- PAGE HANDLING ---------- */
function hideAllPages() {
    for (let i = 1; i <= totalPages; i++) {
        const page = document.getElementById(`page${i}`);
        if (page) page.classList.remove('active');
    }
}

function showPage(pageNumber) {
    hideAllPages();
    const page = document.getElementById(`page${pageNumber}`);
    if (page) page.classList.add('active');

    document.getElementById('pageNumber').innerText =
        `Page ${pageNumber} of ${totalPages}`;
}

function changePage(step) {
    const nextPage = currentPage + step;

    // Stop at bounds (NO wrap)
    if (nextPage < 1 || nextPage > totalPages) {
        return;
    }

    currentPage = nextPage;
    showPage(currentPage);
}

/* ---------- CLICK OUTSIDE TO CLOSE ---------- */
window.addEventListener('click', function (event) {
    const modal = document.getElementById('infoModal');
    if (event.target === modal) {
        closeModal();
    }
});