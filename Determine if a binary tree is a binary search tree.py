"""Given a Binary Tree, figure out whether it’s a Binary Search Tree. In a binary search tree, each node’s key value is smaller than the key value of all nodes in the right subtree, and is greater than the key values of all nodes in the left subtree."""

import collections

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# BFS algorithm to check if the tree is a Binary Search Tree (BST)
def bfs_is_bst(root: TreeNode) -> bool:
    if not root:
        return True
    
    # Queue stores tuples of (node, min_value, max_value)
    queue = collections.deque([(root, float('-inf'), float('inf'))])
    
    while queue:
        node, min_value, max_value = queue.popleft()

        # Check if the current node's value is within the valid range
        if not (min_value < node.value < max_value):
            return False
        
        # Enqueue left child with updated max_value
        if node.left:
            queue.append((node.left, min_value, node.value))
        
        # Enqueue right child with updated min_value
        if node.right:
            queue.append((node.right, node.value, max_value))
    
    return True

# Helper function to check and print if the tree is a BST
def check_if_bst(root):
    if bfs_is_bst(root):
        print("The tree is a Binary Search Tree (BST).")
    else:
        print("The tree is NOT a Binary Search Tree (BST).")

# Example usage:
# Create a binary tree:
#         10
#        /  \
#       5    15
#      / \     \
#     3   7     20

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(20)

# Check if the tree is a BST
check_if_bst(root)

