# pip install Flask
# Two lines spacing for each route

from flask import Flask, render_template, request, redirect, url_for
from queues import Queue  # Import the Queue class from static folder

website = Flask(__name__)

# For Navigation Bar


# Home Page
@website.route("/")
def home():
    return render_template("index.html") 


@website.route("/profile")
def profile():
    # Each image and its matching HTML file (same order)
    characters = [
        {"img": "img1.jpg", "page": "ced"},
        {"img": "img2.jpg", "page": "deqs"},
        {"img": "img3.jpg", "page": "hassan"},
        {"img": "img4.jpg", "page": "ian"},
        {"img": "img5.jpg", "page": "james"},
        {"img": "img6.jpg", "page": "jayvee"},
        {"img": "img7.jpg", "page": "jed"},
        {"img": "img8.jpg", "page": "laei"},
        {"img": "img9.jpg", "page": "marx"},
        {"img": "img10.jpg", "page": "matt"}
    ]
    return render_template("profile.html", characters=characters)


@website.route("/works")
def works():
    return render_template("#works.html")  # Change #works.html per member

# For members, copy and paste this to your own portfolio including the 'queue.html' and 'dequeue.html" file
queue_line = Queue()


@website.route('/queue')
def queue():
    return render_template('queue.html', queue_line=queue_line)


@website.route('/enqueue', methods=['POST'])
def enqueue():
    item = request.form.get('user_enqueue')
    if item:
        queue_line.enqueue(item)
    return redirect(url_for('queue'))


@website.route('/dequeue', methods=['POST'])
def dequeue():
    if not queue_line.is_empty():
        queue_line.dequeue()
    return redirect(url_for('queue'))


# End of Queue


# Start of DEqueue


dequeue_line = []


@website.route('/DEqueue')
def dob_queue():
    return render_template('dequeue.html', dequeue_line=dequeue_line)

@website.route('/enqueue_left', methods=['POST'])
def enqueue_left():
    item = request.form.get('user_enqueue')
    if item:
        dequeue_line.append(item)
    return redirect(url_for('dob_queue'))


@website.route('/dequeue_right', methods=['POST'])
def dequeue_right():
    if dequeue_line:
        dequeue_line.pop(0)
    return redirect(url_for('dob_queue'))


@website.route('/enqueue_head', methods=['POST'])
def enqueue_head():
    item = request.form.get('user_enqueue')
    if item:
        dequeue_line.insert(0, item)
    return redirect(url_for('dob_queue'))

@website.route('/dequeue_tail', methods=['POST'])
def dequeue_tail():
    if dequeue_line:
        dequeue_line.pop()
    return redirect(url_for('dob_queue'))



# End of DEqueue


# 🔹 Route for each member’s individual HTML file
@website.route("/profile/<name>")
def profile_member(name):
    print("🔍 Trying to open:", f"member_profiles/{name}.html")
    try:
        return render_template(f"member_profiles/{name}.html")
    except Exception as e:
        print("⚠️ Error:", e)
        return "Profile not found", 404


if __name__ == '__main__':
    website.run(debug=True)
