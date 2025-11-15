# 2428. Maximum Sum of an Hourglass
# Medium

# You are given an m x n integer matrix grid.

# We define an hourglass as a part of the matrix with the following form:


# Return the maximum sum of the elements of an hourglass.

# Note that an hourglass cannot be rotated and must be entirely contained within the matrix.

# Example 1:


# Input: grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]
# Output: 30
# Explanation: The cells shown above represent the hourglass with the maximum sum: 6 + 2 + 1 + 2 + 9 + 2 + 8 = 30.
# Example 2:


# Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
# Output: 35
# Explanation: There is only one hourglass in the matrix, with the sum: 1 + 2 + 3 + 5 + 7 + 8 + 9 = 35.
 
# Constraints:

# m == grid.length
# n == grid[i].length
# 3 <= m, n <= 150
# 0 <= grid[i][j] <= 106

from typing import List

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        prefix_grid = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m):
            for j in range(n):
                prefix_grid[i + 1][j + 1] = grid[i][j] + prefix_grid[i + 1][j] + prefix_grid[i][j + 1] - prefix_grid[i][j]
                
        max_hourglass = 0
        for i in range(3, m + 1):
            for j in range(3, n + 1):
                grid_sum = prefix_grid[i][j] - prefix_grid[i - 3][j] - prefix_grid[i][j - 3] + prefix_grid[i - 3][j - 3]
                hourglass = grid_sum - grid[i - 2][j - 1] - grid[i - 2][j - 3]
                max_hourglass = max(max_hourglass, hourglass)
                
        return max_hourglass