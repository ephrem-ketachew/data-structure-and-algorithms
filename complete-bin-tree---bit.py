# 222. Count Complete Tree Nodes
# Easy

# Given the root of a complete binary tree, return the number of the nodes in the tree.

# According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Design an algorithm that runs in less than O(n) time complexity.

# Example 1:

# Input: root = [1,2,3,4,5,6]
# Output: 6
# Example 2:

# Input: root = []
# Output: 0
# Example 3:

# Input: root = [1]
# Output: 1

# Constraints:

# The number of nodes in the tree is in the range [0, 5 * 104].
# 0 <= Node.val <= 5 * 104
# The tree is guaranteed to be complete.

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        
        # count = 0
        # open = deque()
        # open.append(root)
        # while open:
        #     node = open.popleft()
        #     count += 1
        #     if node.left:
        #         open.append(node.left)
        #     if node.right:
        #         open.append(node.right)
        
        # return count
        if not root:
            return 0
        
        height = 0
        node = root
        while node:
            height += 1
            node = node.left
            
        inner_nodes_count = 2 ** (height - 1) - 1
        left, right = 1, 2 ** (height - 1)
        leaf_nodes_count = 0
        head = root
        cur_height = 1
        while head and left <= right:
            node = head.left
            mid = (left + right) // 2
            k = cur_height
            while node:
                k += 1
                node = node.right
            if k == height:
                leaf_nodes_count = mid
                left = mid + 1
                head = head.right
            else:
                right = mid - 1
                head = head.left
                
            cur_height += 1
                
        return inner_nodes_count + leaf_nodes_count
        