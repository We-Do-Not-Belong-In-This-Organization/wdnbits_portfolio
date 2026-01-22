// ------------------- GRAPH VISUALIZER -------------------

const canvas = document.getElementById('graphCanvas');
const ctx = canvas.getContext('2d');
const HITBOX_PADDING = 6;

let visualNodes = []; 
let adjList = {};     
let highlightedPath = []; 
let shortestPathActive = false;

// Set internal resolution to a high-definition 16:10 ratio
canvas.width = 1600;
canvas.height = 1000;

// Interaction State
let draggingNode = null;
let dragOffsetX = 0;
let dragOffsetY = 0;

// Click Cycle State: 0 = Fill A next, 1 = Fill B next
let selectionState = 0; 

// Background Dots
const dotColors = ["white", "#0081f1", "#800080"];
let dots = [];
for(let i=0; i<150; i++) {
    dots.push({
        x: Math.random()*canvas.width, y: Math.random()*canvas.height,
        size: Math.random()*1.5,
        speedX: (Math.random()-0.5)*0.3, speedY: (Math.random()-0.5)*0.3,
        color: dotColors[Math.floor(Math.random()*dotColors.length)]
    });
}

// ------------------- ANIMATION LOOP -------------------

function animate() {
    ctx.clearRect(0,0, canvas.width, canvas.height);
    
    // 1. Draw Background
    ctx.fillStyle = "black";
    ctx.fillRect(0,0, canvas.width, canvas.height);
    
    // Draw dots
    for (let d of dots) {
        d.x += d.speedX; d.y += d.speedY;
        if(d.x<0) d.x=canvas.width; if(d.x>canvas.width) d.x=0;
        if(d.y<0) d.y=canvas.height; if(d.y>canvas.height) d.y=0;
        ctx.beginPath();
        ctx.arc(d.x, d.y, d.size, 0, Math.PI*2);
        ctx.fillStyle = d.color;
        ctx.fill();
    }

    // 2. Draw Edges
    ctx.lineWidth = 4;
    for (let node of visualNodes) {
        let neighbors = adjList[node.id] || [];
        for (let neighborId of neighbors) {
            let neighborNode = visualNodes.find(n => n.id === neighborId);
            if (neighborNode) {
                ctx.strokeStyle = "#38a5ffff";
                ctx.shadowColor = "#38a5ffff";
                ctx.shadowBlur = 5;
                ctx.beginPath();
                ctx.moveTo(node.x, node.y);
                ctx.lineTo(neighborNode.x, neighborNode.y);
                ctx.stroke();
                ctx.shadowBlur = 0; 
            }
        }
    }

    // 3. Draw Highlighted Path
    if (highlightedPath.length > 1) {
        ctx.lineWidth = 20;
        ctx.strokeStyle = "#ffffff"; 
        ctx.shadowColor = "#ffffff";
        ctx.shadowBlur = 15;
        ctx.beginPath();
        for (let i = 0; i < highlightedPath.length - 1; i++) {
            const n1 = visualNodes.find(n => n.id === highlightedPath[i]);
            const n2 = visualNodes.find(n => n.id === highlightedPath[i+1]);
            if (n1 && n2) {
                ctx.moveTo(n1.x, n1.y);
                ctx.lineTo(n2.x, n2.y);
            }
        }
        ctx.stroke();
        ctx.shadowBlur = 0;
    }

    // 4. Draw Nodes (Rectangles)
    ctx.font = "bold 24px Arial"; 
    
    // Read current inputs to determine highlights
    const nodeAVal = document.getElementById("nodeA").value;
    const nodeBVal = document.getElementById("nodeB").value;

    for (let node of visualNodes) {
        const metrics = ctx.measureText(node.id);
        const rectWidth = metrics.width + 40;
        const rectHeight = 50; 
        
        const drawX = node.x - (rectWidth / 2);
        const drawY = node.y - (rectHeight / 2);
        
        node.width = rectWidth;
        node.height = rectHeight;

        node.hitX = drawX;
        node.hitY = drawY;
        node.hitW = rectWidth;
        node.hitH = rectHeight;

        ctx.beginPath();
        if (ctx.roundRect) ctx.roundRect(drawX, drawY, rectWidth, rectHeight, 8);
        else ctx.rect(drawX, drawY, rectWidth, rectHeight);

        // --- DYNAMIC COLORING BASED ON SELECTION ---
        if (node.id === nodeAVal) {
            ctx.fillStyle = "#00bfff"; // Source = Green
        } else if (node.id === nodeBVal) {
            ctx.fillStyle = "#0037ff"; // Dest = Magenta
        } else {
            ctx.fillStyle = "rgba(255, 255, 255, 0.9)"; // Default
        }

        ctx.fill();
     
        const isPathNode = shortestPathActive && highlightedPath.includes(node.id);

     
        if (isPathNode) {
            ctx.strokeStyle = "#ffffff"; 
            ctx.lineWidth = 8;           
            ctx.shadowColor = "#ffffff";
            ctx.shadowBlur = 20; 
        } else {
            ctx.strokeStyle = "#00e5ff"; 
            ctx.lineWidth = 4;          
            ctx.shadowBlur = 0;
        }


        ctx.stroke();
        ctx.shadowBlur = 0;
        ctx.lineWidth = 1;

        ctx.fillStyle = "black";
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        ctx.fillText(node.id, node.x, node.y);
    }

    requestAnimationFrame(animate);
}
animate();


