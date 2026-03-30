# 200. Number of Islands
# Medium

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        def sink_island(r: int, c: int) -> None:
            if (r < 0 or r == m) or (c < 0 or c == n ) or grid[r][c] == '0':
                return
            
            grid[r][c] = '0'
            
            sink_island(r - 1, c)
            sink_island(r + 1, c)
            sink_island(r, c - 1)
            sink_island(r, c + 1)
            
        count_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    sink_island(i, j)
                    count_islands += 1
                    
        return count_islands