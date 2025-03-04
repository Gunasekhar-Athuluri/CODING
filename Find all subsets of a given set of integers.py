"""We are given a set of integers and we have to find all the possible subsets of this set of integers."""

"""BACKTRACKING"""

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
