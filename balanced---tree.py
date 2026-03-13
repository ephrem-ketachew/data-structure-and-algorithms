# 1382. Balance a Binary Search Tree
# Medium

# Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

# A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

# Example 1:

# Input: root = [1,null,2,null,3,null,4,null,null]
# Output: [2,1,3,null,null,null,4]
# Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
# Example 2:


# Input: root = [2,1,3]
# Output: [2,1,3]
 
# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# 1 <= Node.val <= 105

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.vals = []
        
        def inorder(root: Optional[TreeNode]) -> None:
            if not root:
                return 
            
            inorder(root.left)
            self.vals.append(root.val)
            inorder(root.right)
            
        # def build(arr: list[list]) -> Optional[TreeNode]:
        #     if not arr:
        #         return None
            
        #     mid = len(arr) // 2
            
        #     root = TreeNode(arr[mid])
            
        #     left_arr = arr[:mid]
        #     right_arr = arr[mid + 1:]
            
        #     root.left = build(left_arr)
        #     root.right = build(right_arr)
            
        #     return root
        
        # inorder(root)
        # root = build(self.vals)
        
        def build(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            mid = (left + right) // 2
            
            root = TreeNode(self.vals[mid])
            
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            
            return root
        
        inorder(root)
        root = build(0, len(self.vals) - 1)
        
        return root