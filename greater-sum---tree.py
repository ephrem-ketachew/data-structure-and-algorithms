# 1038. Binary Search Tree to Greater Sum Tree
# Medium

# Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

# As a reminder, a binary search tree is a tree that satisfies these constraints:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 
# Example 1:

# Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
# Example 2:

# Input: root = [0,null,1]
# Output: [1,null,1]

# Constraints:

# The number of nodes in the tree is in the range [1, 100].
# 0 <= Node.val <= 100
# All the values in the tree are unique.
 

# Note: This question is the same as 538: https://leetcode.com/problems/convert-bst-to-greater-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # self.order = []
        # self.cur = 0
        
        # def inorder(root: Optional[TreeNode], append: bool) -> None:
        #     if not root:
        #         return
            
        #     inorder(root.left, append)
            
        #     if append:
        #         self.order.append(root.val)
        #     else:
        #         root.val = self.order[self.cur]
        #         self.cur += 1
                
        #     inorder(root.right, append)
            
        # inorder(root, True)
        
        # for i in range(len(self.order) - 2, -1, -1):
        #     self.order[i] = self.order[i] + self.order[i + 1]
            
        # inorder(root, False)
        
        # return root
        
        self.running_sum = 0
        def reverse_inorder(root: Optional[TreeNode]) -> None:
            if not root:
                return 0
            
            reverse_inorder(root.right)
            
            self.running_sum += root.val
            root.val = self.running_sum
            
            reverse_inorder(root.left)
            
        reverse_inorder(root)
        
        return root
            