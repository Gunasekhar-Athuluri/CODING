"""The Kth permutation refers to the K-th arrangement of a given set of elements (usually a set of numbers) in a particular order. Essentially, the Kth permutation is the permutation that appears in the Kth position when all the permutations of the set are listed in lexicographical (dictionary) order."""

import math

def find_kth_permutation(n, k):
    # List of numbers to work with
    numbers = [i for i in range(1, n+1)]
    
    # Decrease k by 1 to make it zero-indexed
    k -= 1
    
    # Resultant permutation
    result = []
    
    # We need to find the k-th permutation
    for i in range(n, 0, -1):
        # Calculate the factorial of (i-1)
        fact = math.factorial(i - 1)
        
        # Find the index of the number to add to the result
        index = k // fact
        result.append(numbers.pop(index))
        
        # Update k to find the next number
        k %= fact
    
    # Return the result as a string
    return ''.join(map(str, result))

# Example usage:
n = 3
k = 4
print(f"The {k}th permutation of the set [1, 2, 3] is: {find_kth_permutation(n, k)}")



"""
Example:
Consider the set of numbers [1, 2, 3]. The permutations of this set, listed in lexicographical order (ascending order), are as follows:

123
132
213
231
312
321
Now, if we want the 4th permutation, it is 231.
"""
