# 3212. Count Submatrices With Equal Frequency of X and Y
# Medium

# Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.', return the number of submatrices that contain:

# grid[0][0]
# an equal frequency of 'X' and 'Y'.
# at least one 'X'.

# Example 1:

# Input: grid = [["X","Y","."],["Y",".","."]]

# Output: 3

# Explanation:

# Example 2:

# Input: grid = [["X","X"],["X","Y"]]

# Output: 0

# Explanation:

# No submatrix has an equal frequency of 'X' and 'Y'.

# Example 3:

# Input: grid = [[".","."],[".","."]]

# Output: 0

# Explanation:

# No submatrix has at least one 'X'.

# Constraints:

# 1 <= grid.length, grid[i].length <= 1000
# grid[i][j] is either 'X', 'Y', or '.'.

from typing import List

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        prefix = [[[0, 0] for _ in range(n + 1)] for _ in range(m + 1)]
        
        count = 0        
        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1][0] = prefix[i][j + 1][0] + prefix[i + 1][j][0] - prefix[i][j][0]
                prefix[i + 1][j + 1][1] = prefix[i][j + 1][1] + prefix[i + 1][j][1] - prefix[i][j][1]
                
                if grid[i][j] == 'X':
                    prefix[i + 1][j + 1][0] += 1
                elif grid[i][j] == 'Y':
                    prefix[i + 1][j + 1][1] += 1
                    
                if prefix[i + 1][j + 1][0] == prefix[i + 1][j + 1][1] > 0:
                    count += 1

        return count