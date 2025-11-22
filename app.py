# pip install Flask
# Two lines spacing for each route

from binary_tree import BinaryTree, Node
from flask import Flask, render_template, request, redirect, url_for
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
def works():
    return render_template("/works.html")  # Change #works.html per member

# For members, copy and paste this to your own portfolio including the 'queue.html' and 'dequeue.html" file

# ---- queue system ----


@website.route('/queue')
def queue_page():
    from_page = request.args.get('from_page', '')
    return render_template('queue.html', queue_line=queue_line.display(), from_page=from_page)

@website.route('/enqueue', methods=['POST'])
def enqueue():
    item = request.form.get('user_enqueue')
    if item:
        queue_line.enqueue(item)
    return redirect(url_for('queue_page'))

@website.route('/dequeue', methods=['POST'])
def dequeue():
    queue_line.dequeue()
    return redirect(url_for('queue_page'))

@website.route('/clear_queue', methods=['POST'])
def clear_queue():
    queue_line.clear()
    return redirect(url_for('queue_page'))


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
    if item:
        deque_line.enqueue_front(item)
    return redirect(url_for('deque_page'))


@website.route('/dequeue_rear', methods=['POST'])
def dequeue_rear():
    if not deque_line.is_empty():
        deque_line.dequeue_rear()
    return redirect(url_for('deque_page'))


@website.route('/enqueue_rear', methods=['POST'])
def enqueue_rear():
    item = request.form.get('user_enqueue')
    if item:
        deque_line.enqueue_rear(item)
    return redirect(url_for('deque_page'))


@website.route('/dequeue_front', methods=['POST'])
def dequeue_front():
    if not deque_line.is_empty():
        deque_line.dequeue_front()
    return redirect(url_for('deque_page'))


@website.route('/clear_dob_queue', methods=['POST'])
def clear_dob_queue():
    deque_line.clear()
    return redirect(url_for('deque_page'))



# End of DEqueue

#WORKS (ON PROGRESS)

@website.route('/project')
def project():
    return render_template("project.html")


# 🔹 Route for each member’s HTML
@website.route("/profile/<name>")
def profile_member(name):
    try:
        return render_template(f"member_profiles/{name}.html", member=name)
    except Exception as e:
        print("⚠️ Error:", e)
        return "Profile not found", 404
    

# Route for the back button of queue and deque page

@website.route('/<member_name>/queue')
def member_queue(member_name):
    return render_template('queue.html', queue_line=queue_line.display(), member_name=member_name)

@website.route('/<member_name>/deque')
def member_deque(member_name):
    return render_template('deque.html', deque_items=deque_line.display(), member_name=member_name)

# For binary tree
@website.route("/postorder")
def postorder_page():
    member_name = request.args.get('from_page', '')  # read member from query parameter
    
    # Build the example binary tree
    tree = BinaryTree()
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(2)
    root.left.right = Node(7)
    root.right.left = Node(12)
    root.right.right = Node(20)

    traversal_result = tree.post_traversal(root, [])
    
    return render_template("post_order.html", member=member_name, traversal=traversal_result)




if __name__ == '__main__':
    website.run(debug=True)