// ------------------- LOGIC SYNC -------------------

function fetchGraph() {
    fetch('/get_graph')
        .then(res => res.json())
        .then(data => {
            adjList = data;
            syncVisualNodes(data);
        });
}

function syncVisualNodes(data) {
    const keys = Object.keys(data);
    visualNodes = visualNodes.filter(n => keys.includes(n.id));
    for (let key of keys) {
        if (!visualNodes.find(n => n.id === key)) {
            visualNodes.push({
                id: key,
                x: Math.random() * (canvas.width - 150) + 75,
                y: Math.random() * (canvas.height - 100) + 50,
                width: 50, height: 30
            });
        }
    }
}


// ------------------- CLICK & DRAG LOGIC -------------------

function getMousePos(e) {
    const rect = canvas.getBoundingClientRect();
    const scaleX = canvas.width / rect.width;
    const scaleY = canvas.height / rect.height;

    return { 
        x: (e.clientX - rect.left) * scaleX, 
        y: (e.clientY - rect.top) * scaleY 
    };
}

canvas.addEventListener("mousedown", e => {
    const m = getMousePos(e);
    ctx.font = "bold 14px Arial";
    
    // Hit Test
    for (let i = visualNodes.length - 1; i >= 0; i--) {
        const node = visualNodes[i];
        ctx.font = "bold 24px Arial";
        const metrics = ctx.measureText(node.id);

        if (
    m.x >= node.hitX &&
    m.x <= node.hitX + node.hitW &&
    m.y >= node.hitY &&
    m.y <= node.hitY + node.hitH
        ) {

            
            // --- SMART SELECTION LOGIC ---
            const inputA = document.getElementById("nodeA");
            const inputB = document.getElementById("nodeB");

            if (selectionState === 0) {
                // First click: Fill A, Clear B
                inputA.value = node.id;
                inputB.value = ""; 
                selectionState = 1; // Next click will be B
            } else {
                // Second click: Fill B
                inputB.value = node.id;
                selectionState = 0; // Reset cycle
            }

            // Drag Logic
            draggingNode = node;
            dragOffsetX = m.x - node.x;
            dragOffsetY = m.y - node.y;
            return;
        }
    }
    
    // Clicking empty space will deselect all
    document.getElementById("nodeA").value = "";
    document.getElementById("nodeB").value = "";
    selectionState = 0;
});

canvas.addEventListener("mousemove", e => {
    if (draggingNode) {
        const m = getMousePos(e);
        draggingNode.x = m.x - dragOffsetX;
        draggingNode.y = m.y - dragOffsetY;
    }
});

canvas.addEventListener("mouseup", () => {
    draggingNode = null;
});


// ------------------- API FUNCTIONS -------------------

