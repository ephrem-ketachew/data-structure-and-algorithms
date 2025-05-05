# DLL Swap First and Last ( Interview Question)
# Instructions
# Swap the values of the first and last node

# Method name:
# swap_first_last

# Note that the pointers to the nodes themselves are not swapped - only their values are exchanged.

def swap_first_last(l):
    if l.head is None or l.head.next is None:
        return
    temp = l.head
    current = l.head
    while current.next:
        current = current.next
    l.head.value = current.value
    current.value = temp.value