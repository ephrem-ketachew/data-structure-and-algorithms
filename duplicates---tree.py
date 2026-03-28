# 652. Find Duplicate Subtrees
# Medium

# Given the root of a binary tree, return all duplicate subtrees.

# For each kind of duplicate subtrees, you only need to return the root node of any one of them.

# Two trees are duplicate if they have the same structure with the same node values.

# Example 1:

# Input: root = [1,2,3,4,null,2,4,null,null,4]
# Output: [[2,4],[4]]
# Example 2:

# Input: root = [2,1,1]
# Output: [[1]]
# Example 3:


# Input: root = [2,2,2,3,null,3,null]
# Output: [[2,3],[3]]
 

# Constraints:

# The number of the nodes in the tree will be in the range [1, 5000]
# -200 <= Node.val <= 200

from typing import Optional, List
from collections import Counter

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtree_count = Counter()
        duplicates = []
        def serialize(node: Optional[TreeNode]) -> str:
            if not node:
                return '#'
            
            left_serialize = serialize(node.left)
            right_serialize = serialize(node.right)
            
            cur_serialize = f'{node.val},{left_serialize},{right_serialize}'
            
            subtree_count[cur_serialize] += 1
            if subtree_count[cur_serialize] == 2:
                duplicates.append(node)
                
            return cur_serialize
        
        serialize(root)
                
        return duplicates