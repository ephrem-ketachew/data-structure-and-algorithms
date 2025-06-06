# 230. Kth Smallest Element in a BST

# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Example 1:

# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:

# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3

# Constraints:

# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104
 
# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        global n, kth
        n = 0
        kth = None
        def __inorder_traversal(root):
            if root:
                __inorder_traversal(root.left)
                global n, kth
                n += 1
                if n == k:
                    kth = root.val
                    return
                __inorder_traversal(root.right)
                
        __inorder_traversal(root)
        return kth