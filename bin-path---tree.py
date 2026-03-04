# 257. Binary Tree Paths
# Easy

# Given the root of a binary tree, return all root-to-leaf paths in any order.

# A leaf is a node with no children.

# Example 1:

# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
# Example 2:

# Input: root = [1]
# Output: ["1"]

# Constraints:

# The number of nodes in the tree is in the range [1, 100].
# -100 <= Node.val <= 100

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        output = []
        def _binary_tree_paths(root: Optional[TreeNode], path) -> None:
            if not root.left and not root.right:
                output.append('->'.join(path + [str(root.val)]))
            
            if root.left:
                _binary_tree_paths(root.left, path + [str(root.val)])
                
            if root.right:
                _binary_tree_paths(root.right, path + [str(root.val)])
                
        _binary_tree_paths(root, [])
        
        return output