"""Given two sorted linked lists, merge them so that the resulting linked list is also sorted."""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    # Create a new dummy node that will help in simplifying the logic
    dummy = ListNode()
    current = dummy

    # Traverse both lists until one of them is exhausted
    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            current.next = l1  # Link to the smaller node (l1)
            l1 = l1.next  # Move to the next node in l1
        else:
            current.next = l2  # Link to the smaller node (l2)
            l2 = l2.next  # Move to the next node in l2

        current = current.next  # Move the current pointer to the newly added node

    # If one list is exhausted, append the other list to the result
    if l1 is not None:
        current.next = l1
    elif l2 is not None:
        current.next = l2

    # The dummy node's next points to the head of the merged list
    return dummy.next


# Helper function to print the linked list
def print_list(node: ListNode):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


# Example usage:
# List 1: 1 -> 2 -> 4
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

# List 2: 1 -> 3 -> 4
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

# Merge the lists
merged_list = mergeTwoLists(l1, l2)

# Print the merged list
print_list(merged_list)
