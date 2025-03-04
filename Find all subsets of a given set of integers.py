"""We are given a set of integers and we have to find all the possible subsets of this set of integers."""



"""Using Backtracking"""
def find_subsets(nums):
    result = []
    
    def backtrack(start, current_subset):
        # Add the current subset to the result
        result.append(current_subset[:])
        
        # Explore further subsets by including each remaining element
        for i in range(start, len(nums)):
            # Include nums[i] in the subset
            current_subset.append(nums[i])
            # Recurse to add further elements
            backtrack(i + 1, current_subset)
            # Backtrack and remove nums[i] from the subset
            current_subset.pop()
    
    # Start backtracking with the first element
    backtrack(0, [])
    return result

# Example usage
nums = [1, 2, 3]
subsets = find_subsets(nums)
print(subsets)


"""Using Bit Manipulation"""
def find_subsets_bit_manipulation(nums):
    result = []
    n = len(nums)
    
    # Total number of subsets is 2^n
    for i in range(2 ** n):
        subset = []
        for j in range(n):
            # If the j-th bit is set in i, include nums[j] in the subset
            if (i & (1 << j)) > 0:
                subset.append(nums[j])
        result.append(subset)
    
    return result

# Example usage
nums = [1, 2, 3]
subsets = find_subsets_bit_manipulation(nums)
print(subsets)

