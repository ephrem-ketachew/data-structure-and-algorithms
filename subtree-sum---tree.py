# 508. Most Frequent Subtree Sum
# Medium

# Given the root of a binary tree, return the most frequent subtree sum. If there is a tie, return all the values with the highest frequency in any order.

# The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself).

# Example 1:

# Input: root = [5,2,-3]
# Output: [2,-3,4]
# Example 2:

# Input: root = [5,2,-5]
# Output: [2]

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -105 <= Node.val <= 105

from typing import Optional, List
from collections import Counter

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.sums = Counter()
        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            subtree_sum = root.val + dfs(root.left) + dfs(root.right)
            
            self.sums[subtree_sum] += 1
            
            return subtree_sum
        
        dfs(root)
        
        ans = []
        max_freq = 0
        for num in self.sums:
            freq = self.sums[num]
            if freq > max_freq:
                max_freq = freq
                ans = [num]
            elif freq == max_freq:
                ans.append(num)
                
        return ans