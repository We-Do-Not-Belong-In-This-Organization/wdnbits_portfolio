def insertion_sort(arr):
    """
    Sorts a list using the Insertion Sort algorithm.
    """
    # We work on a copy to avoid messing up original data
    nums = arr.copy()
    
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        
        # Move elements greater than key one position ahead
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
        
    return nums