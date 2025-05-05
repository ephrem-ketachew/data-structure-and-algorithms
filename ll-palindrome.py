# Palindrome Linked List
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Example 1:
# Input: head = [1,2,2,1]
# Output: true
# Example 2:
# Input: head = [1,2]
# Output: false
 
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True
        
        node = None
        current = head
        while current:
            reversed_head = ListNode(current.val)
            reversed_head.next = node
            node = reversed_head
            current = current.next
        
        left = head
        right = reversed_head
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True