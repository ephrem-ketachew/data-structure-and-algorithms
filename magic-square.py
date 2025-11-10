# 1895. Largest Magic Square
# Medium

# A k x k magic square is a k x k grid filled with integers such that every row sum, every column sum, and both diagonal sums are all equal. The integers in the magic square do not have to be distinct. Every 1 x 1 grid is trivially a magic square.

# Given an m x n integer grid, return the size (i.e., the side length k) of the largest magic square that can be found within this grid.

# Example 1:


# Input: grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
# Output: 3
# Explanation: The largest magic square has a size of 3.
# Every row sum, column sum, and diagonal sum of this magic square is equal to 12.
# - Row sums: 5+1+6 = 5+4+3 = 2+7+3 = 12
# - Column sums: 5+5+2 = 1+4+7 = 6+3+3 = 12
# - Diagonal sums: 5+4+3 = 6+4+2 = 12
# Example 2:


# Input: grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
# Output: 2
 
# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# 1 <= grid[i][j] <= 106

from typing import List

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        # I CAN DO THIS YEAH I GOT THIS
        # 10 : 31 AM
        
        m, n = len(grid), len(grid[0])
        row_prefix = [[0] * (n + 1) for _ in range(m)]
        for r in range(m):
            for c in range(n):
                row_prefix[r][c + 1] = row_prefix[r][c] + grid[r][c]
                
        col_prefix = [[0] * n for _ in range(m + 1)]
        for c in range(n):
            for r in range(m):
                col_prefix[r + 1][c] = col_prefix[r][c] + grid[r][c]
                
        def is_magic(r, c, k):
            lr_diag = rl_diag = 0
            for i in range(k):
                lr_diag += grid[r + i][c + i]
                rl_diag += grid[r + i][c + k - 1 - i]
                
            if lr_diag != rl_diag:
                return False
            
            target_sum = lr_diag
            
            for i in range(k):
                row_sum = row_prefix[r + i][c + k] - row_prefix[r + i][c]
                if row_sum != target_sum:
                    return False
                
            for i in range(k):
                col_sum = col_prefix[r + k][c + i] - col_prefix[r][c + i]
                if col_sum != target_sum:
                    return False
                
            return True
        
        
        for k in range(min(m, n), 0, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    if is_magic(r, c, k):
                        return k
                    
        return 1
    
    # 11:04 AM
            