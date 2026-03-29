# 106. Construct Binary Tree from Inorder and Postorder Traversal
# Medium

# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

# Example 1:

# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: inorder = [-1], postorder = [-1]
# Output: [-1]
 
# Constraints:

# 1 <= inorder.length <= 3000
# postorder.length == inorder.length
# -3000 <= inorder[i], postorder[i] <= 3000
# inorder and postorder consist of unique values.
# Each value of postorder also appears in inorder.
# inorder is guaranteed to be the inorder traversal of the tree.
# postorder is guaranteed to be the postorder traversal of the tree.

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        num_idx_map = {}
        for i, num in enumerate(inorder):
            num_idx_map[num] = i
            
        def build(left_in: int, right_in: int, left_post: int, right_post: int) -> Optional[TreeNode]:
            if left_in > right_in:
                return None
            
            root_val = postorder[right_post]
            root = TreeNode(root_val)
            
            root_val_in_inorder_idx = num_idx_map[root_val]
            
            left_inorder_len = root_val_in_inorder_idx - left_in
            
            root.left = build(left_in, root_val_in_inorder_idx - 1, left_post, left_post + left_inorder_len - 1)
            root.right = build(root_val_in_inorder_idx + 1, right_in, left_post + left_inorder_len, right_post - 1)
            
            return root
        
        return build(0, len(inorder) - 1, 0, len(postorder) - 1)