document.addEventListener("DOMContentLoaded", () => {

  // ------------------- PRESS ANY BUTTON -------------------
  const startButton = document.getElementById("startButton");
  const body = document.body;

  function startGame() {
    body.classList.add("zoom-fade");
    startButton.style.display = "none";
    setTimeout(() => {
      window.location.href = "/profile";
    }, 1400);
  }

  if (startButton) {
    startButton.addEventListener("click", startGame);
    document.addEventListener("keydown", startGame); // any key also works
  }

// ------------------- PROFILE HOVER SIDE IMAGES -------------------
const characters = document.querySelectorAll(".character");
const grid = document.querySelector(".grid");

characters.forEach(char => {
  let leftImg, rightImg;

  char.addEventListener("mouseenter", () => {
    if (!grid) return;

    if (leftImg) leftImg.remove();
    if (rightImg) rightImg.remove();

    leftImg = document.createElement("img");
    leftImg.src = `/static/images/${char.dataset.left}`;
    leftImg.className = "side-image left-side";

    rightImg = document.createElement("img");
    rightImg.src = `/static/images/${char.dataset.right}`;
    rightImg.className = "side-image right-side";

    grid.appendChild(leftImg);
    grid.appendChild(rightImg);

    requestAnimationFrame(() => {
      leftImg.classList.add("show");
      rightImg.classList.add("show");
    });
  });

  char.addEventListener("mouseleave", () => {
    if (!leftImg || !rightImg) return;

    leftImg.classList.remove("show");
    rightImg.classList.remove("show");

    setTimeout(() => {
      leftImg.remove();
      rightImg.remove();
    }, 500);
  });
});
  // ------------------- LOADING SCREEN -------------------
const loadingScreen = document.querySelector('.loading-screen');
if (loadingScreen) {
  setTimeout(() => {
    loadingScreen.classList.add('hidden');
    setTimeout(() => loadingScreen.remove(), 1000);
  }, 2000);
}
const tips = [
  'The "WDNBITS" name was founded by Jayvee',
  "If you're reading this, tag your tropa!",
  "Hassan is the youngest in the WDNBITS group",
  "Eh naglapag ng tips",
  "Some tips are randomly given!",
  "Si Jed ay Bass Player",
  "Si Matt ay may 7 dogs",
  "Tag mo yung tropa mo!",
  ".--- .- -. ....... .-. ..- --.. --..\n . .-.. .-.. ....... --- .-. --.- ..- .. .-",
  "3-I",
];

// Picks a random phrase
const randomTip = tips[Math.floor(Math.random() * tips.length)];

// Displayer CAPITAL P, Powerful to!
document.getElementById("randText").textContent = randomTip;
});

// ------------------- QUEUE PAGE ENQUEUE ANIMATION -------------------
const queueBox = document.querySelector('.queue-box');
if (queueBox) {
  queueBox.scrollTop = queueBox.scrollHeight;
}

// Auto-scroll deque box to bottom on page load
window.addEventListener('load', () => {
    const dequeBox = document.querySelector('.queue-box');
    if (dequeBox) {
        dequeBox.scrollTop = dequeBox.scrollHeight;
    }
});

// ------------------- BINARY TREE -------------------

let selected = null;
let nodePositions = []; // {data, x, y, radius}

const canvas = document.getElementById('treeCanvas');
const ctx = canvas.getContext('2d');

canvas.width = 900;
canvas.height = 500;

function fetchTree() {
  fetch('/get_tree')
    .then(response => response.json())
    .then(tree => {
      console.log("TREE RECEIVED:", tree);
      drawTree(tree);
    })
    .catch(err => console.error("fetchTree error:", err));
}

function drawTree(tree) {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  nodePositions = [];
  if (tree) drawNode(tree, canvas.width / 2, 40, 150);
  updateSelectedDisplay();
}

function drawNode(node, x, y, spacing) {
  if (!node) return;

  const radius = 20;

  // Draw connecting lines first (so lines are under circles)
  if (node.left) {
    ctx.beginPath();
    ctx.moveTo(x, y + radius);
    ctx.lineTo(x - spacing, y + 80 - radius);
    ctx.stroke();
  }
  if (node.right) {
    ctx.beginPath();
    ctx.moveTo(x, y + radius);
    ctx.lineTo(x + spacing, y + 80 - radius);
    ctx.stroke();
  }

  // Draw node circle
  ctx.beginPath();
  ctx.arc(x, y, radius, 0, Math.PI * 2);
  ctx.fillStyle = (selected === node.id) ? "#ffaa55" : "#ffffff";
  ctx.fill();
  ctx.stroke();

  // Draw text
  ctx.fillStyle = "#000000";
  ctx.textAlign = "center";
  ctx.textBaseline = "middle";
  ctx.fillText(String(node.data), x, y);

  // Save position for click hit-testing
  nodePositions.push({ id: node.id, data: String(node.data), x, y, r: radius });

  // Recurse to children
  if (node.left) drawNode(node.left, x - spacing, y + 80, spacing / 1.8);
  if (node.right) drawNode(node.right, x + spacing, y + 80, spacing / 1.8);
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
  document.getElementById("selectedDisplay").innerText =
    "Selected Node ID: " + (selected ?? "None");
}

function insertLeft() {
  const value = document.getElementById("valueInput").value;
  if (!selected || !value) return alert("Select a parent and enter a value.");

  fetch("/insert_left", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ parent: selected, value})
  })
    .then(res => res.json())
    .then(tree => {
      document.getElementById("valueInput").value = "";
      drawTree(tree);
    })
    .catch(err => console.error("insertLeft error:", err));
}

function insertRight() {
  const value = document.getElementById("valueInput").value;
  if (!selected || !value) return alert("Select a parent and enter a value.");

  fetch("/insert_right", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ parent: selected, value})
  })
    .then(res => res.json())
    .then(tree => {
      document.getElementById("valueInput").value = "";
      drawTree(tree);
    })
    .catch(err => console.error("insertRight error:", err));
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
      drawTree(tree);
    })
    .catch(err => console.error("deleteNode error:", err));
}

function resetTree() {
  fetch("/reset", { method: "POST" })
    .then(res => res.json())
    .then(tree => {
      selected = null;
      drawTree(tree);
    })
    .catch(err => console.error("resetTree error:", err));
}

// INITIAL LOAD
fetchTree();
