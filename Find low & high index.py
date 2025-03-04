"""Given a sorted array of integers, return the low and high index of the given key. You must return -1 if the indexes are not found. The array length can be in the millions with many duplicates."""

"""1,2,5,5,5,5,5,5,5,5,20"""

"""
key: 1, low = 0 and high = 0
key: 2, low = 1 and high = 1
key: 5, low = 2 and high = 9
key: 20, low = 10 and high = 10
"""

def find_low_high(arr, key):
    def find_first(arr, key):
        low, high = 0, len(arr) - 1
        result = -1
        
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == key:
                result = mid
                high = mid - 1  # Continue searching to the left
            elif arr[mid] < key:
                low = mid + 1
            else:
                high = mid - 1
                
        return result

    def find_last(arr, key):
        low, high = 0, len(arr) - 1
        result = -1
        
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == key:
                result = mid
                low = mid + 1  # Continue searching to the right
            elif arr[mid] < key:
                low = mid + 1
            else:
                high = mid - 1
                
        return result

    # Find the low index (first occurrence)
    low_index = find_first(arr, key)
    if low_index == -1:
        return -1, -1  # If the key is not found
    
    # Find the high index (last occurrence)
    high_index = find_last(arr, key)
    
    return low_index, high_index


# Test cases:
arr = [1, 2, 5, 5, 5, 5, 5, 5, 5, 5, 20]

# Example 1: Find low and high index for key 1
key = 1
low, high = find_low_high(arr, key)
print(f"key: {key}, low = {low}, high = {high}")  # Expected: low = 0, high = 0

# Example 2: Find low and high index for key 2
key = 2
low, high = find_low_high(arr, key)
print(f"key: {key}, low = {low}, high = {high}")  # Expected: low = 1, high = 1

# Example 3: Find low and high index for key 5
key = 5
low, high = find_low_high(arr, key)
print(f"key: {key}, low = {low}, high = {high}")  # Expected: low = 2, high = 9

# Example 4: Find low and high index for key 20
key = 20
low, high = find_low_high(arr, key)
print(f"key: {key}, low = {low}, high = {high}")  # Expected: low = 10, high = 10







"""
To solve this problem efficiently, given that the array is sorted, we can use binary search to find the low and high indices of the given key.

Approach:
Low Index: Use binary search to find the first occurrence of the key.
High Index: Use binary search to find the last occurrence of the key.
Steps:
Low Index: We can modify the binary search to look for the first occurrence of the given key. If the middle element is equal to the key, we keep searching to the left (lower indices) until we find the first occurrence.
High Index: Similarly, we modify the binary search to look for the last occurrence of the key. If the middle element is equal to the key, we keep searching to the right (higher indices) until we find the last occurrence.
Binary Search for First Occurrence:
If the middle element is equal to the key, move left (i.e., set high = mid - 1) to check for earlier occurrences.
If the middle element is greater than the key, move left (high = mid - 1).
If the middle element is smaller than the key, move right (low = mid + 1).
Binary Search for Last Occurrence:
If the middle element is equal to the key, move right (i.e., set low = mid + 1) to check for later occurrences.
If the middle element is greater than the key, move left (high = mid - 1).
If the middle element is smaller than the key, move right (low = mid + 1).


"""

