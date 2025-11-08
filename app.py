# pip install Flask
# Two lines spacing for each route

from flask import Flask, render_template


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


# 🔹 Route for each member’s individual HTML file
@website.route("/profile/<name>")
def profile_member(name):
    try:
        return render_template(f"member_profiles/{name}.html")
    except:
        return "Profile not found", 404


if __name__ == '__main__':
    website.run(debug=True)
