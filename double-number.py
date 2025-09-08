# 2816. Double a Number Represented as a Linked List
# Medium

# You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.

# Return the head of the linked list after doubling it.


# Example 1:

# Input: head = [1,8,9]
# Output: [3,7,8]
# Explanation: The figure above corresponds to the given linked list which represents the number 189. Hence, the returned linked list represents the number 189 * 2 = 378.
# Example 2:


# Input: head = [9,9,9]
# Output: [1,9,9,8]
# Explanation: The figure above corresponds to the given linked list which represents the number 999. Hence, the returned linked list reprersents the number 999 * 2 = 1998. 

# Constraints:

# The number of nodes in the list is in the range [1, 104]
# 0 <= Node.val <= 9
# The input is generated such that the list represents a number that does not have leading zeros, except the number 0 itself.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # num = []
        # node = head
        # while node:
        #     num.append(str(node.val))
        #     node = node.next
            
        # num = int(''.join(num))
        # num *= 2
        # num = str(num)
        
        # new_head = node = ListNode(int(num[0]))
        # for i in range(1, len(num)):
        #     node.next = ListNode(int(num[i]))
        #     node = node.next
            
        # return new_head
        
        # stack = []
        # node = head
        # while node:
        #     stack.append(node.val)
        #     node = node.next
           
        # carry = 0 
        # new_head = None
        # while stack:
        #     num = 2 * stack.pop() + carry
        #     carry = num // 10
        #     num %= 10
            
        #     node = ListNode(num)
        #     node.next = new_head
        #     new_head = node
            
        # if carry:
        #     node = ListNode(carry)
        #     node.next = new_head
        #     new_head = node
            
        # return new_head
        
        def _reverse(head):
            prev = None
            cur = head
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
                
            return prev
                
        carry = 0
        rev_head = node = _reverse(head)
        while node:
            num = 2 * node.val + carry
            carry = num // 10
            num %= 10
            node.val = num
            before = node
            node = node.next
            
        if carry:
            before.next = ListNode(carry)
            
        return _reverse(rev_head)