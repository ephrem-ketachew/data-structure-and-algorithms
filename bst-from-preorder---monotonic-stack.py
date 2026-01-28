# 1008. Construct Binary Search Tree from Preorder Traversal
# Medium

# Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.

# It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.

# A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.

# A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.

# Example 1:

# Input: preorder = [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]
# Example 2:

# Input: preorder = [1,3]
# Output: [1,null,3]

# Constraints:

# 1 <= preorder.length <= 100
# 1 <= preorder[i] <= 1000
# All the values of preorder are unique.

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        # stack = []
        # root = None
        # for num in preorder:
        #     node = TreeNode(num)
        #     if not root:
        #         root = node
        #     right_par = None
        #     while stack and stack[-1].val < node.val:
        #         right_par = stack.pop()
        #     if right_par:
        #         right_par.right = node
        #     elif stack:
        #         stack[-1].left = node
        #     stack.append(node)
            
        # return root
        
        if not preorder:
            return
        
        root = TreeNode(preorder[0])
        stack = [root]
        
        for i in range(1, len(preorder)):
            node = TreeNode(preorder[i])
            if stack and stack[-1].val > node.val:
                stack[-1].left = node
            else:
                parent = stack[-1]
                while stack and stack[-1].val < node.val:
                    parent = stack.pop()
                parent.right = node
            stack.append(node)
            
        return root
            