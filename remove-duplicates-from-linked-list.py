# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def deleteDuplicates(head):
    current = head
    while current and current.next:
        next = current.next
        if current.val == next.val:
            if next.next:
                current.next = next.next
                del next
            else:
                current.next = None
        else:
            current = current.next
    return head
        