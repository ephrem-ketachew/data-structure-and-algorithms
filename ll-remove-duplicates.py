# LL Remove Duplicates
# You are given a singly linked list that contains integer values, where some of these values may be duplicated.

# Your task is to implement a method called remove_duplicates() within the LinkedList class that removes all duplicate values from the list.

# Your method should not create a new list, but rather modify the existing list in-place, preserving the relative order of the nodes.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_duplicates(head):
    if not head:
        return None
    
    previous = head
    current = head.next
    seen = set([previous.val])
    while current:
        if current.val in seen:
            previous.next = current.next
        else:
            seen.add(current.val)
            previous = current
        current = current.next
        
    return head