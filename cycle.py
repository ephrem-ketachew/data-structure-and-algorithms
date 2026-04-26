# 1559. Detect Cycles in 2D Grid
# Medium

# Given a 2D array of characters grid of size m x n, you need to find if there exists any cycle consisting of the same value in grid.

# A cycle is a path of length 4 or more in the grid that starts and ends at the same cell. From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the same value of the current cell.

# Also, you cannot move to the cell that you visited in your last move. For example, the cycle (1, 1) -> (1, 2) -> (1, 1) is invalid because from (1, 2) we visited (1, 1) which was the last visited cell.

# Return true if any cycle of the same value exists in grid, otherwise, return false.

# Example 1:

# Input: grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
# Output: true
# Explanation: There are two valid cycles shown in different colors in the image below:

# Example 2:

# Input: grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
# Output: true
# Explanation: There is only one valid cycle highlighted in the image below:

# Example 3:

# Input: grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
# Output: false

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 500
# grid consists only of lowercase English letters.

from typing import List

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        def dfs(r: int, c: int, target: int, prev: tuple[int], seen_char: str) -> bool:
            grid[r][c] = seen_char
            moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            contains_cycle = False
            for dr, dc in moves:
                x, y = r + dr, c + dc
                if 0 <= x < m and 0 <= y < n:
                    if grid[x][y] == target:
                        contains_cycle = contains_cycle or dfs(x, y, target, (r, c), seen_char)
                    elif (x, y) != prev and grid[x][y] == seen_char:
                        return True
                    
                if contains_cycle:
                    return True
                
            return contains_cycle
        
        seen_tracker = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j].islower():
                    if dfs(i, j, grid[i][j], (-1, -1), str(seen_tracker)):
                        return True
                    seen_tracker += 1
                    
        return False