# 1499. Max Value of Equation
# Hard

# You are given an array points containing the coordinates of points on a 2D plane, sorted by the x-values, where points[i] = [xi, yi] such that xi < xj for all 1 <= i < j <= points.length. You are also given an integer k.

# Return the maximum value of the equation yi + yj + |xi - xj| where |xi - xj| <= k and 1 <= i < j <= points.length.

# It is guaranteed that there exists at least one pair of points that satisfy the constraint |xi - xj| <= k.

# Example 1:

# Input: points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
# Output: 4
# Explanation: The first two points satisfy the condition |xi - xj| <= 1 and if we calculate the equation we get 3 + 0 + |1 - 2| = 4. Third and fourth points also satisfy the condition and give a value of 10 + -10 + |5 - 6| = 1.
# No other pairs satisfy the condition, so we return the max of 4 and 1.
# Example 2:

# Input: points = [[0,0],[3,0],[9,2]], k = 3
# Output: 3
# Explanation: Only the first two points have an absolute difference of 3 or less in the x-values, and give the value of 0 + 0 + |0 - 3| = 3.

# Constraints:

# 2 <= points.length <= 105
# points[i].length == 2
# -108 <= xi, yi <= 108
# 0 <= k <= 2 * 108
# xi < xj for all 1 <= i < j <= points.length
# xi form a strictly increasing sequence.

from typing import List
import heapq
from collections import defaultdict

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        max_heap = []
        deleted = defaultdict(int)
        
        def get_max():
            while max_heap and deleted[-max_heap[0][0]] > 0:
                num = -heapq.heappop(max_heap)[0]
                deleted[num] -= 1
                if deleted[num] == 0:
                    del deleted[num]
            return max_heap[0] if max_heap else None
            
        left = 0
        max_val = float('-inf')
        
        for right in range(len(points)):
            xr, yr = points[right]
            
            while left < right and xr - points[left][0] > k:
                xl, yl = points[left]
                deleted[yl - xl] += 1
                left += 1
                
            
            max_point = get_max()
            if max_point:
                diff_max, x_max = max_point
                y_max = x_max - diff_max
                max_val = max(max_val, y_max + yr + xr - x_max)
            
            heapq.heappush(max_heap, (xr - yr, xr))
            
        return max_val
    
# solution = Solution()
# points = [[1,3],[2,0],[5,10],[6,-10]]
# k = 1
# points = [[0,0],[3,0],[9,2]]
# k = 3
# points = [[-17,5],[-10,-8],[-5,-13],[-2,7],[8,-14]]
# k = 4
# points = [[-18,-4],[-16,-20],[-13,-1],[-7,10],[-2,-2],[-1,-5],[2,11],[5,-10],[9,0],[10,10],[12,2],[17,-5]]
# k = 6
# print(solution.findMaxValueOfEquation(points, k))