# 3239. Minimum Number of Flips to Make Binary Grid Palindromic I
# Medium
# You are given an m x n binary matrix grid.

# A row or column is considered palindromic if its values read the same forward and backward.

# You can flip any number of cells in grid from 0 to 1, or from 1 to 0.

# Return the minimum number of cells that need to be flipped to make either all rows palindromic or all columns palindromic.

# Example 1:

# Input: grid = [[1,0,0],[0,0,0],[0,0,1]]

# Output: 2

# Explanation:

# Flipping the highlighted cells makes all the rows palindromic.

# Example 2:

# Input: grid = [[0,1],[0,1],[0,0]]

# Output: 1

# Explanation:



# Flipping the highlighted cell makes all the columns palindromic.

# Example 3:

# Input: grid = [[1],[0]]

# Output: 0

# Explanation:

# All rows are already palindromic.

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m * n <= 2 * 105
# 0 <= grid[i][j] <= 1

from typing import List

class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        row_flips = 0
        for i in range(len(grid)):
            left, right = 0, len(grid[0]) - 1
            while left < right:
                if grid[i][left] != grid[i][right]:
                    row_flips += 1
                left += 1
                right -= 1
              
        col_flips = 0  
        for i in range(len(grid[0])):
            bot, top = 0, len(grid) - 1
            while bot < top:
                if grid[bot][i] != grid[top][i]:
                    col_flips += 1
                bot += 1
                top -= 1
            
        return min(row_flips, col_flips)
                