# DLL Swap Nodes in Pairs ( Interview Question)
# Instructions
# You are given a doubly linked list.

# Implement a method called swap_pairs within the class that swaps the values of adjacent nodes in the linked list. 
# Note: This DoublyLinkedList does not have a tail pointer which will make the implementation easier.

# Example:

# 1 <-> 2 <-> 3 <-> 4 should become 2 <-> 1 <-> 4 <-> 3

# Your implementation should handle edge cases such as an empty linked list or a linked list with only one node.

# Note: You must solve the problem WITHOUT MODIFYING THE VALUES in the list's nodes (i.e., only the nodes' prev and next pointers may be changed.)

def swap_pairs(head):
    if head is None or head.next is None:
        return head
    before = None
    cur_left = head
    new_head = cur_right = cur_left.next
    while cur_right:
        after = cur_right.next
        cur_left.next = after
        if after:
            after.prev = cur_left
        cur_right.prev = before
        if before:
            before.next = cur_right
        cur_right.next = cur_left
        cur_left.prev = cur_right
        
        before = cur_left
        cur_left = after
        if after:
            cur_right = after.next
        else:
            break
        
    return new_head