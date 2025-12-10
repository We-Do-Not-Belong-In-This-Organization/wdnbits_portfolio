# pip install Flask
# Two lines spacing for each route

from binary_tree import BinaryTree
from binary_search_tree import BinarySearchTree
from tree_node import Node
from flask import Flask, render_template, request, redirect, url_for, jsonify
from queues import Queue  # Import the Queue class
from deques import Deque  # Import the Deque class


website = Flask(__name__)
queue_line = Queue()
deque_line = Deque()
# For Navigation Bar


# Home Page
@website.route("/")
def home():
    return render_template("index.html") 


@website.route("/profile")
def profile():
    characters = [
        {"img": "orbista.png", "page": "ced", "left_img": "ced-left.png", "right_img": "ced-right.png"},
        {"img": "aeron.png", "page": "deqs", "left_img": "deqs-left.png", "right_img": "deqs-right.png"},
        {"img": "hassan.png", "page": "hassan", "left_img": "hassan-left.png", "right_img": "hassan-right.png"},
        {"img": "rafael.png", "page": "ian", "left_img": "rafael-left.png", "right_img": "rafael-right.png"},
        {"img": "james.png", "page": "james", "left_img": "james-left.png", "right_img": "james-right.png"},
        {"img": "jayvee.png", "page": "jayvee", "left_img": "jayvee-left.png", "right_img": "jayvee-right.png"},
        {"img": "jed.png", "page": "jed", "left_img": "jed-left.png", "right_img": "jed-right.png"},
        {"img": "laei.png", "page": "laei", "left_img": "laei-left.png", "right_img": "laei-right.png"},
        {"img": "marx.png", "page": "marx", "left_img": "marx-left.png", "right_img": "marx-right.png"},
        {"img": "matt.png", "page": "matt", "left_img": "matt-left.png", "right_img": "matt-right.png"}
    ]
    return render_template("profile.html", characters=characters)

@website.route("/works")
def worksoon():
    from_page = request.args.get("from_page", None)
    return render_template("coming-soon.html", from_page=from_page)

@website.route("/works")
def works():
    return render_template("/works.html")  # Change #works.html per member

@website.route("/secret")
def secret():
    return render_template("secret.html")

# For members, copy and paste this to your own portfolio including the 'queue.html' and 'dequeue.html" file

# ---- queue system ----


@website.route('/queue')
def queue_page():
    from_page = request.args.get('from_page', '')
    return render_template('queue.html', queue_line=queue_line.display(), from_page=from_page)

@website.route('/enqueue', methods=['POST'])
def enqueue():
    item = request.form.get('user_enqueue')
    from_page = request.form.get('from_page')

    if item:
        queue_line.enqueue(item)

    return redirect(url_for('queue_page', from_page=from_page))

@website.route('/dequeue', methods=['POST'])
def dequeue():
    from_page = request.form.get('from_page')

    queue_line.dequeue()

    return redirect(url_for('queue_page', from_page=from_page))

@website.route('/clear_queue', methods=['POST'])
def clear_queue():
    from_page = request.form.get('from_page')

    queue_line.clear()

    return redirect(url_for('queue_page', from_page=from_page))


# =====================================================
# DEQUE System (no changes)
# =====================================================

@website.route('/deque')
def deque_page():
    from_page = request.args.get('from_page', '')
    return render_template('deque.html', deque_items=deque_line.display(), from_page=from_page)


@website.route('/enqueue_front', methods=['POST'])
def enqueue_front():
    item = request.form.get('user_enqueue')
    from_page = request.form.get('from_page')

    if item:
        deque_line.enqueue_front(item)

    return redirect(url_for('deque_page', from_page=from_page))


@website.route('/dequeue_rear', methods=['POST'])
def dequeue_rear():
    from_page = request.form.get('from_page')

    if not deque_line.is_empty():
        deque_line.dequeue_rear()

    return redirect(url_for('deque_page', from_page=from_page))


@website.route('/enqueue_rear', methods=['POST'])
def enqueue_rear():
    item = request.form.get('user_enqueue')
    from_page = request.form.get('from_page')

    if item:
        deque_line.enqueue_rear(item)

    return redirect(url_for('deque_page', from_page=from_page))


