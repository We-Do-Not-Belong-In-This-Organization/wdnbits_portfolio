def quick_sort(arr):
    # Base case
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = [x for x in arr[1:] if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr[1:] if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)
