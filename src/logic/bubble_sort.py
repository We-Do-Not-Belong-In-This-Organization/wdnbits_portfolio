def bubble_sort(arr):
    """Sort a list in ascending order using Bubble Sort."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:  # swap if out of order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr