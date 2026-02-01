# 1019. Next Greater Node In Linked List
# Medium

# You are given the head of a linked list with n nodes.

# For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.

# Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.

# Example 1:

# Input: head = [2,1,5]
# Output: [5,5,0]
# Example 2:

# Input: head = [2,7,4,3,5]
# Output: [7,0,5,5,0]
 
# Constraints:

# The number of nodes in the list is n.
# 1 <= n <= 104
# 1 <= Node.val <= 109

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        # node = head
        # nums = []
        # while node:
        #     nums.append(node.val)
        #     node = node.next
            
        # result = [0] * len(nums)
        # stack = []
        # for i, num in enumerate(nums):
        #     while stack and nums[stack[-1]] < num:
        #         idx = stack.pop()
        #         result[idx] = num
        #     stack.append(i)
            
        # return result
        
        result = []
        stack = []
        node = head
        while node:
            result.append(0)
            while stack and stack[-1][0] < node.val:
                _, idx = stack.pop()
                result[idx] = node.val
                
            stack.append((node.val, len(result) - 1))
            
            node = node.next
            
        return result