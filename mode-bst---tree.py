# 501. Find Mode in Binary Search Tree
# Easy

# Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

# If the tree has more than one mode, return them in any order.

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.

# Example 1:

# Input: root = [1,null,2,2]
# Output: [2]
# Example 2:

# Input: root = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -105 <= Node.val <= 105
 

# Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

from typing import Optional, List
from collections import Counter

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def _find_mode(root: Optional[TreeNode]) -> Counter:
            if not root:
                return Counter()
            
            counter_left = _find_mode(root.left)
            counter_right = _find_mode(root.right)
            
            return Counter([root.val]) + counter_left + counter_right
        
        counter = _find_mode(root)
        max_freq = max(counter.values())
        ans = []
        for num in counter:
            if counter[num] == max_freq:
                ans.append(num)
                
        return ans            
            