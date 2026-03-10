# 993. Cousins in Binary Tree
# Easy

# Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

# Two nodes of a binary tree are cousins if they have the same depth with different parents.

# Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

# Example 1:

# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false
# Example 2:

# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true
# Example 3:

# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false

# Constraints:

# The number of nodes in the tree is in the range [2, 100].
# 1 <= Node.val <= 100
# Each node has a unique value.
# x != y
# x and y are exist in the tree.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.depth = -1
        self.par_val = -1
        def depth(root: Optional[TreeNode], val: int, cur_depth: int) -> None:
            if not root:
                return
            
            if root.val == val:
                self.depth = cur_depth
                return
                
            if (root.left and root.left.val == val) or (root.right and root.right.val == val):
                self.depth = cur_depth + 1
                self.par_val = root.val
                return
                
            depth(root.left, val, cur_depth + 1)
            depth(root.right, val, cur_depth + 1)
            
        depth(root, x, 0)
        depth_x = self.depth
        par_val_x = self.par_val
        
        depth(root, y, 0)
        depth_y = self.depth
        par_val_y = self.par_val
        
        return depth_x == depth_y and par_val_x != par_val_y