@website.route('/dequeue_front', methods=['POST'])
def dequeue_front():
    from_page = request.form.get('from_page')

    if not deque_line.is_empty():
        deque_line.dequeue_front()

    return redirect(url_for('deque_page', from_page=from_page))


@website.route('/clear_dob_queue', methods=['POST'])
def clear_dob_queue():
    from_page = request.form.get('from_page')

    deque_line.clear()

    return redirect(url_for('deque_page', from_page=from_page))



# End of DEqueue

# 🔹 Route for each member’s HTML
@website.route("/profile/<name>")
def profile_member(name):
    try:
        return render_template(f"member_profiles/{name}.html", member=name)
    except Exception as e:
        print("⚠️ Error:", e)
        return "Profile not found", 404


@website.route("/trees")
def trees_page():
    from_page = request.args.get("from_page", "")
    return render_template("trees.html", from_page=from_page)

# For binary tree
tree = BinaryTree()
tree.root = Node("Root")  # ensure root exists on startup


def serialize(node):
    """Convert Python Node to JSON-friendly dict (or None)."""
    if node is None:
        return None
    return {
        "id": node.id,
        "data": node.data,
        "left": serialize(node.left),
        "right": serialize(node.right)
    }


@website.route("/binary-tree")
def binarytree_page():
    from_page = request.args.get("from_page", "")
    return render_template("binary-tree.html", from_page=from_page)


@website.route("/get_tree")
def get_tree():
    return jsonify(serialize(tree.root))


@website.route("/insert_left", methods=["POST"])
def insert_left():
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


@website.route("/insert_right", methods=["POST"])
def insert_right():
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


@website.route("/delete", methods=["POST"])
def delete_node():
    payload = request.get_json(force=True)
    node_id = payload.get("nodeId")
    if node_id is None:
        return jsonify({"error": "missing nodeId"}), 400

    # Perform deletion
    tree.root = tree.delete(tree.root, node_id)

    return jsonify(serialize(tree.root))




@website.route("/reset", methods=["POST"])
def reset_tree():
    tree.root = Node("Root")
    return jsonify(serialize(tree.root))


@website.route("/traverse", methods=["POST"])
def traverse():
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


@website.route("/search_node", methods=["POST"])
def search_node():
    payload = request.get_json(force=True)
    value = payload.get("value")
    if not value:
        return jsonify({"error": "Please enter a value"}), 400

    node = tree.search_by_value(tree.root, value)
    if node:
        return jsonify({"found": True, "id": node.id})
    else:
        return jsonify({"found": False, "error": "Node not found"}), 404



# ----------- Binary Search Tree -----------

bstree = BinarySearchTree()
bstree.root = None  # start with empty tree


def serialize_bst(node):
    if node is None:
        return None
    return {
        "id": node.id,
        "data": int(node.data),
        "left": serialize_bst(node.left),
        "right": serialize_bst(node.right)
    }


@website.route("/binary-search-tree")
def bst_page():
    from_page = request.args.get("from_page", "")
    return render_template("binary-search-tree.html", from_page=from_page)


@website.route("/get_bstree")
def get_bstree():
    return jsonify(serialize_bst(bstree.root))


@website.route("/insert", methods=["POST"])
def insert():
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



@website.route("/delete_bst", methods=["POST"])
def delete_bst_node():
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



@website.route("/reset_bst", methods=["POST"])
def reset_bstree():
    bstree.root = None
    return jsonify(serialize_bst(bstree.root))



@website.route("/traverse_bst", methods=["POST"])
def traverse_bst():
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



@website.route("/search_bst", methods=["POST"])
def search_bst():
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


@website.route("/find_max", methods=["POST"])
def find_max():
    if bstree.root is None:
        return jsonify({"error": "Tree is empty"}), 400

    max_node = bstree.find_max()
    return jsonify({"max_value": max_node})


@website.route("/find_height", methods=["POST"])
def find_height():
    height = bstree.find_height()
    return jsonify({"height": height})


if __name__ == '__main__':
    website.run(debug=True)
