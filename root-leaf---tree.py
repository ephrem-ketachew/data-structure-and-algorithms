# 1022. Sum of Root To Leaf Binary Numbers
# Easy

# You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

# For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

# The test cases are generated so that the answer fits in a 32-bits integer.

# Example 1:

# Input: root = [1,0,1,0,1,0,1]
# Output: 22
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
# Example 2:

# Input: root = [0]
# Output: 0

# Constraints:

# The number of nodes in the tree is in the range [1, 1000].
# Node.val is 0 or 1.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # self.sum = 0
        # def dfs(root: Optional[TreeNode], digits: list[str]) -> None:
        #     if not root.left and not root.right:
        #         digits = digits + [str(root.val)]
        #         self.sum += int(''.join(digits), 2)
            
        #     if root.left:
        #         dfs(root.left, digits + [str(root.val)])
                
        #     if root.right:
        #         dfs(root.right, digits + [str(root.val)])
            
        # dfs(root, [])
        
        # return self.sum
    
        self.sum = 0
        def dfs(root: Optional[TreeNode], num: int) -> None:
            if not root.left and not root.right:
                self.sum += num * 2 + root.val
            
            if root.left:
                dfs(root.left, num * 2 + root.val)
                
            if root.right:
                dfs(root.right, num * 2 + root.val)
            
        dfs(root, 0)
        
        return self.sum