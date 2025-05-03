# 86. Partition List

# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

 

# Example 1:


# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]
# Example 2:

# Input: head = [2,1], x = 2
# Output: [1,2]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from typing import Optional

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # values_less_than_x = []
        # values_greater_than_x = [] 
        # current = head
        
        # while current:
        #     if current.val < x:
        #         values_less_than_x.append(current.val)
        #     else:
        #         values_greater_than_x.append(current.val)
        #     current = current.next
        
        # current = head
        # for val in values_less_than_x:
        #     current.val = val
        #     current = current.next
        # for val in values_greater_than_x:
        #     current.val = val
        #     current = current.next
            
        # return head
        
        node = ListNode(0)
        node.next = head
        current_left = current = node
        while current:
            before = current
            current = current.next
            if current and current.val < x:
                if current_left.next == current:
                    current_left = current
                    continue
                before_head = current_left.next
                after = current.next
                
                current_left.next = current
                current.next  = before_head
                before.next = after
                
                current_left = current
                current = before
        return node.next