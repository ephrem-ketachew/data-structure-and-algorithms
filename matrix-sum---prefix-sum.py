# 1314. Matrix Block Sum
# Medium

# Given a m x n matrix mat and an integer k, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for:

# i - k <= r <= i + k,
# j - k <= c <= j + k, and
# (r, c) is a valid position in the matrix.

# Example 1:

# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
# Output: [[12,21,16],[27,45,33],[24,39,28]]
# Example 2:

# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
# Output: [[45,45,45],[45,45,45],[45,45,45]]

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n, k <= 100
# 1 <= mat[i][j] <= 100

from typing import List

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = (
                    mat[i][j] +
                    prefix[i + 1][j] +
                    prefix[i][j + 1] -
                    prefix[i][j]
                )
                
        def get_sum(r1, c1, r2, c2):
            r1, c1, r2, c2 = r1 + 1, c1 + 1, r2 + 1, c2 + 1
            return prefix[r2][c2] - prefix[r2][c1 - 1] - prefix[r1 - 1][c2] + prefix[r1 - 1][c1 - 1]
                
        ans = [[0] * (n) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r1 = max(0, i - k)
                c1 = max(0, j - k)
                r2 = min(i + k, m - 1)
                c2 = min(j + k, n - 1)
                
                ans[i][j] = get_sum(r1, c1, r2, c2)
                
        return ans