from flask import Blueprint, render_template, request

# UPDATED IMPORTS: Now importing from two separate files
from src.logic.sorting_folder.insertion import insertion_sort
from src.logic.sorting_folder.merge import merge_sort
from src.logic.bubble_sort import bubble_sort
from src.logic.selection_sort import selection_sort

sorting_bp = Blueprint('sorting', __name__)

# 1. The Menu Page
@sorting_bp.route('/sorting')
def sorting_menu():
    return render_template('works/sorting_menu.html')

# 2. Insertion Sort Page
@sorting_bp.route('/sorting/insertion', methods=['GET', 'POST'])
def insertion_page():
    sorted_numbers = None
    original_input = ""
    error = None

    if request.method == 'POST':
        original_input = request.form.get('numbers')
        try:
            # Clean input: ignore empty items from trailing commas
            number_list = [int(x.strip()) for x in original_input.split(',') if x.strip()]
            
            if not number_list:
                error = "Please enter at least one number."
            else:
                sorted_numbers = insertion_sort(number_list)

        except ValueError:
            error = "Invalid input! Make sure you only enter numbers and commas."
    
    return render_template('works/insertion.html', result=sorted_numbers, original=original_input, error=error)

# 3. Merge Sort Page
@sorting_bp.route('/sorting/merge', methods=['GET', 'POST'])
def merge_page():
    sorted_numbers = None
    original_input = ""
    error = None

    if request.method == 'POST':
        original_input = request.form.get('numbers')
        try:
            # Clean input: ignore empty items from trailing commas
            number_list = [int(x.strip()) for x in original_input.split(',') if x.strip()]
            
            if not number_list:
                error = "Please enter at least one number."
            else:
                sorted_numbers = merge_sort(number_list)

        except ValueError:
            error = "Invalid input! Make sure you only enter numbers and commas."
    
    return render_template('works/merge.html', result=sorted_numbers, original=original_input, error=error)

from flask import Blueprint, request, render_template_string
from src.logic.bubble_sort import bubble_sort
from src.logic.selection_sort import selection_sort

# -----------------------------
# 4 Bubble Sort Blueprint
# -----------------------------
bblsort_bp = Blueprint('bblsort', __name__, url_prefix='/bubble')

@bblsort_bp.route("/", methods=["GET", "POST"])
def bubble_page():
    original = ""
    result = None
    error = None

    if request.method == "POST":
        original = request.form.get("numbers", "")
        try:
            numbers = [int(x.strip()) for x in original.replace(",", " ").split() if x.strip()]
            if not numbers:
                error = "Please enter at least one number."
            else:
                result = bubble_sort(numbers)
        except ValueError:
            error = "Invalid input! Only enter numbers separated by commas or spaces."

    return render_template('works/bubble.html', original=original, result=result, error=error)

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
# 5 Selection Sort Blueprint
# -----------------------------
selection_bp = Blueprint('selectionsort', __name__, url_prefix='/selection')

@selection_bp.route("/", methods=["GET", "POST"])
def selection_page():
    original = ""
    result = None
    error = None

    if request.method == "POST":
        original = request.form.get("numbers", "")
        try:
            numbers = [int(x.strip()) for x in original.replace(",", " ").split() if x.strip()]
            if not numbers:
                error = "Please enter at least one number."
            else:
                result = selection_sort(numbers)
        except ValueError:
            error = "Invalid input! Only enter numbers separated by commas or spaces."

    return render_template('works/selection.html', original=original, result=result, error=error)


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
