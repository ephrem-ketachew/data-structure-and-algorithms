# 92. Reverse Linked List II
# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]

# Example 2:
# Input: head = [5], left = 1, right = 1
# Output: [5]
 
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy_node = ListNode()
        dummy_node.next = head
        previous = dummy_node
        for _ in range(left - 1):
            previous = previous.next
        
        before = None
        current = previous.next
        reversed_tail = current
        for _ in range(right - left +1):
            after = current.next
            current.next = before
            before = current
            current = after
        
        previous.next = before
        if not reversed_tail == current:
            reversed_tail.next = current
        return dummy_node.next