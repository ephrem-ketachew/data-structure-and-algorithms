# 542. 01 Matrix
# Medium

# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

# The distance between two cells sharing a common edge is 1.

# Example 1:


# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
# Example 2:


# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.
 

# Note: This question is the same as 1765: https://leetcode.com/problems/map-of-highest-peak/

from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        ans = [[float('inf')] * n for _ in range(m)]
        queue = deque()
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    queue.append((r, c))
                    ans[r][c] = 0
        
        moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]   
        distance = 0      
        while queue:
            distance += 1
            length = len(queue)
            for _ in range(length):
                r, c = queue.popleft()
                for dr, dc in moves:
                    x, y = r + dr, c + dc
                    if 0 <= x < m and 0 <= y < n and ans[x][y] == float('inf'):
                        ans[x][y] = distance
                        queue.append((x, y))
                        
        return ans