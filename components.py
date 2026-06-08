# 2685. Count the Number of Complete Components
# Medium

# You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.

# Return the number of complete connected components of the graph.

# A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

# A connected component is said to be complete if there exists an edge between every pair of its vertices.

# Example 1:
# Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
# Output: 3
# Explanation: From the picture above, one can see that all of the components of this graph are complete.
# Example 2:

# Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
# Output: 1
# Explanation: The component containing vertices 0, 1, and 2 is complete since there is an edge between every pair of two vertices. On the other hand, the component containing vertices 3, 4, and 5 is not complete since there is no edge between vertices 4 and 5. Thus, the number of complete components in this graph is 1.

# Constraints:

# 1 <= n <= 50
# 0 <= edges.length <= n * (n - 1) / 2
# edges[i].length == 2
# 0 <= ai, bi <= n - 1
# ai != bi
# There are no repeated edges.

from typing import List

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.sizes = [1] * n
        self.edges = [0] * n
        
    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> None:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            self.edges[root_x] += 1
            return
        if root_x < root_y:
            root_x, root_y = root_y, root_x
            
        self.parent[root_y] = root_x
        self.sizes[root_x] += self.sizes[root_y]
        self.edges[root_x] += self.edges[root_y] + 1

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for u, v in edges:
            dsu.union(u, v)
            
        components = set()
        for i in range(n):
            components.add(dsu.find(i))
           
        count = 0 
        for root in components:
            e = dsu.edges[root]
            v = dsu.sizes[root]
            if e == v * (v - 1) // 2:
                count += 1
                
        return count