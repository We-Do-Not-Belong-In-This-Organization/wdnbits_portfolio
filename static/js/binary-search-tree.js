// ------------------- BINARY SEARCH TREE -------------------

let selected = null;
let nodePositions = []; // {data, x, y, radius}
let currentTree = null;
let startTime = Date.now();

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

// ------------------- GRADIENT ANIMATION -------------------


// Helper to get gradient offset (always 0–1, loops smoothly)
function getGradientOffset(speed = 0.0005) { // speed = fraction per ms
    const elapsed = Date.now() - startTime;
    return (elapsed * speed) % 1; // loops from 0 → 1 continuously
}

// Create a neon gradient between two points
function getNeonGradient(x1, y1, x2, y2) {
    const grad = ctx.createLinearGradient(x1, y1, x2, y2);
    const offset1 = getGradientOffset();
    const offset2 = (offset1 + 0.5) % 1;

    grad.addColorStop(offset1, "#9900ffff");
    grad.addColorStop(offset2, "#6f00ffff");

    return grad;
}


// ------------------- TREE RENDERING & INTERACTIONS -------------------


function fetchTree() {
  fetch('/get_bstree')
    .then(response => response.json())
    .then(tree => {
      currentTree = tree;
      drawTree(tree);
    })
    .catch(err => console.error("fetchTree error:", err));
}

function drawTree(tree) {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  nodePositions = [];
  if (tree) drawNode(tree, canvas.width / 2, 40, 200);
  updateSelectedDisplay();
}

function drawNode(node, x, y, spacing) {
  if (!node) return;

  const radius = 20;

  
  // Draw connecting lines first (so lines are under circles)

  if (node.left) {
      const x2 = x - spacing;
      const y2 = y + 100 - radius;

      ctx.strokeStyle = getNeonGradient(x, y + radius, x2, y2);
      ctx.lineWidth = 3;

      // neon glow
      ctx.shadowColor = ctx.strokeStyle;
      ctx.shadowBlur = 10;

      ctx.beginPath();
      ctx.moveTo(x, y + radius);
      ctx.lineTo(x2, y2);
      ctx.stroke();

      ctx.shadowBlur = 0; // reset
  }

    if (node.right) {
        const x2 = x + spacing;
        const y2 = y + 100 - radius;

        ctx.strokeStyle = getNeonGradient(x, y + radius, x2, y2);
        ctx.lineWidth = 3;

        // neon glow
        ctx.shadowColor = ctx.strokeStyle;
        ctx.shadowBlur = 10;

        ctx.beginPath();
        ctx.moveTo(x, y + radius);
        ctx.lineTo(x2, y2);
        ctx.stroke();

        ctx.shadowBlur = 0; // reset
    }

  // Draw node circle
  ctx.beginPath();
  ctx.arc(x, y, radius, 0, Math.PI * 2);
  ctx.fillStyle = (selected === node.id) ? "#00ccffff" : "#ffffffff";
  ctx.fill();
  ctx.strokeStyle = "#9900ffff";  // separate border color
  ctx.lineWidth = 2.5;
  ctx.shadowColor = "#9900ffff";   // glow for node border
  ctx.shadowBlur = 8;
  ctx.stroke();

  // Draw text
  ctx.fillStyle = "#000000ff";
  ctx.textAlign = "center";
  ctx.textBaseline = "middle";
  ctx.fillText(String(node.data), x, y);

  // Save position for click hit-testing
  nodePositions.push({ id: node.id, data: String(node.data), x, y, r: radius });

  // Recurse to children
  if (node.left) drawNode(node.left, x - spacing, y + 100, spacing / 1.8);
  if (node.right) drawNode(node.right, x + spacing, y + 100, spacing / 1.8);
}

// single click listener (no repeated listeners)
canvas.addEventListener("click", function (e) {
  const rect = canvas.getBoundingClientRect();
  const mx = e.clientX - rect.left;
  const my = e.clientY - rect.top;

  // iterate positions to find hit (topmost first)
  for (let pos of nodePositions) {
    const dist = Math.hypot(mx - pos.x, my - pos.y);
    if (dist <= pos.r) {
      selected = pos.id;
      updateSelectedDisplay();
      fetchTree(); // re-render (to show selection)
      return;
    }
  }

  // clicked empty space -> deselect
  selected = null;
  updateSelectedDisplay();
  fetchTree();
});

function updateSelectedDisplay() {
  if (selected === null) {
    document.getElementById("selectedDisplay").innerText = "Selected Node: None";
    return;
  }

  // Find node object in nodePositions
  const node = nodePositions.find(n => n.id === selected);
  if (node) {
    document.getElementById("selectedDisplay").innerText = "Selected Node: " + node.data;
  } else {
    document.getElementById("selectedDisplay").innerText = "Selected Node: None";
  }
}



function insertNode() {
  const value = document.getElementById("valueInput").value.trim();
  if (value === "") return alert("Enter a value to insert.");

  // Easter egg: show an image if value is 1987
  if (value === "1987") {
    const canvas = document.getElementById("treeCanvas");
    const ctx = canvas.getContext("2d");

    const img = new Image();
    img.src = "/static/images/ruzzel_creepy_pasta.jpg"; // put your image in static/images
    img.onload = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
    };
    return; // stop further insertion
  }

  fetch("/insert", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ value })
  })
  .then(res => res.json())
  .then(res => {
    if (res.error) return alert(res.error);
    document.getElementById("valueInput").value = "";
    currentTree = res;
    drawTree(res);
  })
  .catch(err => console.error("insert error:", err));
}


function deleteNode() {
  const value = document.getElementById("valueInput").value.trim();
  if (value === "") return alert("Enter a value to delete.");

  fetch("/delete_bst", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ value })
  })
  .then(res => res.json())
  .then(tree => {
    document.getElementById("valueInput").value = "";
    currentTree = tree;
    drawTree(tree);
  })
  .catch(err => console.error("delete error:", err));
}



function resetTree() {
  fetch("/reset_bst", { method: "POST" })
    .then(res => res.json())
    .then(tree => {
      selected = null;
      currentTree = tree;
      drawTree(tree);
    })
    .catch(err => console.error("resetTree error:", err));
}

function inorderTraversal() {
  fetch("/traverse_bst", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ type: "inorder" })
  })
    .then(res => res.json())
    .then(res => {
      if (res.error) return alert(res.error);
      document.querySelector(".traversal-display").innerHTML =
        `<p><b>In-order:</b> ${res.result}</p>`;
    });
}

function preorderTraversal() {
  fetch("/traverse_bst", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ type: "preorder" })
  })
    .then(res => res.json())
    .then(res => {
      if (res.error) return alert(res.error);
      document.querySelector(".traversal-display").innerHTML =
        `<p><b>Pre-order:</b> ${res.result}</p>`;
    });
}

function postorderTraversal() {
  fetch("/traverse_bst", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ type: "postorder" })
  })
    .then(res => res.json())
    .then(res => {
      if (res.error) return alert(res.error);
      document.querySelector(".traversal-display").innerHTML =
        `<p><b>Post-order:</b> ${res.result}</p>`;
    });
}


function search() {
    const value = document.getElementById("valueInput").value.trim();
    if (value === "") return alert("Please enter a value.");

    fetch("/search_bst", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ value })
    })
    .then(res => res.json())
    .then(res => {
        if (res.found) {
            selected = res.id;       // highlight the found node
            updateSelectedDisplay();
            fetchTree();             // redraw tree to show highlight
        } else {
            alert(res.error);        // node not found
        }
    })
    .catch(err => console.error("search error:", err));
}



// INITIAL LOAD
fetchTree();
