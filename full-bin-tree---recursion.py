# 894. All Possible Full Binary Trees
# Medium

# Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

# Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

# A full binary tree is a binary tree where each node has exactly 0 or 2 children.
 

# Example 1:

# Input: n = 7
# Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
# Example 2:

# Input: n = 3
# Output: [[0,0,0]]

# Constraints:

# 1 <= n <= 20

# Definition for a binary tree node.

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        
        if n == 1:
            return [TreeNode()]
        
        res = []
        for i in range(1, n, 2):
            left_nodes_count = i
            right_nodes_count = n - i - 1
            
            left_nodes = self.allPossibleFBT(left_nodes_count)
            right_nodes = self.allPossibleFBT(right_nodes_count)
            
            for l in left_nodes:
                for r in right_nodes:
                    root = TreeNode()
                    root.left = l
                    root.right = r
                    
                    res.append(root)
                    
        return res