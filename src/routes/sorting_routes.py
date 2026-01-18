from flask import Blueprint, render_template, request

# UPDATED IMPORTS: Now importing from two separate files
from src.logic.sorting_folder.insertion import insertion_sort
from src.logic.sorting_folder.merge import merge_sort
from src.logic.sorting_folder.quicksort import quick_sort

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
