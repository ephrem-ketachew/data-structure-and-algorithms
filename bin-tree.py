# 2196. Create Binary Tree From Descriptions
# Medium

# You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,

# If isLefti == 1, then childi is the left child of parenti.
# If isLefti == 0, then childi is the right child of parenti.
# Construct the binary tree described by descriptions and return its root.

# The test cases will be generated such that the binary tree is valid.

# Example 1:

# Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
# Output: [50,20,80,15,17,19]
# Explanation: The root node is the node with value 50 since it has no parent.
# The resulting binary tree is shown in the diagram.
# Example 2:

# Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
# Output: [1,2,null,null,3,4]
# Explanation: The root node is the node with value 1 since it has no parent.
# The resulting binary tree is shown in the diagram.
 
# Constraints:

# 1 <= descriptions.length <= 104
# descriptions[i].length == 3
# 1 <= parenti, childi <= 105
# 0 <= isLefti <= 1
# The binary tree described by descriptions is valid.

from typing import List, Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = defaultdict(TreeNode)
        child_vals = set()
        all_vals = set()
        for parent, child, is_left in descriptions:
            child_node = nodes[child] if child in nodes else TreeNode(child)
            parent_node = nodes[parent] if parent in nodes else TreeNode(parent)
            
            if is_left == 1:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
                
            if not child in nodes:
                nodes[child] = child_node
                
            if not parent in nodes:
                nodes[parent] = parent_node
                
            all_vals.add(parent)
            all_vals.add(child)
            
            child_vals.add(child)
            
        root_val = sum(all_vals) - sum(child_vals)
        root = nodes[root_val]
        
        return root