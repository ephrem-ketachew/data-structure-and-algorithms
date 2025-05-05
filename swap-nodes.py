# 24. Swap Nodes in Pairs
# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
# Example 1:
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
# Example 2:
# Input: head = []
# Output: []
# Example 3:
# Input: head = [1]
# Output: [1]
# Example 4:
# Input: head = [1,2,3]
# Output: [2,1,3]

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        dummy_node = before = ListNode()
        dummy_node.next = head
        cur_left = head
        cur_right = head.next
        while cur_left and cur_right:
            after = cur_right.next
            
            before.next = cur_right
            cur_right.next = cur_left
            cur_left.next = after 
            
            before = cur_left
            cur_left = after
            if after:
                cur_right = after.next
                
        return dummy_node.next