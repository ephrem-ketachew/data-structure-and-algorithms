# 1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a m x n matrix mat and an integer threshold, return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.
 

# Example 1:


# Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
# Output: 2
# Explanation: The maximum side length of square with sum less than 4 is 2 as shown.
# Example 2:

# Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
# Output: 0
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 300
# 0 <= mat[i][j] <= 104
# 0 <= threshold <= 105

from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m , n = len(mat), len(mat[0])
        
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = mat[i][j] + prefix[i + 1][j] + prefix[i][j + 1] - prefix[i][j]
                
        def can_find(k: int):
            for i in range(k, m + 1):
                for j in range(k, n + 1):
                    if prefix[i][j] - prefix[i - k][j] - prefix[i][j - k] + prefix[i - k][j - k] <= threshold:
                        return True
                    
            return False
        
        left, right, ans = 0, min(m, n), 0
        while left <= right:
            mid = (left + right) // 2
            if can_find(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return ans