function addVertex() {
    const value = document.getElementById("vertexInput").value.trim();
    if (!value) return alert("Enter value");
    fetch('/add_vertex', {
        method: 'POST', body: JSON.stringify({value}), headers: {"Content-Type": "application/json"}
    }).then(fetchGraph);
    document.getElementById("vertexInput").value = "";
}

function addEdge() {
    shortestPathActive = false;
    const v1 = document.getElementById("nodeA").value.trim();
    const v2 = document.getElementById("nodeB").value.trim();
    
    if (!v1 || !v2) return alert("Select two nodes first!");

    fetch('/add_edge', {
        method: 'POST', body: JSON.stringify({v1, v2}), headers: {"Content-Type": "application/json"}
    }).then(() => {
        fetchGraph();
        // --- RESET INPUTS AFTER ADDING ---
        document.getElementById("nodeA").value = "";
        document.getElementById("nodeB").value = "";
        selectionState = 0;
    });
}

function deleteVertex() {
    shortestPathActive = false;
    const v = document.getElementById("nodeA").value.trim();
    if (!v) return alert("Select a node (Source) to delete");
    
    fetch('/delete_vertex', {
        method: 'POST', body: JSON.stringify({value: v}), headers: {"Content-Type": "application/json"}
    }).then(() => {
        document.getElementById("nodeA").value = "";
        document.getElementById("nodeB").value = "";
        fetchGraph();
    });
}

function findShortestPath() {
    const start = document.getElementById("nodeA").value.trim();
    const end = document.getElementById("nodeB").value.trim();
    if(!start || !end) return alert("Select Start and End nodes.");

    fetch('/shortest_path', {
        method: 'POST', body: JSON.stringify({start, end}), headers: {"Content-Type": "application/json"}
    })
    .then(res => res.json())
    .then(res => {
        if (res.found) {
            highlightedPath = res.path;
            shortestPathActive = true;
            document.querySelector(".graph-display").innerHTML = `<p><b>Path:</b> ${res.path.join(" → ")}</p>`;
        } else {
            highlightedPath = [];
            shortestPathActive = false;
            alert(res.error);
        }
    });
}

function runBFS() {
    shortestPathActive = false;
    const start = document.getElementById("nodeA").value.trim();
    if(!start) return alert("Select a Source node.");
    highlightedPath = [];
    fetch('/traverse_graph', {
        method: 'POST', body: JSON.stringify({start_node: start, type: 'bfs'}), headers: {"Content-Type": "application/json"}
    })
    .then(res=>res.json())
    .then(res => {
        document.querySelector(".graph-display").innerHTML = `<p><b>BFS:</b> ${res.result || res.error}</p>`;
    });
}

function runDFS() {
    shortestPathActive = false;
    const start = document.getElementById("nodeA").value.trim();
    if(!start) return alert("Select a Source node.");
    highlightedPath = [];
    fetch('/traverse_graph', {
        method: 'POST', body: JSON.stringify({start_node: start, type: 'dfs'}), headers: {"Content-Type": "application/json"}
    })
    .then(res=>res.json())
    .then(res => {
        document.querySelector(".graph-display").innerHTML = `<p><b>DFS:</b> ${res.result || res.error}</p>`;
    });
}

function handleFileUpload(inputElement) {
    const file = inputElement.files[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = function(e) {
        try {
            const jsonContent = JSON.parse(e.target.result);
            fetch('/load_from_json', {
                method: 'POST', headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(jsonContent)
            }).then(res => res.json()).then(data => {
                adjList = data;
                syncVisualNodes(data);
                highlightedPath = [];
                inputElement.value = '';
                alert("Graph loaded!");
            });
        } catch (err) { alert("Invalid JSON"); }
    };
    reader.readAsText(file);
}

function resetGraph() {
    shortestPathActive = false;
    fetch('/reset_graph', { method: 'POST' })
    .then(res => res.json())
    .then(data => {
        adjList = data;
        visualNodes = [];
        highlightedPath = [];
        document.querySelector(".graph-display").innerHTML = "<p>Output Display</p>";
        document.getElementById("nodeA").value = "";
        document.getElementById("nodeB").value = "";
        animate(); 
    });
}

// Init
fetchGraph();