# 785. Is Graph Bipartite?
# Medium

# There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

# There are no self-edges (graph[u] does not contain u).
# There are no parallel edges (graph[u] does not contain duplicate values).
# If v is in graph[u], then u is in graph[v] (the graph is undirected).
# The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
# A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

# Return true if and only if it is bipartite.

# Example 1:

# Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
# Output: false
# Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.
# Example 2:

# Input: graph = [[1,3],[0,2],[1,3],[0,2]]
# Output: true
# Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
 
# Constraints:

# graph.length == n
# 1 <= n <= 100
# 0 <= graph[u].length < n
# 0 <= graph[u][i] <= n - 1
# graph[u] does not contain u.
# All the values of graph[u] are unique.
# If graph[u] contains v, then graph[v] contains u.

from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # visited = set()
        # def dfs(node: int, prev: int, first_set: set, second_set: set) -> bool:
        #     visited.add(node)
        #     if prev == 0:
        #         if node in first_set:
        #             return False
        #         if node in second_set:
        #             return True
        #         second_set.add(node)
        #     else:
        #         if node in second_set:
        #             return False
        #         if node in first_set:
        #             return True
        #         first_set.add(node)
             
        #     has_valid_partition = True
        #     for neighbor in graph[node]:                        
        #         has_valid_partition = has_valid_partition and dfs(neighbor, prev ^ 1, first_set, second_set)
        #         if not has_valid_partition:
        #             return False
                    
        #     return has_valid_partition
         
        # for i in range(len(graph)):
        #     if i not in visited:
        #         if not dfs(i, 0, set(), set()):
        #             return False
                
        # return True
        
        n = len(graph)
        colors = [0] * n
        def dfs(node: int, color: int) -> bool:
            colors[node] = color
            for neighbor in graph[node]:
                if colors[neighbor] == color:
                    return False
                
                if colors[neighbor] == 0:
                    if not dfs(neighbor, -color):
                        return False
                
            return True
        
        for i in range(n):
            if colors[i] == 0:
                if not dfs(i, 1):
                    return False
                
        return True