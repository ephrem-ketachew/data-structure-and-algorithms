# 947. Most Stones Removed with Same Row or Column
# Medium

# On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

# A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

# Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.

# Example 1:

# Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# Output: 5
# Explanation: One way to remove 5 stones is as follows:
# 1. Remove stone [2,2] because it shares the same row as [2,1].
# 2. Remove stone [2,1] because it shares the same column as [0,1].
# 3. Remove stone [1,2] because it shares the same row as [1,0].
# 4. Remove stone [1,0] because it shares the same column as [0,0].
# 5. Remove stone [0,1] because it shares the same row as [0,0].
# Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.
# Example 2:

# Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
# Output: 3
# Explanation: One way to make 3 moves is as follows:
# 1. Remove stone [2,2] because it shares the same row as [2,0].
# 2. Remove stone [2,0] because it shares the same column as [0,0].
# 3. Remove stone [0,2] because it shares the same row as [0,0].
# Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.
# Example 3:

# Input: stones = [[0,0]]
# Output: 0
# Explanation: [0,0] is the only stone on the plane, so you cannot remove it.

# Constraints:

# 1 <= stones.length <= 1000
# 0 <= xi, yi <= 104
# No two stones are at the same coordinate point.

from typing import List

# class DSU:
#     def __init__(self, m: int, n: int):
#         self.parent = []
#         current = 0
#         for _ in range(m):
#             arr = []
#             for _ in range(n):
#                 arr.append(current)
#                 current += 1
#             self.parent.append(arr)
            
#         self.rank = [[1] * n for _ in range(m)]
      
#     def find(self, a: int, b: int, n: int) -> List[int]:
#         expected = a * n + b
#         if self.parent[a][b] != expected:
#             current = self.parent[a][b]
#             x = current // n
#             y = current % n
#             self.parent[a][b] = self.find(x, y, n)
#         return self.parent[a][b]
    
#     def union(self, a: int, b: int, c: int, d: int, n) -> bool:
#         root_a = self.find(a, b, n)
#         root_b = self.find(c, d, n)
#         if root_a == root_b:
#             return False
        
#         root_a_x = root_a // n
#         root_a_y = root_a % n
#         root_b_x = root_b // n
#         root_b_y = root_b % n
#         if root_a < root_b:
#             self.parent[root_a_x][root_a_y] = root_b
#         elif root_a > root_b:
#             self.parent[root_b_x][root_b_y] = root_a
#         else:
#             self.parent[root_b_x][root_b_y] = root_a
#             self.rank[root_b_x][root_b_y] += 1
#         return True

# class Solution:
#     def removeStones(self, stones: List[List[int]]) -> int:
#         n = m = 1
#         for x, y in stones:
#             m = max(m, x)
#             n = max(n, y)
            
#         n += 1
#         m += 1
#         dsu = DSU(m, n)
#         for i in range(len(stones)):
#             x, y = stones[i]
#             for j in range(i + 1, len(stones)):
#                 a, b = stones[j]
#                 if a == x or b == y:
#                     dsu.union(x, y, a, b, n)
                    
#         components = set()
#         for x, y in stones:
#             key = dsu.find(x, y, n)
#             components.add(key)
            
#         return len(stones) - len(components)

class DSU:
    def __init__(self) -> None:
        self.parent = {}
    
    def find(self, x: int) -> int:
        if x not in self.parent:
            self.parent[x] = x
            
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
            
        return self.parent[x]
    
    def union(self, x: int, y: int) -> None:
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            self.parent[root_y] = root_x
            

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        dsu = DSU()
        OFFSET = 10001
        for x, y in stones:
            dsu.union(x, y + OFFSET)
            
        components = set()
        for x, y in stones:
            components.add(dsu.find(x))
            
        return len(stones) - len(components)