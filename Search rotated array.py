"""Search for a given number in a sorted array, with unique elements, that has been rotated by some arbitrary number. Return -1 if the number does not exist. Assume that the array does not contain duplicates."""

def search_rotated_array(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        
        # If we found the target
        if arr[mid] == target:
            return mid
        
        # If the left part is sorted
        if arr[left] <= arr[mid]:
            # Target lies between left and mid
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # If the right part is sorted
        else:
            # Target lies between mid and right
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1  # Target not found

# Example test cases:
arr1 = [15, 18, 2, 3, 6, 12]
target1 = 3
print(search_rotated_array(arr1, target1))  # Output: 3 (target 3 is at index 3)

arr2 = [4, 5, 6, 7, 0, 1, 2]
target2 = 0
print(search_rotated_array(arr2, target2))  # Output: 4 (target 0 is at index 4)

arr3 = [4, 5, 6, 7, 0, 1, 2]
target3 = 3
print(search_rotated_array(arr3, target3))  # Output: -1 (target 3 is not in the array)

arr4 = [30, 40, 50, 10, 20]
target4 = 10
print(search_rotated_array(arr4, target4))  # Output: 3 (target 10 is at index 3)
