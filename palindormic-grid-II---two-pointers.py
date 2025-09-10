# 3240. Minimum Number of Flips to Make Binary Grid Palindromic II
# Medium
# You are given an m x n binary matrix grid.

# A row or column is considered palindromic if its values read the same forward and backward.

# You can flip any number of cells in grid from 0 to 1, or from 1 to 0.

# Return the minimum number of cells that need to be flipped to make all rows and columns palindromic, and the total number of 1's in grid divisible by 4. 

# Example 1:

# Input: grid = [[1,0,0],[0,1,0],[0,0,1]]

# Output: 3

# Explanation:

# Example 2:

# Input: grid = [[0,1],[0,1],[0,0]]

# Output: 2

# Explanation:



# Example 3:

# Input: grid = [[1],[1]]

# Output: 2

# Explanation:
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m * n <= 2 * 105
# 0 <= grid[i][j] <= 1

from typing import List

class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        flips = 0
        m, n =  len(grid), len(grid[0])
        for j in range(n // 2):
            for i in range(m // 2):
                ones = grid[i][j] + grid[m - 1 - i][j] + grid[i][n - 1 - j] + grid[m - 1 - i][n - 1 - j]
                zeros = 4 - ones
                flips += min(ones, zeros)
          
        pairs = []      
        if m % 2:
            for j in range(n // 2):
                pairs.append((grid[m // 2][j], grid[m // 2][n - 1 - j]))
                
        if n % 2:
            for i in range(m // 2):
                pairs.append((grid[i][n // 2], grid[m - 1 - i][n // 2]))
                
        if n % 2 and m % 2 and grid[m // 2][n // 2]:
            flips += 1
            
        min_swith = 2
        k = 0
        for pair in pairs:
            ones = pair[0] + pair[1]
            cost_to_make_zero = ones
            cost_to_make_one = 2 - cost_to_make_zero
            
            if cost_to_make_one <= cost_to_make_zero:
                k += 1
                
            flips += min(cost_to_make_one, cost_to_make_zero)
            min_swith = min(min_swith, abs(cost_to_make_zero - cost_to_make_one))
           
        if k % 2:
            flips += min_swith
            
        return flips
                