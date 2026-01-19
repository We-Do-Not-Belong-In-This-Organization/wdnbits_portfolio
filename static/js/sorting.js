// ============================
// Sorting Visualizer JS
// ============================

let speed = 300; // default speed
const arrayContainer = document.getElementById("array-container");
const numbersInput = document.getElementById("numbersInput");
const algoSelect = document.getElementById("algoSelect");
const sortButton = document.getElementById("sortButton");
const speedSlider = document.getElementById("speedSlider");
const speedValue = document.getElementById("speedValue");

// Speed slider
speedSlider.addEventListener("input", () => {
    speed = parseInt(speedSlider.value);
    speedValue.innerText = `${speed}ms`;
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

    async function merge(left, right) {
        let result = [];
        while (left.length && right.length) {
            if (left[0] <= right[0]) result.push(left.shift());
            else result.push(right.shift());
            createBars([...result, ...left, ...right]);
            await sleep(speed);
        }
        return [...result, ...left, ...right];
    }

    async function mergeSortRecursive(nums) {
        if (nums.length <= 1) return nums;
        const mid = Math.floor(nums.length / 2);
        const left = await mergeSortRecursive(nums.slice(0, mid));
        const right = await mergeSortRecursive(nums.slice(mid));
        return await merge(left, right);
    }

    return await mergeSortRecursive(nums);
}

// Quick Sort
async function quickSort(arr) {
    const nums = arr.slice();

    async function quickSortRecursive(arr) {
        if (arr.length <= 1) return arr;
        const pivot = arr[0];
        const left = [];
        const right = [];
        for (let i = 1; i < arr.length; i++) {
            if (arr[i] < pivot) left.push(arr[i]);
            else right.push(arr[i]);
            createBars([...left, pivot, ...right]);
            await sleep(speed);
        }
        return [...(await quickSortRecursive(left)), pivot, ...(await quickSortRecursive(right))];
    }

    const sorted = await quickSortRecursive(nums);
    createBars(sorted);
    return sorted;
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

function openModal() {
    document.getElementById('infoModal').style.display = 'block';
}

function closeModal() {
    document.getElementById('infoModal').style.display = 'none';
}

function changePage(step) {
    document.getElementById(`page${currentPage}`).classList.remove('active');
    currentPage += step;
    if (currentPage > totalPages) currentPage = 1;
    if (currentPage < 1) currentPage = totalPages;
    document.getElementById(`page${currentPage}`).classList.add('active');
    document.getElementById('pageNumber').innerText = `Page ${currentPage} of ${totalPages}`;
}

window.onclick = function(event) {
    const modal = document.getElementById('infoModal');
    if (event.target == modal) closeModal();
};
