# 513. Find Bottom Left Tree Value
# Medium

# Given the root of a binary tree, return the leftmost value in the last row of the tree.

# Example 1:

# Input: root = [2,1,3]
# Output: 1
# Example 2:

# Input: root = [1,2,3,4,null,5,6,null,null,7]
# Output: 7
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0
        self.left_bot_val = root.val
        
        def dfs(root: Optional[TreeNode], cur_depth: int) -> None:
            if not root:
                return None
            
            if cur_depth > self.max_depth:
                self.max_depth = cur_depth
                self.left_bot_val = root.val
            
            dfs(root.left, cur_depth + 1)
            dfs(root.right, cur_depth + 1)
            
        dfs(root, 0)
        
        return self.left_bot_val