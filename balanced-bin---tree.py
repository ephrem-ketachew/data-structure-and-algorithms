# 110. Balanced Binary Tree
# Easy

# Given a binary tree, determine if it is height-balanced.

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:


# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True
        def _is_balanced(root: Optional[TreeNode], cur_depth: int) -> int:
            nonlocal is_balanced
            if root == None:
                return cur_depth
            
            left_depth = _is_balanced(root.left, cur_depth + 1)
            right_depth = _is_balanced(root.right, cur_depth + 1)
            
            if abs(left_depth - right_depth) > 1:
                is_balanced = False
                
            return max(left_depth, right_depth)
        
        _is_balanced(root, 0)
        
        return is_balanced