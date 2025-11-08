# pip install Flask
# Two lines spacing for each route

from flask import Flask, render_template


website = Flask(__name__)

# For Navigation Bar


# Home Page
@website.route("/")
def home():
    return render_template("home.html") 


@website.route("/AboutUs")
def profile():
    return render_template("#profile.html")  # Change #profile.html per member


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
