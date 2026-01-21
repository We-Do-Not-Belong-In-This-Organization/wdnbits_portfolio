from flask import Blueprint, render_template, request
from src.logic.sorting_folder.insertion import insertion_sort
from src.logic.sorting_folder.merge import merge_sort
from src.logic.sorting_folder.bubble_sort import bubble_sort
from src.logic.sorting_folder.selection_sort import selection_sort
from src.logic.sorting_folder.quicksort import quick_sort

sorting_bp = Blueprint('sorting', __name__)

@sorting_bp.route('/sorting', methods=['GET', 'POST'])
def sorting_menu():
    """Handles the sorting algorithm demonstration page.

    Displays a form for users to input numbers and select a sorting
    algorithm, then processes the input and returns the sorted result.
    Supports multiple sorting algorithms and basic input validation.

    Returns:
        Rendered HTML template for sorting_menu.html containing:
        - The sorted result (if available)
        - The original user input
        - Any error messages
        - The selected sorting algorithm
        - The originating page for navigation
    """
    sorted_numbers = None
    original_input = ""
    error = None
    selected_algo = None
    
    # Capture 'from_page' so we know where to go back to (e.g., 'matt')
    from_page = request.args.get('from_page') 

    if request.method == 'POST':
        original_input = request.form.get('numbers')
        selected_algo = request.form.get('algo')
        
        # If from_page is lost during POST, try to get it from the URL again
        if not from_page:
            from_page = request.args.get('from_page')

        try:
            if not original_input:
                 error = "Please enter some numbers first."
            else:
                # Handle comma or space separated numbers
                clean_str = original_input.replace(' ', ',')
                number_list = [int(x.strip()) for x in clean_str.split(',') if x.strip()]
                
                if not number_list:
                    error = "Please enter valid numbers."
                else:
                    # Logic to run the correct algorithm
                    if selected_algo == 'insertion':
                        sorted_numbers = insertion_sort(number_list)
                    elif selected_algo == 'merge':
                        sorted_numbers = merge_sort(number_list)
                    elif selected_algo == 'bubble':
                        sorted_numbers = bubble_sort(number_list)
                    elif selected_algo == 'selection':
                        sorted_numbers = selection_sort(number_list)
                    elif selected_algo == 'quick':
                        sorted_numbers = quick_sort(number_list)

        except ValueError:
            error = "Invalid input! Only enter numbers separated by commas or spaces."
        except Exception as e:
            error = f"An error occurred: {str(e)}"

    # Pass everything back to the HTML
    return render_template('works/sorting_menu.html', 
                           result=sorted_numbers, 
                           original=original_input, 
                           error=error,
                           algo=selected_algo,
                           from_page=from_page)