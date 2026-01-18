from flask import Blueprint, render_template, request

from src.logic.sorting_folder.insertion import insertion_sort
from src.logic.sorting_folder.merge import merge_sort
from src.logic.bubble_sort import bubble_sort
from src.logic.selection_sort import selection_sort
from src.logic.sorting_folder.quicksort import quick_sort   # ← make sure this exists

sorting_bp = Blueprint('sorting', __name__)

# -----------------------------
# Sorting Menu
# -----------------------------
@sorting_bp.route('/sorting')
def sorting_menu():
    return render_template('works/sorting_menu.html')

# -----------------------------
# Insertion Sort
# -----------------------------
@sorting_bp.route('/sorting/insertion', methods=['GET', 'POST'])
def insertion_page():
    result = None
    original = ""
    error = None

    if request.method == 'POST':
        original = request.form.get('numbers', '')
        try:
            numbers = [int(x.strip()) for x in original.split(',') if x.strip()]
            if not numbers:
                error = "Please enter at least one number."
            else:
                result = insertion_sort(numbers)
        except ValueError:
            error = "Invalid input! Use numbers separated by commas."

    return render_template('works/insertion.html',
                           result=result,
                           original=original,
                           error=error)

# -----------------------------
# Merge Sort
# -----------------------------
@sorting_bp.route('/sorting/merge', methods=['GET', 'POST'])
def merge_page():
    result = None
    original = ""
    error = None

    if request.method == 'POST':
        original = request.form.get('numbers', '')
        try:
            numbers = [int(x.strip()) for x in original.split(',') if x.strip()]
            if not numbers:
                error = "Please enter at least one number."
            else:
                result = merge_sort(numbers)
        except ValueError:
            error = "Invalid input! Use numbers separated by commas."

    return render_template('works/merge.html',
                           result=result,
                           original=original,
                           error=error)

# -----------------------------
# Bubble Sort
# -----------------------------
@sorting_bp.route('/sorting/bubble', methods=['GET', 'POST'])
def bubble_page():
    result = None
    original = ""
    error = None

    if request.method == 'POST':
        original = request.form.get('numbers', '')
        try:
            numbers = [int(x.strip()) for x in original.replace(',', ' ').split()]
            if not numbers:
                error = "Please enter at least one number."
            else:
                result = bubble_sort(numbers)
        except ValueError:
            error = "Invalid input! Use numbers only."

    return render_template('works/bubble.html',
                           result=result,
                           original=original,
                           error=error)

# -----------------------------
# Selection Sort
# -----------------------------
@sorting_bp.route('/sorting/selection', methods=['GET', 'POST'])
def selection_page():
    result = None
    original = ""
    error = None

    if request.method == 'POST':
        original = request.form.get('numbers', '')
        try:
            numbers = [int(x.strip()) for x in original.replace(',', ' ').split()]
            if not numbers:
                error = "Please enter at least one number."
            else:
                result = selection_sort(numbers)
        except ValueError:
            error = "Invalid input! Use numbers only."

    return render_template('works/selection.html',
                           result=result,
                           original=original,
                           error=error)

# -----------------------------
# Quick Sort
# -----------------------------
@sorting_bp.route('/sorting/quicksort', methods=['GET', 'POST'])
def quicksort_page():
    result = None
    original = ""
    error = None

    if request.method == 'POST':
        original = request.form.get('numbers', '')
        try:
            numbers = [int(x.strip()) for x in original.split(',') if x.strip()]
            if not numbers:
                error = "Please enter at least one number."
            else:
                result = quick_sort(numbers)
        except ValueError:
            error = "Invalid input! Use numbers separated by commas."

    return render_template('works/quicksort.html',
                           result=result,
                           original=original,
                           error=error)
