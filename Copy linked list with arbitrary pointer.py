"""You are given a linked list where the node has two pointers. The first is the regular next pointer. The second pointer is called arbitrary and it can point to any node in the linked list. Your job is to write code to make a deep copy of the given linked list. Here, deep copy means that any operations on the original list should not affect the copied list."""

class Node:
    def __init__(self, val=0, next=None, arbitrary=None):
        self.val = val
        self.next = next
        self.arbitrary = arbitrary

def copyLinkedList(head):
    if not head:
        return None
    
    # Step 1: Insert copied nodes after each original node
    current = head
    while current:
        new_node = Node(current.val)
        new_node.next = current.next
        current.next = new_node
        current = new_node.next
    
    # Step 2: Set arbitrary pointers for the copied nodes
    current = head
    while current:
        if current.arbitrary:
            current.next.arbitrary = current.arbitrary.next
        current = current.next.next
    
    # Step 3: Separate the original list and the copied list
    current = head
    new_head = head.next
    while current:
        copy = current.next
        current.next = copy.next
        if copy.next:
            copy.next = copy.next.next
        current = current.next
    
    return new_head

# Helper function to print the list (for testing purposes)
def print_list(head):
    while head:
        arbitrary_val = head.arbitrary.val if head.arbitrary else None
        print(f"Value: {head.val}, Arbitrary: {arbitrary_val}")
        head = head.next

# Example usage:
# Creating the linked list: 1 -> 2 -> 3 with arbitrary pointers
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

node1.arbitrary = node3  # 1's arbitrary points to 3
node2.arbitrary = node1  # 2's arbitrary points to 1
node3.arbitrary = node2  # 3's arbitrary points to 2

# Copying the linked list
copied_head = copyLinkedList(node1)

# Print the original and copied list
print("Original List:")
print_list(node1)

print("\nCopied List:")
print_list(copied_head)
