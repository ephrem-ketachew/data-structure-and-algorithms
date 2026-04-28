# 2033. Minimum Operations to Make a Uni-Value Grid
# Medium

# You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.

# A uni-value grid is a grid where all the elements of it are equal.

# Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.

# Example 1:

# Input: grid = [[2,4],[6,8]], x = 2
# Output: 4
# Explanation: We can make every element equal to 4 by doing the following: 
# - Add x to 2 once.
# - Subtract x from 6 once.
# - Subtract x from 8 twice.
# A total of 4 operations were used.
# Example 2:

# Input: grid = [[1,5],[2,3]], x = 1
# Output: 5
# Explanation: We can make every element equal to 3.
# Example 3:

# Input: grid = [[1,2],[3,4]], x = 2
# Output: -1
# Explanation: It is impossible to make every element equal.

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 105
# 1 <= m * n <= 105
# 1 <= x, grid[i][j] <= 104

from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = sorted([num for row in grid for num in row])
        n = len(nums)
        mid_left, mid_right = nums[n // 2 - 1], nums[n // 2]
        ops_left = 0
        for num in nums:
            if abs(num - mid_left) % x != 0:
                ops_left = -1
                break
            
            ops_left += abs(num - mid_left) // x
            
        ops_right = 0
        for num in nums:
            if abs(num - mid_right) % x != 0:
                ops_right = -1
                break
            
            ops_right += abs(num - mid_right) // x
            
        if ops_left == -1:
            return ops_right
        
        if ops_right == -1:
            return ops_left
        
        return min(ops_left, ops_right)