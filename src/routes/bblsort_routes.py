from flask import Blueprint, request, render_template_string
from src.logic.bubble_sort import bubble_sort
from src.logic.selection_sort import selection_sort

# -----------------------------
# Bubble Sort Blueprint
# -----------------------------
bblsort_bp = Blueprint('bblsort', __name__, url_prefix='/bubble')


@bblsort_bp.route("/", methods=["GET"])
def bubble_page():
    numbers = request.args.get("numbers", "")
    sorted_arr = []
    if numbers:
        try:
            arr = [int(x) for x in numbers.replace(",", " ").split()]
            sorted_arr = bubble_sort(arr)
        except ValueError:
            return "Error: Only enter numbers separated by commas or spaces", 400

    return f"Original: {numbers} <br> Sorted: {sorted_arr}"


@bblsort_bp.route("/ui", methods=["GET", "POST"])
def bubble_ui():
    sorted_arr = None
    numbers = ""
    if request.method == "POST":
        numbers = request.form.get("numbers", "")
        if numbers:
            try:
                arr = [int(x) for x in numbers.replace(",", " ").split()]
                sorted_arr = bubble_sort(arr)
            except ValueError:
                sorted_arr = "Error: Only enter numbers separated by commas or spaces"

    return render_template_string("""
        <h2>Bubble Sort</h2>
        <form method="post">
            <input type="text" name="numbers" placeholder="Enter numbers, e.g. 5,3 8,1" 
                   value="{{ numbers }}" size="40">
            <button type="submit">Sort</button>
        </form>

        {% if sorted_arr is not none %}
            <p><strong>Original:</strong> {{ numbers }}</p>
            <p><strong>Sorted:</strong> {{ sorted_arr }}</p>
        {% endif %}
    """, numbers=numbers, sorted_arr=sorted_arr)


# -----------------------------
# Selection Sort Blueprint
# -----------------------------
selection_bp = Blueprint('selectionsort', __name__, url_prefix='/selection')


@selection_bp.route("/", methods=["GET"])
def selection_page():
    numbers = request.args.get("numbers", "")
    sorted_arr = []
    if numbers:
        try:
            arr = [int(x) for x in numbers.replace(",", " ").split()]
            sorted_arr = selection_sort(arr)
        except ValueError:
            return "Error: Only enter numbers separated by commas or spaces", 400

    return f"Original: {numbers} <br> Sorted: {sorted_arr}"


@selection_bp.route("/ui", methods=["GET", "POST"])
def selection_ui():
    sorted_arr = None
    numbers = ""
    if request.method == "POST":
        numbers = request.form.get("numbers", "")
        if numbers:
            try:
                arr = [int(x) for x in numbers.replace(",", " ").split()]
                sorted_arr = selection_sort(arr)
            except ValueError:
                sorted_arr = "Error: Only enter numbers separated by commas or spaces"

    return render_template_string("""
        <h2>Selection Sort</h2>
        <form method="post">
            <input type="text" name="numbers" placeholder="Enter numbers, e.g. 5,3 8,1" 
                   value="{{ numbers }}" size="40">
            <button type="submit">Sort</button>
        </form>

        {% if sorted_arr is not none %}
            <p><strong>Original:</strong> {{ numbers }}</p>
            <p><strong>Sorted:</strong> {{ sorted_arr }}</p>
        {% endif %}
    """, numbers=numbers, sorted_arr=sorted_arr)
