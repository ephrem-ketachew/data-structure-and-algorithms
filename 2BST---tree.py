# 1305. All Elements in Two Binary Search Trees
# Medium

# Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

# Example 1:

# Input: root1 = [2,1,4], root2 = [1,0,3]
# Output: [0,1,1,2,3,4]
# Example 2:

# Input: root1 = [1,null,8], root2 = [8,1]
# Output: [1,1,8,8]
 
# Constraints:

# The number of nodes in each tree is in the range [0, 5000].
# -105 <= Node.val <= 105

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        self.list = []
        def inorder(root: Optional[TreeNode]) -> None:
            if not root:
                return
            inorder(root.left)
            self.list.append(root.val)
            inorder(root.right)
            
        inorder(root1)
        arr1 = self.list.copy()
        self.list = []
        inorder(root2)
        arr2 = self.list
        
        ans = []
        i = j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                ans.append(arr1[i])
                i += 1
            else:
                ans.append(arr2[j])
                j += 1
                
        while i < len(arr1):
            ans.append(arr1[i])
            i += 1
            
        while j < len(arr2):
            ans.append(arr2[j])
            j += 1
            
        return ans