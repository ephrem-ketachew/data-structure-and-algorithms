# 3286. Find a Safe Walk Through a Grid
# Medium

# You are given an m x n binary matrix grid and an integer health.

# You start on the upper-left corner (0, 0) and would like to get to the lower-right corner (m - 1, n - 1).

# You can move up, down, left, or right from one cell to another adjacent cell as long as your health remains positive.

# Cells (i, j) with grid[i][j] = 1 are considered unsafe and reduce your health by 1.

# Return true if you can reach the final cell with a health value of 1 or more, and false otherwise.

# Example 1:

# Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1

# Output: true

# Explanation:

# The final cell can be reached safely by walking along the gray cells below.

# Example 2:

# Input: grid = [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], health = 3

# Output: false

# Explanation:

# A minimum of 4 health points is needed to reach the final cell safely.

# Example 3:

# Input: grid = [[1,1,1],[1,0,1],[1,1,1]], health = 5

# Output: true

# Explanation:

# The final cell can be reached safely by walking along the gray cells below.

# Any path that does not go through the cell (1, 1) is unsafe since your health will drop to 0 when reaching the final cell.

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# 2 <= m * n
# 1 <= health <= m + n
# grid[i][j] is either 0 or 1.

from typing import List
import heapq

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        if grid[0][0] == 1:
            health -= 1
        if health == 0:
            return False
            
        m, n = len(grid), len(grid[0])
        max_heap = [(-health, 0, 0)]
        moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        grid_health = [[0] * n for _ in range(m)]
        grid_health[0][0] = health
        while max_heap:
            current_health, r, c = heapq.heappop(max_heap)
            current_health *= -1

            if r == m - 1 and c == n - 1:
                return True
            
            if current_health < grid_health[r][c]:
                continue
            
            for dr, dc in moves:
                x, y = r + dr, c + dc
                if 0 <= x < m and 0 <= y < n:
                    new_health = current_health
                    if grid[x][y] == 1:
                        new_health -= 1
                    
                    if new_health > grid_health[x][y]:
                        grid_health[x][y] = new_health
                        heapq.heappush(max_heap, (-new_health, x, y))
                        
        return False