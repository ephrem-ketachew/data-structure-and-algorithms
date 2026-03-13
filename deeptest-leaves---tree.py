# 1302. Deepest Leaves Sum
# Medium

# Given the root of a binary tree, return the sum of values of its deepest leaves.

# Example 1:

# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15
# Example 2:

# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 19

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# 1 <= Node.val <= 100

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.depth = 0
        self.sum = 0
        
        def dfs(root: Optional[TreeNode], cur_depth: int) -> None:
            cur_depth += 1
            if not root.left and not root.right:
                if cur_depth == self.depth:
                    self.sum += root.val
                elif cur_depth > self.depth:
                    self.sum = root.val
                    self.depth = cur_depth
                    
            if root.left:
                dfs(root.left, cur_depth)
                
            if root.right:
                dfs(root.right, cur_depth)
                
                
        dfs(root, 0)
        
        return self.sum
                    
                    