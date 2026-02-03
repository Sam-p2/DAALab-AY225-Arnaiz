"""
Sorting Algorithms Module
Contains implementations of Bubble Sort, Insertion Sort, and Merge Sort
"""


def bubble_sort(arr):
    """
    Bubble Sort: O(n^2) exchange sort
    Repeatedly steps through the list, compares adjacent elements and swaps them if they're in the wrong order.
    
    Args:
        arr: List of elements to sort
    
    Returns:
        The sorted list (modifies in-place)
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def insertion_sort(arr):
    """
    Insertion Sort: O(n^2) comparison sort
    Builds the final sorted array one item at a time by inserting each element into its correct position.
    
    Args:
        arr: List of elements to sort
    
    Returns:
        The sorted list (modifies in-place)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    """
    Merge Sort: O(n log n) divide-and-conquer algorithm
    Divides the array into halves, recursively sorts them, and merges the sorted halves.
    
    Args:
        arr: List of elements to sort
    
    Returns:
        The sorted list
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return _merge(left, right)


def _merge(left, right):
    """
    Helper function for merge sort that merges two sorted lists.
    
    Args:
        left: Left sorted subarray
        right: Right sorted subarray
    
    Returns:
        Merged sorted array
    """
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


def is_sorted(arr):
    """
    Verify that an array is sorted in ascending order.
    
    Args:
        arr: List to verify
    
    Returns:
        True if sorted, False otherwise
    """
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
