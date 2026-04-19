# 1129. Shortest Path with Alternating Colors
# Medium

# You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

# You are given two arrays redEdges and blueEdges where:

# redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
# blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
# Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.

# Example 1:

# Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
# Output: [0,1,-1]
# Example 2:

# Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
# Output: [0,1,-1]
 

# Constraints:

# 1 <= n <= 100
# 0 <= redEdges.length, blueEdges.length <= 400
# redEdges[i].length == blueEdges[j].length == 2
# 0 <= ai, bi, uj, vj < n

from typing import List
from collections import defaultdict, deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_graph = defaultdict(list)
        blue_graph = defaultdict(list)
        for a, b in redEdges:
            red_graph[a].append(b)
            
        for u, v in blueEdges:
            blue_graph[u].append(v)
            
        queue = deque([(0, -1)])
        ans = [-1] * n
        path = 0
        seen = set([(0, -1)])
        while queue:
            t = len(queue)
            for _ in range(t):
                node, prev = queue.popleft()
                if ans[node] == -1:
                    ans[node] = path
                    
                if prev == 0 or prev == -1:
                    for u in blue_graph[node]:
                        if (u, 1) not in seen:
                            queue.append((u, 1))
                            seen.add((u, 1))
                            
                if prev == 1 or prev == -1:
                    for u in red_graph[node]:
                        if (u, 0) not in seen:
                            queue.append((u, 0))
                            seen.add((u, 0))
                            
            path += 1
            
        return ans