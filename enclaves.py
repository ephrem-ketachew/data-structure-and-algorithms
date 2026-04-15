# 1020. Number of Enclaves
# Medium

# You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

# A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

# Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

# Example 1:

# Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# Output: 3
# Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
# Example 2:

# Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# Output: 0
# Explanation: All 1s are either on the boundary or can reach the boundary.

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 500
# grid[i][j] is either 0 or 1.

from typing import List
from collections import deque

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        for i in range(m):
            if grid[i][0] == 1:
                grid[i][0] = 2
                queue.append((i, 0))
            if grid[i][n - 1] == 1:
                grid[i][n - 1] = 2
                queue.append((i, n - 1))
                
        for j in range(n):
            if grid[0][j] == 1:
                grid[0][j] = 2
                queue.append((0, j))
            if grid[m - 1][j] == 1:
                grid[m - 1][j] = 2
                queue.append((m - 1, j))
         
        moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]       
        while queue:
            r, c = queue.popleft()
            for dr, dc in moves:
                x, y = r + dr, c + dc
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    grid[x][y] = 2
                    queue.append((x, y))

        return sum(row.count(1) for row in grid)