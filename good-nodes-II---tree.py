# 3249. Count the Number of Good Nodes
# Medium

# There is an undirected tree with n nodes labeled from 0 to n - 1, and rooted at node 0. You are given a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

# A node is good if all the subtrees rooted at its children have the same size.

# Return the number of good nodes in the given tree.

# A subtree of treeName is a tree consisting of a node in treeName and all of its descendants.

# Example 1:

# Input: edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]

# Output: 7

# Explanation:

# All of the nodes of the given tree are good.

# Example 2:

# Input: edges = [[0,1],[1,2],[2,3],[3,4],[0,5],[1,6],[2,7],[3,8]]

# Output: 6

# Explanation:

# There are 6 good nodes in the given tree. They are colored in the image above.

# Example 3:

# Input: edges = [[0,1],[1,2],[1,3],[1,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[9,12],[10,11]]

# Output: 12

# Explanation:

# All nodes except node 9 are good.

# Constraints:

# 2 <= n <= 105
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai, bi < n
# The input is generated such that edges represents a valid tree.

from typing import List, Optional
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, children=[]):
        self.val = val
        self.children = []

class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        network = defaultdict(list)
        for a, b in edges:
            network[a].append(b)
            network[b].append(a)
            
        visited = set()
        def build(val: int) -> Optional[TreeNode]:
            if not network[val]:
                return None
            
            root = TreeNode(val)
            visited.add(val)
            for num in network[val]:
                if num not in visited:
                    root.children.append(build(num))
                
            return root
        
        root = build(0)
        
        self.good_nodes_count = 0     
        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            size = 1
            prev_size = -1
            is_good = True
            for child in root.children:
                cur_size = dfs(child)
                size += cur_size
                
                if prev_size != -1 and cur_size != prev_size:
                    is_good = False
                    
                prev_size = cur_size
                
            if is_good:
                self.good_nodes_count += 1
                
            return size
        
        dfs(root)
        
        return self.good_nodes_count