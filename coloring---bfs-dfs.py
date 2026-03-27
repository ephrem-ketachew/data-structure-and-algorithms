# 1034. Coloring A Border
# Medium

# You are given an m x n integer matrix grid, and three integers row, col, and color. Each value in the grid represents the color of the grid square at that location.

# Two squares are called adjacent if they are next to each other in any of the 4 directions.

# Two squares belong to the same connected component if they have the same color and they are adjacent.

# The border of a connected component is all the squares in the connected component that are either adjacent to (at least) a square not in the component, or on the boundary of the grid (the first or last row or column).

# You should color the border of the connected component that contains the square grid[row][col] with color.

# Return the final grid.

# Example 1:

# Input: grid = [[1,1],[1,2]], row = 0, col = 0, color = 3
# Output: [[3,3],[3,2]]
# Example 2:

# Input: grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3
# Output: [[1,3,3],[2,3,3]]
# Example 3:

# Input: grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2
# Output: [[2,2,2],[2,1,2],[2,2,2]]

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# 1 <= grid[i][j], color <= 1000
# 0 <= row < m
# 0 <= col < n

from typing import List
from collections import deque

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        original_color = grid[row][col]
        if original_color == color:
            return grid
        
        m, n = len(grid), len(grid[0])
        
        i, j = row, col
        queue = deque([(i, j)])
        borders = set()
        visited = set()
        while queue:
            i, j = queue.popleft()
            if not(0 <= i < m and 0 <= j < n):
                continue
            
            if (i, j) in visited:
                continue
            
            if grid[i][j] != original_color:
                continue
            
            if i == 0 or grid[i - 1][j] != original_color:
                borders.add((i, j))
                
            if i + 1 == m or grid[i + 1][j] != original_color:
                borders.add((i, j))
                
            if j == 0 or grid[i][j - 1] != original_color:
                borders.add((i, j))
                
            if j + 1 == n or grid[i][j + 1] != original_color:
                borders.add((i, j))
                
                
            queue.append((i - 1, j))
            queue.append((i + 1, j))
            queue.append((i, j - 1))
            queue.append((i, j + 1))
            
            visited.add((i, j))
            
            
        for i, j in borders:
            grid[i][j] = color
            
        return grid