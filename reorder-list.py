# 143. Reorder List
# Medium
# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.


# Example 1:


# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# Example 2:


# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
 

# Constraints:

# The number of nodes in the list is in the range [1, 5 * 104].
# 1 <= Node.val <= 1000

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # stack = []
        # node = head
        # while node:
        #     stack.append(node)
        #     node = node.next
            
        # cur_len, length = 0, len(stack)
        # dummy_node = ListNode()
        # dummy_node.next = head
        # cur_node = dummy_node
        # next_node = head
        
        # while cur_len < length:
        #     cur_node.next = next_node
        #     cur_node = cur_node.next
        #     next_node = next_node.next
        #     cur_len += 1
            
        #     if cur_len == length:
        #         break
            
        #     cur_node.next = stack.pop()
        #     cur_node = cur_node.next
        #     cur_len += 1
            
        # cur_node.next = None
        # dummy_node.next = None
        
        if not head or not head.next:
            return
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        prev, cur = None, slow.next
        slow.next = None
        
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
            
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2