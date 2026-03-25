# 3546. Equal Sum Grid Partition I
# Medium

# You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:

# Each of the two resulting sections formed by the cut is non-empty.
# The sum of the elements in both sections is equal.
# Return true if such a partition exists; otherwise return false.

# Example 1:

# Input: grid = [[1,4],[2,3]]

# Output: true

# Explanation:


# A horizontal cut between row 0 and row 1 results in two non-empty sections, each with a sum of 5. Thus, the answer is true.

# Example 2:

# Input: grid = [[1,3],[2,4]]

# Output: false

# Explanation:

# No horizontal or vertical cut results in two non-empty sections with equal sums. Thus, the answer is false.

# Constraints:

# 1 <= m == grid.length <= 105
# 1 <= n == grid[i].length <= 105
# 2 <= m * n <= 105
# 1 <= grid[i][j] <= 105

from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = grid[i][j] + prefix[i + 1][j] + prefix[i][j + 1] - prefix[i][j]
                
        grid_sum = prefix[-1][-1]
        for j in range(1, n):
            cur_sum = prefix[-1][j]
            if cur_sum == grid_sum - cur_sum:
                return True
            
        for i in range(1, m):
            cur_sum = prefix[i][-1]
            if cur_sum == grid_sum - cur_sum:
                return True
            
            
        return False