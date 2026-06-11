# 1584. Min Cost to Connect All Points
# Medium

# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

# Example 1:

# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
# Explanation: 

# We can connect the points as shown above to get the minimum cost of 20.
# Notice that there is a unique path between every pair of points.
# Example 2:

# Input: points = [[3,12],[-2,5],[-4,1]]
# Output: 18
 
# Constraints:

# 1 <= points.length <= 1000
# -106 <= xi, yi <= 106
# All pairs (xi, yi) are distinct.

from typing import List

class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [1] * n
        
    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                s = abs(x1 - x2) + abs(y1 - y2)
                edges.append([i, j, s])
                
        edges.sort(key=lambda x: x[2])
        dsu = DSU(n)
        mst_cost = 0
        edges_connected = 0
        for u, v, weight in edges:
            if dsu.union(u, v):
                mst_cost += weight
                edges_connected += 1
                
        return mst_cost