def merge_sort(arr):
    """
    Sorts a list using the Merge Sort algorithm (Recursive).
    """
    if len(arr) <= 1:
        return arr

    # Divide the array elements into 2 halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort the halves
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Merge the sorted halves
    return _merge(sorted_left, sorted_right)


def _merge(left, right):
    """Helper function to merge two sorted lists."""
    sorted_list = []
    i = j = 0

    # Compare elements from both lists and append smaller one
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Append any remaining elements
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list