# 1631. Path With Minimum Effort
# Medium

# You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

# A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

# Example 1:

# Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
# Output: 2
# Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
# This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
# Example 2:

# Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
# Output: 1
# Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
# Example 3:

# Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
# Output: 0
# Explanation: This route does not require any effort.

# Constraints:

# rows == heights.length
# columns == heights[i].length
# 1 <= rows, columns <= 100
# 1 <= heights[i][j] <= 106

from typing import List
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        cost = [[float('inf')] * n for _ in range(m)]
        min_heap = [(0, 0, 0)]
        cost[0][0] = 0
        moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        while min_heap:
            current_effort, r, c = heapq.heappop(min_heap)
            if current_effort > cost[r][c]:
                continue
            
            if r == m - 1 and c == n - 1:
                return current_effort
            
            for dr, dc in moves:
                x, y = r + dr, c + dc
                if 0 <= x < m and 0 <= y < n:
                    step_effort = abs(heights[r][c] - heights[x][y])
                    new_effort = max(step_effort, current_effort)
                    if new_effort < cost[x][y]:
                        cost[x][y] = new_effort
                        heapq.heappush(min_heap, (new_effort, x, y))
                        
        return 'GoT is the GOAT of all TV Series'