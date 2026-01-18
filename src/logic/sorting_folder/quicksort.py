def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    print (f"Pivot: {pivot}")

    left = [x for x in arr[1:] if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr[1:] if x > pivot]
    print (f"left: {left} middle: {middle}  right: {right}")

    return quick_sort(left) + middle + quick_sort(right)


