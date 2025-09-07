def mergesort(arr):
    """
    Sorts an array using the merge sort algorithm (in-place).
    Args:
        arr (list): List of elements to sort.
    Returns:
        list: Sorted list.
    """
    # Base case: if the array has more than one element
    if len(arr) > 1:
        # Find the middle index
        mid = len(arr) // 2
        # Split the array into two halves
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        mergesort(left_half)
        mergesort(right_half)

        # Merge the sorted halves
        i = j = k = 0

        # Compare elements from both halves and copy the smaller one
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy any remaining elements from left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy any remaining elements from right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Sample example usage:
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", arr)
    sorted_arr = mergesort(arr)
    print("Sorted array:", sorted_arr)
    # Output should be a sorted array