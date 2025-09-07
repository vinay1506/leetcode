def quicksort(arr):
    # If the array has 0 or 1 elements, it's already sorted
    if len(arr) <= 1:
        return arr
    # Choose the middle element as the pivot
    pivot = arr[len(arr) // 2]
    # Elements less than pivot
    left = [x for x in arr if x < pivot]
    # Elements equal to pivot
    middle = [x for x in arr if x == pivot]
    # Elements greater than pivot
    right = [x for x in arr if x > pivot]
    # Recursively sort left and right, then combine
    return quicksort(left) + middle + quicksort(right)

# Sample example usage:
if __name__ == "__main__":
    arr = [3, 6, 8, 10, 1, 2, 1]
    print("Original array:", arr)
    sorted_arr = quicksort(arr)
    print("Sorted array:", sorted_arr)
    # Output: [1, 1, 2, 3, 6, 8, 10]
