from flask import Blueprint, render_template, request, jsonify
from src.logic.graph import Graph

graph_bp = Blueprint('graph', __name__)
graph_structure = Graph()


@graph_bp.route("/graph")
def graph_page():
    """Displays the interactive graph visualization page.

    Retrieves the page where the user navigated from (if any)
    and passes it to the graph template.

    Returns:
        Rendered HTML template for graph.html.
    """
    from_page = request.args.get("from_page", "Home")
    return render_template("works/graph.html", from_page=from_page)


@graph_bp.route("/get_graph")
def get_graph():
    """Provides the current graph structure as JSON data.

    Used by the frontend to fetch and update graph state.

    Returns:
        JSON object representing vertices and edges.
    """
    return jsonify(graph_structure.get_data())


@graph_bp.route("/add_vertex", methods=["POST"])
def add_vertex():
    """Adds a new vertex to the graph.

    Expects a JSON payload containing the vertex value.

    Returns:
        Updated graph data if successful,
        or an error message if input is missing.
    """
    payload = request.get_json(force=True)
    value = payload.get("value")
    if not value:
        return jsonify({"error": "Missing value"}), 400
    
    graph_structure.add_vertex(value)
    return jsonify(graph_structure.get_data())


@graph_bp.route("/add_edge", methods=["POST"])
def add_edge():
    """Creates an edge between two existing vertices.

    Expects a JSON payload with two vertex identifiers.

    Returns:
        Updated graph data if successful,
        or an error message if vertices are invalid.
    """
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
    """Removes a vertex and its connected edges from the graph.

    Expects a JSON payload containing the vertex value.

    Returns:
        Updated graph data after deletion.
    """
    payload = request.get_json(force=True)
    value = payload.get("value")
    graph_structure.remove_vertex(value)
    return jsonify(graph_structure.get_data())


@graph_bp.route("/traverse_graph", methods=["POST"])
def traverse_graph():
    """Traverses the graph using BFS or DFS.

    Expects a JSON payload with a starting node and
    traversal type ('bfs' or 'dfs').

    Returns:
        JSON result showing traversal order,
        or an error message for invalid input.
    """
    payload = request.get_json(force=True)
    start_node = payload.get("start_node")
    algo = payload.get("type")  # 'bfs' or 'dfs'
    
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
    """Finds the shortest path between two vertices.

    Expects a JSON payload with starting and ending vertices.

    Returns:
        JSON response indicating whether a path was found
        and the corresponding path if it exists.
    """
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
    """Resets the graph by clearing all vertices and edges.

    Returns:
        Empty graph data structure.
    """
    graph_structure.adj_list = {}
    return jsonify(graph_structure.get_data())