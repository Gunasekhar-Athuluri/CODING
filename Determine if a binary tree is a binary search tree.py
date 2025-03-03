"""Given a Binary Tree, figure out whether it’s a Binary Search Tree. In a binary search tree, each node’s key value is smaller than the key value of all nodes in the right subtree, and is greater than the key values of all nodes in the left subtree."""

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_bst(root: TreeNode, min_val=float('-inf'), max_val=float('inf')) -> bool:
    # Base case: if the current node is None, it's a valid BST
    if not root:
        return True
    
    # The value of the current node must be within the range (min_val, max_val)
    if not (min_val < root.value < max_val):
        return False
    
    # Recursively check the left and right subtrees
    return (is_bst(root.left, min_val, root.value) and
            is_bst(root.right, root.value, max_val))

# Helper function to print the result
def check_bst(root):
    if is_bst(root):
        print("The tree is a Binary Search Tree (BST).")
    else:
        print("The tree is NOT a Binary Search Tree (BST).")

# Example usage:
# Creating a binary tree:
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
check_bst(root)

