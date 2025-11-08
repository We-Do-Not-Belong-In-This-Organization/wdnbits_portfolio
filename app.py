# pip install Flask
# Two lines spacing for each route

from flask import Flask, render_template


website = Flask(__name__)

# For Navigation Bar


# Home Page
@website.route("/home")
def home():
    return render_template("index.html") 


@website.route("/")
def profile():
    characters = [
        'img1.jpg', 'img2.jpg', 'img3.jpg', 'img4.jpg', 'img5.jpg',
        'img6.jpg', 'img7.jpg', 'img8.jpg', 'img9.jpg', 'img10.jpg'
    ]
    return render_template("profile.html", characters=characters)  # Change #profile.html per member


@website.route("/works")
def works():
    return render_template("#works.html")  # Change #works.html per member


@website.route("/Contacts")
def contacts():
    return render_template("#contacts.html")  # Change #contacts.html per member

# End of Navigation bar

# Each Profile, can be copy and pasted

@website.route("/routemember")
def profile_member():
    return render_template("#member.html")


if __name__ == '__main__':
    website.run(debug=True)
