def quick_sort(arr):
    """Sorts a list of elements in ascending order using the Quick Sort algorithm."""
    # Base case
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = [x for x in arr[1:] if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr[1:] if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)
