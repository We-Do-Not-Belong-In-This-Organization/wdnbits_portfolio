// ------------------- BINARY TREE -------------------

let selected = null;
let nodePositions = []; // {data, x, y, radius}
let currentTree = null; // store last fetched tree for animation

const canvas = document.getElementById('treeCanvas');
const ctx = canvas.getContext('2d');

canvas.width = 900;
canvas.height = 500;

// ------------------- FLOATING DOT BACKGROUND -------------------

const dotColors = ["white", "#0081f1", "#800080"];
const dotCount = 220;
let dots = [];

function initDots() {
    for (let i = 0; i < dotCount; i++) {
        dots.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            size: Math.random() * 0.5 + 1,
            speedX: (Math.random() - 0.5) * 0.4,
            speedY: (Math.random() - 0.5) * 0.4,
            color: dotColors[Math.floor(Math.random() * dotColors.length)]
        });
    }
}

function updateDots() {
    for (let d of dots) {
        d.x += d.speedX;
        d.y += d.speedY;

        // wrap around screen
        if (d.x < 0) d.x = canvas.width;
        if (d.x > canvas.width) d.x = 0;
        if (d.y < 0) d.y = canvas.height;
        if (d.y > canvas.height) d.y = 0;
    }
}

function drawDots() {
    for (let d of dots) {
        ctx.beginPath();
        ctx.arc(d.x, d.y, d.size, 0, Math.PI * 2);
        ctx.fillStyle = d.color;
        ctx.fill();
    }
}

// ------------------- ANIMATION LOOP -------------------

initDots();

function animate() {
    updateDots();

    // Draw background
    ctx.fillStyle = "black";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    drawDots();

    // Draw tree on top
    if (currentTree) {
        nodePositions = [];
        drawNode(currentTree, canvas.width / 2, 40, 200);
    }

    requestAnimationFrame(animate);
}

animate();

// ------------------- TREE FETCH + DRAW -------------------

function fetchTree() {
    fetch('/get_tree')
        .then(response => response.json())
        .then(tree => {
            currentTree = tree; // store globally
            nodePositions = [];
            drawNode(tree, canvas.width / 2, 40, 200);
            updateSelectedDisplay();
        })
        .catch(err => console.error("fetchTree error:", err));
}

function drawNode(node, x, y, spacing) {
    if (!node) return;

    const radius = 20;
    ctx.strokeStyle = "#0099ffff";
    ctx.lineWidth = 2.5;

    // Draw connecting lines first (so lines are under circles)
    if (node.left) {
        ctx.beginPath();
        ctx.moveTo(x, y + radius);
        ctx.lineTo(x - spacing, y + 100 - radius);
        ctx.stroke();
    }
    if (node.right) {
        ctx.beginPath();
        ctx.moveTo(x, y + radius);
        ctx.lineTo(x + spacing, y + 100 - radius);
        ctx.stroke();
    }

    // Draw node circle
    ctx.beginPath();
    ctx.arc(x, y, radius, 0, Math.PI * 2);
    ctx.fillStyle = (selected === node.id) ? "#ffee00ff" : "#ffffff";
    ctx.fill();
    ctx.stroke();

    // Draw text
    ctx.fillStyle = "#000000ff";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText(String(node.data), x, y);

    // Save for click detection
    nodePositions.push({ id: node.id, data: String(node.data), x, y, r: radius });

    // Recurse
    if (node.left) drawNode(node.left, x - spacing, y + 100, spacing / 1.8);
    if (node.right) drawNode(node.right, x + spacing, y + 100, spacing / 1.8);
}

// ------------------- CLICK HANDLER -------------------

canvas.addEventListener("click", function (e) {
    const rect = canvas.getBoundingClientRect();
    const mx = e.clientX - rect.left;
    const my = e.clientY - rect.top;

    for (let pos of nodePositions) {
        const dist = Math.hypot(mx - pos.x, my - pos.y);
        if (dist <= pos.r) {
            selected = pos.id;
            updateSelectedDisplay();
            fetchTree();
            return;
        }
    }

    selected = null;
    updateSelectedDisplay();
    fetchTree();
});

// ------------------- SELECTED DISPLAY -------------------

function updateSelectedDisplay() {
    if (selected === null) {
        document.getElementById("selectedDisplay").innerText = "Selected Node: None";
        return;
    }
    const node = nodePositions.find(n => n.id === selected);
    document.getElementById("selectedDisplay").innerText =
        node ? "Selected Node: " + node.data : "Selected Node: None";
}

// ------------------- TREE OPERATIONS -------------------

function insertLeft() {
    const value = document.getElementById("valueInput").value;
    if (selected === null || value.trim() === "") return alert("Select a parent and enter a value.");

    fetch("/insert_left", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ parent: selected, value })
    })
        .then(res => res.json())
        .then(res => {
            if (res.error) return alert(res.error);
            document.getElementById("valueInput").value = "";
            currentTree = res;
            drawNode(res, canvas.width / 2, 40, 200);
        });
}

function insertRight() {
    const value = document.getElementById("valueInput").value;
    if (selected === null || value.trim() === "") return alert("Select a parent and enter a value.");

    fetch("/insert_right", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ parent: selected, value })
    })
        .then(res => res.json())
        .then(res => {
            if (res.error) return alert(res.error);
            document.getElementById("valueInput").value = "";
            currentTree = res;
            drawNode(res, canvas.width / 2, 40, 200);
        });
}

function deleteNode() {
    if (!selected) return alert("Select a node to delete.");

    fetch("/delete", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ nodeId: selected })
    })
        .then(res => res.json())
        .then(tree => {
            selected = null;
            currentTree = tree;
            drawNode(tree, canvas.width / 2, 40, 200);
        });
}

function resetTree() {
    fetch("/reset", { method: "POST" })
        .then(res => res.json())
        .then(tree => {
            selected = null;
            currentTree = tree;
            drawNode(tree, canvas.width / 2, 40, 200);
        });
}

function inorderTraversal() {
    fetch("/traverse", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ type: "inorder" })
    })
        .then(res => res.json())
        .then(res => {
            document.querySelector(".traversal-display").innerHTML =
                `<p><b>In-order:</b> ${res.result}</p>`;
        });
}

function preorderTraversal() {
    fetch("/traverse", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ type: "preorder" })
    })
        .then(res => res.json())
        .then(res => {
            document.querySelector(".traversal-display").innerHTML =
                `<p><b>Pre-order:</b> ${res.result}</p>`;
        });
}

function postorderTraversal() {
    fetch("/traverse", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ type: "postorder" })
    })
        .then(res => res.json())
        .then(res => {
            document.querySelector(".traversal-display").innerHTML =
                `<p><b>Post-order:</b> ${res.result}</p>`;
        });
}

function search() {
    const value = document.getElementById("valueInput").value.trim();
    if (value === "") return alert("Please enter a value.");

    fetch("/search_node", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ value })
    })
        .then(res => res.json())
        .then(res => {
            if (res.found) {
                selected = res.id;
                updateSelectedDisplay();
                fetchTree();
            } else {
                alert(res.error);
            }
        });
}

// ------------------- INITIAL LOAD -------------------

fetchTree();
