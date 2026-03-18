# 889. Construct Binary Tree from Preorder and Postorder Traversal
# Medium

# Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

# If there exist multiple answers, you can return any of them.

# Example 1:

# Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
# Output: [1,2,3,4,5,6,7]
# Example 2:

# Input: preorder = [1], postorder = [1]
# Output: [1]

# Constraints:

# 1 <= preorder.length <= 30
# 1 <= preorder[i] <= preorder.length
# All the values of preorder are unique.
# postorder.length == preorder.length
# 1 <= postorder[i] <= postorder.length
# All the values of postorder are unique.
# It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree.

from typing import List, Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # if not preorder:
        #     return None
        
        # if len(preorder) == 1:
        #     return TreeNode(preorder[0])
        
        # root = TreeNode(preorder[0])
        
        # left_root = preorder[1]
        # root_idx = postorder.index(left_root)
        
        # left_postorder = postorder[:root_idx + 1]
        # right_postorder = postorder[root_idx + 1:-1]
        
        # left_subtree_size = root_idx + 1
        
        # left_preorder = preorder[1:1+left_subtree_size]
        # right_preorder = preorder[1+left_subtree_size:]
        
        # root.left = self.constructFromPrePost(left_preorder, left_postorder)
        # root.right = self.constructFromPrePost(right_preorder, right_postorder)
        
        # return root
        
        self.preorder = preorder
        self.postorder_indices = defaultdict(int)
        for i, num in enumerate(postorder):
            self.postorder_indices[num] = i
        
        def dnq(left:int, right: int, post_begin: int, post_end: int) -> Optional[TreeNode]:
            if post_begin > post_end:
                return None
            
            if left == right:
                return TreeNode(self.preorder[left])
            
            root = TreeNode(self.preorder[left])
            
            left_root = self.preorder[left + 1]
            root_idx = self.postorder_indices[left_root]
            
            subtree_size = root_idx + 1 - post_begin
            
            root.left = dnq(left + 1, left + subtree_size, post_begin, root_idx)
            root.right = dnq(left + subtree_size + 1, right, root_idx + 1, post_end - 1)
            
            return root
        
        return dnq(0, len(preorder) - 1, 0, len(postorder) - 1)