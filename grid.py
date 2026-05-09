# 1914. Cyclically Rotating a Grid
# Medium

# You are given an m x n integer matrix grid​​​, where m and n are both even integers, and an integer k.

# The matrix is composed of several layers, which is shown in the below image, where each color is its own layer:

# A cyclic rotation of the matrix is done by cyclically rotating each layer in the matrix. To cyclically rotate a layer once, each element in the layer will take the place of the adjacent element in the counter-clockwise direction. An example rotation is shown below:

# Return the matrix after applying k cyclic rotations to it.

# Example 1:

# Input: grid = [[40,10],[30,20]], k = 1
# Output: [[10,20],[40,30]]
# Explanation: The figures above represent the grid at every state.
# Example 2:

# Input: grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
# Output: [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
# Explanation: The figures above represent the grid at every state.

# Constraints:

# m == grid.length
# n == grid[i].length
# 2 <= m, n <= 50
# Both m and n are even integers.
# 1 <= grid[i][j] <= 5000
# 1 <= k <= 109

from typing import List

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        layers = min(m // 2, n // 2)
        left = top = 0
        right, bot = n - 1, m - 1
        for _ in range(layers):
            arr = []
            for i in range(top, bot + 1):
                arr.append(grid[i][left])
            
            for i in range(left + 1, right):
                arr.append(grid[bot][i])
                
            for i in range(bot, top - 1, -1):
                arr.append(grid[i][right])
                
            for i in range(right - 1, left, -1):
                arr.append(grid[top][i])
                
            idx = len(arr) - (k % len(arr))
            arr = arr[idx:] + arr[:idx]
            j = 0
            for i in range(top, bot + 1):
                grid[i][left] = arr[j]
                j += 1
                
            for i in range(left + 1, right):
                grid[bot][i] = arr[j]
                j += 1
                
            for i in range(bot, top - 1, -1):
                grid[i][right] = arr[j]
                j += 1
                
            for i in range(right - 1, left, -1):
                grid[top][i] = arr[j]
                j += 1
                
            left += 1
            right -= 1
            top += 1
            bot -= 1
        
        return grid