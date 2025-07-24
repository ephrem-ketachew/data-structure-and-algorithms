# 653. Two Sum IV - Input is a BST
# Easy
# Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

# Example 1:


# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true
# Example 2:


# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false
 
# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -104 <= Node.val <= 104
# root is guaranteed to be a valid binary search tree.
# -105 <= k <= 105

# Definition for a binary tree node.

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # approach one BFS
        # seen = set()
        
        # openn = deque()
        # openn.append(root)
        
        # while openn:
        #     node = openn.popleft()
        #     if node:
        #         if k - node.val in seen:
        #             return True
        #         seen.add(node.val)
        #         openn.append(node.left)
        #         openn.append(node.right)
            
        # return False
        
        # approach two
        sorted_arr = []
        def inorder(node: Optional[TreeNode]):
            if node:
                inorder(node.left)
                sorted_arr.append(node.val)
                inorder(node.right)
                
        inorder(root)
        left, right = 0, len(sorted_arr) - 1
        while left < right:
            summ = sorted_arr[left] + sorted_arr[right]
            if summ == k:
                return True
            if summ < k:
                left += 1
            elif summ > k:
                right -= 1
                
        return False
            