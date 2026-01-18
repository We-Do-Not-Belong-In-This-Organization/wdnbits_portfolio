from flask import Blueprint, render_template, request

# UPDATED IMPORTS: Now importing from all four files
from src.logic.sorting_folder.insertion import insertion_sort
from src.logic.sorting_folder.merge import merge_sort
from src.logic.bubble_sort import bubble_sort
from src.logic.selection_sort import selection_sort

sorting_bp = Blueprint('sorting', __name__)


# ==========================================
# 1. The Menu Page
# ==========================================
@sorting_bp.route('/sorting')
def sorting_menu():
    return render_template('works/sorting_menu.html')


# ==========================================
# 2. Insertion Sort Page
# ==========================================
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


# ==========================================
# 3. Merge Sort Page
# ==========================================
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


# ==========================================
# 4. Bubble Sort Page (Converted to match)
# ==========================================
@sorting_bp.route('/sorting/bubble', methods=['GET', 'POST'])
def bubble_page():
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
                sorted_numbers = bubble_sort(number_list)

        except ValueError:
            error = "Invalid input! Make sure you only enter numbers and commas."
    
    return render_template('works/bubble.html', result=sorted_numbers, original=original_input, error=error)


# ==========================================
# 5. Selection Sort Page (Converted to match)
# ==========================================
@sorting_bp.route('/sorting/selection', methods=['GET', 'POST'])
def selection_page():
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
                sorted_numbers = selection_sort(number_list)

        except ValueError:
            error = "Invalid input! Make sure you only enter numbers and commas."
    
    return render_template('works/selection.html', result=sorted_numbers, original=original_input, error=error)

# 6. Quick Sort Page
@sorting_bp.route('/sorting/quicksort', methods=['GET', 'POST'])
def quicksort_page():
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
                sorted_numbers = quick_sort(number_list)

        except ValueError:
            error = "Invalid input! Make sure you only enter numbers and commas."
    
    return render_template('works/quicksort.html', result=sorted_numbers, original=original_input, error=error)