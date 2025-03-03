"""Given the root of a binary tree, display the node values at each level. Node values for all levels should be displayed on separate lines."""
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def level_order_traversal(root: TreeNode):
    if not root:
        return []
    
    levels = []  # This will store the result of the level order traversal
    queue = deque([root])  # Queue to process nodes level by level
    
    while queue:
        level_size = len(queue)  # Number of nodes at the current level
        current_level_values = []  # List to store the values of the current level
        
        for _ in range(level_size):
            current_node = queue.popleft()  # Remove the front node from the queue
            current_level_values.append(current_node.value)  # Add its value to the current level
            
            # Add the left and right children of the current node to the queue
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        
        levels.append(current_level_values)  # Append the current level's values to the final result
    
    return levels

# Helper function to print the level order traversal
def print_level_order(root):
    levels = level_order_traversal(root)
    for level in levels:
        print(" ".join(map(str, level)))

# Example usage:
# Create the binary tree:
#         1
#        / \
#       2   3
#      / \   \
#     4   5   6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

# Print level order traversal
print_level_order(root)
