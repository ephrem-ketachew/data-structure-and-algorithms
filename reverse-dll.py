# 002 DLL Reverse ( Interview Question)
# Instructions
# Create a new method called reverse that reverses the order of the nodes in the list, i.e., the first node becomes the last node, the second node becomes the second-to-last node, and so on.

# To do this, you'll need to traverse the list and change the direction of the pointers between the nodes so that they point in the opposite direction.

# Do not change the value of any of the nodes.

def reverse_doubly_linked_list(head):
    if head is None or head.next is None:
        return head
    before = None
    current = head  
    while current:
        after = current.next
        current.next = before
        current.prev = after
        before = current
        current = after
    return before