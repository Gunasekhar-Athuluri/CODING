"""Print all braces combinations for a given value n so that they are balanced."""
"""
n = 3

{{{}}}
{{}{}} 
{}{}{}
{ { } }
{ }
{{}}
"""

"""BACKTRACKING"""

def generate_balanced_braces(n):
    def backtrack(current, open_count, close_count):
        # Base case: If the current string is of length 2*n and valid, print it
        if len(current) == 2 * n:
            print(current)
            return
        
        # If we can add an opening brace
        if open_count < n:
            backtrack(current + '{', open_count + 1, close_count)
        
        # If we can add a closing brace
        if close_count < open_count:
            backtrack(current + '}', open_count, close_count + 1)
    
    # Start the recursion with an empty string, 0 opening and 0 closing braces
    backtrack('', 0, 0)

# Example usage:
n = 3
generate_balanced_braces(n)

