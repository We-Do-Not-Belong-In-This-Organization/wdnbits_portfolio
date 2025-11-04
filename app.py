from flask import Flask, render_template

website = Flask(__name__)

@website.route("/")
def home_page():
    return render_template("homepage.html") 
        
# For Navigation Bar

@website.route("/home")
def home_page():
    return render_template("homepage.html") 

@website.route("/AboutUs")
def profile():
    return render_template("#profile.html")

@website.route("/works")
def works():
    return render_template("#works.html")

@website.route("/Contacts")
def contacts():
    return render_template("#contants.html")

# End of Navigation bar