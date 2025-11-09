# pip install Flask
# Two lines spacing for each route

from flask import Flask, render_template, request, redirect, url_for

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
    return render_template("#works.html")  # Change #works.html per member

# For members, copy and paste this to your own portfolio including the 'queue.html' and 'dequeue.html" file
queue_line = []


@website.route('/queue')
def queue():
    return render_template('queue.html', queue_line=queue_line)


@website.route('/enqueue', methods=['POST'])
def enqueue():
    item = request.form.get('user_enqueue')
    if item:
        queue_line.append(item)
    return redirect(url_for('queue'))


@website.route('/dequeue', methods=['POST'])
def dequeue():
    if queue_line:
        queue_line.pop(0)
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
