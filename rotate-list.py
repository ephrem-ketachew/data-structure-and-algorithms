# 61. Rotate List
# Medium

# Given the head of a linked list, rotate the list to the right by k places.

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# Example 2:


# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
 

# Constraints:

# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109
    
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
            
        k = k % length
        if k == 0:
            return head
        
        new_head = head
        prev = ListNode()
        prev.next = head
        for _ in range(length - k):
            new_head = new_head.next
            prev = prev.next
        
        prev.next = None
        node = new_head
        while node.next:
            node = node.next
            
        node.next = head
        
        return new_head
            
        