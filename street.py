# 1391. Check if There is a Valid Path in a Grid
# Medium

# You are given an m x n grid. Each cell of grid represents a street. The street of grid[i][j] can be:

# 1 which means a street connecting the left cell and the right cell.
# 2 which means a street connecting the upper cell and the lower cell.
# 3 which means a street connecting the left cell and the lower cell.
# 4 which means a street connecting the right cell and the lower cell.
# 5 which means a street connecting the left cell and the upper cell.
# 6 which means a street connecting the right cell and the upper cell.

# You will initially start at the street of the upper-left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1). The path should only follow the streets.

# Notice that you are not allowed to change any street.

# Return true if there is a valid path in the grid or false otherwise.

# Example 1:

# Input: grid = [[2,4,3],[6,5,2]]
# Output: true
# Explanation: As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).
# Example 2:

# Input: grid = [[1,2,1],[1,2,1]]
# Output: false
# Explanation: As shown you the street at cell (0, 0) is not connected with any street of any other cell and you will get stuck at cell (0, 0)
# Example 3:

# Input: grid = [[1,1,2]]
# Output: false
# Explanation: You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).
 
# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# 1 <= grid[i][j] <= 6

from typing import List
from collections import deque

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        if m == n == 1:
            return True
        
        nxt_right = {1: [1, 3, 5], 2: [], 3: [], 4: [1, 3, 5], 5: [], 6: [1, 3, 5]}
        nxt_left = {1: [1, 4, 6], 2: [], 3: [1, 4, 6], 4: [], 5: [1, 4, 6], 6: []}
        nxt_up = {1: [], 2: [2, 3, 4], 3: [], 4: [], 5: [2, 3, 4], 6: [2, 3, 4]}
        nxt_down = {1: [], 2: [2, 5, 6], 3: [2, 5, 6], 4: [2, 5, 6], 5: [], 6: []}
        
        queue = deque([(0, 0, grid[0][0])])
        grid[0][0] = -1
        moves = [(0, -1, nxt_left), (0, 1, nxt_right), (-1, 0, nxt_up), (1, 0, nxt_down)]
        while queue:
            r, c, street = queue.popleft()           
            for dr, dc, nxt in moves:
                x, y = r + dr, c + dc
                if 0 <= x < m and 0 <= y < n and grid[x][y] in nxt[street]:
                    if (x, y) == (m - 1, n - 1):
                        return True
                    
                    queue.append((x, y, grid[x][y]))
                    grid[x][y] = -1
                    
        return False