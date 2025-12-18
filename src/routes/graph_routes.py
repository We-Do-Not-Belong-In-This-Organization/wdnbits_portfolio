from flask import Blueprint, render_template, request, jsonify
from src.logic.graph import Graph

graph_bp = Blueprint('graph', __name__)
graph_structure = Graph()


@graph_bp.route("/graph")
def graph_page():
    from_page = request.args.get("from_page", "Home")
    return render_template("works/graph.html", from_page=from_page)

@graph_bp.route("/get_graph")
def get_graph():
    return jsonify(graph_structure.get_data())

@graph_bp.route("/add_vertex", methods=["POST"])
def add_vertex():
    payload = request.get_json(force=True)
    value = payload.get("value")
    if not value:
        return jsonify({"error": "Missing value"}), 400
    
    graph_structure.add_vertex(value)
    return jsonify(graph_structure.get_data())

@graph_bp.route("/add_edge", methods=["POST"])
def add_edge():
    payload = request.get_json(force=True)
    v1 = payload.get("v1")
    v2 = payload.get("v2")
    if not v1 or not v2:
        return jsonify({"error": "Missing vertices"}), 400

    success = graph_structure.add_edge(v1, v2)
    if not success:
        return jsonify({"error": "One or both vertices do not exist"}), 400
        
    return jsonify(graph_structure.get_data())

@graph_bp.route("/delete_vertex", methods=["POST"])
def delete_vertex():
    payload = request.get_json(force=True)
    value = payload.get("value")
    graph_structure.remove_vertex(value)
    return jsonify(graph_structure.get_data())

@graph_bp.route("/traverse_graph", methods=["POST"])
def traverse_graph():
    payload = request.get_json(force=True)
    start_node = payload.get("start_node")
    algo = payload.get("type") # 'bfs' or 'dfs'
    
    if not start_node:
        return jsonify({"error": "Start node required"}), 400

    if algo == 'bfs':
        res = graph_structure.bfs(start_node)
    elif algo == 'dfs':
        res = graph_structure.dfs(start_node)
    else:
        return jsonify({"error": "Invalid algorithm"}), 400
        
    return jsonify({"result": " -> ".join(res)})

@graph_bp.route("/shortest_path", methods=["POST"])
def shortest_path():
    payload = request.get_json(force=True)
    start = payload.get("start")
    end = payload.get("end")
    
    path = graph_structure.get_shortest_path(start, end)
    
    if path:
        return jsonify({"found": True, "path": path})
    else:
        return jsonify({"found": False, "error": "No path found"})

@graph_bp.route("/load_from_json", methods=["POST"])
def load_from_json():
    # Expecting payload: { "nodes": ["A", "B"], "edges": [["A", "B"]] }
    data = request.get_json(force=True)
    
    nodes = data.get("nodes", [])
    edges = data.get("edges", [])
    
    # Optional: Clear existing graph before loading?
    # graph_structure.adj_list = {} 
    
    # 1. Add all nodes first
    for n in nodes:
        graph_structure.add_vertex(str(n)) # Ensure string format
        
    # 2. Add all edges
    for edge in edges:
        if len(edge) >= 2:
            graph_structure.add_edge(str(edge[0]), str(edge[1]))
            
    return jsonify(graph_structure.get_data())

@graph_bp.route("/reset_graph", methods=["POST"])
def reset_graph():
    # Clear the dictionary completely
    graph_structure.adj_list = {} 
    return jsonify(graph_structure.get_data())