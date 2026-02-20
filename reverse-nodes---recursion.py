# 25. Reverse Nodes in k-Group
# Hard

# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Example 2:


# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
 

# Constraints:

# The number of nodes in the list is n.
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000
 
# Follow-up: Can you solve the problem in O(1) extra memory space?

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node_cnt = 0
        node = head
        while node:
            node = node.next
            node_cnt += 1
        
        complete_node_cnt = (node_cnt // k) * k
        new_head = None
        count = 0
        node = head
        current = None
        while count < complete_node_cnt:
            previous = current
            current = node
            
            prev = None
            for _ in range(k):
                cur = node
                node = node.next
                cur.next = prev
                prev = cur

            if new_head == None:
                new_head = prev
            else:
                previous.next = prev
                
            count += k
            
        current.next = node
        
        return new_head