# 148. Sort List

# Given the head of a linked list, return the list after sorting it in ascending order.

# Example 1:

# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
# Example 2:

# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
# Example 3:

# Input: head = []
# Output: []

# Constraints:

# The number of nodes in the list is in the range [0, 5 * 104].
# -105 <= Node.val <= 105

from typing import Optional
 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def __merge(head1, head2):
            current = dummy_node = ListNode()
            
            while head1 and head2:
                if head1.val <= head2.val:
                    current.next = head1
                    head1 = head1.next
                else:
                    current.next = head2
                    head2 = head2.next
                current = current.next
                
            while head1:
                current.next = head1
                head1 = head1.next
                current = current.next
            while head2:
                current.next = head2
                head2 = head2.next
                current = current.next
                
            current.next = None
            
            return dummy_node.next
        
        def __sort_linked_list(head):
            slow = fast = head
            while fast and fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
                
            right_head = slow.next
            slow.next = None
            left_head = head
            
            if left_head.next:
                left_head = __sort_linked_list(left_head)
            if right_head.next:
                right_head = __sort_linked_list(right_head)
            return __merge(left_head, right_head)
        
        if not head or not head.next:
            return head
        return __sort_linked_list(head)