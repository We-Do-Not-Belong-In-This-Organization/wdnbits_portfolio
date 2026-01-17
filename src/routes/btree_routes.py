from flask import Blueprint, render_template, request, jsonify
from src.logic.binary_tree import BinaryTree
from src.logic.tree_node import Node

btree_bp = Blueprint('btree', __name__)

tree = BinaryTree()
tree.root = Node("Root")  # ensure root exists on startup


def serialize(node):
    """Convert Python Node to JSON-friendly dict (or None).

    This helper function recursively walks the tree to build a dictionary
    that can be sent to the frontend javascript.

    Parameters:
        node (Node): The current node to process.

    Returns:
        dict or None: The dictionary representation of the node.
    """
    if node is None:
        return None
    return {
        "id": node.id,
        "data": node.data,
        "left": serialize(node.left),
        "right": serialize(node.right)
    }


@btree_bp.route("/binary-tree")
def binarytree_page():
    """Renders the standard Binary Tree interface.

    Query Parameters:
        from_page (str, optional): Navigation origin tracker.

    Returns:
        Rendered HTML template.
    """
    from_page = request.args.get("from_page", "")
    return render_template("works/binary-tree.html", from_page=from_page)


@btree_bp.route("/get_tree")
def get_tree():
    """Fetches the current structure of the Binary Tree.

    Returns:
        JSON: The serialized tree object.
    """
    return jsonify(serialize(tree.root))


@btree_bp.route("/insert_left", methods=["POST"])
def insert_left():
    """Inserts a new node to the left of a specified parent.

    Expects JSON Payload:
        { "parent": int (id), "value": any }

    Returns:
        JSON: The updated tree structure.
        JSON Error: 400 if parent/value missing or child already exists.
    """
    payload = request.get_json(force=True)
    parent = payload.get("parent")
    value = payload.get("value")
    if parent is None or value is None:
        return jsonify(serialize(tree.root)), 400

    node = tree.search(tree.root, parent)
    if node:
        ok = tree.insert_left(node, value)
        if not ok:
            return jsonify({"error": "Left child already exists"}), 400
    # return current tree regardless (so frontend can re-draw)
    return jsonify(serialize(tree.root))


@btree_bp.route("/insert_right", methods=["POST"])
def insert_right():
    """Inserts a new node to the right of a specified parent.

    Expects JSON Payload:
        { "parent": int (id), "value": any }

    Returns:
        JSON: The updated tree structure.
        JSON Error: 400 if parent/value missing or child already exists.
    """
    payload = request.get_json(force=True)
    parent = payload.get("parent")
    value = payload.get("value")
    if parent is None or value is None:
        return jsonify(serialize(tree.root)), 400

    node = tree.search(tree.root, parent)
    if node:
        ok = tree.insert_right(node, value)
        if not ok:
            return jsonify({"error": "Right child already exists"}), 400
    return jsonify(serialize(tree.root))


@btree_bp.route("/delete", methods=["POST"])
def delete_node():
    """Deletes a node based on its unique ID.

    Expects JSON Payload:
        { "nodeId": int }

    Returns:
        JSON: The updated tree structure.
    """
    payload = request.get_json(force=True)
    node_id = payload.get("nodeId")
    if node_id is None:
        return jsonify({"error": "missing nodeId"}), 400

    # Perform deletion
    tree.root = tree.delete(tree.root, node_id)

    return jsonify(serialize(tree.root))




@btree_bp.route("/reset", methods=["POST"])
def reset_tree():
    """Resets the tree to a single default Root node.

    Returns:
        JSON: The new tree with just the Root node.
    """
    tree.root = Node("Root")
    return jsonify(serialize(tree.root))


@btree_bp.route("/traverse", methods=["POST"])
def traverse():
    """Performs a specific traversal (inorder, preorder, postorder).

    Expects JSON Payload:
        { "type": "inorder" | "preorder" | "postorder" }

    Returns:
        JSON: { "result": str } containing the traversal path.
    """
    payload = request.get_json(force=True)
    traverse = payload.get("type")

    if traverse == "inorder":
        result = tree.inorder_traversal(tree.root, "")
    elif traverse == "preorder":
        result = tree.preorder_traversal(tree.root, "")
    elif traverse == "postorder":
        arr = []
        arr = tree.post_traversal(tree.root, arr)
        result = " ".join(str(x) for x in arr)
    else:
        return jsonify({"error": "Unknown traversal type"}), 400

    return jsonify({"result": result})


@btree_bp.route("/search_node", methods=["POST"])
def search_node():
    """Searches for a node by its data value.

    Expects JSON Payload:
        { "value": any }

    Returns:
        JSON: { "found": True, "id": int }
        JSON Error: 404 if not found.
    """
    payload = request.get_json(force=True)
    value = payload.get("value")
    if not value:
        return jsonify({"error": "Please enter a value"}), 400

    node = tree.search_by_value(tree.root, value)
    if node:
        return jsonify({"found": True, "id": node.id})
    else:
        return jsonify({"found": False, "error": "Node not found"}), 404
    