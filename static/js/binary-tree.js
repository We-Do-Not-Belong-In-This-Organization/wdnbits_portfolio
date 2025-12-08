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
  if (tree) drawNode(tree, canvas.width / 2, 40, 200);
  updateSelectedDisplay();
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
  ctx.fillStyle = (selected === node.id) ? "#00d5ffff" : "#ffffff";
  ctx.fill();
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




function insertLeft() {
  const value = document.getElementById("valueInput").value;
  if (selected === null || value.trim() === "") return alert("Select a parent and enter a value.");

  fetch("/insert_left", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ parent: selected, value})
  })
    .then(res => res.json())
    .then(res => {
      if (res.error) return alert(res.error);
      document.getElementById("valueInput").value = "";
      drawTree(res);
    })

    .catch(err => console.error("insertLeft error:", err));
}

function insertRight() {
  const value = document.getElementById("valueInput").value;
  if (selected === null || value.trim() === "") return alert("Select a parent and enter a value.");

  fetch("/insert_right", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ parent: selected, value})
  })
    .then(res => res.json())
    .then(res => {
      if (res.error) return alert(res.error);
      document.getElementById("valueInput").value = "";
      drawTree(res);
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

function inorderTraversal() {
  fetch("/traverse", {
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
  fetch("/traverse", {
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
  fetch("/traverse", {
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

    fetch("/search_node", {
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
