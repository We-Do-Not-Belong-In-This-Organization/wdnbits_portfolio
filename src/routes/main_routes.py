from flask import Blueprint, render_template, request


main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def home():
    """Renders the website's homepage (Landing Page).

    Returns:
        Rendered HTML template for index.html.
    """
    return render_template("index.html") 


@main_bp.route("/profile")
def profile():
    """Renders the main profile selection page.

    This function defines the list of team members (characters) and their 
    associated image assets (main image, left/right aesthetic images) 
    to be displayed on the profile grid.

    Returns:
        Rendered HTML template for profile.html with the characters list.
    """
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


@main_bp.route("/works")
def worksoon():
    """Renders a 'Coming Soon' placeholder page for incomplete sections.

    Query Parameters:
        from_page (str, optional): Navigation origin tracker.

    Returns:
        Rendered HTML template for coming-soon.html.
    """
    from_page = request.args.get("from_page", None)
    return render_template("coming-soon.html", from_page=from_page)


# 🔹 Route for each member’s HTML
@main_bp.route("/profile/<name>")
def profile_member(name):
    """Dynamically renders the individual profile page for a specific team member.

    Parameters:
        name (str): The specific name/ID of the member (e.g., 'ced', 'james').

    Returns:
        Rendered HTML template for the specific member.
        String Error: "Profile not found" with 404 status code if template is missing.
    """
    try:
        return render_template(f"member_profiles/{name}.html", member=name)
    except Exception as e:
        print("⚠️ Error:", e)
        return "Profile not found", 404




@main_bp.route("/trees")
def trees_page():
    """Renders the main navigation hub for Tree data structures.

    Query Parameters:
        from_page (str, optional): Navigation origin tracker.

    Returns:
        Rendered HTML template for trees.html.
    """
    from_page = request.args.get("from_page", "")
    return render_template("works/trees.html", from_page=from_page)