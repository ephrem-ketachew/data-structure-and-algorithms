# 934. Shortest Bridge
# Medium

# You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

# An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

# You may change 0's to 1's to connect the two islands to form one island.

# Return the smallest number of 0's you must flip to connect the two islands.

# Example 1:

# Input: grid = [[0,1],[1,0]]
# Output: 1
# Example 2:

# Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
# Output: 2
# Example 3:

# Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Output: 1
 
# Constraints:

# n == grid.length == grid[i].length
# 2 <= n <= 100
# grid[i][j] is either 0 or 1.
# There are exactly two islands in grid.

from typing import List
from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()
        seen = set()
        def cover_islnad(r: int, c: int) -> None:
            if r == -1 or r == m or c == -1 or c == n or grid[r][c] != 1:
                return
            
            queue.append((r, c, -1))
            seen.add((r, c))
            grid[r][c] = 2
            
            for dr, dc in moves:
                x, y = r + dr, c + dc
                cover_islnad(x, y)
            
        one_covered = False
        for i in range(m):
            if one_covered:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    cover_islnad(i, j)
                    one_covered = True
                    break

        while queue:
            r, c, s = queue.popleft()
            if grid[r][c] == 1:
                return s
            
            for dr, dc in moves:
                x, y = r + dr, c + dc
                if (0 <= x < m) and (0 <= y < n) and (x, y) not in seen:
                    queue.append((x, y, s + 1))
                    seen.add((x, y))