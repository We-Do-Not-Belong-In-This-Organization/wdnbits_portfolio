from flask import Blueprint, render_template, request, jsonify
from src.logic.binary_search_tree import BinarySearchTree
from src.logic.tree_node import Node

bstree_bp = Blueprint('bstree', __name__)
bstree = BinarySearchTree()
bstree.root = None  # start with empty tree


def serialize_bst(node):
    """Recursively converts a BST node and its children into a dictionary.
    
    This is necessary because Python objects (like Nodes) cannot be directly
    sent as JSON responses to the browser.

    Parameters:
        node (Node): The current node to serialize.

    Returns:
        dict or None: A dictionary representing the node (id, data, left, right), 
                      or None if the node is empty.
    """
    if node is None:
        return None
    return {
        "id": node.id,
        "data": int(node.data),
        "left": serialize_bst(node.left),
        "right": serialize_bst(node.right)
    }


@bstree_bp.route("/binary-search-tree")
def bst_page():
    """Renders the main Binary Search Tree interface.

    Query Parameters:
        from_page (str, optional): A query parameter to track navigation origin.

    Returns:
        Rendered HTML template for the BST page.
    """
    from_page = request.args.get("from_page", "")
    return render_template("works/binary-search-tree.html", from_page=from_page)


@bstree_bp.route("/get_bstree")
def get_bstree():
    """Fetches the current structure of the Binary Search Tree.

    Returns:
        JSON: A JSON representation of the entire tree.
    """
    return jsonify(serialize_bst(bstree.root))


@bstree_bp.route("/insert", methods=["POST"])
def insert():
    """Inserts a new value into the Binary Search Tree.

    Expects JSON Payload:
        { "value": int }

    Returns:
        JSON: The updated tree structure if successful.
        JSON Error: 400 status code if value is missing, invalid, or a duplicate.
    """
    payload = request.get_json(force=True)
    value = payload.get("value")
    if not value:
        return jsonify({"error": "Missing value"}), 400

    try:
        val = int(value)
    except ValueError:
        return jsonify({"error": "Value must be an integer"}), 400

    ok = bstree.insert(val)
    if not ok:
        return jsonify({"error": "Value already exists"}), 400

    return jsonify(serialize_bst(bstree.root))



@bstree_bp.route("/delete_bst", methods=["POST"])
def delete_bst_node():
    """Deletes a node with a specific value from the tree.

    Expects JSON Payload:
        { "value": int }

    Returns:
        JSON: The updated tree structure.
        JSON Error: 400 status code if value is missing or invalid.
    """
    payload = request.get_json(force=True)
    value = payload.get("value")
    if not value:
        return jsonify({"error": "Missing value"}), 400

    try:
        val = int(value)
    except ValueError:
        return jsonify({"error": "Value must be an integer"}), 400

    bstree.delete(val)
    return jsonify(serialize_bst(bstree.root))



@bstree_bp.route("/reset_bst", methods=["POST"])
def reset_bstree():
    """Clears the entire Binary Search Tree.

    Returns:
        JSON: An empty JSON object (null root).
    """
    bstree.root = None
    return jsonify(serialize_bst(bstree.root))



@bstree_bp.route("/traverse_bst", methods=["POST"])
def traverse_bst():
    """Performs a specific traversal on the tree.

    Expects JSON Payload:
        { "type": "inorder" | "preorder" | "postorder" }

    Returns:
        JSON: { "result": "1 5 10..." } string of traversed values.
        JSON Error: 400 status code if traversal type is unknown.
    """
    payload = request.get_json(force=True)
    t_type = payload.get("type")
    result = ""
    if t_type == "inorder":
        result = bstree.inorder_traversal().strip()
    elif t_type == "preorder":
        result = bstree.preorder_traversal().strip()
    elif t_type == "postorder":
        result = bstree.postorder_traversal().strip()
    else:
        return jsonify({"error": "Unknown traversal type"}), 400
    print("TRAVERSE CALLED:", t_type)
    return jsonify({"result": result})



@bstree_bp.route("/search_bst", methods=["POST"])
def search_bst():
    """Searches for a specific value in the tree.

    Expects JSON Payload:
        { "value": int }

    Returns:
        JSON: { "found": true, "id": node_id } if found.
        JSON Error: 404 status code if not found, or 400 if input invalid.
    """
    payload = request.get_json(force=True)
    value = payload.get("value")
    if not value:
        return jsonify({"error": "Missing value"}), 400

    try:
        val = int(value)
    except ValueError:
        return jsonify({"error": "Value must be an integer"}), 400

    node = bstree.search(val)
    if node:
        return jsonify({"found": True, "id": node.id})
    else:
        return jsonify({"found": False, "error": "Node not found"}), 404


@bstree_bp.route("/find_max", methods=["POST"])
def find_max():
    """Finds the maximum value in the current tree.

    Returns:
        JSON: { "max_value": int }
        JSON Error: 400 status code if tree is empty.
    """
    if bstree.root is None:
        return jsonify({"error": "Tree is empty"}), 400

    max_node = bstree.find_max()
    return jsonify({"max_value": max_node})


@bstree_bp.route("/find_height", methods=["POST"])
def find_height():
    """Calculates the height of the tree.

    Returns:
        JSON: { "height": int }
    """
    height = bstree.find_height()
    return jsonify({"height": height})