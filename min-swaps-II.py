# 1536. Minimum Swaps to Arrange a Binary Grid
# Medium

# Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.

# A grid is said to be valid if all the cells above the main diagonal are zeros.

# Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.

# The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends at cell (n, n).

# Example 1:

# Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
# Output: 3
# Example 2:


# Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
# Output: -1
# Explanation: All rows are similar, swaps have no effect on the grid.
# Example 3:


# Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
# Output: 0
 

# Constraints:

# n == grid.length == grid[i].length
# 1 <= n <= 200
# grid[i][j] is either 0 or 1

from typing import List

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        arr = []
        for row in grid:
            i = n - 1
            cnt = 0
            while i >= 0 and row[i] == 0:
                cnt += 1
                i -= 1
            arr.append(cnt)
         
        sorted_arr = sorted(arr)
        for i, num in enumerate(sorted_arr):
            if num < i:
                return -1
           
        count_swaps = 0
        for i in range(n - 1):
            need = n - 1 - i
            if arr[i] < need:
                j = i + 1
                while arr[j] < need:
                    j += 1
                    
                count_swaps += j - i
                key = arr[j]
                while j > i:
                    arr[j] = arr[j - 1]
                    j -= 1
                    
                arr[j] = key
                
        return count_swaps
    
# s = Solution()
# grid = [[0,0,1],[1,1,0],[1,0,0]]
# grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
# grid = [[1,0,0],[1,1,0],[1,1,1]]
# grid = [[1,0,0,0,0,0],[0,1,0,1,0,0],[1,0,0,0,0,0],[1,1,1,0,0,0],[1,1,0,1,0,0],[1,0,0,0,0,0]]
# print(s.minSwaps(grid))