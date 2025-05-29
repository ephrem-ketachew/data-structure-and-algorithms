# 108. Convert Sorted Array to Binary Search Tree

# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

# Example 1:


# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Example 2:


# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
       def __sorted_array_to_bst(nums):
            mid = len(nums) // 2
            node = TreeNode(nums[mid])
            if mid > 0:
               node.left = __sorted_array_to_bst(nums[:mid])
            if mid + 1 < len(nums):
                node.right = __sorted_array_to_bst(nums[mid + 1:])
            return node
       
       root = __sorted_array_to_bst(nums)
       
       return root