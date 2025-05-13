# 701. Insert into a Binary Search Tree

# You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

# Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

 
from typing import Optional
 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val)
        
        if root is None:
            root = new_node
            return root
        
        current = root
        while current:            
            if new_node.val < current.val:
                if current.left is None:
                    current.left = new_node
                    return root
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return root
                current = current.right