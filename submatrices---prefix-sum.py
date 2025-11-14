# 2536. Increment Submatrices by One
# Medium

# You are given a positive integer n, indicating that we initially have an n x n 0-indexed integer matrix mat filled with zeroes.

# You are also given a 2D integer array query. For each query[i] = [row1i, col1i, row2i, col2i], you should do the following operation:

# Add 1 to every element in the submatrix with the top left corner (row1i, col1i) and the bottom right corner (row2i, col2i). That is, add 1 to mat[x][y] for all row1i <= x <= row2i and col1i <= y <= col2i.
# Return the matrix mat after performing every query. 

# Example 1:


# Input: n = 3, queries = [[1,1,2,2],[0,0,1,1]]
# Output: [[1,1,0],[1,2,1],[0,1,1]]
# Explanation: The diagram above shows the initial matrix, the matrix after the first query, and the matrix after the second query.
# - In the first query, we add 1 to every element in the submatrix with the top left corner (1, 1) and bottom right corner (2, 2).
# - In the second query, we add 1 to every element in the submatrix with the top left corner (0, 0) and bottom right corner (1, 1).
# Example 2:


# Input: n = 2, queries = [[0,0,1,1]]
# Output: [[1,1],[1,1]]
# Explanation: The diagram above shows the initial matrix and the matrix after the first query.
# - In the first query we add 1 to every element in the matrix.

# Constraints:

# 1 <= n <= 500
# 1 <= queries.length <= 104
# 0 <= row1i <= row2i < n
# 0 <= col1i <= col2i < n

from typing import List

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # prefix_grid = [[0] * (n + 1) for _ in range(n)]
        # for row1, col1, row2, col2 in queries:
        #     for i in range(row1, row2 + 1):
        #         prefix_grid[i][col1] += 1
        #         prefix_grid[i][col2 + 1] -= 1
                
        # for i in range(n):
        #     for j in range(1, n + 1):
        #         prefix_grid[i][j] = prefix_grid[i][j] + prefix_grid[i][j - 1]
        #     prefix_grid[i].pop()
            
        # return prefix_grid
    
        diff = [[0] * (n + 1) for _ in range(n + 1)]
        for row1, col1, row2, col2 in queries:
            diff[row1][col1] += 1
            diff[row1][col2 + 1] -= 1
            diff[row2 + 1][col1] -= 1
            diff[row2 + 1][col2 + 1] += 1
            
        for i in range(n):
            for j in range(n):
                diff[i][j] += (
                    (diff[i - 1][j] if i > 0 else 0) + 
                    (diff[i][j - 1] if j > 0 else 0) -
                    (diff[i - 1][j - 1] if i > 0 and j > 0 else 0)
                )
            
            
        return [row[:n] for row in diff[:n]]