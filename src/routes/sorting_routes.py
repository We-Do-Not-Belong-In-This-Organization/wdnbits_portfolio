from flask import Blueprint, render_template, request
from src.logic.sorting_folder.insertion import insertion_sort, merge_sort

sorting_bp = Blueprint('sorting', __name__)

# 1. The Menu Page
@sorting_bp.route('/sorting')
def sorting_menu():
    # FIXED: Added 'works/' so Flask finds it in the right folder
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
            number_list = [int(x.strip()) for x in original_input.split(',')]
            sorted_numbers = insertion_sort(number_list)
        except ValueError:
            error = "Invalid input! Please enter numbers separated by commas."
    
    # FIXED: Added 'works/'
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
            number_list = [int(x.strip()) for x in original_input.split(',')]
            sorted_numbers = merge_sort(number_list)
        except ValueError:
            error = "Invalid input! Please enter numbers separated by commas."
    
    # FIXED: Added 'works/'
    return render_template('works/merge.html', result=sorted_numbers, original=original_input, error=error)